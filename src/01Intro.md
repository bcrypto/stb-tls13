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
