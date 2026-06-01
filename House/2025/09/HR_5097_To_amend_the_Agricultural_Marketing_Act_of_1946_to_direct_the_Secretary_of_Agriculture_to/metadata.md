# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5097?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5097
- Title: To amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment.
- Congress: 119
- Bill type: HR
- Bill number: 5097
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2026-04-14T08:05:49Z
- Update date including text: 2026-04-14T08:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5097",
    "number": "5097",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment.",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:49Z",
    "updateDateIncludingText": "2026-04-14T08:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5097ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5097\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Mr. Valadao (for himself, Mr. Costa , Ms. Brownley , Mr. Panetta , Mr. LaMalfa , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment.\n#### 1. Automation and mechanization grants for specialty crops producers\nSubtitle A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1621 et seq. ) is amended by adding at the end the following:\n210B. Automation and mechanization grants (a) In general For purposes of enhancing the competitiveness of specialty crop producers in the United States, the Secretary of Agriculture, acting through the Administrator of the Agricultural Marketing Service, shall establish a program under which the Secretary will award grants to eligible entities to acquire certain equipment and provide training with respect to the use of such equipment. (b) Use of funds An eligible entity receiving a grant under this section shall use funds received through the grant\u2014 (1) to acquire mechanized or automated systems and tools that increase the efficiency of a task or reduce human labor for a specific activity, as determined by the Secretary; and (2) to provide training, including worker training, and other professional services required to learn how to deploy and effectively operate such systems and tools, as determined by the Secretary. (c) Amount of grants To the maximum extent practicable, the Secretary shall seek to ensure that the amount of a grant awarded to a single eligible entity is sufficient to provide a significant offset to the costs such eligible entity incurs in carrying out the activities specified in subsection (b). (d) Matching funds requirement The recipient of a grant under this section shall provide non-Federal matching funds equal to not less than 50 percent of the amount of the grant. (e) Definitions In this section: (1) Mechanized or automated systems and tools The term mechanized or automated systems and tools includes\u2014 (A) low dust harvesting tools and equipment; (B) grinding and chipping tools and equipment; (C) sorting machines; (D) phytosanitary, infrared, and pasteurization tools and equipment; (E) traceability tools and equipment; (F) storage and warehousing tools and equipment; (G) drones for monitoring commodity piles and feedstuff for cattle; (H) hedgers or shredders; (I) wireless, networks, and connectivity equipment to support IoT devices; (J) remote, mobile, or drone sensing sensors for field level monitoring of environmental variables for use in farm production or processing management decision making; (K) enhanced precision irrigation automation, remote sensing, and metering, pest and disease detection, nutrient analysis, and crop load assessment equipment and tools; (L) crop monitoring and analytics equipment and tools; (M) potential and predictive near-infrared crop damaged assessments; (N) robotic, semi-autonomous, autonomous, or mechanized systems or other tools; (O) equipment and tools that automate or mechanize seeding, weeding, harvesting, packing (field and in-house), pruning, spraying, transporting, or climate protection (such as shade cloth or light manipulation); and (P) such other automated or mechanized systems or tools that increase efficiency, as determined by the Secretary. (2) Eligible entity The term eligible entity means an individual or entity engaged in the commercial production of specialty crops in the United States. .",
      "versionDate": "2025-09-02",
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
        "updateDate": "2025-09-11T15:38:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-02",
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
          "measure-id": "id119hr5097",
          "measure-number": "5097",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-02",
          "originChamber": "HOUSE",
          "update-date": "2025-09-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5097v00",
            "update-date": "2025-09-11"
          },
          "action-date": "2025-09-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill directs the Agricultural Marketing Service to establish a grant program for commercial specialty crop producers to acquire equipment and provide related training.</p><p>Funds must be used for mechanized or automated systems and tools that increase the efficiency of a task or reduce human labor for a specific activity (e.g., low-dust harvesting tools and equipment, sorting machines, and crop monitoring and analytics equipment and tools).</p><p>The bill includes a minimum 50% cost-sharing requirement.</p>"
        },
        "title": "To amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5097.xml",
    "summary": {
      "actionDate": "2025-09-02",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the Agricultural Marketing Service to establish a grant program for commercial specialty crop producers to acquire equipment and provide related training.</p><p>Funds must be used for mechanized or automated systems and tools that increase the efficiency of a task or reduce human labor for a specific activity (e.g., low-dust harvesting tools and equipment, sorting machines, and crop monitoring and analytics equipment and tools).</p><p>The bill includes a minimum 50% cost-sharing requirement.</p>",
      "updateDate": "2025-09-11",
      "versionCode": "id119hr5097"
    },
    "title": "To amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment."
  },
  "summaries": [
    {
      "actionDate": "2025-09-02",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill directs the Agricultural Marketing Service to establish a grant program for commercial specialty crop producers to acquire equipment and provide related training.</p><p>Funds must be used for mechanized or automated systems and tools that increase the efficiency of a task or reduce human labor for a specific activity (e.g., low-dust harvesting tools and equipment, sorting machines, and crop monitoring and analytics equipment and tools).</p><p>The bill includes a minimum 50% cost-sharing requirement.</p>",
      "updateDate": "2025-09-11",
      "versionCode": "id119hr5097"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5097ih.xml"
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
      "title": "To amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:28Z"
    },
    {
      "title": "To amend the Agricultural Marketing Act of 1946 to direct the Secretary of Agriculture to establish a program under which the Secretary will award grants to specialty crop producers to acquire certain equipment and provide training with respect to the use of such equipment.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T08:05:37Z"
    }
  ]
}
```
