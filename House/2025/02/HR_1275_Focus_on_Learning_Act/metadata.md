# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1275?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1275
- Title: Focus on Learning Act
- Congress: 119
- Bill type: HR
- Bill number: 1275
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-05-14T23:56:20Z
- Update date including text: 2026-05-14T23:56:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1275",
    "number": "1275",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000821",
        "district": "4",
        "firstName": "Bruce",
        "fullName": "Rep. Westerman, Bruce [R-AR-4]",
        "lastName": "Westerman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Focus on Learning Act",
    "type": "HR",
    "updateDate": "2026-05-14T23:56:20Z",
    "updateDateIncludingText": "2026-05-14T23:56:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:00:15Z",
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
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CO"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "RI"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1275ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1275\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Westerman (for himself, Mr. Stauber , Ms. Morrison , and Mr. Crow ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Surgeon General to conduct a study regarding the use of mobile devices in elementary and secondary schools, and to establish a pilot program of awarding grants to enable certain schools to create a school environment free of mobile devices.\n#### 1. Short title\nThis Act may be cited as the Focus on Learning Act .\n#### 2. Definitions\nIn this Act:\n**(1) ESEA terms**\nThe terms child with a disability , elementary school , English learner , local educational agency , and secondary school have the meaning given those terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Mobile device**\nThe term mobile device means any personal mobile telephone or other portable electronic communication device with which a user engages in a call or writes or sends a message or any device in which the user plays a game or watches a video, except that such term does not include school-issued devices.\n**(3) School environment free of mobile devices**\nThe term school environment free of mobile devices means an elementary school or secondary school in which mobile devices of students are kept in a secure container that is controlled by a school administrator.\n**(4) School hours**\nThe term school hours means regular school hours for instruction, including lunch periods, free periods on school grounds, and time between classroom instruction.\n#### 3. Study\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Surgeon General, in consultation with the Secretary of Health and Human Services, shall complete a study regarding the use of mobile devices in elementary schools and secondary schools nationwide, including\u2014\n**(1)**\nthe impact of such use on\u2014\n**(A)**\nstudent learning and academic achievement;\n**(B)**\nstudent educational outcomes and engagement;\n**(C)**\nstudent mental health;\n**(D)**\nclassroom instruction; and\n**(E)**\nschool climate and student behavior; and\n**(2)**\nan analysis of data collected from participating schools in the pilot program under section 4.\n##### (b) Report\nThe Surgeon General, in consultation with the Secretary of Health and Human Services, shall submit a report to Congress containing the results of the study conducted under subsection (a), and shall make such report publicly available.\n#### 4. Pilot program\n##### (a) Program established\nThe Secretary of Education, in consultation with the Secretary of Health and Human Services, shall establish a pilot program, through which the Secretary of Education, in consultation with the Secretary of Health and Human Services, shall award grants to local educational agencies to enable participating schools served by such agencies (referred to in this section as participating schools ) to purchase secure containers and install lockers in order to create a school environment free of mobile devices.\n##### (b) Application\nA local educational agency desiring to participate in the program under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may reasonably require, including\u2014\n**(1)**\nan assurance that such local educational agency will identify and select participating schools in a manner that engages the students, parents, educators, principal, school leaders, and specialized instructional support personnel, of such schools;\n**(2)**\nan assurance that each participating school will have a communication system (which may be mobile devices) allowing teachers, administrators, and staff to communicate with each other and with local emergency responders;\n**(3)**\nan assurance that each participating school will have a clear process for students to be able to contact their parents;\n**(4)**\nthe policy of each participating school on mobile device use during school hours as of the date of the application; and\n**(5)**\na description of what each participating school's new policy on mobile device use during school hours will be upon beginning participation in the pilot program under this section.\n##### (c) Selection\nThe Secretary of Education, in consultation with the Secretary of Health and Human Services, shall select local educational agency applicants for participation in the pilot program based on the Secretary of Education's determination that the applicant\u2019s participation will likely yield helpful information relevant to testing a school environment free of mobile devices.\n##### (d) Exemptions\nParticipating schools may, while maintaining a school environment free of mobile devices, allow exemptions such that mobile devices may be used during school hours\u2014\n**(1)**\nto monitor or treat health conditions;\n**(2)**\nby students who are children with disabilities; and\n**(3)**\nby students who are English learners for translation purposes.\n##### (e) Parental notification\nEach local educational agency that applies for participation in the pilot program under this section shall\u2014\n**(1)**\nnotify parents of students enrolled in elementary schools and secondary schools that are served by the agency and that may become participating schools\u2014\n**(A)**\nnot less than 30 days before submitting an application under this section; and\n**(B)**\nupon receipt of a grant award under this section; and\n**(2)**\nsolicit feedback from such parents before applying for the grant about the local educational agency's desire to implement a school environment free of mobile devices.\n##### (f) Administrative expenses\nThe Secretary of Education and the Secretary of Health and Human Services may use not more than 2 percent of the amounts made available to carry out this section for administrative expenses, data collection, and carrying out the study required under section 3.\n##### (g) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section, $5,000,000 for the period of fiscal years 2025 through 2029.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "404",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Focus on Learning Act",
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
            "updateDate": "2025-05-30T19:22:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-30T19:22:45Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2025-05-30T19:22:45Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-05-30T19:22:45Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-30T19:22:45Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-05-30T19:22:45Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-05-30T19:22:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-17T14:15:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1275",
          "measure-number": "1275",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1275v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Focus on Learning Act</strong></p><p>This bill requires certain federal actions to address the use of mobile devices in elementary and secondary schools.</p><p>First, the bill directs the Office of the Surgeon General, in consultation with the Department of Health and Human Services (HHS), to study and report on the use of mobile devices in elementary and secondary schools nationwide. Among other elements, this study must include the impact of mobile device use on student learning and academic achievement, student educational outcomes, and student mental health.</p><p>Second, the Department of Education, in consultation with HHS, must establish a pilot program to award grants to local educational agencies (LEAs) to enable participating schools served by such LEAs to purchase secure containers and install lockers in order to create a school environment free of mobile devices.</p>"
        },
        "title": "Focus on Learning Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1275.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Focus on Learning Act</strong></p><p>This bill requires certain federal actions to address the use of mobile devices in elementary and secondary schools.</p><p>First, the bill directs the Office of the Surgeon General, in consultation with the Department of Health and Human Services (HHS), to study and report on the use of mobile devices in elementary and secondary schools nationwide. Among other elements, this study must include the impact of mobile device use on student learning and academic achievement, student educational outcomes, and student mental health.</p><p>Second, the Department of Education, in consultation with HHS, must establish a pilot program to award grants to local educational agencies (LEAs) to enable participating schools served by such LEAs to purchase secure containers and install lockers in order to create a school environment free of mobile devices.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr1275"
    },
    "title": "Focus on Learning Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Focus on Learning Act</strong></p><p>This bill requires certain federal actions to address the use of mobile devices in elementary and secondary schools.</p><p>First, the bill directs the Office of the Surgeon General, in consultation with the Department of Health and Human Services (HHS), to study and report on the use of mobile devices in elementary and secondary schools nationwide. Among other elements, this study must include the impact of mobile device use on student learning and academic achievement, student educational outcomes, and student mental health.</p><p>Second, the Department of Education, in consultation with HHS, must establish a pilot program to award grants to local educational agencies (LEAs) to enable participating schools served by such LEAs to purchase secure containers and install lockers in order to create a school environment free of mobile devices.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119hr1275"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1275ih.xml"
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
      "title": "Focus on Learning Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Focus on Learning Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Surgeon General to conduct a study regarding the use of mobile devices in elementary and secondary schools, and to establish a pilot program of awarding grants to enable certain schools to create a school environment free of mobile devices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:34:05Z"
    }
  ]
}
```
