# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/912?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/912
- Title: Securing American Agriculture Act
- Congress: 119
- Bill type: S
- Bill number: 912
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2026-05-20T11:03:28Z
- Update date including text: 2026-05-20T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/912",
    "number": "912",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Securing American Agriculture Act",
    "type": "S",
    "updateDate": "2026-05-20T11:03:28Z",
    "updateDateIncludingText": "2026-05-20T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-10",
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
            "date": "2025-03-10T20:01:21Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-10T20:01:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ID"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WV"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MO"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
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
      "sponsorshipDate": "2025-03-10",
      "state": "WY"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "GA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-05",
      "state": "PA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s912is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 912\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mr. Ricketts (for himself, Mr. Risch , Mrs. Capito , Mr. Schmitt , Mr. Crapo , Ms. Lummis , Mrs. Fischer , Mr. Barrasso , Mr. Scott of Florida , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo direct the Secretary of Agriculture to publish, on an annual basis, an assessment of United States dependency on critical agricultural products or inputs from the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing American Agriculture Act .\n#### 2. Critical agricultural products or inputs assessment\n##### (a) In general\nOn an annual basis, the Secretary of Agriculture (referred to in this section as the Secretary ) shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives an assessment of the dependency of the United States on critical agricultural products or inputs that could be exploited in the event the People\u2019s Republic of China weaponizes any such dependency.\n##### (b) Contents\nEach report under subsection (a) shall\u2014\n**(1)**\naddress, with respect to the critical inputs described in subsection (c)\u2014\n**(A)**\nthe current domestic production capacity of each critical input; and\n**(B)**\nthe current and potential bottlenecks in the supply chain for each critical input that could be exploited by the People\u2019s Republic of China; and\n**(2)**\ncontain recommendations of the Secretary, in consultation with the United States Trade Representative, the Secretary of Commerce, and the Commissioner of Food and Drugs, to reduce the dependency of the United States on the People\u2019s Republic of China to supply critical agricultural products or inputs, including recommendations\u2014\n**(A)**\nto mitigate potential threats posed by the People\u2019s Republic of China to the supply chains of each critical input described in subsection (c); and\n**(B)**\nfor legislative and regulatory actions to reduce barriers to onshore or nearshore production of each such critical input.\n##### (c) Description of critical inputs\nThe critical inputs referred to in subsection (b) include all farm management, agronomic, and field-applied production inputs, including each of the following:\n**(1)**\nAgricultural equipment, machinery, and technology.\n**(2)**\nFuel.\n**(3)**\nFertilizers.\n**(4)**\nFeed, including its components, such as vitamins, amino acids, and minerals.\n**(5)**\nVeterinary drugs and vaccines.\n**(6)**\nCrop protection chemicals.\n**(7)**\nSeed.\n**(8)**\nAny other critical agricultural inputs, as determined by the Secretary.\n##### (d) Collection, distribution, and protection of information\n**(1) Voluntary basis**\nIn conducting an assessment under subsection (a), the Secretary shall not require any private entity to provide information to the Secretary.\n**(2) Aggregate data**\nIn the case of information provided to the Secretary to conduct an assessment under subsection (a), the Secretary, any other officer or employee of the Department of Agriculture or agency thereof, or any other person shall not\u2014\n**(A)**\nuse that information for a purpose other than the development or reporting of aggregate data in a manner such that the identity of the person that supplied the information is not\u2014\n**(i)**\ndiscernible; or\n**(ii)**\nmaterial to the intended uses of the information; or\n**(B)**\ndisclose that information to the public, unless the information has been transformed into a statistical or aggregate form that does not allow the identification of the person that supplied particular information.\n**(3) Confidentiality**\nThe Secretary shall ensure that the assessments under subsection (a) do not include any information that is a trade secret or confidential information subject to\u2014\n**(A)**\nsection 552(b)(4) of title 5, United States Code; or\n**(B)**\nsection 1905 of title 18, United States Code.\n**(4) Immunity from disclosure**\nInformation provided to the Secretary as part of an assessment conducted under subsection (a) shall not be used by the Secretary for any purpose other than to carry out that subsection.",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T16:50:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119s912",
          "measure-number": "912",
          "measure-type": "s",
          "orig-publish-date": "2025-03-10",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s912v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Securing American Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to assess, on an annual basis, U.S. dependency on critical agricultural products or inputs that could be exploited in the event that China weaponizes such a dependency.\u00a0USDA must submit a report to Congress on the assessment, which must\u00a0include recommendations to reduce U.S. dependency on China to supply critical agricultural products or inputs.</p><p>Under the bill, critical inputs include all farm management, agronomic, and field-applied production inputs (e.g., agricultural equipment, fertilizers, veterinary drugs, and seed).</p><p>The bill specifies that, in conducting the assessment, USDA may not require a private entity to provide information to USDA. Further, the bill requires USDA to comply with certain confidentiality requirements and restricts disclosures of the information.</p>"
        },
        "title": "Securing American Agriculture Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s912.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing American Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to assess, on an annual basis, U.S. dependency on critical agricultural products or inputs that could be exploited in the event that China weaponizes such a dependency.\u00a0USDA must submit a report to Congress on the assessment, which must\u00a0include recommendations to reduce U.S. dependency on China to supply critical agricultural products or inputs.</p><p>Under the bill, critical inputs include all farm management, agronomic, and field-applied production inputs (e.g., agricultural equipment, fertilizers, veterinary drugs, and seed).</p><p>The bill specifies that, in conducting the assessment, USDA may not require a private entity to provide information to USDA. Further, the bill requires USDA to comply with certain confidentiality requirements and restricts disclosures of the information.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s912"
    },
    "title": "Securing American Agriculture Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Securing American Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to assess, on an annual basis, U.S. dependency on critical agricultural products or inputs that could be exploited in the event that China weaponizes such a dependency.\u00a0USDA must submit a report to Congress on the assessment, which must\u00a0include recommendations to reduce U.S. dependency on China to supply critical agricultural products or inputs.</p><p>Under the bill, critical inputs include all farm management, agronomic, and field-applied production inputs (e.g., agricultural equipment, fertilizers, veterinary drugs, and seed).</p><p>The bill specifies that, in conducting the assessment, USDA may not require a private entity to provide information to USDA. Further, the bill requires USDA to comply with certain confidentiality requirements and restricts disclosures of the information.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s912"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s912is.xml"
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
      "title": "Securing American Agriculture Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Agriculture to publish, on an annual basis, an assessment of United States dependency on critical agricultural products or inputs from the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:33:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing American Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    }
  ]
}
```
