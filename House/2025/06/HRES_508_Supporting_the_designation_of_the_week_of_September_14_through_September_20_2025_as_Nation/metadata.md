# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/508
- Title: Supporting the designation of the week of September 14 through September 20, 2025, as "National Truck Driver Appreciation Week".
- Congress: 119
- Bill type: HRES
- Bill number: 508
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-08-18T11:58:12Z
- Update date including text: 2025-08-18T11:58:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-12 - IntroReferral: Submitted in House
- 2025-06-12 - IntroReferral: Submitted in House
- Latest action: 2025-06-12: Submitted in House

## Actions

- 2025-06-12 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-12 - IntroReferral: Submitted in House
- 2025-06-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/508",
    "number": "508",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Supporting the designation of the week of September 14 through September 20, 2025, as \"National Truck Driver Appreciation Week\".",
    "type": "HRES",
    "updateDate": "2025-08-18T11:58:12Z",
    "updateDateIncludingText": "2025-08-18T11:58:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres508ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 508\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Bost (for himself and Mr. Carbajal ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the designation of the week of September 14 through September 20, 2025, as National Truck Driver Appreciation Week .\nThat the House of Representatives supports the designation of National Truck Driver Appreciation Week .",
      "versionDate": "2025-06-12",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-27T13:19:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119hres508",
          "measure-number": "508",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-12",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres508v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Truck Driver Appreciation Week.</p>"
        },
        "title": "Supporting the designation of the week of September 14 through September 20, 2025, as \"National Truck Driver Appreciation Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres508.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Truck Driver Appreciation Week.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres508"
    },
    "title": "Supporting the designation of the week of September 14 through September 20, 2025, as \"National Truck Driver Appreciation Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Truck Driver Appreciation Week.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres508"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres508ih.xml"
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
      "title": "Supporting the designation of the week of September 14 through September 20, 2025, as \"National Truck Driver Appreciation Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T12:48:16Z"
    },
    {
      "title": "Supporting the designation of the week of September 14 through September 20, 2025, as \"National Truck Driver Appreciation Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T08:06:19Z"
    }
  ]
}
```
