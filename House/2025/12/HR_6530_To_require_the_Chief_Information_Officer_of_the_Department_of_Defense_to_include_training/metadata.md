# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6530?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6530
- Title: AI Training for National Security Act
- Congress: 119
- Bill type: HR
- Bill number: 6530
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-01-06T19:40:10Z
- Update date including text: 2026-01-06T19:40:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6530",
    "number": "6530",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000560",
        "district": "2",
        "firstName": "Rick",
        "fullName": "Rep. Larsen, Rick [D-WA-2]",
        "lastName": "Larsen",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "AI Training for National Security Act",
    "type": "HR",
    "updateDate": "2026-01-06T19:40:10Z",
    "updateDateIncludingText": "2026-01-06T19:40:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6530ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6530\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Larsen of Washington (for himself and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require the Chief Information Officer of the Department of Defense to include training on artificial intelligence cybersecurity issues for members of the Armed Forces and civilian employees of the Department of Defense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI Training for National Security Act .\n#### 2. Incorporation of artificial intelligence considerations into annual cybersecurity training\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense, acting through the Chief Information Officer of the Department of Defense, shall revise the mandatory annual training on cybersecurity for members of the Armed Forces and civilian employees of the Department of Defense to include content related to the unique cybersecurity challenges posed by the use of artificial intelligence.",
      "versionDate": "2025-12-09",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T19:40:10Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6530ih.xml"
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
      "title": "AI Training for National Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI Training for National Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Chief Information Officer of the Department of Defense to include training on artificial intelligence cybersecurity issues for members of the Armed Forces and civilian employees of the Department of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:30Z"
    }
  ]
}
```
