# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7890?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7890
- Title: Science of Reading Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7890
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-02T18:31:22Z
- Update date including text: 2026-04-02T18:31:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 0.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7890",
    "number": "7890",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Science of Reading Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T18:31:22Z",
    "updateDateIncludingText": "2026-04-02T18:31:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
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
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
            "date": "2026-03-17T19:30:07Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-12T13:30:45Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7890ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7890\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mrs. Houchin (for herself, Mr. Mannion , and Mr. Kiley of California ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to exclude certain instructional approaches from comprehensive literacy instruction, to prioritize certain funds to promote the use of evidence-based literacy instruction and supports aligned to the science of reading, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Science of Reading Act of 2026 .\n#### 2. Promoting reading instruction aligned to science of reading\n##### (a) Comprehensive literacy instruction\nSection 2221(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6641(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (K), by striking ; and and inserting a semicolon;\n**(B)**\nin subparagraph (L), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(M) does not include the use of a three-cueing model. ; and\n**(2)**\nby adding at the end the following:\n(4) Science of reading The term science of reading means an interdisciplinary body of evidence-based research about reading and issues related to reading and writing that\u2014 (A) identifies instruction in phonemic awareness, phonics, vocabulary, fluency, comprehension, and writing as essential components to skilled reading; (B) demonstrates the importance of background knowledge, oral language, the connection between reading and writing, and strong writing instruction; (C) explains why some students have difficulty with reading and writing; and (D) does not use a three-cueing model. (5) Three-cueing model The term three-cueing model means an instructional approach or model that\u2014 (A) uses meaning drawn from context, pictures, or syntax as the primary basis for teaching word recognition (commonly referred to as meaning, structure and syntax, and visual cues or MSV ); or (B) teaches visual memory as the primary basis for word recognition. .\n##### (b) State applications for comprehensive literacy State development grants\nSection 2222(d)(2) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6642(d)(2) ) is amended by inserting at the end\u2014\n(F) A description of the extent to which the State comprehensive literacy instruction plan is aligned to the science of reading. .\n##### (c) Comprehensive literacy state development grant priority\nSection 2222(e) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6642(e) ) is amended by striking the period at the end and inserting , that are aligned to the science of reading. .\n##### (d) Comprehensive literacy state development subgrant priority\n**(1) Birth through kindergarten entry**\nSection 2223(c) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6643(c) ) is amended\u2014\n**(A)**\nby striking grants and inserting subgrants ;\n**(B)**\nby striking grant and inserting subgrant ; and\n**(C)**\nby striking the period at the end and inserting , that are aligned to the science of reading. .\n**(2) Kindergarten through grade 12**\nSection 2224(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6644(b) ) is amended\u2014\n**(A)**\nby striking grants and inserting subgrants ; and\n**(B)**\nby striking the period at the end and inserting that are aligned to the science of reading. .\n#### 3. General provisions\n##### (a) Applicability\nThis Act and the amendments made by this Act shall apply with respect to funds awarded under the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 note et seq.) on or after the date of the enactment of this Act.\n##### (b) Rules of construction\nNothing in this Act or the amendments made by this Act shall be construed to\u2014\n**(1)**\nlimit or alter the rights, protections, and individualized instructional requirements under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), or the Americans with Disabilities Act ( 42 U.S.C. 12101 et seq. ); or\n**(2)**\nauthorize any officer or employee of the Federal Government to mandate, direct, or control a State, local educational agency, or school\u2019s specific instructional content, academic standards and assessments, curricula, or program of instruction.",
      "versionDate": "2026-03-12",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Education programs funding",
            "updateDate": "2026-04-02T18:31:21Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-04-02T18:31:15Z"
          },
          {
            "name": "Language arts",
            "updateDate": "2026-04-02T18:31:10Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2026-04-02T18:31:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-03-16T16:23:16Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7890ih.xml"
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
      "title": "Science of Reading Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Science of Reading Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to exclude certain instructional approaches from comprehensive literacy instruction, to prioritize certain funds to promote the use of evidence-based literacy instruction and supports aligned to the science of reading, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T08:19:25Z"
    }
  ]
}
```
