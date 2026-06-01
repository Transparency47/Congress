# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4692?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4692
- Title: MAMDANI Act
- Congress: 119
- Bill type: HR
- Bill number: 4692
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-09-17T17:21:48Z
- Update date including text: 2025-09-17T17:21:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4692",
    "number": "4692",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "MAMDANI Act",
    "type": "HR",
    "updateDate": "2025-09-17T17:21:48Z",
    "updateDateIncludingText": "2025-09-17T17:21:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
        "item": {
          "date": "2025-07-23T14:01:00Z",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4692ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4692\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Federal Trade Commission to conduct a study on the potential impacts of public grocery stores, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Measuring Adverse Market Disruption And National Impact Act or the MAMDANI Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe retail grocery sector is a critical component of the food supply chain and economy of the United States.\n**(2)**\nRecent proposals in various municipalities have advocated for public grocery stores.\n**(3)**\nSuch proposals raise questions about\u2014\n**(A)**\nthe competitive dynamics between public and private grocery stores with respect to pricing, market access, and consumer choice;\n**(B)**\nimpacts on farmers and food banks; and\n**(C)**\nlong-term sustainability.\n**(4)**\nThe Federal Trade Commission has expertise in analyzing competitive practices with respect to retail markets and is well positioned to assess the effects of government entry into consumer markets.\n#### 3. Study on impacts of public grocery stores\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Commission, in consultation with the Administrator of the Agricultural Marketing Service and the Administrator of the Food and Nutrition Service of the Department of Agriculture, shall conduct a study on the impacts of public grocery stores that includes an analysis of the following:\n**(1)**\nThe competitive impacts of such stores on the following:\n**(A)**\nSmall, medium, and large private grocery stores.\n**(B)**\nFarmers.\n**(C)**\nFood banks and other charitable organizations.\n**(D)**\nWholesale food prices and food supply chains, including impacts with respect to purchasing power, market share shifts, and local and regional food distribution networks.\n**(E)**\nThe retail grocery sector generally.\n**(2)**\nThe impacts of public grocery stores on consumer access, choice, and prices, including with respect to food deserts.\n**(3)**\nWhether public grocery stores would receive subsidies, tax exemptions, or regulatory advantages that may alter competition.\n**(4)**\nHow public grocery stores may affect local, regional, and national agriculture, including prices received by producers.\n**(5)**\nLong-term market impacts with respect to the retail grocery sector, including barriers for private entities to enter and exit such sector.\n**(6)**\nConcerns with respect to unfair competition or market distortion.\n##### (b) Use of existing data\nIn conducting the study under subsection (a), the Commission shall use available data of the Commission, the Department of Agriculture, and other relevant sources, including State and local economic development records, industry reports, and public procurement disclosures.\n##### (c) Report\nNot later than 1 year after the date of the completion of the study required under subsection (a), and annually thereafter, the Commission shall submit to Congress a report that includes information relating to the following:\n**(1)**\nThe results of such study.\n**(2)**\nRecommendations for administrative and legislative action with respect to any concerns identified in such study.\n##### (d) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Food bank**\nThe term food bank means a nonprofit organization that collects, warehouses, and distributes donated or purchased food.\n**(3) Food desert**\nThe term food desert means a census tract that has a poverty rate of 20 percent or higher and has at least 500 residents that live more than 1 mile from a supermarket or large grocery store.\n**(4) Private grocery store**\nThe term private grocery store means a business that\u2014\n**(A)**\nis not owned by a Federal, State, or local government entity; and\n**(B)**\nsells general food products.\n**(5) Public grocery store**\nThe term public grocery store means a business that\u2014\n**(A)**\nis directly owned or operated by a Federal, State, or local government entity; and\n**(B)**\nsells general food products.",
      "versionDate": "2025-07-23",
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
        "name": "Commerce",
        "updateDate": "2025-09-17T17:21:48Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4692ih.xml"
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
      "title": "MAMDANI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAMDANI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Measuring Adverse Market Disruption And National Impact Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Trade Commission to conduct a study on the potential impacts of public grocery stores, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:35Z"
    }
  ]
}
```
