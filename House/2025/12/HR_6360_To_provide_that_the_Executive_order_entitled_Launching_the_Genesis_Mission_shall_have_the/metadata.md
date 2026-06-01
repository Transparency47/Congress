# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6360?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6360
- Title: GENESIS Act
- Congress: 119
- Bill type: HR
- Bill number: 6360
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2025-12-16T09:05:32Z
- Update date including text: 2025-12-16T09:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6360",
    "number": "6360",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "GENESIS Act",
    "type": "HR",
    "updateDate": "2025-12-16T09:05:32Z",
    "updateDateIncludingText": "2025-12-16T09:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6360ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6360\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Kennedy of Utah introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo provide that the Executive order entitled Launching the Genesis Mission shall have the force and effect of law, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growth, Energy, and National Excellence through Science, Innovation, and Security Act or the GENESIS Act .\n#### 2. Legal effect\nNotwithstanding any other provision of law or Executive order, Executive Order 14363 (90 Fed. Reg. 55035), signed on November 24, 2025, and entitled \u201cLaunching the Genesis Mission\u201d, shall have the force and effect of law.",
      "versionDate": "2025-12-02",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-04T15:43:21Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6360ih.xml"
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
      "title": "GENESIS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T09:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GENESIS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T09:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growth, Energy, and National Excellence through Science, Innovation, and Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T09:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the Executive order entitled \"Launching the Genesis Mission\" shall have the force and effect of law, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T09:18:31Z"
    }
  ]
}
```
