# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1535?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1535
- Title: BAD DOGE Act
- Congress: 119
- Bill type: HR
- Bill number: 1535
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2025-07-17T19:27:28Z
- Update date including text: 2025-07-17T19:27:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1535",
    "number": "1535",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "BAD DOGE Act",
    "type": "HR",
    "updateDate": "2025-07-17T19:27:28Z",
    "updateDateIncludingText": "2025-07-17T19:27:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:04:10Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NM"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1535ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1535\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Min (for himself, Ms. Stansbury , Ms. Ansari , Ms. Pressley , and Ms. Crockett ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo repeal President Donald Trump\u2019s January 20, 2025, Executive Order titled Establishing and Implementing the President\u2019s Department of Government Efficiency , and for other purposes.\n#### 1. Short Title\nThis Act may be cited as the Bolstering America\u2019s Democracy and Demanding Oversight and Government Ethics Act or the BAD DOGE Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nThe United States DOGE Service (in this section referred to as USDS ) (formerly known as the United States Digital Service) and the U.S. DOGE Service Temporary Organization (in this section, referred to as USDSTO ) created by Executive Order 14158 (90 Fed. Reg. 8441; relating to establishing and implementing the President\u2019s Department of Government Efficiency ) (in this section referred to as the DOGE Executive Order ) are operating beyond the scope of their authorities and organizational purposes.\n**(2)**\nThe DOGE Executive Order specifically creates the USDSTO as a temporary organization in accordance with section 3161 of title 5, United States Code, which limits the purpose of such an organization to performing a specific study or other project .\n**(3)**\nThe DOGE Executive Order specifies that the USDSTO shall be headed by the USDS Administrator, who is to be appointed by the Office of Management and Budget, and shall be dedicated to advancing the President\u2019s DOGE agenda.\n**(4)**\nThis DOGE agenda is described in the DOGE Executive Order as a Software Modernization Initiative led by the USDS Administrator to improve the quality and efficiency of government-wide software, network infrastructure, and information technology (IT) systems .\n**(5)**\nThe DOGE Executive Order additionally specifies that USDS shall adhere to rigorous data protection standards.\n**(6)**\nIn fact, both the USDS and USDSTO are being led by Elon Musk, who was not appointed as USDS Administrator.\n**(7)**\nThere are no government records indicating that Mr. Musk has any formal role with the Federal Government, or that he is complying with any disclosure or conflict-of-interest requirements that would apply to Federal employees or officials.\n**(8)**\nThe White House subsequently indicated that Mr. Musk is a special government employee but has not produced any evidence that he was retained in this role, or that he is complying with any rules or laws that would be required for a Federal employee or the USDS Administrator.\n**(9)**\nAccording to numerous media reports and first-hand accounts, including social media posts and press statements from Mr. Musk himself, under the leadership of Mr. Musk, the USDSTO has taken actions that go far beyond what the DOGE Executive Order authorized either USDS or USDSTO to do, including freezing payments to different Federal agencies and programs, acquiring personnel information for all Federal employees from the Office of Personnel Management (in this section referred to as OPM ), gaining control over and access to the Department of Treasury\u2019s Bureau of Fiscal Services (in this section referred to as BFS ) Federal payments system and its associated data, locking Federal employees out of their computer systems, offering Federal employees a buyout, and ostensibly terminating Federal agencies, bureaus, and programs created by and funded by Congress.\n**(10)**\nThese actions are inconsistent with the provisions of the DOGE Executive Order and also with what a temporary organization is statutorily permitted to do.\n**(11)**\nMr. Musk\u2019s actions and authorities also grossly exceed what he might be permitted to do as a special government employee .\n**(12)**\nThe USDS and the USDSTO, under the direction of Mr. Musk, are repeatedly violating a number of Federal statutes and provisions of the United States Constitution.\n**(13)**\nUSDS, USDSTO, and Mr. Musk have reportedly gained access to OPM\u2019s personnel files, gained control and access to BFS\u2019s payments systems and associated data, sent a buyout offer to all Federal employees, attempted to dismantle the United States Agency for International Development and the Consumer Financial Protection Bureau without congressional approval, and removed public health information from the Centers for Disease Control and Prevention and the Food and Drug Administration websites, among other things.\n**(14)**\nThese actions violate the Constitution, including Article I, section 1 (Separation of Powers), Article I, section 7 (Presentment and Appropriations Clause), Article I, section 8 (Spending Clause), and Article II, section 3 (Take Care Clause).\n**(15)**\nThese actions also violate a broad array of Federal statutes, including\u2014\n**(A)**\nthe Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 601 et seq. );\n**(B)**\nchapter 15 of title 31, United States Code (commonly known as the Anti-Deficiency Act );\n**(C)**\nsection 6329a through 6329c of title 5, United States Code (commonly known as the Administrative Leave Act of 2016 );\n**(D)**\nchapter 36 of title 44, United States Code (commonly known as the E-Government Act of 2002 );\n**(E)**\nsection 552a of title 5, United States Code (commonly known as the Privacy Act of 1974 );\n**(F)**\nsubchapter II of chapter 35 of title 44, United States Code (commonly known as the Federal Information Security Modernization Act of 2014 );\n**(G)**\nthe Foreign Affairs Reform and Restructuring Act of 1998 ( 22 U.S.C. 6501 et seq. );\n**(H)**\nchapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act );\n**(I)**\nchapter 41 of title 44, United States Code (commonly known as the Paperwork Reduction Act of 1995 );\n**(J)**\nnumerous Federal ethics regulations; and\n**(K)**\nvarious provisions of subchapter II of chapter 5 of title 5, United States Code (commonly known as the Administrative Procedure Act ).\n#### 3. Repeal of Executive Order 14158\nExecutive Order 14158 (90 Fed. Reg. 8441; relating to establishing and implementing the President\u2019s Department of Government Efficiency ) shall have no force or effect.",
      "versionDate": "2025-02-24",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T19:27:28Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-17T19:27:17Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-07-17T19:27:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-01T14:39:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1535",
          "measure-number": "1535",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1535v00",
            "update-date": "2025-04-09"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bolstering America\u2019s Democracy and Demanding Oversight and Government Ethics Act or the BAD DOGE Act</strong></p><p>This bill provides that Executive Order 14158 (relating to establishing and implementing the President's Department of Government Efficiency) shall have no force or effect.</p>"
        },
        "title": "BAD DOGE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1535.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bolstering America\u2019s Democracy and Demanding Oversight and Government Ethics Act or the BAD DOGE Act</strong></p><p>This bill provides that Executive Order 14158 (relating to establishing and implementing the President's Department of Government Efficiency) shall have no force or effect.</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr1535"
    },
    "title": "BAD DOGE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bolstering America\u2019s Democracy and Demanding Oversight and Government Ethics Act or the BAD DOGE Act</strong></p><p>This bill provides that Executive Order 14158 (relating to establishing and implementing the President's Department of Government Efficiency) shall have no force or effect.</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr1535"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1535ih.xml"
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
      "title": "BAD DOGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:06Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BAD DOGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bolstering America\u2019s Democracy and Demanding Oversight and Government Ethics Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal President Donald Trump's January 20, 2025, Executive Order titled \"Establishing and Implementing the President's 'Department of Government Efficiency'\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T12:18:38Z"
    }
  ]
}
```
