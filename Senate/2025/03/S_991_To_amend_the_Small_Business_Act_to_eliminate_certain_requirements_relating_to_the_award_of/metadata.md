# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/991?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/991
- Title: A bill to amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance.
- Congress: 119
- Bill type: S
- Bill number: 991
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-04-06T12:52:29Z
- Update date including text: 2026-04-06T12:52:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/991",
    "number": "991",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance.",
    "type": "S",
    "updateDate": "2026-04-06T12:52:29Z",
    "updateDateIncludingText": "2026-04-06T12:52:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T18:41:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "AK"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s991is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 991\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Sullivan (for himself, Ms. Murkowski , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance.\n#### 1. Elimination of requirement relating to award of construction subcontracts within county or State of performance\nParagraph (11) of section 8(a) of the Small Business Act ( 15 U.S.C. 637(a) ) is repealed.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-05-19",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "3485",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance.",
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
        "updateDate": "2025-03-31T12:31:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s991",
          "measure-number": "991",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s991v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill eliminates a requirement that, to the maximum extent practicable, certain construction subcontracts awarded by the Small Business Administration must be awarded within the county or state where the work is to be performed.</p>"
        },
        "title": "A bill to amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s991.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill eliminates a requirement that, to the maximum extent practicable, certain construction subcontracts awarded by the Small Business Administration must be awarded within the county or state where the work is to be performed.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s991"
    },
    "title": "A bill to amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance."
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill eliminates a requirement that, to the maximum extent practicable, certain construction subcontracts awarded by the Small Business Administration must be awarded within the county or state where the work is to be performed.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s991"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s991is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T10:48:20Z"
    },
    {
      "title": "A bill to amend the Small Business Act to eliminate certain requirements relating to the award of construction subcontracts within the county or State of performance.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T10:56:28Z"
    }
  ]
}
```
