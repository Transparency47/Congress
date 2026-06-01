# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2864?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2864
- Title: Pathways to Paychecks Act
- Congress: 119
- Bill type: S
- Bill number: 2864
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-17T15:35:26Z
- Update date including text: 2025-12-17T15:35:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2864",
    "number": "2864",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
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
    "title": "Pathways to Paychecks Act",
    "type": "S",
    "updateDate": "2025-12-17T15:35:26Z",
    "updateDateIncludingText": "2025-12-17T15:35:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T16:24:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2864is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2864\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Cassidy introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Wagner-Peyser Act to allow States the flexibility to use staffing arrangements that best suit their needs, for employment service offices.\n#### 1. Short title\nThis Act may be cited as the Pathways to Paychecks Act .\n#### 2. Employment service offices\nSection 9 of the Wagner-Peyser Act ( 29 U.S.C. 49h ) is amended by adding at the end the following:\n(d) States may use State merit staff, or other staff that meet the requirements applicable to Federal contractors, to carry out the duties of employment service offices under this Act. .",
      "versionDate": "",
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
        "name": "Labor and Employment",
        "updateDate": "2025-12-17T15:35:25Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2864is.xml"
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
      "title": "Pathways to Paychecks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pathways to Paychecks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Wagner-Peyser Act to allow States the flexibility to use staffing arrangements that best suit their needs, for employment service offices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:26Z"
    }
  ]
}
```
