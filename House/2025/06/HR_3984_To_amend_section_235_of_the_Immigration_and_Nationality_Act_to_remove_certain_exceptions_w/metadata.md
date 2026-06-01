# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3984
- Title: Expedited Removal Expansion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3984
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-05-22T08:08:34Z
- Update date including text: 2026-05-22T08:08:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3984",
    "number": "3984",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Expedited Removal Expansion Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:34Z",
    "updateDateIncludingText": "2026-05-22T08:08:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AZ"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "CO"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AZ"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3984ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3984\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Mace (for herself, Mr. Biggs of Arizona , Mr. Gill of Texas , Ms. Boebert , Mr. Gosar , and Mr. Steube ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 235 of the Immigration and Nationality Act to remove certain exceptions with respect to the inspection of applicants for admission.\n#### 1. Short title\nThis Act may be cited as the Expedited Removal Expansion Act of 2025 .\n#### 2. Inspection of Applicants for Admission\nSection 235(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1) ) is amended in\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i)\u2014\n**(i)**\nby striking (other than an alien described in subparagraph (F)) ; and\n**(ii)**\nby striking under section 212(a)(6)(C) or 212(a)(7), and inserting under section 212 ;\n**(B)**\nin clause (ii)\u2014\n**(i)**\nby striking (other than an alien described in subparagraph (F)) ; and\n**(ii)**\nby striking under section 212(a)(6)(C) or 212(a)(7) and inserting under section 212 ; and\n**(C)**\nin clause (iii)(II)\u2014\n**(i)**\nby striking who is not described in subparagraph (F), ; and\n**(ii)**\nby striking , and who has not affirmatively shown, to the satisfaction of an immigration officer, that the alien has been physically present in the United States continuously for the 2-year period immediately prior to the date of the determination of inadmissibility under this subparagraph ;\n**(2)**\nby striking subparagraph (F); and\n**(3)**\nby redesignating subparagraph (G) as subparagraph (F).",
      "versionDate": "2025-06-12",
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
        "name": "Immigration",
        "updateDate": "2025-07-03T13:54:13Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3984ih.xml"
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
      "title": "Expedited Removal Expansion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T07:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expedited Removal Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T07:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 235 of the Immigration and Nationality Act to remove certain exceptions with respect to the inspection of applicants for admission.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T07:48:21Z"
    }
  ]
}
```
