# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6375?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6375
- Title: 21st Century STEM for Girls and Underrepresented Minorities Act
- Congress: 119
- Bill type: HR
- Bill number: 6375
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-04-06T20:29:56Z
- Update date including text: 2026-04-06T20:29:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6375",
    "number": "6375",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "21st Century STEM for Girls and Underrepresented Minorities Act",
    "type": "HR",
    "updateDate": "2026-04-06T20:29:56Z",
    "updateDateIncludingText": "2026-04-06T20:29:56Z"
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
      "text": "Referred to the House Committee on Education and Workforce.",
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
          "date": "2025-12-03T15:02:20Z",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "DC"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MO"
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
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OH"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NM"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6375ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6375\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mrs. Beatty (for herself, Mrs. McIver , Mr. Lynch , Mr. Johnson of Georgia , Ms. Norton , Mr. Bell , Ms. Lee of Pennsylvania , Mr. Foster , Ms. Brown , and Mrs. Grijalva ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to provide grants to local educational agencies to encourage girls and underrepresented minorities to pursue studies and careers in STEM fields.\n#### 1. Short title\nThis Act may be cited as the 21st Century STEM for Girls and Underrepresented Minorities Act .\n#### 2. Grants to prepare girls and underrepresented minorities\nTitle IV of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7101 et seq. ) is amended by adding at the end the following:\nG Preparing girls and underrepresented minorities for the 21st century 4701. Program authority (a) In General Beginning not later than 90 days after the date of the enactment of this part, the Secretary shall carry out a program under which the Secretary makes grants to qualified local educational agencies, on a competitive basis, to pay the costs of carrying out STEM education activities for girls and underrepresented minorities as described in subsection (c). (b) Application (1) In general To be eligible to receive a grant under this part, a qualified local educational agency shall submit to the Secretary an application at such time, in such form, and containing such information as the Secretary may reasonably require. At minimum, the application shall include a description of the following: (A) The educational program that will be carried out by the local educational agency using the grant, including the content of the program and the research and models used to design the program. (B) How elementary and secondary schools served by the agency will collaborate to fulfill goals of the program. (C) How the agency will ensure that there is a comprehensive plan to improve STEM education for girls and underrepresented minorities in grades kindergarten through grade 12. (D) The process that will be used for the recruitment and selection of students for participation in the program. (E) The instructional and motivational activities that will be included as part of the program. (F) Any expected collaboration among local, regional, or national institutions and organizations for the purpose of fulfilling the goals of the program. (2) Priority In selecting among applications, the Secretary shall give priority to qualified local educational agencies that partner or coordinate, to the extent practicable, with local, regional, or national institutions and organizations that have extensive experience and expertise in\u2014 (A) increasing the participation of girls or underrepresented minorities in STEM fields; or (B) conducting research on methods to increase such participation. (c) Use of funds A qualified local educational agency that receives a grant under this part shall use the grant to carry out a STEM education program for girls and underrepresented minorities from elementary and secondary schools served by the agency. The program may include the following activities: (1) Preparing girls and underrepresented minorities for careers in STEM fields and the advantages of pursuing careers in such fields. (2) Educating the parents of girls and underrepresented minorities about the opportunities and advantages of STEM careers. (3) Enlisting the help of the parents of girls and underrepresented minorities\u2014 (A) to overcome the obstacles faced by such groups; and (B) to encourage their child\u2019s continued interest and involvement in STEM subjects. (4) Providing tutoring and mentoring programs in STEM subjects. (5) Establishing partnerships and other opportunities that expose girls and underrepresented minorities to role models in the STEM fields. (6) Enabling female and underrepresented minority students and their teachers to attend events and academic programs in STEM subjects. (7) Providing after school activities designed to encourage interest and develop the skills of girls and underrepresented minorities in STEM subjects. (8) Summer programs designed to help girls and underrepresented minorities\u2014 (A) develop an interest in STEM subjects; (B) develop skills in such subjects; and (C) understand the relevance and significance of such subjects. (9) Purchasing\u2014 (A) educational instructional materials or software designed to help girls and underrepresented minorities develop an interest in STEM subjects; or (B) equipment, instrumentation, or hardware for teaching STEM subjects to girls and underrepresented minorities and encouraging their interest in such subjects. (10) Field trips to locations, including institutions of higher education, to expose girls and underrepresented minorities to STEM activities, encourage their interest in such activities, and acquaint them with careers in STEM fields. (11) Providing academic advice and assistance in high school course selection to encourage girls and underrepresented minorities to take advanced courses in STEM subjects. (12) Paying up to 50 percent of the cost of an internship in a STEM discipline for female and underrepresented minority students. (13) Providing professional development for teachers and other school personnel, including with respect to\u2014 (A) eliminating gender and racial bias in the classroom; (B) sensitivity to gender and racial differences; (C) engaging students in the face of gender-based and racial peer pressure and parental expectations; (D) creating and maintaining a positive environment; and (E) encouraging girls and underrepresented minorities through academic advice and assistance to pursue advanced classes and careers in STEM fields. (14) Such other STEM-related activities as the local educational agency determines to be appropriate. (d) Grant duration and amount (1) Duration Each grant under this section shall be made for a period of 4 years. (2) Amount The amount of each grant under this section shall be $250,000 for each year of the grant period. (e) Supplement, not supplant A qualified local educational agency that receives a grant under this section shall use the grant only to supplement, and not to supplant, other assistance and funds made available from non-Federal sources for the activities supported by the grant. (f) Annual evaluations (1) Evaluation required Not later than 30 days after last day of each school year for which a qualified local educational agency receives a grant under this section, the agency shall submit to the Secretary a written evaluation of the program carried out using the grant. (2) Elements The evaluation required under subsection (a) shall include\u2014 (A) a description of the program and activities carried out using the grant; (B) a description of the curriculum and any partnerships developed using the grant; (C) the percentage of time that students who participated in the program spent directly engaged in STEM activities; (D) an assessment of the academic progress made by such students during the program, which shall be based on an evaluation of each student at the beginning of the program and after the student completes the program; and (E) such other information as the Secretary may require. (g) Definitions In this section: (1) The term STEM means science, technology, engineering, and mathematics. (2) The term qualified local educational agency means a local agency that\u2014 (A) receives funds under part A of title I; and (B) serves a total student population of which not less than 40 percent are children who are eligible for a free or reduced price lunch under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ). 4702. Authorization of appropriations There are authorized to be appropriated to carry out this part $10,000,000 for each of fiscal years 2026 through 2029. .",
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
        "actionDate": "2025-12-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3340",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "21st Century STEM for Girls and Underrepresented Minorities Act",
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
        "updateDate": "2026-01-05T16:12:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-03",
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
          "measure-id": "id119hr6375",
          "measure-number": "6375",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6375v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-12-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>21st Century STEM for Girls and Underrepresented Minorities Act</strong></p><p>This bill directs the Department of Education to make grants to local educational agencies to pay the costs of carrying out science, technology, engineering, and mathematics (STEM)\u00a0education activities for girls and underrepresented minorities.</p>"
        },
        "title": "21st Century STEM for Girls and Underrepresented Minorities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6375.xml",
    "summary": {
      "actionDate": "2025-12-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>21st Century STEM for Girls and Underrepresented Minorities Act</strong></p><p>This bill directs the Department of Education to make grants to local educational agencies to pay the costs of carrying out science, technology, engineering, and mathematics (STEM)\u00a0education activities for girls and underrepresented minorities.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6375"
    },
    "title": "21st Century STEM for Girls and Underrepresented Minorities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>21st Century STEM for Girls and Underrepresented Minorities Act</strong></p><p>This bill directs the Department of Education to make grants to local educational agencies to pay the costs of carrying out science, technology, engineering, and mathematics (STEM)\u00a0education activities for girls and underrepresented minorities.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6375"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6375ih.xml"
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
      "title": "To amend the Elementary and Secondary Education Act of 1965 to provide grants to local educational agencies to encourage girls and underrepresented minorities to pursue studies and careers in STEM fields.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:28:12Z"
    },
    {
      "title": "21st Century STEM for Girls and Underrepresented Minorities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "21st Century STEM for Girls and Underrepresented Minorities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:20Z"
    }
  ]
}
```
