# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1795
- Title: Empower Charter School Educators to Lead Act
- Congress: 119
- Bill type: S
- Bill number: 1795
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-04-02T19:41:13Z
- Update date including text: 2026-04-02T19:41:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1795",
    "number": "1795",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Empower Charter School Educators to Lead Act",
    "type": "S",
    "updateDate": "2026-04-02T19:41:13Z",
    "updateDateIncludingText": "2026-04-02T19:41:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T19:24:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NJ"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "LA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CO"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-29",
      "state": "AL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1795is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1795\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Cornyn (for himself, Mr. Booker , Mr. Cassidy , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo modify the program of grants to support high-quality charter schools.\n#### 1. Short title\nThis Act may be cited as the Empower Charter School Educators to Lead Act .\n#### 2. Grants to support high-quality charter schools\nSection 4303 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221b ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(C), by striking and after the semicolon; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) (A) provide technical assistance to eligible applicants and authorized public chartering agencies in carrying out the activities described in paragraph (1); (B) work with authorized public chartering agencies in the State to improve authorizing quality, including developing capacity for, and conducting, fiscal oversight and auditing of charter schools; and (C) at the State entity\u2019s discretion\u2014 (i) fund a revolving loan fund or similar mechanisms for expenses under subsection (h) prior to an eligible applicant receiving reimbursement; and (ii) provide assistance to eligible applicants in locating and accessing a facility; and (3) provide pre-charter planning subgrants (in amounts of no more than $100,000 per prospective applicant) to charter school developers that\u2014 (A) intend to submit an application\u2014 (i) to an authorized public chartering agency to operate a charter school; or (ii) to nonprofit or public entities for the provision of financial support to such developers; (B) are led by educators who\u2014 (i) have not less than 54 months of school-based experience (which may include experience in teaching in or administering after school or summer school programs); and (ii) have demonstrated leadership competencies and success with students, as determined by the State entity; and (C) have successfully completed the development of an initial plan for opening a charter school, as evidenced by a description of the educational needs of the community in which the proposed charter school will be located and how the proposed charter school will be suited to meet those needs. ;\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A), by striking 90 percent and inserting 80 percent ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking not less than 7 percent and inserting not more than 10 percent ; and\n**(ii)**\nby striking and after the semicolon;\n**(C)**\nby redesignating subparagraph (C) as subparagraph (D);\n**(D)**\nin subparagraph (D), as so redesignated, by striking 3 percent and inserting 5 percent ; and\n**(E)**\nby inserting after subparagraph (B) the following:\n(C) reserve not more than 5 percent of such funds to carry out the activities described in subsection (b)(3); and ;\n**(3)**\nin subsection (d)(1)(B), by striking this section and inserting subsection (b)(1) ;\n**(4)**\nin subsection (e)(2), by striking this section and inserting subsection (b)(1) ;\n**(5)**\nin subsection (f)(1)(A)(vi)\u2014\n**(A)**\nin the matter preceding subclause (I), by inserting under subsection (b)(1) after program ; and\n**(B)**\nin subclause (II), by striking subgrant funds under this section and inserting subgrant funds under subsection (b)(1) ; and\n**(6)**\nin subsection (h), in the matter preceding paragraph (1), by striking this section and inserting subsection (b)(1) .",
      "versionDate": "2025-05-15",
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
        "actionDate": "2026-01-13",
        "text": "Placed on the Union Calendar, Calendar No. 379."
      },
      "number": "3453",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Empower Charter School Educators to Lead Act",
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
            "name": "Education programs funding",
            "updateDate": "2025-06-30T19:00:06Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2025-06-30T19:00:06Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-06-30T19:00:06Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-06-30T19:00:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-06-02T13:28:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119s1795",
          "measure-number": "1795",
          "measure-type": "s",
          "orig-publish-date": "2025-05-15",
          "originChamber": "SENATE",
          "update-date": "2026-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1795v00",
            "update-date": "2026-04-02"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Empower Charter School Educators to Lead Act</strong></p><p>This bill makes changes to the Charter Schools Program (CSP), which authorizes competitive grants to state entities (e.g., state educational agencies and state charter school boards) to\u00a0support high-quality charter schools.\u00a0</p><p>Specifically, the bill allows state entities to use up to 5% of their CSP grant funds to make pre-charter planning subgrants to certain prospective charter applicants.</p><p>The bill specifies that state entities may also (1)\u00a0fund a revolving loan fund or similar mechanisms for expenses prior to an eligible applicant receiving reimbursement,\u00a0and (2)\u00a0provide assistance to eligible applicants in locating and accessing a charter school facility.</p><p>Under the current CSP, state entities must use at least 7% of their CSP grant funds to provide technical assistance to eligible applicants and authorized public chartering agencies. The bill instead allows state entities to use not more than 10% of these funds for technical assistance.</p><p>Additionally, under the current CSP, state entities may not use more than 3% of CSP grant funds for administrative costs. This bill\u00a0raises the cap to 5%.</p>"
        },
        "title": "Empower Charter School Educators to Lead Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1795.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Empower Charter School Educators to Lead Act</strong></p><p>This bill makes changes to the Charter Schools Program (CSP), which authorizes competitive grants to state entities (e.g., state educational agencies and state charter school boards) to\u00a0support high-quality charter schools.\u00a0</p><p>Specifically, the bill allows state entities to use up to 5% of their CSP grant funds to make pre-charter planning subgrants to certain prospective charter applicants.</p><p>The bill specifies that state entities may also (1)\u00a0fund a revolving loan fund or similar mechanisms for expenses prior to an eligible applicant receiving reimbursement,\u00a0and (2)\u00a0provide assistance to eligible applicants in locating and accessing a charter school facility.</p><p>Under the current CSP, state entities must use at least 7% of their CSP grant funds to provide technical assistance to eligible applicants and authorized public chartering agencies. The bill instead allows state entities to use not more than 10% of these funds for technical assistance.</p><p>Additionally, under the current CSP, state entities may not use more than 3% of CSP grant funds for administrative costs. This bill\u00a0raises the cap to 5%.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119s1795"
    },
    "title": "Empower Charter School Educators to Lead Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Empower Charter School Educators to Lead Act</strong></p><p>This bill makes changes to the Charter Schools Program (CSP), which authorizes competitive grants to state entities (e.g., state educational agencies and state charter school boards) to\u00a0support high-quality charter schools.\u00a0</p><p>Specifically, the bill allows state entities to use up to 5% of their CSP grant funds to make pre-charter planning subgrants to certain prospective charter applicants.</p><p>The bill specifies that state entities may also (1)\u00a0fund a revolving loan fund or similar mechanisms for expenses prior to an eligible applicant receiving reimbursement,\u00a0and (2)\u00a0provide assistance to eligible applicants in locating and accessing a charter school facility.</p><p>Under the current CSP, state entities must use at least 7% of their CSP grant funds to provide technical assistance to eligible applicants and authorized public chartering agencies. The bill instead allows state entities to use not more than 10% of these funds for technical assistance.</p><p>Additionally, under the current CSP, state entities may not use more than 3% of CSP grant funds for administrative costs. This bill\u00a0raises the cap to 5%.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119s1795"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1795is.xml"
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
      "title": "Empower Charter School Educators to Lead Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-04T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Empower Charter School Educators to Lead Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the program of grants to support high-quality charter schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:20Z"
    }
  ]
}
```
