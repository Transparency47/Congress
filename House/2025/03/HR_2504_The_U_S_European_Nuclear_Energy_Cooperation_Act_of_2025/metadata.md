# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2504?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2504
- Title: The U.S.-European Nuclear Energy Cooperation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2504
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-05-12T18:48:56Z
- Update date including text: 2026-05-12T18:48:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 43 - 3.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 43 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2504",
    "number": "2504",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "The U.S.-European Nuclear Energy Cooperation Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T18:48:56Z",
    "updateDateIncludingText": "2026-05-12T18:48:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 43 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
            "date": "2026-03-26T16:24:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-31T16:05:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2504ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2504\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Keating (for himself, Mr. Foster , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State to develop a strategy to strengthen United States-European nuclear energy cooperation and combat Russian malign influence in the nuclear energy sector in Europe.\n#### 1. Short title\nThis Act may be cited as the The U.S.-European Nuclear Energy Cooperation Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn February 24, 2022, the Russian Federation initiated a full-scale invasion of Ukraine which has severely threatened energy security in the United States, Europe, and around the world.\n**(2)**\nThe security of Ukraine\u2019s energy grid has been vital to Ukraine\u2019s success in its defense of its territory and ensuring the Ukrainian government can effectively provide goods and services to Ukrainian citizens.\n**(3)**\nUkraine has operated four nuclear power plants with 15 reactors, primarily Russian-designed water-water energetic reactor (VVER) reactors.\n**(4)**\nRussia, in its war of aggression against Ukraine, has systematically targeted Ukraine\u2019s energy infrastructure through heavy shelling and targeted attacks, particularly in the winter months when innocent Ukrainian civilians are most vulnerable.\n**(5)**\nSince March 2022, Russian forces have illegally occupied the Zaporizhzhia Nuclear Power Station, the largest nuclear power plant in Europe, and Russian forces have surrounded the station with landmines, further threatening regional security.\n**(6)**\nRussian-designed VVER reactors have been built across Europe, including in Belarus, Bulgaria, the Czech Republic, Finland, Germany, Hungary, Slovakia, Turkey, and Ukraine.\n**(7)**\nRussia uses its nuclear power plant designs and fuel services to spread malign influence and threaten United States and European energy security.\n**(8)**\nAs of 2021, Russia owned about 20 percent of the total uranium conversion infrastructure worldwide and in 2020, had the largest uranium enrichment capacity at close to 46 percent.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nin countries seeking or developing a nuclear power industry, the Department of State should prioritize the utilization of products and services from the United States, and then prioritize products and services from Europe and other allied or partner countries, including Canada, Japan, the United Kingdom, and the Republic of Korea when not directly competing with the United States;\n**(2)**\nthe United States and its allies must focus on cooperation, including capacity building and early-stage project support, to expand the nuclear industry in Europe in a way that maintains nonproliferation, security, and safety standards and aligns with international obligations and treaties while combating Russian and Chinese malign influence; and\n**(3)**\nthe United States should continue to pursue the Foundational Infrastructure for Responsible Use of Small Modular Reactor Technology program as a means of helping partner countries meet their clean energy needs with scalable, flexible, secure, and safe nuclear power programs.\n#### 4. Strategy\n##### (a) Strategy required\nThe Secretary of State, in consultation with the Secretary of Energy and the heads of other relevant Federal departments and agencies, shall develop a strategy to strengthen United States-European nuclear energy cooperation and combat Russian malign influence in the nuclear energy sector in Europe.\n##### (b) Elements\nThe strategy required by subsection (a) shall include, at a minimum, the following elements:\n**(1)**\nAn overview and assessment of the Secretary of State\u2019s efforts to broaden participation by United States nuclear industry entities in Europe and promote the accessibility and competitiveness of United States, European, and partner technologies and services against Russian and Chinese technologies in Europe.\n**(2)**\nAn overview of different nuclear reactor types that are currently deployed or under regulatory review in Europe, including large light-water reactors, small modular light-water reactors, and non-light-water reactors, and\u2014\n**(A)**\nwhat role, if any, each reactor type could have in reducing Russia\u2019s influence over European energy supply by 2030, 2035, 2040, 2045, and 2050;\n**(B)**\nchallenges that each reactor type may face with rapid deployment, including costs, market barriers to first-of-a-kind designs, supply chain constraints, and regulatory requirements;\n**(C)**\nthe impacts of each reactor type on maintaining strong nonproliferation standards, including the minimization of weapons-usable nuclear material; and\n**(D)**\nopportunities for the use of United States, European, and partner technologies and services in the deployment or potential deployment of each reactor type.\n**(3)**\nAn overview of different fuel cycles that are currently deployed or under consideration in Europe, including use of low enriched uranium, including high assay low enriched uranium, and spent fuel reprocessing, along with an analysis of the implications of each fuel cycle on\u2014\n**(A)**\nreducing and eliminating Russia\u2019s market share in Europe for uranium, conversion, enrichment, and reactor fuel between now and 2030;\n**(B)**\nachieving long-term energy security free of Russian influence; and\n**(C)**\nmaintaining strong nonproliferation standards, including the minimization of weapons-usable material as well as high nuclear safety and security standards.\n**(4)**\nAn overview of nuclear reactor designs and fuel cycle infrastructure that the United States Government is currently funding the development of, and\u2014\n**(A)**\nthe potential, if any, that each of these technologies have to decrease or eliminate Russia\u2019s market share in the United States and Europe for nuclear power reactors, uranium mining and milling, conversion, enrichment, fuel fabrication, deconversion, and spent nuclear fuel reprocessing in the short, medium, and long term;\n**(B)**\nthe impact of these technologies on the minimization of weapons-usable nuclear material, including the use of highly enriched uranium or plutonium fuels; and\n**(C)**\nan assessment of the use cases for each of these designs and fuel cycles.\n**(5)**\nAn overview of the United States Government\u2019s diplomatic engagements regarding the nuclear energy sector in Europe.\n**(6)**\nA list of countries in Europe with active nuclear power programs, and\u2014\n**(A)**\nan analysis of each country\u2019s nuclear energy policy;\n**(B)**\nan overview of existing areas of cooperation with regards to nuclear energy between each country and\u2014\n**(i)**\nthe United States;\n**(ii)**\nother European and friendly countries; and\n**(iii)**\nadversarial countries including China and Russia;\n**(C)**\nan overview of potential areas for future cooperation between each country and the United States with regards to nuclear energy; and\n**(D)**\na summary of fuel types used in each country\u2019s nuclear power programs.\n**(7)**\nAn overview of Russian and Chinese influence in the European nuclear energy sector.\n**(8)**\nAn overview of how the United States Government is working with allies and partners to counter Russian malign influence within the European energy sector to include steps taken to counter Russian influence in the mining and milling, conversion, enrichment, and fuel fabrication processes as well as in reactor construction.\n**(9)**\nAn overview of how the United States Government balances the urgent strategic need for collaboration with allies and partners on countering Russia\u2019s influence on nuclear energy in Europe, with commercial competitiveness issues that may arise between United States companies and companies in Europe, Canada, Japan, and the Republic of Korea.\n**(10)**\nAn assessment of Rosatom\u2019s role in Russia\u2019s energy sector, to include an overview of strengths and vulnerabilities of the conglomerate.\n##### (c) Submission\nNot later than 120 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate congressional committees the strategy required by subsection (a).\n##### (d) Form\nThe strategy required by subsection (a) shall be submitted in unclassified form, but may contain a classified annex, so long as such annex is provided separately from the unclassified strategy.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated $30,000,000 for each of fiscal years 2025 through 2029 to support critically needed engagement in Europe consistent with the strategy required by section 4(a) on countering Russian malign influence and with a particular focus on responsible nuclear power program capacity building, early stage nuclear power project support, and countering Russian disinformation campaigns.\n#### 6. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives;\n**(B)**\nthe Committee on Foreign Relations of the Senate;\n**(C)**\nthe Committee on Energy and Commerce of the House of the Representatives; and\n**(D)**\nthe Committee on Energy and Natural Resources of the Senate.\n**(2) High assay low enriched uranium**\nThe term high assay low enriched uranium means uranium enriched so that the concentration of the fissile isotope uranium-235 (U-235) is between 5 percent and 20 percent of the mass of uranium.\n**(3) Low enriched uranium**\nThe term low enriched uranium means fuel in which the weight percent of U-235 in the uranium is less than 20 percent.",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-04-14",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Transportation and Infrastructure, Intelligence (Permanent Select), Ways and Means, Rules, the Judiciary, Financial Services, Armed Services, and the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2913",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ukraine Support Act",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-05-12T18:48:24Z"
          },
          {
            "name": "Asia",
            "updateDate": "2026-05-12T16:59:44Z"
          },
          {
            "name": "Canada",
            "updateDate": "2026-05-12T16:59:26Z"
          },
          {
            "name": "China",
            "updateDate": "2026-05-12T17:00:10Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2026-05-12T18:48:56Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-05-12T18:48:32Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-05-12T17:00:20Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-05-12T16:59:21Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-05-12T16:59:14Z"
          },
          {
            "name": "Japan",
            "updateDate": "2026-05-12T16:59:32Z"
          },
          {
            "name": "Nuclear power",
            "updateDate": "2026-05-12T16:58:47Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-05-12T17:00:02Z"
          },
          {
            "name": "South Korea",
            "updateDate": "2026-05-12T16:59:52Z"
          },
          {
            "name": "Technology transfer and commercialization",
            "updateDate": "2026-05-12T17:00:30Z"
          },
          {
            "name": "United Kingdom",
            "updateDate": "2026-05-12T16:59:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-21T17:27:57Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2504ih.xml"
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
      "title": "The U.S.-European Nuclear Energy Cooperation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "The U.S.-European Nuclear Energy Cooperation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to develop a strategy to strengthen United States-European nuclear energy cooperation and combat Russian malign influence in the nuclear energy sector in Europe.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:37Z"
    }
  ]
}
```
