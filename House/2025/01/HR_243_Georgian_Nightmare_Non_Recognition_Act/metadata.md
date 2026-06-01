# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/243
- Title: Georgian Nightmare Non-Recognition Act
- Congress: 119
- Bill type: HR
- Bill number: 243
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-10-01T08:06:18Z
- Update date including text: 2025-10-01T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Sponsor introductory remarks on measure. (CR H189)
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Sponsor introductory remarks on measure. (CR H189)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/243",
    "number": "243",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Georgian Nightmare Non-Recognition Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:18Z",
    "updateDateIncludingText": "2025-10-01T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H189)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:39:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:39:30Z",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MO"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr243ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 243\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Wilson of South Carolina (for himself and Mr. Cohen ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit United States recognition of Bidzina Ivanishvili or any Government of Georgia that is led by Bidzina Ivanishvili, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Georgian Nightmare Non-Recognition Act .\n#### 2. Prohibition of recognition of ivanishvili regime\n##### (a) Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nnot to recognize or normalize relations with any Government of Georgia that is led by Bidzina Ivanishvili or any proxies due to the Ivanishvili regime\u2019s ongoing crimes against the Georgian people;\n**(2)**\nto actively oppose recognition or normalization of relations by other governments with any Government of Georgia that is led by Bidzina Ivanishvili or any proxies, including by fully implementing the mandatory primary and secondary sanctions in Executive Order No. 14024; and\n**(3)**\nto use the full range of authorities, including those provided under the Global Magnitsky Act and Executive Order No. 14024, to deter corrupt activity or foreign influence operations by Georgia on behalf of the Chinese Communist Party, the Iranian regime, and the Russian Federation.\n##### (b) Prohibition\nIn accordance with subsection (a), no Federal official or employee may take any action, and no Federal funds may be made available, to recognize or otherwise imply, in any manner, United States recognition of Bidzina Ivanishvili or any Government in Georgia that is led by Bidzina Ivanishvili or any proxies.\n##### (c) Recognition of president of georgia\nThe United States shall recognize the incumbent President of Georgia prior to the fraudulent elections on October 26, 2024 as the only legitimate leader in Georgia.\n##### (d) Restoration of georgian constitution\nIn the case of the restoration of the Georgian constitution as demonstrated by the holding of free and fair elections as certified by the Chairman and Co-Chairman of the U.S. Helsinki Commission, this policy may be declared void by the President.",
      "versionDate": "2025-01-09",
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
            "name": "Europe",
            "updateDate": "2025-09-17T19:55:07Z"
          },
          {
            "name": "Georgia (Republic)",
            "updateDate": "2025-09-17T19:54:59Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-09-17T19:55:27Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-09-17T19:55:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-21T11:35:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "House",
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
          "measure-id": "id119hr243",
          "measure-number": "243",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr243v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Georgian Nightmare Non-Recognition Act</strong></p><p>This\u00a0bill prohibits federal officials and employees from taking any action, or expending any federal funds, to recognize or imply U.S. recognition of (1) Bidzina Ivanishvili, or (2) any government of the nation of Georgia that is led by Bidzina Ivanishvili or any proxies.</p><p>The bill also specifies that the United States must recognize the incumbent president of Georgia prior to the October 26, 2024, elections as the only legitimate leader of Georgia.</p><p>The President may declare this policy void if the chairman and co-chairman of the U.S. Helsinki Commission certify that Georgia has held free and fair elections.</p>"
        },
        "title": "Georgian Nightmare Non-Recognition Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr243.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Georgian Nightmare Non-Recognition Act</strong></p><p>This\u00a0bill prohibits federal officials and employees from taking any action, or expending any federal funds, to recognize or imply U.S. recognition of (1) Bidzina Ivanishvili, or (2) any government of the nation of Georgia that is led by Bidzina Ivanishvili or any proxies.</p><p>The bill also specifies that the United States must recognize the incumbent president of Georgia prior to the October 26, 2024, elections as the only legitimate leader of Georgia.</p><p>The President may declare this policy void if the chairman and co-chairman of the U.S. Helsinki Commission certify that Georgia has held free and fair elections.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr243"
    },
    "title": "Georgian Nightmare Non-Recognition Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Georgian Nightmare Non-Recognition Act</strong></p><p>This\u00a0bill prohibits federal officials and employees from taking any action, or expending any federal funds, to recognize or imply U.S. recognition of (1) Bidzina Ivanishvili, or (2) any government of the nation of Georgia that is led by Bidzina Ivanishvili or any proxies.</p><p>The bill also specifies that the United States must recognize the incumbent president of Georgia prior to the October 26, 2024, elections as the only legitimate leader of Georgia.</p><p>The President may declare this policy void if the chairman and co-chairman of the U.S. Helsinki Commission certify that Georgia has held free and fair elections.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr243"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr243ih.xml"
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
      "title": "Georgian Nightmare Non-Recognition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T02:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Georgian Nightmare Non-Recognition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T02:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit United States recognition of Bidzina Ivanishvili or any Government of Georgia that is led by Bidzina Ivanishvili, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T02:18:28Z"
    }
  ]
}
```
