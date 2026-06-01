# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3066?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3066
- Title: Pay the People Act
- Congress: 119
- Bill type: S
- Bill number: 3066
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2026-03-30T18:56:00Z
- Update date including text: 2026-03-30T18:56:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3066",
    "number": "3066",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Pay the People Act",
    "type": "S",
    "updateDate": "2026-03-30T18:56:00Z",
    "updateDateIncludingText": "2026-03-30T18:56:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T21:44:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3066is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3066\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo appropriate funds for pay and allowances of Federal employees during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay the People Act .\n#### 2. Appropriations\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term agency means each authority of the executive, legislative, or judicial branch of the Government of the United States; and\n**(2)**\nthe term covered individual \u2014\n**(A)**\nmeans an employee of an agency; and\n**(B)**\nincludes\u2014\n**(i)**\na contractor who provides support to an employee described in subparagraph (A); and\n**(ii)**\na member of the Armed Forces on active duty.\n##### (b) Appropriations\nFor fiscal year 2026, and any fiscal year thereafter, for any period during which interim continuing appropriations or full-year appropriations for that fiscal year are not in effect for an agency, there are appropriated to the head of the agency, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to provide standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to covered individuals with respect to the agency.\n##### (c) Termination\nAppropriations and funds made available and authority granted under subsection (b) shall be available to the head of an agency until whichever of the following first occurs:\n**(1)**\nThe enactment into law of appropriations for the agency until the end of the applicable fiscal year (including a continuing appropriation) that provide amounts for the purposes for which amounts are made available under subsection (b).\n**(2)**\nThe enactment into law of appropriations for the agency until the end of the applicable fiscal year (including a continuing appropriation) without any appropriation for such purposes.\n##### (d) Interim continuing appropriations\nAppropriations made available under subsection (b) may not be obligated by the head of an agency during any period during which continuing appropriations for the purposes for which amounts are made available under subsection (b) are in effect for the agency.\n##### (e) Charging to full-Year appropriations\nObligations or expenditures made by the head of an agency pursuant to subsection (b) shall be charged to the applicable appropriation for the agency whenever a regular appropriation bill or a measure making continuing appropriations until the end of the applicable fiscal year for the agency becomes law.\n##### (f) Retroactive effective date\nThis Act shall take effect as if enacted on September 30, 2025.",
      "versionDate": "2025-10-28",
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
        "actionDate": "2025-11-07",
        "text": "Upon reconsideration, cloture on the motion to proceed to the measure not invoked in Senate by Yea-Nay Vote. 53 - 43. Record Vote Number: 609."
      },
      "number": "3012",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Fairness Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-21",
        "text": "Referred to the House Committee on Appropriations."
      },
      "number": "5801",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Fairness Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-30T18:56:00Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3066is.xml"
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
      "title": "Pay the People Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pay the People Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate funds for pay and allowances of Federal employees during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T06:18:18Z"
    }
  ]
}
```
