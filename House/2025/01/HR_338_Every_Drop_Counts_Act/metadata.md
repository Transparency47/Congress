# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/338
- Title: Every Drop Counts Act
- Congress: 119
- Bill type: HR
- Bill number: 338
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-11-20T09:06:36Z
- Update date including text: 2025-11-20T09:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-11-19 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-11-19 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/338",
    "number": "338",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Every Drop Counts Act",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:36Z",
    "updateDateIncludingText": "2025-11-20T09:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-19T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-12T21:42:57Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "ID"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "ID"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr338ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 338\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Costa (for himself, Mr. Fulcher , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to increase surface water and groundwater storage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Every Drop Counts Act .\n#### 2. Eligible water storage projects\n##### (a) In general\nSubparagraph (B) of section 40903(b)(1) of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3203(b)(1)(B) ) is amended to read as follows:\n(B) Eligible projects The following projects shall be eligible for consideration for a grant under this section: (i) General acre-feet capacity A project that\u2014 (I) has water storage capacity of not less than 200 acre-feet and not more than 30,000 acre-feet; and (II) (aa) increases surface water or groundwater storage; or (bb) conveys water, directly or indirectly, to or from surface water or groundwater storage. (ii) Average annual project life acre-feet capacity A project that\u2014 (I) has water storage capacity of recharges not less than 200 acre-feet and not more than 150,000 acre-feet on an average annual basis over the life of the project for storage or use; and (II) (aa) increases groundwater aquifer storage; (bb) conveys water, directly or indirectly, to or recovers water from groundwater storage; (cc) both increases groundwater aquifer storage and conveys water, directly or indirectly, to or recovers water from groundwater storage; and (dd) stabilizes groundwater levels. .\n##### (b) Authority\nSection 40903(e) of the Infrastructure Investment and Jobs Act ( 43 U.S.C. 3203(e) ) is amended by striking 5 and inserting 10 .\n#### 3. Statutory construction\nNothing in the amendment made by section 2 shall be construed\u2014\n**(1)**\nto supersede or in any manner affect or conflict with State water law, Federal water law, interstate compacts, or treaty obligations;\n**(2)**\nto authorize any acquisition of water by the Federal Government; or\n**(3)**\nto supersede or infringe on any water rights.",
      "versionDate": "2025-01-13",
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
            "name": "Water resources funding",
            "updateDate": "2025-03-03T18:10:11Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2025-03-03T18:10:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-02-18T20:30:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr338",
          "measure-number": "338",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr338v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Every Drop Counts Act</strong></p><p>This bill expands the Bureau of Reclamation's Small Storage Program, which is a grant program for small surface water or groundwater storage projects in certain western states.</p><p>First, the bill expands the types of projects that are eligible for grants under the program. Specifically, the bill makes a project eligible for a grant if the project (1) has water storage capacity of recharges no less than 200 acre-feet and no more than 150,000 acre-feet on an average annual basis over the life of the project for storage or use; and (2) increases groundwater aquifer storage, conveys water to or recovers water from groundwater storage, and stabilizes groundwater levels.</p><p>Next, it extends Reclamation's authority to carry out the grant program for another five years.</p>"
        },
        "title": "Every Drop Counts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr338.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Every Drop Counts Act</strong></p><p>This bill expands the Bureau of Reclamation's Small Storage Program, which is a grant program for small surface water or groundwater storage projects in certain western states.</p><p>First, the bill expands the types of projects that are eligible for grants under the program. Specifically, the bill makes a project eligible for a grant if the project (1) has water storage capacity of recharges no less than 200 acre-feet and no more than 150,000 acre-feet on an average annual basis over the life of the project for storage or use; and (2) increases groundwater aquifer storage, conveys water to or recovers water from groundwater storage, and stabilizes groundwater levels.</p><p>Next, it extends Reclamation's authority to carry out the grant program for another five years.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr338"
    },
    "title": "Every Drop Counts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Every Drop Counts Act</strong></p><p>This bill expands the Bureau of Reclamation's Small Storage Program, which is a grant program for small surface water or groundwater storage projects in certain western states.</p><p>First, the bill expands the types of projects that are eligible for grants under the program. Specifically, the bill makes a project eligible for a grant if the project (1) has water storage capacity of recharges no less than 200 acre-feet and no more than 150,000 acre-feet on an average annual basis over the life of the project for storage or use; and (2) increases groundwater aquifer storage, conveys water to or recovers water from groundwater storage, and stabilizes groundwater levels.</p><p>Next, it extends Reclamation's authority to carry out the grant program for another five years.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr338"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr338ih.xml"
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
      "title": "Every Drop Counts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Every Drop Counts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to increase surface water and groundwater storage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:24Z"
    }
  ]
}
```
