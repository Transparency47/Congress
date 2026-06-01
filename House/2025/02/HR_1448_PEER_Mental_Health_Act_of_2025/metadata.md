# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1448
- Title: PEER Mental Health Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1448
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-07-14T15:21:11Z
- Update date including text: 2025-07-14T15:21:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1448",
    "number": "1448",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001318",
        "district": "",
        "firstName": "Becca",
        "fullName": "Rep. Balint, Becca [D-VT-At Large]",
        "lastName": "Balint",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "PEER Mental Health Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-14T15:21:11Z",
    "updateDateIncludingText": "2025-07-14T15:21:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:33:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "OR"
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
      "sponsorshipDate": "2025-02-21",
      "state": "DC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NJ"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "AL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1448ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1448\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Ms. Balint (for herself, Ms. Salinas , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, to award grants for peer mental health first aid, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Peer Education and Emergency Response for Mental Health Act of 2025 or the PEER Mental Health Act of 2025 .\n#### 2. Grants for peer mental health first aid\nTitle V of the Public Health Service Act is amended by inserting after section 520J of such Act ( 42 U.S.C. 290bb\u201341 ) the following:\n520J\u20131. Grants for peer mental health first aid (a) In general The Secretary shall award grants to eligible entities\u2014 (1) to train teachers, other relevant school personnel (including education support professionals), students, and parents and caregivers of students\u2014 (A) to recognize symptoms of childhood and adolescent mental health conditions; (B) to refer students to appropriate mental health services if necessary; and (C) to recognize signs of immediate mental distress and, upon recognizing such signs apply mental health first aid tactics; and (2) to provide education to such teachers, personnel, students, parents, and caregivers regarding resources that are available in the community for individuals with a mental illness. (b) Relation to other mental health awareness training grants An eligible entity may receive grant funds under this section in addition to receiving amounts made available to such eligible entity pursuant to section 520J. (c) Allocation for schools in rural areas (1) In general In awarding grants under this section, the Secretary shall award not less than 25 percent of the amounts made available to carry out this section for a fiscal year to eligible entities that are elementary schools or secondary schools in rural areas or that are applying for grants on behalf of such schools. (2) Reallocation If the Secretary is unable to obligate the total amount of funds set aside under paragraph (1) for a fiscal year due to a lack of qualified applications from eligible applicants described in paragraph (1), the Secretary shall reallocate the remainder of such funds for making grants under this section to other eligible entities. (d) Application (1) In general To seek a grant under this section, an eligible entity shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require, including a plan for the rigorous evaluation of activities that are carried out with funds received through the grant. (2) Streamlined process The Secretary shall streamline the process for applying for a grant under this section so as to keep such process from imposing an unreasonable barrier, especially for eligible entities with limited personnel available to prepare a grant application. (e) Technical assistance The Secretary shall provide technical assistance to eligible entities applying for, or receiving, grants under this section. Such technical assistance shall include the development and dissemination of best practices for providing training and education described in subsection (a). (f) Definition In this section: (1) The terms elementary school , local educational agency , secondary school , and State educational agency have the meanings given to those terms in section 8101 of the Elementary and Secondary Education Act of 1965. (2) The term eligible entity means an elementary school, a local educational agency, a secondary school, or a State educational agency. (3) The term rural area refers to a rural area as defined by the Health Resources and Services Administration for purposes of awarding rural health grants. (g) Authorization of appropriations To carry out this section, there is authorized to be appropriated $24,963,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-02-21",
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
            "name": "Child health",
            "updateDate": "2025-07-14T15:21:11Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-07-14T15:21:06Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-07-14T15:20:57Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-14T15:20:52Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-14T15:20:42Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-07-14T15:20:14Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-07-14T15:20:46Z"
          },
          {
            "name": "Teaching, teachers, curricula",
            "updateDate": "2025-07-14T15:21:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T15:07:09Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1448ih.xml"
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
      "title": "PEER Mental Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEER Mental Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Peer Education and Emergency Response for Mental Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services, acting through the Assistant Secretary for Mental Health and Substance Use, to award grants for peer mental health first aid, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:18:22Z"
    }
  ]
}
```
