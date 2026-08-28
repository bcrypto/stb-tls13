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
