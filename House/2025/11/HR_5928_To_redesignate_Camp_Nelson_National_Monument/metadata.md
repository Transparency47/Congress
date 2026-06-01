# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5928?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5928
- Title: Camp Nelson National Monument Act
- Congress: 119
- Bill type: HR
- Bill number: 5928
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-02T19:14:11Z
- Update date including text: 2025-12-02T19:14:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5928",
    "number": "5928",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Camp Nelson National Monument Act",
    "type": "HR",
    "updateDate": "2025-12-02T19:14:11Z",
    "updateDateIncludingText": "2025-12-02T19:14:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5928ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5928\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo redesignate Camp Nelson National Monument.\n#### 1. Short title\nThis Act may be cited as the Camp Nelson National Monument Act .\n#### 2. Camp Nelson National Monument\n##### (a) Amendment\nSection 2303 of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ) is amended\u2014\n**(1)**\nin the heading, by striking Heritage ;\n**(2)**\nin subsection (a)(2), by striking Camp Nelson Heritage National Monument and inserting Camp Nelson National Monument ; and\n**(3)**\nin subsection (b)(1), by striking Camp Nelson Heritage National Monument and inserting Camp Nelson National Monument .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to Camp Nelson Heritage National Monument shall be deemed to be a reference to Camp Nelson National Monument.",
      "versionDate": "2025-11-07",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-02T19:14:11Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5928ih.xml"
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
      "title": "Camp Nelson National Monument Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-11T06:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Camp Nelson National Monument Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To redesignate Camp Nelson National Monument.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:19Z"
    }
  ]
}
```
