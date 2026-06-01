# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4110
- Title: The Organic Dairy Data Collection Act
- Congress: 119
- Bill type: HR
- Bill number: 4110
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2025-12-19T09:08:06Z
- Update date including text: 2025-12-19T09:08:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4110",
    "number": "4110",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000597",
        "district": "1",
        "firstName": "Chellie",
        "fullName": "Rep. Pingree, Chellie [D-ME-1]",
        "lastName": "Pingree",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "The Organic Dairy Data Collection Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:08:06Z",
    "updateDateIncludingText": "2025-12-19T09:08:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:03:40Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "WI"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NY"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4110ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4110\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Ms. Pingree (for herself, Mr. Wied , and Mr. Langworthy ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide for the improved collection of data for organic dairy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the The Organic Dairy Data Collection Act .\n#### 2. Improved data collection for organic dairy\n##### (a) In general\nThe Secretary of Agriculture (referred to in this Act as the Secretary ) shall provide support for regional and national programs to collect and publish cost-of-production data for organic milk, including data relating to\u2014\n**(1)**\nthe costs of major organic feedstuffs, including\u2014\n**(A)**\ncorn;\n**(B)**\ncorn silage;\n**(C)**\nsoybeans;\n**(D)**\nsorghum;\n**(E)**\noilseeds;\n**(F)**\nsmall grains;\n**(G)**\nforage crops;\n**(H)**\npasture;\n**(I)**\nhay; and\n**(J)**\nany other major organic feedstuff, as determined by the Secretary;\n**(2)**\nwith respect to the costs described in paragraph (1), prices for\u2014\n**(A)**\nmajor organic feedstuffs produced domestically; and\n**(B)**\nimported major organic feedstuffs; and\n**(3)**\nall other costs relating to the production of organic milk.\n##### (b) Organic All Milk Price Survey\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a survey, to be known as the Organic All Milk Prices Survey , which shall be analogous to the existing All Milk Prices Survey of the National Agricultural Statistics Service, to gather and report monthly data about the amounts that organic dairy farmers are being paid for the organic milk produced by those organic dairy farmers and the prices received for organic milk cows, including\u2014\n**(1)**\nnational data; and\n**(2)**\ndata relating to, at a minimum, the 6 regions with the greatest quantity of organic dairy production, as determined by the Secretary.\n##### (c) Organic milk reporting\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary, using data collected by the National Agricultural Statistics Service, the Economic Research Service, or the Agricultural Marketing Service, shall publish new periodic reports that include, or add to existing periodic reports, data for organic milk, which shall be equivalent to data reported for conventionally produced milk.\n**(2) Requirement**\nReports published under paragraph (1) shall include, at a minimum\u2014\n**(A)**\norganic cost-of-production data by State;\n**(B)**\nregional data relating to the quantity of organic milk production;\n**(C)**\norganic mailbox price for the 6 regions with the greatest quantity of organic dairy production, as determined by the Secretary; and\n**(D)**\nmajor organic feedstuff prices.",
      "versionDate": "2025-06-24",
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
        "updateDate": "2025-07-11T17:39:45Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4110ih.xml"
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
      "title": "The Organic Dairy Data Collection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "The Organic Dairy Data Collection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the improved collection of data for organic dairy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T04:03:43Z"
    }
  ]
}
```
