# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/5?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/5
- Title: A joint resolution directing the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress.
- Congress: 119
- Bill type: SJRES
- Bill number: 5
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-03-03T14:01:39Z
- Update date including text: 2025-03-03T14:01:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/5",
    "number": "5",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A joint resolution directing the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress.",
    "type": "SJRES",
    "updateDate": "2025-03-03T14:01:39Z",
    "updateDateIncludingText": "2025-03-03T14:01:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-23T16:51:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres5is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 5\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Paul introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nDirecting the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress.\n#### 1. Removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress\nPursuant to section 1013 of the Department of State Authorization Act, Fiscal Years 1984 and 1985 ( 50 U.S.C. 1546a ) and in accordance with the provisions of section 601(b) of the International Security Assistance and Arms Export Control Act of 1976 ( Public Law 94\u2013329 ; 90 Stat. 765), Congress hereby directs the President to remove United States Armed Forces from hostilities in or affecting Ukraine by not later than the date that is 30 days after the date of the adoption of this joint resolution (unless the President requests and Congress authorizes a later date), and unless and until a declaration of war or specific authorization for such use of United States Armed Forces has been enacted.\n#### 2. Rule of construction regarding authorizations for use of military force\nConsistent with section 8(a)(1) of the War Powers Resolution ( 50 U.S.C. 1547(a)(1) ), nothing in this joint resolution may be construed as authorizing the use of military force.",
      "versionDate": "2025-01-23",
      "versionType": "IS"
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
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "6",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A joint resolution directing the removal of United States Armed Forces from hostilities in Syria that have not been authorized by Congress.",
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
        "name": "International Affairs",
        "updateDate": "2025-01-27T22:55:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "Senate",
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
          "measure-id": "id119sjres5",
          "measure-number": "5",
          "measure-type": "sjres",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres5v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution directs the President to remove U.S. Armed Forces from hostilities in or affecting Ukraine within 30 days of this resolution's adoption unless a declaration of war or specific authorization for such use of the Armed Forces has been enacted.</p>"
        },
        "title": "A joint resolution directing the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres5.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution directs the President to remove U.S. Armed Forces from hostilities in or affecting Ukraine within 30 days of this resolution's adoption unless a declaration of war or specific authorization for such use of the Armed Forces has been enacted.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119sjres5"
    },
    "title": "A joint resolution directing the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution directs the President to remove U.S. Armed Forces from hostilities in or affecting Ukraine within 30 days of this resolution's adoption unless a declaration of war or specific authorization for such use of the Armed Forces has been enacted.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119sjres5"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres5is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution directing the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-25T05:03:43Z"
    },
    {
      "title": "A joint resolution directing the removal of United States Armed Forces from hostilities in Ukraine that have not been authorized by Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T11:56:29Z"
    }
  ]
}
```
