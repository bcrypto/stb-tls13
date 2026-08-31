# Security Considerations {#SEC}

The security of TLS 1.3 with STB cryptographic parameters depends on the
the underlying algorithms.

The security of `belt-hash` and `belt-che256` is analyzed in {{Agi26}} and
{{Agi20}}, respectively. The security-driven design rationale of the Bash
algorithms is grounded in {{AMMS17}}. The security of the Bign signature
algorithms, which instantiate the short Schnorr signature, is justified, for
example, in {{BloLee19}}.

--- back
