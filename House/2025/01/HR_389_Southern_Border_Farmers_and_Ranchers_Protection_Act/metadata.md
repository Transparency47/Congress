# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/389
- Title: Southern Border Farmers and Ranchers Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 389
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-02-04T05:06:19Z
- Update date including text: 2026-02-04T05:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/389",
    "number": "389",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Southern Border Farmers and Ranchers Protection Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:19Z",
    "updateDateIncludingText": "2026-02-04T05:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:04:25Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr389ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 389\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Ms. De La Cruz (for herself and Mr. Tony Gonzales of Texas ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to authorize payments under the environmental quality incentives program to assist producers in implementing certain conservation practices along the southern border of Texas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Southern Border Farmers and Ranchers Protection Act .\n#### 2. Southern Border Initiative\nSection 1240B of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132 ) is amended by adding at the end the following:\n(k) Southern Border Initiative (1) In general The Secretary shall provide payments to producers under the program to implement conservation practices to address and repair damage, to agricultural land and farming infrastructure on covered land of such producers, that contributes to natural resource concerns or problems. (2) Contract term A contract to provide payments under paragraph (1) shall have a term of 1 year. (3) Covered land defined In this subsection, the term covered land means land in a county at or near the southern border of Texas, including the following counties: (A) Brewster. (B) Brooks. (C) Cameron. (D) Crockett. (E) Culberson. (F) Dimmit. (G) Duval. (H) Edwards. (I) El Paso. (J) Frio. (K) Hidalgo. (L) Hudspeth. (M) Jeff Davis. (N) Jim Hogg. (O) Jim Wells. (P) Karnes. (Q) Kenedy. (R) Kinney. (S) Kleberg. (T) La Salle. (U) Live Oak. (V) Maverick. (W) McMullen. (X) Pecos. (Y) Presidio. (Z) Reeves. (AA) Starr. (BB) Sutton. (CC) Terrell. (DD) Uvalde. (EE) Val Verde. (FF) Webb. (GG) Willacy. (HH) Zapata. (II) Zavala. .",
      "versionDate": "2025-01-14",
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
        "updateDate": "2025-02-19T16:47:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr389",
          "measure-number": "389",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr389v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Southern Border Farmers and Ranchers Protection Act</strong></p><p>This bill directs the Environmental Quality Incentives Program (EQIP) to provide payments to agricultural producers to implement certain conservation practices in counties at or near the Texas southern border. In general, this Department of Agriculture program provides technical and financial assistance to agricultural producers and forest landowners to address natural resource concerns.</p><p>Specifically, EQIP must provide payments to agricultural producers to implement conservation practices to address and repair damage to agricultural land and farming infrastructure that is in a county at or near the Texas southern border and\u00a0contributes to natural resource concerns or problems.</p>"
        },
        "title": "Southern Border Farmers and Ranchers Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr389.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Southern Border Farmers and Ranchers Protection Act</strong></p><p>This bill directs the Environmental Quality Incentives Program (EQIP) to provide payments to agricultural producers to implement certain conservation practices in counties at or near the Texas southern border. In general, this Department of Agriculture program provides technical and financial assistance to agricultural producers and forest landowners to address natural resource concerns.</p><p>Specifically, EQIP must provide payments to agricultural producers to implement conservation practices to address and repair damage to agricultural land and farming infrastructure that is in a county at or near the Texas southern border and\u00a0contributes to natural resource concerns or problems.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr389"
    },
    "title": "Southern Border Farmers and Ranchers Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Southern Border Farmers and Ranchers Protection Act</strong></p><p>This bill directs the Environmental Quality Incentives Program (EQIP) to provide payments to agricultural producers to implement certain conservation practices in counties at or near the Texas southern border. In general, this Department of Agriculture program provides technical and financial assistance to agricultural producers and forest landowners to address natural resource concerns.</p><p>Specifically, EQIP must provide payments to agricultural producers to implement conservation practices to address and repair damage to agricultural land and farming infrastructure that is in a county at or near the Texas southern border and\u00a0contributes to natural resource concerns or problems.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr389"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr389ih.xml"
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
      "title": "Southern Border Farmers and Ranchers Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Southern Border Farmers and Ranchers Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to authorize payments under the environmental quality incentives program to assist producers in implementing certain conservation practices along the southern border of Texas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:34Z"
    }
  ]
}
```
