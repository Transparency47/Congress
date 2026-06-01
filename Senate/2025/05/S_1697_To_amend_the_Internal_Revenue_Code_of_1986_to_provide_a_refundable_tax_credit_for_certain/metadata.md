# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1697?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1697
- Title: RAISE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1697
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-01-26T20:08:37Z
- Update date including text: 2026-01-26T20:08:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1697",
    "number": "1697",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "RAISE Act of 2025",
    "type": "S",
    "updateDate": "2026-01-26T20:08:37Z",
    "updateDateIncludingText": "2026-01-26T20:08:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T19:18:10Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MD"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NV"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1697is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1697\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Booker (for himself, Mr. Padilla , Mr. Blumenthal , Mr. Van Hollen , Ms. Rosen , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a refundable tax credit for certain teachers as a supplement to State efforts to provide teachers with a livable wage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Respect, Advancement, and Increasing Support for Educators Act of 2025 or the RAISE Act of 2025 .\n#### 2. Refundable teacher tax credit\n##### (a) Allowance of tax credit\n**(1) In general**\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Teacher tax credit (a) Credit allowed In the case of an individual who is an eligible educator during school years ending with or within the taxable year, there shall be allowed as a credit against the tax imposed by this chapter an amount equal to the sum of\u2014 (1) $1,000, plus (2) in the case of an eligible educator who is employed at a qualifying school, the applicable amount. (b) Applicable amount For purposes of subsection (a), the applicable amount is the amount which bears the same ratio (not to exceed one) to $14,000 ($9,000, in the case of any early childhood educator without a bachelor's degree) as\u2014 (1) the number of percentage points by which the student poverty ratio for such qualifying school exceeds 39 percent, bears to (2) 36 percentage points. (c) Eligible educator For purposes of this section\u2014 (1) In general The term eligible educator means\u2014 (A) any elementary or secondary teacher, and (B) any early childhood educator. (2) Elementary or secondary teacher (A) In general The term elementary or secondary teacher means an individual who\u2014 (i) is a teacher of record who provides direct classroom teaching (or classroom-type teaching in a nonclassroom setting) in a public elementary school or a public secondary school for not less than 75 percent of the normal or statutory number of hours of work for a full-time teacher over a complete school year (as determined by the State in which the school is located), (ii) meets the applicable requirements for State certification and licensure in the State in which such school is located in the subject area in which the individual is the teacher of record, and (iii) has met the requirements of clauses (i) and (ii) for a period of not less than 1 year before the first day of the taxable year. (B) Teacher of record For purposes of subparagraph (A), the term teacher of record means a teacher who has been assigned the responsibility for specified pupils\u2019 learning in a grade, subject, or course as reflected on the school\u2019s official record of attendance. (3) Early childhood educator The term early childhood educator means an individual who\u2014 (A) has a Child Development Associate credential (or an equivalent credential), or has an associate's degree or higher, (B) meets the applicable requirements for State certification, licensure, or permitting under State law for early childhood education, (C) has primary responsibility for the learning and development of children in an early childhood education program (as defined in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 )) for not less than 75 percent of the normal or statutory number of hours of work for a full-time teacher over a complete program year, as determined by the Secretary of Health and Human Services, and (D) has met the requirements of subparagraphs (A), (B), and (C) for a period of not less than 1 year before the first day of the taxable year. (d) Qualifying school (1) In general The term qualifying school means, with respect to any school year\u2014 (A) a public elementary school or a public secondary school that\u2014 (i) is served by a local educational agency that is eligible in such year for assistance pursuant to part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ), or (ii) is served by an educational service agency, or a location operated by an educational service agency, that is eligible, for the year in which the determination is made, for assistance under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ), (B) an elementary school or secondary school that is funded by the Bureau of Indian Education, or (C) an early childhood education program (as defined in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 )) that serves children who receive, or are eligible for, services for which financial assistance is provided in accordance with the Child Care and Development Block Grant of 1990 ( 42 U.S.C. 9857 et seq. ) or the child and adult care food program established under section 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 ). (2) ESEA definitions For purposes of this subsection, the terms educational service agency , elementary school , local educational agency , secondary school , and State educational agency have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (e) Student poverty ratio (1) In general The term student poverty ratio means\u2014 (A) with respect to any qualifying school described in subparagraph (A) or (B) of subsection (d)(1), the ratio (expressed as a percentage) of\u2014 (i) the total number of children served at such qualifying school meeting at least one measure of poverty described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) ), to (ii) the total number of children served at such qualifying school, and (B) with respect to any qualifying school described in subsection (d)(1)(C), the ratio (expressed as a percentage) of\u2014 (i) the total number of children attending such qualifying school who are eligible for services under the Child Care and Development Block Grant of 1990 ( 42 U.S.C. 9857 et seq. ) or for the child and adult care food program established under section 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 ), to (ii) the total number of children attending such qualifying school. (2) Determination of ratio In determining the student poverty ratio with respect to a qualifying school under paragraph (1)(A), the Secretary shall use the same measure of poverty as is used for purposes of determining the allocation of funds under part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ) with respect to the qualifying school. (f) Inflation adjustment (1) In general In the case of any taxable year beginning after 2026, each of the dollar amounts in subsections (a) and (b) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting in subparagraph (A)(ii) thereof calendar year 2025 for calendar year 2016 . (2) Rounding If any increase determined under paragraph (1) is not a multiple of $50, such increase shall be rounded to the nearest multiple of $50. .\n**(2) Conforming amendments**\n**(A)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Teacher tax credit. .\n**(B)**\nSection 6211(b)(4)(A) of such Code is amended by inserting 36C, after 36B, .\n**(C)**\nSection 1324(b)(2) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n##### (b) Information sharing\n**(1) In General**\nThe Secretary of Education shall\u2014\n**(A)**\ncollect such information as necessary for purposes of determining whether a school is a qualifying school (as defined in section 36C of the Internal Revenue Code of 1986, as added by subsection (a)) and the appropriate amount of tax credit under such section; and\n**(B)**\nprovide such information to the Secretary of the Treasury (or the Secretary's delegate).\n**(2) Information for the Secretary of Education**\nAs a condition of receiving Federal funds and if requested by the Secretary of Education, each qualifying school shall collect and submit to the Secretary of Education such information as may be necessary to enable the Secretary of Education to carry out paragraph (1).\n##### (c) Supplementation of funds\n**(1) Elementary and Secondary Education**\nA State educational agency or local educational agency (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )) shall not reduce or adjust any teacher pay or teacher loan forgiveness program due to the eligibility of teachers within the jurisdiction of such agency for the tax credit under section 36C of the Internal Revenue Code of 1986. Each State educational agency and local educational agency (as so defined), upon request by the Secretary of the Treasury, shall demonstrate that the methodology used to allocate teacher pay and teacher loan forgiveness (if applicable) to qualifying schools (as defined in section 36C(d) of such Code) ensures that each such school receives the same State and local funds for teacher compensation it would receive if the credit under such section 36C had not been enacted.\n**(2) Early childhood education**\nAn agency or other entity that funds, licenses, or regulates an early childhood education program (as defined in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 )) shall not reduce or adjust any teacher pay or teacher loan forgiveness program, or permit such a reduction or adjustment in the early childhood education program, due to the eligibility of teachers within the jurisdiction of such agency for the tax credit under section 36C of the Internal Revenue Code of 1986. Each such agency or entity, upon request by the Secretary of the Treasury, shall demonstrate that the methodology used to allocate teacher pay and teacher loan forgiveness (if applicable) to such early childhood education programs ensures that each such program receives the same State and local funds for teacher compensation it would receive if the credit under such section 36C had not been enacted.\n##### (d) Employer limitations\n**(1) Prohibition of use in collective bargaining**\nAn employer that engages in collective bargaining with employees who are eligible educators, as defined in section 36C(c) of the Internal Revenue Code of 1986, shall not include the amount of the teacher tax credit under section 36C of such Code in determining the amount of salary or other compensation provided to any employee under the collective bargaining agreement.\n**(2) Prohibition of use as punishment or retribution**\nAn employer of an eligible educator, as defined in section 36C of the Internal Revenue Code of 1986, shall not change the work assignment or location of the eligible educator if one of the primary reasons for the change is to\u2014\n**(A)**\nprevent the eligible educator from receiving a teacher tax credit under section 36C of such Code; or\n**(B)**\nreduce the amount of the teacher tax credit that the eligible educator will receive.\n**(3) Enforcement**\nNotwithstanding any other provision of law, the Federal Labor Relations Authority shall have the authority to investigate and enforce any alleged violation of this section in the same manner, and subject to the same procedures, as would apply to an allegation of an unfair labor practice under section 7118 of title 5, United States Code.\n**(4) Definition**\nIn this subsection\u2014\n**(A)**\nthe term affecting commerce has the meaning given the term in section 2 of the National Labor Relations Act ( 29 U.S.C. 152 );\n**(B)**\nthe term employee means an employee of an employer who is employed in a business of an employer that affects commerce; and\n**(C)**\nthe term employer means a person, including a State or political subdivision of a State, engaged in a business affecting commerce.\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 3. Increase in and expansion of deduction for expenses of elementary and secondary school teachers\n##### (a) Increase\n**(1) In general**\nSubparagraph (D) of section 62(a)(2) of the Internal Revenue Code of 1986 is amended by striking $250 and inserting $500 .\n**(2) Inflation adjustment**\nSection 62(d)(3) of such Code is amended\u2014\n**(A)**\nby striking 2015 and inserting 2026 ;\n**(B)**\nby striking the $250 amount and inserting each of the dollar amounts ; and\n**(C)**\nby striking 2014 in subparagraph (B) thereof and inserting 2025 .\n##### (b) Expansion to early childhood educators\nSection 62(d)(1)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking who is a kindergarten and inserting\nwho is\u2014 (i) a kindergarten ;\n**(2)**\nby striking the period at the end and inserting , or ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(ii) an early childhood educator (as defined in section 200 of the Higher Education Act of 1965 ( 20 U.S.C. 1021 )) in an early childhood education program (as defined in section 103 of such Act ( 20 U.S.C. 1003 )) for at least 1,020 hours during a year. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after the date of the enactment of this Act.\n#### 4. Mandatory funding to support local educational agencies that maintain or increase teacher salaries\nSection 2003 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6603 ) is amended\u2014\n**(1)**\nin the section heading, by striking Authorization of appropriations and inserting Funding ; and\n**(2)**\nby striking subsection (a) and inserting the following:\n(a) Appropriations for part A (1) In general There are authorized to be appropriated, and there are appropriated, out of any funds not otherwise appropriated\u2014 (A) for fiscal year 2026, $5,200,000,000 to carry out part A; and (B) for fiscal year 2027 and each succeeding fiscal year, the amount appropriated under this paragraph for the preceding year, increased by a percentage equal to the annual percentage increase in the Consumer Price Index for All Urban Consumers published by the Department of Labor for the most recent calendar year. (2) Reservation for teacher salary incentive grants (A) Definitions In this paragraph: (i) Eligible local educational agency The term eligible local educational agency means a local educational agency that, for the preceding school year, maintained or increased the salary schedule for all teachers employed by the local educational agency. (ii) Teacher salary incentive reservation The term teacher salary incentive reservation means, for each fiscal year, the amount that is 20 percent of the amount by which the funds appropriated under paragraph (1) for the fiscal year exceeds $2,200,000,000. (B) In general For each fiscal year for which the total amount appropriated under paragraph (1) is greater than $2,200,000,000, the Secretary shall, after making any reservations under section 2101(a), reserve and use the teacher salary incentive reservation to award grants, based on allotments under subparagraph (C), to eligible local educational agencies for purposes described in subparagraph (E). (C) Allotments An allotment under this subparagraph for a fiscal year to an eligible local educational agency shall bear the same relationship to the teacher salary incentive reservation as the number of children counted under section 1124(c) who are served by the local educational agency bears to the total number of such children counted under such section served by all eligible local educational agencies that submitted an application under subparagraph (D). (D) Application An eligible local educational agency desiring an allotment under this paragraph shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (E) Use of funds A local educational agency receiving an allotment under subparagraph (C) may use the allotment to carry out one or more of the following: (i) Comprehensive teacher or school leader preparation programs described subsection (d), (e), or (f) of section 202 of the Higher Education Act of 1965. (ii) Support for teachers to earn certifications or credentials in high-need fields or advanced credentials, such as certification or credentialing by the National Board for Professional Teaching Standards. (iii) Teacher leadership programs. (iv) Induction or mentoring programs for new teachers, principals, or other school leaders. (v) High-quality research-based professional development. (vi) Other activities approved by the Secretary that\u2014 (I) promote and strengthen the teaching profession; (II) attract, retain, and diversify the educator workforce; or (III) advance the skills and efficacy of the educator workforce. (F) Supplement, not supplant A local educational agency receiving an allotment under subparagraph (C) shall use the allotment to supplement, and not supplant, any State funds or efforts to raise teacher pay. .",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-02-26",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1611",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RAISE Act of 2025",
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
        "updateDate": "2025-06-06T18:25:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-08",
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
          "measure-id": "id119s1697",
          "measure-number": "1697",
          "measure-type": "s",
          "orig-publish-date": "2025-05-08",
          "originChamber": "SENATE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1697v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-05-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Respect, Advancement, and Increasing Support for Educators Act of 2025 or the RAISE Act of </strong><strong>2025</strong></p><p>This bill establishes a refundable federal tax credit for eligible educators and increases and expands the federal tax deduction for certain classroom and professional development expenses. The bill also increases federal funding for programs that support effective instruction.</p><p>Specifically, the bill allows (1) eligible educators (elementary and secondary public school teachers and early childhood educators) to claim a tax credit of $1,000,\u00a0and (2)\u00a0eligible educators employed at a qualifying school to claim an additional tax credit of up to $14,000 ($9,000 for an early childhood educator without a bachelor\u2019s degree) based on the qualifying school\u2019s student poverty ratio.</p><p>The bill generally defines a <em>qualifying school</em> as</p><ul><li>a public elementary or secondary school served by a local education agency eligible for federal grants that support the education of disadvantaged children,</li><li>an elementary school or secondary school funded by the Bureau of Indian Education, or</li><li>an early childhood education program serving children who are eligible for certain financial or food assistance.</li></ul><p>Further, the bill increases to $500 ($300 in 2025) and continues to adjust annually the above-the-line tax deduction for certain classroom and professional development expenses of educators. The bill also expands eligibility for the credit to include early childhood educators. (Above-the-line tax deductions are subtracted from gross income to calculate adjusted gross income.)</p><p>Finally, the bill provides additional funding for\u00a0education programs, including teacher\u00a0salary incentive grants and\u00a0professional development, certificate, and credentialing programs.</p>"
        },
        "title": "RAISE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1697.xml",
    "summary": {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Respect, Advancement, and Increasing Support for Educators Act of 2025 or the RAISE Act of </strong><strong>2025</strong></p><p>This bill establishes a refundable federal tax credit for eligible educators and increases and expands the federal tax deduction for certain classroom and professional development expenses. The bill also increases federal funding for programs that support effective instruction.</p><p>Specifically, the bill allows (1) eligible educators (elementary and secondary public school teachers and early childhood educators) to claim a tax credit of $1,000,\u00a0and (2)\u00a0eligible educators employed at a qualifying school to claim an additional tax credit of up to $14,000 ($9,000 for an early childhood educator without a bachelor\u2019s degree) based on the qualifying school\u2019s student poverty ratio.</p><p>The bill generally defines a <em>qualifying school</em> as</p><ul><li>a public elementary or secondary school served by a local education agency eligible for federal grants that support the education of disadvantaged children,</li><li>an elementary school or secondary school funded by the Bureau of Indian Education, or</li><li>an early childhood education program serving children who are eligible for certain financial or food assistance.</li></ul><p>Further, the bill increases to $500 ($300 in 2025) and continues to adjust annually the above-the-line tax deduction for certain classroom and professional development expenses of educators. The bill also expands eligibility for the credit to include early childhood educators. (Above-the-line tax deductions are subtracted from gross income to calculate adjusted gross income.)</p><p>Finally, the bill provides additional funding for\u00a0education programs, including teacher\u00a0salary incentive grants and\u00a0professional development, certificate, and credentialing programs.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s1697"
    },
    "title": "RAISE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Respect, Advancement, and Increasing Support for Educators Act of 2025 or the RAISE Act of </strong><strong>2025</strong></p><p>This bill establishes a refundable federal tax credit for eligible educators and increases and expands the federal tax deduction for certain classroom and professional development expenses. The bill also increases federal funding for programs that support effective instruction.</p><p>Specifically, the bill allows (1) eligible educators (elementary and secondary public school teachers and early childhood educators) to claim a tax credit of $1,000,\u00a0and (2)\u00a0eligible educators employed at a qualifying school to claim an additional tax credit of up to $14,000 ($9,000 for an early childhood educator without a bachelor\u2019s degree) based on the qualifying school\u2019s student poverty ratio.</p><p>The bill generally defines a <em>qualifying school</em> as</p><ul><li>a public elementary or secondary school served by a local education agency eligible for federal grants that support the education of disadvantaged children,</li><li>an elementary school or secondary school funded by the Bureau of Indian Education, or</li><li>an early childhood education program serving children who are eligible for certain financial or food assistance.</li></ul><p>Further, the bill increases to $500 ($300 in 2025) and continues to adjust annually the above-the-line tax deduction for certain classroom and professional development expenses of educators. The bill also expands eligibility for the credit to include early childhood educators. (Above-the-line tax deductions are subtracted from gross income to calculate adjusted gross income.)</p><p>Finally, the bill provides additional funding for\u00a0education programs, including teacher\u00a0salary incentive grants and\u00a0professional development, certificate, and credentialing programs.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s1697"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1697is.xml"
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
      "title": "RAISE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RAISE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Respect, Advancement, and Increasing Support for Educators Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a refundable tax credit for certain teachers as a supplement to State efforts to provide teachers with a livable wage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:27Z"
    }
  ]
}
```
