# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4444?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4444
- Title: Student Loan Bankruptcy Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4444
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-02-05T09:06:46Z
- Update date including text: 2026-02-05T09:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4444",
    "number": "4444",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001110",
        "district": "46",
        "firstName": "J.",
        "fullName": "Rep. Correa, J. Luis [D-CA-46]",
        "lastName": "Correa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Student Loan Bankruptcy Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-05T09:06:46Z",
    "updateDateIncludingText": "2026-02-05T09:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:04:45Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VT"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "LA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "LA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "WA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "DC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NY"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "IL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MS"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IN"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "CT"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4444ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4444\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Correa (for himself, Ms. Adams , Ms. Balint , Mr. Carter of Louisiana , Mr. Fields , Ms. Jayapal , Mr. Johnson of Georgia , Ms. Lee of Pennsylvania , Ms. Lofgren , Ms. Norton , Ms. Ross , Mr. Swalwell , Ms. Tlaib , Mr. Thanedar , Mr. Tonko , and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide a more equitable discharge standard for student loan borrowers.\n#### 1. Short title\nThis Act may be cited as the Student Loan Bankruptcy Improvement Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nStudent loan borrowers deserve an opportunity to discharge debt using a fair, nation-wide standard for relief.\n**(2)**\nThe current standard of undue hardship fails to provide an achievable avenue for relief of student loan debt requiring significant costs and a paperwork burden.\n**(3)**\nStudent loan borrowers rarely meet the arbitrary and draconian standard of undue hardship, especially in jurisdictions using the Brunner test, with only 0.01% successfully being discharged as of 2022.\n**(4)**\nThe criteria utilized in the Brunner test, which is used by most bankruptcy courts in the United States, is inconsistent with the main goal of bankruptcy of giving honest debtors a fresh start, enabling them to more fully participate and contribute to the economy.\n**(5)**\nThe Brunner test was developed by the courts decades ago when debtors could discharge their student loans in bankruptcy by simply waiting five or seven years\u2014it should no longer be used now that the waiting period for discharge was eliminated by Congress.\n**(6)**\nBy changing the standard of hardship, Congress would provide bankruptcy courts with needed flexibility to adopt more reasonable criteria in determining discharge standards for student loan debt.\n**(7)**\nAdopting this new hardship standard does not negate requirements for discharge under bankruptcy proceedings like means testing, disclosure requirements, and exemption limitations, securing bankruptcy\u2019s integrity and benefitting both debtors and creditors who have an increased opportunity for repayment.\n**(8)**\nAs of June 2025, around six million borrowers of Federal student loans are passed due by at least 90 days.\n**(9)**\nA majority of borrowers with 90 days or more past due student loans as of June 2025 could move into default by September 2025.\n**(10)**\nMillions of student loan borrowers are facing significant credit score declines making it more expensive or difficult to get necessary insurance, loans, and credit cards.\n**(11)**\nThe vast majority of debtors seeking bankruptcy discharges for student loans never obtained degrees or got degrees that have not enabled them to secure better employment or have a higher earning potential as predicted when Congress adopted the undue hardship standard.\n**(12)**\nAccording to a Duke Law Journal article, between 2011 and 2019, less than 0.1 percent of applications made by student loan debtors in bankruptcy court seeking a discharge of student loan debt were successful, largely because attorneys discourage their clients from seeking an adversary proceeding on the belief that it is too hard to meet the undue hardship standard.\n**(13)**\nEach year, less than one percent of the approximately 250,000 people who file for bankruptcy seek to discharge student loan debt based on undue hardship, a mere fraction of the nearly 43 million people who have Federal student loan debt.\n**(14)**\nBetween November 2022 and September 2024, approximately 2,500 people sought to discharge student loan debt through bankruptcy.\n**(15)**\nThe Department of Education (Department) recently reported that twenty percent of borrowers are in default and another four million are between three and six months behind on their payments. The Department estimates that as many as 10 million borrowers could be in default within a few months.\n**(16)**\nThere is little evidence of debtors abusing the bankruptcy system by seeking unfair discharges of student loan obligations, a concern raised by Congress when it adopted the undue hardship standard.\n**(17)**\nThe concerns of abuse were addressed and minimized with the passage in 2005 of the Bankruptcy Abuse Prevention and Consumer Protection Act with the enactment of a rigorous Means Test to evaluate debtors\u2019 ability to repay debts.\n**(18)**\nStudent loan debt owed by Americans who file for bankruptcy with student loans is often never paid, whereas bankruptcy proceedings provide an opportunity to address this reality.\n**(19)**\nWith the restart of student loan collections, the number of borrowers with student loan debt is expected to rise. The change to a hardship standard will facilitate fair and appropriate discharges and repayment plans.\n#### 3. Amendment 11\nSection 523(a)(8) of title 11, United States Code, is amended by striking undue .\n#### 4. Application of amendment\nThe amendment made by this Act shall apply with respect to cases commenced before, on, and after the date of the enactment of this Act.",
      "versionDate": "2025-07-16",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-11T15:50:16Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4444ih.xml"
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
      "title": "Student Loan Bankruptcy Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Student Loan Bankruptcy Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a more equitable discharge standard for student loan borrowers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:33:20Z"
    }
  ]
}
```
