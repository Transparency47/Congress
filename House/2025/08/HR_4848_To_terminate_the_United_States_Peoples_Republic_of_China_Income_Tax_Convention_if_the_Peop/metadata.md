# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4848
- Title: No Tax Treaties for Foreign Aggressors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4848
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-04-02T17:53:15Z
- Update date including text: 2026-04-02T17:53:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4848",
    "number": "4848",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No Tax Treaties for Foreign Aggressors Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-02T17:53:15Z",
    "updateDateIncludingText": "2026-04-02T17:53:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4848ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4848\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo terminate the United States-People\u2019s Republic of China Income Tax Convention if the People\u2019s Liberation Army initiates an armed attack against Taiwan.\n#### 1. Short title\nThis Act may be cited as the No Tax Treaties for Foreign Aggressors Act of 2025 .\n#### 2. Conditional termination of the United States-People\u2019s Republic of China Income Tax Convention\n##### (a) In general\nThe Secretary of the Treasury shall provide written notice to the People's Republic of China through diplomatic channels of the United States intent to terminate the United States-The People\u2019s Republic of China Income Tax Convention, done at Beijing April 30, 1984, and entered into force January 1, 1987, as provided by Article 28 of the Convention, not later than 30 days after the President notifies the Secretary of the Treasury that the People\u2019s Liberation Army has initiated an armed attack against the Republic of China (commonly known as Taiwan ).\n##### (b) Congressional notification\nThe President shall submit written notification of a termination described in subsection (a) to\u2014\n**(1)**\nthe Committee on Foreign Relations of the Senate ;\n**(2)**\nthe Committee on Finance of the Senate;\n**(3)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(4)**\nthe Committee on Ways and Means of the House of Representatives.",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-08-01",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "2646",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Tax Treaties for Foreign Aggressors Act",
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
        "name": "International Affairs",
        "updateDate": "2025-09-18T20:54:51Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4848ih.xml"
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
      "title": "No Tax Treaties for Foreign Aggressors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax Treaties for Foreign Aggressors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To terminate the United States-People's Republic of China Income Tax Convention if the People's Liberation Army initiates an armed attack against Taiwan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:20Z"
    }
  ]
}
```
