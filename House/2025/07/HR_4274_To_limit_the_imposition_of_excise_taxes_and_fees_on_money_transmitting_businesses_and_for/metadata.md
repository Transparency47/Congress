# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4274
- Title: Remittance Expense Minimization and Integrity for Transfers Act
- Congress: 119
- Bill type: HR
- Bill number: 4274
- Origin chamber: House
- Introduced date: 2025-07-02
- Update date: 2025-07-30T13:54:35Z
- Update date including text: 2025-07-30T13:54:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-02: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-02: Introduced in House

## Actions

- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Introduced in House
- 2025-07-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-02",
    "latestAction": {
      "actionDate": "2025-07-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4274",
    "number": "4274",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Remittance Expense Minimization and Integrity for Transfers Act",
    "type": "HR",
    "updateDate": "2025-07-30T13:54:35Z",
    "updateDateIncludingText": "2025-07-30T13:54:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-02",
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
          "date": "2025-07-02T13:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-02T13:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "TX"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-02",
      "state": "IL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "VA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4274ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4274\nIN THE HOUSE OF REPRESENTATIVES\nJuly 2, 2025 Mr. Liccardo (for himself, Mr. Correa , Mr. Torres of New York , Mr. Vargas , Mr. Vicente Gonzalez of Texas , Mr. Espaillat , Mr. Garc\u00eda of Illinois , and Mr. Subramanyam ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the imposition of excise taxes and fees on money transmitting businesses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Remittance Expense Minimization and Integrity for Transfers Act or the REMIT Act of 2025 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nRemittances are essential cross-border flows of funds from diaspora community members who sent money or goods from wherever they reside to their home countries. While typically only a few hundred dollars per transaction, the total remittance market is estimated by the International Monetary Fund to be over $500,000,000,000 globally. These funds are so significant to the recipient countries that they can make up percentages of their Gross Domestic Product and are significant factors in the elimination of poverty and the stabilization of economies.\n**(2)**\nA 2016 report from Government Accountability Office found that fines on remittances did not stop the flow of remittances, but rather led to consumers using unregulated transfer methods.\n**(3)**\nIn a May 2023 report, the Congressional Research Service corroborated that many alternative remittance systems, also known as Informal Value Transfer Systems (IVTS), lack of documentation and their anonymity and informality can make them attractive for money laundering, terrorist financing, and other illegal purposes.\n**(4)**\nA July 5, 2022, Department of the Treasury Financial Crimes Enforcement Network reiterated longstanding financial-crime concerns about IVTS and that IVTS are being used to fund attempted terrorist attacks, including against the United States.\n**(5)**\nThe 2024 National Money Laundering Risk Assessment by the U.S. Department of the Treasury highlighted that drug traffickers are turning to professional money launderers to launder their ill-gotten proceeds. In particular, drug traffickers use Chinese Money Laundering Organizations (CMLOs), which employ IVTS, among other means, to move value across borders without needing to use the U.S. financial system. While CMLOs provide money laundering services for Transnational Criminal Organizations, their primary objective is to acquire and subsequently sell United States Dollars (and other foreign currencies) using IVTS schemes to assist Chinese nationals seeking to evade the Chinese government\u2019s currency controls. CMLOs operating in the United States increasingly need access to significant amounts of USD to satisfy the demand for IVTS services by cartels, Chinese nationals, and other customers of their services.\n**(6)**\nTo obtain dollars, CMLOs work with South American drug cartels and also anyone who needs their underground cross-border money transfer services.\n**(7)**\nCMLOs are just one example of the organizations that would benefit from the increased demand created by any attempt to limit licit movement of remittances across borders.\n#### 3. Excise taxes and fees\n##### (a) In general\nNotwithstanding any other provision of law. it is not permissible for the Federal Government to require a money transmitting business to pay an excise tax or fee unless the Secretary of the Treasury has certified to Congress, including the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate that such excise tax or fee\u2014\n**(1)**\nwill not increase the potential for money laundering or other financial crime activities; and\n**(2)**\nwill not impose an undue burden on any money transmitting business.\n##### (b) Money transmitting business defined\nIn this section, the term money transmitting business means a licensed sender of money or any other person who engages as a business in the transmission of currency, funds, or value that substitutes for currency, including any person who engages as a business in an informal money transfer system or any network of people who engage as a business in facilitating the transfer of money domestically or internationally outside of the conventional financial institutions system.",
      "versionDate": "2025-07-02",
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
        "updateDate": "2025-07-30T13:54:35Z"
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
      "date": "2025-07-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4274ih.xml"
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
      "title": "To limit the imposition of excise taxes and fees on money transmitting businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:31:31Z"
    },
    {
      "title": "Remittance Expense Minimization and Integrity for Transfers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Remittance Expense Minimization and Integrity for Transfers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T04:23:24Z"
    }
  ]
}
```
