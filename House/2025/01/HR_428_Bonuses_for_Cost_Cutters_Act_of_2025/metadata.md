# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/428
- Title: Bonuses for Cost-Cutters Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 428
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-04-21T15:50:21Z
- Update date including text: 2026-04-21T15:50:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-03-18 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/428",
    "number": "428",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000459",
        "district": "3",
        "firstName": "Charles",
        "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
        "lastName": "Fleischmann",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Bonuses for Cost-Cutters Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T15:50:21Z",
    "updateDateIncludingText": "2026-04-21T15:50:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
            "date": "2026-03-18T13:00:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-15T15:01:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr428ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 428\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Fleischmann introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to enhance the authority under which Federal agencies may pay cash awards to employees for making cost saving disclosures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bonuses for Cost-Cutters Act of 2025 .\n#### 2. Cost savings enhancements\n##### (a) Definitions\nSection 4511 of title 5, United States Code, is amended\u2014\n**(1)**\nin the section heading, by striking Definition and inserting Definitions ; and\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking the period at the end and inserting ; and ;\n**(B)**\nby striking this subchapter, the term and inserting the following: \u201cthis subchapter\u2014\n(1) the term ; and\n**(C)**\nby adding at the end the following:\n(2) the term wasteful expenses means amounts made available for salaries and expenses accounts, operations and maintenance accounts, or other equivalent accounts\u2014 (A) that are identified by an employee of the agency under section 4512(a) as wasteful; and (B) that the Chief Financial Officer of the agency determines are not required for the purpose for which the amounts were made available. .\n##### (b) Authority\nSection 4512 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby inserting The head of an agency may pay a cash award to any employee of such agency whose identification of wasteful expenses to the Chief Financial Officer of the agency has resulted in cost savings for the agency. after the first sentence;\n**(B)**\nin paragraph (1) by striking $10,000 and inserting $20,000 ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby inserting Chief Financial Officer, after Inspector General, ;\n**(ii)**\nby striking employee designated under subsection (b) and inserting designated employee ; and\n**(iii)**\nby inserting or identification after disclosure ; and\n**(D)**\nin the matter following paragraph (2)\u2014\n**(i)**\nby inserting , Chief Financial Officer, after Inspector General ; and\n**(ii)**\nby inserting or identification after disclosure ;\n**(2)**\nin subsection (b) by striking awards permitted under this section and inserting awards for the disclosure of fraud, waste, or mismanagement under this section ; and\n**(3)**\nby adding at the end the following:\n(c) (1) If the Chief Financial Officer of the agency determines that potential wasteful expenses identified by an employee meet the requirements of section 4511(a)(2)(B), the head of the agency shall notify the President for purposes of proposing the expenses for rescission under title X of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 681 et seq. ). (2) In the case of an agency for which there is no Chief Financial Officer, the head of the agency shall designate an agency employee who shall have the authority to make the determinations for identification of wasteful expenses under this section. (d) The head of each agency shall make available, along with, and in the same manner and form as, the provision of information required under section 1116 of title 31, information on disclosures of wasteful expenses under this section, including\u2014 (1) a description of each disclosure of possible wasteful expenses identified by an employee and determined by the agency to have merit; and (2) the number and amount of cash awards provided by the agency under subsection (a). (e) An individual may not receive a cash award under this subchapter if the individual is\u2014 (1) an officer or employee of the Office of the Inspector General of an agency; or (2) ineligible for a cash award under section 4509. (f) The Director of the Office of Personnel Management shall\u2014 (1) ensure that the cash award program of each agency complies with this section; and (2) submit to Congress an annual certification indicating whether the cash award program of each agency complies with this section. (g) Not later than 3 years after the date of enactment of the Bonuses for Cost-Cutters Act of 2025 , and every 3 years thereafter for 6 years, the Comptroller General of the United States shall submit to Congress a report on the operation of the cost savings and awards program under this section, including any recommendations for legislative changes. .\n##### (c) Technical and conforming amendment\nThe table of sections for subchapter II of chapter 45 of title 5, United States Code, is amended by striking the item relating to section 4511 and inserting the following:\n4511. Definitions and general provisions. .",
      "versionDate": "2025-01-15",
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
            "updateDate": "2025-03-06T16:50:30Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-03-06T16:50:30Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-06T16:50:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T16:22:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr428",
          "measure-number": "428",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr428v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bonuses for Cost-Cutters Act of\u00a0</strong><strong>2025</strong></p><p>This bill expands the awards program for cost-saving identifications by federal employees of fraud, waste, or mismanagement to include identifications of certain operational expenses that are wasteful (i.e., that are identified as wasteful by an employee and that an agency determines are not required for the purposes for which the amounts were made available). An agency must propose any identified wasteful expenses for rescission.</p><p>The bill also doubles the maximum cash award that may be made under the program.</p>"
        },
        "title": "Bonuses for Cost-Cutters Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr428.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bonuses for Cost-Cutters Act of\u00a0</strong><strong>2025</strong></p><p>This bill expands the awards program for cost-saving identifications by federal employees of fraud, waste, or mismanagement to include identifications of certain operational expenses that are wasteful (i.e., that are identified as wasteful by an employee and that an agency determines are not required for the purposes for which the amounts were made available). An agency must propose any identified wasteful expenses for rescission.</p><p>The bill also doubles the maximum cash award that may be made under the program.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr428"
    },
    "title": "Bonuses for Cost-Cutters Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bonuses for Cost-Cutters Act of\u00a0</strong><strong>2025</strong></p><p>This bill expands the awards program for cost-saving identifications by federal employees of fraud, waste, or mismanagement to include identifications of certain operational expenses that are wasteful (i.e., that are identified as wasteful by an employee and that an agency determines are not required for the purposes for which the amounts were made available). An agency must propose any identified wasteful expenses for rescission.</p><p>The bill also doubles the maximum cash award that may be made under the program.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr428"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr428ih.xml"
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
      "title": "Bonuses for Cost-Cutters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bonuses for Cost-Cutters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to enhance the authority under which Federal agencies may pay cash awards to employees for making cost saving disclosures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T02:48:20Z"
    }
  ]
}
```
