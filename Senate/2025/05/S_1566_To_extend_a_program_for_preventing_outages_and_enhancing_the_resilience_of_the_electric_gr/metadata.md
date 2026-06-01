# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1566?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1566
- Title: Preventing Power Outages Act
- Congress: 119
- Bill type: S
- Bill number: 1566
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1566",
    "number": "1566",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Preventing Power Outages Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T16:25:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1566is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1566\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Peters (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo extend a program for preventing outages and enhancing the resilience of the electric grid, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Power Outages Act .\n#### 2. Preventing outages and enhancing the resilience of the electric grid\nSection 40101 of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18711 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (1) through (5) as paragraphs (2) through (6), respectively; and\n**(B)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) CAIDI; SAIDI ; SAIFI The terms Customer Average Interruption Duration Index (or CAIDI ), System Average Interruption Duration Index (or SAIDI ), and System Average Interruption Frequency Index (or SAIFI ) have the same meanings as in the standard published by the Institute of Electrical and Electronics Engineers Standards Association entitled IEEE Guide for Electric Power Distribution Reliability Indices and numbered 1366 (or a successor standard), subject to the condition that, in calculating each index, all outages greater than 5 minutes, including on Major Event Days (within the meaning of that standard (or a successor standard)), are included in the calculation. ;\n**(2)**\nin subsection (c)(4)\u2014\n**(A)**\nby striking the paragraph designation and heading and all that follows through In and inserting the following:\n(4) Priority; special consideration (A) Priority In ; and\n**(B)**\nby adding at the end the following:\n(B) Special consideration In making grants to eligible entities under the program, the Secretary shall take into consideration the scores of the eligible entities on the System Average Interruption Duration Index, the System Average Interruption Frequency Index, and the Customer Average Interruption Duration Index during the previous 5 years, with eligible entities having lower reliability, as indicated by higher SAIDI, SAIFI, or CAIDI scores during that period, receiving additional weight or consideration as compared to eligible entities having higher reliability, as indicated by lower SAIDI, SAIFI, or CAIDI scores during that period. ;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (3)(B), by adding at the end the following:\n(vi) The scores of the State or Indian Tribe on the System Average Interruption Duration Index, the System Average Interruption Frequency Index, and the Customer Average Interruption Duration Index during the previous 5 years, with States or Indian Tribes having lower reliability, as indicated by higher SAIDI, SAIFI, or CAIDI scores during that period, receiving additional weight or consideration as compared to States or Indian Tribes having higher reliability, as indicated by lower SAIDI, SAIFI, or CAIDI scores during that period. ; and\n**(B)**\nin paragraph (5)\u2014\n**(i)**\nby striking the paragraph designation and heading and all that follows through In and inserting the following:\n(5) Priority; special consideration (A) Priority In ; and\n**(ii)**\nby adding at the end the following:\n(B) Special consideration In making grants to eligible entities using funds made available to the applicable State or Indian Tribe under the program, the State or Indian Tribe shall take into consideration the scores of the eligible entities on the System Average Interruption Duration Index, the System Average Interruption Frequency Index, and the Customer Average Interruption Duration Index during the previous 5 years, with eligible entities having lower reliability, as indicated by higher SAIDI, SAIFI, or CAIDI scores during that period, receiving additional weight or consideration as compared to eligible entities having higher reliability, as indicated by lower SAIDI, SAIFI, or CAIDI scores during that period. ;\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2), by striking subparagraph (C); and\n**(B)**\nby adding at the end the following:\n(3) Clarification In making grants to eligible entities under this section, the Secretary, a State, or an Indian Tribe may not\u2014 (A) condition the submission of an application for, or receipt of, such a grant on the application addressing more than 1 type or category of activities, technologies, equipment, or hardening measures described in paragraph (1); or (B) give priority or any other preference to an application solely because the application addresses more than 1 type or category of activities, technologies, equipment, or hardening measures described in that paragraph. ; and\n**(5)**\nin subsection (j), by striking 2022 through 2026 and inserting 2027 through 2031, to remain available until expended .",
      "versionDate": "2025-05-01",
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
        "name": "Energy",
        "updateDate": "2025-05-21T13:21:53Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1566is.xml"
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
      "title": "Preventing Power Outages Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Power Outages Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend a program for preventing outages and enhancing the resilience of the electric grid, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:33Z"
    }
  ]
}
```
