# Recommended Elliptic Curves {#CURVES}

The following elliptic curves are recommended for the Bign family:

* `bign-curve256v1` -- a curve at the security level `l = 128`;
* `bign-curve384v1` -- a curve at the security level `l = 192`;
* `bign-curve512v1` -- a curve at the security level `l = 256`.

The recommended curves satisfy the `bign-curves` requirements 1 -- 11
and the following additional requirements:

12. `p` is the largest suitable prime that does not exceed `2^{2l}`.
13. `a = p - 3`.
14. The numbers `q-1` and `q+1` both have large prime factors.

Requirements 12 and 13 speed up reduction modulo `p` and point doubling.
Requirement 14 provides protection against Cheon's attack {{Che10}}. This attack
is not directly applicable to the Bign algorithms; the purpose of the
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
* `b = 54189945433829174764701416670523239872420438478408031144987871676190519`
       `198705`;
* `y_G = 488356269075287361054170956456743653544693319330131140273897917730010`
        `19124371`;
* `q = 2^256 - 51359303463308904523350978545619999225`.

Additional details:

* `seed = 0x5E38010000000000`;
* `q - 1 = 2 * 3 * 5 * 59 * 2707 * 8287 * r_{221}`;
* `q + 1 = 2^3 * 7 * 449 * 31327 * r_{227}`.

## The `bign-curve384v1` Curve

Parameters:

* `p = 2^384 - 317`;
* `a = p - 3`;
* `b = 9305714544225430607690103672579840289571010502599374151660380432967684`
      `614892230431863267093750334370523665755520868`;
* `y_G = 14354597912740189857575301128892105630080584412759834680227804744167`
        `703823413075975665088124941253511968357604377681`;
* `q = 2^384 - 9886438520659958522437788006980660965037549058207958390857`.

Additional details:

* `seed = 0x23AF000000000000`;
* `q - 1 = 2 * 3 * 13 * 23 * 1217 * r_{363}`;
* `q + 1 = 2^3 * 5 * 17 * r_{375}`.

## The `bign-curve512v1` Curve

Parameters:

* `p = 2^512 - 569`;
* `a = p - 3`;
* `b = 569331595477663963012006385132643652032107994185363754061406330518654910`
      `952117316642438613460648635268246458383207794163900221616890901214776352`
      `9108397200`;
* `y_G = 8806852428097742705604110528553452385927484687246095572352640065245926`
        `9248452041464641972904419718257632436153524314482747214108237775694904`
        `99978268765629`;
* `q = 2^512 - 349411042509347120717321956404912222841531102306369452479850777`
      `24188765679887`.

Additional details:

* `seed = 0xAE17020000000000`;
* `q - 1 = 2^4 * 23 * 79 * 767957 * 4433647 * 103529265929 * r_{419}`;
* `q + 1 = 2 * 3^2 * 5 * 19 * 13997 * 93740551 * 20778982613 * r_{427}`.
