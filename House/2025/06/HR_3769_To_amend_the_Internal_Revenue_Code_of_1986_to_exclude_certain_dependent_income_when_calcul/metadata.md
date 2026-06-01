# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3769?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3769
- Title: Dependent Income Exclusion Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3769
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-07-17T15:40:33Z
- Update date including text: 2025-07-17T15:40:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3769",
    "number": "3769",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Dependent Income Exclusion Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-17T15:40:33Z",
    "updateDateIncludingText": "2025-07-17T15:40:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3769ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3769\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Horsford (for himself and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude certain dependent income when calculating modified adjusted gross income for the purposes of eligibility for premium tax credits.\n#### 1. Short title\nThis Act may be cited as the Dependent Income Exclusion Act of 2025 .\n#### 2. Exclusion of certain dependent income for purposes of premium tax credit\n##### (a) In general\nParagraph (2) of section 36B(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Exception for certain dependent income (i) In general There shall not be taken into account under subparagraph (A)(ii) any wages (determined under section 3401(a)) or net earnings from self-employment (as defined in section 1402(a)) of any dependent of the taxpayer who\u2014 (I) has not attained age 18 as of the last day of the calendar year in which the taxable year of the taxpayer begins, or (II) has not attained age 24 as of the last day of such calendar year and, during each of 5 calendar months during such calendar year, is described in subparagraph (A) or (B) of section 152(f)(2) (applied by substituting part-time or full-time for full-time each place it appears, and by deeming any for-profit educational institution not to be an educational organization described in section 170(b)(1)(A)(ii)), is participating in a qualified job-training program, or is participating in an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ). (ii) Qualified job-training program For purposes of this subparagraph, the term qualified job-training program means any program of training services described in section 134(c)(3) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3174(c)(3) ). (iii) Limitation Clause (i) shall not apply to so much of the aggregate income of all dependents of the taxpayer as exceeds an amount equal to 15 percent of the modified adjusted gross income of the taxpayer. (iv) Taxpayers residing in Medicaid non-expansion States In the case of a taxpayer residing in a State which (as of the first day of the taxable year) does not provide for eligibility under clause (i)(VIII) or (ii)(XX) of section 1902(a)(10)(A) of the Social Security Act for medical assistance under title XIX of such Act (or a waiver of the State plan approved under section 1115 of the Social Security Act), clause (i) shall apply to any dependent of such taxpayer only to the extent that the application of such clause would not reduce the household income below 100 percent of the amount equal to the poverty line for a family of the size involved. .\n##### (b) Conforming amendments\n**(1)**\nClause (ii) of section 36B(d)(2)(A) of the Internal Revenue Code of 1986 is amended by inserting , except as provided in subparagraph (C), after individuals .\n**(2)**\nParagraph (3) of section 1411(b) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18081 ) is amended by adding at the end the following new subparagraph:\n(D) Information regarding certain dependents Information regarding whether section 36B(d)(2)(C) will apply to any individuals taken into account as members of the household of the enrollee, and the amount of income from employment of each such individual for the taxable year described in subparagraph (A). .\n##### (c) Effective date\nThe amendments made by this section shall apply to credits allowed under section 36B of the Internal Revenue Code of 1986 for, and advance payments of credits under section 1412 of the Patient Protection and Affordable Care Act with respect to, taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-06-05",
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
        "name": "Taxation",
        "updateDate": "2025-06-25T20:27:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
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
          "measure-id": "id119hr3769",
          "measure-number": "3769",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3769v00",
            "update-date": "2025-07-17"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dependent Income Exclusion Act of 2025</strong></p><p>This bill excludes the wages and net earnings from self-employment of a dependent of a taxpayer\u00a0from the calculation of total household income for purposes of determining eligibility for and the amount of the refundable premium tax credit, subject to limitations.</p><p>Under current law, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL). For tax years before 2021 and after 2025, taxpayers must have a household income that meets or exceeds 100% but is less than 400% of the FPL to be eligible for the tax credit.</p><p>Further, under current law, the calculation of the premium tax credit is based, in part, on taxpayers\u2019 household income such that taxpayers with lower household incomes are eligible for a higher premium tax credit.</p><p>The bill excludes from household income the wages and net earnings from self-employment of a dependent of the taxpayer who (1) is under 18 years old; or (2) is under 24 years old and is, during\u00a0any five calendar months of the year, a full- or part-time student in an educational organization (excluding for-profit educational institutions), is in an apprentice program, or is participating in a job training program.</p><p>The amount that may be excluded is limited to 15% of the taxpayer\u2019s modified adjusted gross income.\u00a0</p>"
        },
        "title": "Dependent Income Exclusion Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3769.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dependent Income Exclusion Act of 2025</strong></p><p>This bill excludes the wages and net earnings from self-employment of a dependent of a taxpayer\u00a0from the calculation of total household income for purposes of determining eligibility for and the amount of the refundable premium tax credit, subject to limitations.</p><p>Under current law, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL). For tax years before 2021 and after 2025, taxpayers must have a household income that meets or exceeds 100% but is less than 400% of the FPL to be eligible for the tax credit.</p><p>Further, under current law, the calculation of the premium tax credit is based, in part, on taxpayers\u2019 household income such that taxpayers with lower household incomes are eligible for a higher premium tax credit.</p><p>The bill excludes from household income the wages and net earnings from self-employment of a dependent of the taxpayer who (1) is under 18 years old; or (2) is under 24 years old and is, during\u00a0any five calendar months of the year, a full- or part-time student in an educational organization (excluding for-profit educational institutions), is in an apprentice program, or is participating in a job training program.</p><p>The amount that may be excluded is limited to 15% of the taxpayer\u2019s modified adjusted gross income.\u00a0</p>",
      "updateDate": "2025-07-17",
      "versionCode": "id119hr3769"
    },
    "title": "Dependent Income Exclusion Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dependent Income Exclusion Act of 2025</strong></p><p>This bill excludes the wages and net earnings from self-employment of a dependent of a taxpayer\u00a0from the calculation of total household income for purposes of determining eligibility for and the amount of the refundable premium tax credit, subject to limitations.</p><p>Under current law, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL). For tax years before 2021 and after 2025, taxpayers must have a household income that meets or exceeds 100% but is less than 400% of the FPL to be eligible for the tax credit.</p><p>Further, under current law, the calculation of the premium tax credit is based, in part, on taxpayers\u2019 household income such that taxpayers with lower household incomes are eligible for a higher premium tax credit.</p><p>The bill excludes from household income the wages and net earnings from self-employment of a dependent of the taxpayer who (1) is under 18 years old; or (2) is under 24 years old and is, during\u00a0any five calendar months of the year, a full- or part-time student in an educational organization (excluding for-profit educational institutions), is in an apprentice program, or is participating in a job training program.</p><p>The amount that may be excluded is limited to 15% of the taxpayer\u2019s modified adjusted gross income.\u00a0</p>",
      "updateDate": "2025-07-17",
      "versionCode": "id119hr3769"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3769ih.xml"
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
      "title": "Dependent Income Exclusion Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dependent Income Exclusion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude certain dependent income when calculating modified adjusted gross income for the purposes of eligibility for premium tax credits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:18:17Z"
    }
  ]
}
```
