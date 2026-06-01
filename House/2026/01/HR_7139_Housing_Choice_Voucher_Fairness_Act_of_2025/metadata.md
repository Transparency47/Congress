# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7139
- Title: Housing Choice Voucher Fairness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 7139
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-01-20T14:26:00Z
- Update date including text: 2026-01-20T14:26:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7139",
    "number": "7139",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [R-CA-3]",
        "lastName": "Kiley",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Housing Choice Voucher Fairness Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-20T14:26:00Z",
    "updateDateIncludingText": "2026-01-20T14:26:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7139ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7139\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Kiley of California introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the United States Housing Act of 1937 to address the payment of tenant-based assistance in cases where a family moves, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Choice Voucher Fairness Act of 2025 .\n#### 2. Transferring housing choice voucher billing\nSection 8(r) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(r) ) is amended by adding at the end the following:\n(6) If an agency provides tenant-based assistance to a family on or after January 1, 2026 and such family moves to a dwelling unit located in an area outside of the area covered by such agency, such agency shall continue providing tenant-based assistance to such family unless the cost of providing rental assistance for such dwelling unit is greater than 10 percent more than the cost of providing rental assistance for such family when they lived in the area covered by such agency. .",
      "versionDate": "2026-01-16",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-01-20T14:25:59Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7139ih.xml"
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
      "title": "Housing Choice Voucher Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Choice Voucher Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the United States Housing Act of 1937 to address the payment of tenant-based assistance in cases where a family moves, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T09:18:20Z"
    }
  ]
}
```
