# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3157
- Title: State Energy Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3157
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-02-04T05:06:19Z
- Update date including text: 2026-02-04T05:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-03 - Committee: Referred to the Subcommittee on Energy.
- 2025-06-05 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-06-05 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 20.
- 2025-09-17 - Calendars: Placed on the Union Calendar, Calendar No. 255.
- 2025-09-17 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-301.
- 2025-09-17 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-301.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-03 - Committee: Referred to the Subcommittee on Energy.
- 2025-06-05 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-06-05 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Ordered to be Reported by the Yeas and Nays: 27 - 20.
- 2025-09-17 - Calendars: Placed on the Union Calendar, Calendar No. 255.
- 2025-09-17 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-301.
- 2025-09-17 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-301.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3157",
    "number": "3157",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "State Energy Accountability Act",
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
      "actionCode": "H12410",
      "actionDate": "2025-09-17",
      "calendarNumber": {
        "calendar": "U00255"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 255.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-09-17",
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
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-301.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-301.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 27 - 20.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
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
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
        "item": [
          {
            "date": "2025-09-17T21:48:22Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-25T16:08:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-01T13:04:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-05T20:14:00Z",
                "name": "Reported by"
              },
              {
                "date": "2025-06-05T20:13:00Z",
                "name": "Markup by"
              },
              {
                "date": "2025-06-03T20:12:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "CO"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3157ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3157\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Langworthy (for himself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to the evaluation of State intermittent energy policies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Energy Accountability Act .\n#### 2. Consideration of effects of State policies on reliable availability of electric energy\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Evaluation of effects of State policies on reliable availability of electric energy (A) In general Each State regulatory authority that implements an intermittent energy policy shall conduct, and make publicly available, a general evaluation of\u2014 (i) the effects of implementing the intermittent energy policy on the reliability of the bulk-power system in the State, including an assessment of the adequacy of available electric energy resources over a 10-year period; (ii) the ability of electric energy resources that comply with the requirements of the intermittent energy policy to meet electric energy demand during emergencies, periods of high demand, or extreme weather events; (iii) the effects of implementing the intermittent energy policy on rates charged by electric utilities; (iv) whether reliable generation facilities that are removed from service in order to comply with the requirements of the intermittent energy policy can be replaced with sufficient electric generation facilities meeting such requirements, which have a capacity accreditation that is equivalent to the capacity accreditation of the removed facilities, to maintain the reliability of the bulk-power system in the State; and (v) the extent to which implementation of the intermittent energy policy requires electric utilities in the State to use replacement electric energy supplies that are generated by reliable generation facilities located outside the State in order to maintain the reliability of the bulk-power system in the State. (B) Prior State actions Notwithstanding section 124 and paragraphs (1) and (2) of section 112(a), each State regulatory authority shall consider and make a determination concerning the standard set out in subparagraph (A) in accordance with the requirements of subsections (a) and (b) of this section, without regard to any proceedings commenced prior to the enactment of this paragraph. (C) Time limitation Notwithstanding subsections (b) and (c) of section 112, each State regulatory authority shall consider and make a determination concerning whether it is appropriate to implement the standard set out in subparagraph (A) not later than 1 year after the date of enactment of this paragraph. (D) Public availability A State regulatory authority that has made a determination concerning whether to implement, and is implementing, the standard set out in subparagraph (A) shall make publicly available the general evaluation described in such subparagraph\u2014 (i) if the applicable State has adopted an intermittent energy policy before the date on which the State regulatory authority makes such determination, not later than 1 year after such date of determination; and (ii) if the applicable State adopts an intermittent energy policy after the date on which the State regulatory authority makes such determination, not later than 1 year after the date of such adoption. (E) Definitions In this paragraph: (i) Bulk-power system The term bulk-power system has the meaning given that term in section 215 of the Federal Power Act ( 16 U.S.C. 824o ). (ii) Intermittent energy policy The term intermittent energy policy means any requirement of a State, enforced by a State regulatory authority, that a State regulated electric utility ensure that a specified portion of the electric energy sold by such electric utility is generated by facilities that are not reliable generation facilities. (iii) Reliable generation facility The term reliable generation facility means an electric generation facility that ensures the reliable availability of electric energy by\u2014 (I) having operational characteristics to enable the generation of electric energy on a continuous basis for a period of not fewer than 30 days; (II) having\u2014 (aa) adequate fuel, or a continuously available energy source, on-site to enable the generation of electric energy on a continuous basis for a period of not fewer than 30 days; or (bb) contractual obligations that ensure adequate fuel supply to achieve the generation of electric energy on a continuous basis for a period of not fewer than 30 days; (III) having operational characteristics to enable the generation of electric energy during emergency and severe weather conditions; and (IV) providing essential services related to the reliable availability of electric energy, including frequency support and voltage support. .",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3157rh.xml",
      "text": "IB\nUnion Calendar No. 255\n119th CONGRESS\n1st Session\nH. R. 3157\n[Report No. 119\u2013301]\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Langworthy (for himself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nSeptember 17, 2025 Additional sponsor: Mr. Balderson\nSeptember 17, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to the evaluation of State intermittent energy policies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Energy Accountability Act .\n#### 2. Consideration of effects of State policies on reliable availability of electric energy\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Evaluation of effects of State policies on reliable availability of electric energy (A) In general Each State regulatory authority that implements an intermittent energy policy shall conduct, and make publicly available, a general evaluation of\u2014 (i) the effects of implementing the intermittent energy policy on the reliability of the bulk-power system in the State, including an assessment of the adequacy of available electric energy resources over a 10-year period; (ii) the ability of electric energy resources that comply with the requirements of the intermittent energy policy to meet electric energy demand during emergencies, periods of high demand, or extreme weather events; (iii) the effects of implementing the intermittent energy policy on rates charged by electric utilities; (iv) whether reliable generation facilities that are removed from service in order to comply with the requirements of the intermittent energy policy can be replaced with sufficient electric generation facilities meeting such requirements, which have a capacity accreditation that is equivalent to the capacity accreditation of the removed facilities, to maintain the reliability of the bulk-power system in the State; and (v) the extent to which implementation of the intermittent energy policy requires electric utilities in the State to use replacement electric energy supplies that are generated by reliable generation facilities located outside the State in order to maintain the reliability of the bulk-power system in the State. (B) Prior State actions Notwithstanding section 124 and paragraphs (1) and (2) of section 112(a), each State regulatory authority shall consider and make a determination concerning the standard set out in subparagraph (A) in accordance with the requirements of subsections (a) and (b) of this section, without regard to any proceedings commenced prior to the enactment of this paragraph. (C) Time limitation Notwithstanding subsections (b) and (c) of section 112, each State regulatory authority shall consider and make a determination concerning whether it is appropriate to implement the standard set out in subparagraph (A) not later than 1 year after the date of enactment of this paragraph. (D) Public availability A State regulatory authority that has made a determination concerning whether to implement, and is implementing, the standard set out in subparagraph (A) shall make publicly available the general evaluation described in such subparagraph\u2014 (i) if the applicable State has adopted an intermittent energy policy before the date on which the State regulatory authority makes such determination, not later than 1 year after such date of determination; and (ii) if the applicable State adopts an intermittent energy policy after the date on which the State regulatory authority makes such determination, not later than 1 year after the date of such adoption. (E) Definitions In this paragraph: (i) Bulk-power system The term bulk-power system has the meaning given that term in section 215 of the Federal Power Act ( 16 U.S.C. 824o ). (ii) Intermittent energy policy The term intermittent energy policy means any requirement of a State, enforced by a State regulatory authority, that a State regulated electric utility ensure that a specified portion of the electric energy sold by such electric utility is generated by facilities that are not reliable generation facilities. (iii) Reliable generation facility The term reliable generation facility means an electric generation facility that ensures the reliable availability of electric energy by\u2014 (I) having operational characteristics to enable the generation of electric energy on a continuous basis for a period of not fewer than 30 days; (II) having\u2014 (aa) adequate fuel, or a continuously available energy source, on-site to enable the generation of electric energy on a continuous basis for a period of not fewer than 30 days; or (bb) contractual obligations that ensure adequate fuel supply to achieve the generation of electric energy on a continuous basis for a period of not fewer than 30 days; (III) having operational characteristics to enable the generation of electric energy during emergency and severe weather conditions; and (IV) providing essential services related to the reliable availability of electric energy, including frequency support and voltage support. .",
      "versionDate": "2025-09-17",
      "versionType": "Reported in House"
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
            "name": "Electric power generation and transmission",
            "updateDate": "2025-07-14T14:53:57Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-07-14T14:56:38Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-07-14T14:54:12Z"
          },
          {
            "name": "Public utilities and utility rates",
            "updateDate": "2025-07-14T14:56:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-21T13:20:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-17",
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
          "measure-id": "id119hr3157",
          "measure-number": "3157",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-17",
          "originChamber": "HOUSE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3157v07",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-09-17",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>State Energy Accountability Act</strong></p><p>This bill directs each state that implements certain energy policies (e.g., policies that require solar or wind energy) to conduct, and make publicly available, a general evaluation of the effects that those policies have on the rates and reliability of the state's electric power grid, including information about meeting electricity demand during emergencies, periods of high demand, or extreme weather events.</p>"
        },
        "title": "State Energy Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3157.xml",
    "summary": {
      "actionDate": "2025-09-17",
      "actionDesc": "Reported to House",
      "text": "<p><strong>State Energy Accountability Act</strong></p><p>This bill directs each state that implements certain energy policies (e.g., policies that require solar or wind energy) to conduct, and make publicly available, a general evaluation of the effects that those policies have on the rates and reliability of the state's electric power grid, including information about meeting electricity demand during emergencies, periods of high demand, or extreme weather events.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119hr3157"
    },
    "title": "State Energy Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-17",
      "actionDesc": "Reported to House",
      "text": "<p><strong>State Energy Accountability Act</strong></p><p>This bill directs each state that implements certain energy policies (e.g., policies that require solar or wind energy) to conduct, and make publicly available, a general evaluation of the effects that those policies have on the rates and reliability of the state's electric power grid, including information about meeting electricity demand during emergencies, periods of high demand, or extreme weather events.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119hr3157"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3157ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3157rh.xml"
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
      "title": "State Energy Accountability Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-09-18T06:53:16Z"
    },
    {
      "title": "State Energy Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Energy Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to the evaluation of State intermittent energy policies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:24Z"
    }
  ]
}
```
