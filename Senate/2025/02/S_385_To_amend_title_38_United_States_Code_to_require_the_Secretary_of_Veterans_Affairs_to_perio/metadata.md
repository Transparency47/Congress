# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/385
- Title: Fairness for Servicemembers and their Families Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 385
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-03-31T20:15:46Z
- Update date including text: 2026-03-31T20:15:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/385",
    "number": "385",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Fairness for Servicemembers and their Families Act of 2025",
    "type": "S",
    "updateDate": "2026-03-31T20:15:46Z",
    "updateDateIncludingText": "2026-03-31T20:15:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T18:13:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NH"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "AZ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s385is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 385\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Cornyn (for himself, Ms. Hassan , Mr. Cruz , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to periodically review the automatic maximum coverage under the Servicemembers\u2019 Group Life Insurance program and the Veterans\u2019 Group Life Insurance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness for Servicemembers and their Families Act of 2025 .\n#### 2. Periodic review of automatic maximum coverage under Servicemembers\u2019 Group Life Insurance and Veterans\u2019 Group Life insurance\n##### (a) In general\nSubchapter III of chapter 19 of title 38, United States Code, is amended by adding at the end the following new section:\n1980B. Periodic review of automatic maximum coverage (a) In general On January 1, 2026, and every five years thereafter, the Secretary shall\u2014 (1) complete a review of how the amount specified in section 1967(a)(3)(A)(i) compares to the amount described in subsection (b); and (2) submit to the Committees on Veterans' Affairs of the House of Representatives and the Senate the results of the review, which may serve as a guide for coverage increases within the existing administrative incremental structure. (b) Amount described The amount described in this subsection is the amount equal to\u2014 (1) $500,000; multiplied by (2) the average percentage by which the Consumer Price Index changed during the five fiscal years preceding the review under subsection (a). (c) Consumer Price Index defined In this section, the term Consumer Price Index means the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 19 of such title is amended by inserting after the item relating to section 1980A the following new item:\n1980B. Periodic review of automatic maximum coverage. .",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-12-12",
        "text": "Became Public Law No: 119-54."
      },
      "number": "970",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fairness for Servicemembers and their Families Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-08T13:57:41Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2025-04-08T13:57:41Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-04-08T13:57:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-23T15:28:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s385",
          "measure-number": "385",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s385v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fairness for Servicemembers and their Families Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to periodically review and report on the maximum coverage available under the\u00a0Servicemembers' Group Life Insurance and Veterans' Group Life Insurance programs. Specifically, the VA must review such coverage amount every five years, taking into account the average percentage by which the Consumer Price Index for All Urban Consumers (CPI-U) increased in the five fiscal years preceding the review.</p>"
        },
        "title": "Fairness for Servicemembers and their Families Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s385.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness for Servicemembers and their Families Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to periodically review and report on the maximum coverage available under the\u00a0Servicemembers' Group Life Insurance and Veterans' Group Life Insurance programs. Specifically, the VA must review such coverage amount every five years, taking into account the average percentage by which the Consumer Price Index for All Urban Consumers (CPI-U) increased in the five fiscal years preceding the review.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119s385"
    },
    "title": "Fairness for Servicemembers and their Families Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fairness for Servicemembers and their Families Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to periodically review and report on the maximum coverage available under the\u00a0Servicemembers' Group Life Insurance and Veterans' Group Life Insurance programs. Specifically, the VA must review such coverage amount every five years, taking into account the average percentage by which the Consumer Price Index for All Urban Consumers (CPI-U) increased in the five fiscal years preceding the review.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119s385"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s385is.xml"
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
      "title": "Fairness for Servicemembers and their Families Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fairness for Servicemembers and their Families Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to require the Secretary of Veterans Affairs to periodically review the automatic maximum coverage under the Servicemembers' Group Life Insurance program and the Veterans' Group Life Insurance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:25Z"
    }
  ]
}
```
