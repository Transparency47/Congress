# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3963?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3963
- Title: Public Inspectors for Safe Infrastructure Act
- Congress: 119
- Bill type: HR
- Bill number: 3963
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-07-15T08:05:18Z
- Update date including text: 2025-07-15T08:05:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-12 - IntroReferral: Sponsor introductory remarks on measure. (CR E570)
- 2025-06-13 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-12 - IntroReferral: Sponsor introductory remarks on measure. (CR E570)
- 2025-06-13 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3963",
    "number": "3963",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000559",
        "district": "8",
        "firstName": "John",
        "fullName": "Rep. Garamendi, John [D-CA-8]",
        "lastName": "Garamendi",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Public Inspectors for Safe Infrastructure Act",
    "type": "HR",
    "updateDate": "2025-07-15T08:05:18Z",
    "updateDateIncludingText": "2025-07-15T08:05:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E570)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T20:52:47Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-12",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MI"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3963ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3963\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Garamendi (for himself, Ms. Brownley , Mr. Lynch , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to require that public employees perform construction inspection work for federally funded highway projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Inspectors for Safe Infrastructure Act .\n#### 2. Requiring construction inspection services for certain highway contracts to be performed by public employees\nSection 112(b) of title 23, United States Code, is amended by adding at the end the following:\n(5) Construction inspection services (A) In general In entering into a contract under this section for the construction of a project subject to subsection (a), including a design-build project under paragraph (3) and a project using a 2-phase contract under paragraph (4), a State transportation department or local transportation agency shall ensure that a public employee performs construction inspection functions for such project. (B) Exception If a State transportation department or local transportation agency does not have adequate existing or obtainable staff to perform construction inspection functions as required under subparagraph (A), the department or agency may obtain such services pursuant to temporary consultant contracts until the department or agency has adequate or existing staff to perform such functions. (C) Time period Any temporary contracts to provide construction inspection services under this subsection shall not exceed the period that ends on the date that is 12 months after the date on which the contract is awarded. (D) Reporting and Transparency (i) In general At least once each fiscal year, a State transportation department or local transportation agency utilizing the exception authority provided in subparagraph (B) shall submit to the Secretary a report containing\u2014 (I) a description of all construction inspection functions provided through temporary consultant contracts under such clause; and (II) a detailed justification of the need for each exception to the requirement of such clause. (ii) Transparency The Secretary shall make the report submitted under clause (i) available to the public through the website of the Department. (E) Definitions In this subsection: (i) Construction inspection function The term \u2018construction inspection function\u2019 includes construction engineering, contract administration, on-site quality control inspection, materials testing, and the functions of a resident engineer or assistant resident engineer responsible for the acceptance or rejection of a project subject to the provisions of subsection (a) of this section. (ii) Public employee The term public employee means an employee of the Federal Government, a State government, or a local government. .",
      "versionDate": "2025-06-12",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-02T18:39:31Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3963ih.xml"
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
      "title": "Public Inspectors for Safe Infrastructure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Inspectors for Safe Infrastructure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to require that public employees perform construction inspection work for federally funded highway projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:34Z"
    }
  ]
}
```
