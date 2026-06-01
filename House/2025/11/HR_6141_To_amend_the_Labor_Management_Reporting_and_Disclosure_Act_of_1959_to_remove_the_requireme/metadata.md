# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6141
- Title: Fair Access to Justice for Union Members Act
- Congress: 119
- Bill type: HR
- Bill number: 6141
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2025-11-21T13:01:43Z
- Update date including text: 2025-11-21T13:01:43Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6141",
    "number": "6141",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001102",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Harris, Mark [R-NC-8]",
        "lastName": "Harris",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Fair Access to Justice for Union Members Act",
    "type": "HR",
    "updateDate": "2025-11-21T13:01:43Z",
    "updateDateIncludingText": "2025-11-21T13:01:43Z"
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
          "date": "2025-11-19T15:02:10Z",
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
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MO"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6141ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6141\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Harris of North Carolina (for himself, Mr. Onder , and Mr. Fine ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Labor-Management Reporting and Disclosure Act of 1959 to remove the requirement that members of a union exhaust internal reasonable hearing procedures prior to bringing certain legal or administrative proceedings.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Justice for Union Members Act .\n#### 2. Removal of exhaustion requirements\n##### (a) In general\nSection 101(a)(4) of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 411(a)(4) ) is amended by striking That any such member may be required to exhaust reasonable hearing procedures (but not to exceed a four-month lapse of time) within such organization, before instituting legal or administrative proceedings against such organizations or any officer thereof: And provided further, .\n##### (b) Effective date\nThe amendment made by this Act shall take effect on the date that is 18 months after the date of enactment of this Act.",
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
        "updateDate": "2025-11-21T13:01:43Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6141ih.xml"
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
      "title": "Fair Access to Justice for Union Members Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Access to Justice for Union Members Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Labor-Management Reporting and Disclosure Act of 1959 to remove the requirement that members of a union exhaust internal reasonable hearing procedures prior to bringing certain legal or administrative proceedings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-20T10:48:17Z"
    }
  ]
}
```
