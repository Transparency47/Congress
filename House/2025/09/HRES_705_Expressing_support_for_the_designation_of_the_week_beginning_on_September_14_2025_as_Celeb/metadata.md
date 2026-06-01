# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/705
- Title: Expressing support for the designation of the week beginning on September 14, 2025, as "Celebrate Community Week".
- Congress: 119
- Bill type: HRES
- Bill number: 705
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-04-07T16:29:04Z
- Update date including text: 2026-04-07T16:29:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H4301)
- Latest action: 2025-09-11: Submitted in House

## Actions

- 2025-09-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H4301)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/705",
    "number": "705",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
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
    "title": "Expressing support for the designation of the week beginning on September 14, 2025, as \"Celebrate Community Week\".",
    "type": "HRES",
    "updateDate": "2026-04-07T16:29:04Z",
    "updateDateIncludingText": "2026-04-07T16:29:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4301)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:00:05Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres705ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 705\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Thompson of Pennsylvania (for himself and Mr. Panetta ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of the week beginning on September 14, 2025, as Celebrate Community Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Celebrate Community Week;\n**(2)**\nrecognizes Kiwanis International, Lions Clubs International, Optimist International, and Rotary International for promoting community service and humanitarian assistance;\n**(3)**\nencourages Kiwanis International, Lions Clubs International, Optimist International, and Rotary International to continue to emphasize the values of community service and improving the community for all individuals, especially our youth;\n**(4)**\napplauds Kiwanis International, Lions Clubs International, Optimist International, and Rotary International for instilling in young people the value of community service; and\n**(5)**\nappreciates Kiwanis International, Lions Clubs International, Optimist International, and Rotary International for the work of their members to continue to strengthen our communities through service.",
      "versionDate": "2025-09-11",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-09-24T13:40:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-11",
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
          "measure-id": "id119hres705",
          "measure-number": "705",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-11",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres705v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-09-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of Celebrate Community Week. </p>"
        },
        "title": "Expressing support for the designation of the week beginning on September 14, 2025, as \"Celebrate Community Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres705.xml",
    "summary": {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Celebrate Community Week. </p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres705"
    },
    "title": "Expressing support for the designation of the week beginning on September 14, 2025, as \"Celebrate Community Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Celebrate Community Week. </p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres705"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres705ih.xml"
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
      "title": "Expressing support for the designation of the week beginning on September 14, 2025, as \"Celebrate Community Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T08:18:24Z"
    },
    {
      "title": "Expressing support for the designation of the week beginning on September 14, 2025, as \"Celebrate Community Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T08:07:15Z"
    }
  ]
}
```
