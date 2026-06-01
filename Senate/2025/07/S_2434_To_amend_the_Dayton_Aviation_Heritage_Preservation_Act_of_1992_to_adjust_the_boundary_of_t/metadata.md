# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2434?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2434
- Title: A bill to amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2434
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-04-07T16:26:36Z
- Update date including text: 2026-04-07T16:26:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2434",
    "number": "2434",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A bill to amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes.",
    "type": "S",
    "updateDate": "2026-04-07T16:26:36Z",
    "updateDateIncludingText": "2026-04-07T16:26:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T16:27:43Z",
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
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2434is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2434\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Husted (for himself and Mr. Moreno ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes.\n#### 1. Dayton Aviation Heritage National Historical Park boundary adjustment\nSection 101 of the Dayton Aviation Heritage Preservation Act of 1992 ( 16 U.S.C. 410ww ) is amended by adding at the end the following:\n(d) Boundary adjustment In addition to the sites described in subsections (b) and (c), the boundary of the park is adjusted to include approximately 1 acre of land in Dayton, Ohio, depicted as Proposed Addition on the map entitled Dayton Aviation Heritage National Historical Park Proposed Boundary Addition and dated February 2023. .",
      "versionDate": "2025-07-24",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "4747",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes.",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:07:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-24",
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
          "measure-id": "id119s2434",
          "measure-number": "2434",
          "measure-type": "s",
          "orig-publish-date": "2025-07-24",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2434v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill adjusts the boundary of the Dayton Aviation Heritage National Historical Park to include approximately one acre of land in Dayton, Ohio.</p>"
        },
        "title": "A bill to amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2434.xml",
    "summary": {
      "actionDate": "2025-07-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill adjusts the boundary of the Dayton Aviation Heritage National Historical Park to include approximately one acre of land in Dayton, Ohio.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2434"
    },
    "title": "A bill to amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-07-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill adjusts the boundary of the Dayton Aviation Heritage National Historical Park to include approximately one acre of land in Dayton, Ohio.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2434"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2434is.xml"
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
      "title": "A bill to amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:32Z"
    },
    {
      "title": "A bill to amend the Dayton Aviation Heritage Preservation Act of 1992 to adjust the boundary of the Dayton Aviation Heritage National Historical Park, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T10:56:20Z"
    }
  ]
}
```
