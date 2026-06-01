# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5226
- Title: Deceptive Downsizing Prohibition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5226
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2026-04-28T08:06:24Z
- Update date including text: 2026-04-28T08:06:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-09: Introduced in House

## Actions

- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5226",
    "number": "5226",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Deceptive Downsizing Prohibition Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:24Z",
    "updateDateIncludingText": "2026-04-28T08:06:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
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
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:04:00Z",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "LA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-09",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-09",
      "state": "DC"
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
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5226ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5226\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Mr. Correa (for himself, Mr. Fields , Mr. Jackson of Illinois , Mr. Johnson of Georgia , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Trade Commission to promulgate regulations that prohibit the practice of deceptive downsizing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deceptive Downsizing Prohibition Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nManufacturers of consumer products, including food, are reducing the size of such products while continuing to use packaging designed for the same or similar product of a larger size.\n**(2)**\nThe practice of deceptive downsizing substantially harms consumers and reduces the purchasing power of consumers.\n**(3)**\nConsumers frequently do not appreciate or recognize that the size of a consumer product has changed until after the purchase, if ever.\n**(4)**\nThe trend toward producing consumer products of reduced size without reducing the price has driven inflation, causing substantial injury to consumers that is not reasonably avoidable.\n**(5)**\nThe Federal Government plays an essential role in protecting consumers from unfair or deceptive acts or practices, including ensuring manufacturers of consumer products do not deceive customers.\n**(6)**\nThis Act shall protect consumers by prohibiting manufacturers of consumer products from selling such products, regardless of price or cost, of reduced size in packaging previously used for the same or similar product of a larger size.\n**(7)**\nConsumers need clear, conspicuous, and easily understandable notice of a change in the size of a consumer product and simply including the reduced size on the packaging without context or highlighting does not provide sufficient notice to consumers to avoid a violation of this Act.\n#### 3. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Consumer product**\nThe term consumer product has the same meaning given the term in section 101 of the Magnuson-Moss Warranty\u2014Federal Trade Commission Improvement Act ( 15 U.S.C. 2301 ).\n**(3) Deceptive downsizing**\nThe term deceptive downsizing means the practice of a manufacturer of a consumer product selling such a product of reduced size using the same or substantially similar packaging that was used for any prior version of the same or substantially similar product that was of larger size.\n**(4) Larger size**\nThe term larger size means a consumer product of greater volume, size, mass, weight, or quantity relative to the consumer product that is the subject of the alleged deceptive downsizing.\n**(5) Reduced size**\nThe term reduced size means a reduction in volume, size, mass, weight, or quantity of a consumer product relative to any prior version of the same or substantially similar consumer product.\n#### 4. Prohibition on deceptive downsizing\n##### (a) Prohibition\nA manufacturer of a consumer product may not engage in deceptive downsizing with respect to such consumer product.\n##### (b) Safe harbor\nA manufacturer of a consumer product shall not be liable for deceptive downsizing with respect to such consumer product in violation of subsection (a) if the manufacturer sells the consumer product in a reduced size using the same or substantially similar packaging as for the larger size of the consumer product and\u2014\n**(1)**\nthe manufacturer provides notice on the principal display panel of such packaging that the consumer product is of reduced size; and\n**(2)**\nsuch notice\u2014\n**(A)**\nis conspicuous, clear, and easy for consumers to read and understand; and\n**(B)**\nstates the larger size of the consumer product and the reduced size of the consumer product.\n#### 5. Regulations relating to prohibition on deceptive downsizing\nThe Commission may promulgate, under section 553 of title 5, United States Code, any regulations the Commission determines necessary to carry out the provisions of this Act.\n#### 6. Enforcement by Federal Trade Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act shall be treated as a violation of section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n##### (b) Powers of Commission\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act, and any person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Rule of construction\nNothing in this Act may be construed to limit the authority of the Commission under any other provision of law.",
      "versionDate": "2025-09-09",
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
            "name": "Consumer affairs",
            "updateDate": "2025-09-16T20:53:55Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-09-16T21:02:08Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-09-16T20:54:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-09-15T17:53:48Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5226ih.xml"
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
      "title": "Deceptive Downsizing Prohibition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deceptive Downsizing Prohibition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Trade Commission to promulgate regulations that prohibit the practice of deceptive downsizing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-13T03:48:23Z"
    }
  ]
}
```
