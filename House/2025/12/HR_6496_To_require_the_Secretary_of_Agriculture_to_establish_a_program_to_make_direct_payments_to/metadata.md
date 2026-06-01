# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6496
- Title: Specialty Crop & Wine Producer Tariff Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 6496
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2026-01-15T09:06:49Z
- Update date including text: 2026-01-15T09:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6496",
    "number": "6496",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Specialty Crop & Wine Producer Tariff Relief Act",
    "type": "HR",
    "updateDate": "2026-01-15T09:06:49Z",
    "updateDateIncludingText": "2026-01-15T09:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "WA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "OR"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6496ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6496\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Mr. Thompson of California (for himself, Mr. Newhouse , Mr. LaMalfa , and Ms. Salinas ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to establish a program to make direct payments to certain specialty crop growers or wine producers who experience certain losses due to increased tariff burdens, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Specialty Crop & Wine Producer Tariff Relief Act .\n#### 2. USDA assistance to certain specialty crop growers and wine producers; authority to purchase surplus crops\n##### (a) Direct payment program\n**(1) In general**\nNot later than 180 days after the date of the enactment of this section, the Secretary of Agriculture (hereinafter the Secretary ) shall establish a program to make direct payments for covered losses, and distribute such payments, to the following persons:\n**(A)**\nSpecialty crop growers.\n**(B)**\nWine producers.\n**(2) Administration**\nThe Secretary shall administer the program established under this subsection in a manner substantially similar to the Marketing Assistance for Specialty Crops program authorized by section 5(e) of the Commodity Credit Corporation Charter Act ( 15 U.S.C. 714c(e) ).\n##### (b) Purchase of surplus crops\nThe Secretary may purchase surplus crops (other than wine grapes) to be distributed for nutrition assistance programs.\n##### (c) Reporting\nBeginning not later than 120 days after the date on which the Secretary first exercises any authority under subsections (a) or (b), and annually thereafter until 2030, the Secretary shall provide to Congress a report, organized by crop and region, on\u2014\n**(1)**\nthe direct payments distributed under subsection (a); and\n**(2)**\nany surplus crops purchased under subsection (b).\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary such sums as are necessary to carry out this section for fiscal years 2026 through 2030.\n##### (e) Administrative Costs\nOut of any funds made available to carry out this section, the Secretary may use not more than 1 percent for administrative costs.\n##### (f) Definitions\nIn this section:\n**(1) Covered loss**\n**(A) In general**\nThe term covered loss includes\u2014\n**(i)**\nincreased costs related to\u2014\n**(I)**\nthe tenderness and perishability of specialty crops;\n**(II)**\nthe need to use specialized handling and transport equipment with temperature and humidity control;\n**(III)**\npackaging to prevent damage;\n**(IV)**\nmoving perishables to market quickly; and\n**(V)**\nhigher labor costs;\n**(ii)**\nreduced exports due to an increased tariff burden;\n**(iii)**\nlost export revenue due to decreased foreign demand;\n**(iv)**\neconomic loss due to reduced market access;\n**(v)**\nreduced contracts with a foreign buyer; and\n**(vi)**\ncancelled or reduced contracts due to reduced foreign demand.\n**(B) Wine or wine grape producers**\nWith respect to a wine producer or a specialty crop grower who produces wine grapes, the term covered loss \u2014\n**(i)**\nhas the meaning given such term under paragraph (A); and\n**(ii)**\nincludes lost qualifying export revenue for wine.\n**(2) Increased tariff burden**\nThe term increased tariff burden means a tariff that was introduced by another country on United States products on or after January 20, 2025.\n**(3) Nutrition programs**\nThe term nutrition programs includes the following:\n**(A)**\nThe school breakfast program established under section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ).\n**(B)**\nThe school lunch program under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ).\n**(C)**\nThe supplemental nutrition assistance program under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ).\n**(D)**\nAny other such programs as determined by the Secretary.\n**(4) Qualifying export revenue**\nThe term qualifying export revenue means the percentage of lost export revenue for wine in an amount equal to the percentage of such wine produced in the United States with United States-grown grapes.\n**(5) Specialty crop**\nThe term specialty crop \u2014\n**(A)**\nhas the meaning given such term in section 3 of the Specialty Crops Competitiveness Act of 2004 ( 7 U.S.C. 1621 note); and\n**(B)**\nincludes wine grapes.\n**(6) Wine**\nThe term wine means the product obtained from normal alcoholic fermentation of the juice of sound ripe grapes or other agricultural products containing natural or added sugar or any such alcoholic beverage to which is added grape brand, fruit brandy, or spirits of wine, which is distilled from the particular agricultural product or products of which the wine is made and other rectified wine products and by whatever name and which does not contain more than 15 percent added flavoring, coloring, and blending material and which contains not more than 24 percent of alcohol by volume, and includes vermouth and sake, known as Japanese rick wine.\n**(7) Wine producer**\nThe term wine producer means any person who\u2014\n**(A)**\nowns, or has access to, a facility and equipment for the conversion of grapes, berries, or other fruit into wine;\n**(B)**\nis engaged in the production of wine for commercial sale; and\n**(C)**\nholds all licenses, permits, or approvals required under Federal or State law for the activities described under subparagraphs (A) and (B).",
      "versionDate": "2025-12-05",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:05:05Z"
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
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6496ih.xml"
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
      "title": "Specialty Crop & Wine Producer Tariff Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Specialty Crop & Wine Producer Tariff Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to establish a program to make direct payments to certain specialty crop growers or wine producers who experience certain losses due to increased tariff burdens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:16Z"
    }
  ]
}
```
