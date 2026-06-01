# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4301
- Title: PEACE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4301
- Origin chamber: House
- Introduced date: 2025-07-07
- Update date: 2025-07-31T12:30:58Z
- Update date including text: 2025-07-31T12:30:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-07: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-07: Introduced in House

## Actions

- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-07",
    "latestAction": {
      "actionDate": "2025-07-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4301",
    "number": "4301",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "PEACE Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-31T12:30:58Z",
    "updateDateIncludingText": "2025-07-31T12:30:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-07",
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
          "date": "2025-07-07T14:00:25Z",
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
          "date": "2025-07-07T14:00:20Z",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4301ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4301\nIN THE HOUSE OF REPRESENTATIVES\nJuly 7, 2025 Mr. Nunn of Iowa (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo secure a peaceful resolution to the Russia-Ukraine conflict by requiring the Secretary of the Treasury to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by certain foreign financial institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing the Escalation of Armed Conflict in Europe Act of 2025 or the PEACE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDuring the night of March 6\u20137, 2025, only one week after the President called for peace between Russia and Ukraine, the Russian military bombarded Ukrainian energy infrastructure and civilian residences.\n**(2)**\nDTEK, a Ukrainian gas producer, noted that the assault represented the sixth Russian attack on its Odesa facilities in just the preceding two and a half weeks.\n**(3)**\nOn March 7, 2025, the President published the following statement: Based on the fact that Russia is absolutely pounding Ukraine on the battlefield right now, I am strongly considering large scale Banking Sanctions, Sanctions, and Tariffs on Russia until a Cease Fire and FINAL SETTLEMENT AGREEMENT ON PEACE IS REACHED. To Russia and Ukraine, get to the table right now, before it is too late. .\n**(4)**\nDespite the President\u2019s calls for a peace settlement, Russia has continued to assault Ukraine, including an April 4 missile attack on Kryvyi Rih that killed 20 people and an April 13 strike on Sumy resulting in 35 deaths.\n**(5)**\nOn May 25, 2025, Russia launched its largest aerial attack of the war, deploying hundreds of drones and ballistic missiles throughout Ukrainian territory.\n**(6)**\nOn May 27, 2025, the President posted on social media with reference to Russian leader Vladimir Putin: He\u2019s playing with fire! .\n#### 3. Sanctions with respect to the Russian Federation\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury shall prescribe regulations to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by a foreign financial institution that knowingly provides significant financial services to\u2014\n**(1)**\nany foreign person designated for the imposition of sanctions with respect to the Russian Federation under\u2014\n**(A)**\nExecutive Orders 13660, 13661, 13662, 13685, or 14024; or\n**(B)**\ntitle II of the Countering America\u2019s Adversaries through Sanctions Act ( Public Law 114\u201344 ) or an amendment made by that title;\n**(2)**\na foreign financial institution subject to the prohibitions of Directive 2 under Executive Order 14024;\n**(3)**\nan entity listed in Annex 1 of Directive 3 under Executive Order 14024; or\n**(4)**\nany foreign person that the Secretary finds operates in the energy sector of the Russian Federation.\n##### (b) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n#### 4. Determination required\nNot later than 90 days after the date of enactment of this Act, the Secretary of the Treasury shall submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate determining whether the following are foreign persons described under section 3(a)(4):\n**(1)**\nGazprom.\n**(2)**\nRosneft.\n**(3)**\nLukoil.\n#### 5. Waiver\nWith respect to a foreign financial institution, the President may waive the requirements of section 3(a) for not more than 180 days at a time upon reporting to Congress that\u2014\n**(1)**\nthe waiver advances the objective of resolving the national emergency described in any Executive Order listed under section 3(a)(1); or\n**(2)**\nthe waiver is important to the national interest of the United States, provided that the President includes a detailed explanation of the reasons therefor.\n#### 6. Termination\nThis Act shall have no force or effect on the earlier of\u2014\n**(1)**\n30 days after the date that the President reports to Congress that the Russian Federation has ceased destabilizing activities with respect to the sovereignty and territorial integrity of Ukraine; or\n**(2)**\nthe date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-07-07",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-22",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 1."
      },
      "number": "4346",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PEACE Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-07-29T22:05:20Z"
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
      "date": "2025-07-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4301ih.xml"
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
      "title": "PEACE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEACE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing the Escalation of Armed Conflict in Europe Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To secure a peaceful resolution to the Russia-Ukraine conflict by requiring the Secretary of the Treasury to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by certain foreign financial institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:33:24Z"
    }
  ]
}
```
