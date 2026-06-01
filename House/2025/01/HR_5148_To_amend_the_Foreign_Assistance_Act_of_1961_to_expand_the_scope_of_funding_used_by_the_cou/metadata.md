# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5148
- Title: Coordinated Counterterrorism Act
- Congress: 119
- Bill type: HR
- Bill number: 5148
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2025-09-11T21:29:50Z
- Update date including text: 2025-09-11T21:29:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5148",
    "number": "5148",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Coordinated Counterterrorism Act",
    "type": "HR",
    "updateDate": "2025-09-11T21:29:50Z",
    "updateDateIncludingText": "2025-09-11T21:29:50Z"
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
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
          "date": "2025-09-04T13:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5148ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5148\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Foreign Assistance Act of 1961 to expand the scope of funding used by the counterterrorism bureau of the Department of State to allow assistance to be made available to counterterrorism-focused military and intelligence units.\n#### 1. Short title\nThis Act may be cited as the Coordinated Counterterrorism Act .\n#### 2. Expansion of antiterrorism assistance\nSection 571 of the Foreign Assistance Act of 1961 (22 U.S.C. 2349aa) is amended\u2014\n**(1)**\nby inserting , intelligence, and military after assistance to foreign countries in order to enhance the ability of their law enforcement ;\n**(2)**\nby inserting information sharing with United States law enforcement agencies, after Such assistance may include ; and\n**(3)**\nby inserting a comma after training services .",
      "versionDate": "",
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
        "name": "International Affairs",
        "updateDate": "2025-09-11T21:29:50Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5148ih.xml"
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
      "title": "Coordinated Counterterrorism Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Coordinated Counterterrorism Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Foreign Assistance Act of 1961 to expand the scope of funding used by the counterterrorism bureau of the Department of State to allow assistance to be made available to counterterrorism-focused military and intelligence units.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:24Z"
    }
  ]
}
```
