# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/34?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/34
- Title: Expressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity.
- Congress: 119
- Bill type: HCONRES
- Bill number: 34
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-03-27T01:45:01Z
- Update date including text: 2026-03-27T01:45:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House
- Latest action: 2025-05-29: Submitted in House

## Actions

- 2025-05-29 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/34",
    "number": "34",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Expressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity.",
    "type": "HCONRES",
    "updateDate": "2026-03-27T01:45:01Z",
    "updateDateIncludingText": "2026-03-27T01:45:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:00:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres34ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 34\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Stansbury submitted the following concurrent resolution; which was referred to the Committee on Foreign Affairs\nCONCURRENT RESOLUTION\nExpressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity.\nThat it is in the national interest for the Senate to provide its advice and consent for the ratification of the Convention on Biological Diversity, which was signed by the United States in New York on June 4, 1993.",
      "versionDate": "2025-05-29",
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
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:24:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
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
          "measure-id": "id119hconres34",
          "measure-number": "34",
          "measure-type": "hconres",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres34v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This concurrent resolution expresses that it is in the national interest for the Senate to provide its advice and consent for the ratification of the Convention on Biological Diversity.</p>"
        },
        "title": "Expressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres34.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution expresses that it is in the national interest for the Senate to provide its advice and consent for the ratification of the Convention on Biological Diversity.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hconres34"
    },
    "title": "Expressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity."
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution expresses that it is in the national interest for the Senate to provide its advice and consent for the ratification of the Convention on Biological Diversity.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hconres34"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres34ih.xml"
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
      "title": "Expressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T09:18:15Z"
    },
    {
      "title": "Expressing the need for the Senate to provide advice and consent to ratification of the United Nations Convention on Biological Diversity.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T08:05:34Z"
    }
  ]
}
```
