# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5315
- Title: FAIR Act
- Congress: 119
- Bill type: HR
- Bill number: 5315
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-22T19:42:22Z
- Update date including text: 2025-09-22T19:42:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5315",
    "number": "5315",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "FAIR Act",
    "type": "HR",
    "updateDate": "2025-09-22T19:42:22Z",
    "updateDateIncludingText": "2025-09-22T19:42:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5315ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5315\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Ms. Hageman (for herself and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the Federal procurement of large language models not developed in accordance with unbiased AI principles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Artificial Intelligence Realization Act of 2025 or the FAIR Act .\n#### 2. Prohibition on Federal procurement of certain large language models\n##### (a) Policy of the United States\nIt is the policy of the United States to promote the innovation and use of trustworthy artificial intelligence.\n##### (b) In general\nTo advance the policy established under subsection (a), the head of each agency shall, procure after the date of the enactment of this Act only those large language models developed in accordance with the following principles:\n**(1)**\nLarge language models shall be truthful in responding to user prompts seeking factual information or analysis.\n**(2)**\nLarge language models shall prioritize historical accuracy, scientific inquiry, and objectivity, and shall acknowledge uncertainty where reliable information is incomplete or contradictory.\n**(3)**\nLarge language models shall be neutral, nonpartisan tools that do not manipulate responses in favor of ideological dogmas such as diversity, equity, and inclusion.\n**(4)**\nDevelopers of large language models shall not intentionally encode partisan or ideological judgments into a large language model output unless those judgments are prompted by or otherwise readily accessible to the end user.\n##### (c) Definitions\nIn this Act:\n**(1) Agency**\nThe term agency \u2014\n**(A)**\nmeans\u2014\n**(i)**\nan executive department (as such term is defined in section 101 of title 5, United States Code);\n**(ii)**\na military department (as such term is defined in section 102 of title 5, United States Code);\n**(iii)**\nan independent establishment (as such term is defined in section 104 of title 5, United States Code); and\n**(iv)**\na wholly owned Government corporation (as such term is defined in section 9101 of title 31, United States Code); and\n**(B)**\ndoes not include the Government Accountability Office.\n**(2) Large language model**\nThe term large language model means a generative AI model trained on vast, diverse datasets that enable the model to generate natural-language responses to user prompts.",
      "versionDate": "2025-09-11",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-22T19:42:22Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5315ih.xml"
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
      "title": "FAIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-20T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Artificial Intelligence Realization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-20T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Federal procurement of large language models not developed in accordance with unbiased AI principles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-20T07:33:29Z"
    }
  ]
}
```
