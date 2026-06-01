# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/191
- Title: LICENSE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 191
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-12-06T06:47:15Z
- Update date including text: 2025-12-06T06:47:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/191",
    "number": "191",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "LICENSE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-06T06:47:15Z",
    "updateDateIncludingText": "2025-12-06T06:47:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-22T20:31:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s191is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 191\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Ms. Lummis (for herself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Transportation to modify certain regulations relating to the requirements for commercial driver\u2019s license testing and commercial learner\u2019s permit holders, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 .\n#### 2. Modifications to certain commercial driver\u2019s license regulations\nNot later than 90 days after the date of enactment of this Act, the Secretary of Transportation, acting through the Administrator of the Federal Motor Carrier Safety Administration, shall\u2014\n**(1)**\nrevise section 384.228 of title 49, Code of Federal Regulations (or a successor regulation), to allow a State or third-party examiner to administer a commercial driver\u2019s license knowledge test if the examiner\u2014\n**(A)**\nmaintains a valid commercial driver\u2019s license test examiner certification;\n**(B)**\ncompletes a commercial driver\u2019s license skills test examiner training course that meets the requirements of subsection (d) of that section; and\n**(C)**\ncompletes 1 unit of instruction described in subsection (c)(3) of that section; and\n**(2)**\nrevise section 383.79 of title 49, Code of Federal Regulations (or a successor regulation), to allow a State to administer a driving skills test to any commercial driver\u2019s license applicant, regardless of the State of domicile of the applicant or where the applicant received driver training.",
      "versionDate": "2025-01-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-23",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "623",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LICENSE Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-03-01T13:44:53Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s191",
          "measure-number": "191",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s191v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 </strong></p><p>This bill requires the Federal Motor Carrier Safety Administration (FMCA) to revise regulations to relax certain requirements related to commercial driver's license (CDL) testing.</p><p>Specifically, the FMCA must allow a state or third-party examiner who has maintained a valid CDL test examiner certification and has previously completed a CDL skills test examiner training course to administer the CDL knowledge test, so long as they have completed one unit of instruction regarding\u00a0the CDL knowledge test.</p><p>The FMCA must also allow a state to administer a driving skills test to any CDL applicant regardless of the applicant's state of domicile or where the applicant received driver training.</p><p>As background, the FMCA implemented temporary waivers for similar CDL testing-related requirements\u00a0in response to the COVID-19 pandemic. These waivers have since expired.</p>"
        },
        "title": "LICENSE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s191.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 </strong></p><p>This bill requires the Federal Motor Carrier Safety Administration (FMCA) to revise regulations to relax certain requirements related to commercial driver's license (CDL) testing.</p><p>Specifically, the FMCA must allow a state or third-party examiner who has maintained a valid CDL test examiner certification and has previously completed a CDL skills test examiner training course to administer the CDL knowledge test, so long as they have completed one unit of instruction regarding\u00a0the CDL knowledge test.</p><p>The FMCA must also allow a state to administer a driving skills test to any CDL applicant regardless of the applicant's state of domicile or where the applicant received driver training.</p><p>As background, the FMCA implemented temporary waivers for similar CDL testing-related requirements\u00a0in response to the COVID-19 pandemic. These waivers have since expired.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119s191"
    },
    "title": "LICENSE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025 or the LICENSE Act of 2025 </strong></p><p>This bill requires the Federal Motor Carrier Safety Administration (FMCA) to revise regulations to relax certain requirements related to commercial driver's license (CDL) testing.</p><p>Specifically, the FMCA must allow a state or third-party examiner who has maintained a valid CDL test examiner certification and has previously completed a CDL skills test examiner training course to administer the CDL knowledge test, so long as they have completed one unit of instruction regarding\u00a0the CDL knowledge test.</p><p>The FMCA must also allow a state to administer a driving skills test to any CDL applicant regardless of the applicant's state of domicile or where the applicant received driver training.</p><p>As background, the FMCA implemented temporary waivers for similar CDL testing-related requirements\u00a0in response to the COVID-19 pandemic. These waivers have since expired.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119s191"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s191is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LICENSE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Licensing Individual Commercial Exam-takers Now Safely and Efficiently Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Transportation to modify certain regulations relating to the requirements for commercial driver's license testing and commercial learner's permit holders, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:20Z"
    }
  ]
}
```
