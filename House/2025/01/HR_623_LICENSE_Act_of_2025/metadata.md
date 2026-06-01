# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/623?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/623
- Title: LICENSE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 623
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-12-06T06:46:49Z
- Update date including text: 2025-12-06T06:46:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-23 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-23 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/623",
    "number": "623",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "LICENSE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-06T06:46:49Z",
    "updateDateIncludingText": "2025-12-06T06:46:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-23T15:39:43Z",
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
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "SD"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "OH"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr623ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 623\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. LaHood (for himself, Mr. Johnson of South Dakota , Mr. Harder of California , Mr. Costa , Mr. Balderson , and Mr. Cuellar ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to modify certain regulations relating to the requirements for commercial driver\u2019s license testing and commercial learner\u2019s permit holders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 .\n#### 2. Modifications to certain commercial driver\u2019s license regulations\nNot later than 90 days after the date of enactment of this Act, the Secretary of Transportation, acting through the Administrator of the Federal Motor Carrier Safety Administration, shall\u2014\n**(1)**\nrevise section 384.228 of title 49, Code of Federal Regulations (or a successor regulation), to allow a State or third-party examiner to administer the commercial driver\u2019s license knowledge test only if the examiner\u2014\n**(A)**\nmaintains a valid commercial driver\u2019s license test examiner certification;\n**(B)**\ncompletes a commercial driver\u2019s license skills test examiner training course that meets the requirements of subsection (d) of such section; and\n**(C)**\ncompletes 1 unit of instruction described in subsection (c)(3) of such section; and\n**(2)**\nrevise section 383.79 of title 49, Code of Federal Regulations (or a successor regulation), to allow a State to administer a driving skills tests to any commercial driver\u2019s license applicant, regardless of the State of domicile of the applicant or where the applicant received driver training.",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-01-22",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "191",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LICENSE Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-24T16:06:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr623",
          "measure-number": "623",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr623v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 </strong></p><p>This bill requires the Federal Motor Carrier Safety Administration (FMCA) to revise regulations to relax certain requirements related to commercial driver's license (CDL) testing. </p><p>Specifically, the FMCA must allow a state or third-party examiner who has maintained a valid CDL test examiner certification and has previously completed a CDL skills test examiner training course to administer the CDL knowledge test, so long as they have completed one unit of instruction regarding\u00a0the CDL knowledge test.</p><p>The FMCA must also allow a state to administer a driving skills test to any CDL applicant regardless of the applicant's state of domicile or where the applicant received driver training.</p><p>As background, the FMCA implemented temporary waivers for similar CDL testing-related requirements\u00a0in response to the COVID-19 pandemic. These waivers have since expired.</p>"
        },
        "title": "LICENSE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr623.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 </strong></p><p>This bill requires the Federal Motor Carrier Safety Administration (FMCA) to revise regulations to relax certain requirements related to commercial driver's license (CDL) testing. </p><p>Specifically, the FMCA must allow a state or third-party examiner who has maintained a valid CDL test examiner certification and has previously completed a CDL skills test examiner training course to administer the CDL knowledge test, so long as they have completed one unit of instruction regarding\u00a0the CDL knowledge test.</p><p>The FMCA must also allow a state to administer a driving skills test to any CDL applicant regardless of the applicant's state of domicile or where the applicant received driver training.</p><p>As background, the FMCA implemented temporary waivers for similar CDL testing-related requirements\u00a0in response to the COVID-19 pandemic. These waivers have since expired.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr623"
    },
    "title": "LICENSE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 </strong></p><p>This bill requires the Federal Motor Carrier Safety Administration (FMCA) to revise regulations to relax certain requirements related to commercial driver's license (CDL) testing. </p><p>Specifically, the FMCA must allow a state or third-party examiner who has maintained a valid CDL test examiner certification and has previously completed a CDL skills test examiner training course to administer the CDL knowledge test, so long as they have completed one unit of instruction regarding\u00a0the CDL knowledge test.</p><p>The FMCA must also allow a state to administer a driving skills test to any CDL applicant regardless of the applicant's state of domicile or where the applicant received driver training.</p><p>As background, the FMCA implemented temporary waivers for similar CDL testing-related requirements\u00a0in response to the COVID-19 pandemic. These waivers have since expired.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr623"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr623ih.xml"
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
      "title": "LICENSE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T08:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LICENSE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to modify certain regulations relating to the requirements for commercial driver's license testing and commercial learner's permit holders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T08:48:25Z"
    }
  ]
}
```
