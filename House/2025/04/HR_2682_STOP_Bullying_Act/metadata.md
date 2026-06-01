# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2682?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2682
- Title: STOP Bullying Act
- Congress: 119
- Bill type: HR
- Bill number: 2682
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2682",
    "number": "2682",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "STOP Bullying Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:02:25Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "DC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "WA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "IL"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2682ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2682\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Krishnamoorthi (for himself, Mr. Khanna , Ms. Norton , Mr. Tonko , Mr. Soto , and Ms. Sherrill ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to establish a grant program that will support efforts at the State level to establish anti-bullying task forces to study, address, and reduce bullying in elementary and secondary schools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the STOP Bullying Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nNearly 1-in-5 K\u201312 students have reported being bullied at school, accounting for more than 10,000,000 students across the country.\n**(2)**\nSince most instances of bullying take place on school grounds, school staff and teachers play an instrumental role in bullying prevention.\n**(3)**\nAccording to the NCES, 68 percent of grade 6\u201312 students who are bullied face repeated incidents over multiple days, and many have reported negative impacts on their physical health as a result of being bullied at school.\n**(4)**\nResearch shows that engaged educators who are supportive of all students help to reduce the overall presence of bullying and harassment on school grounds.\n**(5)**\nMarginalized students face high rates of bullying, with studies showing that 71 percent of Jewish families have experienced antisemitism at school, 78 percent of Sikh students have been bullied at school, 83 percent of LGBTQ+ students have been harassed or assaulted at school, and 44 percent of teenagers with developmental disabilities have been bullied at school.\n**(6)**\nHostile school environments have a detrimental effect on the academic success and health of students.\n**(7)**\n56 percent of bullying incidents are never reported to an adult, inhibiting school systems in addressing hostile environments and supporting the well-being of all students.\n**(8)**\nGovernments and educators in every State have a responsibility to ensure State and local education systems have processes in place for students to be able to learn in a safe environment, regardless of their actual or perceived race, color, national origin, sex, disability, sexual orientation, gender identity, or religion.\n#### 3. State Anti-Bullying Task Force Requirement\nSubpart 2 of part F of title VIII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7881 et seq. ) is amended by adding at the end the following:\n8549D. State Anti-Bullying Task Force Grants (a) Anti-Bullying Task Force Grant Program The Secretary shall carry out a program to make grants to each State to establish and implement a task force to study, address, and reduce bullying in elementary schools and secondary schools. (b) Use of funds Each State task force established under a grant under this section shall use the grant funds to conduct a study on bullying in the elementary schools and secondary schools of such State that includes\u2014 (1) policies of the local educational agencies in such State with respect to bullying; (2) teacher, parent, and student education with respect to bullying; and (3) the incidents of student violence and self-harm as a result of bullying. (c) Membership (1) Chair Each Chief Education Officer of a State shall designate one individual to serve as the chair of the task force of such State. (2) Composition Each State shall designate at least one individual from each of the following categories to serve on the task force of such State: (A) At least one teacher at elementary schools and secondary schools selected in consultation with the union or association representing educators. (B) At least one school administrator. (C) At least one parent of students. (D) At least one K\u201312 student. (E) At least one guidance counselor. (F) At least one child psychologist. (G) At least one school psychologist. (H) At least one paraprofessional. (I) At least one lawyer. (J) At least one representative from a community-based organization who specializes in providing supportive services to students who identify as lesbian, gay, bisexual, transgender, or queer. (K) Professionals who specialize in providing support services to students who identify as lesbian, gay, bisexual, transgender, or queer. (L) At least one individual from the State Education Agency office focused on school improvement and school climate. (M) Additional individuals, as determined by the chair of the task force. (3) Terms of members (A) In general Each member of a task force of State shall be appointed for the duration of the existence of such task force. (B) Vacancies A vacancy on a task force shall be filled in the manner in which the original designation was made under paragraph (2). (4) Discretionary coordination A task force of a State may coordinate activities under this section with other boards and commissions of such State. (d) Report to Chief Education Officer (1) In general Not later than 1 year after the date on which the State submits the study required under subsection (b), the State task force of such State shall submit a final report to the Chief Education Officer of such State and the Secretary of Education containing\u2014 (A) the annual findings and conclusions of the task force; (B) the recommendations of the task force for legislation or administrative actions; and (C) best practices with respect to bullying in elementary schools and secondary schools that includes recommendations for how\u2014 (i) to address and reduce bullying; (ii) to best educate all relevant school staff on recognizing bullying; and (iii) parents can best address and discuss with their children the early warning signs of bullying. (2) Publication Each State task force shall make the final report submitted under paragraph (1) publicly available. .",
      "versionDate": "2025-04-07",
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
        "name": "Education",
        "updateDate": "2025-05-02T12:42:12Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2682ih.xml"
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
      "title": "STOP Bullying Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP Bullying Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to establish a grant program that will support efforts at the State level to establish anti-bullying task forces to study, address, and reduce bullying in elementary and secondary schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:25Z"
    }
  ]
}
```
