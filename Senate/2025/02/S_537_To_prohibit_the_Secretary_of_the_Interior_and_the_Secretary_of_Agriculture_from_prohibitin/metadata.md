# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/537?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/537
- Title: Protecting Access for Hunters and Anglers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 537
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/537",
    "number": "537",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Protecting Access for Hunters and Anglers Act of 2025",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-12",
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
        "item": [
          {
            "date": "2025-02-12T17:35:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-12T17:35:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "KS"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AK"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "LA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WY"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "OK"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "UT"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AR"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "KS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TN"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "SD"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ND"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AR"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TN"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ND"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "SD"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "SC"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s537is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 537\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Daines (for himself, Mr. Moran , Mr. Sullivan , Mr. Cassidy , Mr. Tillis , Mr. Crapo , Mr. Risch , Ms. Lummis , Mr. Barrasso , Mr. Scott of Florida , Mr. Lankford , Mr. Tuberville , Mr. Lee , Mr. Boozman , Mr. Marshall , Mrs. Blackburn , Mr. Wicker , Mrs. Fischer , Mr. Sheehy , Mr. Rounds , Mrs. Britt , Mr. Cramer , Mr. Cotton , Mr. Justice , Mr. Hagerty , Mr. Hoeven , Mrs. Hyde-Smith , Mr. Thune , Mrs. Capito , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo prohibit the Secretary of the Interior and the Secretary of Agriculture from prohibiting the use of lead ammunition or tackle on certain Federal land or water under the jurisdiction of the Secretary of the Interior and the Secretary of Agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Access for Hunters and Anglers Act of 2025 .\n#### 2. Protecting access for hunters and anglers on Federal land and water\n##### (a) In general\nExcept as provided in section 20.21 or 20.108 of title 50, Code of Federal Regulations (as in effect on the date of enactment of this Act), and subsection (b), the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service or the Director of the Bureau of Land Management, and the Secretary of Agriculture, acting through the Chief of the Forest Service (referred to in this section as the applicable Secretary ), may not\u2014\n**(1)**\nprohibit the use of lead ammunition or tackle on Federal land or water that is\u2014\n**(A)**\nunder the jurisdiction of the applicable Secretary; and\n**(B)**\nmade available for hunting or fishing activities; or\n**(2)**\nissue regulations relating to the level of lead in ammunition or tackle to be used on Federal land or water described in paragraph (1).\n##### (b) Exception\nSubsection (a) shall not apply to a prohibition or regulations described in that subsection that are limited to a specific unit of Federal land or water, if the applicable Secretary determines that\u2014\n**(1)**\na decline in wildlife population at the specific unit of Federal land or water is primarily caused by the use of lead in ammunition or tackle, based on the field data from the specific unit of Federal land or water; and\n**(2)**\nthe prohibition or regulations, as applicable, are\u2014\n**(A)**\nconsistent with the law of the State in which the specific Federal land or water is located;\n**(B)**\nconsistent with an applicable policy of the fish and wildlife department of the State in which the specific Federal land or water is located; or\n**(C)**\napproved by the applicable fish and wildlife department of the State in which the specific Federal land or water is located.\n##### (c) Federal register notice\nThe applicable Secretary shall include in a Federal Register notice with respect to any prohibition or regulations that meet the requirements of paragraphs (1) and (2) of subsection (b) an explanation of how the prohibition or regulations, as applicable, meet those requirements.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2026-03-19",
        "text": "Received in the Senate and Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "556",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Access for Hunters and Anglers Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-04-03T13:35:19Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2026-04-03T13:35:19Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-04-03T13:35:19Z"
          },
          {
            "name": "Metals",
            "updateDate": "2026-04-03T13:35:19Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-04-03T13:35:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T15:11:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s537",
          "measure-number": "537",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s537v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Access for Hunters and Anglers Act of 2025</strong></p><p>This bill bars the Fish and Wildlife Service (FWS), the\u00a0Bureau of Land Management (BLM), and the Forest Service from prohibiting or regulating the use of lead ammunition or tackle on federal land or water. The bill makes exceptions for specified existing regulations and where the FWS, the BLM, or the Forest Service\u00a0determines that a decline in wildlife population at the specific unit of federal land or water is primarily caused by the use of lead in ammunition or tackle, based on the field data from such unit, and the state approves the regulations.</p>"
        },
        "title": "Protecting Access for Hunters and Anglers Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s537.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Access for Hunters and Anglers Act of 2025</strong></p><p>This bill bars the Fish and Wildlife Service (FWS), the\u00a0Bureau of Land Management (BLM), and the Forest Service from prohibiting or regulating the use of lead ammunition or tackle on federal land or water. The bill makes exceptions for specified existing regulations and where the FWS, the BLM, or the Forest Service\u00a0determines that a decline in wildlife population at the specific unit of federal land or water is primarily caused by the use of lead in ammunition or tackle, based on the field data from such unit, and the state approves the regulations.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s537"
    },
    "title": "Protecting Access for Hunters and Anglers Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Access for Hunters and Anglers Act of 2025</strong></p><p>This bill bars the Fish and Wildlife Service (FWS), the\u00a0Bureau of Land Management (BLM), and the Forest Service from prohibiting or regulating the use of lead ammunition or tackle on federal land or water. The bill makes exceptions for specified existing regulations and where the FWS, the BLM, or the Forest Service\u00a0determines that a decline in wildlife population at the specific unit of federal land or water is primarily caused by the use of lead in ammunition or tackle, based on the field data from such unit, and the state approves the regulations.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119s537"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s537is.xml"
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
      "title": "Protecting Access for Hunters and Anglers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of the Interior and the Secretary of Agriculture from prohibiting the use of lead ammunition or tackle on certain Federal land or water under the jurisdiction of the Secretary of the Interior and the Secretary of Agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Access for Hunters and Anglers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:25Z"
    }
  ]
}
```
