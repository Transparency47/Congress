# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/121
- Title: Supporting the designation of "Scouting America Day" in celebration of its 115th anniversary.
- Congress: 119
- Bill type: HRES
- Bill number: 121
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2026-04-08T00:34:48Z
- Update date including text: 2026-04-08T00:34:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-07 - Committee: Submitted in House
- 2025-02-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H589)
- Latest action: 2025-02-07: Submitted in House

## Actions

- 2025-02-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-07 - Committee: Submitted in House
- 2025-02-10 - IntroReferral: Sponsor introductory remarks on measure. (CR H589)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/121",
    "number": "121",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Supporting the designation of \"Scouting America Day\" in celebration of its 115th anniversary.",
    "type": "HRES",
    "updateDate": "2026-04-08T00:34:48Z",
    "updateDateIncludingText": "2026-04-08T00:34:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H589)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-07T14:00:10Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres121ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 121\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Thompson of Pennsylvania (for himself and Mr. Bishop ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the designation of Scouting America Day in celebration of its 115th anniversary.\nThat the House of Representatives supports the redesignation of a \u201cScouting America Day\u201d in celebration of the 115th anniversary of its incorporation.",
      "versionDate": "2025-02-07",
      "versionType": "IH"
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
        "actionDate": "2026-02-05",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1041",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the designation of \"Scouting America Day\" in celebration of its 116th anniversary.",
      "type": "HRES"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-04-24T16:18:58Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-04-24T16:18:53Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-04-24T16:19:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T19:24:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hres121",
          "measure-number": "121",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres121v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the redesignation of a Scouting America Day in celebration of the 115th anniversary of the incorporation of Scouting America (formerly known as Boy Scouts of America).</p>"
        },
        "title": "Supporting the designation of \"Scouting America Day\" in celebration of its 115th anniversary."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres121.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the redesignation of a Scouting America Day in celebration of the 115th anniversary of the incorporation of Scouting America (formerly known as Boy Scouts of America).</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hres121"
    },
    "title": "Supporting the designation of \"Scouting America Day\" in celebration of its 115th anniversary."
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the redesignation of a Scouting America Day in celebration of the 115th anniversary of the incorporation of Scouting America (formerly known as Boy Scouts of America).</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hres121"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres121ih.xml"
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
      "title": "Supporting the designation of \"Scouting America Day\" in celebration of its 115th anniversary.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T09:03:52Z"
    },
    {
      "title": "Supporting the designation of \"Scouting America Day\" in celebration of its 115th anniversary.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T09:01:47Z"
    }
  ]
}
```
