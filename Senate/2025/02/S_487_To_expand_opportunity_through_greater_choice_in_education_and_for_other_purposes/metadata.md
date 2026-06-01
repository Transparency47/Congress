# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/487
- Title: CHOICE Act
- Congress: 119
- Bill type: S
- Bill number: 487
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/487",
    "number": "487",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "CHOICE Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T23:06:48Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s487is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 487\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Scott of South Carolina (for himself and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo expand opportunity through greater choice in education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Creating Hope and Opportunity for Individuals and Communities through Education Act or the CHOICE Act .\nI\nImproving the Scholarships for Opportunity and Results Act\n#### 101. Purpose\nThe purpose of this title is to amend the Scholarships for Opportunity and Results Act ( Public Law 112\u201310 , 125 Stat. 199) in order to improve provisions concerning opportunity scholarships available for low-income students in the District of Columbia.\n#### 102. Improvements to the Scholarships for Opportunity and Results Act\nSection 3013(4) of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.13(4), D.C. Official Code) is amended, in the matter preceding subparagraph (A), by inserting , is enrolled, or will be enrolled for the next school year, in a public or private elementary school or secondary school, after District of Columbia .\nII\nEducation portability for individuals with disabilities\n#### 201. Purpose\nThe purpose of this title is to provide options to States to innovate and improve the education of children with disabilities by expanding the choices for students and parents under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ).\n#### 202. Amendments to the Individuals with Disabilities Education Act\n##### (a) Children enrolled in private schools by their parents\nSection 612(a)(10)(A) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1412(a)(10)(A) ) is amended by adding at the end the following:\n(viii) Parent option program If a State has established a program that meets the requirements of section 663(c)(11) (whether statewide or in limited areas of the State) and that allows a parent of a child described in section 663(c)(11)(A) to use public funds, or private funds in accordance with section 663(c)(11)(B)(ii), to pay some or all of the costs of attendance at a private school\u2014 (I) funds allocated to the State under section 611 may be used by the State to supplement such public or private funds, if the Federal funds are distributed to parents who make a genuine independent choice as to the appropriate school for their child, except that in no case shall the amount of Federal funds provided under this subclause to a parent of a child with a disability for a year exceed the total amount of tuition, fees, and transportation costs for the child for the year; (II) the authorization of a parent to exercise this option fulfills the State's obligation under paragraph (1) with respect to the child during the period in which the child is enrolled in the selected school; and (III) a selected school accepting such funds shall not be required to carry out any of the requirements of this title with respect to such child. .\n##### (b) Research and innovation To improve services and results for children with disabilities\nSection 663(c) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1463(c) ) is amended\u2014\n**(1)**\nin paragraph (9), by striking and after the semicolon;\n**(2)**\nin paragraph (10), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(11) supporting the post-award planning and design, and the initial implementation (which may include costs for informing the community, acquiring necessary equipment and supplies, and other initial operational costs), during a period of not more than 3 years, of State programs that allow the parent of a child with a disability to make a genuine independent choice of the appropriate public or private school for their child, if the program\u2014 (A) requires that the child be a child who has received an initial evaluation described in section 614(a) and has been identified as a child with a disability, in accordance with part B; (B) (i) permits the parent to receive from the State funds to be used to pay some or all of the costs of attendance at the selected school (which may include tuition, fees, and transportation costs); or (ii) permits persons to receive a State tax credit for donations to an entity that provides funds to parents of eligible students described in subparagraph (A), to be used by the parents to pay some or all of the costs of attendance at the selected school (which may include tuition, fees, and transportation costs); (C) prohibits any school that agrees to participate in the program from discriminating against eligible students on the basis of race, color, national origin, or sex, except that\u2014 (i) the prohibition of sex discrimination shall not apply to a participating school that is operated by, supervised by, controlled by, or connected to a religious organization to the extent that the application of such prohibition is inconsistent with the religious tenets or beliefs of the school; and (ii) notwithstanding this subparagraph or any other provision of law, a parent may choose, and a school may offer, a single-sex school, class, or activity; (D) notwithstanding any other provision of law, allows any school participating in the program that is operated by, supervised by, controlled by, or connected to, a religious organization to exercise its right in matters of employment consistent with title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ), including the exemptions in that title; (E) allows a school to participate in the program without, consistent with the First Amendment of the Constitution of the United States\u2014 (i) necessitating any change in the participating school's teaching mission; (ii) requiring any private participating school to remove religious art, icons, scriptures, or other symbols; or (iii) precluding any private participating school from retaining religious terms in its name, selecting its board members on a religious basis, or including religious references in its mission statements and other chartering or governing documents; and (F) requires a participating school selected for a child with a disability to be\u2014 (i) accredited, licensed, or otherwise operating in accordance with State law; and (ii) academically accountable to the parent for meeting the educational needs of the student. .\nIII\nMilitary scholarships\n#### 301. Purpose\nThe purpose of this title is to ensure high-quality education for children of military personnel who live on military installations and thus have less freedom to exercise school choice for their children, in order to improve the ability of the Armed Forces to retain such military personnel.\n#### 302. Military scholarship program\n##### (a) Definitions\nIn this section:\n**(1) ESEA definitions**\nThe terms child , elementary school , secondary school , and local educational agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Eligible military student**\nThe term eligible military student means a child who\u2014\n**(A)**\nis a military dependent student;\n**(B)**\nlives on a military installation selected to participate in the program under subsection (b)(2); and\n**(C)**\nchooses to attend a participating school, rather than a school otherwise assigned to the child.\n**(3) Military dependent students**\nThe term military dependent students has the meaning given the term in section 572(e) of the National Defense Authorization Act for Fiscal Year 2006 ( 20 U.S.C. 7703b(e) ).\n**(4) Participating school**\nThe term participating school means a public or private elementary school or secondary school that\u2014\n**(A)**\naccepts scholarship funds provided under this section on behalf of an eligible military student for the costs of tuition, fees, or transportation of the eligible military student; and\n**(B)**\nis accredited, licensed, or otherwise operating in accordance with State law.\n**(5) Secretary**\nThe term Secretary means the Secretary of Defense.\n##### (b) Program authorized\n**(1) In general**\nFrom amounts made available under subsection (g) and beginning for the first full school year following the date of enactment of this Act, the Secretary shall carry out a 5-year pilot program to award scholarships to enable eligible military students to attend the public or private elementary schools or secondary schools selected by the eligible military students' parents.\n**(2) Scope of program**\n**(A) In general**\nThe Secretary shall select not less than 5 military installations to participate in the pilot program described in paragraph (1). In making such selection, the Secretary shall choose military installations where eligible military students would most benefit from expanded educational options.\n**(B) Ineligibility**\nA military installation that provides, on its premises, education for all elementary school and secondary school grade levels through one or more Department of Defense dependents' schools shall not be eligible for participation in the program.\n**(3) Amount of scholarships**\n**(A) In general**\nThe annual amount of each scholarship awarded to an eligible military student under this section shall not exceed the lesser of\u2014\n**(i)**\nthe cost of tuition, fees, and transportation associated with attending the participating school selected by the parents of the student; or\n**(ii)**\n**(I)**\nin the case of an eligible military student attending elementary school\u2014\n**(aa)**\n$8,000 for the first full school year following the date of enactment of this Act; or\n**(bb)**\nthe amount determined under subparagraph (B) for each school year following such first full school year; or\n**(II)**\nin the case of an eligible military student attending secondary school\u2014\n**(aa)**\n$12,000 for the first full school year following the date of enactment of this Act; or\n**(bb)**\nthe amount determined under subparagraph (B) for each school year following such first full school year.\n**(B) Adjustment for inflation**\nFor each school year after the first full school year following the date of enactment of this Act, the amounts specified in subclauses (I) and (II) of subparagraph (A)(ii) shall be adjusted to reflect changes for the 12-month period ending the preceding June in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor.\n**(4) Payments to parents**\nThe Secretary shall make scholarship payments under this section to the parent of the eligible military student in a manner that ensures such payments will be used for the payment of tuition, fees, and transportation expenses (if any) in accordance with this section.\n##### (c) Selection of scholarships recipients\n**(1) Random selection**\nIf more eligible military students apply for scholarships under the program under this section than the Secretary can accommodate, the Secretary shall select the scholarship recipients through a random selection process from students who submitted applications by the application deadline specified by the Secretary.\n**(2) Continued eligibility**\n**(A) In general**\nAn individual who is selected to receive a scholarship under the program under this section shall continue to receive a scholarship for each year of the program until the individual\u2014\n**(i)**\ngraduates from secondary school or elects to no longer participate in the program;\n**(ii)**\nexceeds the maximum age for which the State in which the student lives provides a free public education; or\n**(iii)**\nis no longer an eligible military student.\n**(B) Continued participation for military transfers**\n**(i) Transfer to private non-military housing**\nNotwithstanding subparagraph (A)(iii), an individual receiving a scholarship under this section for a school year who meets the requirements of subparagraphs (A) and (C) of subsection (a)(2) and whose family, during such school year, moves into private non-military housing that is not considered to be part of the military installation, shall continue to receive the scholarship for use at the participating school for the remaining portion of the school year.\n**(ii) Transfer to a different military installation**\nNotwithstanding subparagraph (A)(iii), an individual receiving a scholarship under this section for a school year whose family is transferred to a different military installation shall no longer be eligible to receive such scholarship beginning on the date of the transfer. Such individual may apply to participate in any program offered under this section for the new military installation for a subsequent school year, if such individual qualifies as an eligible military student for such school year.\n##### (d) Nondiscrimination and other provisions\n**(1) Nondiscrimination**\nA participating school shall not discriminate against program participants or applicants on the basis of race, color, national origin, or sex.\n**(2) Applicability and single-sex schools, classes, or activities**\n**(A) In general**\nNot\u00adwith\u00adstand\u00ading any other provision of law, the prohibition of sex discrimination in paragraph (1) shall not apply to a participating school that is operated by, supervised by, controlled by, or connected to a religious organization to the extent that the application of paragraph (1) is inconsistent with the religious tenets or beliefs of the school.\n**(B) Single-sex schools, classes, or activities**\nNotwithstanding paragraph (1) or any other provision of law, a parent may choose, and a participating school may offer, a single-sex school, class, or activity.\n**(3) Children with disabilities**\nNothing in this section may be construed to alter or modify the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ).\n**(4) Rules of conduct and other school policies**\nA participating school, including the schools described in subsection (e), may require eligible students to abide by any rules of conduct and other requirements applicable to all other students at the school.\n##### (e) Religiously affiliated schools\n**(1) In general**\nNotwithstanding any other provision of law, a participating school that is operated by, supervised by, controlled by, or connected to, a religious organization may exercise its right in matters of employment consistent with title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. ), including the exemptions in that title.\n**(2) Maintenance of purpose**\nNotwithstanding any other provision of law, funds made available under this title to eligible military students that are received by a participating school, as a result of their parents' choice, shall not, consistent with the First Amendment of the Constitution of the United States\u2014\n**(A)**\nnecessitate any change in the participating school's teaching mission;\n**(B)**\nrequire any private participating school to remove religious art, icons, scriptures, or other symbols; or\n**(C)**\npreclude any private participating school from retaining religious terms in its name, selecting its board members on a religious basis, or including religious references in its mission statements and other chartering or governing documents.\n##### (f) Reports\n**(1) Annual reports**\nNot later than July 30 of the year following the year of the date of enactment of this Act, and each subsequent year through the year in which the final report is submitted under paragraph (2), the Secretary shall prepare and submit to Congress an interim report on the scholarships awarded under the pilot program under this section that includes the content described in paragraph (3) for the applicable school year of the report.\n**(2) Final report**\nNot later than 90 days after the end of the pilot program under this section, the Secretary shall prepare and submit to Congress a report on the scholarships awarded under the program that includes the content described in paragraph (3) for each school year of the program.\n**(3) Content**\nEach annual report under paragraph (1) and the final report under paragraph (2) shall contain\u2014\n**(A)**\nthe number of applicants for scholarships under this section;\n**(B)**\nthe number, and the average dollar amount, of scholarships awarded;\n**(C)**\nthe number of participating schools;\n**(D)**\nthe number of elementary school students receiving scholarships under this section and the number of secondary school students receiving such scholarships; and\n**(E)**\nthe results of a survey, conducted by the Secretary, regarding parental satisfaction with the scholarship program under this section.\n##### (g) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2025 through 2029.\n##### (h) Offset in Department of Education salaries\nNotwithstanding any other provision of law, for fiscal year 2025 and each of the 4 succeeding fiscal years, the Secretary of Education shall return to the Treasury $10,000,000 of the amounts made available to the Secretary for salaries and expenses of the Department of Education for such year.",
      "versionDate": "2025-02-06",
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
        "updateDate": "2025-03-12T15:11:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s487",
          "measure-number": "487",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-04-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s487v00",
            "update-date": "2025-04-04"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Creating Hope and Opportunity for Individuals and Communities through Education Act or the</strong> <strong>CHOICE Act</strong></p><p>This bill expands school choice programs for elementary and secondary school students.</p><p>The bill specifies that a student in the District of Columbia must, in order to qualify for an opportunity scholarship, be currently enrolled, or be enrolled for the next school year, in a public or private elementary or secondary school.</p><p>The bill also authorizes the Department of Education (ED) to award grants to support the design and implementation of state programs that allow the parent of a child with a disability to choose the appropriate public or private school for their child. It also outlines the requirements for program eligibility.</p><p>Further, if the state has established a program that allows parents to use public or private funds to assist with the cost of their child attending a private school, then the state may supplement those funds with federal special education funds.</p><p>Additionally, the Department of Defense must carry out a five-year pilot program to award scholarships to enable military dependent students who live on military installations to attend the public or private elementary or secondary schools their parents choose.</p><p>The bill also requires ED to return to the Treasury specified amounts made available for salaries and expenses.</p>"
        },
        "title": "CHOICE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s487.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Hope and Opportunity for Individuals and Communities through Education Act or the</strong> <strong>CHOICE Act</strong></p><p>This bill expands school choice programs for elementary and secondary school students.</p><p>The bill specifies that a student in the District of Columbia must, in order to qualify for an opportunity scholarship, be currently enrolled, or be enrolled for the next school year, in a public or private elementary or secondary school.</p><p>The bill also authorizes the Department of Education (ED) to award grants to support the design and implementation of state programs that allow the parent of a child with a disability to choose the appropriate public or private school for their child. It also outlines the requirements for program eligibility.</p><p>Further, if the state has established a program that allows parents to use public or private funds to assist with the cost of their child attending a private school, then the state may supplement those funds with federal special education funds.</p><p>Additionally, the Department of Defense must carry out a five-year pilot program to award scholarships to enable military dependent students who live on military installations to attend the public or private elementary or secondary schools their parents choose.</p><p>The bill also requires ED to return to the Treasury specified amounts made available for salaries and expenses.</p>",
      "updateDate": "2025-04-04",
      "versionCode": "id119s487"
    },
    "title": "CHOICE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Hope and Opportunity for Individuals and Communities through Education Act or the</strong> <strong>CHOICE Act</strong></p><p>This bill expands school choice programs for elementary and secondary school students.</p><p>The bill specifies that a student in the District of Columbia must, in order to qualify for an opportunity scholarship, be currently enrolled, or be enrolled for the next school year, in a public or private elementary or secondary school.</p><p>The bill also authorizes the Department of Education (ED) to award grants to support the design and implementation of state programs that allow the parent of a child with a disability to choose the appropriate public or private school for their child. It also outlines the requirements for program eligibility.</p><p>Further, if the state has established a program that allows parents to use public or private funds to assist with the cost of their child attending a private school, then the state may supplement those funds with federal special education funds.</p><p>Additionally, the Department of Defense must carry out a five-year pilot program to award scholarships to enable military dependent students who live on military installations to attend the public or private elementary or secondary schools their parents choose.</p><p>The bill also requires ED to return to the Treasury specified amounts made available for salaries and expenses.</p>",
      "updateDate": "2025-04-04",
      "versionCode": "id119s487"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s487is.xml"
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
      "updateDate": "2025-03-12T02:23:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CHOICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Hope and Opportunity for Individuals and Communities through Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand opportunity through greater choice in education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:46Z"
    }
  ]
}
```
