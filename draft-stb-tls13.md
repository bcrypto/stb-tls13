---
title: "STB Cryptographic Parameters for Transport Layer Security (TLS)
  Protocol Version 1.3"
abbrev: stb-tls13
docname: draft-stb-tls13-latest
submissiontype: independent
category: info
v: 3
lang: en
ipr: trust200902
stand_alone: yes
smart_quotes: yes
pi: [toc, sortrefs, symrefs]

author:
 -
    name: Sergey Agievich
    ins: S. Agievich
    organization: APMI, Belarusian State University
    email: agievichi@bsu.by
 -
    name: Nikolai Kalosha
    ins: N. Kalosha
    organization: IM, Academy of Sciences of Belarus
    email: kalosha@im.bas-net.by

contributor:
  -
    name: Nastassia Kozlovskaya
    ins: N. Kozlovskaya
    organization: APMI, Belarusian State University

normative:

  RFC5280:
  RFC9846:

informative:

  AgiAfo05:
    title: "Exponential S-boxes"
    target: https://eprint.iacr.org/2004/024
    date: 2005
    seriesinfo:
      Vesti NAN Belarusi: "2005(1), pp. 106-112"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University
      -
        ins: A. Afonenko
        name: Andrey Afonenko
        org: Belarusian State University

  Agi20:
    title: "The Counter mode with encrypted nonces and its extension to AE"
    target: https://eprint.iacr.org/2020/331
    date: 2020
    seriesinfo:
      Mat. Vopr. Kriptogr.: "11(2), pp. 7-24"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University

  Agi26:
    title: "On the security of belt-hash and belt-compress"
    date: 2026-06
    rc: "Pre-proceedings of the 15th Workshop on Current Trends in Cryptology
      (CTCrypt'2026), pp. 445-470"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University

  AMMS17:
    title: "Bash-f: another LRX sponge function"
    target: https://eprint.iacr.org/2016/587
    date: 2017
    seriesinfo:
      Mat. Vopr. Kriptogr.: "8(2), pp. 7-28"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University
      -
        ins: V. Marchuk
        name: Vadim Marchuk
        org: Belarusian State University
      -
        ins: A. Maslau
        name: Alexander Maslau
        org: Belarusian State University
      -
        ins: V. Semenov
        name: Vladislav Semenov
        org: Belarusian State University

  BloLee19:
    title: "On the Multi-user Security of Short Schnorr Signatures with
      Preprocessing"
    target: https://eprint.iacr.org/2019/1105
    date: 2019
    rc: "Proceedings of EUROCRYPT 2022, pp. 614-643"
    author:
      -
        ins: J. Blocki
        name: Jeremiah Blocki
      -
        ins: S. Lee
        name: Seunghoon Lee

  Che10:
    title: "Discrete Logarithm Problems with Auxiliary Inputs"
    date: 2010
    seriesinfo:
      J. Cryptology: "vol. 23, pp. 457-476"
    author:
      -
        ins: J.H. Cheon
        name: Jung Hee Cheon

  HMV04:
    title: "Guide to Elliptic Curve Cryptography"
    date: 2004
    rc: "New York: Springer"
    author:
      -
        ins: D. Hankerson
        name: Darrel Hankerson
      -
        ins: A. Menezes
        name: Alfred Menezes
      -
        ins: S. Vanstone
        name: Scott Vanstone

  LidNie97:
    title: "Finite Fields"
    date: 1997
    rc: "Cambridge University Press"
    author:
      -
        ins: R. Lidl
        name: Rudolf Lidl
      -
        ins: H. Niederreiter
        name: Harald Niederreiter

  McGVie04:
    title: "The security and performance of the Galois/Counter Mode (GCM)
      of operation"
    target: https://eprint.iacr.org/2004/193
    date: 2004
    rc: INDOCRYPT 2004
    author:
      -
        ins: D.A. McGrew
        name: David McGrew
      -
        ins: J. Viega
        name: John Viega

  Sch91:
    title: "Efficient Signature Generation by Smart Cards"
    date: 1991
    seriesinfo:
      J. Cryptology: "4(3), pp. 161-174"
    author:
      -
        ins: C.P. Schnorr
        name: Claus P. Schnorr

  Stb31:
    title: "STB 34.101.31-2020. Information technology and security. Encryption
      and integrity control algorithms"
    date: 2020
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

  Stb45:
    title: "STB 34.101.45-2013. Information technology and security. Digital
      signature and key transport algorithms based on elliptic curves"
    date: 2013
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

  Stb77:
    title: "STB 34.101.77-2020. Information technology and security.
      Sponge-bases cryptographic algorithms"
    date: 2020
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

  Stb90:
    title: "STB 34.101.90-2026. Information technology and security. The
      Transport Layer Security Protocol Version 1.3"
    date: 2026
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

--- abstract

This specification introduces a subset of STB (STandards of Belarus)
cryptographic algorithms and defines their use in TLS 1.3. The document is
self-contained, i.e., it fully describes the required STB algorithms. It can be
used to develop STB-compliant TLS 1.3 implementations without referring to
the original STB standards.

--- middle

# Introduction {#INTRO}

In the TLS 1.3 protocol {{RFC9846}}, the client and server negotiate the
following cryptographic parameters:

1. Hashing and AEAD (Authenticated Encryption with Associated Data) algorithms,
   which together define a cipher suite. TLS parties specify their preferred
   cipher suites in the handshake hello messages.
2. KEM (Key Encapsulation Mechanism) algorithms, which are defined implicitly
   through algebraic group identifiers in the `"supported_groups"` and
   `"key_share"` extensions of hello messages. By default, KEM is implemented
   through the Diffie-Hellman protocol and cyclic groups for this protocol are
   assumed.
3. Digital signature algorithms, which are negotiated through the
   `"signature_algorithms"` and `"signature_algorithms_cert"` extensions.

Based on these parameters, the TLS algorithmic stack is constructed, covering
key exchange, bulk encryption, message authentication and authentication of
parties. Changing the parameters modifies the stack without redesigning its
structure.

This specification introduces a subset of cryptographic algorithms standardized
in Belarus and defines their use as TLS 1.3 cryptographic parameters. These
algorithms are deployed across Belarusian IT systems, powering public key
infrastructures, legally recognized digital signatures, identity cards, VPN
services, etc. The specification aims to improve the recognition of the
algorithms, in particular, to obtain assigned code points for the respective
TLS parameters. This would ensure interoperability and facilitate
interactions with external systems.

National standards of Belarus are designated by the abbreviation STB.
The relevant standards have additionally been assigned short names:

* Belt ({{Stb31}}, introduced in 2007): block cipher-based symmetric
  encryption, data authentication, hashing;
* Bash ({{Stb77}}, introduced in 2016): sponge function-based symmetric
  encryption, data authentication, hashing;
* Bign ({{Stb45}}, introduced in 2011): elliptic curve-based digital signatures
  and key transport.

These short names are also used to refer to the elements of the standards.

This document presents a restricted profile of the STB suite, defining only a
subset of the available algorithms and narrowing their operational parameters.
The sole exception to this restriction is {{BASH.Auto}}, where the complete
functionality of the auxiliary sponge automaton is specified.

# Notation {#NOTATION}

## General

`NIL` :
: empty input, error;

`!=` :
: not equal;

`a^b`, `a^{b}` :
: `b` is the upper index of `a`;

`a_b`, `a_{b}` :
: `b` is the lower index of `a`;

`a b`, `a * b` :
: multiplication;

`{a, b, c, ...}` :
: the set of elements `a, b, c, ...`;

`a in S` :
: `a` belongs to `S`;

`alg(u_1, u_2, ...)` :
: call an algorithm `alg` with inputs `u_1, u_2, ...`;

`a <- u` :
: assign `u` to `a`;

`a <- S` :
: for a set `S`, the same as `a <- u`, where `u` is chosen uniformly at
  random from `S`;

`(a_1, a_2, ...) <- (u_1, u_2, ...)` :
: the same as `a_1 <- u_1`, `a_2 <- u_2, ...`;

`(NIL, a_2) <- (u_1, u_2)` :
: the same as `a_2 <- u_2` (`u_1` is ignored);

`a <-> b` :
: swap the values of `a` and `b`.

## Binary Strings and Integers

`{0, 1}^*` :
: the set of all binary strings of finite length
  (including the empty string of length `0`);

`|u|` :
: the bit length of `u in {0, 1}^*`;

`{0, 1}^n` :
: the set of `u in {0, 1}^*` such that `|u| = n`;

`{0, 1}^{n*}` :
: the set of `u in {0, 1}^*` such that `|u|` is a multiple of `n`;

`u[i]` :
: for `u in {0, 1}^*` and `0 <= i < |u|`, the `i`th bit of `u`
  (bits are numbered from zero);

`u[:m)` :
: for `u in {0, 1}^n` and `0 <= m <= n`, the string `u[0]u[1]...u[m-1]`;

`u[m:)` :
: for `u in {0, 1}^n` and `0 <= m <= n`, the string `u[m]u[m+1]...u[n-1]`;

`u[-m:)` :
: for `u in {0, 1}^n` and `0 <= m <= n`, the string `u[n-m]...u[n-1]`;

`u[m_1:m_2)` :
: for `u in {0, 1}^n` and `0 <= m_1 <= m_2 <= n`, the string
  `u[m_1]u[m_1+1]...u[m_2-1]`;

`u || v` :
: for `u, v in {0, 1}^*`, their concatenation, that is, the string `w`
  of length `|u| + |v|` such that `w[:|u|) = u` and `w[-|v|:) = v`;

`Rep(u, m)` :
: for `u in {0, 1}^*` and a positive integer `m`, the concatenation
  of `m` copies of `u`;

`Split(u, m)` :
: for `u in {0, 1}^*` and a positive integer `m`, the tuple:

  - `()` if `|u| = 0`;
  - `(u)` if `0 < |u| <= m`;
  - `(u[:m), Split(u[m:), m))` if `|u| > m`;

`U mod m` :
: for an integer `U` and a positive integer `m`, the integer
  `r in {0, 1, ..., m-1}` such that `U - r` is a multiple of `m`;

`u & v` :
: for `u, v in {0, 1}^n`, the string `w in {0, 1}^n` such that
  `w[i] = u[i] * v[i]` (bitwise AND);

`u | v` :
: for `u, v in {0, 1}^n`, the string `w in {0, 1}^n` such that
  `w[i] = (u[i] * v[i] + u[i] + v[i]) mod 2` (bitwise OR);

`u ^ v` :
: for `u, v in {0, 1}^n`, the string `w in {0, 1}^n` such that
  `w[i] = (u[i] + v[i]) mod 2` (bitwise exclusive OR);

`~u` :
: for `u in {0, 1}^n`, the string `u ^ Rep(1, n)` (bitwise NOT);

`Bin2Int(u)` :
: for `u in {0, 1}^{8*}`, the number:

  - `0`, if `|u| = 0`;
  - `128 u[0] + 64 u[1] + ... + u[7]`, if `|u| = 8`;
  - `Bin2Int(u[:8)) + 256 * Bin2Int(u[8:))`, if `|u| > 8`
    (binary-to-integer conversion);

`Int2Bin(U, 8n)` :
: for a non-negative integer `U` and a positive integer `n`,
  the string `u in {0, 1}^{8n}` such that `Bin2Int(u) = U mod 2^{8n}`
  (integer-to-binary conversion);

`u + v` :
: for `u, v in {0, 1}^{8n}`, the string
  `Int2Bin(Bin2Int(u) + Bin2Int(v), 8n)`;

`u - v` :
: for `u, v in {0, 1}^{8n}`, the string `w in {0, 1}^{8n}` such that
  `u = w + v`;

`Floor(z)` :
: for a real number `z`, the greatest integer less than or equal to `z`;

`ShLo(u, r)` :
: for `u in {0, 1}^{8n}` and a positive integer `r < 8n`,
  the string `Int2Bin(Floor(Bin2Int(u) / 2^r), 8n)`;

`ShHi(u, r)` :
: for `u in {0, 1}^{8n}` and a positive integer `r < 8n`, the string
  `Int2Bin(2^r * Bin2Int(u), 8n)`;

`RotHi(u, r)` :
: for `u in {0, 1}^{8n}` and a positive integer `r < 8n`, the string
  `ShHi(u, r) ^ ShLo(u, 8n - r)`.

## Miscellaneous

`--` :
: dash;

`\` :
: no line break; used to split large sequences of digits into lines for
  convenience;

`0x` :
: prefix followed by a hexadecimal representation of `u in {0, 1}^{4*}`:

  - every four consecutive bits of `u` are represented by a hexadecimal
    digit in `{0, 1, ..., 9, A, B, C, D, E, F}` (e.g., `10110001 = 0xB1`);

`OID(obj)` :
: an identifier of an object `obj`, a string in `{0, 1}^{8*}`.

## Conventions

for `i = 1, 2, ..., m` :

  - the body of the loop is executed `m` times if `m > 1`;
  - the body of the loop is executed once if `m = 1`;
  - the body of the loop is never executed if `m < 1`;

`(a_1, a_2, ..., a_m)`:

  - a tuple of `m` elements if `m > 1`;
  - a tuple of one element `a_1` if `m = 1`;
  - an empty tuple if `m < 1`.

`u[m_1]u[m_1+1]...u[m_2-1]`:

  - a string of `m_2 - m_1` elements if `m_2 > m_1`;
  - an empty tuple if `m_2 <= m_1`.

# Belt Algorithms {#BELT}

## Preliminaries {#BELT.Prelim}

This specification defines the following algorithms of the Belt family:

* `belt-block` -- block encryption;
* `belt-hash` -- hashing;
* `belt-che256` -- authenticated encryption.

The `belt-block` algorithms (encryption and decryption) define a block cipher
that processes 128-bit blocks using 256-bit keys. This cipher is the basic
primitive, all other Belt algorithms are built on top of it.

The `belt-hash` algorithm implements 256-bit hashing. When processing two
128-bit blocks of data, `belt-block` is invoked 3 times, i.e., the hash rate is
approximately 2/3 of the encryption rate.

The `belt-che256` algorithms (encryption and decryption) implement AEAD in the
CHE (Counter-Hash-Encrypt) mode {{Agi20}}. This mode is similar to the
well-known GCM mode {{McGVie04}}, but it is more robust with respect to nonce
misuse. The nonce length is 128 bits, and the authentication tag length is 64
bits.

## Block Encryption {#BELT.Block}

Block encryption is defined by the encryption algorithm `belt-block` and the
corresponding decryption algorithm. This specification describes only
encryption. The `belt-block` algorithm uses auxiliary transformations `G_5`,
`G_13`, `G_21` which, in turn, use an S-box `H`.

### S-box `H`

The S-box `H` transforms `x in {0, 1}^8` as follows.

1. Parse `(x_1, x_2) = Split(x, 4)`.
2. Find the octet `y` in row `x_1` and column `x_2` of {{SBOX}}
   (all data in the table are in the hexadecimal notation).
3. Return `y`.

|  |0  |1  |2  |3  |4  |5  |6  |7  |8  |9  |A  |B  |C  |D  |E  |F  |
|--|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0 |B1 |94 |BA |C8 |0A |08 |F5 |3B |36 |6D |00 |8E |58 |4A |5D |E4 |
|1 |85 |04 |FA |9D |1B |B6 |C7 |AC |25 |2E |72 |C2 |02 |FD |CE |0D |
|2 |5B |E3 |D6 |12 |17 |B9 |61 |81 |FE |67 |86 |AD |71 |6B |89 |0B |
|3 |5C |B0 |C0 |FF |33 |C3 |56 |B8 |35 |C4 |05 |AE |D8 |E0 |7F |99 |
|4 |E1 |2B |DC |1A |E2 |82 |57 |EC |70 |3F |CC |F0 |95 |EE |8D |F1 |
|5 |C1 |AB |76 |38 |9F |E6 |78 |CA |F7 |C6 |F8 |60 |D5 |BB |9C |4F |
|6 |F3 |3C |65 |7B |63 |7C |30 |6A |DD |4E |A7 |79 |9E |B2 |3D |31 |
|7 |3E |98 |B5 |6E |27 |D3 |BC |CF |59 |1E |18 |1F |4C |5A |B7 |93 |
|8 |E9 |DE |E7 |2C |8F |0C |0F |A6 |2D |DB |49 |F4 |6F |73 |96 |47 |
|9 |06 |07 |53 |16 |ED |24 |7A |37 |39 |CB |A3 |83 |03 |A9 |8B |F6 |
|A |92 |BD |9B |1C |E5 |D1 |41 |01 |54 |45 |FB |C9 |5E |4D |0E |F2 |
|B |68 |20 |80 |AA |22 |7D |64 |2F |26 |87 |F9 |34 |90 |40 |55 |11 |
|C |BE |32 |97 |13 |43 |FC |9A |48 |A0 |2A |88 |5F |19 |4B |09 |A1 |
|D |7E |CD |A4 |D0 |15 |44 |AF |8C |A5 |84 |50 |BF |66 |D2 |E8 |8A |
|E |A2 |D7 |46 |52 |42 |A8 |DF |B3 |69 |74 |C5 |51 |EB |23 |29 |21 |
|F |D4 |EF |D9 |B4 |3A |62 |28 |75 |91 |14 |10 |EA |77 |6C |DA |1D |
{: #SBOX title="The S-box `H`"}

The S-box defines a family of constants `BeltH`. The family is parameterized by
integers `u >= 0` and `n > 0` such that `u + n <= 256`. A particular
constant `BeltH(u, n)` is defined as
`H(Int2Bin(u, 8)) || H(Int2Bin(u + 1, 8)) || ... || H(Int2Bin(u + n - 1, 8))`.
For example, `BeltH(79, 3) = 0xF1C1AB` (`Int2Bin(79, 8) = 0x4F`).

{:aside}
> Note: `H` is constructed using exponentiation in a finite field of size `2^8`
> {{AgiAfo05}}. The array `H[0], H[1], ..., H[255]`, where
> `H[x] = H(Int2Bin(x, 8))`, is generated by the following algorithm:
>
> 1. `H[10] <- 0x00`, `H[11] <- 0x8E`.
> 2. For `x = 12, 13, ..., 9 + 256`:
>    1. `t <- H[(x - 1) mod 256]`;
>    2. for `i = 0, 1, ..., 115`:
>       1. `t <- Clock(t)`;
>    3. `H[x] <- t`.
> 3. Return `H`.
>
> Here `Clock(t) = (t_2 ^ t_3 ^ t_7 ^ t_8) t_1 t_2 ... t_7` for
> `t = t_1 t_2 ... t_8 in {0, 1}^8`.

### The Transformations `G_r`

The transformations `G_5`, `G_13`, `G_21` map the set `{0, 1}^32` to itself.
They are derived from an algorithm `G` by taking `G_r(x) = G(x, r)`.

The algorithm `G` is defined as follows.

Input:

* `x in {0, 1}^32`;
* `r in {5, 13, 21}`.

Output:

* `y in {0, 1}^32`.

Steps:

1. Parse `(x_1, x_2, x_3, x_4) = Split(x, 8)`.
2. `y <- RotHi(H(x_1) || H(x_2) || H(x_3) || H(x_4), r)`.
3. Return `y`.

### The `belt-block` Algorithm

Input:

* `X in {0, 1}^128` -- a plaintext block;
* `K in {0, 1}^256` -- a key.

Output:

* `Y in {0, 1}^128` -- the encrypted block.

Steps:

1. `(a, b, c, d) <- Split(X, 32)`.
2. `(k[1], k[2], ..., k[56]) <- Split(Rep(K, 7), 32)`.
3. For `i = 1, 2, ..., 8`:
   1.  `b <- b ^ G_5(a + k[7i-6])`;
   2.  `c <- c ^ G_21(d + k[7i-5])`;
   3.  `a <- a - G_13(b + k[7i-4])`;
   4.  `e <- G_21(b + c + k[7i-3]) ^ Int2Bin(i, 32)`;
   5.  `b <- b + e`;
   6.  `c <- c - e`;
   7.  `d <- d + G_13(c + k[7i-2])`;
   8.  `b <- b ^ G_21(a + k[7i-1])`;
   9.  `c <- c ^ G_5(d + k[7i])`;
   10. `a <-> b`;
   11. `c <-> d`;
   12. `b <-> c`.
4. `Y <- b || d || a || c`.
5. Return `Y`.

## Hashing {#BELT.Hash}

Hashing is defined by the `belt-hash` algorithm
which uses the auxiliary algorithm `belt-compress`.

### The `belt-compress` Algorithm

Input:

* `X in {0, 1}^512`.

Output:

* `S in {0, 1}^128`;
* `Y in {0, 1}^256`.

Steps:

1. Parse `(X_1, X_2, X_3, X_4) = Split(X, 128)`.
2. `S <- belt-block(X_3 ^ X_4, X_1 || X_2) ^ X_3 ^ X_4`.
3. `Y_1 <- belt-block(X_1, S || X_4) ^ X_1`.
4. `Y_2 <- belt-block(X_2, (S ^ Rep(1, 128)) || X_3) ^ X_2`.
5. Return `(S, Y)`, where `Y = Y_1 || Y_2`.

### The `belt-hash` Algorithm

Input:

* `X in {0, 1}^*` -- data to be hashed.

Output:

* `H in {0, 1}^256` -- the hash value.

Steps:

1. Parse `(X_1, X_2, ..., X_n) = Split(X, 256)`.
2. `r <- Int2Bin(|X|, 128)`.
3. `s <- Rep(0, 128)`.
4. `h <- BeltH(0, 32)`.
5. `X_n <- X_n || Rep(0, 256 - |X_n|)`.
6. For `i = 1, 2, ..., n`:
   1. `(t, h) <- belt-compress(X_i || h)`;
   2. `s <- s ^ t`.
7. `(NIL, H) <- belt-compress(r || s || h)`.
8. Return `H`.

{:aside}
> Note: if `X == NIL`, then `n == 0` and the steps 5 and 6 are not performed.

## Authenticated Encryption {#BELT.AE}

Authenticated encryption is defined by the encryption algorithm `belt-che256`
and the decryption algorithm `belt-che256-inv`.

128-bit blocks are interpreted as polynomials of degree less than 128 over the
binary field `{0, 1}`. The polynomials are added and multiplied modulo a fixed
irreducible polynomial of degree 128. Thus, operations on polynomials are
performed in a finite field (Galois field, see {{LidNie97}}) of size `2^128`.

The transition from blocks to polynomials and the field multiplication are
defined as follows.

`u(x)`:
: for `u in {0, 1}^{8*}`, the polynomial:

 - `0`, if `|u| = 0`;
 - `u[0] x^7 + u[1] x^6 + ... + u[7]`, if `|u| = 8`;
 - `u[:8)(x) + x^8 u[8:)(x)`, if `|u| > 8`;

 `u(x) mod f(x)`:
: for a polynomial `u(x)` and a nonzero polynomial `f(x)`,
  the remainder of the division of `u(x)` by `f(x)`;

 `u * v`:
: for `u, v in {0, 1}^128`, the string `w in {0, 1}^128` such
  that `w(x) = u(x) v(x) mod f(x)`, where `f(x) = x^128 + x^7 + x^2 + x + 1`.

The algorithms use a constant `C in {0, 1}^128` defined as
`C = 0x02 || Rep(0, 120)`. Its polynomial representation is `C(x) = x`.

### The `belt-che256` Algorithm

Input:

* `X in {0, 1}^*` -- plaintext, `|X| < 2^64`;
* `I in {0, 1}^*` -- associated data, `|I| < 2^64`;
* `K in {0, 1}^256` -- a key;
* `S in {0, 1}^128` -- a nonce.

Output:

* `Y in {0, 1}^{|X|}` -- ciphertext;
* `T in {0, 1}^64` -- the authentication tag.

Steps:

1. `(X_1, X_2, ..., X_n) <- Split(X, 128)`.
2. `(I_1, I_2, ..., I_m) <- Split(I, 128)`.
3. Set:
   1. `s <- belt-block(S, K)`;
   2. `r <- s`;
   3. `t <- BeltH(0, 16)`.
4. For `i = 1, 2, ..., m`:
   1. `t <- t ^ (I_i || Rep(0, 128 - |I_i|))`;
   2. `t <- t * r`.
5. For `i = 1, 2, ..., n`:
   1. `s <- (s * C) ^ Int2Bin(1, 128)`;
   2. `Y_i <- X_i ^ belt-block(s, K)[:|X_i|)`;
   3. `t <- t ^ (Y_i || Rep(0, 128 - |Y_i|))`;
   4. `t <- t * r`.
6. `t <- t ^ (Int2Bin(|I|, 64) || Int2Bin(|X|, 64))`.
7. `t <- belt-block(t * r, K)`.
8. `T <- t[:64)`.
9. Return `(Y, T)`, where `Y = Y_1 || Y_2 || ... || Y_n`.

### The `belt-che256-inv` Algorithm

Input:

* `Y in {0, 1}^*` -- ciphertext, `|Y| < 2^64`;
* `I in {0, 1}^*` -- associated data, `|I| < 2^64`;
* `T in {0, 1}^64` -- an authentication tag;
* `K in {0, 1}^256` -- a key;
* `S in {0, 1}^128` -- a nonce.

Output:

* `NIL` -- an authentication error, or `X in {0, 1}^|Y|` -- plaintext.

Steps:

1.  Parse `(Y_1, Y_2, ..., Y_n) = Split(Y, 128)`.
2.  Parse `(I_1, I_2, ..., I_m) = Split(I, 128)`.
3.  Set:
    1. `s <- belt-block(S, K)`;
    2. `r <- s`;
    3. `t <- BeltH(0, 16)`.
4.  For `i = 1, 2, ..., m`:
    1. `t <- t ^ (I_i || Rep(0, 128 - |I_i|))`;
    2. `t <- t * r`.
5.  For `i = 1, 2, ..., n`:
    1. `t <- t ^ (Y_i || Rep(0, 128 - |Y_i|))`;
    2. `t <- t * r`.
6.  `t <- t ^ (Int2Bin(|I|, 64) || Int2Bin(|Y|, 64))`.
7.  `t <- belt-block(t * r, K)`.
8.  If `T != t[:64)`, then return `NIL`.
9.  For `i = 1, 2, ..., n`:
    1. `s <- (s * C) ^ Int2Bin(1, 128)`;
    2. `X_i <- Y_i ^ belt-block(s, K)[:|Y_i|)`.
10. Return `X = X_1 || X_2 || ... || X_n`.

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

# Bign Algorithms {#BIGN}

## Preliminaries {#BIGN.Prelim}

This specification defines the following algorithms of the Bign family:

* `bign-genkeypair` -- key pair generation;
* `bign-valpubkey` -- public key validation;
* `bign-sign` -- signature generation;
* `bign-vfy` -- signature verification.

The first two algorithms implement key management, and the last two instantiate
the short Schnorr signature scheme {{Sch91}} over elliptic curves. Algorithms
operate at three security levels: `l = 128`, `l = 192` and `l = 256`. At level
`l`, the private key, public key and signature consist of `l/4`, `l/2` and
`3l/8` octets, respectively. The elliptic curves used in Bign satisfy the
requirements denoted as `bign-curves` (see {{BIGN.Curves}}). Three curves
recommended by {{Stb45}} are defined in {{CURVES}}.

## The `bign-curves` Elliptic Curves {#BIGN.Curves}

Bign algorithms use elliptic curves of the short Weierstrass form over
prime finite fields. A curve is described by the following parameters:

* `p`: a prime that defines the field `FF_p`. Elements of `FF_p` are integers
  of the set `{0, 1, ..., p-1}`, added and multiplied modulo `p`;
* `a, b in FF_p`: coefficients of the equation `E_{a,b}: y^2 = x^3 + a * x + b`
  defining the curve and the set `E_{a,b}(FF_p)` of its `FF_p`-rational
  points. The set `E_{a,b}(FF_p)` consists of pairs `(x, y)`, `x, y in FF_p`,
  satisfying `E_{a,b}` (affine points) and the point at infinity `O`.

Points of `E_{a,b}(FF_p)` are added via the chord-and-tangent rule {{HMV04}},
turning `E_{a,b}(FF_p)` into an Abelian group with zero element `O`.

Elliptic curve parameters also describe an affine point
`G in E_{a,b}(FF_p)` with a zero `x`-coordinate:

* `y_G in FF_p`: `y`-coordinate of `G`;
* `q`: the order of `G` in the group `E_{a,b}(FF_p)`.

The point `G` generates a group `GG_q` of order `q`. It consists of points `G`,
`2 G = G + G`, `3 G = 2 G + G`, ..., `(q-1) G` and `q G = O`. In Bign, `GG_q`
always coincides with the entire group `E_{a,b}(FF_p)`.

The parameters `(p, a, b, y_G, q)` are passed to all Bign algorithms. The
parameters must satisfy general constraints to ensure a well-defined elliptic
curve group, alongside additional requirements for security and efficiency.

The full list of requirements, called `bign-curves`, is as follows.

1.  At security level `l in {128, 192, 256}`: `2^{2l-1} < p, q < 2^{2l}`.
2.  `p` and `q` are primes.
3.  `p != q`.
4.  `p mod 4 = 3`.
5.  `p^m mod q != 1` for `m = 1, 2, ..., 50`.
6.  `0 < a, b < p`.
7.  `b = Bin2Int(belt-hash(t || seed) || belt-hash(t || seed1)) mod p`, where:
    * `t = Int2Bin(p, 2l) || Int2Bin(a, 2l)`;
    * `seed in {0, 1}^64` is an initialization parameter for the curve
      generation algorithm;
    * `seed1 = Int2Bin(Bin2Int(seed) + 1, 64)`.
8.  `b^{(p-1)/2} mod p = 1`, i.e., `b` is a quadratic residue modulo `p`.
9.  `(4 a^3 + 27 b^2) mod p != 0`.
10. `G = (0, y_G)`, where `y_G = b^{(p+1)/4} mod p`.
11. `q G = O`.

Let `GG_q^*` be the set of affine (nonzero) points of `GG_q`. Points of
`GG_q^*` are encoded as follows.

`Point2Bin(P, m)`:
: for `P = (x, y) in GG_q^*` and positive integer `m <= 4l`, the string
  `(Int2Bin(x, 2l) || Int2Bin(y, 2l))[:m)`.

## Key Management

Algorithms of the Bign family use private keys `d in {1, 2, ..., q-1}` and
public keys `Q in GG_q^*`. The `bign-genkeypair` algorithm generates a key pair
`(d, Q)`, the `bign-valpubkey` algorithm validates `Q`.

If necessary, keys are encoded as binary strings `Int2Bin(d, 2l)` and
`Point2Bin(Q, 4l)`.

### The `bign-genkeypair` Algorithm

Parameters:

* `(p, a, b, q, y_G)` -- elliptic curve parameters that describe the group
  `GG_q` and its generator `G`.

Input:

* None.

Output:

* `d in {1, 2, ..., q-1}` -- a private key;
* `Q in GG_q^*` -- the corresponding public key.

Steps:

1. `d <- {1, 2, ..., q-1}`.
2. `Q <- d G`.
3. Return `(d, Q)`.

### The `bign-valpubkey` Algorithm

Parameters:

* `(p, a, b, q, y_G)` -- elliptic curve parameters.

Input:

* `Q = (x_Q, y_Q)` -- a public key.

Output:

* `1` if `Q` is valid, and `0` otherwise.

Steps:

1. If either condition:
   * `0 <= x_Q, y_Q < p`;
   * `y_Q^2 mod p = (x_Q^3 + a * x_Q + b) mod p`;

   is violated, then return `0`.
2. Return `1`.

## Digital Signatures

Digital signature algorithms are `bign-sign` and `bign-vfy`.
The `bign-sign` algorithm signs messages using a private key `d`,
and `bign-vfy` verifies signatures using the corresponding public key `Q`.

A message `X` to be signed is preprocessed by a hash algorithm `h` that produces
`2l`-bit hash value `H = h(X)`. To distinguish between different hash
algorithms, `H` is used along with a string `OID(h)` that uniquely identifies
`h`. This is the DER encoding of the ASN.1 object identifier for `h`.

During the signing process, an ephemeral key pair is generated. This can be
done either in probabilistic mode, using `bign-genkeypair`, or in deterministic
mode, by using `H` and `d`.

The deterministic mode of `bign-sign` is implemented using the auxiliary
`bign-genk` algorithm.

### The `bign-genk` Algorithm

Parameters:

* `(p, a, b, y_G, q)` -- elliptic curve parameters;
* `OID(h)` -- an identifier of a hash algorithm `h`.

Input:

* `d in {1, 2, ..., q-1}` -- a private key;
* `H in {0, 1}^{2l}` -- a hash value.

Output:

* `k in {1, 2, ..., q-1}` -- an ephemeral private key.

Steps:

1. Pick an arbitrary `t in {0, 1}^*` (`t` can be the empty string).
2. `K <- belt-hash(OID(h) || Int2Bin(d, 2l) || t)`.
3. `r <- H`.
4. Parse `(r_1, r_2, ..., r_n) = Split(r, 128)`.
5. For `i = 1, 2, ...`:
   1. if `n = 2`, then:
      1. `s <- r_1`;
   2. if `n = 3`, then:
      1. `s <- r_1 ^ r_2`;
      2. `r_1 <- r_2`;
   3. if `n = 4`, then:
      1. `s <- r_1 ^ r_2 ^ r_3`;
      2. `r_1 <- r_2`;
      3. `r_2 <- r_3`;
   4. `r_{n-1} <- belt-block(s, K) ^ r_n ^ Int2Bin(i, 128)`;
   5. `r_n <- s`;
   6. `r <- r_1 || r_2 || ... || r_n`;
   7. if `i mod 2n = 0` and `Bin2Int(r) in {1, 2, ..., q-1}`, break.
6. `k <- Bin2Int(r)`.
7. Return `k`.

### The `bign-sign` Algorithm

Parameters:

* `(p, a, b, y_G, q)` -- elliptic curve parameters that describe the security
  level `l`, the group `GG_q` and its generator `G`;
* `h` -- a hash algorithm with the identifier `OID(h)`.

Input:

* `X in {0, 1}^*` -- a message to be signed;
* `d in {1, 2, ..., q-1}` -- a private key.

Output:

* `S in {0, 1}^{3l}` -- the signature.

Steps:

1. `H <- h(X)`.
2. If the signing mode is probabilistic, then:
   1. `(k, R) <- bign-genkeypair()`.
3. Else, if the signing mode is deterministic, then:
   1. `k <- bign-genk(d, H)`;
   2. `R <- k G`.
4. `S_0 <- belt-hash(OID(h) || Point2Bin(R, 2l) || H)[:l)`.
5. `S_1 <- Int2Bin((k - Bin2Int(H) - (Bin2Int(S_0) + 2^l)d)) mod q, 2l)`.
6. `S <- S_0 || S_1`.
7. Return `S`.

### The `bign-vfy` Algorithm

Parameters:

* `(p, a, b, y_G, q)` -- elliptic curve parameters that describe the security
  level `l`, the group `GG_q` and its generator `G`;
* `h` -- a hash algorithm with the identifier `OID(h)`.

Input:

* `X in {0, 1}^*` -- a signed message;
* `S in {0, 1}^*` -- a signature;
* `Q in GG_q^*` -- a public key.

Output:

* `1`, if the signature is valid, and `0` otherwise.

Steps:

1. If `|S| != 3l`, then return `0`.
2. Parse `S = S_0 || S_1`, where `|S_0| = l` and `|S_1| = 2l`.
3. If `Bin2Int(S_1) >= q`, then return `0`.
4. `H <- h(X)`.
5. `R <- ((Bin2Int(S_1) + Bin2Int(H)) mod q)G + (Bin2Int(S_0) + 2^l)Q`.
6. If `R = O`, then return `0`.
7. `t <- belt-hash(OID(h) || Point2Bin(R, 2l) || H)[:l)`.
8. If `S_0 != t`, then return `0`.
9. Return `1`.

# Cryptographic Parameters for TLS {#BTLS}

## Cipher Suites

This specification defines the following cipher suites for TLS 1.3 {{Stb90}}.

|Cipher Suite                  |Value (TBU)    |AEAD             | Hash       |
|------------------------------|---------------|-----------------|------------|
|`TLS_BELT_CHE256_BELT_HASH`   |`{0xFF, 0x1D}` |`belt-che256`    |`belt-hash` |
|`TLS_BASH_PRG_AE2561_BASH256` |`{0xFF, 0x1E}` |`bash-prg-ae2561`|`bash256`   |
{: #SUITES title="STB Cipher Suites"}

Supporting the `TLS_BASH_PRG_AE2561_BASH256` cipher suite is mandated by this
specification. Implementation of `TLS_BELT_CHE256_BELT_HASH` is optional.

Both cipher suites assign `key_length = 32` and `iv_length = 16` (see
{{RFC9846}}, Section 7.3).

In the TLS record protocol, associated data for authenticated encryption
is composed of the `opaque_type`, `legacy_record_version` and `length` fields
of the `TLSCiphertext` structure, 5 bytes in total.

When `bash-prg-ae2561` is used, the associated data `I in {0, 1}^{40}` is
combined with the nonce `S in {0, 1}^{128}` to form the preamble `A`:
`A <- S || I || Rep(0, 24)`. Step 2.1 (`alpha.absorb(I)`) is skipped during both
encryption and decryption.

In the `belt-che256` and `bash-prg-ae2561` algorithms, authentication tags are 8
and 32 bytes long, respectively. An authentication tag `T` is appended to a
ciphertext `Y`, producing the authenticated ciphertext `Y || T` saved to
`TLSCiphertext.encrypted_record`.

A `belt-che256` key must be updated after processing `2^{32}` TLS records.
There are no usage limits for `bash-prg-ae2561` keys.

## The Diffie-Hellman Protocol

The Diffie-Hellman protocol is instantiated as follows.

1. The base cyclic group is a group of elliptic curve points that
   satisfies the `bign-curves` requirements {{BIGN.Curves}}.

2. Ephemeral private and public keys are generated using the
   `bign-genkeypair` algorithm.

3. Parties validate each other's public keys using the
   `bign-valpubkey` algorithm.

4. Parties compute the shared secret `K` as follows: `K = uV`, where `u` is the
   ephemeral private key (scalar), `V` is the ephemeral public key of the
   opposite party (point on the curve). Curve operations are defined in {{BIGN}}.

5. The shared secret `K`, an affine point of the elliptic curve, is encoded as
   `Point2Bin(K, 4l)` {{BIGN.Curves}}, where `l` is the security level.

## Elliptic Curves

The Diffie-Hellman protocol uses the elliptic curves `bign-curve256v1`,
`bign-curve384v1` and `bign-curve512v1` defined in {{CURVES}}.

The group identifiers are added to the `NamedGroup` enumeration (see
{{RFC9846}}, Section 4.3.7):

       enum {
         ...
         bign_curve256v1(0xFE01), /* TBU */
         bign_curve384v1(0xFE02), /* TBU */
         bign_curve512v1(0xFE03)  /* TBU */
         ...
       } NamedGroup;

The identifiers are used in the `supported_groups` and `key_share`
extensions.

## Digital Signature Algorithms

Bign digital signature generation and verification algorithms are instantiated
with three combinations of elliptic curve parameters and hash algorithms for
message preprocessing. These are the resulting compound algorithms.

| Compound Algorithm  | Elliptic Curve    | Hash Algorithm |
|---------------------|-------------------|----------------|
| `bign-with-hbelt`   | `bign-curve256v1` | `belt-hash`    |
| `bign-with-bash384` | `bign-curve384v1` | `bash384`      |
| `bign-with-bash512` | `bign-curve512v1` | `bash512`      |
{: #DSALGS title="Digital Signature Algorithms"}

The digital signature algorithm identifiers are added to the `SignatureScheme`
enumeration (see {{RFC9846}}, Section 4.3.3):

       enum {
         ...
         bign_with_hbelt(0xFE01),     /* TBU */
         bign_with_bash384(0xFE02),   /* TBU */
         bign_with_bash512(0xFE03)    /* TBU */
         ...
       } SignatureScheme;

The identifiers are used in the `signature_algorithms` and
`signature_algorithms_cert` extensions.

# IANA Considerations {#IANA}

This specification requests/registers the following entries to the "TLS Cipher
Suites" registry:

| Value (TBU)  | Description                   | DTLS-OK | Recommended | Reference     |
|--------------|-------------------------------|---------|-------------|---------------|
| `0xFF, 0x1D` | `TLS_BELT_CHE256_BELT_HASH`   | N       | N           | This document |
| `0xFF, 0x1E` | `TLS_BASH_PRG_AE2561_BASH256` | N       | N           | This document |

This specification requests/registers the following entries to the "TLS
Supported Groups" registry:

| Value (TBU) | Description       | DTLS-OK | Recommended | Reference     |
|-------------|-------------------|---------|-------------|---------------|
| `0xFE01`    | `bign-curve256v1` | N       | N           | This document |
| `0xFE02`    | `bign-curve384v1` | N       | N           | This document |
| `0xFE03`    | `bign-curve512v1` | N       | N           | This document |

This specification requests/registers the following entries to the "TLS
SignatureScheme" registry:

| Value (TBU) | Description         | Recommended | Reference     |
|-------------|---------------------|-------------|---------------|
| `0xFE01`    | `bign-with-hbelt`   | N           | This document |
| `0xFE02`    | `bign-with-bash384` | N           | This document |
| `0xFE03`    | `bign-with-bash512` | N           | This document |

{:aside}
> Note: The listed values are placeholders selected from the IANA private-use
> ranges. They are intended for temporary use in pre-IANA-assignment
> implementations of {{Stb90}}. "TBU" indicates that these placeholders will be
> replaced by new IANA-assigned values.

# Security Considerations {#SEC}

The security of TLS 1.3 with STB cryptographic parameters depends on the
the underlying algorithms.

The security of `belt-hash` and `belt-che256` is analyzed in {{Agi26}} and
{{Agi20}}, respectively. The security-driven design rationale of the Bash
algorithms is grounded in {{AMMS17}}. The security of the Bign signature
algorithms, which instantiate the short Schnorr signature, is justified, for
example, in {{BloLee19}}.

--- back

# Recommended Elliptic Curves {#CURVES}

The following elliptic curves are recommended for the Bign family:

* `bign-curve256v1` -- a curve at the security level `l = 128`;
* `bign-curve384v1` -- a curve at the security level `l = 192`;
* `bign-curve512v1` -- a curve at the security level `l = 256`.

The recommended curves satisfy the `bign-curves` requirements 1 -- 11
and the following additional requirements:

12. `p` is the largest suitable prime that does not exceed `2^{2l}`.
13. `a = p - 3`.
14. The numbers `q-1` and `q+1` both have large prime factors.

Requirements 12 and 13 speed up reduction modulo `p` and point doubling.
Requirement 14 provides protection against Cheon's attack {{Che10}}. This attack
is not directly applicable to the Bign algorithms; the purpose of the
requirement is to mitigate risks of using the recommended curves outside of
Bign.

For each security level, the recommended curve was generated as follows:

* 50 curves satisfying the requirements 1 -- 13 were constructed from the
  smallest possible `Bin2Int(seed)` values, starting at `0`;
* among these curves, the one that yields the maximum of `min(gpf(q-1),
  gpf(q+1))` was chosen.

Here `gpf(n)` denotes the greatest prime factor of `n`.

The recommended curves are defined below by parameters `(p, a, b, y_G, q)`.
Seeds used to construct the curves and factorizations of `q-1` and `q+1` are
also given. Large prime divisors are denoted by `r_m`, where `m` is the
divisor's bit length.

## The `bign-curve256v1` Curve

Parameters:

* `p = 2^256 - 189`;
* `a = p - 3`;
* `b = 5418994543382917476470141667052323987242043847840803114498787\`
  `1676190519198705`;
* `y_G = 48835626907528736105417095645674365354469331933013114027389\`
  `791773001019124371`;
* `q = 2^256 - 51359303463308904523350978545619999225`.

Additional details:

* `seed = 0x5E38010000000000`;
* `q - 1 = 2 * 3 * 5 * 59 * 2707 * 8287 * r_{221}`;
* `q + 1 = 2^3 * 7 * 449 * 31327 * r_{227}`.

## The `bign-curve384v1` Curve

Parameters:

* `p = 2^384 - 317`;
* `a = p - 3`;
* `b = 9305714544225430607690103672579840289571010502599374151660380\`
  `432967684614892230431863267093750334370523665755520868`;
* `y_G = 14354597912740189857575301128892105630080584412759834680227\`
  `804744167703823413075975665088124941253511968357604377681`;
* `q = 2^384 -`
  `9886438520659958522437788006980660965037549058207958390857`.

Additional details:

* `seed = 0x23AF000000000000`;
* `q - 1 = 2 * 3 * 13 * 23 * 1217 * r_{363}`;
* `q + 1 = 2^3 * 5 * 17 * r_{375}`.

## The `bign-curve512v1` Curve

Parameters:

* `p = 2^512 - 569`;
* `a = p - 3`;
* `b = 5693315954776639630120063851326436520321079941853637540614063\`
  `30518654910952117316642438613460648635268246458383207794163900221\`
  `6168909012147763529108397200`;
* `y_G = 88068524280977427056041105285534523859274846872460955723526\`
  `40065245926924845204146464197290441971825763243615352431448274721\`
  `410823777569490499978268765629`;
* `q = 2^512 - 34941104250934712071732195640491222284153110230636945\`
  `247985077724188765679887`.

Additional details:

* `seed = 0xAE17020000000000`;
* `q - 1 = 2^4 * 23 * 79 * 767957 * 4433647 * 103529265929 * r_{419}`;
* `q + 1 = 2 * 3^2 * 5 * 19 * 13997 * 93740551 * 20778982613 * r_{427}`.

# ASN.1 Definitions {#ASN1}

## Identifiers

To support STB algorithms in X.509 certificates {{RFC5280}}, this specification
introduces the following ASN.1 object identifiers:

* `bign-with-hbelt`, `bign-with-bash384` and `bign-with-bash512` for the
  algorithms of the same name;
* `bign-pubkey` for public keys of the Bign algorithms;
* `bign-curve256v1`, `bign-curve384v1` and `bign-curve512v1` for the
  recommended curves of the same name.

The identifiers are defined as follows:

       stb OBJECT IDENTIFIER ::= {iso(1) member-body(2) by(112) 0 2 0}

       belt OBJECT IDENTIFIER ::= {stb 34 101 31}
       belt-hash OBJECT IDENTIFIER ::= {belt 81}

       bash OBJECT IDENTIFIER ::= {stb 34 101 77}
       bash256 OBJECT IDENTIFIER ::= {bash 11}
       bash384 OBJECT IDENTIFIER ::= {bash 12}
       bash512 OBJECT IDENTIFIER ::= {bash 13}

       bign OBJECT IDENTIFIER ::= {stb 34 101 45}

       bign-with-hbelt OBJECT IDENTIFIER ::= {bign 12}
       bign-with-bash384 OBJECT IDENTIFIER ::= {bign 14}
       bign-with-bash512 OBJECT IDENTIFIER ::= {bign 15}

       bign-keys OBJECT IDENTIFIER ::= {bign keys(2)}
       bign-pubkey OBJECT IDENTIFIER ::= {bign-keys 1}

       bign-curves OBJECT IDENTIFIER ::= {bign curves(3)}
       bign-curve256v1 OBJECT IDENTIFIER ::= {bign-curves 1}
       bign-curve384v1 OBJECT IDENTIFIER ::= {bign-curves 2}
       bign-curve512v1 OBJECT IDENTIFIER ::= {bign-curves 3}

## Public Keys

At a security level `l`, the public key `Q` is represented as the binary string
`Point2Bin(Q, 4l)`. It is described by the following ASN.1 type:

       PublicKey ::= BIT STRING (SIZE(512|768|1024)).

In X.509 certificates, the public key is described as follows:

       SubjectPublicKeyInfo ::= SEQUENCE {
         algorithm         AlgorithmIdentifier,
         subjectPublicKey  PublicKey
       }

       AlgorithmIdentifier ::= SEQUENCE {
         algorithm   OBJECT IDENTIFIER (bign-pubkey),
         parameters  DomainParameters
       }

       DomainParameters ::= CHOICE {
         named  OBJECT IDENTIFIER
            (bign-curve256v1|bign-curve384v1|bign-curve512v1)
       }

{:aside}
> Note: This specification narrows the options for `DomainParameters` offered
> by {{Stb45}}.

# Test vectors {#TEST}

## Test Vectors for Belt algorithms

### Test Vectors for `belt-block`

~~~
X = BeltH(0, 16)
K = BeltH(128, 32)
Y = belt-block(X, K):
  0x69CCA1C93557C9E3D66BC3E0FA88FA6E
~~~

### Test Vectors for `belt-compress`

~~~
X = BeltH(0, 64)
(S, Y) = belt-compress(X):
  0x46FE7425C9B181EB41DFEE3E72163D5A,
  0xED2F5481D593F40D87FCE37D6BC1A2E1\
    B7D1A2CC975C82D3C0497488C90D99D8
~~~

### Test Vectors for `belt-che256`

~~~
X = BeltH(0, 15)
I = BeltH(16, 32)
K = BeltH(128, 32)
S = BeltH(192, 16)
(Y, T) = belt-che256(X, I, K, S):
  0xBF3DAEAF5D18D2BCC30EA62D2E70A4,
  0x548622B844123FF7
~~~

~~~
Y = BeltH(64, 20)
I = BeltH(80, 32)
K = BeltH(160, 32)
S = BeltH(208, 16)
T = 0x7D9D4F59D40D197D
X = belt-che256-inv(Y, I, T, K, S):
  0x2BABF43EB37B5398A9068F31A3C758\
    B762F44AA9
~~~

### Test Vectors for `belt-hash`

~~~
X = BeltH(0, 13)
Y = belt-hash(X):
  0xABEF9725D4C5A83597A367D14494CC25\
    42F20F659DDFECC961A3EC550CBA8C75
~~~

~~~
X = BeltH(0, 32)
Y = belt-hash(X):
  0x749E4C3653AECE5E48DB4761227742EB\
    6DBE13F4A80F7BEFF1A9CF8D10EE7786
~~~

~~~
X = BeltH(0, 48)
Y = belt-hash(X):
  0x9D02EE446FB6A29FE5C982D4B13AF9D3\
    E90861BC4CEF27CF306BFB0B174A154A
~~~

## Test Vectors for Bash Algorithms

### Test Vectors for `bash256`

~~~
X = NIL
Y = bash256(X):
  0x114C3DFAE373D9BCBC3602D6386F2D6A\
    2059BA1BF9048DBAA5146A6CB775709D
~~~

~~~
X = BeltH(0, 127)
Y = bash256(X):
  0x3D7F4EFA00E9BA33FEED259986567DCF\
    5C6D12D51057A968F14F06CC0F905961
~~~

~~~
X = BeltH(0, 128)
Y = bash256(X):
  0xD7F428311254B8B2D00F7F9EEFBD8F30\
    25FA87C4BABD1BDDBE87E35B7AC80DD6
~~~

~~~
X = BeltH(0, 135)
Y = bash256(X):
  0x1393FA1B65172F2D18946AEAE576FA1C\
    F54FDD354A0CB2974A997DC4865D3100
~~~

### Test Vectors for `bash384`

~~~
X = BeltH(0, 95)
Y = bash384(X):
  0x64334AF830D33F63E9ACDFA184E32522\
    103FFF5C6860110A2CD369EDBC04387C\
    501D8F92F749AE4DE15A8305C353D64D
~~~

~~~
X = BeltH(0, 96)
Y = bash384(X):
  0xD06EFBC16FD6C0880CBFC6A4E3D65AB1\
    01FA82826934190FAABEBFBFFEDE93B2\
    2B85EA72A7FB3147A133A5A8FEBD8320
~~~

~~~
X = BeltH(0, 108)
Y = bash384(X):
  0xFF763296571E2377E71A1538070CC0DE\
    88888606F32EEE6B082788D246686B00\
    FC05A17405C5517699DA44B7EF5F55AB
~~~

### Test Vectors for `bash512`

~~~
X = BeltH(0, 63)
Y = bash512(X):
  0x2A66C87C189C12E255239406123BDEDB\
    F19955EAF0808B2AD705E249220845E2\
    0F4786FB6765D0B5C48984B1B16556EF\
    19EA8192B985E4233D9C09508D6339E7
~~~

~~~
X = BeltH(0, 64)
Y = bash512(X):
  0x07ABBF8580E7E5A321E9B940F667AE20\
    9E2952CEF557978AE743DB086BAB4885\
    B708233C3F5541DF8AAFC3611482FDE4\
    98E58B3379A6622DAC2664C9C118A162
~~~

~~~
X = BeltH(0, 127)
Y = bash512(X):
  0x526073918F97928E9D15508385F42F03\
    ADE3211A23900A30131F8A1E3E1EE21C\
    C09D13CFF6981101235D895746A4643F\
    0AA62B0A7BC98A269E4507A257F0D4EE
~~~

~~~
X = BeltH(0, 192)
Y = bash512(X):
  0x8724C7FF8A2A83F22E38CB9763777B96\
    A70ABA3444F214C763D93CD6D19FCFDE\
    6C3D3931857C4FF6CCCD49BD99852FE9\
    EAA7495ECCDD96B571E0EDCF47F89768
~~~

### Test Vectors for `bash-prg-ae2561`

~~~
A = BeltH(0, 16)
K = BeltH(32, 32)
X = Rep(0, 1536)
I = BeltH(64, 49)
(Y, T) = bash-prg-ae2561(A, X, I, K):
  0x690673766C3E848CAC7C05169FFB7B77\
    51E52A011040E5602573FAF991044A00\
    4329EEF7BED8E6875830A91854D1BD2E\
    DC6FC2FF37851DBAC249DF400A0549EA\
    2E0C811D499E1FF1E5E32FAE7F0532FA\
    4051D0F9E300D9B1DBF119AC8CFFC48D\
    D3CBF1CA0DBA5DD97481C88DF0BE4127\
    85E40988B31585537948B80F5A9C49E0\
    8DD684A7DCA871C380DFDC4C4DFBE61F\
    50D2D0FBD24D8B9D32974A347247D001\
    BAD5B168440025693967E77394DC088B\
    0ECCFA8D291BA13D44F60B06E2EDB351,
  0xCDE5AF6EF9A14B7D0C191B869A6343ED\
    6A4E9AAB4EE00A579E9E682D0EC051E3
~~~

## Test Vectors for Bign Algorithms

### Settings

Test vectors are constructed using the settings given below.

* Elliptic curve parameters: `bign-curve256v1`.

* A private key `d`:

~~~
Int2Bin(d, 256):
  0x1F66B5B84B7339674533F0329C74F218\
    34281FED0732429E0C79235FC273E269
~~~

* A public key `Q`:

~~~
Point2Bin(Q, 512):
  0xBD1A5650179D79E03FCEE49D4C2BD5DD\
    F54CE46D0CF11E4FF87BF7A890857FD0\
    7AC6A60361E8C8173491686D461B2826\
    190C2EDA5909054A9AB84D2AB9D99A90
~~~

* A hashing algorithm `h`: `belt-hash` with
  `OID(belt-hash) = 0x06092A7000020022651F51`.

### Test Vectors for `bign-genk`

~~~
H:
  0xABEF9725D4C5A83597A367D14494CC25\
    42F20F659DDFECC961A3EC550CBA8C75
t = NIL
K:
  0xD61E3A910550E3BCAD5BF4F526FB8DAA\
    DEA9C132E0BAEE03169DF4DF9BD6C20C
Int2Bin(k = bign-genk(d, H), 256):
  0x829614D8411DBBC4E1F2471A40045864\
    40FD8C9553FAB6A1A45CE417AE97111E
~~~

~~~
H:
  0x9D02EE446FB6A29FE5C982D4B13AF9D3\
    E90861BC4CEF27CF306BFB0B174A154A
t:
  0xBE32971343FC9A48A02A885F194B09A1\
    7ECDA4D01544AF
K:
  0xAE44316332A85C3B9F6B31EEEADFF088\
    D30FE507021AC86A3EC8E0874ED33648
Int2Bin(k = bign-genk(d, H), 256):
  0x7ADC8713283EBFA547A2AD9CDFB245AE\
    0F7B968DF0F91CB785D1F932A3583107
~~~

### Test Vectors for `bign-sign`

~~~
X = BeltH(0, 13)
H:
  0xABEF9725D4C5A83597A367D14494CC25\
    42F20F659DDFECC961A3EC550CBA8C75
Int2Bin(k, 256):
  0x4C0E74B2CD5811AD21F23DE7E0FA742C\
    3ED6EC483C461CE15C33A77AA308B7D2
Point2Bin(R, 512):
  0xCCEEF1A313A406649D15DA0A851D486A\
    695B641B20611776252FFDCE39C71060\
    7C9EA1F33C23D20DFCB8485A88BE6523\
    A28ECC3215B47FA289D6C9BE1CE837C0
S = bign-sign(X, d):
  0xE36B7F0377AE4C524027C387FADF1B20\
    CE72F1530B71F2B5FD3A8C584FE2E1AE\
    D20082E30C8AF65011F4FB54649DFD3D
~~~

### Test Vectors for `bign-vfy`

~~~
X = BeltH(0, 48)
S:
  0x47A63C8B9C936E94B5FAB3D9CBD78366\
    290F3210E163EEC8DB4E921E8479D413\
    8F112CC23E6DCE65EC5FF21DF4231C28
H:
  0x9D02EE446FB6A29FE5C982D4B13AF9D3\
    E90861BC4CEF27CF306BFB0B174A154A
Point2Bin(R, 512):
  0x1D5A382B962D4ED06193258CA6DE535D\
    8FD7FACB853171E932EF93B5EE800120\
    03DBB7B5BD07036380BAFA47FCA7E6CA\
    3F179EDDD1AE5086647909183628EDDC
t:
  0x47A63C8B9C936E94B5FAB3D9CBD78366
bign-vfy(X, S, Q):
  1
~~~

