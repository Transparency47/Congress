# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6973?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6973
- Title: COURSE Credit Act
- Congress: 119
- Bill type: HR
- Bill number: 6973
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-01-26T14:40:16Z
- Update date including text: 2026-01-26T14:40:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-07 - IntroReferral: Sponsor introductory remarks on measure. (CR H606)
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-07 - IntroReferral: Sponsor introductory remarks on measure. (CR H606)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6973",
    "number": "6973",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "COURSE Credit Act",
    "type": "HR",
    "updateDate": "2026-01-26T14:40:16Z",
    "updateDateIncludingText": "2026-01-26T14:40:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-07",
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
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H606)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:01:05Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NJ"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "PR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6973ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6973\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Mr. Subramanyam (for himself, Mr. Van Drew , Mr. Walkinshaw , and Mr. Hern\u00e1ndez ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to collect and report information on the treatment of Advanced Placement and International Baccalaureate course credits at institutions of higher education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Creating Opportunities to Use Received Student Exam Credit Act or the COURSE Credit Act .\n#### 2. Data collection and reporting by Department of Education\n##### (a) In general\nThe Secretary of Education shall collect and annually report on the College Scorecard website (or any successor website) information regarding the treatment of Advanced Placement and International Baccalaureate course credits by institutions of higher education.\n##### (b) Coordination\nIn carrying out subsection (a), the Secretary of Education shall coordinate with relevant stakeholders within and outside the Department of Education, including the technical review panel of the Integrated Postsecondary Education Data System.\n##### (c) Elements\nThe information reported under subsection (a) shall include, with respect to each institution of higher education, the following:\n**(1)**\nAn explanation of whether the institution provides credits toward a student\u2019s degree for Advanced Placement or International Baccalaureate exam scores.\n**(2)**\nIf the institution does provide such credits, identification of\u2014\n**(A)**\nthe total maximum number of such credits that may be provided to an individual student for a given program of study;\n**(B)**\nthe minimum score a student must earn on an Advanced Placement or International Baccalaureate exam for the institution to provide the credits and, if applicable, whether such minimum score differs based on the subject matter of the exam or the student\u2019s program of study; and\n**(C)**\nthe type of credit provided by the institution for a given exam score, whether it be full course credit, elective credit, or a course exemption, and an explanation of whether the type of credit provided or the score required to receive such credit differs based on the degree program of the student.\n**(3)**\nAny other information with respect to an institution\u2019s policy on the treatment of Advanced Placement and International Baccalaureate course credits that the Secretary of Education considers relevant.\n#### 3. Dissemination of information by institutions\nSection 485(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1092(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (U), by striking and at the end;\n**(B)**\nin subparagraph (V), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(W) institutional policies regarding the treatment of Advanced Placement and International Baccalaureate course credits, including all information required to be published under subsection (n). ; and\n**(2)**\nby adding at the end the following:\n(n) Information on treatment of AP and IB course credits (1) In general Each institution of higher education participating in any program under this title shall publish, in a prominent location on the public website of the institution, information regarding the treatment of Advanced Placement and International Baccalaureate course credits by the institution. Such information shall include\u2014 (A) an explanation of whether the institution provides credits toward a student\u2019s degree for Advanced Placement or International Baccalaureate exam scores; (B) if the institution does provide such credits, identification of\u2014 (i) the total maximum number of such credits that may be provided to an individual student for a given program of study; (ii) the minimum score a student must earn on an Advanced Placement or International Baccalaureate exam for the institution to provide the credits and, if applicable, whether such minimum score differs based on the subject matter of the exam or the student\u2019s program of study; and (iii) the type of credit provided by the institution for a given exam score, whether it be full course credit, elective credit, or a course exemption, and an explanation of whether the type of credit provided or the score required to receive such credit differs based on the degree program of the student; and (C) any other information with respect to the institution\u2019s policy on the treatment of Advanced Placement and International Baccalaureate course credits that the institution considers relevant. (2) Updates The information required to be published under paragraph (1) shall be updated by the institution, as necessary, to ensure it remains accurate and current. .",
      "versionDate": "2026-01-07",
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
        "updateDate": "2026-01-26T14:40:16Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6973ih.xml"
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
      "title": "COURSE Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COURSE Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Opportunities to Use Received Student Exam Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to collect and report information on the treatment of Advanced Placement and International Baccalaureate course credits at institutions of higher education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:35Z"
    }
  ]
}
```
