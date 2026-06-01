# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/265
- Title: Train FOOD Act
- Congress: 119
- Bill type: HR
- Bill number: 265
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-03-18T18:40:05Z
- Update date including text: 2025-03-18T18:40:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-10 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-10 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/265",
    "number": "265",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Train FOOD Act",
    "type": "HR",
    "updateDate": "2025-03-18T18:40:05Z",
    "updateDateIncludingText": "2025-03-18T18:40:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-10",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:36:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-10T15:26:47Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "LA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "GA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NV"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr265ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 265\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require Amtrak to submit to Congress an annual report with respect to the implementation of certain recommendations of the Amtrak Food and Beverage Working Group for improving the food and beverage service of Amtrak, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Train Furtherance of Outstanding Onboard Dining Act or the Train FOOD Act .\n#### 2. Oversight of implementation by Amtrak of recommendations of Amtrak Food and Beverage Working Group\n##### (a) Annual Amtrak report\nSection 24321 of title 49, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (d) as subsection (f); and\n**(2)**\nby inserting after subsection (c) the following new subsections:\n(d) Implementation advisory committee (1) Establishment Not later than 1 year after the date of enactment of the Train Furtherance of Outstanding Onboard Dining Act , Amtrak shall establish an advisory committee to provide internal review with respect to the implementation by Amtrak of the recommendations contained in the report under subsection (b). (2) Membership The advisory committee shall consist of individuals representing\u2014 (A) Amtrak; (B) the labor organizations representing Amtrak employees who prepare or provide on-board food and beverage service; (C) nonprofit organizations representing Amtrak passengers; and (D) States that are providing funding for State-supported routes. (3) Termination The advisory committee shall terminate on the date on which Amtrak submits the final report required under subsection (e)(1). (e) Annual implementation status report (1) Annual report Not later than 1 year after the date of enactment of the Train Furtherance of Outstanding Onboard Dining Act and annually thereafter until such time as all recommendations contained in the report under subsection (b) are implemented by Amtrak or determined by Amtrak to be impractical or impossible to implement, Amtrak shall\u2014 (A) submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report on the status of the implementation of each such recommendation; and (B) make the report available on a publicly accessible website of Amtrak. (2) Report contents Each report under paragraph (1) shall include\u2014 (A) a description of the progress made by Amtrak in implementing each recommendation contained in the report under subsection (b); (B) identification of each such recommendation for which implementation is complete; (C) identification of each such recommendation that Amtrak determines to be impractical or impossible to implement; (D) for each recommendation identified under subparagraph (C)\u2014 (i) the justification for the determination that the recommendation is impractical or impossible to implement; and (ii) if the justification is all, or in part, attributable to insufficient funding, an estimated cost of implementing the recommendation; (E) a description of how, if at all, food and beverage service of Amtrak has changed\u2014 (i) if in the initial report, since the date of enactment of the Train Furtherance of Outstanding Onboard Dining Act ; and (ii) if in a subsequent report, since the date on which the previous report was finalized; and (F) comments submitted by the advisory committee to Amtrak regarding the information included under subparagraphs (A) through (E). .\n##### (b) GAO report\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report describing the progress made by Amtrak in implementing each recommendation contained in the report under section 24321(b) of title 49, United States Code.",
      "versionDate": "2025-01-09",
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
            "name": "Advisory bodies",
            "updateDate": "2025-03-18T18:39:48Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-18T18:39:42Z"
          },
          {
            "name": "Food industry and services",
            "updateDate": "2025-03-18T18:39:34Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-18T18:39:57Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-18T18:40:05Z"
          },
          {
            "name": "National Railroad Passenger Corporation (Amtrak)",
            "updateDate": "2025-03-18T18:39:16Z"
          },
          {
            "name": "Railroads",
            "updateDate": "2025-03-18T18:39:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-07T12:58:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr265",
          "measure-number": "265",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr265v00",
            "update-date": "2025-02-14"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Train Furtherance of Outstanding Onboard Dining Act or the Train FOOD Act</strong></p><p>This bill directs Amtrak to establish an advisory committee to provide internal review for Amtrak's implementation of the Amtrak Food and Beverage Working Group (FBWG)\u00a0recommendations to improve\u00a0onboard food and beverage service.</p><p>The Amtrak advisory committee must submit an annual report to Congress on the status of Amtrak's implementation of each of the FBWG recommendations. The advisory committee's annual reports must be publicly available on an Amtrak website.</p><p>In addition, the Government Accountability Office must submit a report to Congress describing Amtrak's progress in implementing each\u00a0FBWG report\u00a0recommendation.</p>"
        },
        "title": "Train FOOD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr265.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Train Furtherance of Outstanding Onboard Dining Act or the Train FOOD Act</strong></p><p>This bill directs Amtrak to establish an advisory committee to provide internal review for Amtrak's implementation of the Amtrak Food and Beverage Working Group (FBWG)\u00a0recommendations to improve\u00a0onboard food and beverage service.</p><p>The Amtrak advisory committee must submit an annual report to Congress on the status of Amtrak's implementation of each of the FBWG recommendations. The advisory committee's annual reports must be publicly available on an Amtrak website.</p><p>In addition, the Government Accountability Office must submit a report to Congress describing Amtrak's progress in implementing each\u00a0FBWG report\u00a0recommendation.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr265"
    },
    "title": "Train FOOD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Train Furtherance of Outstanding Onboard Dining Act or the Train FOOD Act</strong></p><p>This bill directs Amtrak to establish an advisory committee to provide internal review for Amtrak's implementation of the Amtrak Food and Beverage Working Group (FBWG)\u00a0recommendations to improve\u00a0onboard food and beverage service.</p><p>The Amtrak advisory committee must submit an annual report to Congress on the status of Amtrak's implementation of each of the FBWG recommendations. The advisory committee's annual reports must be publicly available on an Amtrak website.</p><p>In addition, the Government Accountability Office must submit a report to Congress describing Amtrak's progress in implementing each\u00a0FBWG report\u00a0recommendation.</p>",
      "updateDate": "2025-02-14",
      "versionCode": "id119hr265"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr265ih.xml"
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
      "title": "Train FOOD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Train FOOD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Train Furtherance of Outstanding Onboard Dining Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require Amtrak to submit to Congress an annual report with respect to the implementation of certain recommendations of the Amtrak Food and Beverage Working Group for improving the food and beverage service of Amtrak, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:18Z"
    }
  ]
}
```
