# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/606?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/606
- Title: Supporting the goals and ideals of World Drowning Prevention Day.
- Congress: 119
- Bill type: HRES
- Bill number: 606
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-07T11:31:59Z
- Update date including text: 2026-04-07T11:31:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House
- Latest action: 2025-07-23: Submitted in House

## Actions

- 2025-07-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/606",
    "number": "606",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "O000173",
        "district": "5",
        "firstName": "Ilhan",
        "fullName": "Rep. Omar, Ilhan [D-MN-5]",
        "lastName": "Omar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Supporting the goals and ideals of World Drowning Prevention Day.",
    "type": "HRES",
    "updateDate": "2026-04-07T11:31:59Z",
    "updateDateIncludingText": "2026-04-07T11:31:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:10:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres606ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 606\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Omar (for herself and Ms. Wasserman Schultz ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nSupporting the goals and ideals of World Drowning Prevention Day.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of World Drowning Prevention Day to catalyze concrete action and generate attention globally for drowning prevention and improved water safety;\n**(2)**\nrecognizes the importance of this global advocacy event as an opportunity to highlight the tragic and profound impact of drowning on families and communities and offer lifesaving solutions to prevent it; and\n**(3)**\nencourages intergovernment cooperation to develop new drowning prevention policies, legislation, or investment, and to convene multisectoral roundtables or parliamentary discussions.",
      "versionDate": "2025-07-23",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-10T15:18:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hres606",
          "measure-number": "606",
          "measure-type": "hres",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres606v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the goals and ideals of World Drowning Prevention Day.</p>"
        },
        "title": "Supporting the goals and ideals of World Drowning Prevention Day."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres606.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the goals and ideals of World Drowning Prevention Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres606"
    },
    "title": "Supporting the goals and ideals of World Drowning Prevention Day."
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the goals and ideals of World Drowning Prevention Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres606"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres606ih.xml"
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
      "title": "Supporting the goals and ideals of World Drowning Prevention Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:33Z"
    },
    {
      "title": "Supporting the goals and ideals of World Drowning Prevention Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:06:34Z"
    }
  ]
}
```
