# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4048?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4048
- Title: STEM Pathways for the Future Act
- Congress: 119
- Bill type: HR
- Bill number: 4048
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-09-15T16:50:38Z
- Update date including text: 2025-09-15T16:50:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-17 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-17 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4048",
    "number": "4048",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000620",
        "district": "29",
        "firstName": "Luz",
        "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
        "lastName": "Rivas",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "STEM Pathways for the Future Act",
    "type": "HR",
    "updateDate": "2025-09-15T16:50:38Z",
    "updateDateIncludingText": "2025-09-15T16:50:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-17T15:02:30Z",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "LA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "AL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "MI"
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
      "sponsorshipDate": "2025-06-17",
      "state": "PA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "DE"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4048ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4048\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Ms. Rivas (for herself, Mr. Fields , Ms. Sewell , Mr. Thanedar , Ms. Lee of Pennsylvania , Mr. Sorensen , and Ms. McBride ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Director of the National Science Foundation to establish a program to award grants for certain STEM apprenticeship programs, require an interagency task force to submit a report regarding certain programs of the Federal Government focused primarily on career development and training in STEM, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the STEM Pathways for the Future Act .\n#### 2. Grant program to establish certain STEM apprenticeship programs; Interagency Task Force\n##### (a) Grant program To establish certain STEM apprenticeship programs\nThe National Science Foundation Authorization Act of 2002 ( Public Law 107\u2013368 ) is amended by inserting after section 8 the following new section:\n8A. Grant program to establish certain STEM apprenticeship programs (a) In general Not later than one year after the date of the enactment of this section, the Director shall establish a program to award grants on a competitive basis to eligible recipients to establish STEM apprenticeship programs that are not carried out by four-year institutions of higher education (in this section referred to as the Program ). (b) Application An eligible recipient that seeks a grant under the Program shall submit to the Director an application at such time, in such manner, and containing such information as the Director may require. (c) Awards In awarding grants under the Program, the Director shall give preference to priority recipients over eligible recipients that are not priority recipients. (d) Permissible use of funds As determined appropriate by the Director, a recipient of a grant awarded under the Program may obligate or expend grants funds for the following activities: (1) Recruiting participants to a STEM apprenticeship program established under the Program. (2) Planning and technical assistance to improve such apprenticeship program. (3) Incorporating emerging technology into such apprenticeship program. (4) Entering such apprenticeship program into a consortium with, or establishing an advisory board for such apprenticeship program that is composed of, one or more private sector entities in STEM. (5) Any other activity as the Director may determine. (e) Impermissible use of funds A recipient of a grant awarded under the Program may not obligate or expend grant funds for recruitment, inducement, or associated financial or tangible incentives that might be offered to relocate an existing business from a geographic area to another geographic area. (f) Definitions In this section: (1) Eligible recipient The term eligible recipient means any of the following: (A) A State. (B) An Indian Tribe (as such term is defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )). (C) A city or other political subdivision of such State or Indian Tribe. (D) A public-private partnership focused primarily on career development and training in STEM. (E) A priority recipient. (F) A consortium of any of the entities described in subparagraphs (A) through (E). (2) Priority recipient The term priority recipient means any of the following: (A) An entity that carries out an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ) (B) A community college. (C) A minority-serving institution (as such term is defined in section 10002 of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18901 )). (D) Any other entity as the Director may determine. (E) A consortium that includes an entity described in subparagraphs (A) through (D). (3) STEM The term STEM means the study or practice of science, technology, engineering, or mathematics. .\n##### (b) Interagency Task Force\n**(1) Composition**\nThere is established an interagency task force (in this subsection referred to as the Task Force ) composed of eight members as follows:\n**(A)**\nThe Administrator of the Environmental Protection Agency.\n**(B)**\nThe Director of the National Science Foundation.\n**(C)**\nThe Director of the Office of Science and Technology Policy.\n**(D)**\nThe Secretary of Commerce.\n**(E)**\nThe Secretary of Education.\n**(F)**\nThe Secretary of Energy.\n**(G)**\nThe Secretary of Health and Human Services.\n**(H)**\nThe Secretary of Labor.\n**(2) Report**\nNot later than one year after the date of the enactment of this section, the Task Force shall submit to Congress a report that includes information relating to an identification of each program of the Federal Government that satisfies the following requirements:\n**(A)**\nIs focused primarily on career development and training in STEM.\n**(B)**\nIs carried out through any of the following:\n**(i)**\nAn apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ).\n**(ii)**\nA community college (as such term is defined in section 4 of the National Science Foundation Authorization Act of 2002 ( 42 U.S.C. 1862n note)).\n**(iii)**\nA minority-serving institution (as such term is defined in section 10002 of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 18901 )).\n**(3) Termination**\nThe Task Force shall terminate upon submission of the report under paragraph (2).",
      "versionDate": "2025-06-17",
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
            "name": "Employment and training programs",
            "updateDate": "2025-09-15T16:39:17Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-09-15T16:50:38Z"
          },
          {
            "name": "Science and engineering education",
            "updateDate": "2025-09-15T16:39:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-07-14T11:02:17Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4048ih.xml"
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
      "title": "STEM Pathways for the Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STEM Pathways for the Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-28T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the National Science Foundation to establish a program to award grants for certain STEM apprenticeship programs, require an interagency task force to submit a report regarding certain programs of the Federal Government focused primarily on career development and training in STEM, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-28T07:03:21Z"
    }
  ]
}
```
