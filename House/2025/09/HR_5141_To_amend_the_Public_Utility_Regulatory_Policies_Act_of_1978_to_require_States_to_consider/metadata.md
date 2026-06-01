# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5141
- Title: Stop the Rate Hikes Act
- Congress: 119
- Bill type: HR
- Bill number: 5141
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-02-12T09:06:14Z
- Update date including text: 2026-02-12T09:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5141",
    "number": "5141",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stop the Rate Hikes Act",
    "type": "HR",
    "updateDate": "2026-02-12T09:06:14Z",
    "updateDateIncludingText": "2026-02-12T09:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-09-04T13:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5141ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5141\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Harder of California introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to require States to consider measures that limit the amount of retail utility rate increases a utility company can request to once every 365 days.\n#### 1. Short title\nThis Act may be cited as the Stop the Rate Hikes Act .\n#### 2. Consideration of measures to cap retail utility rate increases to once a year\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Cap on retail utility rate increases to once a year Each electric utility shall request no more than one rate increase once per year. .",
      "versionDate": "2025-09-04",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-09-23T17:20:34Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5141ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stop the Rate Hikes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop the Rate Hikes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to require States to consider measures that limit the amount of retail utility rate increases a utility company can request to once every 365 days.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:32Z"
    }
  ]
}
```
