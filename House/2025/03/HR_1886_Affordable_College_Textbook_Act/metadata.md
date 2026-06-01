# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1886
- Title: Affordable College Textbook Act
- Congress: 119
- Bill type: HR
- Bill number: 1886
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-05T21:40:43Z
- Update date including text: 2025-12-05T21:40:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1886",
    "number": "1886",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Affordable College Textbook Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:40:43Z",
    "updateDateIncludingText": "2025-12-05T21:40:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:04:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1886ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1886\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Neguse introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo expand the use of open textbooks in order to achieve savings for students and improve textbook price information.\n#### 1. Short title\nThis Act may be cited as the Affordable College Textbook Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe high cost of college textbooks continues to be a barrier for many students in achieving higher education.\n**(2)**\nAccording to the College Board, during the 2024\u20132025 academic year, the average student budget for college books and supplies at 4-year public institutions of higher education was $1,290.\n**(3)**\nThe Government Accountability Office found that new textbook prices increased 82 percent between 2002 and 2012 and that although Federal efforts to increase price transparency have provided students and families with more and better information, more must be done to address rising costs.\n**(4)**\nThe growth of the internet has enabled the creation and sharing of digital content, including open educational resources that can be freely used by students, teachers, and members of the public.\n**(5)**\nAccording to the Student PIRGs, expanded use of open educational resources has the potential to save students more than a billion dollars annually.\n**(6)**\nFederal investment in expanding the use of open educational resources has lowered college textbook costs and reduced financial barriers to higher education, while making efficient use of taxpayer funds.\n**(7)**\nEducational materials, including open educational resources, must be accessible to the widest possible range of individuals, including those with disabilities.\n#### 3. Open textbook grant program\n##### (a) Definitions\nIn this section:\n**(1) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(2) Open educational resource**\nThe term open educational resource has the meaning given the term in section 133 of the Higher Education Act of 1965 ( 20 U.S.C. 1015b ).\n**(3) Open textbook**\nThe term open textbook means an open educational resource or set of open educational resources that either is a textbook or can be used in place of a textbook for a postsecondary course at an institution of higher education.\n**(4) Relevant faculty**\nThe term relevant faculty means both tenure track and contingent faculty members who may be involved in the creation or use of open textbooks created as part of an application under subsection (d).\n**(5) Secretary**\nThe term Secretary means the Secretary of Education.\n**(6) Supplemental material**\nThe term supplemental material has the meaning given the term in section 133 of the Higher Education Act of 1965 ( 20 U.S.C. 1015b ).\n##### (b) Grants authorized\nFrom the amounts appropriated under subsection (k), the Secretary shall make grants, on a competitive basis, to eligible entities to support projects that expand the use of open textbooks in order to achieve savings for students while maintaining or improving instruction and student learning outcomes.\n##### (c) Eligible entity\nIn this section, the term eligible entity means an institution of higher education, a consortium of institutions of higher education, or a consortium of States on behalf of institutions of higher education.\n##### (d) Applications\n**(1) In general**\nEach eligible entity desiring a grant under this section, after consultation and consensus with relevant faculty, shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may reasonably require.\n**(2) Contents**\nEach application submitted under paragraph (1) shall include a description of the project to be completed with grant funds and\u2014\n**(A)**\na plan for promoting and tracking the use of open textbooks in postsecondary courses offered by the eligible entity and across participating members of the consortium, where applicable, including an estimate of the projected savings that will be achieved for students;\n**(B)**\na plan for identifying gaps in the open textbook marketplace in courses that are part of degree-granting programs, which may include a plan for evaluating, before creating new open textbooks, whether existing open textbooks could be used or adapted for the same purpose, and in the case that a gap exists, creating new open textbooks;\n**(C)**\na plan for quality review and review of accuracy of any open textbooks to be created or adapted through the grant;\n**(D)**\na plan for assessing the impact of open textbooks on instruction, student learning outcomes, course outcomes, and educational costs at the eligible entity and across participating members of the consortium, where applicable;\n**(E)**\na plan for disseminating information about the results of the project to institutions of higher education outside of the eligible entity, including promoting the adoption of any open textbooks created or adapted through the grant;\n**(F)**\na statement on consultation and consensus with relevant faculty, including those engaged in the creation of open textbooks, in the development of the application;\n**(G)**\na plan for professional development to build the capacity of faculty, instructors, and other staff to adapt and use open textbooks;\n**(H)**\na plan for updating the open textbooks beyond the funded period; and\n**(I)**\na plan to make open textbooks that are accessible to students with disabilities.\n##### (e) Special consideration\nIn awarding grants under this section, the Secretary shall give special consideration to applications that demonstrate the greatest potential to\u2014\n**(1)**\nachieve the highest level of savings for students through sustainable expanded use of open textbooks in postsecondary courses offered by the eligible entity;\n**(2)**\nexpand the use of open textbooks at institutions of higher education outside of the eligible entity; and\n**(3)**\nproduce\u2014\n**(A)**\nthe highest quality open textbooks;\n**(B)**\nopen textbooks that can be most easily utilized and adapted by relevant faculty members at institutions of higher education;\n**(C)**\nopen textbooks that correspond to the highest enrollment courses at institutions of higher education; and\n**(D)**\nopen textbooks created or adapted in partnership with entities within institutions of higher education, including campus bookstores, that will assist in marketing and distribution of the open textbook.\n##### (f) Use of funds\nAn eligible entity that receives a grant under this section shall use the grant funds to carry out any of the following activities to expand the use of open textbooks:\n**(1)**\nProfessional development for any relevant faculty and staff members at institutions of higher education, including the search for and review of open textbooks.\n**(2)**\nCreation or adaptation of open textbooks.\n**(3)**\nDevelopment or improvement of supplemental materials and informational resources that are necessary to support the use of open textbooks, including accessible instructional materials for students with disabilities.\n**(4)**\nResearch evaluating the efficacy of the use of open textbooks for achieving savings for students and the impact on instruction and student learning outcomes.\n##### (g) License\nFor each open textbook, supplemental material, or informational resource created or adapted wholly or in part under this section that constitutes a new copyrightable work, the eligible entity receiving the grant shall release such textbook, material, or resource to the public under a non-exclusive, royalty-free, perpetual, and irrevocable license to exercise any of the rights under copyright conditioned only on the requirement that attribution be given as directed by the copyright owner.\n##### (h) Access and distribution\nThe full and complete digital content of each open textbook, supplemental material, or informational resource created or adapted wholly or in part under this section shall be made available free of charge to the public\u2014\n**(1)**\non an easily accessible and interoperable website, which shall be identified to the Secretary by the eligible entity;\n**(2)**\nin a machine readable, digital format that anyone can directly download, edit with attribution, and redistribute;\n**(3)**\nin a format that conforms to accessibility standards under section 508 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794d ), where feasible; and\n**(4)**\nwith identifying information, including the title, edition, author, publisher, copyright date, and International Standard Book Number, if available.\n##### (i) Report\nUpon an eligible entity\u2019s completion of a project supported under this section, the eligible entity shall prepare and submit a report to the Secretary regarding\u2014\n**(1)**\nthe effectiveness of the project in expanding the use of open textbooks and in achieving savings for students;\n**(2)**\nthe impact of the project on expanding the use of open textbooks at institutions of higher education outside of the eligible entity;\n**(3)**\nopen textbooks, supplemental materials, and informational resources created or adapted wholly or in part under the grant, including instructions on where the public can access each educational resource under the terms of subsection (h);\n**(4)**\nthe impact of the project on instruction and student learning outcomes; and\n**(5)**\nall project costs, including the value of any volunteer labor and institutional capital used for the project.\n##### (j) Annual report to congress\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary shall prepare and submit a report to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives detailing\u2014\n**(1)**\nthe open textbooks, supplemental materials, and informational resources created or adapted wholly or in part under this section;\n**(2)**\nthe adoption of such open textbooks, including outside of the eligible entity;\n**(3)**\nthe savings generated for students, States, and the Federal Government through projects supported under this section; and\n**(4)**\nthe impact of projects supported under this section on instruction and student learning outcomes.\n##### (k) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section such sums as are necessary.\n#### 4. Textbook price information\nSection 133 of the Higher Education Act of 1965 ( 20 U.S.C. 1015b ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby striking paragraph (6) and inserting the following:\n(6) Open educational resource The term open educational resource means a teaching, learning, or research resource that is offered freely to users in at least one form and that resides in the public domain or has been released under an open copyright license that allows for its free use, reuse, modification, and sharing with attribution. ; and\n**(B)**\nin paragraph (9), by striking textbook that and all that follows through the period at the end and inserting textbook that may include printed materials, website access, and electronically distributed materials. ;\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking or other person or adopting entity in charge of selecting course materials and inserting or other person or entity in charge of selecting or aiding in the discovery and procurement of course materials ;\n**(B)**\nin subparagraph (A), by inserting such institution of higher education or to after would make the college textbook or supplemental material available to ; and\n**(C)**\nby adding at the end the following:\n(E) Whether the college textbook or supplemental material is an open educational resource. (F) For a college textbook or supplemental material delivered primarily in a digital format, a summary of terms and conditions under which a publisher collects and uses student data through the student\u2019s use of such college textbook or supplemental material, including whether a student can opt out of such terms and conditions. ;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nin the subsection heading, by striking ISBN ; and\n**(B)**\nby striking paragraph (1) and inserting the following:\n(1) verify and disclose, on (or linked from) the institution's internet course schedule, for each course listed in such course schedule, and in a manner of the institution's choosing (except that if the institution determines that the disclosure of the information described in this subsection is not practicable or available for a college textbook or supplemental material, then the institution shall indicate the status of such information in lieu of the information required under this subsection)\u2014 (A) the International Standard Book Number of required and recommended college textbooks and supplemental materials, except that if the International Standard Book Number is not available for such college textbook or supplemental material, then the institution shall include in the internet course schedule the author, title, publisher, and copyright date for such college textbook or supplemental material; (B) the retail price of required and recommended college textbooks and supplemental materials; (C) any applicable fee information of required and recommended college textbooks and supplemental materials; (D) whether each required and recommended college textbook and supplemental material is an open educational resource; and (E) for a college textbook or supplemental material delivered primarily in a digital format, a link to the summary required to be provided by the publisher under subsection (c)(1)(F); and ;\n**(4)**\nby striking subsection (e) and inserting the following:\n(e) Availability of information for college bookstores (1) In general An institution of higher education receiving Federal financial assistance shall assist a college bookstore that is operated by, or in a contractual relationship or otherwise affiliated with, the institution, in obtaining required and recommended course materials information and such course schedule and enrollment information as is reasonably required to implement this section so that such bookstore may\u2014 (A) verify availability of such materials; (B) source lower cost options, including presenting lower cost alternatives to faculty for faculty to consider, when practicable; and (C) maximize the availability of format options for students. (2) Due dates In carrying out paragraph (1), an institution of higher education may establish due dates for faculty or departments to notify the campus bookstore of required and recommended course materials. ; and\n**(5)**\nin subsection (f)\u2014\n**(A)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (5); and\n**(B)**\nby inserting after paragraph (2) the following:\n(3) available open educational resources; .\n#### 5. Sense of Congress\nIt is the sense of Congress that institutions of higher education should encourage the consideration of open textbooks by faculty within the generally accepted principles of academic freedom that establishes the right and responsibility of faculty members, individually and collectively, to select course materials that are pedagogically most appropriate for their classes.\n#### 6. GAO report\nNot later than 3 years after the date of enactment of this Act, the Comptroller General of the United States shall prepare and submit a report to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives on the cost of textbooks to students at institutions of higher education. The report shall particularly examine\u2014\n**(1)**\nthe implementation of section 133 of the Higher Education Act of 1965 ( 20 U.S.C. 1015b ), as amended by section 4, including\u2014\n**(A)**\nthe availability of college textbook and open educational resource information on course schedules;\n**(B)**\nthe compliance of publishers with applicable requirements under such section; and\n**(C)**\nthe costs and benefits to institutions of higher education, relevant faculty, and students;\n**(2)**\nthe change in the cost of textbooks;\n**(3)**\nthe factors, including open textbooks, that have contributed to the change of the cost of textbooks;\n**(4)**\nthe extent to which open textbooks are used at institutions of higher education; and\n**(5)**\nhow institutions are tracking the impact of open textbooks on instruction and student learning outcomes.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-02-26",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1398-1399)"
      },
      "number": "740",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Affordable College Textbook Act",
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
        "updateDate": "2025-03-23T10:56:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1886",
          "measure-number": "1886",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1886v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Affordable College Textbook Act</strong></p><p>This bill provides statutory authority for an open textbook grant program for\u00a0institutions of higher education (IHEs). (A similar program, known as the Open Textbooks Pilot program, first received federal funding in FY2018.)</p><p>Specifically, the bill directs the Department of Education to make grants to IHEs or states on behalf of IHEs\u00a0to support projects that expand the use of open textbooks. An <em>open textbook</em> is an educational resource that either resides in the public domain or has been released under an intellectual license that permits its free use, reuse, modification, and sharing with others.</p><p>Within three years of the bill's enactment, the Government Accountability Office must report to Congress on the cost of textbooks at IHEs. This report must examine, among other topics, the factors that have contributed\u00a0to the change in the cost of textbooks.</p>"
        },
        "title": "Affordable College Textbook Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1886.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Affordable College Textbook Act</strong></p><p>This bill provides statutory authority for an open textbook grant program for\u00a0institutions of higher education (IHEs). (A similar program, known as the Open Textbooks Pilot program, first received federal funding in FY2018.)</p><p>Specifically, the bill directs the Department of Education to make grants to IHEs or states on behalf of IHEs\u00a0to support projects that expand the use of open textbooks. An <em>open textbook</em> is an educational resource that either resides in the public domain or has been released under an intellectual license that permits its free use, reuse, modification, and sharing with others.</p><p>Within three years of the bill's enactment, the Government Accountability Office must report to Congress on the cost of textbooks at IHEs. This report must examine, among other topics, the factors that have contributed\u00a0to the change in the cost of textbooks.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1886"
    },
    "title": "Affordable College Textbook Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Affordable College Textbook Act</strong></p><p>This bill provides statutory authority for an open textbook grant program for\u00a0institutions of higher education (IHEs). (A similar program, known as the Open Textbooks Pilot program, first received federal funding in FY2018.)</p><p>Specifically, the bill directs the Department of Education to make grants to IHEs or states on behalf of IHEs\u00a0to support projects that expand the use of open textbooks. An <em>open textbook</em> is an educational resource that either resides in the public domain or has been released under an intellectual license that permits its free use, reuse, modification, and sharing with others.</p><p>Within three years of the bill's enactment, the Government Accountability Office must report to Congress on the cost of textbooks at IHEs. This report must examine, among other topics, the factors that have contributed\u00a0to the change in the cost of textbooks.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1886"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1886ih.xml"
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
      "title": "Affordable College Textbook Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T10:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affordable College Textbook Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand the use of open textbooks in order to achieve savings for students and improve textbook price information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:18Z"
    }
  ]
}
```
