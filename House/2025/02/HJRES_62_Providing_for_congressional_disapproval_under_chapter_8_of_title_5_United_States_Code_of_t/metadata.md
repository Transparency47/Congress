# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/62?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/62
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to "Protection of Marine Archaeological Resources".
- Congress: 119
- Bill type: HJRES
- Bill number: 62
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-07-02T22:01:45Z
- Update date including text: 2025-07-02T22:01:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/62",
    "number": "62",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to \"Protection of Marine Archaeological Resources\".",
    "type": "HJRES",
    "updateDate": "2025-07-02T22:01:45Z",
    "updateDateIncludingText": "2025-07-02T22:01:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:01:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "OK"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres62ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 62\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Ezell submitted the following joint resolution; which was referred to the Committee on Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to Protection of Marine Archaeological Resources .\nThat Congress disapproves the rule submitted by the Bureau of Ocean Energy Management relating to Protection of Marine Archaeological Resources (89 Fed. Reg. 71160 (September 3, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-03-14",
        "text": "Became Public Law No: 119-3."
      },
      "number": "11",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to \"Protection of Marine Archaeological Resources\".",
      "type": "SJRES"
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
        "updateDate": "2025-03-01T17:10:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hjres62",
          "measure-number": "62",
          "measure-type": "hjres",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres62v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the\u00a0final rule issued by the Bureau of Ocean Energy Management (BOEM) titled <em>Protection of Marine Archaeological\u00a0</em><em>Resources</em> and published on September 3, 2024. </p><p>The rule requires operators and\u00a0lessees conducting oil and gas exploration or development on the Outer Continental Shelf and that are seeking BOEM approval for such activities to also provide BOEM with an archaeological report for the area of potential effects.\u00a0The report must identify potential archaeological resources (material remains of human life or activities that are at least 50 years old and that are of archaeological interest) on the sea floor. The rule modified regulations that only required such a report when a\u00a0BOEM regional director has reason to believe that an archaeological resource may be present in the lease area.\u00a0</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to \"Protection of Marine Archaeological Resources\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres62.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the\u00a0final rule issued by the Bureau of Ocean Energy Management (BOEM) titled <em>Protection of Marine Archaeological\u00a0</em><em>Resources</em> and published on September 3, 2024. </p><p>The rule requires operators and\u00a0lessees conducting oil and gas exploration or development on the Outer Continental Shelf and that are seeking BOEM approval for such activities to also provide BOEM with an archaeological report for the area of potential effects.\u00a0The report must identify potential archaeological resources (material remains of human life or activities that are at least 50 years old and that are of archaeological interest) on the sea floor. The rule modified regulations that only required such a report when a\u00a0BOEM regional director has reason to believe that an archaeological resource may be present in the lease area.\u00a0</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hjres62"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to \"Protection of Marine Archaeological Resources\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the\u00a0final rule issued by the Bureau of Ocean Energy Management (BOEM) titled <em>Protection of Marine Archaeological\u00a0</em><em>Resources</em> and published on September 3, 2024. </p><p>The rule requires operators and\u00a0lessees conducting oil and gas exploration or development on the Outer Continental Shelf and that are seeking BOEM approval for such activities to also provide BOEM with an archaeological report for the area of potential effects.\u00a0The report must identify potential archaeological resources (material remains of human life or activities that are at least 50 years old and that are of archaeological interest) on the sea floor. The rule modified regulations that only required such a report when a\u00a0BOEM regional director has reason to believe that an archaeological resource may be present in the lease area.\u00a0</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hjres62"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres62ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to \"Protection of Marine Archaeological Resources\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-27T09:18:17Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Ocean Energy Management relating to \"Protection of Marine Archaeological Resources\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-27T09:06:29Z"
    }
  ]
}
```
