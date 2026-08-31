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
