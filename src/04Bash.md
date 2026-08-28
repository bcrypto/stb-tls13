# Bash Algorithms {#BASH}

## Preliminaries {#BASH.Prelim}

This specification defines the following algorithms of the Bash family:

* `bash-f` -- the base sponge function;
* `bash256`, `bash384`, `bash512` -- hashing;
* `bash-prg-ae2561` -- authenticated encryption.

The `bash-f` algorithm implements a 1536-bit sponge function, that is, a
permutation on the set `{0, 1}^1536`. The sponge function is the basic
primitive for all other Bash algorithms. These algorithms use `bash-f` either
directly or through an abstraction layer called a sponge automaton. The
automaton processes a 1536-bit sponge state using a prescribed set of commands
on top of `bash-f`. The design of `bash-f` is explained in {{AMMS17}}.

The `bashLLL` algorithm, `LLL in {256, 384, 512}`, implements `LLL`-bit
hashing.

The `bash-prg-ae2561` algorithms (encryption and decryption) implement AEAD
with 256-bit authentication tags and up to 480-bit preambles. Preambles may
contain customization strings, public data to be authenticated, nonces and
other non-secret objects.

## The Sponge Function {#BASH.F}

The sponge function `bash-f` is defined through an auxiliary algorithm
`bash-s`.

### The `bash-s` Algorithm

Input:

* `W_0, W_1, W_2 in {0, 1}^64`;
* `m_1, n_1, m_2, n_2 in {1, 2, ..., 63}`.

Output:

* `(W_0, W_1, W_2)` -- the transformed input strings.

Steps:

1. `T_0 <- RotHi(W_0, m_1)`.
2. `W_0 <- W_0 ^ W_1 ^ W_2`.
3. `T_1 <- W_1 ^ RotHi(W_0, n_1)`.
4. `W_1 <- T_0 ^ T_1`.
5. `W_2 <- W_2 ^ RotHi(W_2, m_2) ^ RotHi(T_1, n_2)`.
6. `T_0 <- ~W_2`.
7. `T_1 <- W_0 | W_2`.
8. `T_2 <- W_0 & W_1`.
9. `T_0 <- T_0 | W_1`.
10. `W_1 <- W_1 ^ T_1`.
11. `W_2 <- W_2 ^ T_2`.
12. `W_0 <- W_0 ^ T_0`.
13. Return `(W_0, W_1, W_2)`.

### The `bash-f` Algorithm

Input:

* `S in {0, 1}^1536` -- a state.

Output:

* `S in {0, 1}^1536` -- the transformed state.

Steps:

1. Parse `(S_0, S_1, ..., S_23) = Split(S, 64)`.
2. `C <- Bin2Int(BeltH(0, 8))`.
3. For `i = 1, 2, ..., 24`:
   1. `(m_1, n_1, m_2, n_2) <- (8, 53, 14, 1)`.
   2. for `j = 0, 1, ..., 7`:
      1. `(S_j, S_{8+j}, S_{16+j}) <-`
         `bash-s(S_j, S_{8+j}, S_{16+j}, m_1, n_1, m_2, n_2)`.
      2. `m_1 <- (7 * m_1) mod 64`, `n_1 <- (7 * n_1) mod 64`.
         `m_2 <- (7 * m_2) mod 64`, `n_2 <- (7 * n_2) mod 64`.
   3. `(S_0,  S_1,  S_2,  S_3,  S_4,  S_5,  S_6,  S_7,`
      `S_8,  S_9,  S_10, S_11, S_12, S_13, S_14, S_15,`
      `S_16, S_17, S_18, S_19, S_20, S_21, S_22, S_23)`
      `<-`
      `(S_15, S_10, S_9,  S_12, S_11, S_14, S_13, S_8,`
      `S_17, S_16, S_19, S_18, S_21, S_20, S_23, S_22,`
      `S_6,  S_3,  S_0,  S_5,  S_2,  S_7,  S_4,  S_1)`.
   4. `S_23 <- S_23 ^ C`.
   5. if `C mod 2 = 0`, then `C <- ShLo(C, 1)`
      else `C <- ShLo(C, 1) ^ 0xAED8E07F99E12BDC`.
4. Return `S_0 || S_1 || ... || S_23`.

## The Sponge Automaton {#BASH.Auto}

For reasons of completeness, we describe the full functionality of the Bash
automaton. Note that `bash-prg-ae2561` uses only a part of this functionality.

### States and Parameters

An automaton processes a state `S in {0, 1}^1536` using the following
parameters:

* `l in {128, 192, 256}` -- security level;
* `d in {1, 2}` -- capacity level;
* `r in {1536 - 2dl, 1536 - l - dl/2}` -- buffer length;
* `pos in {0, 1, ..., r - 1}` -- current buffer offset.

Parameters `l` and `d` are set when the automaton is initialized and do not
change thereafter.

The state `S` is split into two parts:

1. The buffer `S[:r)` used for input and output.
2. The internal memory `S[r:)`. The bit `S[r]` of the memory has a special
   purpose: the internal command `commit` inverts it to signal the completion
   of the previous command.

### Commands

The state is processed using the following commands:

* `start`: initialize;
* `commit`: complete execution of the previous command (internal command, can
   only be called from other commands);
* `restart`: re-initialize;
* `absorb`: process input data;
* `squeeze`: extract output data;
* `encrypt` / `decrypt`: process plaintext / ciphertext;
* `ratchet`: update the state irreversibly.

The processed data are encoded as follows:

| Type   | Description             | Code (6 bits) |
|--------|-------------------------|---------------|
| `NULL` | Service data            | `000000`      |
| `KEY`  | Key                     | `000001`      |
| `DATA` | Public input data       | `000010`      |
| `TEXT` | Plaintext or ciphertext | `000011`      |
| `OUT`  | Output data             | `000100`      |
{: #DTYPES title="Data Types in Bash Automaton"}

#### The `start` Command

Input:

* `A in {0, 1}^{32*}` -- a preamble (`|A| <= 480`);
* `K in {0, 1}^{32*}` -- a key (`|K| <= 480`; if `K != NIL`, then `|K| >= l`).

Output:

* None.

Steps:

1. If `K != NIL`, then `r <- 1536 - l - dl/2`
   else `r <- 1536 - 2dl`.
2. `pos <- 8 + |A| + |K|`.
3. `S[:pos) <- Int2Bin(|A|/2 + |K|/32, 8) || A || K`.
4. `S[pos:1472) <- Rep(0, 256 - |X_n|)`.
5. `S[1472:) <- Int2Bin(l/4 + d, 64)`.
6. Store parameters `(l, d, r, pos)` with state `S`.

#### The `commit` Command

Input:

* `t in {0, 1}^6` -- data type (see the table above).

Output:

* None.

Steps:

1. `S[pos:pos+8) <- S[pos:pos+8) ^ (t || 01)`.
2. `S[r] <- S[r] ^ 1`.
3. `S <- bash-f(S)`.
4. `pos <- 0`.

#### The `restart` Command

Input:

* `A in {0, 1}^{32*}` -- a preamble (`|A| <= 480`);
* `K in {0, 1}^{32*}` -- a key (`|K| <= 480`; if `K != NIL`, then `|K| >= l`).

Output:

* None.

Steps:

1. If `K != NIL`, then:
   1. `commit(KEY)`;
   2. `r <- 1536 - l - dl/2`.
2. Else `commit(NULL)`.
3. `pos <- 8 + |A| + |K|`.
4. `S[:pos) <- S[:pos) ^ (Int2Bin(|A|/2 + |K|/32, 8) || A || K)`.

#### The `absorb` Command

Input:

* `X in {0, 1}^{8*}` -- input data.

Output:

* None.

Steps:

1. `commit(DATA)`.
2. Parse `(X_1, ..., X_n) = Split(X, r)`.
3. For `i = 1, 2, ..., n`:
   1. `pos <- |X_i|`;
   2. `S[:pos) <- S[:pos) ^ X_i`.
   3. if `pos = r`, then:
      1. `S <- bash-f(S)`;
      2. `pos <- 0`.

#### The `squeeze` Command

Input:

* `n >= 0` -- output length (multiple of `8`).

Output:

* `Y in {0, 1}^n`.

Steps:

1. `commit(OUT)`.
2. `Y <- NIL`.
3. While `|Y| + r <= n`:
   1. `Y <- Y || S[:r)`;
   2. `S <- bash-f(S)`.
4. `pos <- n - |Y|`.
5. `Y <- Y || S[:pos)`.
6. Return `Y`.

#### The `encrypt` Command

Input:

* `X in {0, 1}^{8*}` -- plaintext.

Output:

* `Y in {0, 1}^|X|` -- ciphertext.

Steps:

1. `commit(TEXT)`.
2. Parse `(X_1, ..., X_n) = Split(X, r)`.
3. `Y <- NIL`.
4. For `i = 1, 2, ..., n`:
   1. `pos <- |X_i|`;
   2. `S[:pos) <- S[:pos) ^ X_i`;
   3. `Y <- Y || S[:pos)`;
   4. if `pos = r`, then:
      1. `S <- bash-f(S)`;
      2. `pos <- 0`.
5. Return `Y`.

#### The `decrypt` Command

Input:

* `Y in {0, 1}^{8*}` -- ciphertext.

Output:

* `X in {0, 1}^|Y|` -- plaintext.

Steps:

1. `commit(TEXT)`.
2. Parse `(Y_1, ..., Y_n) = Split(Y, r)`.
3. `X <- NIL`.
4. For `i = 1, 2, ..., n`:
   1. `pos <- |Y_i|`;
   2. `X <- X || (S[:pos) ^ Y_i)`;
   3. `S[:pos) <- Y_i`;
   4. if `pos = r`, then:
      1. `S <- bash-f(S)`;
      2. `pos <- 0`.
5. Return `X`.

#### The `ratchet` Command

Input:

* None.

Output:

* None.

Steps:

1. `T <- S`.
2. `commit(NULL)`.
3. `S <- S ^ T`.

## Hashing {#BASH.Hash}

Hashing is defined by the `bash-hash` algorithm that depends on the security
level `l in {128, 192, 256}`. The algorithms `bashLLL` are instances of
`bash-hash` at different security levels: `bashLLL = bash-hash[l]`, `LLL = 2l`.

### The `bash-hash` Algorithm

Parameters:

* `l in {128, 192, 256}` -- security level.

Input:

* `X in {0, 1}^*` -- data to be hashed.

Output:

* `H in {0, 1}^{2l}` -- the hash value.

Steps:

1. Parse `(X_1, X_2, ..., X_n) = Split(X || 01, 1536 - 4l)`.
2. `X_n <- X_n || Rep(0, 1536 - 4l - |X_n|)`.
3. `S <- Rep(0, 1472) || Int2Bin(l/4, {64}`.
4. For `i = 1, 2, ..., n`:
   1. `S[:1536-4l) <- X_i`;
   2. `S <- bash-f(S)`.
5. `H <- S[:2l)`.
6. Return `H`.

## Authenticated Encryption {#BASH.AE}

Authenticated encryption is defined by the encryption algorithm
`bash-prg-ae2561` and the decryption algorithm `bash-prg-ae2561-inv`. Both
algorithms use an automaton denoted as `alpha`.

### The `bash-prg-ae2561` Algorithm

Input:

* `A in {0, 1}^{32*}` -- a preamble (`|A| <= 480`);
* `X in {0, 1}^{8*}` -- plaintext;
* `I in {0, 1}^{8*}` -- associated data;
* `K in {0, 1}^{32*}` -- a key (`256 <= |K| <= 480`).

Output:

* `Y in {0, 1}^|X|` -- the ciphertext;
* `T in {0, 1}^256` -- the authentication tag.

Steps:

1. `alpha.start[256, 1](A, K)`.
2. Process `(X, I)`:
   1. `alpha.absorb(I)`;
   2. `Y <- alpha.encrypt(X)`;
   3. `T <- alpha.squeeze(l)`.
3. Return `(Y, T)`.

{:aside}
> Notes:
>
> * If `I = NIL`, step 2.1 may be skipped. If `X = NIL`, step 2.2 can be
>   simplified to `Y <- NIL`. Skipped or simplified steps must be mirrored in
>   the decryption algorithm.
> * After returning `(Y, T)`, the automaton may be used to process new `(X, I)`
>   pairs by repeating step 2. Before processing a new pair,
>   `alpha.restart(A, K)` may be called to update the preamble and/or the key.
> * After processing `(X, I)`, `alpha.ratchet(NIL)` may be called to ensure
>   forward secrecy of `X` even after the state of `alpha` has been compromised.

### The `bash-prg-ae2561-inv` Algorithm

Input:

* `A in {0, 1}^{32*}` -- a preamble (`|A| <= 480`);
* `Y in {0, 1}^{8*}` -- ciphertext;
* `I in {0, 1}^{8*}` -- associated data;
* `T in {0, 1}^256` -- an authentication tag;
* `K in {0, 1}^{32*}` -- a key (`256 <= |K| <= 480`).

Output:

* `NIL` -- an authentication error, or `X in {0, 1}^|Y|` -- the decrypted
  data.

Steps:

1. `alpha.start[256, 1](A, K)`.
2. Process `(Y, I, T)`:
   1. `alpha.absorb(I)`;
   2. `X <- alpha.decrypt(Y)`;
   3. if `T != alpha.squeeze(l)`, then return `NIL`.
3. Return `X`.

{:aside}
> Notes:
>
> * During decryption, the variable `X` stores the tentative plaintext until the
>   authentication tag is verified to be correct (step 2.3). If verification
>   fails, `X` must be securely erased.
> * Extensions of the encryption algorithm described in the notes above are
>   mirrored in the decryption algorithm, with one exception: after `NIL` is
>   returned, processing of new triples `(Y, I, T)` must be stopped.
