# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5112
- Title: Tipped Worker Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 5112
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2026-01-09T05:06:18Z
- Update date including text: 2026-01-09T05:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5112",
    "number": "5112",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Tipped Worker Protection Act",
    "type": "HR",
    "updateDate": "2026-01-09T05:06:18Z",
    "updateDateIncludingText": "2026-01-09T05:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-03T14:01:25Z",
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
      "sponsorshipDate": "2025-09-03",
      "state": "NC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "AZ"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
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
      "sponsorshipDate": "2025-09-03",
      "state": "IN"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "PA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "OR"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "NV"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5112ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5112\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mrs. Hayes (for herself, Ms. Adams , Ms. Ansari , Ms. Bonamici , Mr. Carson , Mr. Jackson of Illinois , Ms. Lee of Pennsylvania , Mr. Lieu , Ms. Salinas , Mr. Thanedar , and Ms. Titus ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to repeal the separate minimum wage for tipped employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tipped Worker Protection Act .\n#### 2. Scheduled repeal of separate minimum wage for tipped employees\n##### (a) In general\n**(1) Repeal**\nSection 3(m)(2)(B) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ), as so redesignated by section 3(a) and as amended by section 3(b) of this Act, is amended by striking the sentence beginning with In determining the wage an employer is required to pay a tipped employee, and all that follows through of this subsection. and inserting The wage required to be paid to a tipped employee shall be the wage set forth in section 6(a)(1). .\n**(2) Conforming amendments**\n**(A) Retention of tips**\nSection 3(m)(2)(C) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(B) ), as so redesignated by section 3(a) and as amended by section 3(c) of this Act, is further amended in clause (i) of such section 3(m)(2)(C) by striking Regardless of whether or not an employer takes a tip credit, the employer and inserting An employer .\n**(B) Status as a tipped employee**\nSubsection (t) of section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ) is repealed.\n**(C) Penalties**\nSection 16 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216 ), as amended by this Act, is further amended\u2014\n**(i)**\nin subsection (b), by striking the sum of any tip credit taken by the employer and all such tips unlawfully kept by the employer and inserting the sum of all such tips unlawfully used or kept by the employer ; and\n**(ii)**\nin subsection (c), by striking the sum of any tip credit taken by the employer and all such tips unlawfully kept by the employer and inserting the sum of all such tips unlawfully used or kept by the employer .\n**(3) Delayed effective date**\n**(A) In general**\nExcept as provided in subparagraph (B), the amendments made by paragraphs (1) and (2) shall take effect with the beginning of the first 1-year period described in 3(m)(2)(A)(i) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A)(i) ), as amended by subsection (b), for which the hourly wage for such 1-year period would equal or exceed the minimum wage in effect under section 6(a)(1) as of the beginning of such 1-year period.\n**(B) Special rule for tip pools established or maintained during transition period**\nIn any case in which a system to pool tips is established for the non-supervisory employees of an employer in accordance with section 3(m)(2)(D) of such Act ( 29 U.S.C. 203(m)(2)(D) ) (as added by section 3(d) of this Act) prior to the beginning of the 1-year period described in subparagraph (A), the amendments made by paragraphs (1) and (2) shall apply with respect to such employer beginning with the date on which such system is established.\n##### (b) Minimum wage for tipped employees during transition period\n**(1) In general**\nClause (i) of section 3(m)(2)(B) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ), as so redesignated by section 3(a) of this Act, is amended to read as follows:\n(i) the cash wage paid such employee, which for purposes of such determination shall be not less than\u2014 (I) for the 1-year period beginning on the date of enactment of the Tipped Worker Protection Act , $3.60 an hour; (II) for each succeeding 1-year period, an hourly wage equal to the amount determined under this clause for the preceding 1-year period increased by $1.50 (but not to exceed the minimum wage in effect under section 6(a)(1) as of the beginning of such 1-year period); and .\n**(2) Definition of tipped employee**\nSection 3(t) of such Act ( 29 U.S.C. 203(t) ) is amended by striking he customarily and regularly receives more than $30 a month in tips and inserting the employee customarily and regularly receives for each month an amount in tips equal to (or in excess of) the difference between the total cash wages paid to the employee under subsection (m)(2)(A)(i) for such month and the total wages that would have been paid to the employee for the hours worked in such month pursuant to the minimum wage in effect under section 6(a)(1) but for subsection (m)(2), except that an employee shall not be considered a tipped employee for any workweek in which the employee spends more than 20 percent of the employee\u2019s hours of employment performing duties related to the employee\u2019s occupation for which the employee does not directly receive tips .\n#### 3. Requirements relating to retention and pooling of tips\n##### (a) Treatment of certain amounts as tips\nSection 3(m)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as subparagraphs (B) and (C), respectively; and\n**(2)**\nby inserting before subparagraph (A), as so redesignated, the following:\n(A) Tip includes any discretionary amount paid directly to an employee by a customer and any portion of a mandatory charge imposed on a customer by the employer which is added to the cost of the product or service in any manner that may reasonably lead the customer to believe that the amount collected by the employer from such charge will be paid in full directly to the employee. .\n##### (b) All tips retained by employees\nSubparagraph (B) of section 3(m)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2) ), as redesignated by subsection (a), is amended by striking of this subsection and all that follows through the end of the subparagraph and inserting of this subsection. Any employee shall have the right to retain, regardless of whether received as part of a system to pool tips established in accordance with subparagraph (C), any tips received by such employee. .\n##### (c) No tips retained by employers\nSubparagraph (C) of section 3(m)(2)(C) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2) ), as redesignated by subsection (b), is amended to read as follows:\n(C) (i) Regardless of whether or not an employer takes a tip credit, the employer may not keep tips received by its employees for any purpose or use such tips for any purpose other than to facilitate the distribution to employees of the full amount of all such tips under a system to pool tips established in accordance with subparagraph (D). (ii) A violation of clause (i) includes\u2014 (I) allowing managers or supervisors to keep or use any portion of employees\u2019 tips; and (II) keeping or using any portion of employees\u2019 tips to cover the cost of financial transaction fees, including any fee established, charged, or received by a payment card network for the purpose of compensating an issuer for its involvement in a transaction in which a person uses a debit card or credit card (as the terms \u201cdebit card\u201d, \u201ccredit card\u201d, \u201cissuer\u201d, and \u201cpayment card network\u201d are defined in section 921(c) of the Electronic Fund Transfer Act ( 15 U.S.C. 1693o\u20132(c) )) .\n##### (d) Tip pools\nSection 3(m)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2) ), as amended by this section, is further amended by adding at the end the following:\n(D) (i) In any case in which an employer is provided with written documentation demonstrating that not less than 30 percent of all of the non-supervisory employees of the employer request a vote on whether to establish or modify a system to pool tips in accordance with this subparagraph, such a system shall be considered to be so established or modified if the employer is provided with written documentation demonstrating that not less than 51 percent of all such employees vote in favor of establishing or modifying such a system. (ii) The employer shall maintain a written record of any vote to establish or modify a system to pool tips held pursuant to this subparagraph, including the name of each employee voting and the vote totals. The employer shall provide a copy of such record to any employee upon request. (iii) (I) A system to pool tips established under this subparagraph shall be administered by the employer, at the employer\u2019s expense, in a manner ensuring that\u2014 (aa) participation in the system is voluntary for each employee and determined without coercion from the employer; (bb) such tips are shared among all non-supervisory employees participating in such system; (cc) funds held in such system are maintained separately from any other funds; and (dd) the records of such system are available to be examined by each such participating employee. (II) In administering a system to pool tips established under this subparagraph, an employer may suggest reasonable and customary practices. (III) In any dispute among employees relating to the administration of a system to pool tips established under this subparagraph, the employer may mediate and impose a resolution of the dispute on the employees participating in the system only if\u2014 (aa) in the case of employees in a restaurant or similar retail food establishment, no agreement resolving the dispute can be reached among\u2014 (AA) 50 percent or more of the participating service employees whose primary job duties include direct interaction with customers; and (BB) 50 percent or more of all other participating employees; and (bb) in the case of employees in any other establishment, no agreement resolving the dispute can be reached among 50 percent or more of the participating employees. (iv) An employer shall not be required to compensate any employee participating in a system to pool tips established under this subparagraph in any case arising as a result of another participating employee withholding tips from such system. (v) An employer shall not discharge an employee or otherwise discriminate against an employee based on the employee\u2019s vote with respect to, or participation in, a system to pool tips established under this subparagraph. (vi) In this subparagraph, the term non-supervisory employee means any employee who has, at any point in their typical duties, decision making authority over the scheduling of other employees, the hiring of other employees, or the termination of other employees. .\n##### (e) Service charges\nSection 3(m)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2) ), as amended by this section, is further amended by adding at the end the following:\n(E) (i) In any case in which an employer imposes a mandatory charge on a customer which is added to the cost of the product or service, the employer shall\u2014 (I) disclose to the customer and to all employees involved in the sale of such product or delivery of such service\u2014 (aa) the reason for such charge; and (bb) the portion of such charge, if any, which upon its collection will be paid in full by the employer directly to employees; and (II) promptly pay to employees upon collection of such charge any portion identified in the disclosure required under subclause (I)(bb). (ii) In any case in which an employer represents that a charge is payable at the discretion of the customer, the employer may not add such charge to the cost of any product or service unless first requested by the customer. .\n##### (f) Penalties\nSection 16(e)(2) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(e)(2) ) is amended\u2014\n**(1)**\nby striking section 3(m)(2)(B) and inserting any provision of section 3(m)(2) ; and\n**(2)**\nby inserting or used after kept .\n##### (g) Effective date\nThe amendments made by this section shall take effect on the date of enactment of this Act and shall apply with respect to all tips received on or after such date.\n#### 4. Service charges treated as tips for purposes of employer credit for social security taxes, etc\n##### (a) In general\nSection 3121(q) of the Internal Revenue Code of 1986 is amended by adding at the end the following: In the case of any mandatory charge to which section 3(m)(2)(E) of the Fair Labor Standards Act applies, the portion of such charge described in subclause (I)(bb) of such section shall be treated as tips for purposes of this subsection. .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts received on or after the date of the enactment of this Act.",
      "versionDate": "2025-09-03",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-22T15:39:09Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5112ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to repeal the separate minimum wage for tipped employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:17Z"
    },
    {
      "title": "Tipped Worker Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tipped Worker Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:23:21Z"
    }
  ]
}
```
