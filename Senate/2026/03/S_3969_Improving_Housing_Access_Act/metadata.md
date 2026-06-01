# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3969?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3969
- Title: Improving Housing Access Act
- Congress: 119
- Bill type: S
- Bill number: 3969
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-03-20T18:27:23Z
- Update date including text: 2026-03-20T18:27:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3969",
    "number": "3969",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
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
    "title": "Improving Housing Access Act",
    "type": "S",
    "updateDate": "2026-03-20T18:27:23Z",
    "updateDateIncludingText": "2026-03-20T18:27:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:20:07Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3969is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3969\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Ricketts introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo direct the Comptroller General of the United States to conduct a study that identifies options to remove barriers and improve housing for persons who are elderly or disabled.\n#### 1. Short title\nThis Act may be cited as the Improving Housing Access Act .\n#### 2. Improving housing for the elderly and disabled\nThe Comptroller General of the United States shall, not later than 1 year after the date of the enactment of this section, conduct a study that identifies options to remove barriers and improve housing for persons who are elderly or disabled, including any potential impacts of providing capital advances for\u2014\n**(1)**\nthe program for supportive housing for the elderly under section 202 of the Housing Act of 1959; and\n**(2)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act.",
      "versionDate": "",
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
        "actionDate": "2026-02-17",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "7596",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Housing Access Act",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-03-20T18:27:22Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3969is.xml"
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
      "title": "Improving Housing Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Housing Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Comptroller General of the United States to conduct a study that identifies options to remove barriers and improve housing for persons who are elderly or disabled.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:17Z"
    }
  ]
}
```
