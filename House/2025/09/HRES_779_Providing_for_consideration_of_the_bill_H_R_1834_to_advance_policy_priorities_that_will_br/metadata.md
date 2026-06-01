# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/779?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/779
- Title: Providing for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.
- Congress: 119
- Bill type: HRES
- Bill number: 779
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-03-17T15:54:28Z
- Update date including text: 2026-03-17T15:54:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Rules.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House
- Latest action: 2025-09-30: Submitted in House

## Actions

- 2025-09-30 - IntroReferral: Referred to the House Committee on Rules.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/779",
    "number": "779",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000312",
        "district": "2",
        "firstName": "James",
        "fullName": "Rep. McGovern, James P. [D-MA-2]",
        "lastName": "McGovern",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Providing for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.",
    "type": "HRES",
    "updateDate": "2026-03-17T15:54:28Z",
    "updateDateIncludingText": "2026-03-17T15:54:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-09-30T16:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres779ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 779\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. McGovern submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.\nThat immediately upon adoption of this resolution, the House shall proceed to the consideration in the House of the bill (H.R. 1834) to advance policy priorities that will break the gridlock. All points of order against consideration of the bill are waived. An amendment in the nature of a substitute consisting of the text of H.R. 5450, as introduced, shall be considered as adopted. The bill, as amended, shall be considered as read. All points of order against provisions in the bill, as amended, are waived. The previous question shall be considered as ordered on the bill, as amended, and on any further amendment thereto, to final passage without intervening motion except: (1) one hour of debate equally divided and controlled by the chair and ranking minority member of the Committee on Appropriations or their respective designees; and (2) one motion to recommit.\n#### 2.\nClause 1(c) of rule XIX and clause 8 of rule XX shall not apply to the consideration of H.R. 1834.\n#### 3.\nThe Clerk shall transmit to the Senate a message that the House has passed H.R. 1834 no later than one calendar day after passage.",
      "versionDate": "2025-09-30",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2026-01-16T13:25:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
    "originChamber": "House",
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
          "measure-id": "id119hres779",
          "measure-number": "779",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres779v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "This resolution provides for the consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock."
        },
        "title": "Providing for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres779.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres779"
    },
    "title": "Providing for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "This resolution provides for the consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.",
      "updateDate": "2026-03-13",
      "versionCode": "id119hres779"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres779ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T08:48:28Z"
    },
    {
      "title": "Providing for consideration of the bill (H.R. 1834) to advance policy priorities that will break the gridlock.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:05:40Z"
    }
  ]
}
```
