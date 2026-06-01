# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3722
- Title: Do or Dye Act
- Congress: 119
- Bill type: HR
- Bill number: 3722
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-01-23T09:06:40Z
- Update date including text: 2026-01-23T09:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3722",
    "number": "3722",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Do or Dye Act",
    "type": "HR",
    "updateDate": "2026-01-23T09:06:40Z",
    "updateDateIncludingText": "2026-01-23T09:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:04:40Z",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CO"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3722ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3722\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mrs. Luna (for herself and Mr. Nehls ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to deem adulterated food containing certain color additives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Do or Dye Act .\n#### 2. Food containing certain color additives deemed adulterated\n##### (a) In general\nNotwithstanding the listing and certification (or exemption in effect with respect to such certification) of any qualified color additive or covered color additive pursuant to section 721 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379e )\u2014\n**(1)**\nbeginning on December 31, 2025\u2014\n**(A)**\na qualified color additive shall be deemed unsafe for use in or on food within the meaning of subsection (a) of such section; and\n**(B)**\na food that is, or it bears or contains, such a color additive is adulterated within the meaning of section 402(c) of such Act ( 21 U.S.C. 342(c) ); and\n**(2)**\nbeginning on December 31, 2026\u2014\n**(A)**\na covered color additive shall be deemed unsafe for use in or on food within the meaning of subsection (a) of such section; and\n**(B)**\na food that is, or it bears or contains, such a color additive is adulterated within the meaning of section 402(c) of such Act ( 21 U.S.C. 342(c) ).\n##### (b) Definitions\nIn this Act:\n**(1)**\nThe term covered color additive means the following color additives (as such term is defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )):\n**(A)**\nRed No. 40.\n**(B)**\nYellow No. 5.\n**(C)**\nYellow No. 6.\n**(D)**\nGreen No. 3.\n**(E)**\nBlue No. 1.\n**(F)**\nBlue No. 2.\n**(G)**\nAny additive that is substantially similar to the additives specified in subparagraphs (A) through (F).\n**(2)**\nThe term qualified color additive means the following color additives:\n**(A)**\nCitrus Red No. 2.\n**(B)**\nOrange B.\n**(C)**\nAny additive that is substantially similar to the additives specified in subparagraphs (A) and (B).",
      "versionDate": "2025-06-04",
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
        "name": "Health",
        "updateDate": "2025-06-24T13:30:30Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3722ih.xml"
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
      "title": "Do or Dye Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T09:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Do or Dye Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to deem adulterated food containing certain color additives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T09:33:25Z"
    }
  ]
}
```
