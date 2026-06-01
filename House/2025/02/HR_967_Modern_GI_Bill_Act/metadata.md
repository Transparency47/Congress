# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/967?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/967
- Title: Modern GI Bill Act
- Congress: 119
- Bill type: HR
- Bill number: 967
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-03-19T15:50:54Z
- Update date including text: 2025-03-19T15:50:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-05 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-05 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/967",
    "number": "967",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Modern GI Bill Act",
    "type": "HR",
    "updateDate": "2025-03-19T15:50:54Z",
    "updateDateIncludingText": "2025-03-19T15:50:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-05T22:42:40Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr967ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 967\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to allow individuals who are entitled to Post-9/11 educational assistance to use such assistance to repay Federal student loans.\n#### 1. Short title\nThis Act may be cited as the Modern GI Bill Act .\n#### 2. Use of Post-9/11 educational assistance to repay Federal student loans\n##### (a) Authority\nSubchapter II of chapter 33 of title 38, United States Code, is amended by inserting after section 3320 the following new section:\n3320A. Use of educational assistance benefits for the repayment of Federal student loans (a) Use of benefits Notwithstanding any other provision of this chapter, an individual who is entitled to educational assistance for tuition or fees under this subchapter may apply amounts of such educational assistance to repay some or all of the outstanding balance of principal and interest due on a Federal student loan to the individual. (b) Maximum annual amount; annual adjustment (1) Payment of educational assistance under this section to an individual during fiscal year 2026 may not exceed $15,900. (2) In each fiscal year after fiscal year 2026, the dollar amount in paragraph (1) shall be increased by the same percentage as the percentage by which benefit amounts payable under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) are increased effective December 1 of that year as a result of a determination under section 215(i) of such Act ( 42 U.S.C. 415(i) ). (c) Monthly payments: maximum amount; maximum number (1) The Secretary shall make monthly payments under this section in such amounts as an individual who is entitled to educational assistance for tuition or fees under this subchapter may elect for the repayment of a Federal student loan to that individual. No such amount may exceed one-twelfth of the maximum annual amount calculated under subsection (b)(1). (2) The total number of months of payments for the repayment of a Federal student loan to an individual under this section may not exceed 36 months. (d) Benefit non-Transferable Notwithstanding section 3319 of this title, an individual who is entitled to educational assistance under this section may not transfer such assistance to another individual. (e) Eligible payees The Secretary shall make payments of educational assistance under this section directly to the lender of the Federal student loan of the individual who is entitled to educational assistance under this section. (f) Arrangements To make payments; regulations The Secretary shall enter into such arrangements, and shall prescribe such regulations, that the Secretary determines necessary to carry out this section. (g) Federal student loan defined In this section, the term Federal student loan means any loan made, insured, or guaranteed under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ). .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 3320 the following new item:\n3320A. Use of educational assistance benefits for the repayment of Federal student loans. .\n##### (c) Effective date\nThe amendments made by this section shall apply to educational assistance paid for months beginning on or after the date of the enactment of this Act.",
      "versionDate": "2025-02-04",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T18:48:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr967",
          "measure-number": "967",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr967v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Modern GI Bill Act</strong></p><p>This bill authorizes individuals who are entitled to educational assistance under the Post-9/11 GI Bill to apply amounts of such assistance to repay federal student loans for up to 36 months.</p><p>The bill sets a cap and annual cost-of-living increases for the amount of educational assistance that may be paid to an individual under this bill during FY2026 and the following years.</p>"
        },
        "title": "Modern GI Bill Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr967.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Modern GI Bill Act</strong></p><p>This bill authorizes individuals who are entitled to educational assistance under the Post-9/11 GI Bill to apply amounts of such assistance to repay federal student loans for up to 36 months.</p><p>The bill sets a cap and annual cost-of-living increases for the amount of educational assistance that may be paid to an individual under this bill during FY2026 and the following years.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr967"
    },
    "title": "Modern GI Bill Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Modern GI Bill Act</strong></p><p>This bill authorizes individuals who are entitled to educational assistance under the Post-9/11 GI Bill to apply amounts of such assistance to repay federal student loans for up to 36 months.</p><p>The bill sets a cap and annual cost-of-living increases for the amount of educational assistance that may be paid to an individual under this bill during FY2026 and the following years.</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr967"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr967ih.xml"
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
      "title": "Modern GI Bill Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modern GI Bill Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to allow individuals who are entitled to Post-9/11 educational assistance to use such assistance to repay Federal student loans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:55Z"
    }
  ]
}
```
