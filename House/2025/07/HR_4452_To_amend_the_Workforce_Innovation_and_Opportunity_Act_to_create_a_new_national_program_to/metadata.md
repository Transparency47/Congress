# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4452?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4452
- Title: STEM RESTART Act
- Congress: 119
- Bill type: HR
- Bill number: 4452
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-02-18T09:05:31Z
- Update date including text: 2026-02-18T09:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4452",
    "number": "4452",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "STEM RESTART Act",
    "type": "HR",
    "updateDate": "2026-02-18T09:05:31Z",
    "updateDateIncludingText": "2026-02-18T09:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:03:40Z",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "IN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4452ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4452\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Ms. Houlahan (for herself and Mr. Baird ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to create a new national program to support mid-career workers in reentering the STEM workforce, by providing funding to small- and medium-sized STEM businesses so the businesses can offer paid internships or other returnships that lead to positions above entry level.\n#### 1. Short title\nThis Act may be cited as the STEM Restoring Employment Skills through Targeted Assistance, Re-entry, and Training Act or the STEM RESTART Act .\n#### 2. Returning skilled workers to the stem workforce\n##### (a) In general\nSubtitle D of title I of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby redesignating section 172 ( 29 U.S.C. 3227 ) as section 173; and\n**(2)**\nby inserting after section 171 the following:\n172. Grants to support skilled workers in returning or transitioning to the stem workforce (a) Purposes The purposes of this section are to\u2014 (1) prioritize expanding opportunities, through high-quality internships or other returnships in STEM fields for unemployed or underemployed workers, particularly workers from rural areas, who are mid-career skilled workers seeking to return or transition to in-demand industry sectors or occupations within the STEM workforce, at positions and compensation above entry level; and (2) establish grant funding and other incentives for small-sized and medium-sized companies in in-demand industry sectors or occupations to establish programs that provide on-the-job evaluation, education, and training for mid-career skilled workers described in paragraph (1). (b) Definitions In this section: (1) Medium-sized enterprise The term medium-sized , used with respect to an enterprise, means an entity that employs more than 499 and fewer than 10,000 employees. (2) Restart grant The term RESTART grant means a grant made under subsection (c). (3) Returnship The term returnship shall mean any internship, apprenticeship, re-entry opportunity, direct hiring opportunity with support, or other similar opportunity designed to provide workers seeking to return or transition to the STEM workforce with positions that\u2014 (A) are above entry level; (B) provide salaries, stipends, or other payments, and benefits, that are above entry level; and (C) provide training that leads workers toward full-time careers and provides pathways toward advancement and leadership. (4) Rural area The term rural area means an area that is not an urban area (within the meaning of the notice of final program criteria entitled Urban Area Criteria for the 2010 Census (76 Fed. Reg. 53030 (August 24, 2011))). (5) Small-sized enterprise The term small-sized , used with respect to an enterprise, means an entity that employs more than 49 and fewer than 500 individuals. (6) Stem The term STEM has the meaning given the term in section 2 of the America COMPETES Reauthorization Act of 2010 ( 42 U.S.C. 6621 note). (7) Unemployed or underemployed individual The term unemployed or underemployed individual means\u2014 (A) an unemployed or underemployed individual as defined by the Bureau of Labor Statistics; and (B) a displaced or furloughed worker. (c) Grant (1) In general From the amounts made available to carry out this section, the Secretary shall award grants, on a competitive basis, to eligible entities, to carry out returnship programs that provide opportunities above entry level in STEM fields for mid-career skilled workers, and achieve the purposes described in subsection (a). (2) Periods The Secretary shall award the grants for an initial period of not less than 3 years and not more than 5 years. (3) Amounts In awarding grants under this subsection, the Secretary shall award a grant\u2014 (A) for a small-sized enterprise, in an amount so that each annual payment for the grant is not less than $100,000 or more than $1,000,000; and (B) for a medium-sized enterprise or consortium, in an amount so that each annual payment for the grant is not less than $500,000 or more than $5,000,000. (d) Eligibility (1) Eligible entities To be eligible to receive a RESTART grant under this section, an entity shall\u2014 (A) (i) be located in the United States and have significant operations and employees within the United States; (ii) not be a debtor in a bankruptcy proceeding, within the meaning of section 4003(c)(3)(D)(i)(V) of the CARES Act ( 15 U.S.C. 9042(c)(3)(D)(i)(V) ) or under a State bankruptcy law; and (iii) be within an in-demand industry sector or occupation in a STEM field; and (B) be\u2014 (i) a small-sized enterprise; (ii) a medium-sized enterprise; or (iii) a consortium of small-sized or medium-sized enterprises. (2) Eligible providers (A) In general An eligible entity that desires to partner with a provider in order to carry out a returnship program under this section shall enter into an arrangement with an eligible provider. (B) Provider To be eligible to enter into such an arrangement, a provider\u2014 (i) may or may not directly employ skilled workers in STEM fields but\u2014 (I) shall have expertise in human resources-related activities, such as identifying or carrying out staffing with skilled workers; and (II) shall be capable of providing high-quality education and training services; and (ii) may be\u2014 (I) (aa) an institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )); or (bb) a non-degree-granting institution that is governed by the same body that governs an institution of higher education described in item (aa); (II) a public, private for-profit, or private nonprofit service provider, approved by the local board; (III) a joint labor-management organization; (IV) an eligible provider of adult education and literacy activities under title II; or (V) an established nonprofit organization that conducts research or provides training on technical and employability skills and knowledge aligned to the needs of adult learners and workers. (e) Applications (1) In general To be eligible to receive a RESTART grant to carry out a returnship program, an entity shall submit an application to the Secretary at such time and in such manner as the Secretary may reasonably require. (2) Contents Such an application shall include\u2014 (A) a description of the demand for skilled workers in STEM fields and how the RESTART grant will be used to help meet that demand; (B) a description of how the program will lead to employment of unemployed or underemployed individuals, particularly workers from rural areas, who seek to return or transition to the STEM workforce; (C) if the entity has entered into or plans to enter into an arrangement with an eligible provider as described in subsection (d)(2) to carry out a returnship program, information identifying the eligible provider, and a description of how the arrangement will help the entity build the knowledge and skills of skilled workers participating in the program; (D) a description of how the eligible entity will develop and establish, or expand, a returnship program that adds to the number of full-time employees employed by the entity, but does not displace full-time employees currently (as of the date of submission of the application) employed by the entity; (E) an assurance that any new or existing returnship program developed and established, or expanded, with the grant funds will last for at least 10 weeks and provide compensation to participants in the form of a salary, stipend, or other payment, and benefits, that are offered to full-time employees with equivalent experience and expertise, such as health care or child care benefits; and (F) if the returnship program leads to a recognized postsecondary credential, information on the quality of the program that leads to the credential. (3) Priority In making grants under this section, the Secretary shall give priority to entities who are proposing programs that prioritize returnships for workers in in-demand industry sectors or occupations, according to the State board or from rural areas. (f) Use of funds (1) In general An entity that receives a grant under this section shall use the grant funds to carry out a returnship program, of not less than 10 weeks, through which the entity provides for\u2014 (A) the education and training of returnship participants; and (B) the services of existing employees (as of the date the program begins) of the entity who are working with returnship participants in an educational, training, or managerial role, to maximize the retention rate and effectiveness of the returnship program. (2) Specific uses The grant funds may be used\u2014 (A) to pay for the evaluation, and entry into the program, and education and training of returnship participants, including payment for the duration of the program for the participants for\u2014 (i) equipment, travel, and (as necessary) housing; (ii) mentorship and career counseling; and (iii) salaries, stipends, or payments, and benefits, described in subsection (e)(2)(E); (B) to supplement, and not supplant, the compensation of those existing employees of the entity who are directly supporting a returnship program through the work described in paragraph (1)(B); and (C) to enter into an arrangement with an eligible provider to carry out a returnship program. (3) Existing employees Not more than 20 percent of the grant funds may be used to provide compensation for the existing employees performing the work described in paragraph (1)(B). (4) Coordination with state boards An entity that receives a grant under this section shall coordinate activities with the State board established under section 101, to ensure collaboration and alignment of workforce programs. (g) Reporting and evaluation requirements (1) Report to the secretary An entity that receives a grant under this section for a returnship program shall prepare, certify the contents of, and submit to the Secretary an annual report containing data regarding\u2014 (A) the total number of the participants, and the number of such participants disaggregated by sex, race, and ethnicity; (B) the total number of the participants transitioned into full-time employment, and the number of such transitioned participants disaggregated by sex, race, and ethnicity; and (C) if the returnship program includes participants in an internship, the conversion rate of the internship participants to employees, for the total number of those participants and the conversion rate of those participants disaggregated by sex, race, and ethnicity. (2) Evaluation and report by the secretary Not later than 180 days after receiving the annual reports from grant recipients under paragraph (1), the Secretary shall\u2014 (A) (i) prepare a report that presents the data collected through the reports, including data disaggregated by sex, race, and ethnicity, and an evaluation based on that data of the best practices for effectively implementing returnship (including internship) programs; and (ii) submit the report to the Committee on Education and Workforce of the House of Representatives, and the Committee on Health, Education, Labor, and Pensions of the Senate; and (B) post information on a website on best practices described in subparagraph (A)(i). (h) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $50,000,000 for each of fiscal years 2026 through 2030. .\n##### (b) Table of contents\nThe table of contents in section 1(b) of the Workforce Innovation and Opportunity Act is amended\u2014\n**(1)**\nby redesignating the item relating to section 172 as the item relating to section 173; and\n**(2)**\nby inserting after the item relating to section 171 the following:\nSec. 172. Grants to support skilled workers in returning or transitioning to the STEM workforce. .\n##### (c) Conforming amendment\nSection 8041(g)(2) of the Substance Use-Disorder Prevention that Promotes Opioid Recovery and Treatment for Patients and Communities Act ( 29 U.S.C. 3225a(g)(2) ) is amended in subparagraph (C), by striking 172(f) and inserting 173(f) .",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-07-16",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2306",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STEM RESTART Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-05T15:15:41Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4452ih.xml"
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
      "title": "STEM RESTART Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STEM RESTART Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STEM Restoring Employment Skills through Targeted Assistance, Re-entry, and Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Workforce Innovation and Opportunity Act to create a new national program to support mid-career workers in reentering the STEM workforce, by providing funding to small- and medium-sized STEM businesses so the businesses can offer paid internships or other returnships that lead to positions above entry level.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:33:22Z"
    }
  ]
}
```
