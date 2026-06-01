# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4984
- Title: No Appointments by Rogue Judges Act
- Congress: 119
- Bill type: HR
- Bill number: 4984
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2025-09-19T15:33:11Z
- Update date including text: 2025-09-19T15:33:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4984",
    "number": "4984",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "No Appointments by Rogue Judges Act",
    "type": "HR",
    "updateDate": "2025-09-19T15:33:11Z",
    "updateDateIncludingText": "2025-09-19T15:33:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4984ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4984\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Ms. Mace introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, related to vacancies in offices of United States Attorneys, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Appointments by Rogue Judges Act .\n#### 2. Vacancies of United States Attorneys\nSection 546 of title 28, United States Code, is amended\u2014\n**(1)**\nby amending paragraph (2) of subsection (c) to read as follows:\n(2) the expiration of the time limitations in section 3346. ; and\n**(2)**\nby striking subsection (d).",
      "versionDate": "2025-08-15",
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
        "name": "Law",
        "updateDate": "2025-09-19T15:33:11Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4984ih.xml"
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
      "title": "No Appointments by Rogue Judges Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Appointments by Rogue Judges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, related to vacancies in offices of United States Attorneys, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T06:33:22Z"
    }
  ]
}
```
