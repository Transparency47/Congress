# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6803
- Title: To designate Newark Penn Station in Newark, New Jersey as the "Donald M. Payne, Jr. Transit Center at Newark Penn Station".
- Congress: 119
- Bill type: HR
- Bill number: 6803
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-04-06T13:55:36Z
- Update date including text: 2026-04-06T13:55:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-17 - IntroReferral: Sponsor introductory remarks on measure. (CR H6013)
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-17 - IntroReferral: Sponsor introductory remarks on measure. (CR H6013)
- 2026-02-02 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6803",
    "number": "6803",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001229",
        "district": "10",
        "firstName": "LaMonica",
        "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
        "lastName": "McIver",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To designate Newark Penn Station in Newark, New Jersey as the \"Donald M. Payne, Jr. Transit Center at Newark Penn Station\".",
    "type": "HR",
    "updateDate": "2026-04-06T13:55:36Z",
    "updateDateIncludingText": "2026-04-06T13:55:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H6013)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:42:42Z",
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
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6803ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6803\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mrs. McIver (for herself, Mr. Norcross , Mr. Van Drew , Mr. Conaway , Mr. Smith of New Jersey , Mr. Gottheimer , Mr. Pallone , Mr. Kean , Mr. Menendez , Ms. Pou , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo designate Newark Penn Station in Newark, New Jersey as the Donald M. Payne, Jr. Transit Center at Newark Penn Station .\n#### 1. Findings\nCongress finds the following:\n**(1)**\nCongressman Donald M. Payne, Jr. served the people of New Jersey with distinction as a Member of the United States House of Representatives from 2012 until his passing in 2024, representing New Jersey\u2019s 10th Congressional District with deep dedication and integrity.\n**(2)**\nA native of Newark, New Jersey, Congressman Payne, Jr. was a lifelong public servant. Congressman Payne, Jr. got his start with the New Jersey Highway Authority, later served on the Essex County Board of Freeholders, and eventually rose to become President of the Newark City Council in New Jersey. In these roles, as in Congress, he built a reputation as a champion for public health, transportation access, and social justice.\n**(3)**\nIn his time representing New Jersey\u2019s 10th Congressional District, Congressman Payne, Jr. was a tireless advocate for infrastructure investment and public transit, serving as the Chairman and Ranking Member of the House Committee on Transportation and Infrastructure\u2019s subcommittee on Railroads, Pipelines, and Hazardous Materials.\n**(4)**\nCongressman Payne, Jr. was instrumental in securing Federal funding for improvements to Newark Penn Station, one of the most critical transportation hubs in the Northeast, recognizing its importance to the connectivity and economic vitality of the region.\n**(5)**\nIn addition to his legislative work, Congressman Payne, Jr. was known for his humor, devotion to his family, and signature colorful bow ties. A friend to many, he consistently brought the voices of those too often unheard to the halls of Congress, and worked to extend the founding promises of our Nation to all New Jerseyans.\n**(6)**\nRedesignating Newark Penn Station in Congressman Payne Jr.\u2019s honor is a fitting tribute to a public servant who helped secure pivotal investments in our Nation\u2019s railways and the City of Newark, New Jersey.\n#### 2. Donald M. Payne, Jr. Transit Center at Newark Penn Station\n##### (a) Designation\nNewark Penn Station, located at 1 Raymond Plaza West, Newark, New Jersey, shall be known and designated as the Donald M. Payne, Jr. Transit Center at Newark Penn Station .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to Newark Penn Station shall be deemed to be a reference to the Donald M. Payne, Jr. Transit Center at Newark Penn Station .",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-22T15:09:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-17",
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
          "measure-id": "id119hr6803",
          "measure-number": "6803",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6803v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-12-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill designates Newark Penn Station in Newark, New Jersey, as the Donald M. Payne, Jr. Transit Center at Newark Penn Station.</p><p>Donald Payne Jr. served in the House of Representatives from 2012 until his death in\u00a02024.</p>"
        },
        "title": "To designate Newark Penn Station in Newark, New Jersey as the \"Donald M. Payne, Jr. Transit Center at Newark Penn Station\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6803.xml",
    "summary": {
      "actionDate": "2025-12-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates Newark Penn Station in Newark, New Jersey, as the Donald M. Payne, Jr. Transit Center at Newark Penn Station.</p><p>Donald Payne Jr. served in the House of Representatives from 2012 until his death in\u00a02024.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6803"
    },
    "title": "To designate Newark Penn Station in Newark, New Jersey as the \"Donald M. Payne, Jr. Transit Center at Newark Penn Station\"."
  },
  "summaries": [
    {
      "actionDate": "2025-12-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill designates Newark Penn Station in Newark, New Jersey, as the Donald M. Payne, Jr. Transit Center at Newark Penn Station.</p><p>Donald Payne Jr. served in the House of Representatives from 2012 until his death in\u00a02024.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6803"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6803ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate Newark Penn Station in Newark, New Jersey as the \"Donald M. Payne, Jr. Transit Center at Newark Penn Station\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:33Z"
    },
    {
      "title": "To designate Newark Penn Station in Newark, New Jersey as the \"Donald M. Payne, Jr. Transit Center at Newark Penn Station\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T09:07:24Z"
    }
  ]
}
```
