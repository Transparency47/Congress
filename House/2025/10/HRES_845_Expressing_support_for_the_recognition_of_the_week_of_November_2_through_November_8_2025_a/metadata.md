# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/845?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/845
- Title: Expressing support for the recognition of the week of November 2 through November 8, 2025, as "Drowsy Driving Prevention Week".
- Congress: 119
- Bill type: HRES
- Bill number: 845
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-04-03T16:23:07Z
- Update date including text: 2026-04-03T16:23:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-11-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-10-31: Submitted in House

## Actions

- 2025-10-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-11-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/845",
    "number": "845",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000631",
        "district": "4",
        "firstName": "Madeleine",
        "fullName": "Rep. Dean, Madeleine [D-PA-4]",
        "lastName": "Dean",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Expressing support for the recognition of the week of November 2 through November 8, 2025, as \"Drowsy Driving Prevention Week\".",
    "type": "HRES",
    "updateDate": "2026-04-03T16:23:07Z",
    "updateDateIncludingText": "2026-04-03T16:23:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-01",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-01T17:03:25Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres845ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 845\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Ms. Dean of Pennsylvania (for herself and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing support for the recognition of the week of November 2 through November 8, 2025, as Drowsy Driving Prevention Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Drowsy Driving Prevention Week to raise awareness about the dangers of drowsy driving; and\n**(2)**\nencourages people across the United States to take preventable steps against drowsy driving.",
      "versionDate": "2025-10-31",
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
        "updateDate": "2025-11-25T18:53:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-31",
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
          "measure-id": "id119hres845",
          "measure-number": "845",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-31",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres845v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-10-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution (1) supports the designation of Drowsy Driving Prevention Week to raise awareness about the dangers of drowsy driving, and (2) encourages people across the United States to take preventable steps against drowsy driving.</p>"
        },
        "title": "Expressing support for the recognition of the week of November 2 through November 8, 2025, as \"Drowsy Driving Prevention Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres845.xml",
    "summary": {
      "actionDate": "2025-10-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution (1) supports the designation of Drowsy Driving Prevention Week to raise awareness about the dangers of drowsy driving, and (2) encourages people across the United States to take preventable steps against drowsy driving.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres845"
    },
    "title": "Expressing support for the recognition of the week of November 2 through November 8, 2025, as \"Drowsy Driving Prevention Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution (1) supports the designation of Drowsy Driving Prevention Week to raise awareness about the dangers of drowsy driving, and (2) encourages people across the United States to take preventable steps against drowsy driving.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres845"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres845ih.xml"
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
      "title": "Expressing support for the recognition of the week of November 2 through November 8, 2025, as \"Drowsy Driving Prevention Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-04T06:33:16Z"
    },
    {
      "title": "Expressing support for the recognition of the week of November 2 through November 8, 2025, as \"Drowsy Driving Prevention Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-01T08:05:59Z"
    }
  ]
}
```
