# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2174?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2174
- Title: Paycheck Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2174
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-12-05T22:51:46Z
- Update date including text: 2025-12-05T22:51:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2174",
    "number": "2174",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Paycheck Protection Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:51:46Z",
    "updateDateIncludingText": "2025-12-05T22:51:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 21.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
        "item": [
          {
            "date": "2025-03-25T15:17:45Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-18T16:04:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2174ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2174\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Burlison (for himself, Mrs. Miller of Illinois , and Ms. Mace ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to provide that agencies may not deduct labor organization dues from the pay of Federal employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Paycheck Protection Act .\n#### 2. Labor organization dues not deductible from pay\n##### (a) Federal agencies\n**(1) In general**\nSection 7115 of title 5, United States Code, is amended to read as follows:\n7115. Labor organization dues not deductible from pay An agency may not deduct any amount from the pay of an employee for labor organization dues, fees, or political contributions. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 71 of title 5, United States Code, is amended by striking the item relating to section 7115 and inserting the following:\n7115. Labor organization dues not deductible from pay. .\n##### (b) Postal Service\n**(1) In general**\nSection 1205 of title 39, United States Code, is amended to read as follows:\n1205. Labor organization dues not deductible from pay The Postal Service may not deduct any amount from the pay of an employee for labor organization dues, fees, or political contributions. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 12 of title 39, United States Code, is amended by striking the item relating to section 1205 and inserting the following:\n1205. Labor organization dues not deductible from pay. .",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-05-05",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1597",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Paycheck Protection Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-03T15:55:26Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-06-03T15:55:20Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-06-03T15:55:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-19T15:32:29Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2174ih.xml"
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
      "title": "Paycheck Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Paycheck Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to provide that agencies may not deduct labor organization dues from the pay of Federal employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:26Z"
    }
  ]
}
```
