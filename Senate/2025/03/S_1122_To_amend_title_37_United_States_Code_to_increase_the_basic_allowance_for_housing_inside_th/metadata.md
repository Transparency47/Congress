# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1122
- Title: BAH Restoration Act
- Congress: 119
- Bill type: S
- Bill number: 1122
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-05T21:48:10Z
- Update date including text: 2025-12-05T21:48:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1122",
    "number": "1122",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "BAH Restoration Act",
    "type": "S",
    "updateDate": "2025-12-05T21:48:10Z",
    "updateDateIncludingText": "2025-12-05T21:48:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T20:18:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1122is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1122\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Warnock introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 37, United States Code, to increase the basic allowance for housing inside the United States for members of the uniformed services.\n#### 1. Short title\nThis Act may be cited as the BAH Restoration Act .\n#### 2. Increase in basic allowance for housing inside the United States for members of the uniformed services\nParagraph (3) of section 403(b) of title 37, United States Code, is amended to read as follows:\n(3) The monthly amount of the basic allowance for housing for an area of the United States for a member of a uniformed service shall be the amount of the monthly cost of adequate housing in that area, as determined by the Secretary of Defense, for members of the uniformed services serving in the same pay grade and with the same dependency status as the member. .",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "1956",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BAH Restoration Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T19:15:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119s1122",
          "measure-number": "1122",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1122v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>BAH Restoration Act</strong></p><p>This bill increases the monthly amount of the basic housing allowance for members of the uniformed services inside the United States.</p><p>Specifically, the monthly amount of allowance for a member must be the amount of the monthly cost of adequate housing in the area, as determined by the Department of Defense, for members of the uniformed services serving in the same pay grade and same dependency status as the member. (Currently, the allowance is based on the difference between this amount and a percentage of the national average monthly cost of housing for members with the same pay grade and dependency status.)</p>"
        },
        "title": "BAH Restoration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1122.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>BAH Restoration Act</strong></p><p>This bill increases the monthly amount of the basic housing allowance for members of the uniformed services inside the United States.</p><p>Specifically, the monthly amount of allowance for a member must be the amount of the monthly cost of adequate housing in the area, as determined by the Department of Defense, for members of the uniformed services serving in the same pay grade and same dependency status as the member. (Currently, the allowance is based on the difference between this amount and a percentage of the national average monthly cost of housing for members with the same pay grade and dependency status.)</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119s1122"
    },
    "title": "BAH Restoration Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>BAH Restoration Act</strong></p><p>This bill increases the monthly amount of the basic housing allowance for members of the uniformed services inside the United States.</p><p>Specifically, the monthly amount of allowance for a member must be the amount of the monthly cost of adequate housing in the area, as determined by the Department of Defense, for members of the uniformed services serving in the same pay grade and same dependency status as the member. (Currently, the allowance is based on the difference between this amount and a percentage of the national average monthly cost of housing for members with the same pay grade and dependency status.)</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119s1122"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1122is.xml"
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
      "title": "BAH Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BAH Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 37, United States Code, to increase the basic allowance for housing inside the United States for members of the uniformed services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:24Z"
    }
  ]
}
```
