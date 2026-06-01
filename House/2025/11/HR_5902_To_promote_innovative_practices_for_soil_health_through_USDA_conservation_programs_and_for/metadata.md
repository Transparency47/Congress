# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5902
- Title: Innovative Practices for Soil Health Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5902
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2026-05-16T08:07:35Z
- Update date including text: 2026-05-16T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5902",
    "number": "5902",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Innovative Practices for Soil Health Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:35Z",
    "updateDateIncludingText": "2026-05-16T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
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
        "item": {
          "date": "2025-11-04T19:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-05T19:47:48Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5902ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5902\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Beyer (for himself, Mr. Lawler , and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo promote innovative practices for soil health through USDA conservation programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Innovative Practices for Soil Health Act of 2025 .\n#### 2. Environmental quality incentives program\n##### (a) Definitions\nSection 1240A of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131 ) is amended\u2014\n**(1)**\nin paragraph (6)(B)\u2014\n**(A)**\nin clause (v), by striking and at the end;\n**(B)**\nby redesignating clause (vi) as clause (vii); and\n**(C)**\nby inserting after clause (v) the following:\n(vi) greenhouse gas emissions reduction planning; and ;\n**(2)**\nin paragraph (7), in the matter preceding subparagraph (A), by striking natural resource concern or problem and inserting resource concern ;\n**(3)**\nby redesignating paragraphs (9) and (10) as paragraphs (10) and (11), respectively; and\n**(4)**\nby inserting after paragraph (8) the following:\n(9) Resource concern The term resource concern means a natural resource condition of the soil, water, air, plant, animal, or energy resource base that impairs the sustainability or intended uses of the resource. .\n##### (b) On-Farm conservation innovation trials\nSection 1240H(c)(1)(B)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20138(c)(1)(B)(i) ) is amended\u2014\n**(1)**\nin subclause (II), by inserting on-farm nutrient recycling, after plans, ;\n**(2)**\nin subclause (VI), by striking and at the end; and\n**(3)**\nby adding at the end the following:\n(VIII) perennial production systems, including agroforestry and perennial forages and grain crops; and .\n#### 3. Conservation stewardship program\n##### (a) Definitions\nSection 1240I of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201321 ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by inserting enhancements, after practices, ; and\n**(B)**\nin subparagraph (B)(v), by inserting and climate change before the period at the end;\n**(2)**\nin paragraph (3)(C), by inserting maintained, actively after implemented, ;\n**(3)**\nin paragraph (5), in the matter preceding subparagraph (A), by striking natural resource concern or problem and inserting resource concern ;\n**(4)**\nby redesignating paragraph (7) as paragraph (8); and\n**(5)**\nby inserting after paragraph (6) the following:\n(7) Resource concern The term resource concern means a natural resource condition of the soil, water, air, plant, animal, or energy resource base that impairs the sustainability or intended uses of the resource. .\n##### (b) Conservation Stewardship Program\nSection 1240J(a) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201322(a) ) is amended by striking paragraphs (1) and (2) and inserting the following:\n(1) by maintaining, actively managing, and, where practicable, improving existing conservation activities; and (2) by undertaking additional conservation activities. .\n##### (c) Stewardship contracts\n**(1) Submission of contract offers**\nSection 1240K(a)(2)(B) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201323(a)(2)(B) ) is amended by striking improving, maintaining, and managing and inserting maintaining, actively managing, and, where practicable, improving .\n**(2) Evaluation of contract offers**\nSection 1240K(b) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201323(b) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking clause (iii) and inserting the following:\n(iii) other criteria consistent with an equal weighting of the factors described in clauses (i) and (ii), as determined by the Secretary, including criteria the Secretary determines are necessary to ensure that\u2014 (I) the program effectively targets improvements to soil health, increases in carbon sequestration, and reductions in greenhouse gas emissions; and (II) other national, State, and local priority resource concerns are effectively addressed. ; and\n**(B)**\nby striking paragraph (3).\n**(3) Contract renewal**\nSection 1240K(e) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201323(e) ) is amended to read as follows:\n(e) Contract Renewal (1) In general The Secretary may provide the producer an opportunity to renew an existing contract in the first half of the fifth year of the contract period if the producer\u2014 (A) demonstrates compliance with the terms of the existing contract; (B) agrees to adopt and continue to integrate new or improved conservation activities across the entire agricultural operation, demonstrating continued improvement during the additional 5-year period, as determined by the Secretary; and (C) agrees, by the end of the contract period, to meet the stewardship threshold of at least 2 additional priority resource concerns on the agricultural operation, if applicable. (2) Ranking and payments In determining whether to accept an application for contract renewal under this subsection, and when calculating payments for those renewed contracts, the Secretary shall consider the full conservation benefits across the entire applicable agricultural operation, including\u2014 (A) the number of priority resource concerns with respect to which the producer is expected to meet or exceed the stewardship threshold by the end of the contract period; and (B) the active management and maintenance of ongoing conservation activities, including\u2014 (i) the conservation activities adopted during a prior contract period; and (ii) the new or improved conservation activities to be adopted if a contract is renewed. .\n##### (d) Duties of the Secretary\n**(1) Conservation stewardship payments**\nSection 1240L(c) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(c) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by inserting on 1 or more types of eligible land covered by the contract after activities ; and\n**(ii)**\nin subparagraph (B), by striking improving, maintaining, and managing and inserting maintaining, actively managing, and improving ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking subparagraph (B) and inserting the following:\n(B) Income forgone by the producer, including amounts that reflect\u2014 (i) increased economic risk; and (ii) loss in revenue due to\u2014 (I) production changes; (II) anticipated reductions in yield; (III) transitioning to an organic, resource-conserving cropping or grazing, or perennial production system; or (IV) acreage converted to conservation uses. ; and\n**(ii)**\nin subparagraph (E), by inserting , actively managed, and, where applicable, improved after maintained .\n**(2) Supplemental payments**\nSection 1240L(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(d) ) is amended\u2014\n**(A)**\nin the subsection heading, by inserting , perennial production systems, after rotations ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(ii)**\nby inserting after subparagraph (B) the following:\n(C) Perennial production system The term perennial production system means\u2014 (i) the use of cropland for agroforestry, including alley cropping, silvopasture, and related production practices, as determined by the Secretary; (ii) the use of woodland for agroforestry, including forest farming, multistory cropping, and related production practices, as determined by the Secretary; and (iii) the use of cropland for perennial forages or perennial grain crops. ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking or at the end;\n**(ii)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(C) a perennial production system. ; and\n**(D)**\nin paragraph (3), by striking or advanced grazing management and inserting , advanced grazing management, or a perennial production system .\n**(3) Soil health**\nSection 1240L(k) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(k) ) is amended by striking the period at the end and inserting the following:\n, including by\u2014 (1) conducting outreach to encourage the use of contracts to improve soil health and sequester carbon in the soil; and (2) offering payments for soil testing to provide producers and the Secretary with information on the soil health and carbon sequestration impacts of conservation activities. .\n#### 4. Funding and administration\nSection 1242 of the Food Security Act of 1985 ( 16 U.S.C. 3842 ) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nby inserting an individual, before a commercial entity ;\n**(B)**\nby striking State or local and inserting State, local, or Tribal ; and\n**(C)**\nby striking nutrient management planning, and inserting soil health planning, greenhouse gas emissions reduction planning, nutrient management planning, integrated pest management planning, agroforestry planning, organic transition planning, ;\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (3)(A)\u2014\n**(i)**\nby inserting individuals, before commercial entities, ; and\n**(ii)**\nby striking State or local and inserting State, local, or Tribal ; and\n**(B)**\nin paragraph (5), by inserting or organic after sustainability ; and\n**(3)**\nin subsection (i)\u2014\n**(A)**\nin the subsection heading, by inserting perennial agriculture system, after organic, ; and\n**(B)**\nin paragraph (2), by inserting a perennial agriculture system, after production, each place it appears.\n#### 5. National and regional agroforestry centers\nSection 1243 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 16 U.S.C. 1642 note; Public Law 101\u2013624 ) is amended\u2014\n**(1)**\nby striking the section heading and inserting National and regional agroforestry centers ;\n**(2)**\nby redesignating subsections (b), (c), and (d) as subsections (c), (d), and (e), respectively;\n**(3)**\nby striking subsection (a) and inserting the following:\n(a) Definition of agroforestry In this section, the term agroforestry means a management system that intentionally integrates trees and shrubs into crop and animal farming systems to build more profitable and weather-resilient farms, ranches, and communities, address natural resource concerns and conservation needs, and establish productive and sustainable land use practices, including\u2014 (1) riparian forest buffers; (2) alley cropping; (3) silvopasture; (4) forest farming and multistory cropping; and (5) windbreaks, shelterbelts, hedgerows, field borders, and living snow fences. (b) National and Regional Agroforestry Centers (1) In general The Secretary of Agriculture (referred to in this section as the Secretary )\u2014 (A) shall establish at the Forestry Sciences Laboratory of the Forest Service, in Lincoln, Nebraska, a National Agroforestry Research, Development, and Demonstration Center; and (B) acting through the Chief of the Forest Service and in cooperation with the Natural Resources Conservation Service, shall establish not fewer than 3 additional regional agroforestry centers at other locations, as determined by the Secretary. (2) National and Regional Directors The Secretary, acting through the Chief of the Forest Service, in coordination with the Natural Resources Conservation Service, shall appoint a National Director and Regional Directors to manage and coordinate the program established under subsection (c). ;\n**(4)**\nin subsection (c) (as so redesignated)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby striking Center and inserting Centers established under subparagraphs (A) and (B) of subsection (b)(1) (referred to in this section as the Centers ) ; and\n**(ii)**\nby inserting and organizations after nonprofit foundations ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking on semiarid lands that and inserting that build soil health and ; and\n**(ii)**\nby inserting , including agroforestry systems on semiarid land and other fragile agroecosystems where woody perennial plant communities can enhance carbon sequestration and reduce greenhouse gas emissions before the semicolon;\n**(C)**\nin paragraph (3), by striking forestry products for commercial sale from semiarid land and inserting agroforestry products for commercial sale ;\n**(D)**\nin paragraph (4)\u2014\n**(i)**\nby striking in semiarid regions ; and\n**(ii)**\nby striking the Great Plains region and inserting particular regions ;\n**(E)**\nin paragraph (5), by inserting technical assistance and before technology ;\n**(F)**\nby striking paragraph (6) and inserting the following:\n(6) develop improved silvopasture, alley cropping, forest farming, multistory cropping, riparian buffer, windbreak and shelterbelt, and other perennial production and conservation systems and technologies to improve soil health, carbon sequestration, drought preparedness, soil and water conservation, environmental quality, and biological diversity; ;\n**(G)**\nin paragraph (7), by striking on semiarid lands ;\n**(H)**\nin paragraph (8), by striking on semiarid lands worldwide and inserting worldwide, including on semiarid land ; and\n**(I)**\nin paragraph (9)\u2014\n**(i)**\nby striking on semiarid lands ; and\n**(ii)**\nby inserting and climate change after pollution ;\n**(5)**\nin subsection (d) (as so redesignated)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking Center and inserting Centers ;\n**(B)**\nin paragraph (1), by striking and at the end;\n**(C)**\nin paragraph (2), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(3) facilitate agroforestry adoption by disseminating comprehensive information on Federal, State, local, and Tribal programs that provide support for agroforestry. ; and\n**(6)**\nby amending subsection (e) (as so redesignated) to read as follows:\n(e) Grants The Secretary may establish regional grant programs at each of the Centers to support agroforestry projects, including demonstration farms. .",
      "versionDate": "2025-11-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T16:48:56Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5902ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Innovative Practices for Soil Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "title": "Innovative Practices for Soil Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T10:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote innovative practices for soil health through USDA conservation programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T10:33:21Z"
    }
  ]
}
```
