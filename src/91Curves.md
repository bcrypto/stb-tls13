# Recommended Elliptic Curves {#CURVES}

The following elliptic curves are recommended for the Bign family:

* `bign-curve256v1` -- a curve at the security level `l = 128`;
* `bign-curve384v1` -- a curve at the security level `l = 192`;
* `bign-curve512v1` -- a curve at the security level `l = 256`.

The recommended curves satisfy the `bign-curves` requirements 1 -- 12
and the following additional requirements:

13. `p` is the largest suitable prime that does not exceed `2^{2l}`.
14. `a = p - 3`.
15. The numbers `q-1` and `q+1` both have large prime factors.

Requirements 13 and 14 speed up reduction modulo `p` and point doubling.
Requirement 15 provides protection against Cheon's attack {{Che10}}. This
attack is not directly applicable to the Bign algorithms; the purpose of the
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
