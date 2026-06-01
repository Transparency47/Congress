# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2840?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2840
- Title: Housing Supply Frameworks Act
- Congress: 119
- Bill type: HR
- Bill number: 2840
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-04-13T15:02:42Z
- Update date including text: 2026-04-13T15:02:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2840",
    "number": "2840",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Housing Supply Frameworks Act",
    "type": "HR",
    "updateDate": "2026-04-13T15:02:42Z",
    "updateDateIncludingText": "2026-04-13T15:02:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "VA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "OH"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "GU"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "PA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "TX"
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
      "sponsorshipDate": "2025-06-10",
      "state": "VA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "TX"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "NJ"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "FL"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "ID"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "KS"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "PA"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2840ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2840\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Flood (for himself and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo direct the Secretary of Housing and Urban Development, acting through the Assistant Secretary for Policy Development and Research, to publish guidelines and best practices for State zoning and local zoning frameworks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Supply Frameworks Act .\n#### 2. Findings\nCongress finds the followings:\n**(1)**\nAs of 2022 in the United States, there was an estimated housing shortage of 3,850,000 homes. This housing supply shortage has resulted in a record number of cost-burdened households across regions and spanning the large and small cities, towns, and coastal and rural communities of the United States.\n**(2)**\nSeveral factors contribute to the undersupply of housing in the United States, particularly workforce housing, including rising costs of construction, a shortage of labor, supply chain disruptions, and a lack of reliable funding sources.\n**(3)**\nRegulatory barriers at the State and local levels, such as zoning and land use regulations, also inhibit the creation of new housing to meet local and regional housing needs.\n**(4)**\nState and local governments are proactively exploring solutions for reforming regulatory barriers, but additional resources, data, and models can help adequately address these challenges.\n**(5)**\nWhile land use regulation is the responsibility of State and local governments, there is Federal support for necessary reforms, and there is an opportunity for the Federal Government to provide support and assistance to State and local governments that wish to undertake necessary reforms in a manner that fits their communities' needs.\n**(6)**\nTherefore, zoning ordinances or systems of land use regulation that have the intent or effect of restricting housing opportunities based on economic status or income without interests that are substantial, legitimate, nondiscriminatory and that outweigh the regional need for housing are contrary to the regional and national interest.\n#### 3. Definitions\nIn this Act:\n**(1) Affordable housing**\nThe term affordable housing means housing in which the occupant is paying no more than 30 percent of gross income for housing costs.\n**(2) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary for Policy Development and Research of the Department of Housing and Urban Development.\n**(3) Framework-related terms**\n**(A) Local zoning framework**\nThe term local zoning framework means the local zoning codes and other ordinances, procedures, and policies governing zoning and land-use at the local level.\n**(B) State zoning framework**\nThe term State zoning framework means the State legislation or State agency and department procedures, or such legislation or procedures in an insular area of the United States, enabling local planning and zoning authorities and establishing and guiding related policies and programs.\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n#### 4. Guidelines on State and local zoning frameworks\n##### (a) Establishment\nNot later than 3 years after the date of enactment of this section, the Assistant Secretary shall publish documents outlining guidelines and best practices to support production of adequate housing to meet the needs of communities and provide housing opportunities for individuals at every income level across communities with respect to\u2014\n**(1)**\nState zoning frameworks; and\n**(2)**\nlocal zoning frameworks.\n##### (b) Consultation; public comment\nDuring the 2 year period beginning on the date of enactment of this section, in developing the guidelines and best practices required under the previous subsection, the Assistant Secretary shall\u2014\n**(1)**\npublish draft guidelines in the Federal Register for public comment; and\n**(2)**\nestablish a task force for the purpose of providing consultation to draft guidelines published under the previous clause, the members of which shall include\u2014\n**(A)**\nplanners and architects;\n**(B)**\nadvocates with experience in affordable housing, community development efforts, and fair housing;\n**(C)**\nhousing developers, including affordable and market-rate housing developers, manufactured housing developers, and other business interests;\n**(D)**\ncommunity engagement experts and community members impacted by zoning decisions;\n**(E)**\npublic housing authorities and transit authorities;\n**(F)**\nmembers of local zoning and planning boards and local and regional transportation planning organizations;\n**(G)**\nState officials responsible for housing or land use, including members of State zoning boards of appeals;\n**(H)**\nacademic researchers; and\n**(I)**\nhome builders.\n##### (c) Contents\nThe guidelines and best practices required under subsection (a) shall\u2014\n**(1)**\nwith respect to State zoning frameworks, outline potential models for updated State enabling legislation or State agency and department procedures;\n**(2)**\ninclude recommendations regarding\u2014\n**(A)**\nthe reduction or elimination of parking minimums;\n**(B)**\nthe increase in maximum floor area ratio requirements and maximum building heights and the reduction in minimum lot sizes and set-back requirements;\n**(C)**\nthe elimination of restrictions against accessory dwelling units;\n**(D)**\nincreasing by-right uses, including duplex, triplex, or quadplex buildings, across cities or metropolitan areas, including mechanisms, such as proximity to transit, to determine the jurisdictional level for rezoning and ensures development that does not disproportionately burden residents of economically distressed areas;\n**(E)**\nreview of by-right development proposals to streamline review and reduce uncertainty, including\u2014\n**(i)**\nnondiscretionary, ministerial review; and\n**(ii)**\nentitlement and design review processes;\n**(F)**\nthe reduction of obstacles to a range of housing types at all levels of affordability, including manufactured and modular housing;\n**(G)**\nState model zoning regulations for directing local reforms, including mechanisms to encourage adoption;\n**(H)**\nprovisions to encourage transit-oriented development, including increased permissible units per structure and reduced minimum lot sizes near existing or planned public transit stations;\n**(I)**\npotential reforms to the public engagement process, including\u2014\n**(i)**\nmeaningful access for persons with limited English proficiency and effective communication improvements for persons with disabilities;\n**(ii)**\nleveraging of virtual meeting technologies; and\n**(iii)**\nproactive outreach in communities;\n**(J)**\nreforms to protest petition statutes;\n**(K)**\nthe standardization, reduction, or elimination of impact fees;\n**(L)**\ncost effective and appropriate building codes;\n**(M)**\nmodels for community benefit agreements;\n**(N)**\nmechanisms to preserve affordability, limit disruption of low-income communities, and prevent displacement of existing residents;\n**(O)**\nwith respect to State zoning frameworks, a model for a State zoning appeals process, which would\u2014\n**(i)**\ncreate a process for developers or builders requesting a variance, conditional use, or zoning district change or otherwise petitioning a local zoning or planning board for a project including a State-defined amount of affordable housing to appeal a rejection to a State body or regional body empowered by the State;\n**(ii)**\nestablish qualifications for communities to be exempted from the appeals process based on their available stock of affordable housing; and\n**(iii)**\nestablish a State zoning appeals board to consider appeals to a variance rejection and objectively evaluate petitions based on the potential for environmental damage and infrastructural capacity;\n**(P)**\nwith respect to State zoning frameworks, best practices on the disposition of land owned by State governments for affordable housing development;\n**(Q)**\nwith respect to local zoning frameworks\u2014\n**(i)**\nthe simplification and standardization of existing zoning codes;\n**(ii)**\nmaximum review timelines;\n**(iii)**\ndifferentiations between best practices for rural, suburban, and urban communities, and communities with different levels of density or population distribution; and\n**(iv)**\nbest practices for the disposition of land owned by local governments; and\n**(R)**\nother land use measures that promote access to new housing opportunities identified by the Secretary; and\n**(3)**\nconsider\u2014\n**(A)**\nlocal housing needs, including ways to set and measure housing goals and targets;\n**(B)**\na range of affordability for rental units, with a prioritization of units attainable to extremely low-income, low-income, and moderate income residents;\n**(C)**\na range of affordability for homeownership units attainable to low-income and moderate-income residents;\n**(D)**\nwith respect to State zoning frameworks, distinctions between States providing constitutional or statutory home rule authority to municipalities and States operating under the Dillon rule, as articulated in Hunter v. Pittsburgh (207 U.S. 161 (1907));\n**(E)**\naccountability measures;\n**(F)**\nthe long-term cost to residents and businesses if more housing is not constructed;\n**(G)**\nbarriers to individuals seeking to access affordable housing in growing communities and communities with economic opportunity;\n**(H)**\nconsistency with respect to fair housing and civil rights requirements;\n**(I)**\neffects of adopting any recommendations on eligibility for Federal discretionary grants under the Department of Housing and Urban Development, the Department of Transportation, and the Department of Agriculture, and tax credits for the purpose of housing or community development;\n**(J)**\ncoordination between infrastructure investments and housing planning;\n**(K)**\nwith respect to State zoning frameworks, statewide mechanisms to preserve existing affordability over the long term, including support for land banks and community land trusts;\n**(L)**\nwith respect to State zoning frameworks, guidance to States on collecting and maintaining proactive data on the current rental housing market and rental registries;\n**(M)**\npublic comments described in subsection (b)(1); and\n**(N)**\nother considerations as identified by the Secretary.\n#### 5. Reporting\nNot later than 5 years after the date on which the Assistant Secretary publishes the guidelines and best practices for State and local zoning frameworks, the Assistant Secretary shall submit to Congress a report describing\u2014\n**(1)**\nthe States that have adopted recommendations from the guidelines and best practices, pursuant to section 4 of this Act;\n**(2)**\na summary of the localities that have adopted recommendations from the guidelines and best practices, pursuant to Section 4 of this Act;\n**(3)**\na list of States that adopted a State zoning framework;\n**(4)**\na summary of the modifications that each State has made in their State zoning framework; and\n**(5)**\na general summary of the types of updates localities have made to their local zoning framework.\n#### 6. Abolishment of regulatory barriers clearinghouse\n##### (a) In general\nThe Regulatory Barriers Clearinghouse established pursuant to section 1205 of the Housing and Community Development Act of 1992 ( 42 U.S.C. 12705d ) is abolished.\n##### (b) Repeal\nSection 1205 of the Housing and Community Development Act of 1992 ( 42 U.S.C. 12705d ) is repealed.\n#### 7. Authorization of Appropriations\nThere is authorized to be appropriated to the Secretary of Housing and Urban Development to carry out this Act $3,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1299",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Supply Frameworks Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-05-19T15:02:44Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2840ih.xml"
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
      "title": "Housing Supply Frameworks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Supply Frameworks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-26T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Housing and Urban Development, acting through the Assistant Secretary for Policy Development and Research, to publish guidelines and best practices for State zoning and local zoning frameworks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-26T03:48:21Z"
    }
  ]
}
```
