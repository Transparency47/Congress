# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5584?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5584
- Title: LIFT AI Act
- Congress: 119
- Bill type: HR
- Bill number: 5584
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-05-21T08:07:34Z
- Update date including text: 2026-05-21T08:07:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5584",
    "number": "5584",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000398",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
        "lastName": "Kean",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "LIFT AI Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:34Z",
    "updateDateIncludingText": "2026-05-21T08:07:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "RI"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CO"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sponsorshipDate": "2026-05-20",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5584ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5584\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Kean (for himself and Mr. Amo ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo improve educational efforts related to artificial intelligence literacy at the K through 12 level, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Literacy in Future Technologies Artificial Intelligence Act or the LIFT AI Act .\n#### 2. Preparing k\u201312 educators and students for an ai literate future\n##### (a) Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nartificial intelligence (AI) is rapidly transforming the modern world, driving innovation across industries, enhancing productivity, and reshaping the way we live and work;\n**(2)**\nto ensure the United States remains a global leader in this technological revolution, the United States should provide the Nation\u2019s youth with opportunities to cultivate the skills and understanding necessary to use and create the next generation of AI technology;\n**(3)**\nit is the policy of the United States to promote AI literacy and proficiency among Americans by promoting the appropriate integration of AI into education, providing comprehensive AI training for educators, and fostering early exposure to AI concepts and technology to develop an AI-ready workforce and the next generation of American AI innovators;\n**(4)**\nas strategic adversaries pursue AI technology for the purposes of surveillance, weaponization, and economic competition, maintaining United States leadership through an AI literate public is essential; and\n**(5)**\nawards made under this section should recognize\u2014\n**(A)**\nthe rapidly evolving nature of AI technology, and identify and focus on those skills that will remain relevant to AI literacy considering likely changes in AI capabilities; and\n**(B)**\nstudent progression to more advanced topics as they progress through K\u201312 education.\n##### (b) Awards\nThe Director may make awards on a merit-reviewed, competitive basis to institutions of higher education or nonprofit organizations (or a consortium thereof) to support research activities to develop educational curricula, instructional material, teacher professional development, and evaluation methods for AI literacy at the K\u201312 level.\n##### (c) Use of award funds\nActivities funded by awards made under this section may include the following:\n**(1)**\nFormal and informal K\u201312 education curriculum development focused on the essential abilities and competencies necessary for AI literacy that is learner-centered, project-based, and can be personalized in the classroom and other learning environments.\n**(2)**\nEngaging State and local educational agencies, superintendents, principals, educators, or other school leaders of students in kindergarten through grade 12 in professional learning opportunities to\u2014\n**(A)**\nenhance AI literacy and proficiency;\n**(B)**\npromote responsible use of AI; and\n**(C)**\ndevelop best practices.\n**(3)**\nDeveloping AI literacy evaluation tools and resources for educators assessing proficiency in AI literacy.\n**(4)**\nDesigning and implementing professional development courses and experiences in AI literacy, including mentoring, for State and local educational agencies, principals, educators, or other school leaders that integrate in-person, virtual, and distance learning experiences.\n**(5)**\nDevelopment of hands-on learning tools to assist in developing and improving AI literacy.\n**(6)**\nAugmenting the existing curriculum to incorporate AI literacy where appropriate, including responsible use of AI in learning.\n**(7)**\nAdditional activities determined appropriate by the Director.\n##### (d) Implementation\nThe Director may carry out this section by making awards through new or existing programs.\n##### (e) Definitions\nIn this section:\n**(1) Ai literacy**\nThe term AI literacy means having the age-appropriate knowledge and ability to use artificial intelligence effectively, to critically interpret outputs, to solve problems in an AI-enabled world, and to mitigate potential risks.\n**(2) Artificial intelligence; ai**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ; enacted as part of title LVI of division E of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 )).\n**(3) Director**\nThe term Director means the Director of the National Science Foundation.\n**(4) K\u201312 education**\nThe term K\u201312 education means elementary schools and secondary schools (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )).",
      "versionDate": "2025-09-26",
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
        "actionDate": "2026-04-28",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "4414",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LIFT AI Act",
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
        "updateDate": "2025-12-17T15:44:13Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5584ih.xml"
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
      "title": "LIFT AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIFT AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Literacy in Future Technologies Artificial Intelligence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve educational efforts related to artificial intelligence literacy at the K through 12 level, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:20Z"
    }
  ]
}
```
