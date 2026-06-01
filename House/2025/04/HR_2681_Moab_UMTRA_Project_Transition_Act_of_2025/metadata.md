# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2681?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2681
- Title: Moab UMTRA Project Transition Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2681
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-02-25T13:43:54Z
- Update date including text: 2026-02-25T13:43:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2681",
    "number": "2681",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Moab UMTRA Project Transition Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-25T13:43:54Z",
    "updateDateIncludingText": "2026-02-25T13:43:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "UT"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "UT"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2681ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2681\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Kennedy of Utah (for himself, Mr. Owens , Ms. Maloy , and Mr. Moore of Utah ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 to provide for the transfer of the Moab site to Grand County, Utah, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Moab UMTRA Project Transition Act of 2025 .\n#### 2. Moab UMTRA project\nSection 3405(i) of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 ( 10 U.S.C. 8720 note; Public Law 105\u2013261 ) is amended\u2014\n**(1)**\nby striking paragraph (5);\n**(2)**\nby redesignating paragraph (6) as paragraph (5); and\n**(3)**\nby adding at the end the following:\n(6) Transfer of Moab site to Grand County (A) In general Subject to subparagraphs (B), (C), and (D), on achieving a remedial action completion status sufficient for land conveyance, as determined by the Secretary of Energy in consultation with relevant regulatory authorities, and subject to any regulatory or use restrictions, if determined necessary to protect human health and safety by the Secretary of Energy or the Nuclear Regulatory Commission (including restrictions pursuant to the Uranium Mill Tailings Radiation Control Act of 1978 ( 42 U.S.C. 7901 et seq. ) and part 192 of title 40, Code of Federal Regulations (or successor regulations)), the Secretary of Energy shall convey, at no cost, all available right, title, and interest of the United States in and to the Moab site to Grand County, Utah. (B) Retention of certain water rights In carrying out the conveyance under subparagraph (A), in accordance with applicable law, the Secretary of Energy shall ensure that the United States retains such water rights as the Secretary of Energy determines necessary to carry out the responsibilities of the Secretary of Energy under the Uranium Mill Tailings Radiation Control Act of 1978 ( 42 U.S.C. 7901 et seq. ), part 192 of title 40, Code of Federal Regulations (or successor regulations), and other applicable requirements, including, if the remediation of groundwater is ongoing at the time of the conveyance, such rights as are necessary to maintain access to wells and the associated surface footprint of those wells. (C) Prohibition The conveyance under subparagraph (A) shall include a provision that prohibits Grand County, Utah, from reconveying to a private entity or nonprofit organization any portion of the land conveyed to Grand County, Utah, under that subparagraph. (D) Additional terms and conditions The Secretary of Energy may require such additional terms and conditions in connection with the conveyance under subparagraph (A) as the Secretary determines necessary to protect the interests of the United States. .",
      "versionDate": "2025-04-07",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-02-04",
        "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably."
      },
      "number": "1321",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Moab UMTRA Project Transition Act of 2025",
      "type": "S"
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
        "name": "Energy",
        "updateDate": "2025-05-05T13:45:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2681",
          "measure-number": "2681",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2681v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Moab UMTRA Project Transition Act of 2025</strong></p><p>This bill allows the Department of Energy (DOE) to convey the\u00a0Moab site to Grand County, Utah, at no cost\u00a0when it finishes cleaning up uranium mill tailings (i.e., radioactive waste) at the site. (The Moab\u00a0site is a uranium milling site located approximately three miles northwest of Moab, Utah.)</p><p>DOE must\u00a0retain certain water rights that are necessary to carry out its responsibilities, such as maintaining access to wells and the associated surface footprint of the wells if the remediation of groundwater is ongoing at the time of the conveyance.</p><p>The conveyance of the site must include a provision that prohibits Grand County from\u00a0reconveying to a private entity or nonprofit organization any portion of the land conveyed to the county.</p>"
        },
        "title": "Moab UMTRA Project Transition Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2681.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Moab UMTRA Project Transition Act of 2025</strong></p><p>This bill allows the Department of Energy (DOE) to convey the\u00a0Moab site to Grand County, Utah, at no cost\u00a0when it finishes cleaning up uranium mill tailings (i.e., radioactive waste) at the site. (The Moab\u00a0site is a uranium milling site located approximately three miles northwest of Moab, Utah.)</p><p>DOE must\u00a0retain certain water rights that are necessary to carry out its responsibilities, such as maintaining access to wells and the associated surface footprint of the wells if the remediation of groundwater is ongoing at the time of the conveyance.</p><p>The conveyance of the site must include a provision that prohibits Grand County from\u00a0reconveying to a private entity or nonprofit organization any portion of the land conveyed to the county.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr2681"
    },
    "title": "Moab UMTRA Project Transition Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Moab UMTRA Project Transition Act of 2025</strong></p><p>This bill allows the Department of Energy (DOE) to convey the\u00a0Moab site to Grand County, Utah, at no cost\u00a0when it finishes cleaning up uranium mill tailings (i.e., radioactive waste) at the site. (The Moab\u00a0site is a uranium milling site located approximately three miles northwest of Moab, Utah.)</p><p>DOE must\u00a0retain certain water rights that are necessary to carry out its responsibilities, such as maintaining access to wells and the associated surface footprint of the wells if the remediation of groundwater is ongoing at the time of the conveyance.</p><p>The conveyance of the site must include a provision that prohibits Grand County from\u00a0reconveying to a private entity or nonprofit organization any portion of the land conveyed to the county.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119hr2681"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2681ih.xml"
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
      "title": "Moab UMTRA Project Transition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T03:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Moab UMTRA Project Transition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T03:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 to provide for the transfer of the Moab site to Grand County, Utah, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T03:18:16Z"
    }
  ]
}
```
