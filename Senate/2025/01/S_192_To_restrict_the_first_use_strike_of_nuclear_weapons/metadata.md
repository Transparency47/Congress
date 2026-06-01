# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/192?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/192
- Title: Restricting First Use of Nuclear Weapons Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 192
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2026-04-28T11:03:21Z
- Update date including text: 2026-04-28T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/192",
    "number": "192",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Restricting First Use of Nuclear Weapons Act of 2025",
    "type": "S",
    "updateDate": "2026-04-28T11:03:21Z",
    "updateDateIncludingText": "2026-04-28T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-01-22T20:37:22Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-22T20:37:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "OR"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "VT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-22",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "OR"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s192is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 192\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Markey (for himself, Mr. Merkley , Ms. Warren , Mr. Van Hollen , Mr. Welch , Mr. Sanders , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo restrict the first-use strike of nuclear weapons.\n#### 1. Short title\nThis Act may be cited as the Restricting First Use of Nuclear Weapons Act of 2025 .\n#### 2. Findings and declaration of policy\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Constitution gives Congress the sole power to declare war.\n**(2)**\nThe framers of the Constitution understood that the monumental decision to go to war, which can result in massive death and the destruction of civilized society, must be made by the representatives of the people and not by a single person.\n**(3)**\nAs stated by section 2(c) of the War Powers Resolution ( Public Law 93\u2013148 ; 50 U.S.C. 1541 ), the constitutional powers of the President as Commander-in-Chief to introduce United States Armed Forces into hostilities, or into situations where imminent involvement in hostilities is clearly indicated by the circumstances, are exercised only pursuant to (1) a declaration of war, (2) specific statutory authorization, or (3) a national emergency created by attack upon the United States, its territories or possessions, or its armed forces .\n**(4)**\nNuclear weapons are uniquely powerful weapons that have the capability to instantly kill millions of people, create long-term health and environmental consequences throughout the world, directly undermine global peace, and put the United States at existential risk from retaliatory nuclear strikes.\n**(5)**\nA first-use nuclear strike carried out by the United States would constitute a major act of war.\n**(6)**\nA first-use nuclear strike conducted absent a declaration of war by Congress would violate the Constitution.\n**(7)**\nThe President has the sole authority to authorize the use of nuclear weapons, an order which military officers of the United States must carry out in accordance with their obligations under the Uniform Code of Military Justice.\n**(8)**\nGiven its exclusive power under the Constitution to declare war, Congress must provide meaningful checks and balances to the President\u2019s sole authority to authorize the use of a nuclear weapon.\n##### (b) Declaration of policy\nIt is the policy of the United States that no first-use nuclear strike should be conducted absent a declaration of war by Congress.\n#### 3. Prohibition on conduct of first-use nuclear strikes\n##### (a) Prohibition\nNo Federal funds may be obligated or expended to conduct a first-use nuclear strike unless such strike is conducted pursuant to a war declared by Congress that expressly authorizes such strike.\n##### (b) First-Use nuclear strike defined\nIn this section, the term first-use nuclear strike means an attack using nuclear weapons against an enemy that is conducted without the Secretary of Defense and the Chairman of the Joint Chiefs of Staff first confirming to the President that there has been a nuclear strike against the United States, its territories, or its allies (as specified in section 3(b)(2) of the Arms Export Control Act ( 22 U.S.C. 2753(b)(2) )).",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-23",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "669",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restricting First Use of Nuclear Weapons Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-09-10T20:24:56Z"
          },
          {
            "name": "Military command and structure",
            "updateDate": "2025-09-10T20:25:10Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-09-10T20:25:21Z"
          },
          {
            "name": "Nuclear weapons",
            "updateDate": "2025-09-10T20:25:27Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-09-10T20:25:35Z"
          },
          {
            "name": "War and emergency powers",
            "updateDate": "2025-09-10T20:25:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-04-17T17:48:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s192",
          "measure-number": "192",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s192v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Restricting First Use of Nuclear Weapons Act of 2025 </strong></p><p>This bill prohibits using federal funds to conduct a first-use nuclear strike unless Congress expressly authorizes such a strike pursuant to a declaration of war. A first-use nuclear strike is an attack using nuclear weapons against an enemy without confirming that there has been a nuclear strike against the United States, its territories, or its allies.</p>"
        },
        "title": "Restricting First Use of Nuclear Weapons Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s192.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restricting First Use of Nuclear Weapons Act of 2025 </strong></p><p>This bill prohibits using federal funds to conduct a first-use nuclear strike unless Congress expressly authorizes such a strike pursuant to a declaration of war. A first-use nuclear strike is an attack using nuclear weapons against an enemy without confirming that there has been a nuclear strike against the United States, its territories, or its allies.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119s192"
    },
    "title": "Restricting First Use of Nuclear Weapons Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restricting First Use of Nuclear Weapons Act of 2025 </strong></p><p>This bill prohibits using federal funds to conduct a first-use nuclear strike unless Congress expressly authorizes such a strike pursuant to a declaration of war. A first-use nuclear strike is an attack using nuclear weapons against an enemy without confirming that there has been a nuclear strike against the United States, its territories, or its allies.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119s192"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s192is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Restricting First Use of Nuclear Weapons Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restricting First Use of Nuclear Weapons Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restrict the first-use strike of nuclear weapons.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:28Z"
    }
  ]
}
```
