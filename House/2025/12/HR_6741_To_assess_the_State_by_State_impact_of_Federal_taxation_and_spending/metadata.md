# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6741
- Title: Payer State Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6741
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-09T16:09:33Z
- Update date including text: 2026-01-09T16:09:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6741",
    "number": "6741",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Payer State Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T16:09:33Z",
    "updateDateIncludingText": "2026-01-09T16:09:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6741ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6741\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Foster (for himself, Ms. Schakowsky , Mr. Gottheimer , and Mr. Garc\u00eda of Illinois ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo assess the State by State impact of Federal taxation and spending.\n#### 1. Short title\nThis Act may be cited as the Payer State Transparency Act of 2025 .\n#### 2. Calculation of Federal tax burdens and outlays\n##### (a) State by State Calculation of Federal tax burdens\n**(1) In General**\nThe Secretary of Commerce, acting through the Director of the Bureau of Economic Analysis, shall calculate the Federal tax burden of each State for each calendar year.\n**(2) Calculation of Federal tax burden**\nFor purposes of calculating the Federal tax burden of each State under paragraph (1), the Secretary shall\u2014\n**(A)**\ntreat Federal taxes paid by an individual as a burden on the State in which such individual resides; and\n**(B)**\ntreat Federal taxes paid by a legal business entity as a burden on each State in which economic activity of such entity is performed in the same proportion that the economic activity of such entity in such State bears to the economic activity of such entity in all the States.\n##### (b) State by State Calculation of Federal Outlays\n**(1) In General**\nThe Director of the Office of Management and Budget, in coordination with the Council of Economic Advisers and the Secretary of the Treasury, shall calculate the total amount of Federal outlays received by each State in each fiscal year.\n**(2) Treatment of Contract Awards**\nFor purposes of calculating the amount of Federal outlays received by a State under paragraph (1), a Federal contract award shall be treated as a Federal outlay received by each State in which performance under the award takes place in the same proportion that such performance in such State bears to such performance in all the States.\n##### (c) State Defined\nIn this section the term State means each of the several States.\n#### 3. Joint report\nNot later than the date that is 180 days after the beginning of each calendar year, the Secretary of Commerce and the Director of the Office of Management and Budget shall\u2014\n**(1)**\njointly submit to Congress a report containing the results of the calculations described in section 2 with respect to such calendar year; and\n**(2)**\npublish the report on a publicly accessible website of the Bureau of Economic Analysis.",
      "versionDate": "2025-12-16",
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
        "name": "Taxation",
        "updateDate": "2026-01-09T16:09:33Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6741ih.xml"
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
      "title": "Payer State Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Payer State Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To assess the State by State impact of Federal taxation and spending.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:28Z"
    }
  ]
}
```
