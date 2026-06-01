# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2182
- Title: Pre-Pilot Pathway Act
- Congress: 119
- Bill type: HR
- Bill number: 2182
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-06-12T08:07:00Z
- Update date including text: 2025-06-12T08:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-18 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-18 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2182",
    "number": "2182",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Pre-Pilot Pathway Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:07:00Z",
    "updateDateIncludingText": "2025-06-12T08:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-18T20:46:51Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2182ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2182\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Donalds (for himself, Mr. Davis of North Carolina , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish an apprenticeship program for students at flight training providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pre-Pilot Pathway Act .\n#### 2. Apprenticeship program for pilots\n##### (a) Definitions\nIn this section:\n**(1) Apprentice**\nThe term apprentice means a student enrolled at a flight training provider.\n**(2) Flight training provider**\nThe term flight training provider means a flight academy certified under part 141 of title 14, Code of Federal Regulations.\n**(3) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Establishment\nThe Secretary, in consultation with appropriate industry stakeholders and flight training providers who conduct flight training under part 141 of title 14, Code of Federal Regulations, shall establish an apprenticeship program to establish a pipeline of qualified and interested individuals to become commercial pilots.\n##### (c) Selection\nUnder the apprenticeship program established under subsection (b), each flight training provider participating in the apprenticeship program established under subsection (b) may select up to 8 applicants, or more if considered appropriate by the Secretary based upon the size and type of each participating flight training provider, to serve as apprentices each academic year.\n##### (d) Curriculum and requirements\n**(1) In general**\nTo graduate from an apprenticeship program established under subsection (b), an apprentice shall satisfy any relevant requirements and minimum curriculum under part 141 of title 14, Code of Federal Regulations (or successor regulations), including all curriculum under subpart C of such part.\n**(2) Minimum requirements**\nNothing in this Act prevents a flight training provider from imposing additional requirements, such as modifying the terms of service of the apprenticeship program, on an apprentice taking part in an apprenticeship program established pursuant to this section.\n##### (e) Optional program\nA flight training provider may choose not to participate in an apprenticeship program established under this section.\n##### (f) Regulations\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue such regulations as are necessary to implement this Act.\n##### (g) Incentivizing retired pilots\nThe Secretary shall take such actions as may be appropriate to develop methods to incentivize pilots, including retired military pilots, retiring airline pilots, and graduates of the apprenticeship programs established under this section, to become instructors, mentors, or program advisors at participating flight training providers, including through the development of pathway programs for such pilots to gain initial qualifications or concurrent qualifications as certified flight instructors under part 61 or part 141 of title 14, Code of Federal Regulations.\n##### (h) Reporting and evaluation\n**(1) Reporting**\nThe Secretary shall submit to Congress an annual report detailing apprentice progress, retention rates, and post-graduation employment outcomes under the program under this section.\n**(2) Evaluation**\nThe Secretary shall conduct an annual review of the apprenticeship program\u2019s effectiveness, including the impact on addressing pilot shortages.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-04-03T12:09:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
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
          "measure-id": "id119hr2182",
          "measure-number": "2182",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2182v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pre-Pilot Pathway Act </strong></p><p>This bill directs the Department of Transportation (DOT) to establish an apprenticeship program with flight training providers (e.g., flight schools) in order to establish a commercial pilot pipeline; DOT must issue any necessary regulations to implement the program within one year of the bill's enactment.</p><p>Each flight training provider participating in the program may select up to eight applicants (or more applicants based on a determination by DOT) per academic year to serve as apprentices.</p><p>DOT must take appropriate actions to develop methods to incentivize pilots, including retired pilots, to become flight school instructors, mentors, or program advisors at participating flight training providers. This includes developing pathway programs for pilots to gain initial qualifications or concurrent qualifications as certified flight instructors.</p><p>Further, DOT must conduct an annual review of the apprenticeship program\u2019s effectiveness, including the impact on addressing pilot shortages.</p>"
        },
        "title": "Pre-Pilot Pathway Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2182.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pre-Pilot Pathway Act </strong></p><p>This bill directs the Department of Transportation (DOT) to establish an apprenticeship program with flight training providers (e.g., flight schools) in order to establish a commercial pilot pipeline; DOT must issue any necessary regulations to implement the program within one year of the bill's enactment.</p><p>Each flight training provider participating in the program may select up to eight applicants (or more applicants based on a determination by DOT) per academic year to serve as apprentices.</p><p>DOT must take appropriate actions to develop methods to incentivize pilots, including retired pilots, to become flight school instructors, mentors, or program advisors at participating flight training providers. This includes developing pathway programs for pilots to gain initial qualifications or concurrent qualifications as certified flight instructors.</p><p>Further, DOT must conduct an annual review of the apprenticeship program\u2019s effectiveness, including the impact on addressing pilot shortages.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr2182"
    },
    "title": "Pre-Pilot Pathway Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pre-Pilot Pathway Act </strong></p><p>This bill directs the Department of Transportation (DOT) to establish an apprenticeship program with flight training providers (e.g., flight schools) in order to establish a commercial pilot pipeline; DOT must issue any necessary regulations to implement the program within one year of the bill's enactment.</p><p>Each flight training provider participating in the program may select up to eight applicants (or more applicants based on a determination by DOT) per academic year to serve as apprentices.</p><p>DOT must take appropriate actions to develop methods to incentivize pilots, including retired pilots, to become flight school instructors, mentors, or program advisors at participating flight training providers. This includes developing pathway programs for pilots to gain initial qualifications or concurrent qualifications as certified flight instructors.</p><p>Further, DOT must conduct an annual review of the apprenticeship program\u2019s effectiveness, including the impact on addressing pilot shortages.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr2182"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2182ih.xml"
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
      "title": "Pre-Pilot Pathway Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pre-Pilot Pathway Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish an apprenticeship program for students at flight training providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T04:18:28Z"
    }
  ]
}
```
