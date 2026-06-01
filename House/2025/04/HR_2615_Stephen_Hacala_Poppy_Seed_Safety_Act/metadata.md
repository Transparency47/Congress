# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2615
- Title: Stephen Hacala Poppy Seed Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 2615
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2025-12-05T22:47:41Z
- Update date including text: 2025-12-05T22:47:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2615",
    "number": "2615",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000809",
        "district": "3",
        "firstName": "Steve",
        "fullName": "Rep. Womack, Steve [R-AR-3]",
        "lastName": "Womack",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Stephen Hacala Poppy Seed Safety Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:47:41Z",
    "updateDateIncludingText": "2025-12-05T22:47:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CT"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AR"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AR"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "AR"
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
      "sponsorshipDate": "2025-08-26",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2615ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2615\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Mr. Womack (for himself, Ms. DeLauro , Mr. Hill of Arkansas , Mr. Westerman , and Mr. Crawford ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the sale of food that is, or contains, unsafe poppy seeds.\n#### 1. Short title\nThis Act may be cited as the Stephen Hacala Poppy Seed Safety Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds as follows:\n**(1)**\nStephen Hacala was a 24-year-old from Fayetteville, Arkansas, who was dearly loved by family and friends when he died from morphine intoxication caused by consumption of contaminated poppy seeds.\n**(2)**\nAt least 19 people in the United States have been confirmed to have died from morphine overdoses from contaminated poppy seeds.\n**(3)**\nWomen in the United States have tested positive for opiates in hospitals at childbirth due to poppy seed consumption in food, leading to unwarranted scrutiny from child welfare officials.\n**(4)**\nIn 2023, the Department of Defense issued a warning to all servicemembers to avoid poppy seed consumption due to opiate contamination and the risk of positive drug tests.\n**(5)**\nStudies of pharmaceutical opiates have found that a dose of just 20 to 50 morphine milligram equivalents per day increases the risk of overdose and death among patients prescribed morphine for pain treatment.\n**(6)**\nPoppy products purchased in the United States have been found to have up to 2,788 milligrams of morphine per kilogram of seeds after extraction.\n**(7)**\nWhile poppy seeds are excluded from the definition of opium poppy and poppy straw under the Controlled Substances Act ( 21 U.S.C. 801 et seq. ), that definition does not exclude unwashed poppy seeds that have been contaminated with opium alkaloids from the latex of the plant. The opium alkaloids (inclusive of morphine, codeine, and thebaine), if present as contaminants on poppy seed material, are also not exempted from control under that Act.\n##### (b) Purpose\nIt is the purpose of this Act to establish levels for contamination of poppy seeds by morphine, by codeine, and by other illicit compounds, after which poppy seeds shall be considered adulterated substances that are prohibited in interstate commerce.\n#### 3. Unsafe poppy seeds as adulterants in food\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\nnot later than 1 year after the date of enactment of this Act, issue a proposed rule establishing levels for contamination of poppy seeds by morphine, by codeine, and by other alkaloid compounds, and by any other compound which the Secretary may designate, after which poppy seeds shall be deemed adulterated under section 402 of the Federal Food, Drug, and Cosmetic Act ( 42 U.S.C. 342 ); and\n**(2)**\nnot later than 2 years after the date of enactment of this Act, finalize such rule.\n#### 4. Poppy seeds as a controlled substance\nNothing in this Act shall be construed as exempting poppy seeds that are contaminated by morphine, codeine, another alkaloid compound, or any other compound designated by the Secretary of Health and Human Services under section 3 from regulation under the Controlled Substances Act ( 21 U.S.C. 801 et seq. ).",
      "versionDate": "2025-04-02",
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
        "actionDate": "2025-04-02",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1258",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stephen Hacala Poppy Seed Safety Act",
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
        "name": "Health",
        "updateDate": "2025-04-09T13:57:25Z"
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
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2615ih.xml"
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
      "title": "Stephen Hacala Poppy Seed Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stephen Hacala Poppy Seed Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the sale of food that is, or contains, unsafe poppy seeds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:18Z"
    }
  ]
}
```
