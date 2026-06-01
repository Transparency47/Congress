# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1262
- Title: A bill to require the Secretary of Agriculture to release a reversionary interest in certain land in the Black River State Forest in Millston, Wisconsin, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1262
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2026-02-27T19:20:22Z
- Update date including text: 2026-02-27T19:20:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 209.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 209.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1262",
    "number": "1262",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "A bill to require the Secretary of Agriculture to release a reversionary interest in certain land in the Black River State Forest in Millston, Wisconsin, and for other purposes.",
    "type": "S",
    "updateDate": "2026-02-27T19:20:22Z",
    "updateDateIncludingText": "2026-02-27T19:20:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 209.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-02",
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
            "date": "2025-10-27T22:36:45Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T20:01:07Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-02T20:09:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1262is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1262\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Johnson (for himself and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture to release a reversionary interest in certain land in the Black River State Forest in Millston, Wisconsin, and for other purposes.\n#### 1. Release of reversionary interest, Black River State Forest, Wisconsin\n##### (a) Definitions\nIn this section:\n**(1) Deli, Inc**\nThe term Deli, Inc. means Deli, Inc., a sphagnum moss production business located in Millston, Wisconsin.\n**(2) Deli land**\nThe term Deli land means the approximately 37.27 acres of land owned or optioned to acquire, subject to the approval of the land exchange by the Wisconsin Department of Natural Resources, the Wisconsin Natural Resources Board, and the Governor of the State, in 2 separate parcels, by Deli, Inc., located in Millston, Wisconsin, as depicted on the map and more particularly described as follows:\n**(A)**\nThe approximately 31.3-acre parcel (including land within the road right-of-way), together with any improvements\u2014\n**(i)**\ncomprising the NE 1/4 NE 1/4 of sec. 29, T. 20 N., R. 2 W., Town of Millston, Jackson County, Wisconsin;\n**(ii)**\nexcluding\u2014\n**(I)**\nland lying north of the railroad right-of-way; and\n**(II)**\na parcel 150 feet wide, with 50 feet lying to the northeast, and 100 feet to the southwest, of a line commencing at a point 5 feet east of the northwest corner of the quarter-quarter section described in clause (i), thence south 56\u00b0 E. 39\u2032 a distance of 222 feet, thence south 57\u00b0 E. 31\u2032 a distance of 1359 feet; and\n**(iii)**\nsubject to\u2014\n**(I)**\nany public water use or easements on Lee Lake; and\n**(II)**\nany easements or restrictions of record, public roadways, zoning and use ordinances, and the railroad right-of-way.\n**(B)**\nThe approximately 5.97-acre parcel located in the SW 1/4 SW 1/4 of sec. 20, T. 20 N., R. 4 W., Town of Millston, Jackson County, Wisconsin, comprising lot 7 of Certified Survey Map No. 4483, as recorded in volume 19S of the certified survey maps, page 334, as Document No. 413440 in the Jackson County Register of Deeds.\n**(3) Map**\nThe term map means the map entitled Black River State Forest \u2013 Deli, Inc. and dated June 26, 2023.\n**(4) State**\nThe term State means the State of Wisconsin.\n**(5) State forest land**\nThe term State forest land means the approximately 31.83 acres of land located in the Black River State Forest in Millston, Wisconsin, as depicted on the map and more particularly described as follows:\n**(A)**\nThe 23.13-acre parcel\u2014\n**(i)**\ncomprising the portion of the E 1/2 SE 1/4 of sec. 20, T. 20 N., R. 2. W., Town of Millston, Jackson County, Wisconsin, lying south of the Interstate 94 southern right-of-way; and\n**(ii)**\nexcluding a triangular parcel in the southwest corner described as commencing at the southwest corner, thence east 260 feet, thence northwesterly to a point on the west boundary thereof 200 feet north of the southwest corner, thence south to the place of beginning.\n**(B)**\nThe 8.70-acre parcel comprising the portion of the NE 1/4 NE 1/4 of sec. 29, T. 20 N., R. 2. W., Town of Millston, Jackson County, Wisconsin, lying north of the railroad right-of-way, forming a triangular piece, and more particularly described as commencing at the northeast corner of that quarter-quarter section, thence west 1010 feet to the north line of the railroad right-of-way, thence southeasterly along the boundary of the railroad to the east line of that quarter-quarter section, thence north on the east line 750 feet to the place of beginning.\n##### (b) Conditional release\n**(1) Findings**\nCongress finds that\u2014\n**(A)**\nthe State forest land is subject to a reversionary interest of the United States pursuant to section 32(c) of The Bankhead-Jones Farm Tenant Act ( 7 U.S.C. 1011(c) ), requiring that the State forest land be used for public purposes in perpetuity; and\n**(B)**\nthe State and Deli, Inc. have agreed that\u2014\n**(i)**\nthe State will convey to Deli, Inc. the State forest land in exchange for the Deli land; and\n**(ii)**\nafter that exchange, the Deli land will be added to Black River State Forest in the State.\n**(2) Release**\nIf the State offers, in a written agreement, to convey to Deli, Inc., the State forest land in exchange for the conveyance of the Deli land by Deli, Inc. to the State\u2014\n**(A)**\nthe reversionary interest of the United States in the State forest land shall be released; and\n**(B)**\nthe Secretary of Agriculture shall provide, as expeditiously as practicable, recordable evidence of the release under subparagraph (A) in the form of a quitclaim deed, which shall\u2014\n**(i)**\nconvey any interest of the United States in and to the State forest land, without consideration; and\n**(ii)**\nbe provided to the State for recording before the exchange deeds are recorded.\n**(3) Corrections**\nThe Secretary of Agriculture, in consultation with the State, may make any necessary corrections to the legal description of the State forest land for purposes of the quitclaim deed described in paragraph (2)(B).",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1262rs.xml",
      "text": "II\nCalendar No. 209\n119th CONGRESS\n1st Session\nS. 1262\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Johnson (for himself and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nOctober 27, 2025 Reported by Mr. Boozman , without amendment\nA BILL\nTo require the Secretary of Agriculture to release a reversionary interest in certain land in the Black River State Forest in Millston, Wisconsin, and for other purposes.\n#### 1. Release of reversionary interest, Black River State Forest, Wisconsin\n##### (a) Definitions\nIn this section:\n**(1) Deli, Inc**\nThe term Deli, Inc. means Deli, Inc., a sphagnum moss production business located in Millston, Wisconsin.\n**(2) Deli land**\nThe term Deli land means the approximately 37.27 acres of land owned or optioned to acquire, subject to the approval of the land exchange by the Wisconsin Department of Natural Resources, the Wisconsin Natural Resources Board, and the Governor of the State, in 2 separate parcels, by Deli, Inc., located in Millston, Wisconsin, as depicted on the map and more particularly described as follows:\n**(A)**\nThe approximately 31.3-acre parcel (including land within the road right-of-way), together with any improvements\u2014\n**(i)**\ncomprising the NE 1/4 NE 1/4 of sec. 29, T. 20 N., R. 2 W., Town of Millston, Jackson County, Wisconsin;\n**(ii)**\nexcluding\u2014\n**(I)**\nland lying north of the railroad right-of-way; and\n**(II)**\na parcel 150 feet wide, with 50 feet lying to the northeast, and 100 feet to the southwest, of a line commencing at a point 5 feet east of the northwest corner of the quarter-quarter section described in clause (i), thence south 56\u00b0 E. 39\u2032 a distance of 222 feet, thence south 57\u00b0 E. 31\u2032 a distance of 1359 feet; and\n**(iii)**\nsubject to\u2014\n**(I)**\nany public water use or easements on Lee Lake; and\n**(II)**\nany easements or restrictions of record, public roadways, zoning and use ordinances, and the railroad right-of-way.\n**(B)**\nThe approximately 5.97-acre parcel located in the SW 1/4 SW 1/4 of sec. 20, T. 20 N., R. 4 W., Town of Millston, Jackson County, Wisconsin, comprising lot 7 of Certified Survey Map No. 4483, as recorded in volume 19S of the certified survey maps, page 334, as Document No. 413440 in the Jackson County Register of Deeds.\n**(3) Map**\nThe term map means the map entitled Black River State Forest \u2013 Deli, Inc. and dated June 26, 2023.\n**(4) State**\nThe term State means the State of Wisconsin.\n**(5) State forest land**\nThe term State forest land means the approximately 31.83 acres of land located in the Black River State Forest in Millston, Wisconsin, as depicted on the map and more particularly described as follows:\n**(A)**\nThe 23.13-acre parcel\u2014\n**(i)**\ncomprising the portion of the E 1/2 SE 1/4 of sec. 20, T. 20 N., R. 2. W., Town of Millston, Jackson County, Wisconsin, lying south of the Interstate 94 southern right-of-way; and\n**(ii)**\nexcluding a triangular parcel in the southwest corner described as commencing at the southwest corner, thence east 260 feet, thence northwesterly to a point on the west boundary thereof 200 feet north of the southwest corner, thence south to the place of beginning.\n**(B)**\nThe 8.70-acre parcel comprising the portion of the NE 1/4 NE 1/4 of sec. 29, T. 20 N., R. 2. W., Town of Millston, Jackson County, Wisconsin, lying north of the railroad right-of-way, forming a triangular piece, and more particularly described as commencing at the northeast corner of that quarter-quarter section, thence west 1010 feet to the north line of the railroad right-of-way, thence southeasterly along the boundary of the railroad to the east line of that quarter-quarter section, thence north on the east line 750 feet to the place of beginning.\n##### (b) Conditional release\n**(1) Findings**\nCongress finds that\u2014\n**(A)**\nthe State forest land is subject to a reversionary interest of the United States pursuant to section 32(c) of The Bankhead-Jones Farm Tenant Act ( 7 U.S.C. 1011(c) ), requiring that the State forest land be used for public purposes in perpetuity; and\n**(B)**\nthe State and Deli, Inc. have agreed that\u2014\n**(i)**\nthe State will convey to Deli, Inc. the State forest land in exchange for the Deli land; and\n**(ii)**\nafter that exchange, the Deli land will be added to Black River State Forest in the State.\n**(2) Release**\nIf the State offers, in a written agreement, to convey to Deli, Inc., the State forest land in exchange for the conveyance of the Deli land by Deli, Inc. to the State\u2014\n**(A)**\nthe reversionary interest of the United States in the State forest land shall be released; and\n**(B)**\nthe Secretary of Agriculture shall provide, as expeditiously as practicable, recordable evidence of the release under subparagraph (A) in the form of a quitclaim deed, which shall\u2014\n**(i)**\nconvey any interest of the United States in and to the State forest land, without consideration; and\n**(ii)**\nbe provided to the State for recording before the exchange deeds are recorded.\n**(3) Corrections**\nThe Secretary of Agriculture, in consultation with the State, may make any necessary corrections to the legal description of the State forest land for purposes of the quitclaim deed described in paragraph (2)(B).",
      "versionDate": "2025-10-27",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
            "name": "Forests, forestry, trees",
            "updateDate": "2025-11-21T15:35:17Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-11-21T15:35:23Z"
          },
          {
            "name": "Wisconsin",
            "updateDate": "2025-11-21T15:35:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-21T21:16:13Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1262is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1262rs.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture to release a reversionary interest in certain land in the Black River State Forest in Millston, Wisconsin, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:18:31Z"
    },
    {
      "title": "A bill to require the Secretary of Agriculture to release a reversionary interest in certain land in the Black River State Forest in Millston, Wisconsin, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:08:55Z"
    }
  ]
}
```
