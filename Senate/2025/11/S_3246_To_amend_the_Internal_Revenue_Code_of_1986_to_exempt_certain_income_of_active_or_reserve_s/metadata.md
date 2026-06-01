# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3246?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3246
- Title: Service Members Tax Relief Act
- Congress: 119
- Bill type: S
- Bill number: 3246
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-19T14:59:39Z
- Update date including text: 2025-12-19T14:59:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3246",
    "number": "3246",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Service Members Tax Relief Act",
    "type": "S",
    "updateDate": "2025-12-19T14:59:39Z",
    "updateDateIncludingText": "2025-12-19T14:59:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T17:22:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3246is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3246\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Ricketts introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exempt certain income of active or reserve service members from tax.\n#### 1. Short title\nThis Act may be cited as the Service Members Tax Relief Act .\n#### 2. Exemption from income tax for uniformed service members\n##### (a) In general\nPart III of subchapter B of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after section 139L the following new section:\n139M. Certain income earned by uniformed service members (a) In general Gross income shall not include any compensation received by an individual in connection with such individual\u2019s service during the taxable year as an active or reserve member of the Uniformed Services of the United States. (b) Exclusion of retirement income For purposes of this section, the term compensation does not include any pension or retirement pay. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Certain income earned by uniformed service members. .\n##### (c) Effective date\nThe amendments made by this section shall apply to income earned in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Service Members Tax Relief Act",
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
        "name": "Taxation",
        "updateDate": "2025-12-18T15:58:52Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3246is.xml"
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
      "title": "Service Members Tax Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Service Members Tax Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exempt certain income of active or reserve service members from tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:13Z"
    }
  ]
}
```
