# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/894?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/894
- Title: Keeping Drugs Out of Schools Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 894
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-03-19T08:07:12Z
- Update date including text: 2026-03-19T08:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/894",
    "number": "894",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001156",
        "district": "38",
        "firstName": "Linda",
        "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
        "lastName": "S\u00e1nchez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Keeping Drugs Out of Schools Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:12Z",
    "updateDateIncludingText": "2026-03-19T08:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:07:45Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "NM"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "OR"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr894ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 894\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. S\u00e1nchez (for herself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize grants to implement school-community partnerships for preventing substance use and misuse among youth.\n#### 1. Short title\nThis Act may be cited as the Keeping Drugs Out of Schools Act of 2025 .\n#### 2. Grant program\n##### (a) Definitions\nIn this section:\n**(1) Director**\nThe term Director means the Director of the Office of National Drug Control Policy.\n**(2) Drug-Free Communities funded coalition**\nThe term Drug-Free Communities funded coalition means a recipient of a grant under section 1032 of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1532 ).\n**(3) Effective drug prevention programs**\nThe term effective drug prevention programs , with respect to a school-community partnership between a Drug-Free Communities funded coalition and a local school, means strategies, policies, and activities that\u2014\n**(A)**\nare tailored to meet the needs of the student population of the school, based on the environment of the school and the community surrounding the school; and\n**(B)**\nprevent and reduce substance use and misuse among local youth.\n**(4) Eligible entity**\nThe term eligible entity means a coalition (within the meaning of section 1032 of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1532 )) that\u2014\n**(A)**\nreceives or has received a grant under subchapter I of chapter 2 of title I of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1523 et seq. ); and\n**(B)**\nhas a memorandum of understanding in effect with not less than 1 local school to establish a school-community partnership.\n**(5) Local school**\nThe term local school means an elementary, middle, or high school located in an area served by an eligible entity.\n**(6) School-community partnership**\nThe term school-community partnership means a partnership between a Drug-Free Communities funded coalition and not less than 1 local school for the purpose of implementing effective drug prevention programs.\n**(7) Substance use and misuse**\nThe term substance use and misuse \u2014\n**(A)**\nhas the meaning given the term in paragraph (9) of section 1023 of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1523 ); and\n**(B)**\nincludes the use of electronic or other delivery mechanisms to consume a substance described in subparagraph (A), (B), or (C) of that paragraph.\n##### (b) Grants authorized\n**(1) In general**\n**(A) Initial grants**\nSubject to paragraph (2), the Director may award grants to eligible entities for the purpose of implementing a school-community partnership.\n**(B) Renewal grants**\nSubject to paragraph (2), the Director may award to an eligible entity who has received a grant under subparagraph (A) an additional grant for each fiscal year during the 3-fiscal-year period following the fiscal year for which the grant was awarded under subparagraph (A), for the purpose of continuing the school-community partnership.\n**(2) Limitations**\n**(A) Amount**\nThe amount of a grant under this subsection may not exceed $75,000 for a fiscal year.\n**(B) Recipients**\nNot more than 1 eligible entity may receive a grant under this subsection to establish a school-community partnership with a particular local school.\n##### (c) Interagency agreement\nThe Director may enter into an interagency agreement with a National Drug Control Program agency, as defined in section 702 of the Office of National Drug Control Policy Reauthorization Act of 1998 ( 21 U.S.C. 1701 ), to delegate authority for\u2014\n**(1)**\nthe execution of grants under this section; and\n**(2)**\nother activities necessary to carry out the responsibilities of the Director under this section.\n##### (d) Application\n**(1) In general**\nAn eligible entity desiring a grant under this section, in coordination with each local school with which the eligible entity has a school-community partnership, shall submit to the Director an application at such time, in such manner, and accompanied by such information as the Director may require.\n**(2) Plan**\nThe application submitted under paragraph (1) shall include a detailed, comprehensive plan for the school-community partnership to implement effective drug prevention programs.\n##### (e) Use of funds\n**(1) In general**\nAn eligible entity receiving a grant under this section shall use funds from the grant\u2014\n**(A)**\nto implement the plan described in subsection (d)(2); and\n**(B)**\nif necessary, to obtain specialized training and assistance from the organization receiving the grant under section 4(a) of Public Law 107\u201382 ( 21 U.S.C. 1521 note).\n**(2) Supplement not supplant**\nGrants provided under this section shall be used to supplement, and not supplant, Federal and non-Federal funds that are otherwise available for drug prevention programs in local schools.\n##### (f) Evaluation\nSection 1032(a)(6) of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1532(a)(6) ) shall apply to a grant under this section in the same manner as that section applies to a grant under subchapter I of chapter 2 of subtitle A of title I of that Act ( 21 U.S.C. 1531 et seq. ).\n##### (g) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to carry out this section $7,000,000 for each of fiscal years 2026 through 2031.\n**(2) Administrative costs**\nNot more than 8 percent of the funds appropriated under paragraph (1) may be used by the Director for administrative expenses associated with the responsibilities of the Director under this section.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "329",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keeping Drugs Out of Schools Act of 2025",
      "type": "S"
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
            "name": "Child safety and welfare",
            "updateDate": "2025-04-07T14:35:13Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-04-07T14:35:13Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-07T14:35:13Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-07T14:35:13Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2025-04-07T14:35:13Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-04-07T14:35:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-06T15:21:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr894",
          "measure-number": "894",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr894v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keeping Drugs Out of Schools Act of 2025</strong></p><p>This bill allows the Office of National Drug Control Policy to award grants for eligible entities to implement school-community partnerships for preventing and reducing substance use and misuse among youth. <em>Eligible entity</em> refers to a coalition that (1)\u00a0receives or has received a grant under the Drug-Free Communities Support Program, and (2) has a memorandum of understanding in effect with not less than one local school\u00a0to establish a school-community partnership.</p>"
        },
        "title": "Keeping Drugs Out of Schools Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr894.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keeping Drugs Out of Schools Act of 2025</strong></p><p>This bill allows the Office of National Drug Control Policy to award grants for eligible entities to implement school-community partnerships for preventing and reducing substance use and misuse among youth. <em>Eligible entity</em> refers to a coalition that (1)\u00a0receives or has received a grant under the Drug-Free Communities Support Program, and (2) has a memorandum of understanding in effect with not less than one local school\u00a0to establish a school-community partnership.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr894"
    },
    "title": "Keeping Drugs Out of Schools Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keeping Drugs Out of Schools Act of 2025</strong></p><p>This bill allows the Office of National Drug Control Policy to award grants for eligible entities to implement school-community partnerships for preventing and reducing substance use and misuse among youth. <em>Eligible entity</em> refers to a coalition that (1)\u00a0receives or has received a grant under the Drug-Free Communities Support Program, and (2) has a memorandum of understanding in effect with not less than one local school\u00a0to establish a school-community partnership.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr894"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr894ih.xml"
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
      "title": "Keeping Drugs Out of Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keeping Drugs Out of Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize grants to implement school-community partnerships for preventing substance use and misuse among youth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:23Z"
    }
  ]
}
```
