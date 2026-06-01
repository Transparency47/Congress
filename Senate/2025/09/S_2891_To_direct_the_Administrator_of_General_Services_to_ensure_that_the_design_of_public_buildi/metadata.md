# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2891?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2891
- Title: Democracy in Design Act
- Congress: 119
- Bill type: S
- Bill number: 2891
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-02-26T12:03:17Z
- Update date including text: 2026-02-26T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2891",
    "number": "2891",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Democracy in Design Act",
    "type": "S",
    "updateDate": "2026-02-26T12:03:17Z",
    "updateDateIncludingText": "2026-02-26T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
            "date": "2025-09-18T20:26:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T20:26:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2891is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2891\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Van Hollen (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo direct the Administrator of General Services to ensure that the design of public buildings in the United States adheres to the guiding principles for Federal architecture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Democracy in Design Act .\n#### 2. Continuing investigation and survey of public buildings\n##### (a) In general\nSection 3303 of title 40, United States Code, is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding paragraph (1), by inserting (referred to in this section as the Administrator ) after Services ; and\n**(2)**\nby adding at the end the following:\n(e) Guiding principles for Federal architecture The Administrator shall ensure that the design of public buildings in the United States adheres to the principles described in the report published by the Ad Hoc Committee on Federal Office Space entitled Guiding Principles for Federal Architecture and dated June 1, 1962. .\n##### (b) Rulemaking\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator of General Services shall promulgate such regulations as are necessary\u2014\n**(A)**\nto implement the amendment made by subsection (a)(2); and\n**(B)**\nto establish minimum standards by which the Administrator of General Services shall design public buildings (as defined in section 3301(a) of title 40, United States Code) in the United States.\n**(2) Notice and comment**\nThe regulations required under paragraph (1) shall be issued after notice and an opportunity for public comment in accordance with the procedure applicable to substantive rules under section 553 of title 5, United States Code.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-02-25",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "1584",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Democracy in Design Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-02T20:08:28Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2891is.xml"
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
      "title": "Democracy in Design Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Democracy in Design Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Administrator of General Services to ensure that the design of public buildings in the United States adheres to the guiding principles for Federal architecture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:22Z"
    }
  ]
}
```
