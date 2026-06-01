# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4983?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4983
- Title: KOTEL Act
- Congress: 119
- Bill type: HR
- Bill number: 4983
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2025-09-11T20:54:31Z
- Update date including text: 2025-09-11T20:54:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4983",
    "number": "4983",
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
    "title": "KOTEL Act",
    "type": "HR",
    "updateDate": "2025-09-11T20:54:31Z",
    "updateDateIncludingText": "2025-09-11T20:54:31Z"
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
          "date": "2025-08-15T16:00:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4983ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4983\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo repeal a prohibition against the use of funds for site acquisition, development, or construction of any facility in Israel, Jerusalem, or the West Bank.\n#### 1. Short title\nThis Act may be cited as the Keeping Official Territories Eligible for Land-use Act or the KOTEL Act .\n#### 2. Repeal of prohibition\nSection 414 of the Omnibus Diplomatic Security and Antiterrorism Act of 1986 ( 22 U.S.C. 4862 ) is repealed.",
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
        "name": "International Affairs",
        "updateDate": "2025-09-11T20:54:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4983ih.xml"
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
      "title": "KOTEL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "KOTEL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T06:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keeping Official Territories Eligible for Land-use Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T06:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal a prohibition against the use of funds for site acquisition, development, or construction of any facility in Israel, Jerusalem, or the West Bank.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T06:33:22Z"
    }
  ]
}
```
