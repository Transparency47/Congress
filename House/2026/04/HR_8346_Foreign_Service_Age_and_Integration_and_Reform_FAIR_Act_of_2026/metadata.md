# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8346?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8346
- Title: Foreign Service Age and Integration and Reform (FAIR) Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8346
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-21T21:53:04Z
- Update date including text: 2026-04-21T21:53:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8346",
    "number": "8346",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "O000176",
        "district": "2",
        "firstName": "Johnny",
        "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
        "lastName": "Olszewski",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Foreign Service Age and Integration and Reform (FAIR) Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T21:53:04Z",
    "updateDateIncludingText": "2026-04-21T21:53:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:03:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8346ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8346\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Olszewski (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo raise the Foreign Service mandatory retirement age by aligning it with the Social Security Full Retirement Age, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Service Age and Integration and Reform (FAIR) Act of 2026 .\n#### 2. Modification of mandatory retirement age\nSection 812(a)(1) of the Foreign Service Act of 1980 ( 22 U.S.C. 4052(a)(1) ) is amended by striking age 65 and inserting age 67 or the applicable retirement age (as defined in section 216(l) of the Social Security Act ( 42 U.S.C. 416(l) )), whichever is greater, .",
      "versionDate": "2026-04-16",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-05",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "4002",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Foreign Service Age Integration and Reform (FAIR) Act of 2026",
      "type": "S"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-21T21:53:04Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8346ih.xml"
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
      "title": "Foreign Service Age and Integration and Reform (FAIR) Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T02:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Service Age and Integration and Reform (FAIR) Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To raise the Foreign Service mandatory retirement age by aligning it with the Social Security Full Retirement Age, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:34Z"
    }
  ]
}
```
