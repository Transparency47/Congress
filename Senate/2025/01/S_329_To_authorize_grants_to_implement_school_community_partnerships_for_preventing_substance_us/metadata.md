# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/329?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/329
- Title: Keeping Drugs Out of Schools Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 329
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-12-05T22:02:36Z
- Update date including text: 2025-12-05T22:02:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/329",
    "number": "329",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Keeping Drugs Out of Schools Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:02:36Z",
    "updateDateIncludingText": "2025-12-05T22:02:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
        "item": {
          "date": "2025-01-30T18:05:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "IA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s329is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 329\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mrs. Shaheen (for herself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo authorize grants to implement school-community partnerships for preventing substance use and misuse among youth.\n#### 1. Short title\nThis Act may be cited as the Keeping Drugs Out of Schools Act of 2025 .\n#### 2. Grant program\n##### (a) Definitions\nIn this section:\n**(1) Director**\nThe term Director means the Director of the Office of National Drug Control Policy.\n**(2) Drug-Free Communities funded coalition**\nThe term Drug-Free Communities funded coalition means a recipient of a grant under section 1032 of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1532 ).\n**(3) Effective drug prevention programs**\nThe term effective drug prevention programs , with respect to a school-community partnership between a Drug-Free Communities funded coalition and a local school, means strategies, policies, and activities that\u2014\n**(A)**\nare tailored to meet the needs of the student population of the school, based on the environment of the school and the community surrounding the school; and\n**(B)**\nprevent and reduce substance use and misuse among local youth.\n**(4) Eligible entity**\nThe term eligible entity means a coalition (within the meaning of section 1032 of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1532 )) that\u2014\n**(A)**\nreceives or has received a grant under subchapter I of chapter 2 of title I of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1523 et seq. ); and\n**(B)**\nhas a memorandum of understanding in effect with not less than 1 local school to establish a school-community partnership.\n**(5) Local school**\nThe term local school means an elementary, middle, or high school located in an area served by an eligible entity.\n**(6) School-community partnership**\nThe term school-community partnership means a partnership between a Drug-Free Communities funded coalition and not less than 1 local school for the purpose of implementing effective drug prevention programs.\n**(7) Substance use and misuse**\nThe term substance use and misuse \u2014\n**(A)**\nhas the meaning given the term in paragraph (9) of section 1023 of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1523 ); and\n**(B)**\nincludes the use of electronic or other delivery mechanisms to consume a substance described in subparagraph (A), (B), or (C) of that paragraph.\n##### (b) Grants authorized\n**(1) In general**\n**(A) Initial grants**\nSubject to paragraph (2), the Director may award grants to eligible entities for the purpose of implementing a school-community partnership.\n**(B) Renewal grants**\nSubject to paragraph (2), the Director may award to an eligible entity who has received a grant under subparagraph (A) an additional grant for each fiscal year during the 3-fiscal-year period following the fiscal year for which the grant was awarded under subparagraph (A), for the purpose of continuing the school-community partnership.\n**(2) Limitations**\n**(A) Amount**\nThe amount of a grant under this subsection may not exceed $75,000 for a fiscal year.\n**(B) Recipients**\nNot more than 1 eligible entity may receive a grant under this subsection to establish a school-community partnership with a particular local school.\n##### (c) Interagency agreement\nThe Director may enter into an interagency agreement with a National Drug Control Program agency, as defined in section 702 of the Office of National Drug Control Policy Reauthorization Act of 1998 ( 21 U.S.C. 1701 ), to delegate authority for\u2014\n**(1)**\nthe execution of grants under this section; and\n**(2)**\nother activities necessary to carry out the responsibilities of the Director under this section.\n##### (d) Application\n**(1) In general**\nAn eligible entity desiring a grant under this section, in coordination with each local school with which the eligible entity has a school-community partnership, shall submit to the Director an application at such time, in such manner, and accompanied by such information as the Director may require.\n**(2) Plan**\nThe application submitted under paragraph (1) shall include a detailed, comprehensive plan for the school-community partnership to implement effective drug prevention programs.\n##### (e) Use of funds\n**(1) In general**\nAn eligible entity receiving a grant under this section shall use funds from the grant\u2014\n**(A)**\nto implement the plan described in subsection (d)(2); and\n**(B)**\nif necessary, to obtain specialized training and assistance from the organization receiving the grant under section 4(a) of Public Law 107\u201382 ( 21 U.S.C. 1521 note).\n**(2) Supplement not supplant**\nGrants provided under this section shall be used to supplement, and not supplant, Federal and non-Federal funds that are otherwise available for drug prevention programs in local schools.\n##### (f) Evaluation\nSection 1032(a)(6) of the Anti-Drug Abuse Act of 1988 ( 21 U.S.C. 1532(a)(6) ) shall apply to a grant under this section in the same manner as that section applies to a grant under subchapter I of chapter 2 of subtitle A of title I of that Act ( 21 U.S.C. 1531 et seq. ).\n##### (g) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to carry out this section $7,000,000 for each of fiscal years 2026 through 2031.\n**(2) Administrative costs**\nNot more than 8 percent of the funds appropriated pursuant to paragraph (1) may be used by the Director for administrative expenses associated with the responsibilities of the Director under this section.",
      "versionDate": "2025-01-30",
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
        "actionDate": "2025-01-31",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "894",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keeping Drugs Out of Schools Act of 2025",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-04-07T14:34:41Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-04-07T14:34:35Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-07T14:34:51Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-07T14:34:46Z"
          },
          {
            "name": "Educational guidance",
            "updateDate": "2025-04-07T14:34:56Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-04-07T14:34:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-03T16:20:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s329",
          "measure-number": "329",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s329v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Keeping Drugs Out of Schools Act of 2025</strong></p><p>This bill allows the Office of National Drug Control Policy to award grants for eligible entities to implement school-community partnerships for preventing and reducing substance use and misuse among youth. <em>Eligible entity</em> refers to a coalition that (1)\u00a0receives or has received a grant under the Drug-Free Communities Support Program, and (2) has a memorandum of understanding in effect with not less than one local school\u00a0to establish a school-community partnership.</p>"
        },
        "title": "Keeping Drugs Out of Schools Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s329.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keeping Drugs Out of Schools Act of 2025</strong></p><p>This bill allows the Office of National Drug Control Policy to award grants for eligible entities to implement school-community partnerships for preventing and reducing substance use and misuse among youth. <em>Eligible entity</em> refers to a coalition that (1)\u00a0receives or has received a grant under the Drug-Free Communities Support Program, and (2) has a memorandum of understanding in effect with not less than one local school\u00a0to establish a school-community partnership.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s329"
    },
    "title": "Keeping Drugs Out of Schools Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Keeping Drugs Out of Schools Act of 2025</strong></p><p>This bill allows the Office of National Drug Control Policy to award grants for eligible entities to implement school-community partnerships for preventing and reducing substance use and misuse among youth. <em>Eligible entity</em> refers to a coalition that (1)\u00a0receives or has received a grant under the Drug-Free Communities Support Program, and (2) has a memorandum of understanding in effect with not less than one local school\u00a0to establish a school-community partnership.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s329"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s329is.xml"
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
      "title": "Keeping Drugs Out of Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keeping Drugs Out of Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize grants to implement school-community partnerships for preventing substance use and misuse among youth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:25Z"
    }
  ]
}
```
