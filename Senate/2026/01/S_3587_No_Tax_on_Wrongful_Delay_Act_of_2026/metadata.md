# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3587?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3587
- Title: No Tax on Wrongful Delay Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3587
- Origin chamber: Senate
- Introduced date: 2026-01-07
- Update date: 2026-02-10T00:30:23Z
- Update date including text: 2026-02-10T00:30:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in Senate
- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-07: Introduced in Senate

## Actions

- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3587",
    "number": "3587",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "No Tax on Wrongful Delay Act of 2026",
    "type": "S",
    "updateDate": "2026-02-10T00:30:23Z",
    "updateDateIncludingText": "2026-02-10T00:30:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T18:21:43Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3587is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3587\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2026 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an exemption from gross income for interest paid to taxpayers by the Internal Revenue Service following an audit or litigation in which the taxpayer prevailed.\n#### 1. Short title\nThis Act may be cited as the No Tax on Wrongful Delay Act of 2026 .\n#### 2. Exemption from gross income for interest paid to taxpayers following audit or litigation\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139M. Interest paid to taxpayers following an audit or litigation Gross income shall not include any interest which, pursuant to section 6611, is required to be paid upon any overpayment in respect of any internal revenue tax following\u2014 (1) an examination pursuant to the provisions of section 7602, (2) any suit or proceeding brought by the taxpayer for the credit or refund of taxes, or (3) any civil action commenced by the United States for the collection or recovery of taxes. .\n##### (b) Conforming amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 140 the following new item:\nSec. 139M. Interest paid to taxpayers following an audit or litigation. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-01-07",
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
        "name": "Taxation",
        "updateDate": "2026-02-10T00:30:23Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3587is.xml"
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
      "title": "No Tax on Wrongful Delay Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax on Wrongful Delay Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide an exemption from gross income for interest paid to taxpayers by the Internal Revenue Service following an audit or litigation in which the taxpayer prevailed.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T04:18:26Z"
    }
  ]
}
```
