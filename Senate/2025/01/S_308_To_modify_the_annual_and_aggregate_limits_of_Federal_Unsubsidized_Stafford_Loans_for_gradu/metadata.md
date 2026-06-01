# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/308
- Title: Graduate Opportunity and Affordable Loans Act
- Congress: 119
- Bill type: S
- Bill number: 308
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/308",
    "number": "308",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Graduate Opportunity and Affordable Loans Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T20:01:04Z",
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
      "sponsorshipDate": "2025-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s308is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 308\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Tuberville (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo modify the annual and aggregate limits of Federal Unsubsidized Stafford Loans for graduate and professional students, and to terminate Federal Direct PLUS Loans for graduate and professional students, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Graduate Opportunity and Affordable Loans Act .\n#### 2. Loan reforms\nSection 455 of the Higher Education Act of 1965 (20 U.S.C.1087e) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3)(A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking part B and inserting part B\u2014\n**(ii)**\nbeginning in the matter preceding clause (i), by striking for any period and all that follows through professional student and inserting the following:\n(i) for any period of instruction beginning on or after July 1, 2012, a graduate or professional student ; and\n**(iii)**\nin clause (ii), by inserting for any period of instruction beginning on July 1, 2012 and ending on June 30, 2025 (subject to paragraph (4)(C)), before the maximum annual ; and\n**(B)**\nby adding at the end the following:\n(4) Graduate and professional annual and aggregate limits for Unsubsidized Stafford loans beginning July 1, 2025 (A) Annual limits beginning July 1, 2025 Subject to subparagraph (C), beginning on July 1, 2025, the maximum annual amount of Federal Direct Unsubsidized Stafford loans\u2014 (i) a graduate student, who is not a professional student, may borrow in any academic year (as defined in section 481(a)(2)) or its equivalent shall be $20,500; and (ii) a professional student may borrow in any academic year (as defined in section 481(a)(2)) or its equivalent shall be $40,500. (B) Aggregate limits beginning July 1, 2025 Subject to subparagraph (C), beginning on July 1, 2025, the maximum aggregate amount of Federal Direct Unsubsidized Stafford loans\u2014 (i) a graduate student, who is not a professional student, may borrow is $65,000, in addition to the amount borrowed for undergraduate education; and (ii) a professional student may borrow is $130,000, in addition to the amount borrowed for undergraduate education. (C) Phase out provisions Notwithstanding the date of the applicability of the limits set forth in this paragraph, an eligible graduate student, including a professional student, who received a disbursement of a Federal Direct Unsubsidized Stafford loan after June 30, 2024, and before July 1, 2025, for the 2024\u20132025 award year, may receive a Federal Direct Unsubsidized Stafford loan for the 2025\u20132026 award year in amounts that are subject to the annual and aggregate loan limits applicable prior to July 1, 2025, if the borrower did not graduate prior to the 2025\u20132026 award year. (D) Definitions In this paragraph: (i) Graduate student The term graduate student means a student enrolled in a program at the postbaccalaureate level, such as a postbaccalaureate certificate, a master\u2019s degree, or a doctor\u2019s degree. (ii) Professional student The term professional student means a student enrolled in a doctor\u2019s degree-professional practice program. (iii) Postbaccalaureate certificate; master's degree; doctor's degree; doctor's degree professional-practice The terms postbaccalaureate certificate , master\u2019s degree , doctor\u2019s degree , and doctor\u2019s degree professional-practice shall have the meaning provided in the 2022\u20132023 glossary of the Integrated Postsecondary Education Data System (OMB NO. 1859\u20130582 v. 30). (5) Termination of authority to make Federal Direct PLUS loans to graduate and professional students (A) In general Notwithstanding any other provision of law, for any period of instruction beginning on or after July 1, 2025, a graduate student (including a professional student) shall not be eligible to receive a Federal Direct PLUS Loan under this part for enrollment in a program of graduate or doctor's degree professional-practice education. (B) Phase out provisions Not later than 30 days after the date of enactment of the Graduate Opportunity and Affordable Loans Act, each institution of higher education that enrolls graduate students or professional students shall notify prospective and enrolled graduate students and professional students that the Federal Direct PLUS Loan program will end for graduate students and professional students on June 30, 2025. (C) Definitions The definitions in paragraph (4)(D) shall apply to this paragraph. (6) Institutionally-determined limits Notwithstanding any other provision of this part, an eligible institution (at the discretion of a financial aid administrator at the institution) may prorate or limit the amount of a loan a student who is enrolled in a program of study at that institution for a period of instruction beginning on or after July 1, 2025, may borrow under this part for an academic year, as long as any proration or limit is applied consistently to all borrowers entering such program of study. .",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
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
            "updateDate": "2025-04-07T14:32:38Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-07T14:32:24Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-04-07T14:32:32Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2025-04-07T14:32:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-11T15:05:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s308",
          "measure-number": "308",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s308v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Graduate Opportunity and Affordable Loans Act</strong></p><p>This bill limits federal student loan borrowing for graduate and professional students.</p><p>Specifically, the bill terminates the ability of a graduate or professional student to receive a Direct PLUS Loan. Institutions of higher education (IHEs) must notify their prospective and enrolled graduate and professional students that Direct PLUS Loans terminate on June 30, 2025.</p><p>Additionally, the bill establishes the aggregate loan limit for Direct Unsubsidized Loans as $65,000 for a graduate student (in addition to the amount borrowed for undergraduate education) and $130,000 for a professional student (in addition to the amount borrowed for undergraduate education).</p><p>The bill allows IHEs to set lower loan limits.</p>"
        },
        "title": "Graduate Opportunity and Affordable Loans Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s308.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Graduate Opportunity and Affordable Loans Act</strong></p><p>This bill limits federal student loan borrowing for graduate and professional students.</p><p>Specifically, the bill terminates the ability of a graduate or professional student to receive a Direct PLUS Loan. Institutions of higher education (IHEs) must notify their prospective and enrolled graduate and professional students that Direct PLUS Loans terminate on June 30, 2025.</p><p>Additionally, the bill establishes the aggregate loan limit for Direct Unsubsidized Loans as $65,000 for a graduate student (in addition to the amount borrowed for undergraduate education) and $130,000 for a professional student (in addition to the amount borrowed for undergraduate education).</p><p>The bill allows IHEs to set lower loan limits.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s308"
    },
    "title": "Graduate Opportunity and Affordable Loans Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Graduate Opportunity and Affordable Loans Act</strong></p><p>This bill limits federal student loan borrowing for graduate and professional students.</p><p>Specifically, the bill terminates the ability of a graduate or professional student to receive a Direct PLUS Loan. Institutions of higher education (IHEs) must notify their prospective and enrolled graduate and professional students that Direct PLUS Loans terminate on June 30, 2025.</p><p>Additionally, the bill establishes the aggregate loan limit for Direct Unsubsidized Loans as $65,000 for a graduate student (in addition to the amount borrowed for undergraduate education) and $130,000 for a professional student (in addition to the amount borrowed for undergraduate education).</p><p>The bill allows IHEs to set lower loan limits.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119s308"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s308is.xml"
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
      "title": "Graduate Opportunity and Affordable Loans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Graduate Opportunity and Affordable Loans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the annual and aggregate limits of Federal Unsubsidized Stafford Loans for graduate and professional students, and to terminate Federal Direct PLUS Loans for graduate and professional students, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:33Z"
    }
  ]
}
```
