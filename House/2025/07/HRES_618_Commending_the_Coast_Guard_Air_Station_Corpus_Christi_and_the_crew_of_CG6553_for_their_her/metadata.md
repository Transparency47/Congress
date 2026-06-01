# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/618?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/618
- Title: Commending the Coast Guard, Air Station Corpus Christi, and the crew of CG-6553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas.
- Congress: 119
- Bill type: HRES
- Bill number: 618
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-04-07T10:31:49Z
- Update date including text: 2026-04-07T10:31:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-30 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-07-29: Submitted in House

## Actions

- 2025-07-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-29 - IntroReferral: Submitted in House
- 2025-07-30 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/618",
    "number": "618",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Commending the Coast Guard, Air Station Corpus Christi, and the crew of CG-6553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas.",
    "type": "HRES",
    "updateDate": "2026-04-07T10:31:49Z",
    "updateDateIncludingText": "2026-04-07T10:31:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-07-29T21:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-30T21:31:48Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "MO"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "LA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres618ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 618\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Cloud (for himself, Mr. Crenshaw , Mr. Graves , Mr. Williams of Texas , Mrs. Fletcher , Mr. Lawler , Ms. Johnson of Texas , Mr. Tony Gonzales of Texas , Mr. Carter of Texas , Mr. McCaul , Mr. Higgins of Louisiana , Mr. Babin , Mr. Cuellar , Mr. Green of Texas , Mr. Veasey , and Ms. Crockett ) submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nCommending the Coast Guard, Air Station Corpus Christi, and the crew of CG\u20136553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas.\nThat the House of Representatives\u2014\n**(1)**\ncommends the Coast Guard for its courageous and swift response to the flooding disaster in Texas;\n**(2)**\nexpresses its profound and deep appreciation for the extraordinary Coast Guard members who risked their lives to save hundreds from the floods; and\n**(3)**\nextends its deepest gratitude to all of the Federal, State, and local first responders and volunteers who have responded to this horrific tragedy to help Texas in its time of need.",
      "versionDate": "2025-07-29",
      "versionType": "IH"
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
        "updateDate": "2025-09-10T16:59:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119hres618",
          "measure-number": "618",
          "measure-type": "hres",
          "orig-publish-date": "2025-07-29",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres618v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution commends the Coast Guard for its courageous and swift response to the July 2025 flooding disaster in Texas.</p><p>It also extends gratitude to all of the federal, state, and local first responders and volunteers who responded to this tragedy.</p>"
        },
        "title": "Commending the Coast Guard, Air Station Corpus Christi, and the crew of CG-6553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres618.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution commends the Coast Guard for its courageous and swift response to the July 2025 flooding disaster in Texas.</p><p>It also extends gratitude to all of the federal, state, and local first responders and volunteers who responded to this tragedy.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres618"
    },
    "title": "Commending the Coast Guard, Air Station Corpus Christi, and the crew of CG-6553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas."
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution commends the Coast Guard for its courageous and swift response to the July 2025 flooding disaster in Texas.</p><p>It also extends gratitude to all of the federal, state, and local first responders and volunteers who responded to this tragedy.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres618"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres618ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Commending the Coast Guard, Air Station Corpus Christi, and the crew of CG-6553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T13:03:25Z"
    },
    {
      "title": "Commending the Coast Guard, Air Station Corpus Christi, and the crew of CG-6553 for their heroic efforts and courageous response to the catastrophic flooding across central Texas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:11Z"
    }
  ]
}
```
