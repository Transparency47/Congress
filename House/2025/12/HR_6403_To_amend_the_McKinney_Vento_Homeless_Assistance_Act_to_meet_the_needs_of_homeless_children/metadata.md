# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6403
- Title: Homeless Children and Youth Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6403
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-04-30T08:07:02Z
- Update date including text: 2026-04-30T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6403",
    "number": "6403",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Homeless Children and Youth Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-30T08:07:02Z",
    "updateDateIncludingText": "2026-04-30T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-03T15:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
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
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6403ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6403\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Lawler (for himself, Ms. Bynum , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the McKinney-Vento Homeless Assistance Act to meet the needs of homeless children, youth, and families, and honor the assessments and priorities of local communities.\n#### 1. Short title\nThis Act may be cited as the Homeless Children and Youth Act of 2025 .\n#### 2. Amendments to the McKinney-Vento Homeless Assistance Act\n##### (a) In general\nThe McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11301 et seq. ) is amended\u2014\n**(1)**\nin section 103 ( 42 U.S.C. 11302 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (5)(A)\u2014\n**(I)**\nby striking are sharing and all that follows through charitable organizations, ;\n**(II)**\nby striking 14 days each place that term appears and inserting 30 days ;\n**(III)**\nin clause (i), by inserting or after the semicolon;\n**(IV)**\nby striking clause (ii); and\n**(V)**\nby redesignating clause (iii) as clause (ii); and\n**(ii)**\nby amending paragraph (6) to read as follows:\n(6) a child or youth defined as homeless under any other Federal program who, without further action by the Department of Housing and Urban Development, has been verified as homeless under any other Federal program by the director, designee of the director, or other person responsible for the implementation of a program established under this Act or any other Federal statute. ;\n**(B)**\nin subsection (b), by striking fleeing and all that follows through the period at the end and inserting the following: experiencing or has experienced domestic violence, dating violence, sexual assault, stalking, or human trafficking, or other dangerous or life threatening conditions, which has made it unsafe to remain in their current housing or caused homelessness. ; and\n**(C)**\nby adding at the end the following:\n(f) Other definitions In this section\u2014 (1) the term child or youth defined as homeless under any other Federal program has the meaning given the term in section 401; and (2) the term other Federal statute has the meaning given the term in section 401. (g) Rule of construction If the Secretary of Housing and Urban Development promulgates rules, issues guidance, or sets forth conditions in any application, notice of funding availability, or other publication or advisory regarding the provisions of this Act, the Secretary shall ensure that\u2014 (1) any individual defined as homeless under subsection (a) or (b) is eligible for any program or program component under this Act; and (2) all individuals defined as homeless under subsection (a) proposed to be served by an applicant, and all proposed program components or housing or service models, are given the same priority, points, or weight. ;\n**(2)**\nin section 401 ( 42 U.S.C. 11360 )\u2014\n**(A)**\nin paragraph (1)(C)\u2014\n**(i)**\nby striking clauses (ii) and (iv);\n**(ii)**\nby redesignating clauses (iii), (v), (vi), and (vii) as clauses (ii), (iii), (iv), and (v), respectively; and\n**(iii)**\nby striking the flush text following clause (v), as so redesignated;\n**(B)**\nin paragraph (2)(A)\u2014\n**(i)**\nin clause (i), by striking and lives and all that follows through shelter and inserting under any provision of section 103 ;\n**(ii)**\nin clause (ii), by striking and living or residing in a place not meant for human habitation, a safe haven, or in an emergency shelter continuously and inserting under any provision of section 103 ; and\n**(iii)**\nin clause (iii)\u2014\n**(I)**\nby striking (or a minor head of household if no adult is present in the household) and inserting or a minor head of household (if no adult is present in the household), ; and\n**(II)**\nby inserting before the period at the end the following: , or has child with a disability, as defined in section 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 ), or an infant or toddler with a disability, as defined in section 632 of such Act ( 20 U.S.C. 1432 ) ;\n**(C)**\nby striking paragraph (7);\n**(D)**\nby redesignating paragraphs (2) through (6) as paragraphs (3) through (7), respectively;\n**(E)**\nby inserting after paragraph (1) the following:\n(2) Child or youth defined as homeless under any other Federal program The term child or youth defined as homeless under any other Federal program means\u2014 (A) a homeless child or youth, as defined in section 725, including any parent or guardian with whom the child or youth is living; and (B) a youth who\u2014 (i) is not more than 24 years of age; (ii) cannot live safely with a parent, legal guardian, or relative; and (iii) has no other safe alternative living arrangement. ;\n**(F)**\nin paragraph (10)(A), by inserting any provision of before section 103 ;\n**(G)**\nby redesignating paragraphs (14) through (33) as paragraphs (15) through (34), respectively;\n**(H)**\nby inserting after paragraph (13) the following:\n(14) Other Federal statute The term other Federal statute includes\u2014 (A) the Runaway and Homeless Youth Act ( 42 U.S.C. 5701 et seq. ); (B) the Head Start Act ( 42 U.S.C. 9831 et seq. ); (C) the Child Care and Development Block Grant of 1990 ( 42 U.S.C. 9858 et seq. ); (D) subtitle N of the Violence Against Women Act of 1994 ( 42 U.S.C. 14043e et seq. ); (E) section 330(h) of the Public Health Service Act ( 42 U.S.C. 254b(h) ); (F) section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ); (G) the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ); and (H) the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ). ;\n**(I)**\nin paragraph (32), as so redesignated, by inserting children under 5 years of age, youth and young adults between 14 and 24 years of age, after status, or age), ;\n**(J)**\nin paragraph (33), as so redesignated, by inserting trafficking, after victims of ; and\n**(K)**\nin paragraph (34), as so redesignated\u2014\n**(i)**\nby inserting victims of trafficking, after assist ;\n**(ii)**\nby striking stalking victims and inserting stalking ; and\n**(iii)**\nby inserting trafficking, after concerning ;\n**(3)**\nin section 402(f) ( 42 U.S.C. 11360a(f) )\u2014\n**(A)**\nin paragraph (1)(B), by inserting considering the prevalence and needs of homeless individuals, as defined under any provision of section 103 after involved ; and\n**(B)**\nin paragraph (3)(D)\u2014\n**(i)**\nin clause (v), by striking and at the end;\n**(ii)**\nby redesignating clause (vi) as clause (vii); and\n**(iii)**\nby inserting after clause (v) the following:\n(vi) the submission of HMIS data to the Secretary on at least an annual basis; and ;\n**(4)**\nby inserting after section 408 ( 42 U.S.C. 11364 ) the following:\n409. Availability of HMIS data (a) In general The community-wide homeless management information system (in this section referred to as HMIS ) data provided to the Secretary under section 402(f)(3)(D)(vi) shall be made publically available on the internet website of the Department of Housing and Urban Development. (b) Required data The data publically available under subsection (a) shall be updated on at least an annual basis and shall include\u2014 (1) a cumulative count of the number of homeless individuals and families, as defined under any provision of section 103; (2) a cumulative assessment of the patterns of assistance provided under subtitles B and C for each geographic area involved; (3) a count of the number of homeless individuals and families, as defined under any provision of section 103, that are documented through the HMIS by each collaborative applicant; and (4) a count of the number of homeless women, as defined under any provision of section 103 and both unaccompanied and accompanied, including a breakout of the count by\u2014 (A) age range; (B) disability; and (C) length of time experiencing homelessness. ;\n**(5)**\nin section 422 ( 42 U.S.C. 11382 )\u2014\n**(A)**\nin subsection (c)(1)(B), by striking establish and inserting demonstrate local, needs-based ; and\n**(B)**\nby striking subsection (j) and inserting the following:\n(j) Rule of construction In awarding grants under subsection (a) and releasing a notification of funding availability under subsection (b), the Secretary shall\u2014 (1) without further action by the Department of Housing and Urban Development, ensure that any individual defined as homeless under any provision of section 103 is eligible for any program or program component under this Act; (2) ensure that homeless populations proposed to be served by the applicant, and proposed program components or housing or service models, are not awarded different priority, points, or weight; and (3) ensure that scoring is based primarily on the extent to which the applicant demonstrates that the project and program components\u2014 (A) would meet the priorities identified in the plan submitted under section 427(b)(1)(B); and (B) are cost-effective in meeting the overall goals and objectives identified in that plan. ;\n**(6)**\nin section 424(d) ( 42 U.S.C. 11384(d) ), by striking paragraph (5);\n**(7)**\nin section 425(c) ( 42 U.S.C. 11385(c) ), by striking and (G) providing and inserting (G) providing transportation to employment, early care and education programs, career and technical education programs, and health and mental health care services, and (H) providing ;\n**(8)**\nin section 426(b) ( 42 U.S.C. 11386(b) )\u2014\n**(A)**\nin paragraph (4), by amending subparagraph (D) to read as follows:\n(D) in the case of programs providing housing or services to families or youth, they will designate a staff person to be responsible for ensuring that children and youth being served in the program are\u2014 (i) enrolled in school and connected to appropriate services in the community, including Head Start, services provided under part C of the Individuals with Disabilities Education Act ( 20 U.S.C. 1431 et seq. ), programs authorized under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858 et seq. ), career and technical education, and services provided by local educational agency liaisons designated under subtitle B of title VII of this Act; and (ii) in the case of an unaccompanied youth, as defined in section 725, informed of their status as an independent student under section 480 of the Higher Education Act of 1965 ( 20 U.S.C. 1087vv ) and receive verification of such status for purposes of the Free Application for Federal Student Aid described in section 483 of such Act ( 20 U.S.C. 1090 ); and ;\n**(B)**\nin paragraph (6), by inserting the actual compliance with the certifications required under paragraph (4) and after Secretary ; and\n**(C)**\nin paragraph (7)\u2014\n**(i)**\nby inserting and youth after needs of children ;\n**(ii)**\nby inserting or unaccompanied youth after when families ;\n**(iii)**\nby inserting and unaccompanied youth after with children ; and\n**(iv)**\nby striking such children's and inserting such children and youth's ;\n**(9)**\nin section 427(b) ( 42 U.S.C. 11386a(b) )\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (vi), by adding and at the end;\n**(II)**\nin clause (vii), by striking and at the end; and\n**(III)**\nby striking clause (viii);\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby amending clause (iii) to read as follows:\n(iii) how the recipient will collaborate with local educational agencies, early care and education programs, and institutions of higher education to assist in the identification of and services to youth and families who become or remain homeless, including the steps the recipient will take to inform youth and families of their eligibility for services under part B of subtitle VII of this Act, the Head Start Act ( 42 U.S.C. 9831 et seq. ), the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858 et seq. ), and the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ); ; and\n**(II)**\nby striking clause (v) and inserting the following:\n(v) how the recipient will ensure the full implementation of the certifications and agreements described in paragraphs (4)(D) and (7) of section 426(b); ;\n**(iii)**\nin subparagraph (C)(i), by inserting and appropriate after rapid ; and\n**(iv)**\nby striking subparagraphs (F) and (G) and inserting the following:\n(F) for communities that establish and operate a centralized or coordinated assessment system, the extent to which that system\u2014 (i) ensures that individuals who are most in need of assistance receive it in a timely manner; (ii) in assessing need under clause (i), uses separate, specific, age-appropriate criteria for assessing the safety and needs of children under 5 years of age, school-age children, unaccompanied youth and young adults between 14 and 24 years of age, and families that are unrelated to the criteria through which an individual qualifies as homeless under section 103; (iii) is accessible to unaccompanied youth and homeless families; (iv) diverts individuals to safe, stable, age-appropriate accommodations; and (v) includes affordable housing developers, youth service providers, early childhood programs, local educational agencies, and mental health organizations; and (G) such other factors as the Secretary determines to be appropriate to carry out this subtitle in an effective and efficient manner, except that such factors may not have the effect of prioritizing or weighting, unless justified by local data or information contained in a plan submitted under subparagraph (B)\u2014 (i) any service with respect to a specific subpopulation of homeless individuals over another; or (ii) any program component or housing or service model over another. ; and\n**(B)**\nby amending paragraph (3) to read as follows:\n(3) Homelessness counts The Secretary shall require that communities that conduct an annual count of homeless people shall count all homeless individuals identified and reported by any program funded under any provision of this Act or any other Federal statute. ;\n**(10)**\nin section 428 ( 42 U.S.C. 11386b )\u2014\n**(A)**\nin subsection (a)(1)\u2014\n**(i)**\nby striking disabilities and and inserting disabilities, ; and\n**(ii)**\nby inserting , and homeless families where a child has a disability before the period at the end;\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (1), by inserting promoting before independent ; and\n**(ii)**\nby striking paragraphs (2) and (3) and inserting the following:\n(2) Prohibition The Secretary shall not provide bonuses or other incentives under paragraph (1) that have the effect of prioritizing or weighting, unless justified by local data or information contained in a plan submitted under section 427(b)(1)(B)\u2014 (A) any service with respect to a specific subpopulation of homeless individuals over another; or (B) any program component or housing or service model over another. (3) Rule of construction For purposes of this subsection, activities that have been proven to be effective at reducing homelessness generally or reducing homelessness for a specific subpopulation include any activity determined by the Secretary, after providing notice and an opportunity for public comment, to have been proven effective at\u2014 (A) reducing homelessness generally; (B) reducing homelessness for a specific subpopulation; (C) reducing homelessness in a community for populations overrepresented in any counts conducted in that community under section 427(b)(3); or (D) achieving homeless prevention, reducing recidivism, and promoting self-sufficiency and independent living. (4) Encouraging local success and innovation In providing bonuses or incentives under paragraph (1), the Secretary shall seek to encourage the implementation of proven strategies and innovation in reducing homelessness among the local priority populations identified in the plan submitted by an applicant under section 427(b)(1)(B). The Secretary shall not implement bonuses or incentives that promote a national priority established by the Secretary. ; and\n**(C)**\nby striking subsection (e); and\n**(11)**\nby amending section 434 ( 42 U.S.C. 11388 ) to read as follows:\n434. Reports to Congress (a) In general The Secretary shall submit to Congress an annual report, which shall\u2014 (1) summarize the activities carried out under this subtitle and set forth the findings, conclusions, and recommendations of the Secretary as a result of the activities; (2) include, for the year preceding the date on which the report is submitted\u2014 (A) data required to be made publically available in the report under section 409; and (B) data on programs funded under any other Federal statute; and (3) provide information on\u2014 (A) the extent to which the data collected under section 427(b)(3) may be duplicative; and (B) the policies and practices employed to account for such duplication, where applicable, to ensure an accurate point-in-time count. (b) Timing A report under subsection (a) shall be submitted not later than 4 months after the end of each fiscal year. .\n##### (b) Technical and conforming amendment\nThe table of contents in section 101(b) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11301 note) is amended by inserting after the item relating to section 408 the following:\nSec. 409. Availability of HMIS data. .",
      "versionDate": "2025-12-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1667",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Homeless Children and Youth Act of 2025",
      "type": "S"
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
        "name": "Housing and Community Development",
        "updateDate": "2026-01-05T16:39:48Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6403ih.xml"
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
      "title": "Homeless Children and Youth Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homeless Children and Youth Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the McKinney-Vento Homeless Assistance Act to meet the needs of homeless children, youth, and families, and honor the assessments and priorities of local communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:18:26Z"
    }
  ]
}
```
