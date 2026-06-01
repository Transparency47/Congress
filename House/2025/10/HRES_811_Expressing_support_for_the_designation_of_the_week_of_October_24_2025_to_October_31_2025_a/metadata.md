# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/811?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/811
- Title: Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as "Bat Week".
- Congress: 119
- Bill type: HRES
- Bill number: 811
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-04-09T11:49:14Z
- Update date including text: 2026-04-09T11:49:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-10-17 - IntroReferral: Submitted in House
- 2025-10-17 - IntroReferral: Submitted in House
- Latest action: 2025-10-17: Submitted in House

## Actions

- 2025-10-17 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-10-17 - IntroReferral: Submitted in House
- 2025-10-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/811",
    "number": "811",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "B001318",
        "district": "",
        "firstName": "Becca",
        "fullName": "Rep. Balint, Becca [D-VT-At Large]",
        "lastName": "Balint",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
    "type": "HRES",
    "updateDate": "2026-04-09T11:49:14Z",
    "updateDateIncludingText": "2026-04-09T11:49:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres811ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 811\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Ms. Balint submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nExpressing support for the designation of the week of October 24, 2025, to October 31, 2025, as Bat Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of Bat Week ;\n**(2)**\nencourages the observance of Bat Week with appropriate events and activities;\n**(3)**\nacknowledges the important role bats play as pollinators and pest control for agriculture; and\n**(4)**\nintends to\u2014\n**(A)**\ncontinue working to conserve bat species and their habitat; and\n**(B)**\nwork to defeat the disease known as white-nose syndrome.",
      "versionDate": "2025-10-17",
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
        "actionDate": "2025-10-28",
        "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7787)"
      },
      "number": "454",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
      "type": "SRES"
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-12-08T16:28:39Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-12-08T16:28:39Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-12-08T16:28:39Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-12-08T16:28:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-12-09T15:41:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-17",
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
          "measure-id": "id119hres811",
          "measure-number": "811",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres811v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-10-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of Bat\u00a0Week and acknowledges the important role bats play as pollinators and pest control for agriculture.</p>"
        },
        "title": "Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres811.xml",
    "summary": {
      "actionDate": "2025-10-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of Bat\u00a0Week and acknowledges the important role bats play as pollinators and pest control for agriculture.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hres811"
    },
    "title": "Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of Bat\u00a0Week and acknowledges the important role bats play as pollinators and pest control for agriculture.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hres811"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres811ih.xml"
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
      "title": "Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T08:18:13Z"
    },
    {
      "title": "Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T08:05:27Z"
    }
  ]
}
```
