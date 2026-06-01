# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/40?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/40
- Title: A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.
- Congress: 119
- Bill type: SJRES
- Bill number: 40
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-07-01T14:13:19Z
- Update date including text: 2025-07-01T14:13:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/40",
    "number": "40",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.",
    "type": "SJRES",
    "updateDate": "2025-07-01T14:13:19Z",
    "updateDateIncludingText": "2025-07-01T14:13:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T16:58:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres40is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 40\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Sanders introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed export of certain defense articles to Israel.\nThat the following proposed export to Israel is prohibited:\n**(1)**\nThe export of the following firearms, parts, and components controlled under Category I of the United States Munitions List in the amount of $1,000,000 or more and described in Transmittal No. DDTC 23\u2013085, which was submitted to Congress pursuant to section 36(c) of the Arms Export Control Act ( 22 U.S.C. 2776(c) ) and communication of which was published in the Congressional Record on March 24, 2025 (Executive Communication 511): 2,300 Colt M4 carbine, 11.5\u201d barrel length, 5.56mm caliber, fully automatic rifles to M.R.D. Efram Investments Ltd in Israel for ultimate end use by the Israel National Police.",
      "versionDate": "2025-03-27",
      "versionType": "IS"
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
        "updateDate": "2025-05-19T18:21:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119sjres40",
          "measure-number": "40",
          "measure-type": "sjres",
          "orig-publish-date": "2025-03-27",
          "originChamber": "SENATE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres40v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution prohibits a proposed export of certain firearms, parts, and components to Israel.</p>"
        },
        "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres40.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits a proposed export of certain firearms, parts, and components to Israel.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119sjres40"
    },
    "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel."
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution prohibits a proposed export of certain firearms, parts, and components to Israel.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119sjres40"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres40is.xml"
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
      "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:24Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval of the proposed export of certain defense articles to Israel.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T10:56:29Z"
    }
  ]
}
```
