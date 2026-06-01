# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/532?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/532
- Title: OPTN Fee Collection Authority Act
- Congress: 119
- Bill type: S
- Bill number: 532
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-02-05T17:33:59Z
- Update date including text: 2026-02-05T17:33:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/532",
    "number": "532",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "OPTN Fee Collection Authority Act",
    "type": "S",
    "updateDate": "2026-02-05T17:33:59Z",
    "updateDateIncludingText": "2026-02-05T17:33:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:48:37Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s532is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 532\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Grassley (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo authorize the Secretary of Health and Human Services to collect registration fees from members of the Organ Procurement and Transplantation Network, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the OPTN Fee Collection Authority Act .\n#### 2. Organ Procurement and Transplantation Network\nSection 372 of the Public Health Service Act ( 42 U.S.C. 274 ) is amended\u2014\n**(1)**\nin subsection (b)(2)\u2014\n**(A)**\nby moving the margins of subparagraphs (M) through (O) 2 ems to the left;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by striking , and and inserting ; and ; and\n**(ii)**\nin clause (ii), by striking the comma at the end and inserting a semicolon;\n**(C)**\nin subparagraph (C), by striking twenty-four-hour telephone service and inserting 24-hour telephone or information technology service ;\n**(D)**\nin each of subparagraphs (B) through (M), by striking the comma at the end and inserting a semicolon;\n**(E)**\nin subparagraph (N), by striking transportation, and and inserting transportation; ;\n**(F)**\nin subparagraph (O), by striking the period and inserting a semicolon; and\n**(G)**\nby adding at the end the following:\n(P) encourage the integration of electronic health records systems through application programming interfaces (or successor technologies) among hospitals, organ procurement organizations, and transplant centers, including the use of automated electronic hospital referrals and the grant of remote, electronic access to hospital electronic health records of potential donors by organ procurement organizations, in a manner that complies with the privacy regulations promulgated under the Health Insurance Portability and Accountability Act of 1996, at part 160 of title 45, Code of Federal Regulations, and subparts A, C, and E of part 164 of such title (or any successor regulations); and (Q) consider establishing a dashboard to display the number of transplants performed, the types of transplants performed, the number and types of organs that entered the Organ Procurement and Transplantation Network system and failed to be transplanted, and other appropriate statistics, which should be updated more frequently than annually. ; and\n**(2)**\nby adding at the end the following:\n(d) Registration fees (1) In general The Secretary may collect registration fees from any member of the Organ Procurement and Transplantation Network for each transplant candidate such member places on the list described in subsection (b)(2)(A)(i). Such registration fees shall be collected and distributed only to support the operation of the Organ Procurement and Transplantation Network. Such registration fees are authorized to remain available until expended. (2) Collection The Secretary may collect the registration fees under paragraph (1) directly or through awards made under subsection (b)(1)(A). (3) Distribution Any amounts collected under this subsection shall\u2014 (A) be credited to the currently applicable appropriation, account, or fund of the Department of Health and Human Services as discretionary offsetting collections; and (B) be available, only to the extent and in the amounts provided in advance in appropriations Acts, to distribute such fees among awardees described in subsection (b)(1)(A). (4) Transparency The Secretary shall\u2014 (A) promptly post on the website of the Organ Procurement and Transplantation Network\u2014 (i) the amount of registration fees collected under this subsection from each member of the Organ Procurement and Transplantation Network; and (ii) a list of activities such fees are used to support; and (B) update the information posted pursuant to subparagraph (A), as applicable for each calendar quarter for which fees are collected under paragraph (1). (5) GAO review Not later than 2 years after the date of enactment of this subsection, the Comptroller General of the United States shall, to the extent data are available\u2014 (A) conduct a review concerning the activities under this subsection; and (B) submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Finance of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report on such review, including related recommendations, as applicable. (6) Sunset The authority to collect registration fees under paragraph (1) shall expire on the date that is 3 years after the date of enactment of the OPTN Fee Collection Authority Act . .",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-09-10",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2751",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Permanent OPTN Fee Authority Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-10",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "5259",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Permanent OPTN Fee Authority Act",
      "type": "HR"
    },
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-02",
        "text": "Received in the Senate."
      },
      "number": "1262",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mikaela Naylon Give Kids a Chance Act",
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
            "name": "Computers and information technology",
            "updateDate": "2025-07-03T13:58:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-03T13:59:16Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-03T13:59:03Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-07-03T13:58:57Z"
          },
          {
            "name": "Organ and tissue donation and transplantation",
            "updateDate": "2025-07-03T13:58:40Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-07-03T13:58:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-10T17:54:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s532",
          "measure-number": "532",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s532v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>OPTN Fee Collection Authority Act</strong></p><p>This bill authorizes the Health Resources and Services Administration (HRSA), for three years, to collect registration fees directly from a member of the Organ Procurement and Transplantation Network (OPTN) (e.g., organ procurement organizations and\u00a0transplant hospitals) for each transplant candidate the member places on the waiting list. </p><p> Registration fees for the OPTN were historically collected through a contractor. The bill authorizes\u00a0HRSA, for three years following the bill\u2019s enactment, to collect registration fees directly from OPTN members for each candidate they place on the list and distribute the fees to support the operation of the OPTN. HRSA must publish on the OPTN website the amount of fees collected from each member and their use.</p><p>The bill requires the Government Accountability Office to conduct a review relating to the registration fees and report to Congress within two years after the bill\u2019s enactment.</p><p>Additionally, the bill supports (1) the integration of electronic health records systems into the OPTN, such as automated referrals and granting procurement organizations access to records of potential donors; and (2) the establishment of a dashboard to display statistics relating to the OPTN.</p>"
        },
        "title": "OPTN Fee Collection Authority Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s532.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>OPTN Fee Collection Authority Act</strong></p><p>This bill authorizes the Health Resources and Services Administration (HRSA), for three years, to collect registration fees directly from a member of the Organ Procurement and Transplantation Network (OPTN) (e.g., organ procurement organizations and\u00a0transplant hospitals) for each transplant candidate the member places on the waiting list. </p><p> Registration fees for the OPTN were historically collected through a contractor. The bill authorizes\u00a0HRSA, for three years following the bill\u2019s enactment, to collect registration fees directly from OPTN members for each candidate they place on the list and distribute the fees to support the operation of the OPTN. HRSA must publish on the OPTN website the amount of fees collected from each member and their use.</p><p>The bill requires the Government Accountability Office to conduct a review relating to the registration fees and report to Congress within two years after the bill\u2019s enactment.</p><p>Additionally, the bill supports (1) the integration of electronic health records systems into the OPTN, such as automated referrals and granting procurement organizations access to records of potential donors; and (2) the establishment of a dashboard to display statistics relating to the OPTN.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119s532"
    },
    "title": "OPTN Fee Collection Authority Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>OPTN Fee Collection Authority Act</strong></p><p>This bill authorizes the Health Resources and Services Administration (HRSA), for three years, to collect registration fees directly from a member of the Organ Procurement and Transplantation Network (OPTN) (e.g., organ procurement organizations and\u00a0transplant hospitals) for each transplant candidate the member places on the waiting list. </p><p> Registration fees for the OPTN were historically collected through a contractor. The bill authorizes\u00a0HRSA, for three years following the bill\u2019s enactment, to collect registration fees directly from OPTN members for each candidate they place on the list and distribute the fees to support the operation of the OPTN. HRSA must publish on the OPTN website the amount of fees collected from each member and their use.</p><p>The bill requires the Government Accountability Office to conduct a review relating to the registration fees and report to Congress within two years after the bill\u2019s enactment.</p><p>Additionally, the bill supports (1) the integration of electronic health records systems into the OPTN, such as automated referrals and granting procurement organizations access to records of potential donors; and (2) the establishment of a dashboard to display statistics relating to the OPTN.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119s532"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s532is.xml"
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
      "title": "OPTN Fee Collection Authority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "OPTN Fee Collection Authority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Health and Human Services to collect registration fees from members of the Organ Procurement and Transplantation Network, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:31Z"
    }
  ]
}
```
