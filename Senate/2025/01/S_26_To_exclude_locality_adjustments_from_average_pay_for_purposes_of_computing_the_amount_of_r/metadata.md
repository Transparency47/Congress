# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/26?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/26
- Title: A bill to exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees.
- Congress: 119
- Bill type: S
- Bill number: 26
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2025-04-14T14:01:36Z
- Update date including text: 2025-04-14T14:01:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in Senate
- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-07: Introduced in Senate

## Actions

- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/26",
    "number": "26",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A bill to exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees.",
    "type": "S",
    "updateDate": "2025-04-14T14:01:36Z",
    "updateDateIncludingText": "2025-04-14T14:01:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T19:35:11Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s26is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 26\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Cassidy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees.\n#### 1. Exclusion of locality adjustments from retirement annuities\nSection 8401 of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by inserting , which for a revised average pay employee shall exclude any locality-based comparability payments under section 5304 or 5304a, after rates of basic pay ;\n**(2)**\nin paragraph (38)(B), by striking and at the end;\n**(3)**\nin paragraph (39), by striking the period at the end and inserting ; and ; and\n**(4)**\nby adding at the end the following:\n(40) the term revised average pay employee means an individual who\u2014 (A) on the date of enactment of this paragraph\u2014 (i) is not an employee or Member covered under this chapter; (ii) is not performing civilian service which is creditable service under section 8411; and (iii) has not performed any civilian service which is creditable service under section 8411; and (B) after the date of enactment of this paragraph, becomes employed as an employee or becomes a Member covered under this chapter performing service which is creditable service under section 8411. .",
      "versionDate": "2025-01-07",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-02-12T19:27:41Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-02-12T19:27:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-06T16:59:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119s26",
          "measure-number": "26",
          "measure-type": "s",
          "orig-publish-date": "2025-01-07",
          "originChamber": "SENATE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s26v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill excludes locality-based comparability payments from the calculation of retirement and disability annuities for new employees in the Federal Employees\u2019 Retirement System. (General schedule and certain other federal employees receive locality-based comparability payments when their official worksite is located in a geographic area with a pay disparity between federal and non-federal workers of more than 5%.)</p>"
        },
        "title": "A bill to exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s26.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill excludes locality-based comparability payments from the calculation of retirement and disability annuities for new employees in the Federal Employees\u2019 Retirement System. (General schedule and certain other federal employees receive locality-based comparability payments when their official worksite is located in a geographic area with a pay disparity between federal and non-federal workers of more than 5%.)</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119s26"
    },
    "title": "A bill to exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees."
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill excludes locality-based comparability payments from the calculation of retirement and disability annuities for new employees in the Federal Employees\u2019 Retirement System. (General schedule and certain other federal employees receive locality-based comparability payments when their official worksite is located in a geographic area with a pay disparity between federal and non-federal workers of more than 5%.)</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119s26"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s26is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:23Z"
    },
    {
      "title": "A bill to exclude locality adjustments from average pay for purposes of computing the amount of retirement annuities of new employees.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-08T11:56:17Z"
    }
  ]
}
```
