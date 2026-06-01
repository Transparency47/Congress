# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5911?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5911
- Title: Crystal Reservoir Conveyance Act
- Congress: 119
- Bill type: HR
- Bill number: 5911
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2026-05-29T15:19:09Z
- Update date including text: 2026-05-29T15:19:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-02-10 - Committee: Subcommittee Hearings Held
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported in the Nature of a Substitute by Unanimous Consent.
- 2026-04-21 - Committee: Subcommittee on Federal Lands Discharged
- 2026-05-20 - Calendars: Placed on the Union Calendar, Calendar No. 576.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-662.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-662.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-02-10 - Committee: Subcommittee Hearings Held
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported in the Nature of a Substitute by Unanimous Consent.
- 2026-04-21 - Committee: Subcommittee on Federal Lands Discharged
- 2026-05-20 - Calendars: Placed on the Union Calendar, Calendar No. 576.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-662.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-662.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5911",
    "number": "5911",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Crystal Reservoir Conveyance Act",
    "type": "HR",
    "updateDate": "2026-05-29T15:19:09Z",
    "updateDateIncludingText": "2026-05-29T15:19:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-05-20",
      "calendarNumber": {
        "calendar": "U00576"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 576.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-05-20",
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
      "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-662.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-662.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Federal Lands Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
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
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
        "item": [
          {
            "date": "2026-05-20T17:53:49Z",
            "name": "Reported By"
          },
          {
            "date": "2026-04-21T17:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-04T19:02:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-21T17:00:00Z",
                "name": "Discharged from"
              },
              {
                "date": "2026-02-10T19:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-03T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5911ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5911\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Hurd of Colorado introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of Agriculture to convey to the City of Ouray, Colorado, certain land managed by the Forest Service, together with a reservoir.\n#### 1. Short title\nThis Act may be cited as the Crystal Reservoir Conveyance Act .\n#### 2. Conveyance of Federal land to Ouray, Colorado\n##### (a) Definitions\nIn this section:\n**(1) City**\nThe term City means the City of Ouray, Colorado.\n**(2) Federal land**\nThe term Federal land means\u2014\n**(A)**\nthe site known as Crystal Reservoir in Ouray County, Colorado, including\u2014\n**(i)**\nthe lake associated with that reservoir;\n**(ii)**\nFull Moon Dam and associated facilities, including the spillway and outlet;\n**(iii)**\nFull Moon Ditch and Reservoir Number 10; and\n**(iv)**\nall infrastructure associated with the reservoir; and\n**(B)**\nthe parcel comprising approximately 45 acres of land underlying and surrounding Crystal Reservoir, as depicted on the Map, managed by the Forest Service as necessary for access for repair, operation, and maintenance of Crystal Reservoir and the features described in clauses (i) through (iv) of subparagraph (A).\n**(3) Map**\nThe term Map means the map prepared by the Forest Service entitled Crystal Reservoir Conveyance and dated June 23, 2025.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance\nAs soon as practicable after the date of enactment of this Act, the Secretary shall convey to the City\u2014\n**(1)**\nall right, title, and interest of the United States in and to the Federal land; and\n**(2)**\nall water rights associated with the Federal land, including the Full Moon Ditch and Reservoir Number 10 water rights described in the decree of the State of Colorado in Civil Action No. 1959, dated May 11, 1942.\n##### (c) Requirements\nThe conveyance under subsection (b) shall be\u2014\n**(1)**\nmade by quitclaim deed;\n**(2)**\nsubject to\u2014\n**(A)**\nvalid existing rights; and\n**(B)**\nthe reversionary interest described in subsection (e)(3); and\n**(3)**\nexcept as provided in subsection (d)(2), completed at no cost to the City.\n##### (d) Costs\n**(1) In general**\nExcept as provided in paragraph (2), the Secretary shall pay all costs associated with the conveyance under subsection (b).\n**(2) Survey**\nThe City shall pay all costs associated with any surveys conducted for the purpose of accomplishing the conveyance under subsection (b).\n##### (e) Terms and conditions\n**(1) In general**\nAs a condition of the conveyance of the Federal land under subsection (b), the City shall agree\u2014\n**(A)**\nto grant to the Secretary an easement for each trail and road in existence on the date of the conveyance that, as determined by the Secretary, originates at, terminates at, or traverses the Federal land;\n**(B)**\neffective beginning on the date of the conveyance, to assume responsibility for the costs of all repairs, operations, and maintenance of Full Moon Dam and related infrastructure, including Full Moon Ditch and Reservoir Number 10;\n**(C)**\nto maintain the Federal land in perpetuity as open space, to be held open\u2014\n**(i)**\nfor full public access for recreational activities, including fishing; and\n**(ii)**\nnot subject to any fee for recreational access;\n**(D)**\nnot to conduct on the Federal land any development, commercial operations, or construction, other than as needed for the operation and maintenance of Full Moon Dam, Crystal Reservoir, and related infrastructure, including Full Moon Ditch and Reservoir Number 10; and\n**(E)**\nnot to expand the historical footprint of Crystal Reservoir in a manner that would flood, impair, or harm any wetlands located upstream of the Federal land, subject to the condition that deepening Crystal Reservoir in a manner consistent with the water rights of the City shall be allowed.\n**(2) Other terms and conditions**\nThe conveyance under subsection (b) shall be subject to such other terms and conditions as the Secretary determines to be appropriate.\n**(3) Reversionary interest**\nIf the Federal land conveyed under subsection (b) ceases to be used in accordance with the terms and conditions under this subsection, the Federal land shall revert to the United States, at the discretion of the Secretary, if the Secretary determines that reversion is in the best interest of the United States.\n##### (f) Use of Red Mountain Ditch\nAfter the conveyance under subsection (b), the Secretary shall allow the structure located near the Federal land commonly known as Red Mountain Ditch , located near Red Mountain Pass, to continue to be used by the City for all decreed purposes under Colorado water law, including the diversion and delivery of water for storage in Crystal Reservoir.\n##### (g) Water rights\n**(1) In general**\nSubject to paragraph (2), the City may use Crystal Reservoir for\u2014\n**(A)**\nstorage of water and in-reservoir uses, consistent with any water rights; or\n**(B)**\nreleases of water for augmentation and other beneficial uses, consistent with any water rights.\n**(2) State water law**\nThe City shall manage all water rights associated with the Federal land in accordance with applicable water laws of the State of Colorado.\n##### (h) Rule of construction\nNothing in this section prohibits the City from making any expenditure for repair of Full Moon Dam or any other feature of the Federal land before the date of the conveyance under subsection (b), subject to the approval of the Secretary.\n##### (i) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall finalize the Map and a legal description of the Federal land to be conveyed under subsection (b).\n**(2) Corrections**\nThe Secretary and the City, by mutual agreement, may correct any minor errors in the Map or legal description under paragraph (1).\n**(3) Map on file**\nThe Map and legal description under paragraph (1) shall be on file and available for public inspection in each appropriate office of the Forest Service.",
      "versionDate": "2025-11-04",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr5911rh.xml",
      "text": "IB\nUnion Calendar No. 576\n119th CONGRESS\n2d Session\nH. R. 5911\n[Report No. 119\u2013662]\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Hurd of Colorado introduced the following bill; which was referred to the Committee on Natural Resources\nMay 20, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on November 4, 2025\nA BILL\nTo direct the Secretary of Agriculture to convey to the City of Ouray, Colorado, certain land managed by the Forest Service, together with a reservoir.\n#### 1. Short title\nThis Act may be cited as the Crystal Reservoir Conveyance Act .\n#### 2. Conveyance of Federal land to Ouray, Colorado\n##### (a) Definitions\nIn this section:\n**(1) City**\nThe term City means the City of Ouray, Colorado.\n**(2) Federal land**\nThe term Federal land means\u2014\n**(A)**\nthe site known as Crystal Reservoir in Ouray County, Colorado, including\u2014\n**(i)**\nthe lake associated with that reservoir;\n**(ii)**\nFull Moon Dam and associated facilities, including the spillway and outlet;\n**(iii)**\nFull Moon Ditch and Reservoir Number 10; and\n**(iv)**\nall infrastructure associated with the reservoir; and\n**(B)**\nthe parcel comprising approximately 45 acres of land underlying and surrounding Crystal Reservoir, as depicted on the Map, managed by the Forest Service as necessary for access for repair, operation, and maintenance of Crystal Reservoir and the features described in clauses (i) through (iv) of subparagraph (A).\n**(3) Map**\nThe term Map means the map prepared by the Forest Service entitled Crystal Reservoir Conveyance and dated June 23, 2025.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (b) Conveyance\nAs soon as practicable after the date of enactment of this Act, the Secretary shall convey to the City\u2014\n**(1)**\nexcept as otherwise provided in this Act, all right, title, and interest of the United States in and to the Federal land; and\n**(2)**\nall right, title and interest of the United States in and to any water rights held for use on, appurtenant to, or otherwise associated with the Federal land, including the Full Moon Ditch and Reservoir Number 10 water rights described in the decree of the State of Colorado in Civil Action No. 1959, dated May 11, 1942.\n##### (c) Requirements\nThe conveyance under subsection (b) shall\u2014\n**(1)**\nconvey fee simple title to the Federal land;\n**(2)**\nbe subject to\u2014\n**(A)**\nvalid existing rights;\n**(B)**\nthe reservation to the United States, in the deed conveying the Federal land, of easements for each road, trail, and trailhead in existence on the date of the conveyance, together with such additional rights as are reasonably necessary for access, administration, operation, maintenance, repair, and replacement of those improvements; and\n**(C)**\nthe reversionary interest described in subsection (e)(3); and\n**(3)**\nexcept as provided in subsection (d)(2), be completed at no cost to the City.\n##### (d) Costs\n**(1) In general**\nExcept as provided in paragraph (2), the Secretary shall pay all costs associated with the conveyance under subsection (b).\n**(2) Survey**\nThe City shall pay all costs associated with any surveys conducted for the purpose of accomplishing the conveyance under subsection (b).\n##### (e) Terms and conditions\n**(1) In general**\nAs a condition of the conveyance of the Federal land under subsection (b), the City shall agree\u2014\n**(A)**\neffective beginning on the date of the conveyance, to assume responsibility for the costs of all repairs, operations, maintenance, replacement, rehabilitation, and regulatory compliance relating to Full Moon Dam and related infrastructure, including Full Moon Ditch and Reservoir Number 10;\n**(B)**\nto maintain the Federal land in perpetuity as open space, to be held open\u2014\n**(i)**\nfor public access for recreational activities, including fishing, except as reasonably necessary for public safety, resource protection, emergency response, or the operation, maintenance, repair, replacement, or rehabilitation of Full Moon Dam, Crystal Reservoir, or related infrastructure; and\n**(ii)**\nnot subject to any fee for recreational access;\n**(C)**\nnot to conduct on the Federal land any development, commercial operations, or construction, other than as needed for the operation, maintenance, repair, replacement, rehabilitation, public safety, and regulatory compliance for dam safety of Full Moon Dam, Crystal Reservoir, and related infrastructure, including Full Moon Ditch and Reservoir Number 10; and\n**(D)**\nnot to expand the surface footprint of Crystal Reservoir at normal operating levels (as depicted on the Map) in a manner that would flood, impair, or harm any wetlands located upstream of the Federal land, subject to the condition that deepening Crystal Reservoir in a manner consistent with the water rights of the City shall otherwise be allowed.\n**(2) Necessary action agreement**\nThe conveyance under subsection (b) shall be made subject to terms agreed to by the Secretary and the City that authorize the City to take such action on the easements described in subsection (c)(2)(B) as the City determines is reasonable and necessary for\u2014\n**(A)**\npublic safety;\n**(B)**\nemergency response; or\n**(C)**\nthe operation, maintenance, repair, replacement, or rehabilitation by the City of Full Moon Dam, Crystal Reservoir, or related infrastructure.\n**(3) Other terms and conditions**\nThe conveyance under subsection (b) shall be subject to such other terms and conditions as the Secretary determines to be appropriate.\n**(4) Reversionary interest**\n**(A) Written notice**\nIf the Federal land conveyed under subsection (b) ceases to be used in accordance with the terms and conditions under this subsection the Secretary shall submit to the City written notice with respect to such use.\n**(B) Reversion**\nAfter the 90-day period beginning on the date written notice is submitted to the City under subparagraph (A), if the Federal land conveyed under subsection (b) continues to be used in a manner not in accordance with the terms and conditions under this subsection during such period, the Federal land shall revert to the United States, at the discretion of the Secretary, if the Secretary determines that reversion is in the best interest of the United States.\n##### (f) Easement\n**(1) In general**\nAfter the conveyance under subsection (b), the Secretary\u2014\n**(A)**\nshall recognize a perpetual easement for the Red Mountain Ditch for use by the City\u2014\n**(i)**\nfor the purposes relating to the Ditch specified in the decrees entitled Case No. 1751-B and Case No. 2013CW3040 for the State of Colorado, including the diversion and delivery of water (not to exceed 6 cubic feet per second) for storage in Crystal Reservoir and subsequent beneficial use; and\n**(ii)**\nto access, operate, maintain, repair, replace, or improve the Ditch and its appurtenances for such purposes; and\n**(B)**\nmay require special use authorizations for non-routine maintenance and repairs of Red Mountain Ditch or for the replacement or improvement of the Ditch.\n**(2) Red Mountain Ditch defined**\nIn this subsection, the term Red Mountain Ditch means the Ditch known as Red Mountain Ditch constructed in or about 1945 located, as of the date of the enactment of this Act, on lands administered by the San Juan National Forest and the Grand Mesa, Uncompahgre, and Gunnison National Forest, in Section 14, Township 42 North, Range 8 West, New Mexico Principal Meridian.\n##### (g) Water rights\nAfter the conveyance under subsection (b), the City may use water in Crystal Reservoir for any beneficial use, subject to applicable water laws of the State of Colorado.\n##### (h) Map and legal description\n**(1) In general**\nAs soon as practicable after the date of enactment of this Act, the Secretary shall finalize the Map and a legal description of the Federal land to be conveyed under subsection (b).\n**(2) Corrections**\nThe Secretary and the City, by mutual agreement, may correct any clerical or typographical errors in the Map or legal description under paragraph (1).\n**(3) Map on file**\nThe Map and legal description under paragraph (1) shall be on file and available for public inspection in each appropriate office of the Forest Service.",
      "versionDate": "2026-05-20",
      "versionType": "Reported in House"
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
        "actionDate": "2026-02-12",
        "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held."
      },
      "number": "2754",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Crystal Reservoir Conveyance Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colorado",
            "updateDate": "2026-02-17T20:20:35Z"
          },
          {
            "name": "Dams and canals",
            "updateDate": "2026-02-17T20:20:35Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-02-17T20:20:35Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-17T20:20:35Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2026-02-17T20:20:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-28T14:40:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-05-20",
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
          "measure-id": "id119hr5911",
          "measure-number": "5911",
          "measure-type": "hr",
          "orig-publish-date": "2026-05-20",
          "originChamber": "HOUSE",
          "update-date": "2026-05-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5911v07",
            "update-date": "2026-05-29"
          },
          "action-date": "2026-05-20",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Crystal Reservoir Conveyance Act</strong></p><p>This bill directs the Forest Service to convey specified property and water rights in\u00a0Ouray County, Colorado, to the City of Ouray, Colorado, for use as open space for recreational activities (such as fishing) at no cost to the public.</p><p>The property and water rights include the site known as Crystal Reservoir and the associated lake and infrastructure, Full Moon Dam and the associated facilities, and the approximately 45-acre parcel of land underlying and surrounding Crystal Reservoir.</p><p>The conveyance must (1) convey fee simple title to the land; (2) be subject to existing valid rights and easements; and (3) be completed at no cost to the city, except for costs related to necessary surveys.</p><p>The conveyance must also be subject to a reversionary interest whereby if the land is used in a manner that violates the conveyance, the land shall revert to the United States, subject to the discretion of the Forest Service.\u00a0</p><p>In addition to holding the land open to the public for recreational purposes, the city must assume responsibly for Full Moon Dam and must not conduct unneeded development or commercial operations, nor alter Crystal Reservoir in a manner that would harm wetlands located upstream, subject to certain conditions.\u00a0</p><p>After the completion of this conveyance, the Forest Service\u00a0must recognize a perpetual easement for the site known as Red Mountain Ditch for use by the city\u00a0for specified activities related to Crystal Reservoir.\u00a0</p>"
        },
        "title": "Crystal Reservoir Conveyance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5911.xml",
    "summary": {
      "actionDate": "2026-05-20",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Crystal Reservoir Conveyance Act</strong></p><p>This bill directs the Forest Service to convey specified property and water rights in\u00a0Ouray County, Colorado, to the City of Ouray, Colorado, for use as open space for recreational activities (such as fishing) at no cost to the public.</p><p>The property and water rights include the site known as Crystal Reservoir and the associated lake and infrastructure, Full Moon Dam and the associated facilities, and the approximately 45-acre parcel of land underlying and surrounding Crystal Reservoir.</p><p>The conveyance must (1) convey fee simple title to the land; (2) be subject to existing valid rights and easements; and (3) be completed at no cost to the city, except for costs related to necessary surveys.</p><p>The conveyance must also be subject to a reversionary interest whereby if the land is used in a manner that violates the conveyance, the land shall revert to the United States, subject to the discretion of the Forest Service.\u00a0</p><p>In addition to holding the land open to the public for recreational purposes, the city must assume responsibly for Full Moon Dam and must not conduct unneeded development or commercial operations, nor alter Crystal Reservoir in a manner that would harm wetlands located upstream, subject to certain conditions.\u00a0</p><p>After the completion of this conveyance, the Forest Service\u00a0must recognize a perpetual easement for the site known as Red Mountain Ditch for use by the city\u00a0for specified activities related to Crystal Reservoir.\u00a0</p>",
      "updateDate": "2026-05-29",
      "versionCode": "id119hr5911"
    },
    "title": "Crystal Reservoir Conveyance Act"
  },
  "summaries": [
    {
      "actionDate": "2026-05-20",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Crystal Reservoir Conveyance Act</strong></p><p>This bill directs the Forest Service to convey specified property and water rights in\u00a0Ouray County, Colorado, to the City of Ouray, Colorado, for use as open space for recreational activities (such as fishing) at no cost to the public.</p><p>The property and water rights include the site known as Crystal Reservoir and the associated lake and infrastructure, Full Moon Dam and the associated facilities, and the approximately 45-acre parcel of land underlying and surrounding Crystal Reservoir.</p><p>The conveyance must (1) convey fee simple title to the land; (2) be subject to existing valid rights and easements; and (3) be completed at no cost to the city, except for costs related to necessary surveys.</p><p>The conveyance must also be subject to a reversionary interest whereby if the land is used in a manner that violates the conveyance, the land shall revert to the United States, subject to the discretion of the Forest Service.\u00a0</p><p>In addition to holding the land open to the public for recreational purposes, the city must assume responsibly for Full Moon Dam and must not conduct unneeded development or commercial operations, nor alter Crystal Reservoir in a manner that would harm wetlands located upstream, subject to certain conditions.\u00a0</p><p>After the completion of this conveyance, the Forest Service\u00a0must recognize a perpetual easement for the site known as Red Mountain Ditch for use by the city\u00a0for specified activities related to Crystal Reservoir.\u00a0</p>",
      "updateDate": "2026-05-29",
      "versionCode": "id119hr5911"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5911ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr5911rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Crystal Reservoir Conveyance Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Crystal Reservoir Conveyance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "title": "Crystal Reservoir Conveyance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Agriculture to convey to the City of Ouray, Colorado, certain land managed by the Forest Service, together with a reservoir.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T04:48:16Z"
    }
  ]
}
```
