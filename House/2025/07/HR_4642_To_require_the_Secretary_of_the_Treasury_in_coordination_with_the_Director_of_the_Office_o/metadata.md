# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4642
- Title: Fiscal Contingency Preparedness Act
- Congress: 119
- Bill type: HR
- Bill number: 4642
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-23T08:07:36Z
- Update date including text: 2026-05-23T08:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 39 - 1.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 39 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4642",
    "number": "4642",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Fiscal Contingency Preparedness Act",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:36Z",
    "updateDateIncludingText": "2026-05-23T08:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 39 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
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
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
            "date": "2026-03-18T13:01:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-23T14:12:05Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "ME"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "PA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "NY"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "OH"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "IN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "OH"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NC"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MI"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "AR"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "HI"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "KY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NC"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4642ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4642\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Cline (for himself, Mr. Golden of Maine , Mr. Bergman , and Ms. Perez ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, to examine the ability of the Federal Government to respond to potential fiscal shocks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fiscal Contingency Preparedness Act .\n#### 2. Annual report\n##### (a) In general\nSection 331(e) of title 31, United States Code, is amended by adding at the end the following:\n(3) (A) As a component of the report required under paragraph (1), the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, shall examine the fiscal risks and fiscal impacts of the response of the Federal Government to potential national and international fiscal shocks. (B) In making the examination required under subparagraph (A), the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, shall\u2014 (i) include an assessment of the fiscal risks and fiscal impacts of the Federal Government responding to events, such as\u2014 (I) an economic recession or depression; (II) a domestic energy crisis; (III) a catastrophic natural disaster; (IV) a health crisis, such as a global pandemic; (V) a significant armed conflict or event; (VI) a significant cyber attack; and (VII) a financial crisis; (ii) determine the estimated short-term and long-term fiscal effects on the Federal Government in the case of an event described in clause (i); and (iii) describe significant economic impacts and indicators selected by the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, to convey the short-term and long-term fiscal effects on the Federal Government in the case of an event described in clause (i) in the method that best accomplishes the goal of the examination. (C) In making the examination required under subparagraph (A) and determining the scope and magnitude of an event described in subparagraph (B)(i), the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, may consider historical instances of those events and the response of the Federal Government to those historical instances. (D) In including the examination required under subparagraph (A) in the report required under paragraph (1), the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, may structure and report the examination in the method that best accomplishes the goal of the examination. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the later of\u2014\n**(1)**\nthe first date following the date of enactment of this Act on which the Secretary of the Treasury, in coordination with the Office of Management and Budget, submits a report under section 331(e)(1) of title 31, United States Code; and\n**(2)**\n180 days after the date of enactment of this Act.\n##### (c) GAO report\nNot later than 1 year after the date on which the Secretary of the Treasury publishes the first examination required under section 331(e)(3)(A) of title 31, United States Code, as added by subsection (a), after the date of enactment of this Act, and periodically thereafter as determined necessary by the Comptroller General of the United States, the Comptroller General of the United States shall\u2014\n**(1)**\nreview the methodology and results of the fiscal analysis performed during the examination;\n**(2)**\npublish a report of the findings of the review under paragraph (1) on the website of the Government Accountability Office; and\n**(3)**\nsubmit to the Committee on the Budget of the Senate and the Committee on the Budget of the House of Representatives the report published under paragraph (2).",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2492",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fiscal Contingency Preparedness Act",
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
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T19:05:52Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2026-04-16T19:05:57Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-16T19:05:39Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-16T19:05:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-16T22:26:14Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4642ih.xml"
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
      "title": "Fiscal Contingency Preparedness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fiscal Contingency Preparedness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Treasury, in coordination with the Director of the Office of Management and Budget, to examine the ability of the Federal Government to respond to potential fiscal shocks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:32Z"
    }
  ]
}
```
