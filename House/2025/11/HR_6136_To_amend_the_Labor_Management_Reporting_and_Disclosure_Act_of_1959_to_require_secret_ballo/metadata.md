# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6136
- Title: PURE Act
- Congress: 119
- Bill type: HR
- Bill number: 6136
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2025-12-02T16:05:26Z
- Update date including text: 2025-12-02T16:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6136",
    "number": "6136",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PURE Act",
    "type": "HR",
    "updateDate": "2025-12-02T16:05:26Z",
    "updateDateIncludingText": "2025-12-02T16:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6136ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6136\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Fine (for himself and Mr. Harris of North Carolina ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Labor-Management Reporting and Disclosure Act of 1959 to require secret ballot elections of members for certain union officers.\n#### 1. Short title\nThis Act may be cited as the Protecting Union Representation and Elections Act or the PURE Act .\n#### 2. Secret ballot for certain elections\n##### (a) In general\nSection 401 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 481 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking either ; and\n**(B)**\nby striking or at a convention of delegates chosen by secret ballot ; and\n**(2)**\nin subsection (d), by striking or by labor organization officers representative of such members who have been elected by secret ballot .\n##### (b) Effective date\nThe amendments made by this Act shall take effect on the date that is 18 months after the date of enactment of this Act.",
      "versionDate": "2025-11-19",
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
        "name": "Labor and Employment",
        "updateDate": "2025-12-02T16:05:26Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6136ih.xml"
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
      "title": "PURE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PURE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Union Representation and Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Labor-Management Reporting and Disclosure Act of 1959 to require secret ballot elections of members for certain union officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T01:48:19Z"
    }
  ]
}
```
