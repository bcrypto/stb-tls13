# IANA Considerations {#IANA}

IANA has assigned the following entries to the "TLS Cipher Suites" registry:

| Value        | Description                   | DTLS-OK | Recommended | Reference     |
|--------------|-------------------------------|---------|-------------|---------------|
| `0x00, 0x72` | `TLS_BELT_CHE256_BELT_HASH`   | N       | N           | This document |
| `0x00, 0x73` | `TLS_BASH_PRG_AE2561_BASH256` | N       | N           | This document |

IANA has assigned the following entries to the "TLS Supported Groups" registry:

| Value | Description       | DTLS-OK | Recommended | Reference     |
|-------|-------------------|---------|-------------|---------------|
| `42`  | `bign-curve256v1` | N       | N           | This document |
| `43`  | `bign-curve384v1` | N       | N           | This document |
| `44`  | `bign-curve512v1` | N       | N           | This document |

IANA has assigned the following entries to the "TLS SignatureScheme" registry:

| Value    | Description         | Recommended | Reference     |
|----------|---------------------|-------------|---------------|
| `0x0710` | `bign-with-hbelt`   | N           | This document |
| `0x0711` | `bign-with-bash384` | N           | This document |
| `0x0712` | `bign-with-bash512` | N           | This document |
