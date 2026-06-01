# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/264
- Title: Train EATS Act
- Congress: 119
- Bill type: HR
- Bill number: 264
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-01-14T16:37:29Z
- Update date including text: 2026-01-14T16:37:29Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/264",
    "number": "264",
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
    "title": "Train EATS Act",
    "type": "HR",
    "updateDate": "2026-01-14T16:37:29Z",
    "updateDateIncludingText": "2026-01-14T16:37:29Z"
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
          "date": "2025-01-09T14:35:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-10T15:26:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr264ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 264\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require Amtrak to make traditional dining and an alternative, more affordable food and beverage service available to passengers on overnight routes of Amtrak, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Train Establishment of Appetizing Table Service Act or the Train EATS Act .\n#### 2. Food and beverage service requirements on overnight routes of Amtrak\n##### (a) In general\nChapter 243 of title 49, United States Code, is amended by adding at the end the following new section:\n24324. Food and beverage service requirements on overnight routes of Amtrak. (a) In general On each covered route, Amtrak shall make available\u2014 (1) to the extend practicable, in accordance with subsection (b), traditional dining; and (2) to all passengers an alternative food and beverage service that is more affordable than traditional dining. (b) Priority of traditional dining capacity On each covered route on which traditional dining is available, Amtrak shall offer any traditional dining capacity not otherwise used by passengers in First Class or Business Class to passengers traveling in Coach Class (or other base fare class ticket) for a fee on a first-come, first-serve basis. (c) Traditional dining meal options Amtrak shall ensure that traditional dining on a covered route includes\u2014 (1) a healthy meal option; and (2) upon pre-order from a passenger to whom traditional dining is offered, meals that satisfy the dietary restrictions of the passenger. (d) Regulations The Secretary of Transportation shall issue such regulations as are necessary to carry out this section. (e) Definitions In this section: (1) Covered route The term covered route means a rail passenger transportation route operated by Amtrak that is scheduled to depart and arrive on different dates. (2) Healthy meal option The term healthy meal option means a meal the nutritional contents of which are consistent with the Dietary Guidelines for Americans established under section 301 of the National Nutrition Monitoring and Related Research Act of 1990 ( 7 U.S.C. 5341 ). (3) Traditional dining With respect to rail passenger transportation, the term traditional dining means a food and beverage service\u2014 (A) for which a passenger is seated at a table in a car designated solely for such food and beverage service to order and eat a meal; and (B) that is serviced by wait staff. .\n##### (b) Clerical amendments\nThe analysis for chapter 243 of title 49, United States Code, is amended by adding at the end the following new item:\n24324. Food and beverage service requirements on overnight routes of Amtrak. .",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-14T16:37:28Z"
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
          "measure-id": "id119hr264",
          "measure-number": "264",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr264v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Train Establishment of Appetizing Table Service Act or the Train EATS Act\u00a0</strong></p><p>This bill requires Amtrak to provide a range of dining services to passengers on overnight routes.</p><p>Specifically, Amtrak must make available (1) traditional dining (i.e., table service), to the extent practicable; and (2) an alternative food and beverage service that is more affordable than traditional dining.</p><p>On each overnight route, Amtrak must offer any traditional dining capacity not otherwise used by first-class or business-class passengers\u00a0to passengers in coach class for a fee. </p><p>In addition, Amtrak must ensure that traditional dining on overnight routes includes (1) a healthy meal option, and (2) the option for passengers to preorder meals that satisfy their dietary restrictions.</p><p>The Department of Transportation must issue any necessary regulations.</p>"
        },
        "title": "Train EATS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr264.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Train Establishment of Appetizing Table Service Act or the Train EATS Act\u00a0</strong></p><p>This bill requires Amtrak to provide a range of dining services to passengers on overnight routes.</p><p>Specifically, Amtrak must make available (1) traditional dining (i.e., table service), to the extent practicable; and (2) an alternative food and beverage service that is more affordable than traditional dining.</p><p>On each overnight route, Amtrak must offer any traditional dining capacity not otherwise used by first-class or business-class passengers\u00a0to passengers in coach class for a fee. </p><p>In addition, Amtrak must ensure that traditional dining on overnight routes includes (1) a healthy meal option, and (2) the option for passengers to preorder meals that satisfy their dietary restrictions.</p><p>The Department of Transportation must issue any necessary regulations.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr264"
    },
    "title": "Train EATS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Train Establishment of Appetizing Table Service Act or the Train EATS Act\u00a0</strong></p><p>This bill requires Amtrak to provide a range of dining services to passengers on overnight routes.</p><p>Specifically, Amtrak must make available (1) traditional dining (i.e., table service), to the extent practicable; and (2) an alternative food and beverage service that is more affordable than traditional dining.</p><p>On each overnight route, Amtrak must offer any traditional dining capacity not otherwise used by first-class or business-class passengers\u00a0to passengers in coach class for a fee. </p><p>In addition, Amtrak must ensure that traditional dining on overnight routes includes (1) a healthy meal option, and (2) the option for passengers to preorder meals that satisfy their dietary restrictions.</p><p>The Department of Transportation must issue any necessary regulations.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr264"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr264ih.xml"
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
      "title": "Train EATS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Train EATS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Train Establishment of Appetizing Table Service Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require Amtrak to make traditional dining and an alternative, more affordable food and beverage service available to passengers on overnight routes of Amtrak, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:15Z"
    }
  ]
}
```
