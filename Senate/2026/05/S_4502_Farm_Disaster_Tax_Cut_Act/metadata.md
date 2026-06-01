# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4502
- Title: Farm Disaster Tax Cut Act
- Congress: 119
- Bill type: S
- Bill number: 4502
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-28T20:31:01Z
- Update date including text: 2026-05-28T20:31:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4502",
    "number": "4502",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Farm Disaster Tax Cut Act",
    "type": "S",
    "updateDate": "2026-05-28T20:31:01Z",
    "updateDateIncludingText": "2026-05-28T20:31:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T19:35:08Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4502is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4502\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mr. Ossoff introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude crop insurance indemnity payments from gross income.\n#### 1. Short title\nThis Act may be cited as the Farm Disaster Tax Cut Act .\n#### 2. Crop insurance indemnity payments excluded from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139L the following new section:\n139M. Crop insurance indemnity payments (a) In general Gross income shall not include any crop insurance indemnity payment made pursuant to the Federal Crop Insurance Act ( 7 U.S.C. 1501 et seq. ). (b) Termination This section shall not apply to any payment for losses which occur after December 31, 2028. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Crop insurance indemnity payments. .\n##### (c) Effective date\nThe amendments made by this section shall apply to payments for losses which occur after August 5, 2024.",
      "versionDate": "2026-05-12",
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
        "updateDate": "2026-05-28T20:31:00Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4502is.xml"
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
      "title": "Farm Disaster Tax Cut Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farm Disaster Tax Cut Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude crop insurance indemnity payments from gross income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:03:24Z"
    }
  ]
}
```
