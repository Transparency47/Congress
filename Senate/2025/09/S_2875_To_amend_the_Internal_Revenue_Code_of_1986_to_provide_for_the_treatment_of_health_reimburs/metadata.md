# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2875
- Title: CHOICE Act
- Congress: 119
- Bill type: S
- Bill number: 2875
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-01-10T07:01:28Z
- Update date including text: 2026-01-10T07:01:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2875",
    "number": "2875",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "CHOICE Act",
    "type": "S",
    "updateDate": "2026-01-10T07:01:28Z",
    "updateDateIncludingText": "2026-01-10T07:01:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T18:58:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "TN"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "IN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2875is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2875\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Sheehy introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for the treatment of health reimbursement arrangements integrated with individual market coverage.\n#### 1. Short title\nThis Act may be cited as the Custom Health Option and Individual Care Expense Act or the CHOICE Act .\n#### 2. Treatment of health reimbursement arrangements integrated with individual market coverage\n##### (a) In general\nSection 9815(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking Exception.\u2014 Notwithstanding subsection (a) and inserting the following:\nExceptions.\u2014 (1) Self-insured group health plans Notwithstanding subsection (a) , and\n**(2)**\nby adding at the end the following new paragraph:\n(2) Custom health option and individual care expense arrangements (A) In general For purposes of this subchapter, a custom health option and individual care expense arrangement shall be treated as meeting the requirements of section 9802 and sections 2705, 2711, 2713, and 2715 of title XXVII of the Public Health Service Act. (B) Custom health option and individual care expense arrangements defined For purposes of this section, the term custom health option and individual care expense arrangement means a health reimbursement arrangement\u2014 (i) which is an employer-provided group health plan funded solely by employer contributions to provide payments or reimbursements for medical care subject to a maximum fixed dollar amount for a period, (ii) under which such payments or reimbursements may only be made for medical care provided during periods during which the individual is covered\u2014 (I) under individual health insurance coverage (other than coverage that consists solely of excepted benefits), or (II) under part A and B of title XVIII of the Social Security Act or part C of such title, (iii) which meets the nondiscrimination requirements of subparagraph (C), (iv) which meets the substantiation requirements of subparagraph (D), and (v) which meets the notice requirements of subparagraph (E). (C) Nondiscrimination (i) In general An arrangement meets the requirements of this subparagraph if an employer offering such arrangement to an employee within a specified class of employee\u2014 (I) offers such arrangement to all employees within such specified class on the same terms, and (II) does not offer any other group health plan (other than an account-based group health plan or a group health plan that consists solely of excepted benefits) to any employees within such specified class. In the case of an employer who offers a group health plan provided through health insurance coverage in the small group market (that is subject to section 2701 of the Public Health Service Act) to all employees within such specified class, subclause (II) shall not apply to such group health plan. (ii) Specified class of employee For purposes of this subparagraph, any of the following may be designated as a specified class of employee: (I) Full-time employees. (II) Part-time employees. (III) Salaried employees. (IV) Non-salaried employees. (V) Employees whose home location is in the same rating area. (VI) Employees who are included in a unit of employees covered under a collective bargaining agreement to which the employer is subject (determined under rules similar to the rules of section 105(h)). (VII) Employees who have not met a group health plan, or health insurance issuer offering group health insurance coverage, waiting period requirement that satisfies section 2708 of the Public Health Service Act. (VIII) Seasonal employees. (IX) Employees who are nonresident aliens and who receive no earned income (within the meaning of section 911(d)(2)) from the employer which constitutes income from sources within the United States (within the meaning of section 861(a)(3)). (X) Under such rules as the Secretary may prescribe, employees who are hired for temporary placement with an unrelated person that is not the common law employer. (XI) Employees who are hired in the same date range. (XII) Such other classes of employees as the Secretary may designate. An employer may designate (in such manner as is prescribed by the Secretary) two or more of the classes described in the preceding subclauses as the specified class of employees to which the arrangement is offered for purposes of applying this subparagraph. (iii) Special rule for new hires An employer may designate prospectively so much of a specified class of employees as are hired after a date set by the employer. Such subclass of employees shall be treated as the specified class for purposes of applying clause (i). (iv) Rules for determining type of employee For purposes for clause (ii), any determination of full-time, part-time, or seasonal employment status shall be made under rules similar to the rules of section 105(h) or 4980H, whichever the employer elects for the plan year. Such election shall apply with respect to all employees of the employer for the plan year. (v) Permitted variation For purposes of clause (i)(I), an arrangement shall not fail to be treated as provided on the same terms within a specified class merely because the maximum dollar amount of payments and reimbursements which may be made under the terms of the arrangement for the year with respect to each employee within such class\u2014 (I) increases as additional dependents of the employee are covered under the arrangement, and (II) increases with respect to a participant as the age of the participant increases, but not in excess of an amount equal to 300 percent of the lowest maximum dollar amount with respect to such a participant determined without regard to age. (D) Substantiation requirements An arrangement meets the requirements of this subparagraph if the arrangement has reasonable procedures to substantiate\u2014 (i) that the participant and any dependents are, or will be, enrolled in coverage described in subparagraph (B)(ii) as of the beginning of the plan year of the arrangement (or as of the beginning of coverage under the arrangement in the case of an employee who first becomes eligible to participate in the arrangement after the date notice is given with respect to the plan under subparagraph (E) (determined without regard to clause (iii) thereof)), and (ii) any requests made for payment or reimbursement of medical care under the arrangement and that the participant and any dependents remain so enrolled. (E) Notice (i) In general Except as provided in clause (iii), an arrangement meets the requirements of this subparagraph if, under the arrangement, each employee eligible to participate is, not later than 60 days before the beginning of the plan year, given written notice of the employee\u2019s rights and obligations under the arrangement which\u2014 (I) is sufficiently accurate and comprehensive to apprise the employee of such rights and obligations, and (II) is written in a manner calculated to be understood by the average employee eligible to participate. (ii) Notice requirements Such notice shall include such information as the Secretary may by regulation prescribe. (iii) Notice deadline for certain employees In the case of an employee\u2014 (I) who first becomes eligible to participate in the arrangement after the date notice is given with respect to the plan under clause (i) (determined without regard to this clause), or (II) whose employer is first established fewer than 120 days before the beginning of the first plan year of the arrangement, the requirements of this subparagraph shall be treated as met if the notice required under clause (i) is provided not later than the date the arrangement may take effect with respect to such employee. .\n##### (b) Inclusion of CHOICE arrangement permitted benefits on W\u20132\n**(1) In general**\nSection 6051(a) of such Code is amended by striking and at the end of paragraph (18), by striking the period at the end of paragraph (19) and inserting , and , and by inserting after paragraph (19) the following new paragraph:\n(20) the total amount of permitted benefits for enrolled individuals under a custom health option and individual care expense arrangement (as defined in section 9815(b)(2)) with respect to such employee. .\n##### (c) Treatment of current rules relating to certain arrangements\n**(1) No inference**\nTo the extent not inconsistent with the amendments made by this section\u2014\n**(A)**\nno inference shall be made from such amendments with respect to the rules prescribed in the Federal Register on June 20, 2019, (84 Fed. Reg. 28888) relating to health reimbursement arrangements and other account-based group health plans, and\n**(B)**\nany reference to custom health option and individual care expense arrangements shall for purposes of such rules be treated as including a reference to individual coverage health reimbursement arrangements.\n**(2) Other conforming of rules**\nThe Secretary of the Treasury, the Secretary of Health and Human Services, and the Secretary of Labor shall modify such rules as may be necessary to conform to the amendments made by this section.\n##### (d) Effective date\nThe amendments made by this section shall apply to plan years beginning after December 31, 2025.\n#### 3. Participants in CHOICE arrangement eligible for purchase of Exchange insurance under cafeteria plan\n##### (a) In general\nSection 125(f)(3) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Exception for participants in CHOICE arrangement Subparagraph (A) shall not apply in the case of an employee participating in an custom health option and individual care expense arrangement (within the meaning of section 9815(b)(2)) offered by the employee\u2019s employer. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 4. Employer credit for CHOICE arrangement\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Employer credit for CHOICE arrangement (a) In general For purposes of section 38, in the case of an eligible employer, the CHOICE arrangement credit determined under this section for any taxable year is an amount, with respect to each employee enrolled during the credit period in a CHOICE arrangement maintained by the employer, equal to\u2014 (1) $100 multiplied by the number of months for which the employee is so enrolled during the first year in the credit period, and (2) one-half of the dollar amount in effect under paragraph (1) for the taxable year, multiplied by the number of months for which the employee is so enrolled during the second year of the credit period. (b) Arrangement must constitute minimum essential coverage An employee shall not be taken into account under subsection (a) unless such employee\u2019s eligibility for the CHOICE arrangement (determined without regard to the employee being enrolled) would cause the employee to be treated under section 36B(c)(2) as being eligible for minimum essential coverage consisting of an eligible employer-sponsored plan (as defined in section 5000A(f)(2)). (c) Definitions For purposes of this section\u2014 (1) CHOICE arrangement The term CHOICE arrangement means a custom health option and individual care expense arrangement (as defined in section 9815(b)(2)(B)). (2) Credit period The credit period with respect to an eligible employer is the first 2 one-year periods beginning with the month during which the employer first establishes a CHOICE arrangement on behalf of employees of the employer. (3) Eligible employer The term eligible employer means, with respect to any taxable year beginning in a calendar year, an employer who is not an applicable large employer for the calendar year under section 4980H. (d) Inflation adjustment (1) In general In the case of any taxable year beginning in a calendar year after 2026, the dollar amount in subsection (a) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding If any amount after adjustment under paragraph (1) is not a multiple of $10, such amount shall be rounded to the next lower multiple of $10. .\n##### (b) Credit made part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the CHOICE arrangement credit determined under section 45BB(a). .\n##### (c) Credit allowed against alternative minimum tax\nSection 38(c)(4)(B) of such Code is amended\u2014\n**(1)**\nby redesignating clauses (x), (xi), and (xii) as clauses (xi), (xii), and (xiii), respectively, and\n**(2)**\nby inserting after clause (ix) the following new clause:\n(x) the credit determined under section 45BB, .\n##### (d) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Employer credit for CHOICE arrangement. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5463",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Choice Arrangement",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "name": "Taxation",
        "updateDate": "2025-11-21T15:59:08Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2875is.xml"
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
      "title": "CHOICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CHOICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Custom Health Option and Individual Care Expense Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide for the treatment of health reimbursement arrangements integrated with individual market coverage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-09T04:48:15Z"
    }
  ]
}
```
