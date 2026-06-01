# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/411?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/411
- Title: Keweenaw Bay Indian Community Land Claim Settlement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 411
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-10T06:58:14Z
- Update date including text: 2025-12-10T06:58:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-06-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-06-04 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/411",
    "number": "411",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Keweenaw Bay Indian Community Land Claim Settlement Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-10T06:58:14Z",
    "updateDateIncludingText": "2025-12-10T06:58:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
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
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:04:20Z",
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
                "date": "2025-06-11T17:39:58Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-04T14:13:13Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr411ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 411\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Bergman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide compensation to the Keweenaw Bay Indian Community for the taking without just compensation of land by the United States inside the exterior boundaries of the L\u2019Anse Indian Reservation that were guaranteed to the Community under a treaty signed in 1854.\n#### 1. Short title\nThis Act may be cited as the Keweenaw Bay Indian Community Land Claim Settlement Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe Keweenaw Bay Indian Community is a federally recognized Indian Tribe residing on the L\u2019Anse Indian Reservation in Baraga County in the Upper Peninsula of the State of Michigan;\n**(2)**\nthe Community is a successor in interest to the Treaty with the Chippewa Indians of the Mississippi and Lake Superior, made and concluded at La Pointe of Lake Superior October 4, 1842 (7 Stat. 591) (referred to in this section as the 1842 Treaty ), which, among other things, guaranteed the usufructuary rights of the Community over a large area of land that was ceded to the United States, until such time that those usufructuary rights were properly and legally extinguished;\n**(3)**\nthe Community is also a successor in interest to the Treaty with the Chippewa Indians of Lake Superior and the Mississippi, made and concluded at La Pointe September 30, 1854 (10 Stat. 1109) (referred to in this section as the 1854 Treaty );\n**(4)**\narticle 2, paragraph 1 of the 1854 Treaty created the L\u2019Anse Indian Reservation as a permanent reservation;\n**(5)**\npursuant to article 13 of the 1854 Treaty, the 1854 Treaty became obligatory on the contracting parties when ratified by the President and the Senate on January 10, 1855;\n**(6)**\nin 1850, Congress enacted the Act of September 28, 1850 (commonly known and referred to in this section as the Swamp Land Act ) (9 Stat. 519, chapter 84), which authorized the State of Arkansas and other States, including the State of Michigan, to construct the necessary levees and drains to reclaim certain unsold swamp and overflowed lands, made unfit thereby for cultivation and stating that those lands shall remain unsold at the passage of this act\u2026 . ;\n**(7)**\nfollowing enactment of the Swamp Land Act, the State claimed thousands of acres of swamp land in the State pursuant to that Act;\n**(8)**\nbetween 1893 and 1937, the General Land Office patented 2,743 acres of land to the State that were located within the exterior boundaries of the Reservation (referred to in this section as Reservation Swamp Lands );\n**(9)**\nthe right of the Community to use and occupy the unsold land within the Reservation had not been extinguished when the United States patented the Reservation Swamp Lands to the State;\n**(10)**\nin 1852, Congress enacted the Act of August 26, 1852 (10 Stat. 35, chapter 92) (referred to in this section as the Canal Land Act ), to facilitate the building of the Sault Ste. Marie Canal at the Falls of the St. Mary\u2019s River, to connect Lake Superior to Lake Huron;\n**(11)**\npursuant to the Canal Land Act, the United States granted the State the right to select 750,000 acres of unsold public land within the State to defray the cost of construction of the Sault Ste. Marie Canal;\n**(12)**\nthe State identified and selected, among other land, a minimum of 1,333.25 and up to 2,720 acres within the exterior boundaries of the Reservation (referred to in this section as the Reservation Canal Lands );\n**(13)**\nthe Department of the Interior approved the land selections of the State, including the Reservation Canal Lands, after ratification of the 1854 Treaty;\n**(14)**\nthe Secretary noted that the approval described in paragraph (13) was subject to any valid interfering rights ;\n**(15)**\nthe 1854 Treaty set apart from the public domain all unsold land within the Reservation to the Community as of September 30, 1854, which preceded the date on which the State established legally effective title to the Reservation Canal Lands;\n**(16)**\nthe Community made claims to the Department of the Interior with respect to the Reservation Swamp Lands and the Reservation Canal Lands, providing legal analysis and ethnohistorical support for those claims;\n**(17)**\nin December 2021, the Department of the Interior stated that We have carefully reviewed pertinent documents, including the Tribe\u2019s expert reports, and have determined that the Tribe\u2019s claims to the Swamp Lands and Canal Lands have merit ;\n**(18)**\nthe United States, through the actions of the General Land Office, deprived the Community of the exclusive use and occupancy of the Reservation Swamp Lands and the Reservation Canal Lands within the Reservation, without just compensation as required under the Takings Clause of the Fifth Amendment to the Constitution of the United States;\n**(19)**\nthe loss of the Reservation Swamp Lands and the Reservation Canal Lands without just compensation has\u2014\n**(A)**\nimpacted the exercise by the Community of cultural, religious, and subsistence rights on the land;\n**(B)**\ncaused a harmful disconnect between the Community and its land;\n**(C)**\nimpacted the ability of the Community to fully exercise its economy within the Reservation; and\n**(D)**\nhad a negative economic impact on the development of the economy of the Community;\n**(20)**\ncertain non-Indian individuals, entities, and local governments occupy land within the boundaries of the Reservation\u2014\n**(A)**\nacquired ownership interests in the Reservation Swamp Lands and the Reservation Canal Lands in good faith; and\n**(B)**\nhave an interest in possessing clear title to that land;\n**(21)**\nthis Act allows the United States\u2014\n**(A)**\nto secure a fair and equitable settlement of past inequities suffered by the Community as a result of the actions of the United States that caused the taking of the Reservation Swamp Lands and the Reservation Canal Lands without just compensation; and\n**(B)**\nto ensure protection of the ownership of the Reservation Swamp Lands and the Reservation Canal Lands by non-Indian occupants of the Reservation, through the settlement of the claims of the Community to that land, and through that action, the relief of any clouds on title;\n**(22)**\na settlement will allow the Community to receive just compensation and the local landowners to obtain clear title to land, without long and protracted litigation that would be both costly and detrimental to all involved; and\n**(23)**\nthis Act achieves both justice for the Community and security for current landowners through a restorative and non-confrontational process.\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto acknowledge the uncompensated taking by the Federal Government of the Reservation Swamp Lands and the Reservation Canal Lands;\n**(2)**\nto provide compensation to the Community for the uncompensated taking of the Reservation Swamp Lands and the Reservation Canal Lands by the Federal Government;\n**(3)**\nto extinguish all claims by the Community to the Reservation Swamp Lands and the Reservation Canal Lands and to confirm the ownership by the current landowners of the Reservation Swamp Lands and the Reservation Canal Lands, who obtained that land in good faith;\n**(4)**\nto extinguish all potential claims by the Community against the United States, the State, and current landowners concerning title to, use of, or occupancy of the Reservation Swamp Lands and the Reservation Canal Lands; and\n**(5)**\nto authorize the Secretary\u2014\n**(A)**\nto compensate the Community; and\n**(B)**\nto take any other action necessary to carry out this Act.\n#### 4. Definitions\nIn this Act:\n**(1) Community**\nThe term Community means the Keweenaw Bay Indian Community.\n**(2) County**\nThe term County means Baraga County, Michigan.\n**(3) Reservation**\nThe term Reservation means the L\u2019Anse Indian Reservation, located in\u2014\n**(A)**\nT. 51 N., R. 33 W.;\n**(B)**\nT. 51 N., R. 32 W.;\n**(C)**\nT. 50 N., R. 33 W., E 1/2 ;\n**(D)**\nT. 50 N., R. 32 W., W 1/2 ; and\n**(E)**\nthat portion of T. 51 N., R. 31 W. lying west of Huron Bay.\n**(4) Reservation Canal Lands**\nThe term Reservation Canal Lands means the 1,333.25 to 2,720 acres of Community land located within the exterior boundaries of the Reservation that the Federal Government conveyed to the State pursuant to the Act of August 26, 1852 (10 Stat. 35, chapter 92).\n**(5) Reservation Swamp Lands**\nThe term Reservation Swamp Lands means the 2,743 acres of land located within the exterior boundaries of the Reservation that the Federal Government conveyed to the State between 1893 and 1937 pursuant to the Act of September 28, 1850 (commonly known as the Swamp Land Act ) (sections 2479 through 2481 of the Revised Statutes (43 U.S.C. 982 through 984)).\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(7) State**\nThe term State means the State of Michigan.\n#### 5. Payments\n##### (a) Transfer of funds\nAs soon as practicable after the date on which the amount authorized to be appropriated under subsection (c) is made available to the Secretary, the Secretary shall transfer $33,900,000 to the Community.\n##### (b) Use of funds\n**(1) In general**\nSubject to paragraph (2), the Community may use the amount received under subsection (a) for any lawful purpose, including\u2014\n**(A)**\ngovernmental services;\n**(B)**\neconomic development;\n**(C)**\nnatural resources protection; and\n**(D)**\nland acquisition.\n**(2) Restriction on use of funds**\nThe community may not use the amount received under subsection (a) to acquire land for gaming purposes.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out subsection (a), $33,900,000 for fiscal year 2026, to remain available until expended.\n#### 6. Extinguishment of claims\n##### (a) In general\nEffective on the date on which the Community receives the payment under section 5(a), all claims of the Community to the Reservation Swamp Lands and the Reservation Canal Lands owned by persons or entities other than the Community are extinguished.\n##### (b) Clear title\nEffective on the date on which the Community receives the payment under section 5(a), the title of all current owners to the Reservation Swamp Lands and the Reservation Canal Lands is cleared of all preexisting rights held by the Community and any of the members of the Community.\n#### 7. Effect\nNothing in this Act authorizes\u2014\n**(1)**\nthe Secretary to take land into trust for the benefit of the Community for gaming purposes; or\n**(2)**\nthe Community to use land acquired using amounts received under this Act for gaming purposes.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-09-29",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 175."
      },
      "number": "642",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keweenaw Bay Indian Community Land Claim Settlement Act of 2025",
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
            "name": "Federal-Indian relations",
            "updateDate": "2025-02-24T20:42:17Z"
          },
          {
            "name": "Indian claims",
            "updateDate": "2025-02-24T20:42:17Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2025-02-24T20:42:17Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-02-24T20:42:17Z"
          },
          {
            "name": "Michigan",
            "updateDate": "2025-02-24T20:42:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-02-21T12:39:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr411",
          "measure-number": "411",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr411v00",
            "update-date": "2025-03-05"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keweenaw Bay Indian Community Land Claim Settlement Act of 2025</strong></p><p>This bill directs the Department of the Interior to transfer funds to the Keweenaw Bay Indian Community (KBIC) in Baraga County, Michigan, in order to settle the KBIC's land claims and clear title to those lands.</p><p>The KBIC may use these funds for any lawful purpose except to acquire land for gaming.</p>"
        },
        "title": "Keweenaw Bay Indian Community Land Claim Settlement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr411.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keweenaw Bay Indian Community Land Claim Settlement Act of 2025</strong></p><p>This bill directs the Department of the Interior to transfer funds to the Keweenaw Bay Indian Community (KBIC) in Baraga County, Michigan, in order to settle the KBIC's land claims and clear title to those lands.</p><p>The KBIC may use these funds for any lawful purpose except to acquire land for gaming.</p>",
      "updateDate": "2025-03-05",
      "versionCode": "id119hr411"
    },
    "title": "Keweenaw Bay Indian Community Land Claim Settlement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keweenaw Bay Indian Community Land Claim Settlement Act of 2025</strong></p><p>This bill directs the Department of the Interior to transfer funds to the Keweenaw Bay Indian Community (KBIC) in Baraga County, Michigan, in order to settle the KBIC's land claims and clear title to those lands.</p><p>The KBIC may use these funds for any lawful purpose except to acquire land for gaming.</p>",
      "updateDate": "2025-03-05",
      "versionCode": "id119hr411"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr411ih.xml"
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
      "title": "Keweenaw Bay Indian Community Land Claim Settlement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keweenaw Bay Indian Community Land Claim Settlement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide compensation to the Keweenaw Bay Indian Community for the taking without just compensation of land by the United States inside the exterior boundaries of the L'Anse Indian Reservation that were guaranteed to the Community under a treaty signed in 1854.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T10:48:16Z"
    }
  ]
}
```
