# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4652?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4652
- Title: Preventing Fraudulent ICE Impersonation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4652
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-23T15:33:50Z
- Update date including text: 2026-03-23T15:33:50Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4652",
    "number": "4652",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Preventing Fraudulent ICE Impersonation Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-23T15:33:50Z",
    "updateDateIncludingText": "2026-03-23T15:33:50Z"
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
          "date": "2025-07-23T14:15:10Z",
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
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4652ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4652\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Espaillat (for himself and Mr. Correa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo enhance penalties for the unauthorized use and sale of Immigration and Customs Enforcement apparel and insignia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Fraudulent ICE Impersonation Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUnauthorized individuals have impersonated U.S. Immigration and Customs Enforcement (ICE) officers, causing fear and distrust in communities.\n**(2)**\nThe unauthorized use of ICE insignia and apparel poses a significant risk to public safety, undermines trust in law enforcement, and facilitates fraudulent activities.\n**(3)**\nStrengthening penalties and restricting the sale of ICE-branded apparel and insignia is necessary to protect communities from fraud and abuse.\n#### 3. Prohibition on unauthorized use of ice apparel and insignia\n##### (a) Unlawful Impersonation of an ICE Officer\n**(1) In general**\nIt shall be unlawful for any individual who is not an officer or employee of the Department of Homeland Security, acting within the scope of their official duties, to wear, display, or possess apparel, badges, insignia, or other items bearing the words ICE or Immigration and Customs Enforcement in a manner that could reasonably be interpreted as an attempt to impersonate a Federal law enforcement officer.\n**(2) Penalty**\nAny person who violates this subsection shall be fined under title 18, United States Code, imprisoned for not more than 7 years, or both.\n##### (b) Prohibition on Sale of ICE Apparel and Insignia\n**(1) In general**\nIt shall be unlawful for any individual or entity to manufacture, sell, offer for sale, or distribute any apparel, badge, or insignia bearing the official marks, logos, or designations of the U.S. Immigration and Customs Enforcement without express authorization from the Department of Homeland Security.\n**(2) Civil penalty**\nAny person or entity who violates this subsection shall be subject to a civil penalty of not more than $100,000 per violation.\n#### 4. Seizure and forfeiture\n##### (a) Seizure and forfeiture\nAny unauthorized ICE apparel or insignia manufactured, sold, distributed, or possessed in violation of this Act shall be subject to seizure and forfeiture in accordance with chapter 46 of title 18, United States Code.\n##### (b) Sentencing enhancement\nThe United States Sentencing Commission shall take such actions as may be necessary to provide that impersonation of an immigration official shall result in an enhancement of any term of imprisonment of no less than 6 months.\n#### 5. Public awareness and reporting mechanism\n##### (a)\nThe Secretary of Homeland Security shall establish a public awareness campaign to inform communities about the dangers of individuals impersonating ICE officers and provide resources for reporting such activities.\n##### (b)\nThe Secretary shall also establish a national reporting mechanism, including a dedicated hotline and online portal, to facilitate the reporting of individuals impersonating ICE officers.\n##### (c)\nNot later than 180 days after the date of enactment of this Act and every 180 days thereafter, the Comptroller General of the United States shall conduct a study on the impersonation of immigration officials and the underlying factors that should be considered for any potential solution to the issue, and submit thereon a report to Congress.\n#### 6. Rulemaking\nThe Secretary of Homeland Security shall issue regulations necessary to carry out this Act not later than 180 days after the date of enactment.\n#### 7. Definition\nIn this Act\u2014\n**(1)**\nthe term ICE means U.S. Immigration and Customs Enforcement; and\n**(2)**\nthe term official means\u2014\n**(A)**\na public official, as such term is defined in section 201(a)(1) of title 18, United States Code; and\n**(B)**\na person who has been selected to be a public official, as such term is defined in section 201(a)(2) of title 18, United States Code.",
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
        "name": "Immigration",
        "updateDate": "2025-09-12T14:07:32Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4652ih.xml"
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
      "title": "Preventing Fraudulent ICE Impersonation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Fraudulent ICE Impersonation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance penalties for the unauthorized use and sale of Immigration and Customs Enforcement apparel and insignia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T05:18:34Z"
    }
  ]
}
```
