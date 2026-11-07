# IANA Considerations {#IANA}

This specification registers the following entries to the "TLS Cipher Suites"
registry:

| Value        | Description                   | DTLS-OK | Recommended | Reference     |
|--------------|-------------------------------|---------|-------------|---------------|
| `0x00, 0x72` | `TLS_BELT_CHE256_BELT_HASH`   | N       | N           | This document |
| `0x00, 0x73` | `TLS_BASH_PRG_AE2561_BASH256` | N       | N           | This document |

This specification registers the following entries to the "TLS Supported
Groups" registry:

| Value | Description       | DTLS-OK | Recommended | Reference     |
|-------|-------------------|---------|-------------|---------------|
| `42`  | `bign-curve256v1` | N       | N           | This document |
| `43`  | `bign-curve384v1` | N       | N           | This document |
| `44`  | `bign-curve512v1` | N       | N           | This document |

This specification registers the following entries to the "TLS SignatureScheme"
registry:

| Value    | Description         | Recommended | Reference     |
|----------|---------------------|-------------|---------------|
| `0x0710` | `bign-with-hbelt`   | N           | This document |
| `0x0711` | `bign-with-bash384` | N           | This document |
| `0x0712` | `bign-with-bash512` | N           | This document |

{:aside}
> Note: The listed values are placeholders selected from the IANA private-use
> ranges. They are intended for temporary use in pre-IANA-assignment
> implementations of {{Stb90}}. "TBU" indicates that these placeholders will be
> replaced by new IANA-assigned values.
