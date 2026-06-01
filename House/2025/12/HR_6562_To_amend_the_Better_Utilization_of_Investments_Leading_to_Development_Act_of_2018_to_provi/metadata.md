# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6562
- Title: United States Development Finance Corporation Effectiveness Act
- Congress: 119
- Bill type: HR
- Bill number: 6562
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-04-17T19:20:26Z
- Update date including text: 2026-04-17T19:20:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6562",
    "number": "6562",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001091",
        "district": "20",
        "firstName": "Joaquin",
        "fullName": "Rep. Castro, Joaquin [D-TX-20]",
        "lastName": "Castro",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "United States Development Finance Corporation Effectiveness Act",
    "type": "HR",
    "updateDate": "2026-04-17T19:20:26Z",
    "updateDateIncludingText": "2026-04-17T19:20:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6562ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6562\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Castro of Texas introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Better Utilization of Investments Leading to Development Act of 2018 to provide for increased effectiveness.\n#### 1. Short title\nThis Act may be cited as the United States Development Finance Corporation Effectiveness Act .\n#### 2. Annual report\nSection 1443 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9653 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (4), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby inserting at the end the following:\n(5) the United States strategic, foreign policy, and development objectives advanced through projects supported by the Corporation; and (6) the health of the Corporation\u2019s portfolio, including an annual overview of funds committed, funds disbursed, default and recovery rates, capital mobilized, equity investments\u2019 year on year returns, and any difference between how investments were modeled at commitment and how they ultimately performed, to include a narrative explanation explaining any changes. ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking subparagraphs (A) and (B) and inserting the following:\n(A) the desired development impact and strategic outcomes for projects, and whether or not the Corporation is meeting the associated metrics, goals, and development objectives, including, to the extent practicable, in the years after conclusion of projects; (B) whether the Corporation\u2019s support for projects that focus on achieving strategic outcomes are achieving such strategic objectives of such investments over the duration of the support and lasting after the Corporation\u2019s support is completed; (C) the value of private sector assets brought to bear relative to the amount of support provided by the Corporation and the value of any other public sector support; (D) the total private capital projected to be mobilized by projects supported by the Corporation during that year, including an analysis of the lenders and investors involved and investment instruments used; (E) the total private capital actually mobilized by projects supported by the Corporation that were fully funded by the end of that year, including\u2014 (i) an analysis of the lenders and investors involved and investment instruments used; and (ii) a comparison with the private capital projected to be mobilized for the projects described in this paragraph; (F) a breakdown of\u2014 (i) the amount and percentage of Corporation support provided to less developed countries, advancing income countries, and high-income countries in the previous fiscal year; and (ii) the amount and percentage of Corporation support provided to less developed countries, advancing income countries, and high-income countries averaged over the last 5 fiscal years; (G) a breakdown of the aggregate amounts and percentage of the maximum contingent liability of the Corporation authorized to be outstanding pursuant to section 1433 in less developed countries, advancing income countries, and high-income countries; (H) the risk appetite of the Corporation to undertake projects in less developed countries and in sectors that are critical to development but less likely to deliver substantial financial returns; and (I) efforts by the Chief Executive Officer to incentivize calculated risk-taking by transaction teams, including through the conduct of development performance reviews and provision of development performance rewards; ;\n**(B)**\nin paragraph (3)(B), by striking ; and and inserting a semicolon;\n**(C)**\nby redesignating paragraph (4) as paragraph (5); and\n**(D)**\nby inserting after paragraph (3) the following:\n(4) to the extent practicable, recommendations for measures that could enhance the strategic goals of projects to adapt to changing circumstances; and .\n#### 3. Publicly available project information\nSection 1444 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9654 ) is amended in paragraph (1) to read as follows:\n(1) maintain a user-friendly, publicly available, machine-readable database with detailed project-level information, as appropriate and to the extent practicable, including a description of the support provided by the Corporation under title II, which shall include, to the greatest extent feasible for each project\u2014 (A) the information included in the report to Congress under section 1443; (B) project-level performance metrics; and (C) a description of the development impact of the project, including anticipated impact prior to initiation of the project and assessed impact during and after the completion of the project; and .",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
        "updateDate": "2026-01-08T16:43:16Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6562ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Better Utilization of Investments Leading to Development Act of 2018 to provide for increased effectiveness.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:21Z"
    },
    {
      "title": "United States Development Finance Corporation Effectiveness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States Development Finance Corporation Effectiveness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:20Z"
    }
  ]
}
```
