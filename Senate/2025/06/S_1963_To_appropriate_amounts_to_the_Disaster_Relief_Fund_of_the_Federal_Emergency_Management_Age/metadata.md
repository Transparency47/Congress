# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1963?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1963
- Title: Emergency Disaster Relief Fund Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1963
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2025-07-30T21:48:27Z
- Update date including text: 2025-07-30T21:48:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1963",
    "number": "1963",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Emergency Disaster Relief Fund Act of 2025",
    "type": "S",
    "updateDate": "2025-07-30T21:48:27Z",
    "updateDateIncludingText": "2025-07-30T21:48:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:58:37Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1963is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1963\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Tillis introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo appropriate amounts to the Disaster Relief Fund of the Federal Emergency Management Agency.\n#### 1. Short title\nThis Act may be cited as the Emergency Disaster Relief Fund Act of 2025 .\n#### 2. Disaster relief fund\n##### (a) In general\nThere is appropriated, out of amounts in the Treasury not otherwise appropriated, $25,000,000,000 for fiscal year 2025 to the Administrator of the Federal Emergency Management Agency for the account entitled Federal Emergency Management Administration\u2014Disaster Relief Fund .\n##### (b) Emergency designation\n**(1) In general**\nThe amounts provided by this Act are designated as an emergency requirement pursuant to section 4(g) of the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 933(g) ).\n**(2) Designation in house and senate**\nThis Act is designated as being for an emergency requirement pursuant to section 4001(a)(1) of S. Con. Res. 14 (117th Congress), the concurrent resolution on the budget for fiscal year 2022, and to legislation establishing fiscal year 2025 budget enforcement in the House of Representatives.",
      "versionDate": "2025-06-05",
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
        "name": "Emergency Management",
        "updateDate": "2025-07-30T21:48:27Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1963is.xml"
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
      "title": "Emergency Disaster Relief Fund Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emergency Disaster Relief Fund Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate amounts to the Disaster Relief Fund of the Federal Emergency Management Agency.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:34:07Z"
    }
  ]
}
```
