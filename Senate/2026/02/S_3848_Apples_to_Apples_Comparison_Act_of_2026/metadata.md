# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3848
- Title: Apples to Apples Comparison Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3848
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-03-02T19:34:55Z
- Update date including text: 2026-03-02T19:34:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-11: Introduced in Senate

## Actions

- 2026-02-11 - IntroReferral: Introduced in Senate
- 2026-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3848",
    "number": "3848",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Apples to Apples Comparison Act of 2026",
    "type": "S",
    "updateDate": "2026-03-02T19:34:55Z",
    "updateDateIncludingText": "2026-03-02T19:34:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T22:11:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3848is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3848\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Scott of South Carolina introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to require the Secretary of Health and Human Services to publish information on expenditures under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Apples to Apples Comparison Act of 2026 .\n#### 2. Requiring the Secretary of Health and Human Services to publish information on expenditures under the Medicare program\nSection 1874 of the Social Security Act ( 42 U.S.C. 1395kk ) is amended\u2014\n**(1)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting (and, beginning with 2027, publish on the public website of the Centers for Medicare & Medicaid Services in machine-readable files information on) after a report on ;\n**(ii)**\nin subparagraph (A), by inserting (and, beginning with 2027, by county and Metropolitan Statistical Area) after State ; and\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (ii), by striking and at the end;\n**(II)**\nin clause (iii), by striking the period and inserting ; and ; and\n**(III)**\nby adding at the end the following new clause:\n(iv) beginning with 2027, each category of individuals described in subsection (h)(1). ; and\n**(B)**\nby adding at the end the following new paragraph:\n(3) Special rule for 2027 report and publication of information As part of the report and publication of information required under paragraph (1) for 2027, the Secretary shall include enrollment information submitted under this subsection for each preceding year (beginning with 2015), broken down by county and Metropolitan Statistical Area and provided for each category of individuals described in subsection (h)(1). ; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Information on expenditures (1) In general Not later than 30 days after the last day of each year (beginning with 2027), the Secretary shall, for each county and each Metropolitan Statistical Area, publish on the public website of the Centers for Medicare & Medicaid Services in machine-readable files the total and average expenditures under this title for items and services furnished to individuals entitled to benefits under part A or enrolled under part B residing in such county or Metropolitan Statistical Area for each month occurring in the specified historical period and for each month occurring in the specified projected period with respect to such year, broken down by the following categories of individuals: (A) Individuals entitled to benefits under part A and not enrolled under part B. (B) Individuals who are\u2014 (i) not entitled to benefits under part A; (ii) enrolled under part B; and (iii) not enrolled under a Medicare Advantage plan under part C. (C) Individuals who are\u2014 (i) entitled to benefits under part A and enrolled under part B; and (ii) not enrolled under a Medicare Advantage plan under part C. (D) Individuals described in subparagraph (A) who are enrolled in a prescription drug plan under part D. (E) Individuals described in subparagraph (B) who are enrolled in a prescription drug plan under part D. (F) Individuals described in subparagraph (C) who are enrolled in a prescription drug plan under part D. (G) Individuals described in subparagraph (A) who are not enrolled in a prescription drug plan under part D. (H) Individuals described in subparagraph (B) who are not enrolled in a prescription drug plan under part D. (I) Individuals described in subparagraph (C) who are not enrolled in a prescription drug plan under part D. (J) Individuals described in subparagraph (A) who are enrolled in a Federal health care program (as defined in section 1128B) or a health plan under chapter 89 of title 5, United States Code. (K) Individuals described in subparagraph (B) who are enrolled in such a program or plan. (L) Individuals described in subparagraph (C) who are enrolled in such a program or plan. (M) Individuals described in subparagraph (A) who are not enrolled in such a program or plan. (N) Individuals described in subparagraph (B) who are not enrolled in such a program or plan. (O) Individuals described in subparagraph (C) who are not enrolled in such a program or plan. (P) Individuals described in subparagraph (A) who are enrolled in a group health plan (as defined in section 2791 of the Public Health Service Act) or a medicare supplemental policy under section 1882. (Q) Individuals described in subparagraph (B) who are enrolled in such a plan or policy. (R) Individuals described in subparagraph (C) who are enrolled in such a plan or policy. (S) Individuals described in subparagraph (A) who are not enrolled in such a plan or policy. (T) Individuals described in subparagraph (B) who are not enrolled in such a plan or policy. (U) Individuals described in subparagraph (C) who are not enrolled in such a plan or policy. (V) Individuals enrolled in a specialized MA plan for special needs individuals, broken down by each type of plan. (W) Individuals enrolled in an MA plan other than a plan described in subparagraph (V). (X) Individuals enrolled in an MA plan. (Y) Individuals described in subparagraph (X) who are enrolled in a Federal health care program (as defined in section 1128B) or a health plan under chapter 89 of title 5, United States Code. (Z) Individuals described in subparagraph (X) who are not enrolled in such a program or plan. (AA) Individuals described in subparagraph (X) who are enrolled in a group health plan (as defined in section 2791 of the Public Health Service Act) or a medicare supplemental policy under section 1882. (BB) Individuals described in subparagraph (X) who are not enrolled in such a plan or policy. (CC) Individuals described in subparagraph (X) who are enrolled in a prescription drug plan under part D. (DD) Individuals described in subparagraph (X) who are not enrolled in such a plan. (EE) Individuals described in subparagraph (X) who are enrolled in an MA\u2013PD plan. (FF) Individuals described in subparagraph (X) who are not enrolled in such a plan. (GG) Individuals described in subparagraph (CC) or (EE) who are enrolled in a Federal health care program (as defined in section 1128B) or a health plan under chapter 89 of title 5, United States Code. (HH) Individuals described in subparagraph (CC) or (EE) who are not enrolled in such a program or plan. (II) Individuals enrolled in an employer group waiver plan. (2) Definitions For purposes of this subsection: (A) Specified historical period The term specified historical period means, with respect to a year, the 10-year period ending on the last day of such year. (B) Specified projected period The term specified projected period means, with respect to a year, the period beginning on the first day of the subsequent year of a duration specified by the Secretary (but in no case to exceed a duration of 5 years). .\n#### 3. MedPAC analysis of Medicare Advantage and fee-for-service expenditures\nSection 1805(b) of the Social Security Act ( 42 U.S.C. 1395b\u20136(b) ) is amended by adding at the end the following new paragraph:\n(12) Analysis of Medicare Advantage and fee-for-service expenditures (A) In general The Commission shall, as part of the report described in paragraph (1)(C) submitted for each year (beginning with 2027), include a retrospective analysis of average expenditures under this title for individuals enrolled in a Medicare Advantage plan under part C compared to average expenditures under this title for individuals entitled to benefits under part A and enrolled under part B who are eligible to enroll under such a plan but who are not so enrolled. (B) Considerations In preparing each analysis described in subparagraph (A), the Commission shall\u2014 (i) use data provided by the Chief Actuary of the Centers for Medicare & Medicaid Services and the Boards of Trustees of the Federal Hospital Insurance Trust Fund established under section 1817 and the Federal Supplementary Medical Insurance Trust fund established under section 1841 and such other data as the Commission determines appropriate; (ii) take into account\u2014 (I) differences in value provided under Medicare Advantage plans compared to the value provided under parts A and B, such as the existence of out-of-pocket expenditure caps, supplemental benefits available under such plans, and the integration of benefits for covered part D drugs under certain such plans; (II) demographic differences of individuals enrolled in Medicare Advantage plans compared to individuals entitled to benefits under part A and enrolled under part B who are not enrolled in such a plan; and (III) differences in HCC risk scores; and (iii) not take into account any favorable selection differences with respect to enrollment in such plans. (C) Publication requirements With respect to each analysis described in subparagraph (A), the Commission shall\u2014 (i) make public all data used in preparing such analysis in a manner that\u2014 (I) allows replication of such analysis; and (II) protects the confidentiality of personal information of individuals entitled to benefits under part A and enrolled under part B; (ii) not later than 60 days prior to the submission of such analysis, make public the methodology used to conduct such analysis and allow at least 30 days for public comment on such methodology; and (iii) make public a response to each such comment received on the methodology prior to or concurrent with the submission of such analysis. .\n#### 4. Trustees report of expenditure information\nSection 1874 of the Social Security Act ( 42 U.S.C. 1395kk ), as amended by section 2, is amended by adding at the end the following new subsection:\n(i) Trustees\u2019 report of expenditure information (1) In general The Boards of Trustees of the Federal Hospital Insurance Trust Fund established under section 1817 and the Federal Supplementary Medical Insurance Trust Fund established under section 1841 shall jointly, as part of the reports described in sections 1817(b)(2) and 1841(b)(2) submitted for a year (beginning with 2027), include information on aggregate and average expenditures under this title for the following categories of individuals and, in the case of the category described in subparagraph (C), broken down by expenditures under part A and expenditures under part B: (A) Individuals entitled to benefits under part A and not enrolled under part B. (B) Individuals enrolled under part B and not entitled to benefits under part A. (C) Individuals entitled to benefits under part A, enrolled under part B, and not enrolled in a Medicare Advantage plan under part C. (2) Provision of disaggregated information The Boards of Trustees described in paragraph (1) shall, as part of all expenditure data (including data tables) made public by such Boards, disaggregate such data, to the extent practicable, based on the categories of individuals described in paragraph (1). .",
      "versionDate": "2026-02-11",
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
        "actionDate": "2025-06-24",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4093",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Apples to Apples Comparison Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-03-02T19:34:55Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3848is.xml"
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
      "title": "Apples to Apples Comparison Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Apples to Apples Comparison Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T04:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to require the Secretary of Health and Human Services to publish information on expenditures under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T04:03:26Z"
    }
  ]
}
```
