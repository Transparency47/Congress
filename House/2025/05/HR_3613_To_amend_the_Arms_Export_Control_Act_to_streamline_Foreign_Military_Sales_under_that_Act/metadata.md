# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3613?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3613
- Title: Streamlining Foreign Military Sales Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3613
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-10-18T08:05:46Z
- Update date including text: 2025-10-18T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 23.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 23.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3613",
    "number": "3613",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "Z000018",
        "district": "1",
        "firstName": "Ryan",
        "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
        "lastName": "Zinke",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Streamlining Foreign Military Sales Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:46Z",
    "updateDateIncludingText": "2025-10-18T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 27 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
            "date": "2025-07-22T15:40:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-23T14:00:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "TX"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3613ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3613\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Zinke (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Arms Export Control Act to streamline Foreign Military Sales under that Act.\n#### 1. Short title\nThis Act may be cited as the Streamlining Foreign Military Sales Act of 2025 .\n#### 2. Amendments to Arms Export Control Act\nThe Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) is amended\u2014\n**(1)**\nin section 36(a)(10), by striking $250,000 each place it appears and inserting $500,000 ;\n**(2)**\nin section 25(a)(1), by striking $7,000,000 and inserting $30,000,000 ;\n**(3)**\nin section 25(a)(1), by striking 25,000,000 and inserting 105,000,000 ;\n**(4)**\nin sections 3(d)(1), 3(d)(3)(A), 36(b)(1), 35(b)(5)(C), 36(c)(1), and 63(a)(1), by striking $14,000,000 each place it appears and inserting $30,000,000 ;\n**(5)**\nin sections 3(d)(5), 25(a)(1), 36(b)(6)(A), 36(c)(5)(A) and 63(a)(2), by striking $25,000,000 each place it appears and inserting $55,000,000 ;\n**(6)**\nin sections 3(d)(1), 3(d)(3)(A), 36(b)(1), 36(b)(5)(C), 36(c)(1), 47(6), 63(a)(1), and 71(d), by striking $50,000,000 each place it appears and inserting $105,000,000 ;\n**(7)**\nin sections 3(d)(5), 36(b)(6)(B), 36(c)(5)(B), and 63(a)(2), by striking $100,000,000 each place it appears and inserting $205,000,000 ;\n**(8)**\nin sections 36(b)(1), 36(b)(5)(C), and 47(6), by striking $200,000,000 each place it appears and inserting $410,000,000 ; and\n**(9)**\nin section 36(b)(6)(C), by striking $300,000,000 and inserting $615,000,000 .",
      "versionDate": "2025-05-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-08-19T13:43:53Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2025-08-19T13:43:46Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-08-19T13:48:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:06:35Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3613ih.xml"
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
      "title": "Streamlining Foreign Military Sales Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Foreign Military Sales Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Arms Export Control Act to streamline Foreign Military Sales under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:28Z"
    }
  ]
}
```
