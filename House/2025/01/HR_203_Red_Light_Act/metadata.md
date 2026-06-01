# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/203
- Title: Red Light Act
- Congress: 119
- Bill type: HR
- Bill number: 203
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-22T08:06:30Z
- Update date including text: 2025-03-22T08:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-04 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-04 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/203",
    "number": "203",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Red Light Act",
    "type": "HR",
    "updateDate": "2025-03-22T08:06:30Z",
    "updateDateIncludingText": "2025-03-22T08:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-04",
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
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:22:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-04T14:34:13Z",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "WI"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr203ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 203\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Tenney introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo withhold Federal highway funds from States that provide driver\u2019s licenses or identification cards to aliens who are unlawfully present in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Red Light Act .\n#### 2. Withholding of funds for providing identification cards to certain aliens\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following new section:\n180. Withholding of funds for providing identification cards to certain aliens (a) Withholding of funds for noncompliance For fiscal year 2023 and each fiscal year thereafter, the Secretary shall withhold 100 percent of the amount required to be apportioned under each of sections 104(b)(1), 104(b)(3), and 104(b)(4) of this title to any State that is described in subsection (b). (b) State described A State described in this subsection is a State that has enacted a law that allows the State to provide a driver\u2019s license or other identification card to an alien who is unlawfully present in the United States. (c) Effect of withholding funds (1) In general Any funds withheld under subsection (a) from apportionment to any State shall remain available until the end of the fiscal year for which the funds are apportioned. (2) Reapportionment If, before the last day of the fiscal year for which funds withheld under subsection (a) are apportioned to a State, the State repeals all laws of such State described in subsection (b), the Secretary shall, on the first day on which the State repeals all such laws, apportion to the State the funds withheld under subsection (a) that remain available for apportionment to the State. (3) Apportionment among States If, at the end of the fiscal year in which funds are withheld from a State under paragraph (1), the State has not repealed the law described in subsection (b), the Secretary shall apportion the corresponding withheld funds described in subsection (a) on a proportional basis to all remaining States that have not enacted laws described in subsection (b). (4) Withholding in future year In the case in which a State has funds withheld under paragraph (1) and is reapportioned funds under paragraph (2) and subsequently enacts a law described in subsection (b) after the date on which the funds are reapportioned under paragraph (2), the Secretary shall withhold the amount of funds withheld under subsection (a) in the fiscal year following the fiscal year in which such actions occur and each fiscal year thereafter. (d) Identification card defined The term identification card means a personal identification card, as defined in section 1028(d) of title 18, United States Code, issued by a State. .\n##### (b) Clerical amendment\nChapter 1 of title 23, United States Code, in the table of contents is amended by adding at the end the following:\n180. Withholding of funds for providing identification cards to certain aliens. .",
      "versionDate": "2025-01-03",
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
        "updateDate": "2025-02-04T13:05:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr203",
          "measure-number": "203",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr203v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Red Light Act</strong></p><p>This bill directs the Department of Transportation to withhold all of a state's share of certain\u00a0federal highway funds (specifically, funds for the National Highway Performance Program, the Highway Safety Improvement Program, and the Congestion Mitigation and Air Quality Improvement Program) in FY2023 and thereafter if such state has enacted a law to provide driver's licenses or other identification cards to aliens who are unlawfully present in the United States.</p>"
        },
        "title": "Red Light Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr203.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Red Light Act</strong></p><p>This bill directs the Department of Transportation to withhold all of a state's share of certain\u00a0federal highway funds (specifically, funds for the National Highway Performance Program, the Highway Safety Improvement Program, and the Congestion Mitigation and Air Quality Improvement Program) in FY2023 and thereafter if such state has enacted a law to provide driver's licenses or other identification cards to aliens who are unlawfully present in the United States.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr203"
    },
    "title": "Red Light Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Red Light Act</strong></p><p>This bill directs the Department of Transportation to withhold all of a state's share of certain\u00a0federal highway funds (specifically, funds for the National Highway Performance Program, the Highway Safety Improvement Program, and the Congestion Mitigation and Air Quality Improvement Program) in FY2023 and thereafter if such state has enacted a law to provide driver's licenses or other identification cards to aliens who are unlawfully present in the United States.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr203"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr203ih.xml"
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
      "title": "Red Light Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Red Light Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T07:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To withhold Federal highway funds from States that provide driver's licenses or identification cards to aliens who are unlawfully present in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T07:48:27Z"
    }
  ]
}
```
