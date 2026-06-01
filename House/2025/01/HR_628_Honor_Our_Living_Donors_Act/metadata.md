# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/628?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/628
- Title: Honor Our Living Donors Act
- Congress: 119
- Bill type: HR
- Bill number: 628
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-02-05T17:33:48Z
- Update date including text: 2026-02-05T17:33:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/628",
    "number": "628",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Honor Our Living Donors Act",
    "type": "HR",
    "updateDate": "2026-02-05T17:33:48Z",
    "updateDateIncludingText": "2026-02-05T17:33:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:00:25Z",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "IN"
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
      "sponsorshipDate": "2025-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "KS"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "OR"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "SC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DE"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr628ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 628\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Obernolte (for himself and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to eliminate consideration of the income of organ recipients in providing reimbursement of expenses to donating individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honor Our Living Donors Act .\n#### 2. No consideration of income of organ recipient\nSection 377 of the Public Health Service Act ( 42 U.S.C. 274f ) is amended\u2014\n**(1)**\nby redesignating subsections (c) through (f) as subsections (d) through (g), respectively;\n**(2)**\nby inserting after subsection (b) the following:\n(c) No consideration of income of organ recipient The recipient of a grant under this section, in providing reimbursement to a donating individual through such grant, shall not give any consideration to the income of the organ recipient. ; and\n**(3)**\nin subsection (f), as so redesignated\u2014\n**(A)**\nin paragraph (1), by striking subsection (c)(1) and inserting subsection (d)(1) ; and\n**(B)**\nin paragraph (2), by striking subsection (c)(2) and inserting subsection (d)(2) .\n#### 3. Removal of expectation of payments by organ recipients\nSection 377(e) of the Public Health Service Act ( 42 U.S.C. 274f(e) ), as redesignated by section 2, is amended\u2014\n**(1)**\nin paragraph (1), by adding or at the end;\n**(2)**\nin paragraph (2), by striking ; or and inserting a period; and\n**(3)**\nby striking paragraph (3).\n#### 4. Annual report\nSection 377 of the Public Health Service Act ( 42 U.S.C. 274f ), as amended by sections 2 and 3, is further amended by adding at the end the following:\n(h) Annual report Not later than December 31 of each year, the Secretary shall\u2014 (1) prepare, submit to the Congress, and make public a report on whether grants under this section provided adequate funding during the preceding fiscal year to reimburse all donating individuals participating in the grant program under this section for all qualifying expenses; and (2) include in each such report\u2014 (A) the estimated number of all donating individuals participating in the grant program under this section who did not receive reimbursement for all qualifying expenses during the preceding fiscal year; and (B) the total amount of funding that is estimated to be necessary to fully reimburse all donating individuals participating in the grant program under this section for all qualifying expenses. .",
      "versionDate": "2025-01-22",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "957",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Honor Our Living Donors Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-17T14:16:53Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-17T14:16:53Z"
          },
          {
            "name": "Organ and tissue donation and transplantation",
            "updateDate": "2025-03-17T14:16:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-20T19:28:59Z"
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
          "measure-id": "id119hr628",
          "measure-number": "628",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr628v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Honor Our Living Donors Act</strong></p><p>This bill modifies certain\u00a0criteria used to determine eligibility under the Living Organ Donation Reimbursement Program, which reimburses organ donors for certain incidental expenses related to organ donation (e.g., travel expenses).\u00a0</p><p>The bill specifies that the organ recipient's income may not be considered in determining whether an organ donor may be reimbursed under the program. (Currently, an organ recipient's income may not be greater than 350% of the federal poverty guidelines.) Additionally, under the bill, organ donors may be reimbursed regardless of whether the organ recipient pays them (or could be expected to pay them) for their expenses.</p><p>The Department of Health and Human Services must report on whether the program adequately covers the expenses of organ donors, and if not, the amount of necessary funding.\u00a0</p>"
        },
        "title": "Honor Our Living Donors Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr628.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honor Our Living Donors Act</strong></p><p>This bill modifies certain\u00a0criteria used to determine eligibility under the Living Organ Donation Reimbursement Program, which reimburses organ donors for certain incidental expenses related to organ donation (e.g., travel expenses).\u00a0</p><p>The bill specifies that the organ recipient's income may not be considered in determining whether an organ donor may be reimbursed under the program. (Currently, an organ recipient's income may not be greater than 350% of the federal poverty guidelines.) Additionally, under the bill, organ donors may be reimbursed regardless of whether the organ recipient pays them (or could be expected to pay them) for their expenses.</p><p>The Department of Health and Human Services must report on whether the program adequately covers the expenses of organ donors, and if not, the amount of necessary funding.\u00a0</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr628"
    },
    "title": "Honor Our Living Donors Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honor Our Living Donors Act</strong></p><p>This bill modifies certain\u00a0criteria used to determine eligibility under the Living Organ Donation Reimbursement Program, which reimburses organ donors for certain incidental expenses related to organ donation (e.g., travel expenses).\u00a0</p><p>The bill specifies that the organ recipient's income may not be considered in determining whether an organ donor may be reimbursed under the program. (Currently, an organ recipient's income may not be greater than 350% of the federal poverty guidelines.) Additionally, under the bill, organ donors may be reimbursed regardless of whether the organ recipient pays them (or could be expected to pay them) for their expenses.</p><p>The Department of Health and Human Services must report on whether the program adequately covers the expenses of organ donors, and if not, the amount of necessary funding.\u00a0</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr628"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr628ih.xml"
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
      "title": "Honor Our Living Donors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honor Our Living Donors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to eliminate consideration of the income of organ recipients in providing reimbursement of expenses to donating individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:33Z"
    }
  ]
}
```
