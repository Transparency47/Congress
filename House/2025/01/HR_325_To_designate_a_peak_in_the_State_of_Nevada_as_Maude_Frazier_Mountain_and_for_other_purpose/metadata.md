# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/325
- Title: To designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 325
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-03-27T21:02:30Z
- Update date including text: 2025-03-27T21:02:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/325",
    "number": "325",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "To designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-03-27T21:02:30Z",
    "updateDateIncludingText": "2025-03-27T21:02:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-09T14:30:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr325ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 325\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Titus introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes.\n#### 1. Designation of Maude Frazier Mountain in the State of Nevada\n##### (a) In general\nThe peak of Frenchman Mountain located at latitude 36\u00b010\u203245\u2033 N, by longitude 114\u00b059\u203252\u2033 W in the State of Nevada shall be known and designated as Maude Frazier Mountain .\n##### (b) References\nAny reference in a law, map, regulation, document, record, or other paper of the United States to the peak referred to in subsection (a) shall be deemed to be a reference to Maude Frazier Mountain .",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
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
            "name": "Congressional tributes",
            "updateDate": "2025-02-24T20:23:57Z"
          },
          {
            "name": "Nevada",
            "updateDate": "2025-02-24T20:23:57Z"
          },
          {
            "name": "Wilderness and natural areas, wildlife refuges, wild rivers, habitats",
            "updateDate": "2025-02-24T20:23:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-20T14:57:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr325",
          "measure-number": "325",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr325v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill designates the peak of Frenchman Mountain in Nevada as the Maude Frazier Mountain.</p>"
        },
        "title": "To designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr325.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates the peak of Frenchman Mountain in Nevada as the Maude Frazier Mountain.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr325"
    },
    "title": "To designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates the peak of Frenchman Mountain in Nevada as the Maude Frazier Mountain.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr325"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr325ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "title": "To designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:19Z"
    },
    {
      "title": "To designate a peak in the State of Nevada as Maude Frazier Mountain, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:59Z"
    }
  ]
}
```
