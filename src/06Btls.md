# STB Cryptographic Parameters {#BTLS}

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
