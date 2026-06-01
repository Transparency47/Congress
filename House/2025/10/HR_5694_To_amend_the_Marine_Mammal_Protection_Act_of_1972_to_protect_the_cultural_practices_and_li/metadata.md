# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5694?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5694
- Title: ARTIST Act
- Congress: 119
- Bill type: HR
- Bill number: 5694
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2026-05-15T08:08:25Z
- Update date including text: 2026-05-15T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by Unanimous Consent.
- 2026-05-14 - Committee: Subcommittee on Water, Wildlife and Fisheries Discharged
- Latest action: 2025-10-06: Introduced in House

## Actions

- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by Unanimous Consent.
- 2026-05-14 - Committee: Subcommittee on Water, Wildlife and Fisheries Discharged

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5694",
    "number": "5694",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "ARTIST Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:25Z",
    "updateDateIncludingText": "2026-05-15T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
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
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
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
      "actionDate": "2026-05-14",
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
      "text": "Subcommittee on Water, Wildlife and Fisheries Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-19",
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
      "actionDate": "2025-10-06",
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
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-06",
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
            "date": "2026-05-14T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-06T19:01:50Z",
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
                "date": "2026-05-14T14:30:00Z",
                "name": "Discharged from"
              },
              {
                "date": "2026-03-26T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-19T14:00:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5694ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5694\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Mr. Begich introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Marine Mammal Protection Act of 1972 to protect the cultural practices and livelihoods of producers of Alaska Native handicrafts and marine mammal ivory products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Alaska\u2019s Right To Ivory Sales and Tradition Act or the ARTIST Act .\n#### 2. Alaska Native handicrafts\nSection 101(b) of the Marine Mammal Protection Act Of 1972 ( 16 U.S.C. 1371(b) ) is amended to read as follows:\n(b) Exemption for Alaskan Natives (1) Definitions In this subsection: (A) Authentic Alaska Native article of handicrafts and clothing The term authentic Alaska Native article of handicrafts and clothing means an item composed wholly, or in some significant respect, of natural materials that is produced, decorated, or fashioned in the exercise of traditional Alaska Native handicrafts by an Indian, Aleut, or Eskimo who resides in Alaska and who dwells on the coast of the North Pacific Ocean or the Arctic Ocean without the use of a pantograph, multiple carvers, or any other mass copying device. (B) Marine mammal ivory The term marine mammal ivory includes a tooth or tusk from a species of walrus, narwhal, or whale. (C) Traditional Alaska Native handicrafts The term traditional Alaska Native handicrafts includes weaving, carving, stitching, sewing, lacing, beading, drawing, and painting. (2) Exemption (A) In general Except as provided in section 109, the provisions of this Act shall not apply with respect to the taking of any marine mammal by any Indian, Aleut, or Eskimo who resides in Alaska and who dwells on the coast of the North Pacific Ocean or the Arctic Ocean if such taking\u2014 (i) (I) is for subsistence purposes; or (II) is done for purposes of creating and selling authentic Alaska Native articles of handicrafts and clothing; and (ii) in each case, is not accomplished in a wasteful manner. (B) Special rules (i) Interstate commerce of items An item presented as an authentic Alaska Native article of handicrafts and clothing may be sold in interstate commerce only if it comports with the definition provided in paragraph (1)(A). (ii) Edible portion of marine mammal Any edible portion of a marine mammal taken for the primary purpose of creating and selling authentic Alaska Native articles of handicrafts and clothing may be sold in a native village or town in Alaska or for native consumption. (3) Limitations (A) In general Notwithstanding paragraph (2), if, under this Act, the Secretary determines any species or stock of marine mammal subject to taking by Indians, Aleuts, or Eskimos to be depleted, the Secretary may prescribe regulations upon the taking of such marine mammals by any Indian, Aleut, or Eskimo described in this subsection. (B) Content of regulations The regulations described in subparagraph (A) may be established with reference to species or stocks, geographical description of the area included, the season for taking, or any other factors related to the reason for establishing such regulations and consistent with the purposes of this Act. (C) Notice and hearing; removal of regulations The regulations described in subparagraph (A) shall be prescribed after notice and hearing required by section 103 of this title and shall be removed as soon as the Secretary determines that the need for their imposition has disappeared. (D) Regulations to be supported by substantial evidence In promulgating any regulation or making any assessment pursuant to a hearing or proceeding under this subsection or section 117(b)(2), or in making any determination of depletion under this subsection or finding regarding unmitigable adverse impacts under subsection (a)(5) that affects stocks or persons to which this subsection applies, the Secretary shall demonstrate in writing (and make such writing publicly available on the website of the Secretary) that, in consideration of the whole record, including Indigenous knowledge, such regulation, assessment, determination, or finding is supported by substantial evidence. The preceding sentence shall only be applicable in an action brought by one or more Alaska Native organizations representing persons to which this subsection applies. (4) Prohibitions No State shall prohibit the importation, sale, offer for sale, transfer, trade, barter, possession, or possession with the intent to sell, transfer, trade, or barter of marine mammal ivory or marine mammal bone or baleen incorporated under this title by an Indian, Aleut, or Eskimo, into an authentic Alaska Native article of handicrafts and clothing. .",
      "versionDate": "2025-10-06",
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
        "actionDate": "2025-10-10",
        "actionTime": "12:33:05",
        "text": "Held at the desk."
      },
      "number": "254",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ARTIST Act",
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
            "name": "Alaska",
            "updateDate": "2026-03-30T18:26:37Z"
          },
          {
            "name": "Alaska Natives and Hawaiians",
            "updateDate": "2026-03-30T18:26:37Z"
          },
          {
            "name": "Historical and cultural resources",
            "updateDate": "2026-03-30T18:26:37Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2026-03-30T18:26:37Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-03-30T18:26:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-12-16T17:20:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-06",
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
          "measure-id": "id119hr5694",
          "measure-number": "5694",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5694v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Alaska\u2019s Right To Ivory Sales and Tradition Act or the ARTIST Act</strong></p><p>This bill prohibits states from imposing bans on marine mammal products produced by Alaska Natives.</p><p>Specifically, states may not prohibit the importation, sale, transfer, trade, barter, or possession of marine mammal ivory, marine mammal bone, or baleen legally produced by an Alaska Native as an authentic Alaska Native article of handicrafts and clothing.</p>"
        },
        "title": "ARTIST Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5694.xml",
    "summary": {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Alaska\u2019s Right To Ivory Sales and Tradition Act or the ARTIST Act</strong></p><p>This bill prohibits states from imposing bans on marine mammal products produced by Alaska Natives.</p><p>Specifically, states may not prohibit the importation, sale, transfer, trade, barter, or possession of marine mammal ivory, marine mammal bone, or baleen legally produced by an Alaska Native as an authentic Alaska Native article of handicrafts and clothing.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5694"
    },
    "title": "ARTIST Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Alaska\u2019s Right To Ivory Sales and Tradition Act or the ARTIST Act</strong></p><p>This bill prohibits states from imposing bans on marine mammal products produced by Alaska Natives.</p><p>Specifically, states may not prohibit the importation, sale, transfer, trade, barter, or possession of marine mammal ivory, marine mammal bone, or baleen legally produced by an Alaska Native as an authentic Alaska Native article of handicrafts and clothing.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr5694"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5694ih.xml"
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
      "title": "ARTIST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARTIST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Alaska\u2019s Right To Ivory Sales and Tradition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Marine Mammal Protection Act of 1972 to protect the cultural practices and livelihoods of producers of Alaska Native handicrafts and marine mammal ivory products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:18:21Z"
    }
  ]
}
```
