# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1715?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1715
- Title: Protecting Privacy in Purchases Act
- Congress: 119
- Bill type: S
- Bill number: 1715
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2026-02-13T12:03:21Z
- Update date including text: 2026-02-13T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1715",
    "number": "1715",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Protecting Privacy in Purchases Act",
    "type": "S",
    "updateDate": "2026-02-13T12:03:21Z",
    "updateDateIncludingText": "2026-02-13T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-12",
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
        "item": [
          {
            "date": "2025-05-12T22:03:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-12T22:03:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "WV"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "WY"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "LA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "ND"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "MT"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "UT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "ND"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "OK"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "MS"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "KS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "MS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "WV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MT"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1715is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1715\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Hagerty (for himself, Mr. Justice , Mr. Graham , Mr. Risch , Ms. Lummis , Mr. Cassidy , Mr. Hoeven , Mr. Budd , Mr. Daines , Mr. Lee , Mr. Ricketts , Mr. Cramer , Mr. Crapo , Mr. Scott of Florida , Mr. Mullin , Mrs. Fischer , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit payment card networks and covered entities from requiring the use of or assigning merchant category codes that distinguish a firearms retailer from a general merchandise retailer or sporting goods retailer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Privacy in Purchases Act .\n#### 2. Distinguishing firearms sales\n##### (a) Definitions\nIn this section:\n**(1) Ammunition**\nThe term ammunition has the meaning given the term in section 921(a)(17)(A) of title 18, United States Code, as applied to a firearm, as defined in paragraph (3).\n**(2) Covered entity**\nThe term covered entity means any entity that establishes a relationship with\u2014\n**(A)**\na merchant for the purposes of processing credit, debit, or prepaid transactions; or\n**(B)**\nanother entity that establishes a relationship with a merchant for the purposes of processing credit, debit, or prepaid transactions.\n**(3) Firearm**\nThe term firearm means an item described in paragraph (3), (5), (7), (16), (29), or (30) of section 921(a) of title 18, United States Code.\n**(4) Firearms retailer**\nThe term firearms retailer means a person or entity engaged in the lawful business of selling or trading\u2014\n**(A)**\nfirearms; or\n**(B)**\nammunition to be used in firearms.\n**(5) Merchant category code**\nThe term merchant category code means a multi-digit code that is issued by the International Organization for Standardization for the purposes of enabling the classification of merchants into specific categories based on the type of business or trade of the merchant or the services supplied by the merchant.\n**(6) Payment card network**\nThe term payment card network means an entity that, directly or through a licensed member, processor, or agent, provides a proprietary service, infrastructure, software, or hardware that routes information used to authorize, clear, and settle credit card and debit card transactions.\n##### (b) Prohibitions relating to merchant category codes\n**(1) Payment card networks**\nA payment card network may not require a firearms retailer to use, nor require a covered entity to assign to a firearms retailer, a merchant category code that distinguishes the firearms retailer from a general merchandise retailer or a sporting goods retailer.\n**(2) Covered entities**\nNeither a covered entity, nor any agent of a covered entity, may assign to a firearms retailer any merchant category code that distinguishes the firearms retailer from a general merchandise retailer or a sporting goods retailer.\n##### (c) Enforcement\n**(1) In general**\nThe Attorney General shall\u2014\n**(A)**\nenforce this section, including by conducting investigations of potential violations of this section; and\n**(B)**\nnot later than 90 days after the date of enactment of this Act, establish a process for a person, including a firearms retailer, to submit to the Attorney General a complaint relating to an alleged violation of this section.\n**(2) Investigation**\nThe Attorney General shall investigate each complaint received through the processes established under paragraph (1)(B).\n**(3) Written notice**\nIf the Attorney General determines after conducting an investigation (whether initiated by the Attorney General or through a complaint received through the process established under paragraph (1)(B)) that a payment card network or a covered entity has violated this section, the Attorney General shall send to that payment card network or covered entity, as applicable, written notice of that violation that requires the payment card network or covered entity to remedy the violation not later than 30 days after the date on which the payment card network or covered entity receives that notice.\n**(4) Injunction**\nIf a payment card network or covered entity does not remedy a violation of this section within 30 days of receiving written notice under paragraph (3), the Attorney General may bring an action in an appropriate district court of the United States to enjoin the violating behavior.\n##### (d) Preemption\nAny law of a State or local government regulating merchant category codes for firearm retailers is hereby preempted by this section.\n##### (e) No private right of action\nNothing in this section may be construed as establishing a private right of action.\n##### (f) Report\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Attorney General shall submit to Congress a report that\u2014\n**(1)**\nfor the year covered by the report, identifies the total number of investigations undertaken by the Attorney General under this section, whether initiated by the Attorney General or through a complaint received through the process established under subsection (c)(1)(B);\n**(2)**\nincludes a summary of each investigation described in paragraph (1), including the disposition of each such investigation; and\n**(3)**\nprovides any available data and analysis regarding the effectiveness of this Act.",
      "versionDate": "2025-05-12",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-28T12:41:49Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1715is.xml"
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
      "title": "Protecting Privacy in Purchases Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Privacy in Purchases Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit payment card networks and covered entities from requiring the use of or assigning merchant category codes that distinguish a firearms retailer from a general merchandise retailer or sporting goods retailer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:20Z"
    }
  ]
}
```
