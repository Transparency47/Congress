# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3530?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3530
- Title: Strategic Resources Non-discrimination Act
- Congress: 119
- Bill type: S
- Bill number: 3530
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-14T16:23:33Z
- Update date including text: 2026-01-14T16:23:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3530",
    "number": "3530",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Strategic Resources Non-discrimination Act",
    "type": "S",
    "updateDate": "2026-01-14T16:23:33Z",
    "updateDateIncludingText": "2026-01-14T16:23:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T18:48:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3530is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3530\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Cramer introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Defense Production Act of 1950 to prohibit discrimination based on energy source in the use of certain authorities under title I and title III of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategic Resources Non-discrimination Act .\n#### 2. Limitations on certain authorities under the Defense Production Act of 1950\n##### (a) Domestic energy supplies\nSection 101(c)(1) of the Defense Production Act of 1950 ( 50 U.S.C. 4511(c)(1) ) is amended by inserting , other than for purposes of environmental protection, after domestic energy supplies .\n##### (b) Prohibition on discrimination based on industry\nTitle III of the Defense Production Act of 1950 ( 50 U.S.C. 4531 et seq. ) is amended by adding at the end the following:\n306. Prohibition on discrimination based on energy source In using the authorities under this title, the President may not deny financial support pursuant to sections 301, 302, or 303, other than for the production of energy, based on engagement by a person in the exploration, development, production, utilization, transportation, or sale of fossil fuel-based energy. .",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-08-01",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4835",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strategic Resources Non-discrimination Act",
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
        "name": "Energy",
        "updateDate": "2026-01-14T16:23:33Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3530is.xml"
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
      "title": "Strategic Resources Non-discrimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strategic Resources Non-discrimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Defense Production Act of 1950 to prohibit discrimination based on energy source in the use of certain authorities under title I and title III of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-13T05:48:22Z"
    }
  ]
}
```
