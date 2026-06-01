# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1759?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1759
- Title: Affordable PLUS Repayment Options for Parents Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1759
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-02-06T19:42:13Z
- Update date including text: 2026-02-06T19:42:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1759",
    "number": "1759",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Affordable PLUS Repayment Options for Parents Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-06T19:42:13Z",
    "updateDateIncludingText": "2026-02-06T19:42:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:06:45Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "VA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "DC"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "AL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NM"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MI"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MS"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MI"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1759ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1759\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Waters (for herself, Ms. Adams , Ms. Bynum , Mr. Carson , Mr. Davis of Illinois , Mr. Doggett , Ms. Jayapal , Ms. Johnson of Texas , Ms. McClellan , Mrs. McIver , Ms. Norton , Mr. Olszewski , Mrs. Ramirez , Ms. Schakowsky , Ms. Sewell , Ms. Stansbury , Mr. Swalwell , Mr. Thanedar , Mr. Thompson of Mississippi , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to allow borrowers of Parent PLUS loans or loans under section 428B made on behalf of a dependent student to repay such loans pursuant to an income-contingent repayment plan or income-based repayment plan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Affordable PLUS Repayment Options for Parents Act of 2025 .\n#### 2. Income-contingent repayment plan\nSection 455 of the Higher Education Act of 1965 ( 20 U.S.C. 1087e ) is amended\u2014\n**(1)**\nin subsection (d)(1)(D), by striking , except that the plan described in this subparagraph shall not be available to the borrower of a Federal Direct PLUS loan made on behalf of a dependent student ; and\n**(2)**\nin subsection (e)(1), by inserting at the end the following: An income contingent repayment plan under this subsection shall be available to a borrower of a Federal Direct PLUS loan made on behalf of a dependent student or a Federal Direct Consolidation Loan the proceeds of which were used to discharge the liability on such a Federal Direct PLUS loan. .\n#### 3. Income-based repayment plan\n##### (a) Clarification of IBR\nSection 455(d)(1)(E) of such Act ( 20 U.S.C. 1087e(d)(1)(E) ) is amended by striking , except that the plan described in this subparagraph shall not be available to the borrower of a Federal Direct PLUS Loan made on behalf of a dependent student or a Federal Direct Consolidation Loan, if the proceeds of such loan were used to discharge the liability on such Federal Direct PLUS Loan or a loan under section 428B made on behalf of a dependent student .\n##### (b) IBR\nSection 493C of the Higher Education Act of 1965 ( 20 U.S.C. 1098e ) is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) Definition In this section, the term partial financial hardship , when used with respect to a borrower, means that for such borrower\u2014 (1) the annual amount due on the total amount of loans made, insured, or guaranteed under part B or D to a borrower as calculated under the standard repayment plan under section 428(b)(9)(A)(i) or 455(d)(1)(A), based on a 10-year repayment period; exceeds (2) 15 percent of the result obtained by calculating, on at least an annual basis, the amount by which\u2014 (A) the borrower's, and the borrower's spouse's (if applicable), adjusted gross income; exceeds (B) 150 percent of the poverty line applicable to the borrower's family size as determined under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ). ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking (other than an excepted PLUS loan or excepted consolidation loan) ;\n**(B)**\nin paragraph (6)(A), by striking (other than an excepted PLUS loan or excepted consolidation loan) ; and\n**(C)**\nin paragraph (7), by striking (other than a loan under section 428B or a Federal Direct PLUS Loan) ; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by striking (other than an excepted PLUS loan or excepted consolidation loan), ; and\n**(B)**\nin paragraph (2)(B), by striking (other than an excepted PLUS loan or excepted consolidation loan) .\n#### 4. Effective date and application\nThe amendments made by this Act shall take effect on the date of enactment of this Act, and shall apply with respect to each borrower who, on or after such date\u2014\n**(1)**\nhas an outstanding balance on a Federal Direct PLUS Loan (or a loan under section 428B) made on behalf of a dependent student or a Federal Direct Consolidation Loan the proceeds of which were used to discharge the liability on such a Federal Direct PLUS loan (or on such a loan under section 428B); and\n**(2)**\nis repaying or will repay such loan pursuant to an income-contingent repayment plan under section 455(e) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(e) ) or an income-based repayment plan under section 493C of such Act ( 20 U.S.C. 1098e ).",
      "versionDate": "2025-02-27",
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
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-02-06T19:42:08Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-02-06T19:41:59Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-02-06T19:42:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-21T17:19:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1759",
          "measure-number": "1759",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-09-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1759v00",
            "update-date": "2025-09-08"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Affordable PLUS Repayment Options for Parents Act of 2025</strong></p><p>This bill allows borrowers of Parent PLUS Loans to repay their loans under an income-contingent repayment (ICR) plan or an income-based repayment (IBR) plan.</p><p>Under current law, borrowers of Parent PLUS Loans are only eligible for the following repayment plans: the standard repayment plan, the graduated repayment plan, and the extended repayment plan. These borrowers are generally prohibited from repaying their loans under ICR or IBR plans. However, borrowers may become eligible for the ICR plan upon consolidation of their loans into a Direct Consolidation Loan. This bill removes these restrictions to allow a borrower of a Parent PLUS Loan to repay the loan under an\u00a0ICR plan (even without consolidation) or an\u00a0IBR plan.</p><p>The bill allows these expanded repayment options to be available to new and existing borrowers of Parent PLUS Loans.</p>"
        },
        "title": "Affordable PLUS Repayment Options for Parents Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1759.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Affordable PLUS Repayment Options for Parents Act of 2025</strong></p><p>This bill allows borrowers of Parent PLUS Loans to repay their loans under an income-contingent repayment (ICR) plan or an income-based repayment (IBR) plan.</p><p>Under current law, borrowers of Parent PLUS Loans are only eligible for the following repayment plans: the standard repayment plan, the graduated repayment plan, and the extended repayment plan. These borrowers are generally prohibited from repaying their loans under ICR or IBR plans. However, borrowers may become eligible for the ICR plan upon consolidation of their loans into a Direct Consolidation Loan. This bill removes these restrictions to allow a borrower of a Parent PLUS Loan to repay the loan under an\u00a0ICR plan (even without consolidation) or an\u00a0IBR plan.</p><p>The bill allows these expanded repayment options to be available to new and existing borrowers of Parent PLUS Loans.</p>",
      "updateDate": "2025-09-08",
      "versionCode": "id119hr1759"
    },
    "title": "Affordable PLUS Repayment Options for Parents Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Affordable PLUS Repayment Options for Parents Act of 2025</strong></p><p>This bill allows borrowers of Parent PLUS Loans to repay their loans under an income-contingent repayment (ICR) plan or an income-based repayment (IBR) plan.</p><p>Under current law, borrowers of Parent PLUS Loans are only eligible for the following repayment plans: the standard repayment plan, the graduated repayment plan, and the extended repayment plan. These borrowers are generally prohibited from repaying their loans under ICR or IBR plans. However, borrowers may become eligible for the ICR plan upon consolidation of their loans into a Direct Consolidation Loan. This bill removes these restrictions to allow a borrower of a Parent PLUS Loan to repay the loan under an\u00a0ICR plan (even without consolidation) or an\u00a0IBR plan.</p><p>The bill allows these expanded repayment options to be available to new and existing borrowers of Parent PLUS Loans.</p>",
      "updateDate": "2025-09-08",
      "versionCode": "id119hr1759"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1759ih.xml"
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
      "title": "Affordable PLUS Repayment Options for Parents Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:50Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable PLUS Repayment Options for Parents Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to allow borrowers of Parent PLUS loans or loans under section 428B made on behalf of a dependent student to repay such loans pursuant to an income-contingent repayment plan or income-based repayment plan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:49Z"
    }
  ]
}
```
