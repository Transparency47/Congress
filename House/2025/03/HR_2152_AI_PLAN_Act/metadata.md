# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2152
- Title: AI PLAN Act
- Congress: 119
- Bill type: HR
- Bill number: 2152
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-18T19:15:53Z
- Update date including text: 2026-05-18T19:15:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2152",
    "number": "2152",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "AI PLAN Act",
    "type": "HR",
    "updateDate": "2026-05-18T19:15:53Z",
    "updateDateIncludingText": "2026-05-18T19:15:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
        "item": [
          {
            "date": "2026-05-13T15:51:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-14T13:06:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CT"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AK"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2152ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2152\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Nunn of Iowa (for himself and Mr. Himes ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require a strategy to defend against the economic and national security risks posed by the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Artificial Intelligence Practices, Logistics, Actions, and Necessities Act or the AI PLAN Act .\n#### 2. Strategy to defend against risks posed by the use of artificial intelligence\n##### (a) Sense of Congress\nIt is the sense of Congress that the development and use of artificial intelligence in the commission of financial crimes by adversarial actors poses a significant risk to the national and economic security of the United States.\n##### (b) Strategy To defend against risks posed by misinformation, fraud, and financial crime conducted with artificial intelligence\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act and annually thereafter, the Secretary of the Treasury, the Secretary of Homeland Security, and the Secretary of Commerce, in consultation with the officials specified in paragraph (3), shall jointly submit to Congress a report that includes the following:\n**(A)**\nA description of interagency policies and procedures to defend United States financial markets, United States persons, United States businesses, and global supply chains from the national and economic security risks posed by the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation.\n**(B)**\nAn itemized list of readily available resources, hardware, software, and technologies that can be immediately utilized to combat the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation.\n**(C)**\nAn itemized list of resources, hardware, software, technologies, people, and budgetary estimates needed to help Federal departments and agencies to combat the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation.\n**(2) Considerations**\nReports required pursuant to paragraph (1) shall take the following risks into consideration:\n**(A)**\nDeepfakes.\n**(B)**\nVoice cloning.\n**(C)**\nForeign election interference.\n**(D)**\nSynthetic Identities.\n**(E)**\nFalse flags and false signals that disrupt market operations.\n**(F)**\nOverall digital fraud.\n**(3) Officials specified**\nThe officials specified in this paragraph are the following:\n**(A)**\nThe United States Trade Representative.\n**(B)**\nThe Attorney General.\n**(C)**\nThe Chairman of the Board of Governors of the Federal Reserve System.\n**(D)**\nThe Director of the National Institute of Standards and Technology.\n**(E)**\nThe Under Secretary of Commerce for Industry and Security.\n**(F)**\nThe Chairman of the Securities and Exchange Commission.\n##### (c) Recommendations\nNot later than 90 days after each report under subsection (b) is submitted, the Secretary of the Treasury, the Secretary of Homeland Security, and the Secretary of Commerce shall jointly submit to Congress a set of recommendations relating to each such respective report that contain the following:\n**(1)**\nLegislative recommendations to address the risks posed by the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation.\n**(2)**\nBest practices to assist American businesses and government entities with risk mitigation and incident response to address the risks posed by the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation.",
      "versionDate": "2025-03-14",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-05-18T18:48:21Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-05-18T19:15:53Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-05-18T18:55:11Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-05-18T19:15:42Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-05-18T19:14:22Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-05-18T19:14:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-18T19:15:35Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-18T19:15:22Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-05-18T19:14:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-04-01T17:35:21Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2152ih.xml"
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
      "title": "AI PLAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI PLAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Artificial Intelligence Practices, Logistics, Actions, and Necessities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a strategy to defend against the economic and national security risks posed by the use of artificial intelligence in the commission of financial crimes, including fraud and the dissemination of misinformation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:37Z"
    }
  ]
}
```
