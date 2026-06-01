# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/472?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/472
- Title: Ski Hill Resources for Economic Development Act
- Congress: 119
- Bill type: S
- Bill number: 472
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S795-796)
- 2025-09-11 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-104.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-104.
- 2026-02-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 333.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S795-796)
- 2025-09-11 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-104.
- 2026-02-11 - Committee: Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-104.
- 2026-02-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 333.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/472",
    "number": "472",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Ski Hill Resources for Economic Development Act",
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 333.",
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
      "text": "Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-104.",
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
      "text": "Committee on Energy and Natural Resources. Reported by Senator Lee without amendment. With written report No. 119-104.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S795-796)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
            "date": "2026-02-11T19:34:50Z",
            "name": "Reported By"
          },
          {
            "date": "2025-09-11T13:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-06T22:03:33Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WY"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "OR"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NM"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s472is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 472\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Barrasso (for himself, Mr. Bennet , Mr. Hickenlooper , Mrs. Shaheen , Ms. Hassan , Ms. Lummis , Ms. Cortez Masto , Mr. Wyden , Mr. Risch , Mr. Crapo , Mr. Daines , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Omnibus Parks and Public Lands Management Act of 1996 to provide for the establishment of a Ski Area Fee Retention Account, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ski Hill Resources for Economic Development Act .\n#### 2. Establishment of ski area fee retention account\n##### (a) In general\nSection 701 of division I of the Omnibus Parks and Public Lands Management Act of 1996 ( 16 U.S.C. 497c ) is amended by adding at the end the following:\n(k) Ski area fee retention account (1) Definitions In this subsection: (A) Account The term Account means the Ski Area Fee Retention Account established under paragraph (2). (B) Covered unit The term covered unit means the unit of the National Forest System that collects the ski area permit rental charge under this section. (C) Secretary The term Secretary means the Secretary of Agriculture. (2) Establishment The Secretary of the Treasury shall establish a special account in the Treasury, to be known as the Ski Area Fee Retention Account . (3) Deposits Subject to paragraphs (4) and (5), a ski area permit rental charge collected by the Secretary under this section shall\u2014 (A) be deposited in the Account; (B) be available to the Secretary for use, without further appropriation; and (C) remain available for the period of 4 fiscal years beginning with the first fiscal year after the fiscal year in which the ski area permit rental charge is deposited in the Account under subparagraph (A). (4) Distribution of amounts in the account (A) Local distribution of funds (i) In general Except as provided in subparagraph (C), the Secretary shall expend 80 percent of the ski area permit rental charges deposited in the Account from a covered unit at the covered unit in accordance with clause (ii). (ii) Distribution Of the amounts made available for expenditure under clause (i)\u2014 (I) 75 percent shall be used at the covered unit for activities described in paragraph (5)(A); and (II) 25 percent shall be used for activities at the covered unit described in paragraph (5)(B). (B) Agency-wide distribution of funds The Secretary shall expend 20 percent of the ski area permit rental charges deposited in the Account from a covered unit at any unit of the National Forest System for an activity described in subparagraph (A) or (B) of paragraph (5). (C) Reduction of percentage (i) Reduction The Secretary shall reduce the percentage otherwise applicable under subparagraph (A)(i) to not less than 60 percent if the Secretary determines that the amount otherwise made available under that subparagraph exceeds the reasonable needs of the covered unit for which expenditures may be made in the applicable fiscal year. (ii) Distribution of funds The balance of the ski area permit rental charges that are collected at a covered unit, deposited into the Account, and not distributed in accordance with subparagraph (A) or (B) shall be available to the Secretary for expenditure at any other unit of the National Forest System in accordance with the following: (I) 75 percent shall be used for activities described in paragraph (5)(A). (II) 25 percent shall be used for activities described in paragraph (5)(B). (5) Expenditures Amounts available to the Secretary for expenditure from the Account shall be only used for\u2014 (A) (i) the administration of the Forest Service ski area program, including\u2014 (I) the processing of an application for a new ski area or a ski area improvement project, including staffing and contracting for the processing; and (II) administering a ski area permit described in subsection (a); (ii) staff training for\u2014 (I) the processing of an application for\u2014 (aa) a new ski area; (bb) a ski area improvement project; or (cc) a special use permit; or (II) administering\u2014 (aa) a ski area permit described in subsection (a); or (bb) a special use permit; (iii) an interpretation activity, National Forest System visitor information, a visitor service, or signage; (iv) direct costs associated with collecting a ski area permit rental charge or other fee collected by the Secretary related to recreation; (v) planning for, or coordinating to respond to, a wildfire in or adjacent to a recreation site, particularly a ski area; or (vi) reducing the likelihood of a wildfire starting, or the risks posed by a wildfire, in or adjacent to a recreation site, particularly a ski area, except through hazardous fuels reduction activities; or (B) (i) the repair, maintenance, or enhancement of a Forest Service-owned facility, road, or trail directly related to visitor enjoyment, visitor access, or visitor health or safety; (ii) habitat restoration directly related to recreation; (iii) law enforcement related to public use and recreation; (iv) the construction or expansion of parking areas; (v) the processing or administering of a recreation special use permit; (vi) avalanche information and education activities carried out by the Secretary or nonprofit partners; (vii) search and rescue activities carried out by the Secretary, a local government, or a nonprofit partner; or (viii) the administration of leases under\u2014 (I) the Forest Service Facility Realignment and Enhancement Act of 2005 ( 16 U.S.C. 580d note; Public Law 109\u201354 ); and (II) section 8623 of the Agriculture Improvement Act of 2018 ( 16 U.S.C. 580d note; Public Law 115\u2013334 ). (6) Limitation Amounts in the Account may not be used for\u2014 (A) the conduct of wildfire suppression; or (B) the acquisition of land for inclusion in the National Forest System. (7) Effect (A) In general Nothing in this subsection affects the applicability of section 7 of the Act of April 24, 1950 (commonly known as the Granger-Thye Act ) ( 16 U.S.C. 580d ), to ski areas on National Forest System land. (B) Supplemental funding Rental charges retained and expended under this subsection shall supplement (and not supplant) appropriated funding for the operation and maintenance of each covered unit. (C) Cost recovery Nothing in this subsection affects any cost recovery under any provision of law (including regulations) for processing an application for or monitoring compliance with a ski area permit or other recreation special use permit. .\n##### (b) Effective date\nThis section (including the amendments made by this section) shall take effect on the date that is 60 days after the date of enactment of this Act.",
      "versionDate": "2025-02-06",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s472rs.xml",
      "text": "II\nCalendar No. 333\n119th CONGRESS\n2d Session\nS. 472\n[Report No. 119\u2013104]\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Barrasso (for himself, Mr. Bennet , Mr. Hickenlooper , Mrs. Shaheen , Ms. Hassan , Ms. Lummis , Ms. Cortez Masto , Mr. Wyden , Mr. Risch , Mr. Crapo , Mr. Daines , Mr. Sheehy , Mr. Luj\u00e1n , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nFebruary 11, 2026 Reported by Mr. Lee , without amendment\nA BILL\nTo amend the Omnibus Parks and Public Lands Management Act of 1996 to provide for the establishment of a Ski Area Fee Retention Account, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ski Hill Resources for Economic Development Act .\n#### 2. Establishment of ski area fee retention account\n##### (a) In general\nSection 701 of division I of the Omnibus Parks and Public Lands Management Act of 1996 ( 16 U.S.C. 497c ) is amended by adding at the end the following:\n(k) Ski area fee retention account (1) Definitions In this subsection: (A) Account The term Account means the Ski Area Fee Retention Account established under paragraph (2). (B) Covered unit The term covered unit means the unit of the National Forest System that collects the ski area permit rental charge under this section. (C) Secretary The term Secretary means the Secretary of Agriculture. (2) Establishment The Secretary of the Treasury shall establish a special account in the Treasury, to be known as the Ski Area Fee Retention Account . (3) Deposits Subject to paragraphs (4) and (5), a ski area permit rental charge collected by the Secretary under this section shall\u2014 (A) be deposited in the Account; (B) be available to the Secretary for use, without further appropriation; and (C) remain available for the period of 4 fiscal years beginning with the first fiscal year after the fiscal year in which the ski area permit rental charge is deposited in the Account under subparagraph (A). (4) Distribution of amounts in the account (A) Local distribution of funds (i) In general Except as provided in subparagraph (C), the Secretary shall expend 80 percent of the ski area permit rental charges deposited in the Account from a covered unit at the covered unit in accordance with clause (ii). (ii) Distribution Of the amounts made available for expenditure under clause (i)\u2014 (I) 75 percent shall be used at the covered unit for activities described in paragraph (5)(A); and (II) 25 percent shall be used for activities at the covered unit described in paragraph (5)(B). (B) Agency-wide distribution of funds The Secretary shall expend 20 percent of the ski area permit rental charges deposited in the Account from a covered unit at any unit of the National Forest System for an activity described in subparagraph (A) or (B) of paragraph (5). (C) Reduction of percentage (i) Reduction The Secretary shall reduce the percentage otherwise applicable under subparagraph (A)(i) to not less than 60 percent if the Secretary determines that the amount otherwise made available under that subparagraph exceeds the reasonable needs of the covered unit for which expenditures may be made in the applicable fiscal year. (ii) Distribution of funds The balance of the ski area permit rental charges that are collected at a covered unit, deposited into the Account, and not distributed in accordance with subparagraph (A) or (B) shall be available to the Secretary for expenditure at any other unit of the National Forest System in accordance with the following: (I) 75 percent shall be used for activities described in paragraph (5)(A). (II) 25 percent shall be used for activities described in paragraph (5)(B). (5) Expenditures Amounts available to the Secretary for expenditure from the Account shall be only used for\u2014 (A) (i) the administration of the Forest Service ski area program, including\u2014 (I) the processing of an application for a new ski area or a ski area improvement project, including staffing and contracting for the processing; and (II) administering a ski area permit described in subsection (a); (ii) staff training for\u2014 (I) the processing of an application for\u2014 (aa) a new ski area; (bb) a ski area improvement project; or (cc) a special use permit; or (II) administering\u2014 (aa) a ski area permit described in subsection (a); or (bb) a special use permit; (iii) an interpretation activity, National Forest System visitor information, a visitor service, or signage; (iv) direct costs associated with collecting a ski area permit rental charge or other fee collected by the Secretary related to recreation; (v) planning for, or coordinating to respond to, a wildfire in or adjacent to a recreation site, particularly a ski area; or (vi) reducing the likelihood of a wildfire starting, or the risks posed by a wildfire, in or adjacent to a recreation site, particularly a ski area, except through hazardous fuels reduction activities; or (B) (i) the repair, maintenance, or enhancement of a Forest Service-owned facility, road, or trail directly related to visitor enjoyment, visitor access, or visitor health or safety; (ii) habitat restoration directly related to recreation; (iii) law enforcement related to public use and recreation; (iv) the construction or expansion of parking areas; (v) the processing or administering of a recreation special use permit; (vi) avalanche information and education activities carried out by the Secretary or nonprofit partners; (vii) search and rescue activities carried out by the Secretary, a local government, or a nonprofit partner; or (viii) the administration of leases under\u2014 (I) the Forest Service Facility Realignment and Enhancement Act of 2005 ( 16 U.S.C. 580d note; Public Law 109\u201354 ); and (II) section 8623 of the Agriculture Improvement Act of 2018 ( 16 U.S.C. 580d note; Public Law 115\u2013334 ). (6) Limitation Amounts in the Account may not be used for\u2014 (A) the conduct of wildfire suppression; or (B) the acquisition of land for inclusion in the National Forest System. (7) Effect (A) In general Nothing in this subsection affects the applicability of section 7 of the Act of April 24, 1950 (commonly known as the Granger-Thye Act ) ( 16 U.S.C. 580d ), to ski areas on National Forest System land. (B) Supplemental funding Rental charges retained and expended under this subsection shall supplement (and not supplant) appropriated funding for the operation and maintenance of each covered unit. (C) Cost recovery Nothing in this subsection affects any cost recovery under any provision of law (including regulations) for processing an application for or monitoring compliance with a ski area permit or other recreation special use permit. .\n##### (b) Effective date\nThis section (including the amendments made by this section) shall take effect on the date that is 60 days after the date of enactment of this Act.",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1084",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ski Hill Resources for Economic Development Act",
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
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "Sports and recreation facilities",
            "updateDate": "2025-09-15T14:54:18Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-09-15T14:54:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-06T12:38:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s472",
          "measure-number": "472",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s472v00",
            "update-date": "2026-02-09"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ski Hill Resources for Economic Development Act</strong></p><p>This bill\u00a0allows\u00a0National Forest System (NFS) units\u00a0to keep the majority of ski area permit rental fees that were generated within their boundaries and outlines how revenues from those fees may be used.\u00a0Such fees are collected by the Department of Agriculture (USDA) from ski area operators on NFS land.</p><p>Within the NFS unit where the fees were generated,\u00a0USDA must expend (1) 60%-48% of the collected fees for activities such as administration of the ski area permit program, visitor information, or reducing the likelihood of wildfire in or adjacent to a recreation site; and (2) 20% of the collected fees for activities such as repair of a Forest Service-owned facility, habitat restoration, or search and rescue activities.</p><p>The remainder of the collected fees must be expended by USDA at any NFS unit for any of the activities specified in this bill.</p>"
        },
        "title": "Ski Hill Resources for Economic Development Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s472.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ski Hill Resources for Economic Development Act</strong></p><p>This bill\u00a0allows\u00a0National Forest System (NFS) units\u00a0to keep the majority of ski area permit rental fees that were generated within their boundaries and outlines how revenues from those fees may be used.\u00a0Such fees are collected by the Department of Agriculture (USDA) from ski area operators on NFS land.</p><p>Within the NFS unit where the fees were generated,\u00a0USDA must expend (1) 60%-48% of the collected fees for activities such as administration of the ski area permit program, visitor information, or reducing the likelihood of wildfire in or adjacent to a recreation site; and (2) 20% of the collected fees for activities such as repair of a Forest Service-owned facility, habitat restoration, or search and rescue activities.</p><p>The remainder of the collected fees must be expended by USDA at any NFS unit for any of the activities specified in this bill.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s472"
    },
    "title": "Ski Hill Resources for Economic Development Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ski Hill Resources for Economic Development Act</strong></p><p>This bill\u00a0allows\u00a0National Forest System (NFS) units\u00a0to keep the majority of ski area permit rental fees that were generated within their boundaries and outlines how revenues from those fees may be used.\u00a0Such fees are collected by the Department of Agriculture (USDA) from ski area operators on NFS land.</p><p>Within the NFS unit where the fees were generated,\u00a0USDA must expend (1) 60%-48% of the collected fees for activities such as administration of the ski area permit program, visitor information, or reducing the likelihood of wildfire in or adjacent to a recreation site; and (2) 20% of the collected fees for activities such as repair of a Forest Service-owned facility, habitat restoration, or search and rescue activities.</p><p>The remainder of the collected fees must be expended by USDA at any NFS unit for any of the activities specified in this bill.</p>",
      "updateDate": "2026-02-09",
      "versionCode": "id119s472"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s472is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s472rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Ski Hill Resources for Economic Development Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-13T04:43:24Z"
    },
    {
      "title": "Ski Hill Resources for Economic Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ski Hill Resources for Economic Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Parks and Public Lands Management Act of 1996 to provide for the establishment of a Ski Area Fee Retention Account, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:53Z"
    }
  ]
}
```
