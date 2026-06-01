# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/165
- Title: A resolution expressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded.
- Congress: 119
- Bill type: SRES
- Bill number: 165
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-02-04T04:11:37Z
- Update date including text: 2026-02-04T04:11:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S2528)
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S2528)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/165",
    "number": "165",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "A resolution expressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded.",
    "type": "SRES",
    "updateDate": "2026-02-04T04:11:37Z",
    "updateDateIncludingText": "2026-02-04T04:11:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Veterans' Affairs. (text: CR S2528)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T17:59:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres165is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 165\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Sanders submitted the following resolution; which was referred to the Committee on Veterans' Affairs\nRESOLUTION\nExpressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded.\nThat it is the sense of the Senate that the Department of Veterans Affairs must immediately reject and rescind its Agency Reduction in Force and Reorganization Plan.",
      "versionDate": "2025-04-09",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T20:11:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119sres165",
          "measure-number": "165",
          "measure-type": "sres",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres165v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses the sense of the Senate that the Department of Veterans Affairs must immediately reject and rescind its Agency Reduction in Force and Reorganization Plan.</p>"
        },
        "title": "A resolution expressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres165.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses the sense of the Senate that the Department of Veterans Affairs must immediately reject and rescind its Agency Reduction in Force and Reorganization Plan.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119sres165"
    },
    "title": "A resolution expressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded."
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses the sense of the Senate that the Department of Veterans Affairs must immediately reject and rescind its Agency Reduction in Force and Reorganization Plan.</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119sres165"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres165is.xml"
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
      "title": "A resolution expressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:17Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate that the plan of President Trump and Elon Musk to fire 83,000 employees of the Department of Veterans Affairs is unacceptable and must be rescinded.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T10:56:21Z"
    }
  ]
}
```
