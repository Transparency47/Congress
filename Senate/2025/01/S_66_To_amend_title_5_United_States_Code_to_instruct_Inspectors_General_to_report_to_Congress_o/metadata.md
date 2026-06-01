# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/66?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/66
- Title: Transparency in Bureaucratic Communications Act
- Congress: 119
- Bill type: S
- Bill number: 66
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/66",
    "number": "66",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Transparency in Bureaucratic Communications Act",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T21:16:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s66is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 66\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 5, United States Code, to instruct Inspectors General to report to Congress on social media communications.\n#### 1. Short title\nThis Act may be cited as the Transparency in Bureaucratic Communications Act .\n#### 2. Inspector General Act of 1978\nSection 405(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (21)(B), by striking and at the end;\n**(2)**\nin paragraph (22)(B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(23) a detailed description of the contents and particular circumstances of any communication, or attempted communication, between the establishment and any internet computer service, information content provider, or access software provider (as defined under section 230(f) of the Communications Act of 1934 ( 47 U.S.C. 230(f) ), including\u2014 (A) communications regarding content moderation (as described under section 230(c)(2) of the Communications Act of 1934 ( 47 U.S.C. 230(c)(2) ); (B) user content, including posts, photos, and videos; and (C) any other communications relating to the internet computer service, information content provider, or access software provider\u2019s data inputs, algorithms, modeling and simulation processes, analysis tools, or any related tool. .",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in Senate"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-08T14:14:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119s66",
          "measure-number": "66",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s66v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Transparency in Bureaucratic Communications Act</strong></p><p>This bill requires federal offices of inspectors general to include in their existing semiannual reports to Congress information about any communications between their department or agency and certain online platforms and services.\u00a0</p><p>Specifically, such reports must include details on the contents and circumstances of any communication or attempted communication with an internet platform, information content provider, or access software provider. Covered communications include those addressing specific online content, content moderation practices, and any other topic related to a platform's or service's data inputs, algorithms, modeling and simulation processes, analysis tools, or any related tool.\u00a0</p>"
        },
        "title": "Transparency in Bureaucratic Communications Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s66.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Transparency in Bureaucratic Communications Act</strong></p><p>This bill requires federal offices of inspectors general to include in their existing semiannual reports to Congress information about any communications between their department or agency and certain online platforms and services.\u00a0</p><p>Specifically, such reports must include details on the contents and circumstances of any communication or attempted communication with an internet platform, information content provider, or access software provider. Covered communications include those addressing specific online content, content moderation practices, and any other topic related to a platform's or service's data inputs, algorithms, modeling and simulation processes, analysis tools, or any related tool.\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119s66"
    },
    "title": "Transparency in Bureaucratic Communications Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Transparency in Bureaucratic Communications Act</strong></p><p>This bill requires federal offices of inspectors general to include in their existing semiannual reports to Congress information about any communications between their department or agency and certain online platforms and services.\u00a0</p><p>Specifically, such reports must include details on the contents and circumstances of any communication or attempted communication with an internet platform, information content provider, or access software provider. Covered communications include those addressing specific online content, content moderation practices, and any other topic related to a platform's or service's data inputs, algorithms, modeling and simulation processes, analysis tools, or any related tool.\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119s66"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s66is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Transparency in Bureaucratic Communications Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Transparency in Bureaucratic Communications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to instruct Inspectors General to report to Congress on social media communications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:20Z"
    }
  ]
}
```
