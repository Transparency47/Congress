# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/544?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/544
- Title: Mining Regulatory Clarity Act
- Congress: 119
- Bill type: S
- Bill number: 544
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-03-12 - Committee: Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.
- 2025-04-09 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-105.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-105.
- 2026-02-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 334.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-03-12 - Committee: Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.
- 2025-04-09 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-105.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-105.
- 2026-02-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 334.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/544",
    "number": "544",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Mining Regulatory Clarity Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 334.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-105.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-105.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Hearings held. Hearings printed: S.Hrg. 119-46.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-12",
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
            "date": "2026-02-11T19:37:21Z",
            "name": "Reported By"
          },
          {
            "date": "2025-04-09T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-12T15:58:39Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-12T15:58:39Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-12T19:16:07Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s544is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 544\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Ms. Cortez Masto (for herself, Mr. Risch , Ms. Rosen , Mr. Crapo , and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide for the location of multiple hardrock mining mill sites, to establish the Abandoned Hardrock Mine Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mining Regulatory Clarity Act .\n#### 2. Hardrock mining mill sites\n##### (a) Multiple mill sites\nSection 2337 of the Revised Statutes ( 30 U.S.C. 42 ) is amended by adding at the end the following:\n(c) Additional mill sites (1) Definitions In this subsection: (A) Mill site The term mill site means a location of public land that is reasonably necessary for waste rock or tailings disposal or other operations reasonably incident to mineral development on, or production from land included in a plan of operations. (B) Operations; Operator The terms operations and operator have the meanings given those terms in section 3809.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this subsection). (C) Plan of operations The term plan of operations means a plan of operations that an operator must submit and the Secretary of the Interior or the Secretary of Agriculture, as applicable, must approve before an operator may begin operations, in accordance with, as applicable\u2014 (i) subpart 3809 of title 43, Code of Federal Regulations (or successor regulations establishing application and approval requirements); and (ii) part 228 of title 36, Code of Federal Regulations (or successor regulations establishing application and approval requirements). (D) Public land The term public land means land owned by the United States that is open to location under sections 2319 through 2344 of the Revised Statutes ( 30 U.S.C. 22 et seq. ), including\u2014 (i) land that is mineral-in-character (as defined in section 3830.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this subsection)); (ii) nonmineral land (as defined in section 3830.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this subsection)); and (iii) land where the mineral character has not been determined. (2) In general Notwithstanding subsections (a) and (b), where public land is needed by the proprietor of a lode or placer claim for operations in connection with any lode or placer claim within the proposed plan of operations, the proprietor may\u2014 (A) locate and include within the plan of operations as many mill site claims under this subsection as are reasonably necessary for its operations; and (B) use or occupy public land in accordance with an approved plan of operations. (3) Mill sites convey no mineral rights A mill site under this subsection does not convey mineral rights to the locator. (4) Size of mill sites A location of a single mill site under this subsection shall not exceed 5 acres. (5) Mill site and lode or placer claims on same tracts of public land A mill site may be located under this subsection on a tract of public land on which the claimant or operator maintains a previously located lode or placer claim. (6) Effect on mining claims The location of a mill site under this subsection shall not affect the validity of any lode or placer claim, or any rights associated with such a claim. (7) Patenting A mill site under this section shall not be eligible for patenting. (8) Savings provisions Nothing in this subsection\u2014 (A) diminishes any right (including a right of entry, use, or occupancy) of a claimant; (B) creates or increases any right (including a right of exploration, entry, use, or occupancy) of a claimant on land that is not open to location under the general mining laws; (C) modifies any provision of law or any prior administrative action withdrawing land from location or entry; (D) limits the right of the Federal Government to regulate mining and mining-related activities (including requiring claim validity examinations to establish the discovery of a valuable mineral deposit) in areas withdrawn from mining, including under\u2014 (i) the general mining laws; (ii) the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); (iii) the Wilderness Act ( 16 U.S.C. 1131 et seq. ); (iv) sections 100731 through 100737 of title 54, United States Code; (v) the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); (vi) division A of subtitle III of title 54, United States Code (commonly referred to as the \u2018National Historic Preservation Act\u2019); or (vii) section 4 of the Act of July 23, 1955 (commonly known as the Surface Resources Act of 1955 ) (69 Stat. 368, chapter 375; 30 U.S.C. 612 ); (E) restores any right (including a right of entry, use, or occupancy, or right to conduct operations) of a claimant that\u2014 (i) existed prior to the date on which the land was closed to, or withdrawn from, location under the general mining laws; and (ii) that has been extinguished by such closure or withdrawal; or (F) modifies section 404 of division E of the Consolidated Appropriations Act, 2024 ( Public Law 118\u201342 ). .\n##### (b) Abandoned hardrock mine fund\n**(1) Establishment**\nThere is established in the Treasury of the United States a separate account, to be known as the Abandoned Hardrock Mine Fund (referred to in this subsection as the Fund ).\n**(2) Source of deposits**\nAny amounts collected by the Secretary of the Interior pursuant to the claim maintenance fee under section 10101(a)(1) of the Omnibus Budget Reconciliation Act of 1993 ( 30 U.S.C. 28f(a)(1) ) on mill sites located under subsection (c) of section 2337 of the Revised Statutes ( 30 U.S.C. 42 ) shall be deposited into the Fund.\n**(3) Use**\nThe Secretary of the Interior may make expenditures from amounts available in the Fund, without further appropriations, only to carry out section 40704 of the Infrastructure Investment and Jobs Act ( 30 U.S.C. 1245 ).\n**(4) Allocation of funds**\nAmounts made available under paragraph (3)\u2014\n**(A)**\nshall be allocated in accordance with section 40704(e)(1) of the Infrastructure Investment and Jobs Act ( 30 U.S.C. 1245(e)(1) ); and\n**(B)**\nmay be transferred in accordance with section 40704(e)(2) of that Act ( 30 U.S.C. 1245(e)(2) ).\n##### (c) Clerical amendments\nSection 10101 of the Omnibus Budget Reconciliation Act of 1993 ( 30 U.S.C. 28f ) is amended\u2014\n**(1)**\nby striking the Mining Law of 1872 ( 30 U.S.C. 28\u201328e ) each place it appears and inserting sections 2319 through 2344 of the Revised Statutes ( 30 U.S.C. 22 et seq. ) ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the second sentence, by striking Such claim maintenance fee and inserting the following:\n(B) Fee The claim maintenance fee under subparagraph (A) ; and\n**(ii)**\nin the first sentence, by striking The holder of and inserting the following:\n(A) In general The holder of ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the second sentence, by striking Such claim maintenance fee and inserting the following:\n(B) Fee The claim maintenance fee under subparagraph (A) ; and\n**(ii)**\nin the first sentence, by striking The holder of and inserting the following:\n(A) In general The holder of ; and\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the second sentence, by striking The location fee and inserting the following:\n(2) Fee The location fee ; and\n**(B)**\nin the first sentence, by striking The claim main tenance fee and inserting the following:\n(1) In general The claim maintenance fee .",
      "versionDate": "2025-02-12",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s544rs.xml",
      "text": "II\nCalendar No. 334\n119th CONGRESS\n2d Session\nS. 544\n[Report No. 119\u2013105]\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Ms. Cortez Masto (for herself, Mr. Risch , Ms. Rosen , Mr. Crapo , and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nFebruary 11, 2026 Reported by Mr. Lee , without amendment\nA BILL\nTo provide for the location of multiple hardrock mining mill sites, to establish the Abandoned Hardrock Mine Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mining Regulatory Clarity Act .\n#### 2. Hardrock mining mill sites\n##### (a) Multiple mill sites\nSection 2337 of the Revised Statutes ( 30 U.S.C. 42 ) is amended by adding at the end the following:\n(c) Additional mill sites (1) Definitions In this subsection: (A) Mill site The term mill site means a location of public land that is reasonably necessary for waste rock or tailings disposal or other operations reasonably incident to mineral development on, or production from land included in a plan of operations. (B) Operations; Operator The terms operations and operator have the meanings given those terms in section 3809.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this subsection). (C) Plan of operations The term plan of operations means a plan of operations that an operator must submit and the Secretary of the Interior or the Secretary of Agriculture, as applicable, must approve before an operator may begin operations, in accordance with, as applicable\u2014 (i) subpart 3809 of title 43, Code of Federal Regulations (or successor regulations establishing application and approval requirements); and (ii) part 228 of title 36, Code of Federal Regulations (or successor regulations establishing application and approval requirements). (D) Public land The term public land means land owned by the United States that is open to location under sections 2319 through 2344 of the Revised Statutes ( 30 U.S.C. 22 et seq. ), including\u2014 (i) land that is mineral-in-character (as defined in section 3830.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this subsection)); (ii) nonmineral land (as defined in section 3830.5 of title 43, Code of Federal Regulations (as in effect on the date of enactment of this subsection)); and (iii) land where the mineral character has not been determined. (2) In general Notwithstanding subsections (a) and (b), where public land is needed by the proprietor of a lode or placer claim for operations in connection with any lode or placer claim within the proposed plan of operations, the proprietor may\u2014 (A) locate and include within the plan of operations as many mill site claims under this subsection as are reasonably necessary for its operations; and (B) use or occupy public land in accordance with an approved plan of operations. (3) Mill sites convey no mineral rights A mill site under this subsection does not convey mineral rights to the locator. (4) Size of mill sites A location of a single mill site under this subsection shall not exceed 5 acres. (5) Mill site and lode or placer claims on same tracts of public land A mill site may be located under this subsection on a tract of public land on which the claimant or operator maintains a previously located lode or placer claim. (6) Effect on mining claims The location of a mill site under this subsection shall not affect the validity of any lode or placer claim, or any rights associated with such a claim. (7) Patenting A mill site under this section shall not be eligible for patenting. (8) Savings provisions Nothing in this subsection\u2014 (A) diminishes any right (including a right of entry, use, or occupancy) of a claimant; (B) creates or increases any right (including a right of exploration, entry, use, or occupancy) of a claimant on land that is not open to location under the general mining laws; (C) modifies any provision of law or any prior administrative action withdrawing land from location or entry; (D) limits the right of the Federal Government to regulate mining and mining-related activities (including requiring claim validity examinations to establish the discovery of a valuable mineral deposit) in areas withdrawn from mining, including under\u2014 (i) the general mining laws; (ii) the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1701 et seq. ); (iii) the Wilderness Act ( 16 U.S.C. 1131 et seq. ); (iv) sections 100731 through 100737 of title 54, United States Code; (v) the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ); (vi) division A of subtitle III of title 54, United States Code (commonly referred to as the \u2018National Historic Preservation Act\u2019); or (vii) section 4 of the Act of July 23, 1955 (commonly known as the Surface Resources Act of 1955 ) (69 Stat. 368, chapter 375; 30 U.S.C. 612 ); (E) restores any right (including a right of entry, use, or occupancy, or right to conduct operations) of a claimant that\u2014 (i) existed prior to the date on which the land was closed to, or withdrawn from, location under the general mining laws; and (ii) that has been extinguished by such closure or withdrawal; or (F) modifies section 404 of division E of the Consolidated Appropriations Act, 2024 ( Public Law 118\u201342 ). .\n##### (b) Abandoned hardrock mine fund\n**(1) Establishment**\nThere is established in the Treasury of the United States a separate account, to be known as the Abandoned Hardrock Mine Fund (referred to in this subsection as the Fund ).\n**(2) Source of deposits**\nAny amounts collected by the Secretary of the Interior pursuant to the claim maintenance fee under section 10101(a)(1) of the Omnibus Budget Reconciliation Act of 1993 ( 30 U.S.C. 28f(a)(1) ) on mill sites located under subsection (c) of section 2337 of the Revised Statutes ( 30 U.S.C. 42 ) shall be deposited into the Fund.\n**(3) Use**\nThe Secretary of the Interior may make expenditures from amounts available in the Fund, without further appropriations, only to carry out section 40704 of the Infrastructure Investment and Jobs Act ( 30 U.S.C. 1245 ).\n**(4) Allocation of funds**\nAmounts made available under paragraph (3)\u2014\n**(A)**\nshall be allocated in accordance with section 40704(e)(1) of the Infrastructure Investment and Jobs Act ( 30 U.S.C. 1245(e)(1) ); and\n**(B)**\nmay be transferred in accordance with section 40704(e)(2) of that Act ( 30 U.S.C. 1245(e)(2) ).\n##### (c) Clerical amendments\nSection 10101 of the Omnibus Budget Reconciliation Act of 1993 ( 30 U.S.C. 28f ) is amended\u2014\n**(1)**\nby striking the Mining Law of 1872 ( 30 U.S.C. 28\u201328e ) each place it appears and inserting sections 2319 through 2344 of the Revised Statutes ( 30 U.S.C. 22 et seq. ) ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the second sentence, by striking Such claim maintenance fee and inserting the following:\n(B) Fee The claim maintenance fee under subparagraph (A) ; and\n**(ii)**\nin the first sentence, by striking The holder of and inserting the following:\n(A) In general The holder of ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin the second sentence, by striking Such claim maintenance fee and inserting the following:\n(B) Fee The claim maintenance fee under subparagraph (A) ; and\n**(ii)**\nin the first sentence, by striking The holder of and inserting the following:\n(A) In general The holder of ; and\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the second sentence, by striking The location fee and inserting the following:\n(2) Fee The location fee ; and\n**(B)**\nin the first sentence, by striking The claim main tenance fee and inserting the following:\n(1) In general The claim maintenance fee .",
      "versionDate": "2026-02-11",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-03-17",
        "text": "Read twice. Placed on Senate Legislative Calendar under General Orders. Calendar No. 357."
      },
      "number": "1366",
      "relationshipDetails": {
        "item": [
          {
            "identifiedBy": "House",
            "type": "Related bill"
          },
          {
            "identifiedBy": "CRS",
            "type": "Related bill"
          }
        ]
      },
      "title": "Mining Regulatory Clarity Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-24",
        "text": "Placed on the Union Calendar, Calendar No. 175."
      },
      "number": "4754",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Department of the Interior, Environment, and Related Agencies Appropriations Act, 2026",
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
            "name": "Government trust funds",
            "updateDate": "2025-05-12T19:16:24Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-05-12T19:16:19Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-05-12T19:16:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-05-27T16:26:24Z"
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
          "measure-id": "id119s544",
          "measure-number": "544",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s544v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Mining Regulatory Clarity Act</strong></p><p>This bill\u00a0allows mining operators to use federal lands for activities ancillary to mining, such as waste disposal, regardless of whether those lands contain mineral deposits valuable enough to be mined (mineral validity). It also establishes the Abandoned\u00a0Hardrock Mine Fund.</p><p>The bill addresses a 2022 decision in the U.S. Court of Appeals for the Ninth Circuit\u00a0related to the Rosemont Copper Mine in Arizona (commonly known as <a href=\"https://cdn.ca9.uscourts.gov/datastore/opinions/2022/05/12/19-17585.pdf\">the Rosemont decision</a>, described further in <a href=\"https://crs.gov/Reports/R48166\">CRS Report R48166</a>). The court held that mining claims are only allowed where mineral validity has been established and that mill site claims are more appropriate means for establishing a mining waste disposal site under the Mining Act.</p><p>The bill allows a mining operator to (1) locate and include within its plan of operations as many mill site claims (e.g., areas for waste rock disposal)\u00a0as are reasonably necessary for its operations, and (2) use or occupy public land in accordance with an approved plan of operations.</p><p>Additionally, the bill requires any revenue generated from fees for such mill site claims to be deposited into the Abandoned Hardrock Mine Fund. The Department of the Interior must use the fund for certain abandoned hardrock mine reclamation activities.</p>"
        },
        "title": "Mining Regulatory Clarity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s544.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mining Regulatory Clarity Act</strong></p><p>This bill\u00a0allows mining operators to use federal lands for activities ancillary to mining, such as waste disposal, regardless of whether those lands contain mineral deposits valuable enough to be mined (mineral validity). It also establishes the Abandoned\u00a0Hardrock Mine Fund.</p><p>The bill addresses a 2022 decision in the U.S. Court of Appeals for the Ninth Circuit\u00a0related to the Rosemont Copper Mine in Arizona (commonly known as <a href=\"https://cdn.ca9.uscourts.gov/datastore/opinions/2022/05/12/19-17585.pdf\">the Rosemont decision</a>, described further in <a href=\"https://crs.gov/Reports/R48166\">CRS Report R48166</a>). The court held that mining claims are only allowed where mineral validity has been established and that mill site claims are more appropriate means for establishing a mining waste disposal site under the Mining Act.</p><p>The bill allows a mining operator to (1) locate and include within its plan of operations as many mill site claims (e.g., areas for waste rock disposal)\u00a0as are reasonably necessary for its operations, and (2) use or occupy public land in accordance with an approved plan of operations.</p><p>Additionally, the bill requires any revenue generated from fees for such mill site claims to be deposited into the Abandoned Hardrock Mine Fund. The Department of the Interior must use the fund for certain abandoned hardrock mine reclamation activities.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s544"
    },
    "title": "Mining Regulatory Clarity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mining Regulatory Clarity Act</strong></p><p>This bill\u00a0allows mining operators to use federal lands for activities ancillary to mining, such as waste disposal, regardless of whether those lands contain mineral deposits valuable enough to be mined (mineral validity). It also establishes the Abandoned\u00a0Hardrock Mine Fund.</p><p>The bill addresses a 2022 decision in the U.S. Court of Appeals for the Ninth Circuit\u00a0related to the Rosemont Copper Mine in Arizona (commonly known as <a href=\"https://cdn.ca9.uscourts.gov/datastore/opinions/2022/05/12/19-17585.pdf\">the Rosemont decision</a>, described further in <a href=\"https://crs.gov/Reports/R48166\">CRS Report R48166</a>). The court held that mining claims are only allowed where mineral validity has been established and that mill site claims are more appropriate means for establishing a mining waste disposal site under the Mining Act.</p><p>The bill allows a mining operator to (1) locate and include within its plan of operations as many mill site claims (e.g., areas for waste rock disposal)\u00a0as are reasonably necessary for its operations, and (2) use or occupy public land in accordance with an approved plan of operations.</p><p>Additionally, the bill requires any revenue generated from fees for such mill site claims to be deposited into the Abandoned Hardrock Mine Fund. The Department of the Interior must use the fund for certain abandoned hardrock mine reclamation activities.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s544"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s544is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s544rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Mining Regulatory Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:22Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Mining Regulatory Clarity Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-13T04:43:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mining Regulatory Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-10T15:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the location of multiple hardrock mining mill sites, to establish the Abandoned Hardrock Mine Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T15:48:31Z"
    }
  ]
}
```
