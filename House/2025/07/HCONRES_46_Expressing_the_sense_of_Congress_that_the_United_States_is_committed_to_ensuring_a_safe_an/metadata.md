# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/46?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/46
- Title: Expressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate.
- Congress: 119
- Bill type: HCONRES
- Bill number: 46
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-06T20:08:30Z
- Update date including text: 2026-04-06T20:08:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Submitted in House
- 2025-07-23 - IntroReferral: Submitted in House
- Latest action: 2025-07-23: Submitted in House

## Actions

- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/46",
    "number": "46",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate.",
    "type": "HCONRES",
    "updateDate": "2026-04-06T20:08:30Z",
    "updateDateIncludingText": "2026-04-06T20:08:30Z"
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-07-23T14:10:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:10:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres46ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 46\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Thompson of California (for himself, Mr. Huffman , Mr. Morelle , and Mr. Thanedar ) submitted the following concurrent resolution; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nCONCURRENT RESOLUTION\nExpressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate.\nThat Congress\u2014\n**(1)**\nformally recognizes its obligation to future generations to restore a safe climate;\n**(2)**\ndeclares that climate restoration, along with achieving net-zero CO2 emissions, are climate policy priorities; and\n**(3)**\ncalls on the President, Secretary of State, and United States Ambassador to the United Nations to take actions that will restore the climate and stabilize greenhouse gas concentrations at preindustrial levels.",
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
        "updateDate": "2025-09-10T15:17:28Z"
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
          "measure-id": "id119hconres46",
          "measure-number": "46",
          "measure-type": "hconres",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres46v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution declares that climate restoration, along with achieving net-zero CO2 emissions, are climate policy priorities. It also urges the President, the Department of State, and the United Nations to take actions that will restore the climate and stabilize greenhouse gas concentrations at preindustrial levels.</p>"
        },
        "title": "Expressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres46.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution declares that climate restoration, along with achieving net-zero CO2 emissions, are climate policy priorities. It also urges the President, the Department of State, and the United Nations to take actions that will restore the climate and stabilize greenhouse gas concentrations at preindustrial levels.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hconres46"
    },
    "title": "Expressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate."
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution declares that climate restoration, along with achieving net-zero CO2 emissions, are climate policy priorities. It also urges the President, the Department of State, and the United Nations to take actions that will restore the climate and stabilize greenhouse gas concentrations at preindustrial levels.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hconres46"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres46ih.xml"
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
      "title": "Expressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:34Z"
    },
    {
      "title": "Expressing the sense of Congress that the United States is committed to ensuring a safe and healthy climate for future generations, and thus to restoring the climate.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:06:15Z"
    }
  ]
}
```
