# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6859?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6859
- Title: HOTDOG Act
- Congress: 119
- Bill type: HR
- Bill number: 6859
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-21T18:58:16Z
- Update date including text: 2026-01-21T18:58:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6859",
    "number": "6859",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "HOTDOG Act",
    "type": "HR",
    "updateDate": "2026-01-21T18:58:16Z",
    "updateDateIncludingText": "2026-01-21T18:58:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:00:10Z",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-18",
      "state": "LA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "VA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6859ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6859\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Mr. Goldman of New York (for himself, Mr. Deluzio , Mr. Ryan , Mr. Garcia of California , Mr. Garc\u00eda of Illinois , Mr. Veasey , Mr. Carter of Louisiana , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Trade Commission to conduct a study on certain concession pricing practices, and for other purposes.\n#### 1. Short title\nThis Act may cited as the Honest Oversight of Ticketed Dining and Onsite Grub Act or the HOTDOG Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMany sports venues receive significant public investments through direct grants, State and local tax credits, economic development incentives, and tax-exempt bonds.\n**(2)**\nIn 2025, the cost of concessions at major sporting events and concerts are unaffordable for the average American family.\n**(3)**\nAt Madison Square Garden, the average price of a beer is $16, more than twice the average in New York City, making it the third most expensive among NBA arenas.\n**(4)**\nAt Highmark Stadium, home of the Buffalo Bills, beer costs $10 on average, which is double the price fans would pay at a nearby bar across the street.\n**(5)**\nFans across music concerts and professional sports, including the National Basketball Association, National Football League, National Hockey League, and Major League Baseball, face exorbitant concession prices in addition to already high-ticket costs.\n**(6)**\nStreet pricing, a model that aligns concession pricing inside a venue with prices for comparable items in surrounding communities, has been adopted by certain venues to make concessions more affordable, producing benefits for both businesses and consumers.\n**(7)**\nFans and travelers attending events at venues supported by their tax dollars deserve clear, transparent, and fair pricing of food and beverage concessions.\n#### 3. Study on concession pricing practices\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Commission shall conduct a study with respect to concession pricing practices at a nationwide sample of covered venues that includes information relating to the following:\n**(1)**\nThe price of food and drink items offered for sale by such venues.\n**(2)**\nA comparison between such prices and the price of the same or similar food and drink items offered for sale by the communities surrounding such venues, including bars and restaurants.\n**(3)**\nPricing practices at such venues, including the use of any of the following by such venues:\n**(A)**\nDynamic pricing.\n**(B)**\nService fees.\n**(C)**\nPromotions such as value deals.\n**(4)**\nThe extent to which such venues disclose the price of food and drink items offered for sale by such venues prior to purchase, including by listing such prices online and disclosing such prices at the point of entry of such venues.\n**(5)**\nConsumer-friendly pricing policies that balance consumer access to affordable food and drink items with the cost of venue operations, including price caps on the price of such food and drink items and menu options for such food and drink items offered at a reduced price.\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Commission shall submit to Congress a report that includes information relating to the following:\n**(1)**\nThe results of the study conducted under subsection (a).\n**(2)**\nRecommendations for legislative, regulatory, and industry action with respect to improving affordability and transparency with respect to concession pricing practices.\n##### (c) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered venue**\nThe term covered venue means a stadium or arena that\u2014\n**(A)**\nis used for a professional sports exhibition or game, a music concert, or any other comparable event (as determined by the Commission) for at least 5 days per year;\n**(B)**\nwas constructed or operated with funds from a public subsidy, including funds from a direct grant, a State or local tax credit, an economic development incentive, or a tax-exempt bond;\n**(C)**\nrequires ticketed entry for consumers; and\n**(D)**\noffers food and drink items for sale to such consumers.\n**(3) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory or possession of the United States, and each federally recognized Indian Tribe.",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-21T16:40:02Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6859ih.xml"
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
      "title": "HOTDOG Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T18:58:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOTDOG Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T18:58:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honest Oversight of Ticketed Dining and Onsite Grub Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T18:58:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Trade Commission to conduct a study on certain concession pricing practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:36Z"
    }
  ]
}
```
