# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2836?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2836
- Title: POP Act
- Congress: 119
- Bill type: S
- Bill number: 2836
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-01-21T07:01:17Z
- Update date including text: 2026-01-21T07:01:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2836",
    "number": "2836",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "POP Act",
    "type": "S",
    "updateDate": "2026-01-21T07:01:17Z",
    "updateDateIncludingText": "2026-01-21T07:01:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-09-17T17:58:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2836is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2836\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mr. Merkley (for himself, Ms. Warren , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit health insurance issuers and certain health care providers under Medicare from being under common ownership, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Patients Over Profit Act or the POP Act .\n#### 2. Prohibition on common ownership of health insurance issuers and certain health care providers under Medicare\n##### (a) In general\nIt shall be unlawful for any person to both\u2014\n**(1)**\ndirectly or indirectly own, operate, or control the whole or any part of an applicable provider or a management services organization that has a management services agreement with an applicable provider; and\n**(2)**\ndirectly or indirectly own, operate, or control the whole or any part of a health insurance issuer.\n##### (b) Divestment\nAny person in violation of subsection (a) shall divest either the applicable provider (or, if applicable, the management services organization) or the health insurance issuer of such person\u2014\n**(1)**\nin the case of an applicable provider, management services organization, or health insurance issuer acquired on or before the date of enactment of this Act, not later than 2 years after such date of enactment; or\n**(2)**\nin the case of an applicable provider, management services organization, or health insurance issuer acquired after the date of enactment of this Act, not later than 1 year after the date of acquisition.\n##### (c) Civil actions\n**(1) In general**\nWhen the Inspector General of the Department of Health and Human Services, the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice, the Federal Trade Commission, or an Attorney General of a State has reason to believe that a person is in violation of subsection (a) or (b), such Inspector General, Assistant Attorney General, Federal Trade Commission, or Attorney General of a State may bring a civil action in an applicable district court of the United States for the relief described in paragraph (2).\n**(2) Injunctive and equitable relief**\nIn any action described in paragraph (1), the applicable court, on a finding that a person is in violation of subsection (a) or (b), shall issue an order requiring such person\u2014\n**(A)**\nto cease and desist from such violation, and divest either the applicable provider (or, if applicable, the management services organization) or the health insurance issuer of such person; and\n**(B)**\nto disgorge any revenue received from the provision of health care services during the period of such violation.\n**(3) Deposit and distribution**\nAny revenue disgorged pursuant to an action under this subsection for a violation of subsection (a) or (b) shall be deposited into a fund created by the Federal Trade Commission and distributed by the Federal Trade Commission to be put to use in the interest of serving the health care needs of the harmed community. Receipt of any funds under this paragraph shall not alter or diminish the rights of an individual to bring an action or recover any amount as otherwise authorized by law.\n##### (d) FTC review\n**(1) Reporting required**\nAny divestment of an applicable provider, management services organization, or health insurance issuer required under subsection (b) shall be reported to the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice under section 7A of the Clayton Act ( 15 U.S.C. 18a ) without respect to the thresholds under subsection (a)(2) of that section.\n**(2) Tolling of divestment period during review**\nThe divestment period under subsection (b) shall be tolled during the pendency of any waiting period required under section 7A of the Clayton Act ( 15 U.S.C. 18a ).\n**(3) Review of effect of divestiture**\nWith respect to each divestiture undertaken pursuant to subsection (b), in addition to any applicable review under section 7A of the Clayton Act ( 15 U.S.C. 18a ), the Federal Trade Commission and the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice shall review the effect on competition, financial viability, and the public interest\u2014\n**(A)**\nof the divestiture; and\n**(B)**\nof the subsequent acquisition of the applicable provider (or, if applicable, the management services organization) or the health insurance issuer of such person by the acquiring person.\n##### (e) Rulemaking authority\nThe Federal Trade Commission shall promulgate rules to carry out this section. Such rules shall not diminish any obligation under this section.\n##### (f) Rule of construction\nNothing in this section shall be construed to limit the authority of the Federal Trade Commission, the Inspector General of the Department of Justice, the Department of Health and Human Services, or the Attorney General of a State under any other provision of law.\n##### (g) Enforcement under Medicare Advantage and Medicare part D\n**(1) Medicare Advantage**\nSection 1857 of the Social Security Act ( 42 U.S.C. 1395w\u201327 ) is amended by adding at the end the following new subsection:\n(j) Prohibition on common ownership of MA organizations and applicable providers (1) In general For plan years beginning on or after January 1, 2026, the Secretary may not contract with, or provide payment under this part to, a Medicare Advantage organization with respect to offering an MA plan or MA\u2013PD plan under this part if the organization\u2014 (A) directly or indirectly owns, operates, or controls the whole or any part of an applicable provider or a management services organization that has a management services agreement with an applicable provider; or (B) is directly or indirectly owned, operated, or controlled in whole or part by a person who also directly or indirectly owns, operates, or controls the whole or any part of an applicable provider or a management services organization that has a management services agreement with an applicable provider. (2) Certification Each Medicare Advantage organization shall furnish to the Secretary (in a form and manner, and at a time, specified by the Secretary) a certification of compliance with this subsection, as well as such information as the Secretary determines necessary to carry out this subsection. (3) False claims submitted by entities in violation of prohibition on common ownership Any claim for payment from an entity in violation of paragraph (1) constitutes a false or fraudulent claim for purposes of subchapter III of title 31, United States Code. (4) Definitions In this subsection: (A) Applicable provider (i) In general Subject to clause (ii), the term applicable provider means any entity that receives payment for furnishing services covered under part B or under a Medicare Advantage plan under part C. (ii) Exclusions Such term does not include\u2014 (I) a hospital (as defined in section 1861(e)), a critical access hospital (as defined in section 1861(mm)(1)), or a rural emergency hospital (as defined in section 1861(kkk)(2)); (II) a supplier of durable medical equipment, prosthetics, orthotics, or supplies; or (III) a pharmacy. (B) Management services agreement The term management services agreement means a contract between a management services organization and an applicable provider for management or administrative services relating to, supporting, or facilitating the provision of health care services. (C) Management services organization The term management services organization means any organization or entity that contracts with an applicable provider to perform management or administrative services relating to, supporting, or facilitating the provision of health care services. .\n**(2) Medicare part D**\nSection 1860D\u201312(b)(3) of the Social Security Act ( 42 U.S.C. 1395w\u2013112(b)(3) ) is amended by adding at the end the following new subparagraph:\n(G) Prohibition on common ownership Section 1857(j). .\n##### (h) Definitions\nIn this section:\n**(1) Applicable provider**\n**(A) In general**\nSubject to subparagraph (B), the term applicable provider means any entity that receives payment for furnishing services covered under part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. ) or under a Medicare Advantage plan under part C of such title ( 42 U.S.C. 1395w\u201321 et seq. ).\n**(B) Exclusions**\nSuch term does not include\u2014\n**(i)**\na hospital (as defined in section 1861(e) of the Social Security Act ( 42 U.S.C. 1395x(e) )), a critical access hospital (as defined in section 1861(mm)(1) of such Act ( 42 U.S.C. 1395x(mm)(1) )), or a rural emergency hospital (as defined in section 1861(kkk)(2));\n**(ii)**\na supplier of durable medical equipment, prosthetics, orthotics, and supplies; or\n**(iii)**\na pharmacy.\n**(2) Health insurance issuer**\nThe term health insurance issuer has the meaning given that term in section 2791 of the Public Health Service Act ( 42 U.S.C. 300gg\u201391 ).\n**(3) Management services agreement**\nThe term management services agreement means a contract between a management services organization and an applicable provider for management or administrative services relating to, supporting, or facilitating the provision of health care services.\n**(4) Management services organization**\nThe term management services organization means any organization or entity that contracts with an applicable provider to perform management or administrative services relating to, supporting, or facilitating the provision of health care services.\n**(5) Person**\nThe term person has the meaning given the term in section 8 of the Sherman Act ( 15 U.S.C. 7 ).",
      "versionDate": "2025-09-17",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-17",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Energy and Commerce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5433",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "POP Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-09T22:13:56Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2836is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "POP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "POP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Patients Over Profit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit health insurance issuers and certain health care providers under Medicare from being under common ownership, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:27Z"
    }
  ]
}
```
