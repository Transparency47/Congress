# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5801?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5801
- Title: Shutdown Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 5801
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2026-03-30T18:55:22Z
- Update date including text: 2026-03-30T18:55:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-10-21: Introduced in House

## Actions

- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5801",
    "number": "5801",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Shutdown Fairness Act",
    "type": "HR",
    "updateDate": "2026-03-30T18:55:22Z",
    "updateDateIncludingText": "2026-03-30T18:55:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "WI"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "OK"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "KS"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "GA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "IA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "VA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "IN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "WI"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "OH"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "PA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IN"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "KS"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5801ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5801\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Johnson of South Dakota (for himself, Mr. Mackenzie , Mr. Wied , Mrs. Bice , Mr. Issa , Mr. Lawler , Mr. Mann , Mr. Austin Scott of Georgia , and Mrs. Miller-Meeks ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo appropriate funds for pay and allowances of excepted Federal employees for periods of work performed during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shutdown Fairness Act .\n#### 2. Appropriations\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term agency means each authority of the executive, legislative, or judicial branch of the Government of the United States;\n**(2)**\nthe term excepted employee \u2014\n**(A)**\nmeans an employee of an agency who the head of that agency determines is an excepted employee or an employee performing emergency work, as those terms are defined by the Office of Personnel Management; and\n**(B)**\nincludes\u2014\n**(i)**\na contractor who\u2014\n**(I)**\nprovides support to an employee described in subparagraph (A); and\n**(II)**\nis required to perform work during a lapse in appropriations, as determined by the head of the agency with respect to which the contractor provides support; and\n**(ii)**\na member of the Armed Forces on active duty; and\n**(3)**\nthe term excepted work means work performed by an excepted employee during a period during which interim or full-year appropriations for the applicable fiscal year are not in effect for the applicable agency.\n##### (b) Appropriations\nFor fiscal year 2026, and any fiscal year thereafter, for any period during which interim continuing appropriations or full-year appropriations for that fiscal year are not in effect for an agency, there are appropriated to the head of the agency, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to provide standard rates of pay, allowances, pay differentials, benefits, and other payments otherwise payable on a regular basis to excepted employees of the agency with respect to any period of excepted work performed by the excepted employees.\n##### (c) Termination\nAppropriations and funds made available and authority granted under subsection (b) shall be available to the head of an agency until whichever of the following first occurs:\n**(1)**\nThe enactment into law of appropriations for the agency until the end of the applicable fiscal year (including a continuing appropriation) that provide amounts for the purposes for which amounts are made available under subsection (b).\n**(2)**\nThe enactment into law of appropriations for the agency until the end of the applicable fiscal year (including a continuing appropriation) without any appropriation for such purposes.\n##### (d) Interim continuing appropriations\nAppropriations made available under subsection (b) may not be obligated by the head of an agency during any period during which continuing appropriations for the purposes for which amounts are made available under subsection (b) are in effect for the agency.\n##### (e) Charging to full-Year appropriations\nObligations or expenditures made by the head of an agency pursuant to subsection (b) shall be charged to the applicable appropriation for the agency whenever a regular appropriation bill or a measure making continuing appropriations until the end of the applicable fiscal year for the agency becomes law.\n##### (f) Retroactive effective date\nThis Act shall take effect as if enacted on September 30, 2025.",
      "versionDate": "2025-10-21",
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
        "actionDate": "2025-10-09",
        "text": "Read twice and referred to the Committee on Appropriations."
      },
      "number": "3001",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Shutdown Fairness Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-07",
        "text": "Upon reconsideration, cloture on the motion to proceed to the measure not invoked in Senate by Yea-Nay Vote. 53 - 43. Record Vote Number: 609."
      },
      "number": "3012",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Shutdown Fairness Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-28",
        "text": "Read twice and referred to the Committee on Appropriations."
      },
      "number": "3066",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pay the People Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-10-24T13:40:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-21",
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
          "measure-id": "id119hr5801",
          "measure-number": "5801",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-21",
          "originChamber": "HOUSE",
          "update-date": "2025-10-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5801v00",
            "update-date": "2025-10-24"
          },
          "action-date": "2025-10-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Shutdown Fairness Act</strong></p><p>This bill provides appropriations to pay federal employees who work during a government shutdown.</p><p>Specifically, the bill provides appropriations for federal agencies to provide standard rates of pay, allowances, pay differentials, benefits, and other payments to excepted employees for work performed during any period in which interim continuing appropriations or full-year appropriations are not in effect for a fiscal year (i.e., a government shutdown). An excepted employee is an employee who is required to work during a government shutdown.</p><p>Under current law, excepted employees are not paid until the government shutdown is over. This bill provides appropriations to pay excepted employees during a government shutdown. The bill also specifies that the term\u00a0<em>excepted employee </em>includes certain contractors who support federal employees during a government shutdown and members of the Armed Forces who are on active duty.\u00a0</p><p>A federal agency may not use the funds provided by this bill during any period in which continuing appropriations are in effect for the purpose of paying\u00a0excepted employees of the agency.</p><p>The bill must take effect as if it had been enacted on September 30, 2025.\u00a0</p>"
        },
        "title": "Shutdown Fairness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5801.xml",
    "summary": {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Shutdown Fairness Act</strong></p><p>This bill provides appropriations to pay federal employees who work during a government shutdown.</p><p>Specifically, the bill provides appropriations for federal agencies to provide standard rates of pay, allowances, pay differentials, benefits, and other payments to excepted employees for work performed during any period in which interim continuing appropriations or full-year appropriations are not in effect for a fiscal year (i.e., a government shutdown). An excepted employee is an employee who is required to work during a government shutdown.</p><p>Under current law, excepted employees are not paid until the government shutdown is over. This bill provides appropriations to pay excepted employees during a government shutdown. The bill also specifies that the term\u00a0<em>excepted employee </em>includes certain contractors who support federal employees during a government shutdown and members of the Armed Forces who are on active duty.\u00a0</p><p>A federal agency may not use the funds provided by this bill during any period in which continuing appropriations are in effect for the purpose of paying\u00a0excepted employees of the agency.</p><p>The bill must take effect as if it had been enacted on September 30, 2025.\u00a0</p>",
      "updateDate": "2025-10-24",
      "versionCode": "id119hr5801"
    },
    "title": "Shutdown Fairness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Shutdown Fairness Act</strong></p><p>This bill provides appropriations to pay federal employees who work during a government shutdown.</p><p>Specifically, the bill provides appropriations for federal agencies to provide standard rates of pay, allowances, pay differentials, benefits, and other payments to excepted employees for work performed during any period in which interim continuing appropriations or full-year appropriations are not in effect for a fiscal year (i.e., a government shutdown). An excepted employee is an employee who is required to work during a government shutdown.</p><p>Under current law, excepted employees are not paid until the government shutdown is over. This bill provides appropriations to pay excepted employees during a government shutdown. The bill also specifies that the term\u00a0<em>excepted employee </em>includes certain contractors who support federal employees during a government shutdown and members of the Armed Forces who are on active duty.\u00a0</p><p>A federal agency may not use the funds provided by this bill during any period in which continuing appropriations are in effect for the purpose of paying\u00a0excepted employees of the agency.</p><p>The bill must take effect as if it had been enacted on September 30, 2025.\u00a0</p>",
      "updateDate": "2025-10-24",
      "versionCode": "id119hr5801"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5801ih.xml"
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
      "title": "Shutdown Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shutdown Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To appropriate funds for pay and allowances of excepted Federal employees for periods of work performed during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:24Z"
    }
  ]
}
```
