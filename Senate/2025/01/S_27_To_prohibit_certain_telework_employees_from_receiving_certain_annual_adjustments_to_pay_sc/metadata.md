# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/27?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/27
- Title: Federal Employee Return to Work Act
- Congress: 119
- Bill type: S
- Bill number: 27
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2025-05-14T17:27:07Z
- Update date including text: 2025-05-14T17:27:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/27",
    "number": "27",
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
    "title": "Federal Employee Return to Work Act",
    "type": "S",
    "updateDate": "2025-05-14T17:27:07Z",
    "updateDateIncludingText": "2025-05-14T17:27:07Z"
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
          "date": "2025-01-07T19:36:13Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s27is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 27\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Cassidy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit certain telework employees from receiving certain annual adjustments to pay schedules, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Employee Return to Work Act .\n#### 2. Definitions\nIn this Act:\n**(1) Covered employee**\nThe term covered employee \u2014\n**(A)**\nmeans an employee who teleworks not fewer than 1 day, or in the case of an alternative work schedule, not less than 20 percent, a week; and\n**(B)**\ndoes not include an employee who\u2014\n**(i)**\nteleworks not fewer than 1 day a week; and\n**(ii)**\nis\u2014\n**(I)**\nis disabled and receives reasonable accommodations;\n**(II)**\na member of the Foreign Service of the United States;\n**(III)**\na Federal law enforcement officer;\n**(IV)**\na member of the Armed Forces on active duty; or\n**(V)**\nany other employee, the official worksite of whom is not described in section 531.605(a)(1) of title 5, Code of Federal Regulations (or any corresponding similar regulation or ruling).\n**(2) Employee**\nThe term employee has the meaning given the term in section 2105 of title 5, United States Code.\n**(3) Telework**\nThe term telework has the meaning given the term in section 6501 of title 5, United States Code.\n#### 3. Annual adjustments to pay schedules\nNo covered employee may receive an annual adjustment under section 5303 of title 5, United States Code.\n#### 4. Pay localities\nEach covered employee shall be paid at the rate of basic pay under the applicable grade and step for that employee under the locality pay area designated as Rest of U.S. \u2014\n**(1)**\nas of the date on which the employee becomes a covered employee; and\n**(2)**\nwhich shall not be adjusted under section 5304 of title 5, United States Code.\n#### 5. Effective date\nThis Act shall take effect on the first day of the first full fiscal year beginning after the date of enactment of this Act.",
      "versionDate": "2025-01-07",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-07",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Employee Return to Work Act",
      "type": "HR"
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
            "name": "Commuting",
            "updateDate": "2025-03-05T16:07:14Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-05T16:07:14Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-05T16:07:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:05:41Z"
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
          "measure-id": "id119s27",
          "measure-number": "27",
          "measure-type": "s",
          "orig-publish-date": "2025-01-07",
          "originChamber": "SENATE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s27v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Federal Employee Return to Work Act</strong></p><p>This bill prohibits providing certain annual or locality-based\u00a0pay increases to teleworking federal employees.</p><p>Currently, federal law mandates annual adjustments to General Schedule (GS) pay rates according to (1) a formula based on the annual percentage change in the Employment Cost Index (a measure of labor costs in the private sector); and (2) the difference between public and private sector pay rates in an employee's locality, if that difference exceeds 5%. For example, in 2025, the default annual rate of pay for a GS-7 (step 1) employee is $49,960; the adjusted annual rate of pay for a GS-7 (step 1) employee in the locality pay area that includes Washington, DC, is $57,164.\u00a0</p><p>The bill makes executive agency employees who telework at least one\u00a0day each week (or, in the case of an alternative work schedule, 20% or more each week) ineligible for these\u00a0payments.</p><p>The bill is effective on the first day of the fiscal year beginning after the bill's enactment.\u00a0</p>"
        },
        "title": "Federal Employee Return to Work Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s27.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Employee Return to Work Act</strong></p><p>This bill prohibits providing certain annual or locality-based\u00a0pay increases to teleworking federal employees.</p><p>Currently, federal law mandates annual adjustments to General Schedule (GS) pay rates according to (1) a formula based on the annual percentage change in the Employment Cost Index (a measure of labor costs in the private sector); and (2) the difference between public and private sector pay rates in an employee's locality, if that difference exceeds 5%. For example, in 2025, the default annual rate of pay for a GS-7 (step 1) employee is $49,960; the adjusted annual rate of pay for a GS-7 (step 1) employee in the locality pay area that includes Washington, DC, is $57,164.\u00a0</p><p>The bill makes executive agency employees who telework at least one\u00a0day each week (or, in the case of an alternative work schedule, 20% or more each week) ineligible for these\u00a0payments.</p><p>The bill is effective on the first day of the fiscal year beginning after the bill's enactment.\u00a0</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s27"
    },
    "title": "Federal Employee Return to Work Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Employee Return to Work Act</strong></p><p>This bill prohibits providing certain annual or locality-based\u00a0pay increases to teleworking federal employees.</p><p>Currently, federal law mandates annual adjustments to General Schedule (GS) pay rates according to (1) a formula based on the annual percentage change in the Employment Cost Index (a measure of labor costs in the private sector); and (2) the difference between public and private sector pay rates in an employee's locality, if that difference exceeds 5%. For example, in 2025, the default annual rate of pay for a GS-7 (step 1) employee is $49,960; the adjusted annual rate of pay for a GS-7 (step 1) employee in the locality pay area that includes Washington, DC, is $57,164.\u00a0</p><p>The bill makes executive agency employees who telework at least one\u00a0day each week (or, in the case of an alternative work schedule, 20% or more each week) ineligible for these\u00a0payments.</p><p>The bill is effective on the first day of the fiscal year beginning after the bill's enactment.\u00a0</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s27"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s27is.xml"
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
      "title": "Federal Employee Return to Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Employee Return to Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain telework employees from receiving certain annual adjustments to pay schedules, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:28Z"
    }
  ]
}
```
