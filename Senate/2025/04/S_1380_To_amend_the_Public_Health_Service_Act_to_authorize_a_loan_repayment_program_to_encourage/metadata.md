# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1380
- Title: SPARC Act
- Congress: 119
- Bill type: S
- Bill number: 1380
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1380",
    "number": "1380",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "SPARC Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
        "item": [
          {
            "date": "2026-03-19T14:00:16Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-04-09T19:42:30Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "MS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "VT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1380is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1380\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Ms. Rosen (for herself and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to authorize a loan repayment program to encourage specialty medicine physicians to serve in rural communities experiencing a shortage of specialty medicine physicians, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Specialty Physicians Advancing Rural Care Act or the SPARC Act .\n#### 2. Specialty medical practitioners workforce in rural communities\nTitle VII of the Public Health Service Act ( 42 U.S.C. 292 et seq. ) is amended\u2014\n**(1)**\nby redesignating part G ( 42 U.S.C. 795j et seq. ) as part H; and\n**(2)**\nby inserting after part F ( 42 U.S.C. 295h ) the following new part:\nG Specialty medicine workforce in rural communities 782. Loan repayment program (a) In general (1) Program for specialty medicine physicians The Secretary, acting through the Administrator of the Health Resources and Services Administration, shall carry out a program under which\u2014 (A) the Secretary enters into agreements with specialty medicine physicians to make payments in accordance with subsection (b) on the principal of and interest on any eligible loans described in subsection (c); and (B) the specialty medicine physicians each agree to complete a period of obligated service described in subsection (d) as a specialty medicine physician in the United States in a rural community experiencing a shortage of specialty medicine physicians. (2) Program for non-physician specialty health care providers The Secretary, acting through the Administrator of the Health Resources and Services Administration, may carry out a program under which\u2014 (A) the Secretary enters into agreements with non-physician specialty health care providers to make payments in accordance with subsection (b) on the principal of and interest on any eligible loans described in subsection (c); and (B) the non-physician specialty health care providers each agree to complete a period of obligated service described in subsection (d) as a non-physician specialty health care provider in the United States in a rural community experiencing a shortage of such providers. (b) Payments For each year of obligated service by a specialty medicine physician pursuant to an agreement under subsection (a)(1) or by a non-physician specialty health care provider pursuant to an agreement under subsection (a)(2), the Secretary shall make a payment to such physician or provider as follows: (1) Service in shortage area The Secretary shall pay\u2014 (A) for each year of obligated service by a specialty medicine physician or non-physician specialty health care provider pursuant to an agreement under paragraph (1) or (2) of subsection (a), 1/6 of the principal of and interest on each eligible loan of the physician or provider which is outstanding on the date the physician or provider began service pursuant to the agreement; and (B) for completion of the sixth and final year of such service, the remainder of such principal and interest. (2) Maximum amount The total amount of payments under this section to any specialty medicine physician or non-physician specialty health care provider shall not exceed $250,000. (c) Eligible loans The loans eligible for repayment under this section are each of the following: (1) Any loan for education in specialty medicine or specialty health care. (2) Any Federal Direct Stafford Loan, Federal Direct PLUS Loan, Federal Direct Unsubsidized Stafford Loan, or Federal Direct Consolidation Loan (as such terms are used in section 455 of the Higher Education Act of 1965). (3) Any Federal Perkins Loan under part E of title I of the Higher Education Act of 1965. (4) Any other Federal loan as determined appropriate by the Secretary. (d) Period of obligated service Any specialty medicine physician or non-physician specialty health care provider receiving payments under this section as required by an agreement under paragraph (1) or (2) of subsection (a) shall agree to a 6-year commitment to full-time employment, with no more than 1 year passing between any 2 years of covered employment, as a specialty medicine physician or non-physician specialty health care provider, as applicable, in the United States in a rural community experiencing a shortage of specialty medicine physicians or non-physician specialty health care providers, as applicable. (e) Ineligibility for double benefits No borrower may, for the same service, receive a reduction of loan obligations or a loan repayment under both\u2014 (1) this section; and (2) any federally supported loan forgiveness program, including under section 338B, 338I, or 846 of this Act, or section 428J, 428L, 455(m), or 460 of the Higher Education Act of 1965. (f) Breach (1) Liquidated damages formula The Secretary may establish a liquidated damages formula to be used in the event of a breach of an agreement entered into under paragraph (1) or (2) of subsection (a). (2) Limitation The failure by a specialty medicine physician or a non-physician specialty health care provider to complete the full period of service obligated pursuant to such an agreement, taken alone, shall not constitute a breach of the agreement, so long as the physician or provider completed in good faith the years of service for which payments were made to the physician or provider under this section. (g) Special rules for non-Physician specialty health care providers Non-physician specialty health care providers participating in the program under this section are not eligible for other Federal loan forgiveness programs specific to health care providers. Not more than 15 percent of amounts made available to carry out this section for a fiscal year may be allocated to awards to non-physician specialty health care providers. (h) Reports to Congress Not later than 5 years after the date of enactment of this section, and not less than every other year thereafter through fiscal year 2033, the Secretary shall report to Congress on\u2014 (1) the practice location of special medicine physicians and non-physician specialty health care providers participating, or who have participated, in the loan repayment program under this section; and (2) the impact of the loan repayment program under this section on the availability of specialty medicine or specialty health care services in the United States in rural communities experiencing a shortage of specialty medicine physicians or non-physician specialty health care providers. (i) Data updates The Administrator of the Health Resources and Services Administration shall update publicly available data on the supply of specialty medicine physicians and non-physician specialty health care providers, as appropriate. (j) Definitions In this section: (1) Non-physician specialty health care provider The term non-physician specialty health care provider means a health professional other than a physician who is licensed to provide patient care other than primary care services. (2) Specialty medicine physician The term specialty medicine physician means a physician practicing in an area of medicine other than primary care. (k) Authorization of appropriations To carry out this section, there are authorized to be appropriated such sums as may be necessary for fiscal years 2025 through 2034. .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4681",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SPARC Act",
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
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-04-06T18:12:13Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2026-04-06T18:12:00Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-04-06T18:12:21Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-04-06T18:12:17Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-04-06T18:12:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-19T14:56:56Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1380is.xml"
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
      "title": "SPARC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SPARC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Specialty Physicians Advancing Rural Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to authorize a loan repayment program to encourage specialty medicine physicians to serve in rural communities experiencing a shortage of specialty medicine physicians, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:25Z"
    }
  ]
}
```
