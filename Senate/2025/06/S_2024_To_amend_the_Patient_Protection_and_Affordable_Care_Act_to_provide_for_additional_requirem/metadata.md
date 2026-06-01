# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2024?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2024
- Title: ENROLL Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2024
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-12-05T21:38:14Z
- Update date including text: 2025-12-05T21:38:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2024",
    "number": "2024",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "ENROLL Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:38:14Z",
    "updateDateIncludingText": "2025-12-05T21:38:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T16:08:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NH"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NM"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-11",
      "state": "ME"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-16",
      "state": "VT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2024is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2024\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Ms. Baldwin (for herself, Mrs. Shaheen , Mr. Merkley , Mr. Luj\u00e1n , Mr. King , Mr. Wyden , Mr. Booker , Ms. Duckworth , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Patient Protection and Affordable Care Act to provide for additional requirements with respect to the navigator program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expand Navigators\u2019 Resources for Outreach, Learning, and Longevity Act of 2025 or the ENROLL Act of 2025 .\n#### 2. Providing for additional requirements with respect to the navigator program\n##### (a) In general\nSection 1311(i) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(i) ) is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(C) Selection of recipients In the case of an Exchange established and operated by the Secretary within a State pursuant to section 1321(c), in awarding grants under paragraph (1), the Exchange shall\u2014 (i) select entities to receive such grants based on an entity\u2019s demonstrated capacity to carry out each of the duties specified in paragraph (3); (ii) not take into account whether or not the entity has demonstrated how the entity will provide information to individuals relating to group health plans that are not qualified health plans; and (iii) ensure that, each year, the Exchange awards such a grant to at least 1 entity described in this paragraph that is a community and consumer-focused nonprofit group. ;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (C), by inserting after qualified health plans the following: , State Medicaid plans under title XIX of the Social Security Act, and State children\u2019s health insurance programs under title XXI of such Act ;\n**(B)**\nin subparagraph (D), by striking and at the end;\n**(C)**\nin subparagraph (E), by striking the period and inserting ; and ;\n**(D)**\nby adding at the end the following:\n(F) conduct public education activities in plain language to raise awareness of the requirements of and the protections provided under qualified health plans. ; and\n**(E)**\nby adding at the end the following flush left sentence:\nThe duties specified in the preceding sentence may be carried out by such a navigator at any time during a year.\n**(3)**\nin paragraph (4)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by striking not ;\n**(B)**\nin clause (i)\u2014\n**(i)**\nby inserting not before be ; and\n**(ii)**\nby striking ; or and inserting a semicolon;\n**(C)**\nin clause (ii)\u2014\n**(i)**\nby inserting not before receive ; and\n**(ii)**\nby striking the period and inserting a semicolon; and\n**(D)**\nby adding at the end the following new clause:\n(iii) maintain physical presence in the State of the Exchange so as to allow in-person assistance to consumers. ; and\n**(4)**\nin paragraph (6)\u2014\n**(A)**\nby striking Funding .\u2014Grants under and inserting\nFunding .\u2014 (A) State Exchanges Grants under ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) Federal Exchanges For purposes of carrying out this subsection, with respect to an Exchange established and operated by the Secretary within a State pursuant to section 1321(c), the Secretary shall obligate $100,000,000 out of amounts collected through the user fees on participating health insurance issuers pursuant to section 156.50 of title 45, Code of Federal Regulations (or any successor regulations) for fiscal year 2026 and each subsequent fiscal year. Such amount for a fiscal year shall remain available until expended. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-06-11",
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
        "actionDate": "2025-06-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3907",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ENROLL Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-07-01T12:53:25Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2024is.xml"
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
      "title": "ENROLL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ENROLL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expand Navigators\u2019 Resources for Outreach, Learning, and Longevity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Patient Protection and Affordable Care Act to provide for additional requirements with respect to the navigator program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:24Z"
    }
  ]
}
```
