# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1995
- Title: Securing American Agriculture Act
- Congress: 119
- Bill type: HR
- Bill number: 1995
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-05-20T08:08:16Z
- Update date including text: 2026-05-20T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1995",
    "number": "1995",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Securing American Agriculture Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:16Z",
    "updateDateIncludingText": "2026-05-20T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:54:28Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "HI"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "KS"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IN"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MO"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "VA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NE"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "PA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1995ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1995\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Hinson (for herself, Mr. Krishnamoorthi , Mr. Moolenaar , Ms. Tokuda , Mr. Scott Franklin of Florida , Ms. Davids of Kansas , Mr. Newhouse , Mr. Carson , Mr. Alford , Mr. Cline , Mr. Finstad , Mrs. Miller-Meeks , and Mr. Moore of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo direct the Secretary of Agriculture to publish, on an annual basis, an assessment on United States dependency on critical agricultural products or inputs from the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing American Agriculture Act .\n#### 2. Critical agricultural products or inputs study\n##### (a) In general\nThe Secretary of Agriculture (in this section referred to as the Secretary ) shall, on an annual basis, submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate, an assessment of the dependency of the United States on critical agricultural products or inputs that could be exploited in the event the People\u2019s Republic of China weaponizes any such critical dependency.\n##### (b) Contents\nThe assessment under subsection (a) shall\u2014\n**(1)**\naddress, with respect to the critical inputs specified in subsection (c), the following:\n**(A)**\nthe current domestic production capacity of each such critical input; and\n**(B)**\nthe current and potential bottlenecks in the supply chain for each such critical input that could be exploited by the People\u2019s Republic of China; and\n**(2)**\ncontain the Secretary\u2019s recommendations to reduce the dependency of the United States on the People\u2019s Republic of China to supply critical agricultural products or inputs, including\u2014\n**(A)**\nrecommendations to mitigate potential threats posed by the People\u2019s Republic of China to the supply chains of each critical input specified in subsection (c); and\n**(B)**\nrecommendations for legislative and regulatory actions to reduce barriers to onshore or nearshore the production of each such critical input.\n##### (c) Critical inputs\nThe critical inputs specified in this subsection shall include all farm management, agronomic, and field-applied production inputs, including each of the following:\n**(1)**\nAgricultural equipment, machinery, and technology.\n**(2)**\nFuel.\n**(3)**\nFertilizers.\n**(4)**\nFeed, including its components, such as vitamins, amino acids, and minerals.\n**(5)**\nVeterinary drugs and vaccines.\n**(6)**\nCrop protection chemicals.\n**(7)**\nSeed.\n**(8)**\nAny other critical agricultural inputs, as determined by the Secretary.\n##### (d) Collection, distribution, and protection of information\n**(1) Voluntary basis**\nIn conducting an assessment under subsection (a), the Secretary may not require any private entity to provide information to the Secretary.\n**(2) Aggregate data**\nIn the case of information provided to the Secretary to conduct an assessment under subsection (a), neither the Secretary, any other officer or employee of the Department of Agriculture or agency thereof, nor any other person may\u2014\n**(A)**\nuse such information for a purpose other than the development or reporting of aggregate data in a manner such that the identity of the person who supplied such information is not discernible and is not material to the intended uses of such information; or\n**(B)**\ndisclose such information to the public, unless such information has been transformed into a statistical or aggregate form that does not allow the identification of the person who supplied particular information.\n**(3) Confidentiality**\nThe Secretary shall ensure that assessments submitted under subsection (a) do not include any information that is a trade secret or confidential information subject to section 552(b)(4) of title 5, United States Code, or section 1905 of title 18, United States Code.\n**(4) Immunity from disclosure**\nAny information provided to the Secretary as part of an assessment conducted under subsection (a) may not be used by the Secretary for any purpose other than to carry out such subsection.",
      "versionDate": "2025-03-10",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T16:49:06Z"
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
          "measure-id": "id119hr1995",
          "measure-number": "1995",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1995v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Securing American Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to assess, on an annual basis, U.S. dependency on critical agricultural products or inputs that could be exploited in the event that China weaponizes such a dependency.\u00a0USDA must submit a report to Congress on the assessment, which must\u00a0include recommendations to reduce U.S. dependency on China to supply critical agricultural products or inputs.\u00a0</p><p>Under the bill, critical inputs include all farm management, agronomic, and field-applied production inputs (e.g., agricultural equipment, fertilizers, veterinary drugs, and seed).</p><p>The bill specifies that, in conducting the assessment, USDA may not require a private entity to provide information to USDA. Further, the bill requires USDA to comply with certain confidentiality requirements and restricts disclosures of the information.\u00a0\u00a0</p>"
        },
        "title": "Securing American Agriculture Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1995.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing American Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to assess, on an annual basis, U.S. dependency on critical agricultural products or inputs that could be exploited in the event that China weaponizes such a dependency.\u00a0USDA must submit a report to Congress on the assessment, which must\u00a0include recommendations to reduce U.S. dependency on China to supply critical agricultural products or inputs.\u00a0</p><p>Under the bill, critical inputs include all farm management, agronomic, and field-applied production inputs (e.g., agricultural equipment, fertilizers, veterinary drugs, and seed).</p><p>The bill specifies that, in conducting the assessment, USDA may not require a private entity to provide information to USDA. Further, the bill requires USDA to comply with certain confidentiality requirements and restricts disclosures of the information.\u00a0\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr1995"
    },
    "title": "Securing American Agriculture Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Securing American Agriculture Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to assess, on an annual basis, U.S. dependency on critical agricultural products or inputs that could be exploited in the event that China weaponizes such a dependency.\u00a0USDA must submit a report to Congress on the assessment, which must\u00a0include recommendations to reduce U.S. dependency on China to supply critical agricultural products or inputs.\u00a0</p><p>Under the bill, critical inputs include all farm management, agronomic, and field-applied production inputs (e.g., agricultural equipment, fertilizers, veterinary drugs, and seed).</p><p>The bill specifies that, in conducting the assessment, USDA may not require a private entity to provide information to USDA. Further, the bill requires USDA to comply with certain confidentiality requirements and restricts disclosures of the information.\u00a0\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr1995"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1995ih.xml"
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
      "title": "Securing American Agriculture Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing American Agriculture Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to publish, on an annual basis, an assessment on United States dependency on critical agricultural products or inputs from the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:28Z"
    }
  ]
}
```
