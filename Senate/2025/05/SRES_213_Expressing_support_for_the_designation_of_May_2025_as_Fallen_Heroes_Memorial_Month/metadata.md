# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/213
- Title: A resolution expressing support for the designation of May 2025 as "Fallen Heroes Memorial Month".
- Congress: 119
- Bill type: SRES
- Bill number: 213
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-08-08T16:42:47Z
- Update date including text: 2025-08-08T16:42:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S2844)
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Referred to the Committee on Veterans' Affairs. (text: CR S2844)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/213",
    "number": "213",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "A resolution expressing support for the designation of May 2025 as \"Fallen Heroes Memorial Month\".",
    "type": "SRES",
    "updateDate": "2025-08-08T16:42:47Z",
    "updateDateIncludingText": "2025-08-08T16:42:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Veterans' Affairs. (text: CR S2844)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T19:45:43Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres213is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 213\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Tuberville submitted the following resolution; which was referred to the Committee on Veterans\u2019 Affairs\nRESOLUTION\nExpressing support for the designation of May 2025 as Fallen Heroes Memorial Month .\nThat the Senate\u2014\n**(1)**\nhonors the more than 1,300,000 veterans who gave their lives in service to the United States;\n**(2)**\nrecognizes the families and loved ones of the fallen heroes of the United States and lifts them up in prayer;\n**(3)**\nurges the people of the United States to reflect on the contributions of those heroes and to honor the memory of those who paid the ultimate sacrifice in securing the blessings of liberty for the United States; and\n**(4)**\nrequests that the President issue a proclamation\u2014\n**(A)**\ndesignating May 2025 as Fallen Heroes Memorial Month ;\n**(B)**\naffirming the everlasting gratitude of the United States for members of the Armed Forces who made the ultimate sacrifice; and\n**(C)**\ncalling on the people of the United States to remember and honor the fallen heroes of the United States and to pay tribute to them through volunteering and supporting veteran service organizations.",
      "versionDate": "2025-05-08",
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
        "updateDate": "2025-06-03T19:35:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119sres213",
          "measure-number": "213",
          "measure-type": "sres",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2025-08-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres213v00",
            "update-date": "2025-08-08"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution honors the more than 1.3 million veterans who gave their lives in service to the United States and recognizes the families and loved ones of such veterans.</p><p>The resolution also requests that the President issue a proclamation designating May 2025 as Fallen Heroes Memorial Month.</p>"
        },
        "title": "A resolution expressing support for the designation of May 2025 as \"Fallen Heroes Memorial Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres213.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution honors the more than 1.3 million veterans who gave their lives in service to the United States and recognizes the families and loved ones of such veterans.</p><p>The resolution also requests that the President issue a proclamation designating May 2025 as Fallen Heroes Memorial Month.</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119sres213"
    },
    "title": "A resolution expressing support for the designation of May 2025 as \"Fallen Heroes Memorial Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution honors the more than 1.3 million veterans who gave their lives in service to the United States and recognizes the families and loved ones of such veterans.</p><p>The resolution also requests that the President issue a proclamation designating May 2025 as Fallen Heroes Memorial Month.</p>",
      "updateDate": "2025-08-08",
      "versionCode": "id119sres213"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres213is.xml"
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
      "title": "A resolution expressing support for the designation of May 2025 as \"Fallen Heroes Memorial Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:24Z"
    },
    {
      "title": "A resolution expressing support for the designation of May 2025 as \"Fallen Heroes Memorial Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T10:56:15Z"
    }
  ]
}
```
