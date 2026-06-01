# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/150
- Title: Terminating the national emergency declared to impose global tariffs.
- Congress: 119
- Bill type: HJRES
- Bill number: 150
- Origin chamber: House
- Introduced date: 2026-02-17
- Update date: 2026-02-19T20:07:38Z
- Update date including text: 2026-02-19T20:07:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-17: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-02-17: Introduced in House

## Actions

- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-17",
    "latestAction": {
      "actionDate": "2026-02-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/150",
    "number": "150",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Terminating the national emergency declared to impose global tariffs.",
    "type": "HJRES",
    "updateDate": "2026-02-19T20:07:38Z",
    "updateDateIncludingText": "2026-02-19T20:07:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-17",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-02-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-17",
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
          "date": "2026-02-17T16:00:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres150ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 150\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 17, 2026 Mr. Meeks submitted the following joint resolution; which was referred to the Committee on Foreign Affairs\nJOINT RESOLUTION\nTerminating the national emergency declared to impose global tariffs.\nThat, pursuant to section 202 of the National Emergencies Act ( 50 U.S.C. 1622 ), the national emergency declared on April 2, 2025, by the President in Executive Order 14257 (90 Fed. Reg. 15041) is terminated effective on the date of the enactment of this joint resolution.",
      "versionDate": "2026-02-17",
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
        "actionDate": "2025-04-30",
        "text": "Motion to table the motion to reconsider the vote by which S.J. Res. 49 failed of passage (Record Vote No. 225) agreed to in Senate by Yea-Nay Vote. 50 - 49. Record Vote Number: 226."
      },
      "number": "49",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution terminating the national emergency declared to impose global tariffs.",
      "type": "SJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-31",
        "actionTime": "13:15:26",
        "text": "Held at the desk."
      },
      "number": "88",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution terminating the national emergency declared to impose global tariffs.",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-02-19T18:48:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-17",
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
          "measure-id": "id119hjres150",
          "measure-number": "150",
          "measure-type": "hjres",
          "orig-publish-date": "2026-02-17",
          "originChamber": "HOUSE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres150v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2026-02-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution terminates the national emergency declared by President Donald J. Trump on April 2, 2025, which imposed a 10% tariff on most imports to the United States and additional duties on specified trading partners.</p>"
        },
        "title": "Terminating the national emergency declared to impose global tariffs."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres150.xml",
    "summary": {
      "actionDate": "2026-02-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution terminates the national emergency declared by President Donald J. Trump on April 2, 2025, which imposed a 10% tariff on most imports to the United States and additional duties on specified trading partners.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hjres150"
    },
    "title": "Terminating the national emergency declared to impose global tariffs."
  },
  "summaries": [
    {
      "actionDate": "2026-02-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution terminates the national emergency declared by President Donald J. Trump on April 2, 2025, which imposed a 10% tariff on most imports to the United States and additional duties on specified trading partners.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hjres150"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres150ih.xml"
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
      "title": "Terminating the national emergency declared to impose global tariffs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T09:18:27Z"
    },
    {
      "title": "Terminating the national emergency declared to impose global tariffs.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T09:05:49Z"
    }
  ]
}
```
