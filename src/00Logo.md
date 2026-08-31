---
title: "STB Cryptographic Parameters for Transport Layer Security (TLS)
  Protocol Version 1.3"
abbrev: stb-tls13
docname: draft-stb-tls13-00
submissiontype: independent
category: info
v: 3
lang: en
ipr: trust200902
stand_alone: yes
smart_quotes: yes
pi: [toc, sortrefs, symrefs]

author:
 -
    name: Sergey Agievich
    ins: S. Agievich
    organization: APMI, Belarusian State University
    email: agievichi@bsu.by
 -
    name: Nikolai Kalosha
    ins: N. Kalosha
    organization: IM, Academy of Sciences of Belarus
    email: kalosha@im.bas-net.by

contributor:
  -
    name: Nastassia Kozlovskaya
    ins: N. Kozlovskaya
    organization: APMI, Belarusian State University

normative:

  RFC5280:
  RFC9846:

informative:

  AgiAfo05:
    title: "Exponential S-boxes"
    target: https://eprint.iacr.org/2004/024
    date: 2005
    seriesinfo:
      Vesti NAN Belarusi: "2005(1), pp. 106-112"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University
      -
        ins: A. Afonenko
        name: Andrey Afonenko
        org: Belarusian State University

  Agi20:
    title: "The Counter mode with encrypted nonces and its extension to AE"
    target: https://eprint.iacr.org/2020/331
    date: 2020
    seriesinfo:
      Mat. Vopr. Kriptogr.: "11(2), pp. 7-24"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University

  Agi26:
    title: "On the security of belt-hash and belt-compress"
    date: 2026-06
    rc: "Pre-proceedings of the 15th Workshop on Current Trends in Cryptology
      (CTCrypt'2026), pp. 445-470"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University

  AMMS17:
    title: "Bash-f: another LRX sponge function"
    target: https://eprint.iacr.org/2016/587
    date: 2017
    seriesinfo:
      Mat. Vopr. Kriptogr.: "8(2), pp. 7-28"
    author:
      -
        ins: S. Agievich
        name: Sergey Agievich
        org: Belarusian State University
      -
        ins: V. Marchuk
        name: Vadim Marchuk
        org: Belarusian State University
      -
        ins: A. Maslau
        name: Alexander Maslau
        org: Belarusian State University
      -
        ins: V. Semenov
        name: Vladislav Semenov
        org: Belarusian State University

  BloLee19:
    title: "On the Multi-user Security of Short Schnorr Signatures with
      Preprocessing"
    target: https://eprint.iacr.org/2019/1105
    date: 2019
    rc: "Proceedings of EUROCRYPT 2022, pp. 614-643"
    author:
      -
        ins: J. Blocki
        name: Jeremiah Blocki
      -
        ins: S. Lee
        name: Seunghoon Lee

  Che10:
    title: "Discrete Logarithm Problems with Auxiliary Inputs"
    date: 2010
    seriesinfo:
      J. Cryptology: "vol. 23, pp. 457-476"
    author:
      -
        ins: J.H. Cheon
        name: Jung Hee Cheon

  HMV04:
    title: "Guide to Elliptic Curve Cryptography"
    date: 2004
    rc: "New York: Springer"
    author:
      -
        ins: D. Hankerson
        name: Darrel Hankerson
      -
        ins: A. Menezes
        name: Alfred Menezes
      -
        ins: S. Vanstone
        name: Scott Vanstone

  LidNie97:
    title: "Finite Fields"
    date: 1997
    rc: "Cambridge University Press"
    author:
      -
        ins: R. Lidl
        name: Rudolf Lidl
      -
        ins: H. Niederreiter
        name: Harald Niederreiter

  McGVie04:
    title: "The security and performance of the Galois/Counter Mode (GCM)
      of operation"
    target: https://eprint.iacr.org/2004/193
    date: 2004
    rc: INDOCRYPT 2004
    author:
      -
        ins: D.A. McGrew
        name: David McGrew
      -
        ins: J. Viega
        name: John Viega

  Sch91:
    title: "Efficient Signature Generation by Smart Cards"
    date: 1991
    seriesinfo:
      J. Cryptology: "4(3), pp. 161-174"
    author:
      -
        ins: C.P. Schnorr
        name: Claus P. Schnorr

  Stb31:
    title: "STB 34.101.31-2020. Information technology and security. Encryption
      and integrity control algorithms"
    date: 2020
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

  Stb45:
    title: "STB 34.101.45-2013. Information technology and security. Digital
      signature and key transport algorithms based on elliptic curves"
    date: 2013
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

  Stb77:
    title: "STB 34.101.77-2020. Information technology and security.
      Sponge-bases cryptographic algorithms"
    date: 2020
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

  Stb90:
    title: "STB 34.101.90-2026. Information technology and security. The
      Transport Layer Security Protocol Version 1.3"
    date: 2026
    author:
      -
        ins: The State Committee for Standardization of the Republic of Belarus

--- abstract

This specification introduces a subset of STB (STandards of Belarus)
cryptographic algorithms and defines their use in TLS 1.3. The document is
self-contained, i.e., it fully describes the required STB algorithms. It can be
used to develop STB-compliant TLS 1.3 implementations without referring to
the original STB standards.

--- middle
