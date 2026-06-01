# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1013?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1013
- Title: CAPE Canaveral Act
- Congress: 119
- Bill type: S
- Bill number: 1013
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-12-06T07:09:39Z
- Update date including text: 2025-12-06T07:09:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1013",
    "number": "1013",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CAPE Canaveral Act",
    "type": "S",
    "updateDate": "2025-12-06T07:09:39Z",
    "updateDateIncludingText": "2025-12-06T07:09:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T14:58:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1013is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1013\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mrs. Moody (for herself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the headquarters of the National Aeronautics and Space Administration to be transferred to Brevard County, Florida.\n#### 1. Short title\nThis Act may be cited as the Consolidating Aerospace Programs Efficiently at Canaveral Act or CAPE Canaveral Act .\n#### 2. Transfer of National Aeronautics and Space Administration headquarters to Brevard County, Florida\nNot later than 1 year after the date of the enactment of this Act, the headquarters of the National Aeronautics and Space Administration shall be transferred to Brevard County, Florida.",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "2422",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CAPE Canaveral Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-31T13:46:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1013",
          "measure-number": "1013",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1013v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Consolidating Aerospace Programs Efficiently at Canaveral Act or the CAPE Canaveral Act</strong></p><p>This bill requires the headquarters of the National Aeronautics and Space Administration to be relocated to Brevard County, Florida within one year of the bill\u2019s enactment.\u00a0</p>"
        },
        "title": "CAPE Canaveral Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1013.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Consolidating Aerospace Programs Efficiently at Canaveral Act or the CAPE Canaveral Act</strong></p><p>This bill requires the headquarters of the National Aeronautics and Space Administration to be relocated to Brevard County, Florida within one year of the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s1013"
    },
    "title": "CAPE Canaveral Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Consolidating Aerospace Programs Efficiently at Canaveral Act or the CAPE Canaveral Act</strong></p><p>This bill requires the headquarters of the National Aeronautics and Space Administration to be relocated to Brevard County, Florida within one year of the bill\u2019s enactment.\u00a0</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s1013"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1013is.xml"
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
      "title": "CAPE Canaveral Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T11:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CAPE Canaveral Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Consolidating Aerospace Programs Efficiently at Canaveral Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-28T11:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the headquarters of the National Aeronautics and Space Administration to be transferred to Brevard County, Florida.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:20Z"
    }
  ]
}
```
