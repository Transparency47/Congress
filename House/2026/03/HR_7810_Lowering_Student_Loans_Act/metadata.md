# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7810?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7810
- Title: Lowering Student Loans Act
- Congress: 119
- Bill type: HR
- Bill number: 7810
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-04-10T08:06:15Z
- Update date including text: 2026-04-10T08:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7810",
    "number": "7810",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Lowering Student Loans Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:15Z",
    "updateDateIncludingText": "2026-04-10T08:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "GU"
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
      "sponsorshipDate": "2026-04-09",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7810ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7810\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mr. Thompson of California (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to set interest rates for Federal student loans made on or after July 1, 2026, at 2 percent, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lowering Student Loans Act .\n#### 2. Interest rates for Federal student loans\n##### (a) Federal Direct Loans\nSection 455(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (9) and (10) as paragraphs (10) and (11), respectively;\n**(2)**\nin paragraph (8)\u2014\n**(A)**\nin the heading of such paragraph, by striking 2013. and inserting 2013 and before July 1, 2026. ; and\n**(B)**\nin subparagraphs (A) through (D), by inserting and before July 1, 2026, after July 1, 2013, ; and\n**(3)**\nby inserting after paragraph (8) the following:\n(9) Interest rate provisions for loans on or after July 1, 2026 (A) Rates for Direct Loans other than Consolidation Loans (i) New loans Notwithstanding the preceding paragraphs of this subsection, for Federal Direct Stafford Loans, Federal Direct Unsubsidized Stafford Loans, and Federal Direct PLUS Loans (including such a loan made to a parent on behalf of a dependent student) for which the first disbursement is made on or after July 1, 2026, the applicable rate of interest shall be 2 percent on the unpaid principal balance of the loan. (ii) Existing loans Notwithstanding the preceding paragraphs of this subsection and subject to subparagraphs (C) and (D), with respect to a loan described in clause (i) for which the first disbursement was made before July 1, 2026, and for which the applicable rate of interest is greater than 2 percent, beginning on July 1, 2026, the applicable rate of interest for such loan shall be 2 percent on the unpaid principal balance of such loan. (B) Rates for Consolidation Loans (i) New loans Notwithstanding the preceding paragraphs of this subsection, any Federal Direct Consolidation Loan for which the application is received on or after July 1, 2026, shall bear interest at an annual rate on the unpaid principal balance of the loan that is 2 percent. (ii) Existing loans Notwithstanding the preceding paragraphs of this subsection and subject to subparagraphs (C) and (D), any Federal Direct Consolidation Loan for which the application was received before July 1, 2026, and which bears interest at an annual rate on the unpaid principal balance of the loan that is greater than 2 percent, shall, beginning on July 1, 2026, bear interest at an annual rate on the unpaid principal balance of the loan that is 2 percent. (iii) FFEL consolidation loans A borrower of a consolidation loan made, insured, or guaranteed under part B may consolidate such loan into a Federal Direct Consolidation Loan under this part in accordance with section 428C(a)(3)(B)(i)(V). (C) Notice and opt out for existing loans With respect to each borrower with a loan described in subparagraph (A)(ii) or a Federal Direct Consolidation Loan described in subparagraph (B)(ii), the Secretary shall\u2014 (i) not later than the date that is 90 days before July 1, 2026, provide to the borrower notice of the adjustment of the applicable rate of interest for such a loan pursuant to this paragraph, which shall include information relating to opting out of such adjustment as described in clause (ii); and (ii) allow the borrower to, not later than 90 days after receiving such notice, opt out of such adjustment. (D) Terms and conditions Except as expressly provided in subparagraphs (A) and (B), nothing in this paragraph may be construed to alter or affect the terms, conditions, or benefits of a loan described in this paragraph. (E) Rate The applicable rate of interest under this paragraph for Federal Direct Stafford Loans, Federal Direct Unsubsidized Stafford Loans, Federal Direct PLUS Loans (including such a loan made to a parent on behalf of a dependent student), and Federal Direct Consolidation Loans shall be fixed for the period of the loan. (F) Loan servicers Not later than the date that is 90 days before July 1, 2026, the Secretary shall\u2014 (i) notify student loan servicers of the rate adjustments for all loans pursuant to this paragraph; and (ii) establish a borrower complaint resolution process with respect to any errors or delays relating to such adjustments. .\n##### (b) FFEL loans\nSection 428C(a)(3)(B)(i)(V) of the Higher Education Act of 1965 ( 20 U.S.C. 1078\u20133(a)(3)(B)(i)(V) ) is amended\u2014\n**(1)**\nin item (cc), by striking the period at the end and inserting a semicolon;\n**(2)**\nin item (dd), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(ee) for the purpose of being eligible for the annual interest rate described in section 455(b)(9)(C). .",
      "versionDate": "2026-03-04",
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
        "name": "Education",
        "updateDate": "2026-04-01T20:01:25Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7810ih.xml"
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
      "title": "Lowering Student Loans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lowering Student Loans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to set interest rates for Federal student loans made on or after July 1, 2026, at 2 percent, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T06:48:32Z"
    }
  ]
}
```
