# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2400
- Title: Art Market Integrity Act
- Congress: 119
- Bill type: S
- Bill number: 2400
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-09-17T16:45:03Z
- Update date including text: 2025-09-17T16:45:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2400",
    "number": "2400",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Art Market Integrity Act",
    "type": "S",
    "updateDate": "2025-09-17T16:45:03Z",
    "updateDateIncludingText": "2025-09-17T16:45:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T16:22:13Z",
          "name": "Referred To"
        }
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "IA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "RI"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NJ"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2400is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2400\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Fetterman (for himself, Mr. Grassley , Mr. Whitehouse , Mr. McCormick , Mr. Kim , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend title 31, United States Code, to subject certain art traders to provisions relating to records and reports on monetary instruments transactions.\n#### 1. Short title\nThis Act may be cited as the Art Market Integrity Act .\n#### 2. Records and reports on monetary instruments transactions\n##### (a) Records and reports\n**(1) In general**\nSection 5312 of title 31, United States Code, is amended\u2014\n**(A)**\nin subsection (a)(2)\u2014\n**(i)**\nby redesignating subparagraphs (Y) and (Z) as subparagraphs (Z) and (AA), respectively; and\n**(ii)**\nby inserting after subparagraph (X) the following:\n(Y) a person engaged in the trade in works of art, including a dealer, advisor, consultant, custodian, gallery, auction house, museum, collector, or any other person who engages as a business as an intermediary in the sale of works of art, unless the person\u2014 (i) during the prior year, participated in no single transaction valued over $10,000 that involved a work of art; (ii) has not, during the prior year, participated in total transactions valued at $50,000 that involved a work of art; or (iii) is a person engaged in the art market for the sole purpose of selling works of art created by the person. ; and\n**(B)**\nin subsection (c), by adding at the end the following:\n(2) Work of art The term work of art means any original painting, sculpture, watercolor, print, drawing, photograph, installation art, or video art, not including\u2014 (A) applied art such as product design, fashion design, architectural design, or interior design; or (B) mass-produced decorative art, including ceramics, textiles, or carpets. .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall take effect on the earlier of\u2014\n**(A)**\nthe effective date of the rules issued under subsection (c); and\n**(B)**\nthe date that is 360 days after the date of enactment of this Act.\n##### (b) Mandatory update to Treasury guidance on art transactions\n**(1) In general**\nNot later than 360 days after the date of enactment of this Act, the Secretary of the Treasury shall issue updated guidance to the advisory issued by the Office of Foreign Asset Control on October 30, 2020, regarding the risks of high-value artwork transactions involving sanctioned persons or entities.\n**(2) Interagency coordination**\nThe Secretary of Treasury shall consult and coordinate with appropriate Federal agencies to update the guidance described in paragraph (1).\n##### (c) Rulemaking\nNot later than 180 days after the date of enactment of this Act, the Secretary of the Treasury (acting through the Director of the Financial Crimes Enforcement Network), in consultation and coordination with appropriate Federal agencies, shall issue proposed rules to carry out the amendments made by subsection (a), including\u2014\n**(1)**\ndetermining which persons should be subject to the rulemaking based on domestic or international geographical location;\n**(2)**\nthe degree to which the regulations should apply based on status as an agent or intermediary acting on behalf of a purchaser; and\n**(3)**\nwhether certain exemptions should apply to the regulations.\n##### (d) Technical and conforming amendments\nSection 6110(a) of the Anti-Money Laundering Act of 2020 (title LXI of division F of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 134 Stat. 4561)) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking subparagraphs (Z) and (AA) and inserting subparagraphs (AA) and (BB) ; and\n**(ii)**\nby striking subparagraphs (Y) and (Z) and inserting subparagraphs (Z) and (AA) ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking subparagraph (X) and inserting subparagraph (Y) ; and\n**(ii)**\nby striking \u2018(Y) a and inserting \u2018(X) a ; and\n**(2)**\nin paragraph (2), by striking Section 5312(a)(2)(Y) and inserting Section 5312(a)(2)(X) .",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-17T16:45:03Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2400is.xml"
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
      "title": "Art Market Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Art Market Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 31, United States Code, to subject certain art traders to provisions relating to records and reports on monetary instruments transactions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:32Z"
    }
  ]
}
```
