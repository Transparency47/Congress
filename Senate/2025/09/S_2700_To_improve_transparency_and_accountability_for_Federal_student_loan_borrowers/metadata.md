# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2700
- Title: DECIDE Act
- Congress: 119
- Bill type: S
- Bill number: 2700
- Origin chamber: Senate
- Introduced date: 2025-09-03
- Update date: 2025-09-22T14:48:47Z
- Update date including text: 2025-09-22T14:48:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in Senate
- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-09-03: Introduced in Senate

## Actions

- 2025-09-03 - IntroReferral: Introduced in Senate
- 2025-09-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2700",
    "number": "2700",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "DECIDE Act",
    "type": "S",
    "updateDate": "2025-09-22T14:48:47Z",
    "updateDateIncludingText": "2025-09-22T14:48:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T20:15:31Z",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2700is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2700\nIN THE SENATE OF THE UNITED STATES\nSeptember 3, 2025 Mr. Husted (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve transparency and accountability for Federal student loan borrowers.\n#### 1. Short title\nThis Act may be cited as the Debt, Earnings, and Cost Information Disclosure for Education Act or the DECIDE Act .\n#### 2. Improving transparency and accountability for student loan borrowers\n##### (a) Program-Level data\nThe Secretary of Education shall expand and update annually the College Scorecard, or any successor, with the following program-level data for each certificate, degree, graduate, and professional program for which students are eligible to receive Federal student aid:\n**(1)**\nThe median annual earnings of the programmatic cohort of students who received Federal funds (including Federal Pell Grants or student loans under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. )) for enrollment in such program during the academic year that is 10 years before the year of the determination, regardless of completion status.\n**(2)**\nThe median amount of Federal Direct Stafford Loan debt, as determined by the Secretary of Education, that borrowers of such loans who completed the program had at the time they entered repayment on such Federal Direct Stafford Loans.\n**(3)**\nIn the case of a graduate or professional program, the median amount of Graduate Federal Direct PLUS loan debt, as determined by the Secretary of Education, that borrowers of such loans who completed the program had at the time they entered repayment on such Graduate PLUS loans.\n**(4)**\nThe median amount of Parent Federal Direct PLUS loan debt, as determined by the Secretary of Education, for students who completed the program and on whose behalf a parent borrowed such Parent PLUS loans.\n**(5)**\nThe default rate of students who completed the program, as determined by the Secretary of Education.\n**(6)**\nThe repayment rate.\n##### (b) Institution-Level data\nThe Secretary of Education shall expand and update annually the College Scorecard, or any successor, with the following institution-level data:\n**(1)**\nThe cohort default rate.\n**(2)**\nThe repayment rate.\n**(3)**\nThe rate of default on Graduate Federal Direct PLUS loans, as determined by the Secretary of Education, and the repayment rate of such loans for students who received such loans for attendance at the institution.\n**(4)**\nThe rate of default on Parent Federal Direct PLUS loans, as determined by the Secretary of Education, and the repayment rate of such loans for students on whose behalf a parent borrowed such loans for the student\u2019s attendance at the institution.\n##### (c) Definitions\nIn this Act:\n**(1) Cohort default rate**\nThe term cohort default rate has the meaning given the term in section 435(m) of the Higher Education Act of 1965 ( 20 U.S.C. 1085(m) ).\n**(2) Repayment rate**\n**(A) In general**\nThe term repayment rate means the share of borrowers that graduated with Federal student loans in repayment that belong to a status category described in subparagraph (B), 2 years after entering repayment.\n**(B) Status categories**\nThe status categories shall be determined by the Secretary of Education and may include the categories: making progress, not making progress, deferment, paid in full, forbearance, defaulted, delinquent, and discharged.\n**(C) Exclusions**\nThe repayment rate shall exclude private student loans and Federal loans originated at a different institution.",
      "versionDate": "2025-09-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-09-22T14:48:47Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2700is.xml"
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
      "title": "DECIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DECIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Debt, Earnings, and Cost Information Disclosure for Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve transparency and accountability for Federal student loan borrowers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:25Z"
    }
  ]
}
```
