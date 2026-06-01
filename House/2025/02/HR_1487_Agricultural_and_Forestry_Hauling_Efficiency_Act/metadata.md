# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1487
- Title: Agricultural and Forestry Hauling Efficiency Act
- Congress: 119
- Bill type: HR
- Bill number: 1487
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-10-11T08:05:13Z
- Update date including text: 2025-10-11T08:05:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-21 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2025-02-26 - IntroReferral: Sponsor introductory remarks on measure. (CR H845)
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-21 - Committee: Referred to the Subcommittee on Highways and Transit.
- 2025-02-26 - IntroReferral: Sponsor introductory remarks on measure. (CR H845)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1487",
    "number": "1487",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Agricultural and Forestry Hauling Efficiency Act",
    "type": "HR",
    "updateDate": "2025-10-11T08:05:13Z",
    "updateDateIncludingText": "2025-10-11T08:05:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H845)",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:35:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-21T22:26:12Z",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1487ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1487\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. McGuire (for himself and Mr. Wittman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to increase the maximum gross vehicle weight for certain agricultural vehicles operating on a segment of the Interstate System in the Commonwealth of Virginia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agricultural and Forestry Hauling Efficiency Act .\n#### 2. Vehicle weight limitations\nSection 127 of title 23, United States Code, is amended by adding at the end the following:\n(z) Exception for agricultural vehicles in Commonwealth of Virginia (1) In general The Commonwealth of Virginia may allow, by special permit, the operation of a covered agricultural vehicle on the Interstate System in the Commonwealth of Virginia if such vehicle does not exceed 90,000 pounds. (2) Covered agricultural vehicle defined In this subsection, the term covered agricultural vehicle means a vehicle that is transporting unprocessed agricultural crops used for food, feed or fiber, or raw or unfinished forest products, including logs, pulpwood, rough-sawn green lumber, biomass, or wood chips. .",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-14T18:38:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1487",
          "measure-number": "1487",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1487v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Agricultural and Forestry Hauling Efficiency Act</strong></p><p>This bill allows Virginia to increase the vehicle weight limit for covered agricultural vehicles traveling on interstate highways to 90,000 pounds. Specifically, Virginia may provide a special permit for these covered agricultural vehicles\u00a0to operate\u00a0on interstate highways in Virginia.</p><p>The term\u00a0<em>covered agricultural\u00a0vehicle\u00a0</em>means a vehicle that is transporting (1) unprocessed agricultural crops used for food, feed, or fiber; or (2) raw or unfinished forest products, including logs, pulpwood, rough-sawn green lumber, biomass, or wood chips.</p><p>Under current law, there is an\u00a080,000 pound overall gross vehicle weight limit\u00a0for interstate highways,\u00a0with exceptions. Virginia allows certain agricultural vehicles that do not exceed 90,000 pounds to travel on Virginia highways that are not part of the interstate highway system.</p>"
        },
        "title": "Agricultural and Forestry Hauling Efficiency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1487.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Agricultural and Forestry Hauling Efficiency Act</strong></p><p>This bill allows Virginia to increase the vehicle weight limit for covered agricultural vehicles traveling on interstate highways to 90,000 pounds. Specifically, Virginia may provide a special permit for these covered agricultural vehicles\u00a0to operate\u00a0on interstate highways in Virginia.</p><p>The term\u00a0<em>covered agricultural\u00a0vehicle\u00a0</em>means a vehicle that is transporting (1) unprocessed agricultural crops used for food, feed, or fiber; or (2) raw or unfinished forest products, including logs, pulpwood, rough-sawn green lumber, biomass, or wood chips.</p><p>Under current law, there is an\u00a080,000 pound overall gross vehicle weight limit\u00a0for interstate highways,\u00a0with exceptions. Virginia allows certain agricultural vehicles that do not exceed 90,000 pounds to travel on Virginia highways that are not part of the interstate highway system.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr1487"
    },
    "title": "Agricultural and Forestry Hauling Efficiency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Agricultural and Forestry Hauling Efficiency Act</strong></p><p>This bill allows Virginia to increase the vehicle weight limit for covered agricultural vehicles traveling on interstate highways to 90,000 pounds. Specifically, Virginia may provide a special permit for these covered agricultural vehicles\u00a0to operate\u00a0on interstate highways in Virginia.</p><p>The term\u00a0<em>covered agricultural\u00a0vehicle\u00a0</em>means a vehicle that is transporting (1) unprocessed agricultural crops used for food, feed, or fiber; or (2) raw or unfinished forest products, including logs, pulpwood, rough-sawn green lumber, biomass, or wood chips.</p><p>Under current law, there is an\u00a080,000 pound overall gross vehicle weight limit\u00a0for interstate highways,\u00a0with exceptions. Virginia allows certain agricultural vehicles that do not exceed 90,000 pounds to travel on Virginia highways that are not part of the interstate highway system.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr1487"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1487ih.xml"
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
      "title": "Agricultural and Forestry Hauling Efficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T09:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agricultural and Forestry Hauling Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to increase the maximum gross vehicle weight for certain agricultural vehicles operating on a segment of the Interstate System in the Commonwealth of Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:03:26Z"
    }
  ]
}
```
