# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5900?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5900
- Title: SCAM Act
- Congress: 119
- Bill type: HR
- Bill number: 5900
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-11-19T17:23:23Z
- Update date including text: 2025-11-19T17:23:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5900",
    "number": "5900",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "SCAM Act",
    "type": "HR",
    "updateDate": "2025-11-19T17:23:23Z",
    "updateDateIncludingText": "2025-11-19T17:23:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5900ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5900\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Vindman (for himself and Mr. Baird ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo direct the Department of Defense to establish a joint task force to investigate transnational cybercrimes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Cross-border Attacks and Manipulation Act or the SCAM Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to estimates from the United States Institute of Peace, China-linked transnational organized crime (TOC) groups operating fraud farms in Southeast Asia are stealing nearly $43,800,000,000 annually through digital scams.\n**(2)**\nThese scams increasingly affect Americans, disproportionately targeting populations such as the elderly and socially isolated.\n**(3)**\nAccording to the Federal Trade Commission (FTC), in 2024 alone\u2014\n**(A)**\n246,783 scam text messages were reported, resulting in $469,000,000 in losses to Americans;\n**(B)**\n371,664 scam emails were reported, leading to $502,000,000 in losses to Americans; and\n**(C)**\n284,651 scam phone calls were reported, causing $948,000,000 in losses to Americans.\n**(4)**\nTransnational organized crime (TOC) groups maintain documented ties to the Chinese Communist Party (CCP). Chinese officials and state-owned enterprises (SOEs) have provided direct support for the construction and operation of TOC-linked facilities, raising serious concerns about a coordinated campaign of foreign interference and sabotage.\n**(5)**\nThe CCP\u2019s involvement in TOC networks presents an urgent national security threat. These networks funnel financial assets and sensitive personal information of U.S. citizens to a hostile foreign power, undermining both American economic security and individual privacy.\n**(6)**\nThese criminal networks have deeply embedded themselves into Southeast Asian economies, exerting destabilizing influence across the region.\n**(7)**\nProceeds from these scams are used to fund warlords and fuel ongoing civil conflicts, compounding regional instability.\n**(8)**\nTOC networks have trafficked an estimated 300,000 individuals into cyber scam operations across Southeast Asia. Victims, including United States citizens, are forced to work under conditions that the U.S.-China Economic and Security Review Commission compares to modern slavery. The United Nations has warned that human trafficking tied to these scam centers has reached the level of a humanitarian and human rights crisis.\n**(9)**\nThe U.S.-China Economic and Security Review Commission has acknowledged credible reports linking scam compounds in the Philippines to Chinese espionage activity. These facilities are being constructed near air bases strategically important to U.S. operations, including Clark Air Base and Basa Air Base, which is part of the Enhanced Defense Cooperation Agreement. The Philippine intelligence community has provided compelling evidence that these compounds have been used for surveillance and cyber intrusions.\n**(10)**\nThe Chinese government has used the presence of Chinese TOC networks in Southeast Asia to pressure regional governments to allow a greater role for Chinese security forces. This effort threatens national sovereignty and regional stability.\n**(11)**\nTOC networks endanger American defense priorities as well as democracy, good governance, and stability around the world by co-opting local elites, undermining law enforcement, weakening state authority, and threatening the United States' strategic interest in building a free and open Indo-Pacific.\n**(12)**\nAn effective response by the United States Government will require a coordinated, whole-of-government effort that draws on the competencies of Federal agencies in information collection, financial enforcement, diplomatic engagement, defense and intelligence preparedness, and law enforcement.\n#### 3. Joint task force to investigate transnational cybercrimes\n##### (a) Establishment\n**(1) In general**\nThe Secretary of Defense, acting through the head of U.S. Cyber Command and in coordination with the heads of other appropriate agencies, shall establish a joint task force to coordinate efforts to investigate, disrupt, and protect citizens of the United States from transnational cybercrimes and foreign-operated scam networks, including fraudulent text and direct messing centers and other digital fraud schemes targeting citizens of the United States.\n**(2) Membership**\nThe task force shall, at a minimum, be composed of\u2014\n**(A)**\nan official of the Department of State, including\u2014\n**(i)**\nthe Assistant Secretary for Emerging Threats;\n**(ii)**\nthe Assistant Secretary for International Narcotics and Law Enforcement; and\n**(iii)**\nthe Assistant Secretary for Democracy, Human Rights, and Labor;\n**(B)**\nofficials of the Department of Defense, including U.S. Cyber Command and the National Mission Force;\n**(C)**\nan official of the Office of the Director of National Intelligence;\n**(D)**\nan official of the Federal Trade Commission;\n**(E)**\nan official of the Federal Communications Commission;\n**(F)**\nofficials of the Office of Foreign Assets Control and the Financial Crimes Enforcement Network of the Department of the Treasury;\n**(G)**\nofficials of the Department of Justice, including officials from\u2014\n**(i)**\nthe Criminal Division, including the International Unit of the Money Laundering and Asset Recovery Section;\n**(ii)**\nthe Office of International Affairs;\n**(iii)**\nthe National Security Division; and\n**(iv)**\nthe Office of the Cyber Ambassador;\n**(H)**\nan official of the Federal Bureau of Investigation\u2019s Internet Crime Complaint Center;\n**(I)**\nrepresentatives of State and local governments that\u2014\n**(i)**\nare leading efforts to counter cybercrimes; or\n**(ii)**\nare disproportionately affected by cybercrimes; and\n**(J)**\nrepresentatives of relevant expert non-profit organizations.\n**(3) Leadership**\nThe members of the task force, in consultation with the leadership of the Department of Defense, may assign responsibility to an appropriate office within the Department of Defense to serve as the lead for the task force to coordinate the preparation and submission of the report required by subsection (c) and hold offices and agencies responsible for implementation.\n##### (b) Priority\nIn carrying out its duties under subsection (a) and in preparing the report under subsection (c), the task force shall prioritize work related to scam operations with ties to the Chinese Communist Party in the Indo-Pacific region.\n##### (c) Report\nNot later than one year after the date of enactment of this Act, the task force established under subsection (a) shall submit to the Committees on Armed Services of the House of Representatives and of the Senate a report\u2014\n**(1)**\nidentifying emerging trends related to the scam operations described in subsection (a) that are tied to international criminal organizations, including efforts to\u2014\n**(A)**\nscam and steal data from United States persons;\n**(B)**\ncultivate relationships with adversarial governments and foreign intelligence services;\n**(C)**\nacquire land in proximity to United States military installations and United States treaty allies\u2019 and partners\u2019 military installations;\n**(D)**\nleverage, collaborate with, or place foreign nationals of concern in sensitive positions within Indo-Pacific regional governments;\n**(E)**\nundermine United States diplomatic engagement, peacekeeping operations, and security cooperation efforts throughout the world, with a priority on the Indo-Pacific region;\n**(F)**\nacquire territory or influence around critical waterways; and\n**(G)**\nconstruct militarily-capable infrastructure such as airports;\n**(2)**\nrecommending policy options for the Federal Government, Congress, and nongovernmental industry leaders to prevent and penalize the scam operations described in subsection (a) that are tied to international criminal organizations, which may include the use of sanctions, civil asset forfeiture, and action in cyberspace in defense of the United States, its persons, assets, and interests against the scam networks described in subsection (a), including\u2014\n**(A)**\nprotecting Americans\u2019 personal data and financial assets;\n**(B)**\nsafeguarding the sovereignty of United States allies and partners; and\n**(C)**\nsecuring United States military installations and United States treaty allies\u2019 and partners\u2019 military installations located near known or suspected scam compounds;\n**(3)**\nproposing a framework for a whole-of-society approach to support disproportionately affected demographic groups, communications platforms, States, and localities impacted by the scam networks described in subsection (a), including methods for timely dissemination of scam-related information and protective guidance through publicly accessible Federal facilities (including United States Postal Service locations, Social Security Administration field offices, military installations, and Department of Veterans Affairs facilities) and comparable State and local venues;\n**(4)**\nincluding an assessment and updates of the overall scale of scam centers in Southeast Asia and recent trendlines;\n**(5)**\ninformation about how the Chinese Government is exploiting the problem of scam centers to expand its security presence and influence in the region; and\n**(6)**\ninformation about government bodies, individual government officials, militias, and corporations in Southeast Asia that have ties to transnational criminal organizations or profit from scam centers.\n##### (d) Implementation\nThe task force shall assist in the implementation of any recommendations or proposals contained in the report submitted under subsection (c).\n##### (e) Sunset\nThe authority under this section shall sunset on the date that is 5 years after the date on which the task force submits the report under subsection (c).",
      "versionDate": "2025-10-31",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T17:23:22Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5900ih.xml"
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
      "title": "SCAM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCAM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Cross-border Attacks and Manipulation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Department of Defense to establish a joint task force to investigate transnational cybercrimes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T04:48:16Z"
    }
  ]
}
```
