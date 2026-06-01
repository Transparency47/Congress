# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4018?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4018
- Title: To unleash America's offshore critical minerals and resources.
- Congress: 119
- Bill type: HR
- Bill number: 4018
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-09-09T18:22:28Z
- Update date including text: 2025-09-09T18:22:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-17 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-02 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-09-03 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-17 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-02 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-09-03 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4018",
    "number": "4018",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "E000235",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Ezell, Mike [R-MS-4]",
        "lastName": "Ezell",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "To unleash America's offshore critical minerals and resources.",
    "type": "HR",
    "updateDate": "2025-09-09T18:22:28Z",
    "updateDateIncludingText": "2025-09-09T18:22:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:01:15Z",
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
                "date": "2025-09-03T13:16:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-07-02T13:02:01Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-17T15:01:20Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "IA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "FL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "MN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "IN"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "VA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "MS"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "OK"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "OH"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "CO"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4018ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4018\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Ezell (for himself and Mrs. Miller-Meeks ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo unleash America\u2019s offshore critical minerals and resources.\n#### 1. Findings\nCongress finds the following:\n**(1)**\nThe United States has a core national security and economic interest in maintaining leadership in deep sea science and technology and seabed mineral resources.\n**(2)**\nThe United States faces unprecedented economic and national security challenges in securing reliable supplies of critical minerals independent of foreign adversary control.\n**(3)**\nVast offshore seabed areas hold critical minerals and energy resources.\n**(4)**\nThese resources are key to strengthening our economy, securing our energy future, and reducing dependence on foreign suppliers for critical minerals.\n**(5)**\nThe United States also controls seabed mineral resources in one of the largest ocean areas of the world.\n**(6)**\nOur Nation can, through the exercise of existing authorities and by establishing international partnerships, access potentially vast resources in seabed polymetallic nodules, other subsea geologic structures, and coastal deposits containing strategic minerals such as nickel, cobalt, copper, manganese, titanium, and rare earth elements, which are vital to our national security and economic prosperity.\n**(7)**\nOur Nation must take immediate action to accelerate the responsible development of seabed mineral resources, quantify the Nation\u2019s endowment of seabed minerals, reinvigorate American leadership in associated extraction and processing technologies, and ensure secure supply chains for our defense, infrastructure, and energy sectors.\n**(8)**\nIt is the policy of the United States to advance United States leadership in seabed mineral development by\u2014\n**(A)**\nrapidly developing domestic capabilities for the exploration, characterization, collection, and processing of seabed mineral resources through streamlined permitting without compromising environmental and transparency standards;\n**(B)**\nsupporting investment in deep sea science, mapping, and technology;\n**(C)**\nenhancing coordination among executive departments and agencies with respect to seabed mineral development activities described in this Act;\n**(D)**\nestablishing the United States as a global leader in responsible seabed mineral exploration, development technologies, and practices, and as a partner for countries developing seabed mineral resources in areas within their national jurisdictions, including their exclusive economic zones;\n**(E)**\ncreating a robust domestic supply chain for critical minerals derived from seabed mineral resources to support economic growth, reindustrialization, and military preparedness, including through new processing capabilities; and\n**(F)**\nstrengthening partnerships with allies and industry to counter China\u2019s growing influence over seabed mineral resources and to ensure United States companies are well-positioned to support allies and partners interested in developing seabed minerals responsibly in areas within their national jurisdictions, including their exclusive economic zones.\n#### 2. Strategic seabed critical mineral access\n##### (a) Expediting issuance of certain authorizations under Deep Seabed Hard Mineral Resources Act\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Commerce, acting through the Administrator of the National Oceanic and Atmospheric Administration and in consultation with the Secretary of State and Secretary of the Interior, acting through the Director of the Bureau of Ocean Energy Management, shall expedite the process for reviewing and issuing licenses for exploration and permits for commercial recovery under the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1401 et seq. ).\n**(2) Requirements**\nIn expediting the process described in paragraph (1), the entities described in that paragraph shall ensure efficiency, predictability, and competitiveness for United States companies.\n##### (b) Expediting issuance of certain authorizations under Outer Continental Shelf Lands Act\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of the Interior shall establish an expedited process for reviewing and approving permits for prospecting and granting leases under the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 et seq. ).\n**(2) Requirements**\nThe expedited process established under paragraph (1) shall ensure efficiency, predictability, and competitiveness for United States companies.\n##### (c) Seabed mapping plan\nNot later than 60 days after the date of the enactment of this Act, the Secretary of the Interior, in consultation with the Secretary of State, Secretary of Commerce, and heads of other relevant Federal agencies, and in cooperation with commercial and other nongovernmental organizations, shall develop a plan to map priority areas of the seabed United States outer Continental Shelf, to include extended areas of the outer Continental Shelf, such as those with abundant or accessible seabed mineral resources, to accelerate data collection and characterization.\n##### (d) Identification of certain critical minerals\nNot later than 60 days after the date of the enactment of this Act, the Secretary of the Interior\u2014\n**(1)**\nshall identify which critical minerals may be derived from seabed mineral resources; and\n**(2)**\nin coordination with the Secretary of Defense and Secretary of Energy, determine which critical minerals derived from seabed mineral resources are essential for applications such as defense infrastructure, manufacturing, and energy.\n##### (e) Engagement with key partners and allies\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Commerce, in coordination with the Secretary of State, Secretary of the Interior, and Secretary of Energy, shall engage with key partners and allies to offer support for seabed mineral resource exploration, extraction, processing, and environmental monitoring in areas within the jurisdictions of such key partners and allies, including by\u2014\n**(A)**\nseeking scientific collaboration and commercial development opportunities for United States companies; and\n**(B)**\ndeveloping a prioritized list of foreign countries for engagement.\n**(2) Key partner or ally determination**\n**(A) In general**\nThe Secretary of State shall determine whether an entity is a key partner or ally for the purposes of this Act, based on factors such as\u2014\n**(i)**\nexisting agreements with the United States;\n**(ii)**\nalignment with strategic interests of the United States; and\n**(iii)**\nparticipation in joint initiatives.\n**(B) Notification**\nThe Secretary of State shall notify the Secretary of Commerce, Secretary of the Interior, and Secretary of Energy of any determination made under subparagraph (A).\n##### (f) Reports\nNot later than 60 days after the date of the enactment of this Act\u2014\n**(1)**\nthe Secretary of the Interior, in coordination with the Secretary of Commerce and Secretary of Energy, and in consultation with the heads of other relevant Federal agencies, shall submit to the Committee on Natural Resources of the House of Representatives and the Committees on Energy and Natural Resources and Commerce, Science, and Transportation of the Senate a report that identifies private sector interest in and opportunities for seabed mineral resource exploration and mining on the outer Continental Shelf, in areas beyond national jurisdiction, and in areas within the jurisdiction of a foreign country that expresses interest in partnering with United States companies with respect to seabed mineral resource development; and\n**(2)**\nthe Secretary of the Interior, jointly with the Secretary of State, Secretary of Commerce, and Secretary of Energy, shall submit to the Committee on Natural Resources of the House of Representatives and the Committees on Energy and Natural Resources and Commerce, Science, and Transportation of the Senate a report regarding the feasibility of an international benefit-sharing mechanism for seabed mineral resource extraction and development that occurs in an area beyond the jurisdiction of any country.\n#### 3. General provisions\n##### (a) Rule of construction\nNothing in this Act shall be construed to impair or otherwise affect the authority granted by law to an executive department or agency, or the head thereof.\n##### (b) No creation of right or benefit\nThis Act does not create any right or benefit, substantive or procedural, enforceable at law or in equity by any party against the United States, its departments, agencies, entities, officers, employees, or agents, or any other person.\n#### 4. Definitions\nIn this Act:\n**(1) Commercial recovery**\nThe term commercial recovery has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n**(2) Critical mineral**\nThe term critical mineral has the meaning given the term in section 7002(a)(3) of the Energy Act of 2020 ( 30 U.S.C. 1606(a)(3) ).\n**(3) Exploration**\nThe term exploration has the meaning given the term in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).\n**(4) Lease**\nThe term lease has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(5) Mineral**\nThe term mineral means\u2014\n**(A)**\na critical mineral;\n**(B)**\nuranium;\n**(C)**\ncopper;\n**(D)**\npotash;\n**(E)**\ngold; and\n**(F)**\nany other element or compound the Chair of the National Energy Dominance Council determines appropriate.\n**(6) Outer Continental Shelf**\nThe term outer Continental Shelf has the meaning given the term in section 2 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1331 ).\n**(7) Processing**\nThe term processing includes the concentration, separation, refinement, alloying, and conversion of minerals into usable forms.\n**(8) Prospecting**\nThe term prospecting has the meaning given the term geological and geophysical (G&G) prospecting activities in section 580.1 of title 30, Code of Federal Regulations (or a similar successor regulation).\n**(9) Seabed mineral resource**\nThe term seabed mineral resource means a mineral-bearing material located in the seabed of the outer Continental Shelf, including\u2014\n**(A)**\na polymetallic nodule;\n**(B)**\na cobalt-rich ferromanganese crust;\n**(C)**\na polymetallic sulfide;\n**(D)**\na heavy mineral sand; and\n**(E)**\na phosphorite.\n**(10) United States company**\nThe term United States company has the meaning given the term United States citizen in section 4 of the Deep Seabed Hard Mineral Resources Act ( 30 U.S.C. 1403 ).",
      "versionDate": "2025-06-17",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alliances",
            "updateDate": "2025-09-09T18:22:03Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-09-09T18:17:25Z"
          },
          {
            "name": "Metals",
            "updateDate": "2025-09-09T18:22:28Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-09-09T18:17:16Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-09-09T18:22:16Z"
          },
          {
            "name": "Seashores and lakeshores",
            "updateDate": "2025-09-09T18:17:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-07-09T13:11:24Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4018ih.xml"
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
      "title": "To unleash America's offshore critical minerals and resources.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T07:18:35Z"
    },
    {
      "title": "To unleash America's offshore critical minerals and resources.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T08:05:49Z"
    }
  ]
}
```
