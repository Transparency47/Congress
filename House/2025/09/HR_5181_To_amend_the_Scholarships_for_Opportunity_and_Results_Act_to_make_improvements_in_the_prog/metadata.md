# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5181
- Title: SOAR Act Improvements Act
- Congress: 119
- Bill type: HR
- Bill number: 5181
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2026-02-20T19:40:08Z
- Update date including text: 2026-02-20T19:40:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 25 - 20.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 25 - 20.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5181",
    "number": "5181",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "F000450",
        "district": "5",
        "firstName": "Virginia",
        "fullName": "Rep. Foxx, Virginia [R-NC-5]",
        "lastName": "Foxx",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "SOAR Act Improvements Act",
    "type": "HR",
    "updateDate": "2026-02-20T19:40:08Z",
    "updateDateIncludingText": "2026-02-20T19:40:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 25 - 20.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
        "item": [
          {
            "date": "2025-09-10T16:40:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-08T16:02:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5181ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5181\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Ms. Foxx introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend the Scholarships for Opportunity and Results Act to make improvements in the program for awarding school choice scholarships to students in the District of Columbia.\n#### 1. Short title\nThis Act may be cited as the SOAR Act Improvements Act .\n#### 2. Grant duration and Applications\n##### (a) Extension of grant duration\nSection 3004(a)(2) of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.04(a)(2), D.C. Official Code) is amended by striking 5 years and inserting 5 years, and may renew such grants for an additional period of not more than 5 years, without a competitive process, when the Secretary determines appropriate and desirable to maintain continuity in the program .\n##### (b) Changes to application content\n**(1) Noninterference in regular admissions standards or procedures**\nSection 3005(b)(1)(C) of such Act (sec. 38\u20131853.05(b)(1)(C), D.C. Official Code) is amended by striking the semicolon at the end and inserting , if such a process will not interfere with the regular admission standards or procedures of the school; .\n**(2) Change to residency requirement of eligible entity board members**\n**(A) In general**\nSection 3005(b)(1)(M) of such Act (sec. 38\u20131853.05(b)(1)(M), D.C. Official Code) is amended by striking District of Columbia and inserting Washington metropolitan region .\n**(B) Washington metropolitan region defined**\nSection 3013 of such Act (sec. 38\u20131853.13, D.C. Official Code) is amended by adding at the end the following:\n(12) Washington metropolitan region The term Washington metropolitan region includes the District of Columbia, the counties of Montgomery and Prince Georges in Maryland, and the counties of Arlington and Fairfax and the cities of Alexandria and Falls Church in Virginia. .\n#### 3. Accreditation requirements\n##### (a) In general\nSection 3007(a)(5)(A) of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.07(a)(5)(A), D.C. Official Code) is amended\u2014\n**(1)**\nby amending clause (i) to read as follows:\n(i) in the case of a school that is a participating school as of the date of enactment of the SOAR Act Improvements Act, is recognized by\u2014 (I) a national or regional accrediting body; or (II) an accrediting body sited by the Student and Visitor Exchange English Language Program administered by U.S. Immigration and Customs Enforcement; and ; and\n**(2)**\nby amending clause (ii) to read as follows:\n(ii) in the case of a school that is not a participating school as of the date of enactment of the SOAR Act Improvements Act, is fully accredited by an accrediting body described under clause (i) not later than 5 years after the date on which that school began the process of pursuing participation under this division. .\n##### (b) Removal of completed report\nSection 3007(a)(5) of such Act (sec. 38\u20131853.07(a)(5), D.C. Official Code) is further amended by striking subparagraph (B) and redesignating subparagraph (C) as subparagraph (B).\n#### 4. Use of funds\n##### (a) Extension of funds for use in pre-Kindergarten\nSection 3007(a)(3)(B)(i)(I) of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.07(a)(3)(B)(i)(I), D.C. Official Code) is amended by striking kindergarten and inserting pre-kindergarten .\n##### (b) Maximum scholarship amount\nSection 3007(a)(3)(B)(ii) of such Act (sec. 38\u20131853.07(a)(3)(B)(ii), D.C. Official Code) is amended by adding at the end the following: In any year, an eligible entity receiving a grant under section 3004(a) has sole authority to establish a maximum scholarship amount less than the amount permitted in (3)(B)(i).\n##### (c) Extension of funds for additional student academic assistance\n**(1) In general**\nSection 3007 of such Act (sec. 38\u20131853.07, D.C. Official Code) is further amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin the heading, by striking and Parental Assistance and inserting , Parental Assistance, and Student Academic Assistance ; and\n**(ii)**\nby adding at the end the following:\n(3) The expenses of providing tutoring service to participating eligible students who need additional academic assistance. If there are insufficient funds to provide tutoring services to all such students in a year, the eligible entity shall give priority in such year to students who previously attended an elementary school or secondary school identified as one of the lowest-performing schools under the District of Columbia\u2019s accountability system. ;\n**(B)**\nby striking subsection (c) and redesignating subsection (d) as subsection (c); and\n**(C)**\nin subsection (c), as so redesignated\u2014\n**(i)**\nin paragraph (2)(B), by striking subsections (b) and (c) and inserting subsection (b) ; and\n**(ii)**\nin paragraph (3), by striking subsections (b) and (c) and inserting subsection (b) .\n**(2) Increase in amount of funds**\nSection 3007(b) of such Act (sec. 38\u20131853.07(b), D.C. Official Code) is further amended in the matter preceding paragraph (1), by striking $2,000,000 and inserting $2,200,000 ;\n**(3) Removal of completed study**\nSection 3007(b)(1) of such Act (sec. 38\u20131853.07(b)(1), D.C. Official Code) is further amended\u2014\n**(A)**\nin subparagraph (E), by striking ; and and inserting a period; and\n**(B)**\nby striking subparagraph (F).\n#### 5. Standardized testing requirements\nSection 3008(h) of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.08(h), D.C. Official Code) is amended\u2014\n**(1)**\nin paragraph (1), by striking section 3009(a)(2)(A)(i) and inserting section 3009(a) ;\n**(2)**\nby amending paragraph (2) to read as follows:\n(2) Administration of tests The Institute of Education Sciences may administer assessments to students participating in the evaluation under section 3009(a) for the purpose of conducting the evaluation under such section. ; and\n**(3)**\nin paragraph (3), by striking the nationally norm-referenced standardized test described in paragraph (2) and inserting a nationally norm-referenced standardized test .\n#### 6. Evaluations\n##### (a) Modification in evaluation frequency\nSection 3009(a)(1)(A) of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.09(a)(1)(A), D.C. Official Code) is amended to read as follows:\n(A) jointly enter into an agreement with the Institute of Education Sciences of the Department of Education to\u2014 (i) conduct an evaluation of the opportunity scholarship program under this division; and (ii) not later than January 1, 2027, and every 7 years thereafter, issue a public report on the opportunity scholarship program under this division. .\n##### (b) Responsibility of Secretary\n**(1) Ensuring evaluations are rigorous**\nSection 3009(a)(2)(A)(i) of such Act (sec. 38\u20131853.09(a)(2)(A)(i), D.C. Official Code) is amended to read as follows:\n(i) is rigorous; and .\n**(2) Ensuring proper information is made public**\nSection 3009(a)(2)(B) of such Act (sec. 38\u20131853.09(a)(2)(B), D.C. Official Code) is amended to read as follows:\n(B) disseminate information on the impact of the program on academic progress and educational attainment. .\n##### (c) Responsibility of Institute of Education Sciences\n**(1) Evaluation of participating eligible students**\nSection 3009(a)(3) of such Act (sec. 38\u20131853.09(a)(3), D.C. Official Code) is amended\u2014\n**(A)**\nby amending subparagraph (A) to read as follows:\n(A) assess the academic progress of participating eligible students who use an opportunity scholarship in each of grades 3 through 8; ; and\n**(B)**\nby striking subparagraph (B) and redesignating subparagraph (C) as subparagraph (B).\n**(2) Technical amendment**\nSection 3009(a)(3) of such Act (sec. 38\u20131853.09(a)(3), D.C. Official Code) is further amended in the heading, by striking on Education and inserting of Education .\n##### (d) Issues To be evaluated\nSection 3009(a)(4) of such Act (sec. 38\u20131853.09(a)(4), D.C. Official Code) is amended\u2014\n**(1)**\nby amending subparagraph (A) to read as follows:\n(A) The academic progress of participating eligible students who use an opportunity scholarship compared to the academic progress of a comparison group of students with similar backgrounds, which may include students in the District of Columbia public schools and the District of Columbia public charter schools. ;\n**(2)**\nin subparagraph (B), by striking increasing the satisfaction of such parents and students with their choice and inserting the satisfaction of those parents and students with the program ;\n**(3)**\nby amending subparagraph (D) to read as follows:\n(D) The high school graduation rates, college enrollment rates, college persistence rates, and college graduation rates of participating eligible students who use an opportunity scholarship compared with the rates of public school students described in subparagraph (A), to the extent practicable. ;\n**(4)**\nby amending subparagraph (E) to read as follows:\n(E) The safety of the schools attended by participating eligible students who use an opportunity scholarship compared with the schools attended by public school students described in subparagraph (A), to the extent practicable. ;\n**(5)**\nby striking subparagraphs (F) and (G); and\n**(6)**\nby redesignating subparagraph (H) as subparagraph (F).\n##### (e) Effective date\nThe amendments made by this section shall apply with respect to evaluations carried out on or after the expiration of the 2-year period beginning on the date of the enactment of this Act.\n#### 7. Report by entity receiving funds\n##### (a) Change to contents of report\nSection 3010 of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.10, D.C. Official Code) is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nby striking subparagraph (A); and\n**(B)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (A) and (B), respectively; and\n**(2)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A), by striking aggregate academic achievement of other participating students at the student\u2019s school in the same grade or level, as appropriate, and the ; and\n**(B)**\nby amending subparagraph (B) to read as follows:\n(B) any incidents of school violence, student suspensions, and student expulsions; and .\n##### (b) Effective date\nThe amendments made this section shall apply with respect to reports submitted for school years beginning on or after the date of the enactment of this Act.\n#### 8. Extension of authorization of appropriation\n##### (a) In general\nSection 3014 of the Scholarships for Opportunity and Results Act (sec. 38\u20131853.14, D.C. Official Code) is amended in subsection (a)\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking through fiscal year 2023 and inserting through fiscal year 2032 ;\n**(2)**\nin paragraph (1), by striking one-third and inserting one-half ; and\n**(3)**\nin paragraph (2), by striking one-third and inserting one-sixth .\n##### (b) Effective date\nThe amendments made by this section shall apply beginning with respect to fiscal year 2024.",
      "versionDate": "2025-09-08",
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
        "actionDate": "2026-01-28",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3710",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SOAR Permanent Authorization Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Academic performance and assessments",
            "updateDate": "2025-09-29T14:02:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-29T14:02:24Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-09-29T14:00:35Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-09-29T14:00:45Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-09-29T14:01:04Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-29T14:02:17Z"
          },
          {
            "name": "Maryland",
            "updateDate": "2025-09-29T14:00:51Z"
          },
          {
            "name": "Preschool education",
            "updateDate": "2025-09-29T14:01:00Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-09-29T14:00:40Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-09-29T14:02:07Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-09-29T14:00:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-09-10T12:10:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-08",
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
          "measure-id": "id119hr5181",
          "measure-number": "5181",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-08",
          "originChamber": "HOUSE",
          "update-date": "2025-12-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5181v00",
            "update-date": "2025-12-09"
          },
          "action-date": "2025-09-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>SOAR Act Improvements Act</strong></p><p>This bill reauthorizes through FY2032 and modifies the District of Columbia (DC) Opportunity Scholarship Program, which is a federal program that funds private school scholarships for low-income students in\u00a0DC.</p><p>Under\u00a0the program, the Department of Education (ED) issues grants to nonprofit organizations to pay for income-qualified DC residents to attend DC private elementary or secondary schools of their choice. The bill expands the program to include pre-kindergarten students and authorizes ED to renew grants for up to five years without a new application.\u00a0</p><p>Current law requires nonprofits to ensure that if more scholarship students apply to a particular school than the school can accommodate, students will be randomly selected for admission. The bill specifies that this only applies if random selection would not interfere with the school's regular admission standards or procedures.</p><p>Current law also requires schools to be properly accredited\u00a0in order to participate in the program (i.e., enroll scholarship students). The bill authorizes a nonparticipating school to enroll scholarship students provided it obtains accreditation within five years of\u00a0first pursuing participation in the program.</p><p>The bill also makes other administrative changes to the program, including (1) authorizing the majority of voting members of a nonprofit\u2019s board to live in the DC metropolitan area, rather than in DC itself; (2)\u00a0removing a cap on the use of funds for tutoring students; and (3) directing ED and the mayor of DC to periodically evaluate and publicly report on the program.</p>"
        },
        "title": "SOAR Act Improvements Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5181.xml",
    "summary": {
      "actionDate": "2025-09-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SOAR Act Improvements Act</strong></p><p>This bill reauthorizes through FY2032 and modifies the District of Columbia (DC) Opportunity Scholarship Program, which is a federal program that funds private school scholarships for low-income students in\u00a0DC.</p><p>Under\u00a0the program, the Department of Education (ED) issues grants to nonprofit organizations to pay for income-qualified DC residents to attend DC private elementary or secondary schools of their choice. The bill expands the program to include pre-kindergarten students and authorizes ED to renew grants for up to five years without a new application.\u00a0</p><p>Current law requires nonprofits to ensure that if more scholarship students apply to a particular school than the school can accommodate, students will be randomly selected for admission. The bill specifies that this only applies if random selection would not interfere with the school's regular admission standards or procedures.</p><p>Current law also requires schools to be properly accredited\u00a0in order to participate in the program (i.e., enroll scholarship students). The bill authorizes a nonparticipating school to enroll scholarship students provided it obtains accreditation within five years of\u00a0first pursuing participation in the program.</p><p>The bill also makes other administrative changes to the program, including (1) authorizing the majority of voting members of a nonprofit\u2019s board to live in the DC metropolitan area, rather than in DC itself; (2)\u00a0removing a cap on the use of funds for tutoring students; and (3) directing ED and the mayor of DC to periodically evaluate and publicly report on the program.</p>",
      "updateDate": "2025-12-09",
      "versionCode": "id119hr5181"
    },
    "title": "SOAR Act Improvements Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>SOAR Act Improvements Act</strong></p><p>This bill reauthorizes through FY2032 and modifies the District of Columbia (DC) Opportunity Scholarship Program, which is a federal program that funds private school scholarships for low-income students in\u00a0DC.</p><p>Under\u00a0the program, the Department of Education (ED) issues grants to nonprofit organizations to pay for income-qualified DC residents to attend DC private elementary or secondary schools of their choice. The bill expands the program to include pre-kindergarten students and authorizes ED to renew grants for up to five years without a new application.\u00a0</p><p>Current law requires nonprofits to ensure that if more scholarship students apply to a particular school than the school can accommodate, students will be randomly selected for admission. The bill specifies that this only applies if random selection would not interfere with the school's regular admission standards or procedures.</p><p>Current law also requires schools to be properly accredited\u00a0in order to participate in the program (i.e., enroll scholarship students). The bill authorizes a nonparticipating school to enroll scholarship students provided it obtains accreditation within five years of\u00a0first pursuing participation in the program.</p><p>The bill also makes other administrative changes to the program, including (1) authorizing the majority of voting members of a nonprofit\u2019s board to live in the DC metropolitan area, rather than in DC itself; (2)\u00a0removing a cap on the use of funds for tutoring students; and (3) directing ED and the mayor of DC to periodically evaluate and publicly report on the program.</p>",
      "updateDate": "2025-12-09",
      "versionCode": "id119hr5181"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5181ih.xml"
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
      "title": "SOAR Act Improvements Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SOAR Act Improvements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Scholarships for Opportunity and Results Act to make improvements in the program for awarding school choice scholarships to students in the District of Columbia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T08:18:28Z"
    }
  ]
}
```
