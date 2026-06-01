# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2514?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2514
- Title: Trucker Bathroom Access Act
- Congress: 119
- Bill type: HR
- Bill number: 2514
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-05-30T08:05:41Z
- Update date including text: 2026-05-30T08:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-31 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-31 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2514",
    "number": "2514",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Trucker Bathroom Access Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:41Z",
    "updateDateIncludingText": "2026-05-30T08:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-31T21:17:38Z",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WI"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "KS"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "NV"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "IL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
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
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NH"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NJ"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2514ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2514\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Nehls (for himself, Ms. Houlahan , Ms. Scholten , and Mr. Babin ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, with respect to restroom access for certain drivers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Trucker Bathroom Access Act .\n#### 2. Restroom access for drivers\n##### (a) In general\nSubchapter I of chapter 141 of title 49, United States Code, is amended by adding at the end the following:\n14105. Restroom access for drivers (a) In general A covered driver shall be granted access to any covered restroom facility at any covered establishment to which such employee delivers any goods or cargo or is waiting to be loaded to transport goods or cargo. (b) Rule of construction Nothing in this section shall be construed to require a covered establishment to make any physical changes to a restroom to be in compliance with this section. (c) Definitions In this section: (1) Covered driver The term covered driver means any commercial motor vehicle operator with respect to whom the Secretary of Transportation has power to establish qualifications and maximum hours of service pursuant to the provisions of section 31502. (2) Covered restroom facility The term covered restroom facility means a restroom located on the premises of a covered establishment that is intended for use by customers or employees of the establishment and that is\u2014 (A) located in an area where providing access would not create an obvious health or safety risk to a covered driver; and (B) located in an area where providing access would not pose an obvious security risk to the covered establishment. (3) Covered establishment The term covered establishment \u2014 (A) means a place of business open to the general public for the sale of goods or services; (B) a shipper, receiver, manufacturer, warehouse, distribution center, or any other business entity that is receiving or sending goods by commercial motor vehicle; and (C) does not include any structure such as a filling station, service station, or restaurant of 800 square feet or less that has a restroom located within such structure that is only intended for use by employees. .\n##### (b) Clerical amendment\nThe analysis for chapter 141 of title 49, United States Code, is amended by inserting after the item relating to section 14104 the following new item:\n14105. Restroom access for drivers. .\n#### 3. Restroom access for drayage truck operators\n##### (a) In general\nA terminal operator shall provide a sufficient number of covered restrooms for use by covered drayage truck operators in areas of the terminal that such operators typically have access to.\n##### (b) Requirements\nTo be in compliance with subsection (a), a terminal operator shall provide\u2014\n**(1)**\naccess to existing restrooms while covered drayage truck operators are on port property and when such access does not pose an obvious safety risk to such truck operators and other employees of the terminal operator in the area;\n**(2)**\nadditional restrooms, if necessary, at locations where there is the most need; and\n**(3)**\na place for covered drayage truck operators to park vehicles while accessing such restrooms.\n##### (c) Definitions\nIn this section:\n**(1) Covered drayage truck operator**\nThe term covered drayage truck operator means the driver of any in-use on-road vehicle with a gross vehicle weight rating of greater than 33,000 pounds operating on or transgressing through port or intermodal rail yard property for the purpose of loading, unloading, or transporting cargo, including containerized, bulk, or break-bulk goods.\n**(2) Terminal operator**\nThe term terminal operator \u2014\n**(A)**\nmeans the business entity operating a marine terminal for loading and unloading cargo to and from marine vessels; and\n**(B)**\nincludes the port authority if the port is directly operating the marine terminal in loading and unloading cargo to and from marine vessels.\n**(3) Covered restroom**\nThe term covered restroom means a restroom or portable chemical toilet that is located in an area that does not pose an obvious health or safety risk to a covered drayage truck operator.",
      "versionDate": "2025-03-31",
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
        "updateDate": "2025-04-07T13:14:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2514",
          "measure-number": "2514",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2025-06-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2514v00",
            "update-date": "2025-06-30"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Trucker Bathroom Access Act</strong></p><p>This bill expands access to restroom facilities for certain commercial truck drivers, including drayage truck operators.</p><p><em>Drayage truck operator</em> means the driver of any in-use on-road vehicle with a gross vehicle weight rating of greater than 33,000 pounds operating on or transgressing through port or intermodal rail yard property for the purpose of loading, unloading, or transporting cargo, including containerized, bulk, or break-bulk goods.</p><p>Specifically, the bill requires certain retailers, warehouses, and other establishments to give commercial truck drivers access to existing restroom facilities when they are loading or delivering cargo, or waiting to load or transport cargo.</p><p>Further, operators of\u00a0marine terminals, including port authorities, must provide drayage truck operators with (1) access to existing restrooms, (2) additional restrooms if necessary, and (3) parking while accessing such restrooms.\u00a0</p>"
        },
        "title": "Trucker Bathroom Access Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2514.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Trucker Bathroom Access Act</strong></p><p>This bill expands access to restroom facilities for certain commercial truck drivers, including drayage truck operators.</p><p><em>Drayage truck operator</em> means the driver of any in-use on-road vehicle with a gross vehicle weight rating of greater than 33,000 pounds operating on or transgressing through port or intermodal rail yard property for the purpose of loading, unloading, or transporting cargo, including containerized, bulk, or break-bulk goods.</p><p>Specifically, the bill requires certain retailers, warehouses, and other establishments to give commercial truck drivers access to existing restroom facilities when they are loading or delivering cargo, or waiting to load or transport cargo.</p><p>Further, operators of\u00a0marine terminals, including port authorities, must provide drayage truck operators with (1) access to existing restrooms, (2) additional restrooms if necessary, and (3) parking while accessing such restrooms.\u00a0</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2514"
    },
    "title": "Trucker Bathroom Access Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Trucker Bathroom Access Act</strong></p><p>This bill expands access to restroom facilities for certain commercial truck drivers, including drayage truck operators.</p><p><em>Drayage truck operator</em> means the driver of any in-use on-road vehicle with a gross vehicle weight rating of greater than 33,000 pounds operating on or transgressing through port or intermodal rail yard property for the purpose of loading, unloading, or transporting cargo, including containerized, bulk, or break-bulk goods.</p><p>Specifically, the bill requires certain retailers, warehouses, and other establishments to give commercial truck drivers access to existing restroom facilities when they are loading or delivering cargo, or waiting to load or transport cargo.</p><p>Further, operators of\u00a0marine terminals, including port authorities, must provide drayage truck operators with (1) access to existing restrooms, (2) additional restrooms if necessary, and (3) parking while accessing such restrooms.\u00a0</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2514"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2514ih.xml"
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
      "title": "Trucker Bathroom Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Trucker Bathroom Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, with respect to restroom access for certain drivers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:38Z"
    }
  ]
}
```
