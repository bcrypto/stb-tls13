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
