# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1321?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1321
- Title: Moab UMTRA Project Transition Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1321
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1321",
    "number": "1321",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Moab UMTRA Project Transition Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
            "date": "2026-02-04T22:05:37Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-08T14:53:07Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:28Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1321is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1321\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Curtis (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 to provide for the transfer of the Moab site to Grand County, Utah, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Moab UMTRA Project Transition Act of 2025 .\n#### 2. Moab UMTRA project\nSection 3405(i) of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 ( 10 U.S.C. 8720 note; Public Law 105\u2013261 ) is amended\u2014\n**(1)**\nby striking paragraph (5);\n**(2)**\nby redesignating paragraph (6) as paragraph (5); and\n**(3)**\nby adding at the end the following:\n(6) Transfer of Moab site to Grand County (A) In general Subject to subparagraphs (B), (C), and (D), on achieving a remedial action completion status sufficient for land conveyance, as determined by the Secretary of Energy in consultation with relevant regulatory authorities, and subject to any regulatory or use restrictions, if determined necessary to protect human health and safety by the Secretary of Energy or the Nuclear Regulatory Commission (including restrictions pursuant to the Uranium Mill Tailings Radiation Control Act of 1978 ( 42 U.S.C. 7901 et seq. ) and part 192 of title 40, Code of Federal Regulations (or successor regulations)), the Secretary of Energy shall convey, at no cost, all available right, title, and interest of the United States in and to the Moab site to Grand County, Utah. (B) Retention of certain water rights In carrying out the conveyance under subparagraph (A), in accordance with applicable law, the Secretary of Energy shall ensure that the United States retains such water rights as the Secretary of Energy determines necessary to carry out the responsibilities of the Secretary of Energy under the Uranium Mill Tailings Radiation Control Act of 1978 ( 42 U.S.C. 7901 et seq. ), part 192 of title 40, Code of Federal Regulations (or successor regulations), and other applicable requirements, including, if the remediation of groundwater is ongoing at the time of the conveyance, such rights as are necessary to maintain access to wells and the associated surface footprint of those wells. (C) Prohibition The conveyance under subparagraph (A) shall include a provision that prohibits Grand County, Utah, from reconveying to a private entity or nonprofit organization any portion of the land conveyed to Grand County, Utah, under that subparagraph. (D) Additional terms and conditions The Secretary of Energy may require such additional terms and conditions in connection with the conveyance under subparagraph (A) as the Secretary determines necessary to protect the interests of the United States. .",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2681",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Moab UMTRA Project Transition Act of 2025",
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
            "name": "Land transfers",
            "updateDate": "2025-12-11T19:32:41Z"
          },
          {
            "name": "Nuclear Regulatory Commission (NRC)",
            "updateDate": "2025-12-11T19:25:19Z"
          },
          {
            "name": "Nuclear power",
            "updateDate": "2025-12-11T19:30:08Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-12-11T19:31:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-05T13:45:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-08",
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
          "measure-id": "id119s1321",
          "measure-number": "1321",
          "measure-type": "s",
          "orig-publish-date": "2025-04-08",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1321v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-04-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Moab UMTRA Project Transition Act of 2025</strong></p><p>This bill allows the Department of Energy (DOE) to convey the\u00a0Moab site to Grand County, Utah, at no cost\u00a0when it finishes cleaning up uranium mill tailings (i.e., radioactive waste) at the site. (The Moab\u00a0site is a uranium milling site located approximately three miles northwest of Moab, Utah.)</p><p>DOE must\u00a0retain certain water rights that are necessary to carry out its responsibilities, such as maintaining access to wells and the associated surface footprint of the wells if the remediation of groundwater is ongoing at the time of the conveyance.</p><p>The conveyance of the site must include a provision that prohibits Grand County from\u00a0reconveying to a private entity or nonprofit organization any portion of the land conveyed to the county.</p>"
        },
        "title": "Moab UMTRA Project Transition Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1321.xml",
    "summary": {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Moab UMTRA Project Transition Act of 2025</strong></p><p>This bill allows the Department of Energy (DOE) to convey the\u00a0Moab site to Grand County, Utah, at no cost\u00a0when it finishes cleaning up uranium mill tailings (i.e., radioactive waste) at the site. (The Moab\u00a0site is a uranium milling site located approximately three miles northwest of Moab, Utah.)</p><p>DOE must\u00a0retain certain water rights that are necessary to carry out its responsibilities, such as maintaining access to wells and the associated surface footprint of the wells if the remediation of groundwater is ongoing at the time of the conveyance.</p><p>The conveyance of the site must include a provision that prohibits Grand County from\u00a0reconveying to a private entity or nonprofit organization any portion of the land conveyed to the county.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s1321"
    },
    "title": "Moab UMTRA Project Transition Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Moab UMTRA Project Transition Act of 2025</strong></p><p>This bill allows the Department of Energy (DOE) to convey the\u00a0Moab site to Grand County, Utah, at no cost\u00a0when it finishes cleaning up uranium mill tailings (i.e., radioactive waste) at the site. (The Moab\u00a0site is a uranium milling site located approximately three miles northwest of Moab, Utah.)</p><p>DOE must\u00a0retain certain water rights that are necessary to carry out its responsibilities, such as maintaining access to wells and the associated surface footprint of the wells if the remediation of groundwater is ongoing at the time of the conveyance.</p><p>The conveyance of the site must include a provision that prohibits Grand County from\u00a0reconveying to a private entity or nonprofit organization any portion of the land conveyed to the county.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s1321"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1321is.xml"
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
      "title": "Moab UMTRA Project Transition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Moab UMTRA Project Transition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 to provide for the transfer of the Moab site to Grand County, Utah, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:27Z"
    }
  ]
}
```
