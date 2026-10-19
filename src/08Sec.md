# Security Considerations {#SEC}

The security of TLS 1.3 with STB cryptographic parameters depends on the
the underlying algorithms.

The security-driven design rationale of the `belt-block` and
`bash-f` algorithms, the core primitives of the Belt and Bash families,
is provided in {{AGMK02}} and {{AMMS17}}.

Security analysis of `belt-hash` in {{Agi26}} shows that under an idealized
internal compression function, the collision attack requires approximately
`2^{128}` operations, and the preimage and second-preimage attacks require at
least `2^{192}` operations. Both complexities are achievable, although the
latter holds only if the resulting preimages are relatively long and of a
weakly controlled format. Thus, while the collision security of `belt-hash`
matches that of an ideal (random) 256-bit hash function, its preimage security
is lower. However, structural constraints on preimages prevent this lower
security bound from being exploited in TLS 1.3. In particular, the Bign digital
signature that uses `belt-hash` for internal hashing is potentially affected at
the security level `l = 256`, where inverting `belt-hash` in under `2^{256}`
operations could accelerate signature forgery. However, the forgery attack
requires the preimage to be a short string with a highly restricted format,
rendering it infeasible.

The security of `belt-che256` is analyzed in {{Agi20}}. The security guarantees
established in that analysis are justified provided that the total number of
128-bit blocks processed by the underlying `belt-block` cipher is significantly
less than `2^{64}`. This constraint is directly addressed in the definition of
the `TLS_BELT_CHE256_BELT_HASH` ciphersuite, which requires rekeying
`belt-che256` after processing `2^{32}` TLS records.

The `bash256` algorithm follows an overwrite mode of sponge-based hash
functions {{BDPV11}}. In this mode, security guarantees of `bash256`-based
HMAC--and, in turn, HKDF--can be justified using the approach of {{Bel06}},
where the underlying `bash-f` algorithm is treated as a classical compression
function, or directly within the framework of sponge-based cryptography
(see Section 5.1.3 of {{BDPV11a}}).

The security of the Bign signature algorithms, which instantiate the short
Schnorr signature, is justified, for example, in {{BloLee19}}. The
deterministic mode of `bign-sign` avoids drawbacks of the usual
probabilistic mode, where the weaknesses of RNG / PRNG can yield reuse of
ephemeral keys and thus compromise the private key. We recommend using the
deterministic mode with a randomly generated `t`, the deterministic mode with a
fixed `t`, and the probabilistic mode, in this order of preference.

--- back
