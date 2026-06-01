# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5458
- Title: CCAMPIS Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 5458
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-03-31T20:26:21Z
- Update date including text: 2026-03-31T20:26:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Education and Workforce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5458",
    "number": "5458",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001101",
        "district": "5",
        "firstName": "Katherine",
        "fullName": "Rep. Clark, Katherine M. [D-MA-5]",
        "lastName": "Clark",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "CCAMPIS Reauthorization Act",
    "type": "HR",
    "updateDate": "2026-03-31T20:26:21Z",
    "updateDateIncludingText": "2026-03-31T20:26:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:06:45Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "HI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "IL"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5458ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5458\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Ms. Clark of Massachusetts (for herself, Ms. Bonamici , Mr. Gomez , Ms. Pettersen , Ms. McClellan , and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Care Access Means Parents In School Program under the Higher Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the Child Care Access Means Parents In Schools Reauthorization Act or the CCAMPIS Reauthorization Act .\n#### 2. Child care access means parents in school\nSection 419N of the Higher Education Act of 1965 ( 20 U.S.C. 1070e ) is amended to read as follows:\n419N. Child care access means parents in school (a) Purpose The purpose of this section is to facilitate the success of eligible student parents in postsecondary education through the provision of child care services, including campus-based child care services. (b) Program authorized (1) Authority The Secretary may award grants to eligible institutions to assist the eligible institutions in providing child care services to eligible student parents. (2) Amount of grants (A) Minimum grant amount A grant under this section shall be awarded in an amount that is not less than $75,000 per year. (B) Maximum grant amount A grant under this section shall be awarded in an amount that is not more than $2,000,000 per year. (C) Ratable increases and decreases The amount specified in subparagraph (A) shall be ratably increased or decreased to the extent that funds available under subsection (i) exceed or are less than (respectively) the amount required to provide the amount specified in subparagraph (A). (3) Duration and payments (A) Duration The Secretary shall award a grant under this section for a period of 5 years. (B) Payments Subject to subparagraphs (C) and (D), the Secretary shall make annual grant payments under this section. (C) Supplemental grants The Secretary may consider applications from an eligible institution that receives grant funds under this section for additional funds in any subsequent fiscal year, if such institution demonstrates the need for such additional funds, subject to the maximum grant amount under paragraph (2)(B) and the duration of the original grant under subparagraph (A). (D) Continuation awards The Secretary shall make continuation awards under this section to an institution of higher education only if the Secretary determines, on the basis of the reports submitted under subsection (g)(1), that the institution is making a good faith effort to ensure that eligible student parents at the institution have access to affordable, quality child care services. (4) Definition of eligible institution In this section, the term eligible institution means\u2014 (A) an institution of higher education, as defined in section 101, with respect to which, the total number of students eligible for a Federal Pell Grant enrolled at the institution of higher education in the most recently completed award year was equal to or greater than 150; or (B) a consortium of institutions of higher education described in subparagraph (A). (c) Use of funds (1) In General An eligible institution receiving a grant under this section shall use such grant funds to support access to child care services for eligible student parents enrolled at such institution by carrying out 1 or more of the following activities: (A) Establishing or supporting a campus-based child care program. (B) Providing subsidized child care using a sliding fee scale. (C) Providing subsidized and accessible before and after school services. (2) Permitted uses In addition to the required activities described in paragraph (1), an eligible institution receiving a grant under this section may use such grant funds to carry out 1 or more of the following activities: (A) Providing support services for eligible student parents. (B) Enhancing the quality of the campus-based child care program supported under this section, including to meet at least one of the purposes described in subparagraphs (A) through (C) of subsection (d)(15). (3) Prohibitions (A) Use of funds prohibition Funds under this section shall not be used for construction, except for renovation or repair to meet applicable State or local health or safety requirements. (B) Prohibition on additional eligibility requirements No eligible institution receiving a grant under this section may require a student parent to meet requirements (such as requirements related to work, academic progress, or enrollment intensity) to be eligible for child care services under this section other than the requirements listed in paragraph (5). (4) Rule of construction Nothing in this section shall be construed to prohibit an institution of higher education that receives grant funds under this section from serving the child care needs of the community served by such institution. (5) Definition of eligible student parent For the purpose of this section, the term eligible student parent means a student who\u2014 (A) is the parent or guardian of 1 or more dependent child; (B) is enrolled at an eligible institution; and (C) for the award year for which the determination is made\u2014 (i) is eligible to receive a Federal Pell Grant; or (ii) meets the financial eligibility criteria for receiving a Federal Pell Grant under section 401, but is not eligible for a Federal Pell Grant for such award year because\u2014 (I) the student has not completed the Free Application for Federal Student Aid described in section 483; (II) the student does not meet the eligibility requirements of section 484; or (III) the student is enrolled in a graduate or first professional course of study. (6) Publicity The Secretary shall publicize the availability of grants under this section, in addition to publication in the Federal Register, and shall inform appropriate educational, nonprofit, and child care organizations of such availability. (7) Special rule Any assistance provided to eligible student parents from grants provided under this section shall not be treated as other financial assistance for the purposes of section 471(3). (d) Applications An eligible institution desiring a grant under this section shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require. Such application shall\u2014 (1) demonstrate that the institution is an eligible institution described in subsection (b)(4); (2) specify the amount of funds requested; (3) demonstrate the need of eligible student parents at the institution for accessible and affordable child care services by including in the application\u2014 (A) information regarding student demographics; (B) an assessment of child care capacity on or near campus; (C) information regarding the existence of waiting lists for child care services on or near campus; (D) information regarding additional needs created by concentrations of poverty or by geographic isolation; and (E) other relevant data; (4) contain a description of the activities to be assisted, including whether the grant funds will support an existing child care program or a new child care program; (5) identify the resources, including technical expertise and financial support, the institution will draw upon to support the child care program and the participation of eligible student parents in the program (such as accessing social services funding, using student activity fees to help pay the costs of child care, using resources obtained by meeting the needs of parents who are not eligible student parents, and accessing foundation, corporate, or other institutional support) and demonstrate that the use of the resources will not result in increases in student tuition and fees; (6) contain an assurance that the institution will meet the child care needs of eligible student parents through the provision of services, or through a contract for the provision of services; (7) describe the extent to which the child care program will coordinate with the institution\u2019s early childhood education curriculum, to the extent the curriculum is available, to meet the needs of the students in the early childhood education program at the institution, and the needs of the parents and children participating in the child care program assisted under this section; (8) in the case of an institution seeking assistance to establish a campus-based child care program\u2014 (A) provide a timeline, covering the period from receipt of the grant through the provision of the child care services, delineating the specific steps the institution will take to achieve the goal of providing eligible student parents with child care services; (B) specify any measures the institution will take to assist eligible student parents with child care during the period before the institution provides child care services; (C) include a plan for identifying resources needed for the child care services, including space in which to provide child care services, and technical assistance if necessary; and (D) include plans to assure quality of campus-based child care facilities; (9) in the case of an institution seeking assistance for a campus-based child care program in existence on the date of the application\u2014 (A) provide information regarding the number of eligible student parents served through campus-based child care on such date; (B) provide information on the age groups of children to be served; (C) specify any measures the institution will take to assist eligible student parents who are waitlisted for the campus-based child care program; (D) provide information regarding the application of subsidies or a sliding fee scale for child care services; (E) specify what staff positions will be supported by funding under this section, and how those staff positions support the purpose under subsection (a); (F) provide information on the total number of children served by the campus-based child care program, and number of children of students served; and (G) specify if funding will be used to enhance program quality as described in subsection (c)(2)(B); (10) in the case of an institution seeking assistance that will contract for the provision of child care services\u2014 (A) provide information on the age groups of children to be served; (B) provide information regarding the application of subsidies or a sliding fee scale for child care services; and (C) provide information regarding parameters the institution will use in selecting child care providers in contracting for the provision of services, including\u2014 (i) assessment of program quality; and (ii) geographic location; (11) contain an assurance that any child care facility assisted under this section will meet the applicable State and local government licensing, certification, approval, or registration requirements; (12) describe how information regarding the availability of subsidized child care will be provided to students; (13) contain an assurance that the institution will assist student parents receiving child care services provided under this section in enrolling in Federal, State, Tribal, or local means-tested benefits programs for which they may be eligible, including\u2014 (A) the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ), a nutrition assistance program carried out under section 19 of such Act ( 7 U.S.C. 2028 ), or a nutrition assistance program carried out by the Secretary of Agriculture in the Northern Mariana Islands; (B) the supplemental security income program under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ); (C) the program of block grants to States for temporary assistance for needy families under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ); (D) the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ); (E) the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ); (F) Federal housing assistance programs, including tenant-based assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ), and public housing, as defined in section 3(b)(1) of such Act ( 42 U.S.C. 1437a(b)(1) ); (G) Federal child care assistance programs, including assistance under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ); (H) the free and reduced price school lunch program established under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ); (I) refundable credit for coverage under a qualified health plan under section 36B of the Internal Revenue Code of 1986; (J) the earned income tax credit under section 32 of the Internal Revenue Code of 1986; (K) the child tax credit under section 24 of the Internal Revenue Code of 1986; and (L) any other means-tested Federal program determined by the Secretary to be appropriate; (14) contain an abstract summarizing the contents of such application and how the institution intends to achieve the purpose under subsection (a); (15) contain a plan for any child care program assisted under this section to, not later than 3 years after the date the institution first receives assistance under this section\u2014 (A) meet the Head Start performance standards described in section 641A(a)(1)(B) of the Head Start Act ( 42 U.S.C. 9836a(a)(1)(B) ) or other equivalent evidence-based standards approved by the Secretary; (B) be in the top tier of the quality rating improvement system for such facilities used by the State in which the facility is located; or (C) be accredited by a national early childhood accrediting body with demonstrated valid and reliable program quality standards; and (16) contain an assurance that the institution will comply with the prohibitions described in subsection (c)(3). (e) Technical assistance The Secretary may provide technical assistance\u2014 (1) to eligible institutions to help such institutions qualify for, apply for, and maintain a grant under this section; and (2) to institutions receiving grants under this section to help such institutions meet the reporting requirements described in subsection (g). (f) Priority (1) In general The Secretary shall give priority in awarding grants under this section to eligible institutions that submit applications describing programs that\u2014 (A) leverage local or institutional resources, including in-kind contributions, to support the activities assisted under this section; (B) utilize a sliding fee scale for child care services provided under this section in order to support a high number of eligible student parents pursuing postsecondary education at the institution; and (C) provide additional resources or supports to students who are single parents. (2) Limitation The Secretary may not establish a priority in awarding grants under this section to eligible institutions that\u2014 (A) propose projects solely with off-campus child care providers; or (B) that are designed to support 2 or more child care providers. (g) Reporting requirements; continuing eligibility (1) Reporting requirements Each eligible institution receiving a grant under this section shall report to the Secretary annually information on\u2014 (A) the population of eligible student parents who received child care services under this section, including\u2014 (i) the number of such eligible student parents, disaggregated by full- and part-time status; (ii) information on such eligible student parents, including demographic information disaggregated by\u2014 (I) sex; (II) status as a single parent; (III) race and ethnicity; (IV) age groups of the dependents of such student parents; (V) classification as a student with a disability; (VI) recipients of educational assistance under laws administered by the Secretary of Defense or the Secretary of Veterans Affairs; (VII) status as a first-generation college student; and (VIII) levels of degree or credential pursued by such eligible student parents; and (iii) the number of such eligible student parents who\u2014 (I) remain enrolled at the institution during the academic year for which they received such services; (II) remain enrolled at the institution during the subsequent academic year after which they first received such services; (III) graduate from the institution during the academic year for which they received such services; (IV) transfer to a different institution during the academic year for which they received such services; or (V) withdrew from the institution during the academic year for which they received such services; (B) the fee structure for eligible student parents to receive child care services under this section, including any sliding scale; (C) the percentage of the institution\u2019s grant that was used directly to subsidize any fees charged for\u2014 (i) campus-based child care services for eligible student parents; and (ii) off-campus child care services for eligible student parents; (D) information on institutional or local resources, including in-kind contributions, leveraged to help eligible student parents access child care services; and (E) the relevant quality information of the child care services supported by a grant under this section, including\u2014 (i) the name of the accrediting agency or association that is providing accreditation to such child care services, if applicable; and (ii) the tier or level of the State tiered and transparent system for measuring the quality of child care providers that is associated with such child care services, if applicable. (2) Report (A) Report required On an annual basis, the Secretary shall make publicly available a report that includes a summary of the information described in paragraph (1). (B) Stakeholder consultation The Secretary shall work with relevant stakeholders to determine the manner in which the data described under paragraph (1) and summarized under subparagraph (A) is collected. (h) Nondiscrimination No person in the United States shall, on the basis of actual or perceived race, color, religion, national origin, sex (including sexual orientation, gender identity, pregnancy, childbirth, a medical condition related to pregnancy or childbirth, or sex stereotype), or disability, be excluded from participation in, be denied the benefits of, or be subjected to discrimination by any program funded, in whole or in part, with funds made available under this section or with amounts appropriated for grants, contracts, or certificates administered with such funds. (i) Authorization of appropriations There are authorized to be appropriated to carry out this section $500,000,000 for each of fiscal years 2026 through 2031. .",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2862",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CCAMPIS Reauthorization Act",
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
        "name": "Education",
        "updateDate": "2025-11-18T16:20:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119hr5458",
          "measure-number": "5458",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-18",
          "originChamber": "HOUSE",
          "update-date": "2026-02-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5458v00",
            "update-date": "2026-02-26"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Child Care Access Means Parents In Schools Reauthorization Act or the CCAMPIS Reauthorization Act</strong></p><p>This bill reauthorizes through FY2031 and revises the Child Care Access Means Parents in School Program. The program awards grants to support the participation of eligible low-income parents in postsecondary education through the provision of campus-based child care services.</p><p>Among other revisions to the program, the bill increases the minimum and maximum grant amounts, allows grant funds to be used for additional purposes (e.g., child care subsidies and support services), and specifies additional grant application requirements.</p>"
        },
        "title": "CCAMPIS Reauthorization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5458.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Child Care Access Means Parents In Schools Reauthorization Act or the CCAMPIS Reauthorization Act</strong></p><p>This bill reauthorizes through FY2031 and revises the Child Care Access Means Parents in School Program. The program awards grants to support the participation of eligible low-income parents in postsecondary education through the provision of campus-based child care services.</p><p>Among other revisions to the program, the bill increases the minimum and maximum grant amounts, allows grant funds to be used for additional purposes (e.g., child care subsidies and support services), and specifies additional grant application requirements.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119hr5458"
    },
    "title": "CCAMPIS Reauthorization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Child Care Access Means Parents In Schools Reauthorization Act or the CCAMPIS Reauthorization Act</strong></p><p>This bill reauthorizes through FY2031 and revises the Child Care Access Means Parents in School Program. The program awards grants to support the participation of eligible low-income parents in postsecondary education through the provision of campus-based child care services.</p><p>Among other revisions to the program, the bill increases the minimum and maximum grant amounts, allows grant funds to be used for additional purposes (e.g., child care subsidies and support services), and specifies additional grant application requirements.</p>",
      "updateDate": "2026-02-26",
      "versionCode": "id119hr5458"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5458ih.xml"
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
      "title": "CCAMPIS Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CCAMPIS Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Care Access Means Parents In Schools Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Care Access Means Parents In School Program under the Higher Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:20Z"
    }
  ]
}
```
