# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6202?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6202
- Title: Brand USA Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 6202
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-03-30T18:26:09Z
- Update date including text: 2026-03-30T18:26:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Appropriations.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6202",
    "number": "6202",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Brand USA Restoration Act",
    "type": "HR",
    "updateDate": "2026-03-30T18:26:09Z",
    "updateDateIncludingText": "2026-03-30T18:26:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6202ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6202\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Krishnamoorthi introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo appropriate funds to the Travel Promotion Fund to offset reductions to the Fund made by the One Big Beautiful Bill Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Brand USA Restoration Act .\n#### 2. Appropriation to Travel Promotion Fund\nThere are appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, $80,000,000, to be deposited into the Travel Promotion Fund established by subsection (d) of the Travel Promotion Act of 2009 ( 22 U.S.C. 2131(d) ).",
      "versionDate": "2025-11-20",
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
        "name": "Commerce",
        "updateDate": "2026-03-30T18:26:08Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6202ih.xml"
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
      "title": "Brand USA Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Brand USA Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To appropriate funds to the Travel Promotion Fund to offset reductions to the Fund made by the One Big Beautiful Bill Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T12:48:41Z"
    }
  ]
}
```
