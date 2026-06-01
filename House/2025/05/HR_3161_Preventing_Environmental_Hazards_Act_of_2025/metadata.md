# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3161
- Title: Preventing Environmental Hazards Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3161
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3161",
    "number": "3161",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Preventing Environmental Hazards Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "ME"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NC"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3161ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3161\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Murphy (for himself, Ms. Pingree , Mr. Davis of North Carolina , Mr. Rouzer , and Mr. Wittman ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo make protection against damage and loss resulting from the erosion and undermining of shorelines available under the National Flood Insurance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Environmental Hazards Act of 2025 .\n#### 2. Flood insurance coverage for structures on land subject to imminent collapse or subsidence\n##### (a) In general\nSection 1306 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4013 ) is amended by adding at the end the following new subsection:\n(e) Erosion coverage (1) In general If any structure covered by a contract for flood insurance under this title and located on land that is along the shore of a lake or other body of water is condemned or deemed unsafe for habitation by a State or local authority due to imminent collapse or subsidence as a result of shoreline erosion or determined by a State or local authority to be situated partially or wholly over water, a shoreline bluff, or escarpment, or below Mean Higher High Water on tidal waterbodies (regardless of whether as a result of long-term, chronic erosion or as a result of waves or currents of water exceeding anticipated cyclical levels), the Administrator shall (following final determination by the Administrator that the claim is in compliance with regulations developed pursuant to paragraph (7)(A)) pay amounts under such flood insurance contract for proper demolition or relocation as follows: (A) Demolition For proper demolition\u2014 (i) following final determination by the Administrator, 40 percent of the value of the structure; and (ii) following demolition of the structure (including any septic containment system) within 6 months of payment under clause (i) and prior to collapse, the remaining 60 percent of the value of the structure or the actual cost of demolition, whichever amount is less. (B) Relocation For proper relocation (including removal of any septic containment system) if the owner chooses to relocate the structure, following final determination by the Administrator, prior to collapse, up to 40 percent of the value of the structure; except that the total payment under this subparagraph shall not exceed the actual cost of relocation. (2) Collapse or subsidence If any structure subject to a final determination under paragraph (1) collapses or subsides, or a period of six or more months elapses, before the owner demolishes or relocates the structure and the Administrator determines that the owner has failed to take reasonable and prudent action to demolish or relocate the structure, the Administrator shall not pay more than the amount provided in paragraph (1)(A)(i) with respect to the structure. (3) Value of structure For purposes of paying flood insurance pursuant to this subsection, the value of a structure shall be whichever of the following is lowest: (A) The fair market value of a comparable structure that is not subject to imminent collapse or subsidence. (B) The price paid for the structure and any improvement to the structure, as adjusted for inflation in accordance with an index determined by the Administrator to be appropriate. (C) The value of the structure under the flood insurance contract issued pursuant to this title. (4) Coverage terms (A) Maximum claim Notwithstanding any provision of this subsection, the amount paid under a flood insurance contract in connection with any claim under this subsection may not exceed the lesser of\u2014 (i) the amount of coverage under the flood insurance contract for the structure; or (ii) $250,000. (B) Exclusion of loss of contents Flood insurance coverage under this subsection shall not cover any loss of or damage to any contents of a structure. (5) Applicability (A) In general The provisions of this subsection shall apply to contracts for flood insurance under this title that are in effect on, or entered into after, the date of the enactment of this subsection. (B) Coverage on certification date The provisions of this subsection shall not apply to any structure not subject to a contract for flood insurance under this title on the date of a certification under paragraph (1). (C) Period of coverage The provisions of this subsection shall not apply to any structure unless the structure is covered by a contract for flood insurance under this title\u2014 (i) for a period of 12 months on or before the date of the enactment of this Act; or (ii) for a continuous period of 4 years prior to certification under paragraph (1). (6) Termination of coverage For any structure that is subject to a final determination under paragraph (1), no subsequent flood insurance coverage under this title or assistance under the Disaster Relief Act of 1974 (except emergency assistance essential to save lives and protect property, public health and safety) shall be available for the same structure, or a different structure on any remaining portions of the parcel of land originally afforded assistance under this subsection. (7) Regulations (A) In general The Administrator shall promulgate regulations and guidelines to implement this subsection. (B) Applicability Prior to issuance of regulations regarding the State and local certifications pursuant to paragraph (1), all provisions of this subsection shall apply to any structure that\u2014 (i) otherwise meets the requirements of this subsection; and (ii) is imminently threatened by shoreline erosion, regardless of whether as a result of long-term, chronic erosion or as a result of waves or currents of water exceeding anticipated cyclical levels. .\n##### (b) Effective date\nThe amendment made by this section shall become effective on the date of the enactment of this Act.",
      "versionDate": "2025-05-01",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T12:02:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119hr3161",
          "measure-number": "3161",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2026-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3161v00",
            "update-date": "2026-03-11"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Preventing Environmental Hazards Act of 2025</strong></p><p>This bill expands National Flood Insurance Program (NFIP) coverage to include the demolition or relocation of certain coastal structures that are facing imminent collapse\u00a0or subsidence.</p><p>Specifically, NFIP must pay for demolition or relocation for NFIP-insured structures that are condemned or deemed unsafe by state or local authorities due to the threat of imminent collapse or subsidence from shoreline erosion or that meet other location criteria.</p><p>The bill sets forth provisions for the valuation of the structure, the maximum claim to be paid, and the terms of coverage termination.</p><p>This bill applies to structures covered by NFIP (1) for a period of 12 months on or before the date of the bill\u2019s enactment, or (2) for a continuous period of 4 years prior to certification for coverage established by this bill.</p>"
        },
        "title": "Preventing Environmental Hazards Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3161.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventing Environmental Hazards Act of 2025</strong></p><p>This bill expands National Flood Insurance Program (NFIP) coverage to include the demolition or relocation of certain coastal structures that are facing imminent collapse\u00a0or subsidence.</p><p>Specifically, NFIP must pay for demolition or relocation for NFIP-insured structures that are condemned or deemed unsafe by state or local authorities due to the threat of imminent collapse or subsidence from shoreline erosion or that meet other location criteria.</p><p>The bill sets forth provisions for the valuation of the structure, the maximum claim to be paid, and the terms of coverage termination.</p><p>This bill applies to structures covered by NFIP (1) for a period of 12 months on or before the date of the bill\u2019s enactment, or (2) for a continuous period of 4 years prior to certification for coverage established by this bill.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr3161"
    },
    "title": "Preventing Environmental Hazards Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preventing Environmental Hazards Act of 2025</strong></p><p>This bill expands National Flood Insurance Program (NFIP) coverage to include the demolition or relocation of certain coastal structures that are facing imminent collapse\u00a0or subsidence.</p><p>Specifically, NFIP must pay for demolition or relocation for NFIP-insured structures that are condemned or deemed unsafe by state or local authorities due to the threat of imminent collapse or subsidence from shoreline erosion or that meet other location criteria.</p><p>The bill sets forth provisions for the valuation of the structure, the maximum claim to be paid, and the terms of coverage termination.</p><p>This bill applies to structures covered by NFIP (1) for a period of 12 months on or before the date of the bill\u2019s enactment, or (2) for a continuous period of 4 years prior to certification for coverage established by this bill.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr3161"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3161ih.xml"
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
      "title": "Preventing Environmental Hazards Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Environmental Hazards Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make protection against damage and loss resulting from the erosion and undermining of shorelines available under the National Flood Insurance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:43Z"
    }
  ]
}
```
