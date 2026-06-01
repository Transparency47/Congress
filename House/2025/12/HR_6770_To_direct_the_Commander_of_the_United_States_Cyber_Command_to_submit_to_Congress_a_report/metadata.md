# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6770
- Title: Scam Defense Strategy Act
- Congress: 119
- Bill type: HR
- Bill number: 6770
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-06T20:00:25Z
- Update date including text: 2026-01-06T20:00:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6770",
    "number": "6770",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Scam Defense Strategy Act",
    "type": "HR",
    "updateDate": "2026-01-06T20:00:25Z",
    "updateDateIncludingText": "2026-01-06T20:00:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6770ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6770\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Vindman (for himself and Mr. Finstad ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Commander of the United States Cyber Command to submit to Congress a report regarding recommended actions in cyberspace to defend the United States against transnational organized crime networks linked to the Chinese Communist Party that operate digital scams.\n#### 1. Short title\nThis Act may be cited as the Scam Defense Strategy Act .\n#### 2. Transnational organized crime networks\n##### (a) Findings\nCongress finds the following:\n**(1)**\nAccording to estimates from the United States Institutes of Peace, China-linked transnational organized crime groups that operate fraud farms in Southeast Asia steal nearly $43,800,000,000 annually through digital scams.\n**(2)**\nSuch scams increasingly affect Americans and disproportionately target vulnerable populations such as the elderly and socially isolated.\n**(3)**\nAccording to the Federal Trade Commission, in 2024 alone\u2014\n**(A)**\n246,783 scam text messages were reported, resulting in $469,000,000 in losses to Americans;\n**(B)**\n371,664 scam emails were reported, resulting in $502,000,000 in losses to Americans; and\n**(C)**\n284,651 scam phone calls were reported, resulting in $948,000,000 in losses to Americans.\n**(4)**\nTransnational organized crime groups maintain documented ties to the Chinese Communist Party. Chinese officials and state-owned enterprises have provided direct support for the construction and operation of facilities linked to transnational organized crime, raising serious concerns about a coordinated campaign of foreign interference and sabotage.\n**(5)**\nThe involvement of the Chinese Communist Party in transnational organized crime networks presents an urgent national security threat. These networks funnel financial assets and sensitive personal information of United States citizens to a hostile foreign power, undermining American economic security and individual privacy.\n**(6)**\nSuch transnational organized crime networks have deeply imbedded themselves into Southeast Asian economies, exerting destabilizing influence across the region.\n**(7)**\nProceeds from scams operated by these transnational crime networks are used to fund warlords and ongoing civil conflicts, compounding regional instability.\n**(8)**\nTransnational organized crime networks have trafficked an estimated 300,000 individuals into cyber scam operations across Southeast Asia. Victims, including United States citizens, are forced to work under conditions that the U.S.-China Economic and Security Review Commission compares to modern slavery. The United Nations has warned that human trafficking tied to these scam centers has reached the level of a humanitarian and human rights crisis.\n**(9)**\nThe U.S.-China Economic and Security Review has acknowledged credible reports linking scam facilities in the Philippines to Chinese espionage activity. These facilities are being constructed near air bases strategically important to United States operations, including Clark Air Base and Basa Air Base, a key site under the Enhanced Defense Cooperative Agreement. Philippine intelligence has provided compelling evidence that these compounds have been used for surveillance and cyber intrusions.\n**(10)**\nThe Chinese government has used the presence of Chinese transnational organized crime networks in Southeast Asia to pressure regional governments to allow a greater role for Chinese security forces, which threatens national sovereignty and regional stability.\n**(11)**\nTransnational organized crime networks endanger American defense priorities as well as democracy, good governance, and stability worldwide by co-opting local elites, undermining law enforcement, weakening state authority, and threatening the strategic interests of the United States in building a free and open Indo-Pacific.\n**(12)**\nAn effective response by the United States Government will require a coordinated, whole-of-government effort drawing on the competencies of Federal agencies in information collection, financial enforcement, diplomatic engagement, defense and intelligence preparedness, and law enforcement.\n##### (b) Report\nNot later than 6 months after the date of the enactment of this Act, the Commander of the United States Cyber Command shall submit to Congress a report regarding recommended actions for the Secretary of Defense to take in cyberspace to defend the United States and United States citizens, assets, and interests against transnational organized crime networks linked to the Chinese Communist Party that operate digital scams.",
      "versionDate": "2025-12-16",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T20:00:24Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6770ih.xml"
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
      "title": "Scam Defense Strategy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Scam Defense Strategy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Commander of the United States Cyber Command to submit to Congress a report regarding recommended actions in cyberspace to defend the United States against transnational organized crime networks linked to the Chinese Communist Party that operate digital scams.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:30Z"
    }
  ]
}
```
