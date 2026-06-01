# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1299
- Title: Housing Supply Frameworks Act
- Congress: 119
- Bill type: S
- Bill number: 1299
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-04-13T15:02:43Z
- Update date including text: 2026-04-13T15:02:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1299",
    "number": "1299",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001303",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
        "lastName": "Blunt Rochester",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Housing Supply Frameworks Act",
    "type": "S",
    "updateDate": "2026-04-13T15:02:43Z",
    "updateDateIncludingText": "2026-04-13T15:02:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
        "item": {
          "date": "2025-04-03T23:19:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "ID"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NE"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1299is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1299\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Ms. Blunt Rochester (for herself, Mr. Crapo , Mr. Fetterman , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo direct the Secretary of Housing and Urban Development, acting through the Assistant Secretary for Policy Development and Research, to publish guidelines and best practices for State zoning and local zoning frameworks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Supply Frameworks Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAs of 2022 in the United States, there was an estimated housing shortage of 3,850,000 homes. This housing supply shortage has resulted in a record number of cost-burdened households across regions and spanning the large and small cities, towns, and coastal and rural communities of the United States.\n**(2)**\nSeveral factors contribute to the undersupply of housing in the United States, particularly workforce housing, including rising costs of construction, a shortage of labor, supply chain disruptions, and a lack of reliable funding sources.\n**(3)**\nRegulatory barriers at the State and local levels, such as zoning and land use regulations, also inhibit the creation of new housing to meet local and regional housing needs.\n**(4)**\nState and local governments are proactively exploring solutions for reforming regulatory barriers, but additional resources, data, and models can help adequately address these challenges.\n**(5)**\nWhile land use regulation is the responsibility of State and local governments, there is Federal support for necessary reforms, and there is an opportunity for the Federal Government to provide support and assistance to State and local governments that wish to undertake necessary reforms in a manner that fits their communities\u2019 needs.\n**(6)**\nTherefore, zoning ordinances or systems of land use regulation that have the intent or effect of restricting housing opportunities based on economic status or income without interests that are substantial, legitimate, nondiscriminatory and that outweigh the regional need for housing are contrary to the regional and national interest.\n#### 3. Definitions\nIn this Act:\n**(1) Affordable housing**\nThe term affordable housing means housing for which the monthly payment is not more than 30 percent of the monthly income of the household.\n**(2) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary for Policy Development and Research of the Department of Housing and Urban Development.\n**(3) Local zoning framework**\nThe term local zoning framework means the local zoning codes and other ordinances, procedures, and policies governing zoning and land-use at the local level.\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(5) State zoning framework**\nThe term State zoning framework means the State legislation or State agency and department procedures, or such legislation or procedures in an insular area of the United States, enabling local planning and zoning authorities and establishing and guiding related policies and programs.\n#### 4. Guidelines on State and local zoning frameworks\n##### (a) Establishment\nNot later than 3 years after the date of enactment of this section, the Assistant Secretary shall publish documents outlining guidelines and best practices to support production of adequate housing to meet the needs of communities and provide housing opportunities for individuals at every income level across communities with respect to\u2014\n**(1)**\nState zoning frameworks; and\n**(2)**\nlocal zoning frameworks.\n##### (b) Consultation; public comment\nDuring the 2 year period beginning on the date of enactment of this Act, in developing the guidelines and best practices required under subsection (a), the Assistant Secretary shall\u2014\n**(1)**\npublish draft guidelines in the Federal Register for public comment; and\n**(2)**\nestablish a task force for the purpose of providing consultation to draft guidelines published under paragraph (1), the members of which shall include\u2014\n**(A)**\nplanners and architects;\n**(B)**\nadvocates with experience in affordable housing, community development efforts, and fair housing;\n**(C)**\nhousing developers, including affordable and market-rate housing developers, manufactured housing developers, and other business interests;\n**(D)**\ncommunity engagement experts and community members impacted by zoning decisions;\n**(E)**\npublic housing authorities and transit authorities;\n**(F)**\nmembers of local zoning and planning boards and local and regional transportation planning organizations;\n**(G)**\nState officials responsible for housing or land use, including members of State zoning boards of appeals;\n**(H)**\nacademic researchers; and\n**(I)**\nhome builders.\n##### (c) Contents\nThe guidelines and best practices required under subsection (a) shall\u2014\n**(1)**\nwith respect to State zoning frameworks, outline potential models for updated State enabling legislation or State agency and department procedures;\n**(2)**\ninclude recommendations regarding\u2014\n**(A)**\nthe reduction or elimination of parking minimums;\n**(B)**\nthe increase in maximum floor area ratio requirements and maximum building heights and the reduction in minimum lot sizes and set-back requirements;\n**(C)**\nthe elimination of restrictions against accessory dwelling units;\n**(D)**\nincreasing by-right uses, including duplex, triplex, or quadplex buildings, across cities or metropolitan areas;\n**(E)**\nmechanisms, including proximity to transit, to determine the appropriate scope for rezoning and ensure development that does not disproportionately burden residents of economically distressed areas;\n**(F)**\nprovisions regarding review of by-right development proposals to streamline review and reduce uncertainty, including\u2014\n**(i)**\nnondiscretionary, ministerial review; and\n**(ii)**\nentitlement and design review processes;\n**(G)**\nthe reduction of obstacles to a range of housing types at all levels of affordability, including manufactured and modular housing;\n**(H)**\nState model zoning regulations for directing local reforms, including mechanisms to encourage adoption;\n**(I)**\nprovisions to encourage transit-oriented development, including increased permissible units per structure and reduced minimum lot sizes near existing or planned public transit stations;\n**(J)**\npotential reforms to the public engagement process, including\u2014\n**(i)**\nmeaningful access for persons with limited English proficiency and effective communication improvements for persons with disabilities;\n**(ii)**\nleveraging of virtual meeting technologies; and\n**(iii)**\nproactive outreach in communities;\n**(K)**\nreforms to protest petition statutes;\n**(L)**\nthe standardization, reduction, or elimination of impact fees;\n**(M)**\ncost effective and appropriate building codes;\n**(N)**\nmodels for community benefit agreements;\n**(O)**\nmechanisms to preserve affordability, limit disruption of low-income communities, and prevent displacement of existing residents;\n**(P)**\nwith respect to State zoning frameworks\u2014\n**(i)**\nState model codes for directing local reforms, including mechanisms to encourage adoption;\n**(ii)**\na model for a State zoning appeals process, which would\u2014\n**(I)**\ncreate a process for developers or builders requesting a variance, conditional use, special permit, zoning district change, similar discretionary permit, or otherwise petitioning a local zoning or planning board for a project including a State-defined amount of affordable housing to appeal a rejection to a State body or regional body empowered by the State;\n**(II)**\nestablish qualifications for communities to be exempted from the appeals process based on their available stock of affordable housing; and\n**(III)**\nestablish a State zoning appeals board to consider appeals to a discretionary permit rejection and objectively evaluate petitions based on the potential for environmental damage and infrastructural capacity; and\n**(iii)**\nbest practices on the disposition of land owned by State governments for affordable housing development;\n**(Q)**\nwith respect to local zoning frameworks\u2014\n**(i)**\nthe simplification and standardization of existing zoning codes;\n**(ii)**\nmaximum review timelines;\n**(iii)**\nbest practices for the disposition of land owned by local governments for affordable housing development; and\n**(iv)**\ndifferentiations between best practices for rural, suburban, and urban communities, and communities with different levels of density or population distribution; and\n**(R)**\nother land use measures that promote access to new housing opportunities identified by the Secretary; and\n**(3)**\nconsider\u2014\n**(A)**\nconsistency with respect to fair housing and civil rights requirements;\n**(B)**\nthe effects of adopting any recommendation on eligibility for Federal discretionary grants provided by the Department of Housing and Urban Development, the Department of Transportation, and the Department of Agriculture, and tax credits for the purpose of housing or community development;\n**(C)**\ncoordination between infrastructure investments and housing planning;\n**(D)**\nlocal housing needs, including ways to set and measure housing goals and targets;\n**(E)**\na range of affordability for rental units, with a prioritization of units attainable to extremely low-income, low-income, and moderate-income residents;\n**(F)**\na range of affordability for homeownership units attainable to low-income and moderate-income residents;\n**(G)**\naccountability measures;\n**(H)**\nthe long-term cost to residents and businesses if more housing is not constructed;\n**(I)**\nbarriers to individuals seeking to access affordable housing in growing communities and communities with economic opportunity;\n**(J)**\nwith respect to State zoning frameworks\u2014\n**(i)**\ndistinctions between States providing constitutional or statutory home rule authority to municipalities and States operating under the Dillon Rule, as articulated in Hunter v. Pittsburgh, 207 U.S. 161 (1907);\n**(ii)**\nstatewide mechanisms to preserve existing affordability over the long term, including support for land banks and community land trusts; and\n**(iii)**\nguidance to States on collecting and maintaining proactive data on the current rental housing market and rental registries;\n**(K)**\npublic comments described in subsection (b)(1); and\n**(L)**\nother considerations, as identified by the Secretary.\n#### 5. Reporting\nNot later than 5 years after the date on which the Assistant Secretary publishes the guidelines and best practices for State and local zoning frameworks, the Assistant Secretary shall submit to Congress a report describing\u2014\n**(1)**\nthe States that have adopted recommendations from the guidelines and best practices, pursuant to section 4 of this Act;\n**(2)**\na summary of the localities that have adopted recommendations from the guidelines and best practices, pursuant to Section 4 of this Act;\n**(3)**\na list of States that adopted a State zoning framework;\n**(4)**\na summary of the modifications that each State has made in their State zoning framework;\n**(5)**\na general summary of the types of updates localities have made to their local zoning framework; and\n**(6)**\nof the States that have adopted a State zoning framework or recommendations from the guidelines and best practices, the effect of such adoptions on the number of building permits issued.\n#### 6. Abolishment of regulatory barriers clearinghouse\n##### (a) In general\nThe Regulatory Barriers Clearinghouse established pursuant to section 1205 of the Housing and Community Development Act of 1992 ( 42 U.S.C. 12705d ) is abolished.\n##### (b) Repeal\nSection 1205 of the Housing and Community Development Act of 1992 ( 42 U.S.C. 12705d ) is repealed.\n#### 7. Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this Act $3,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "2840",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Supply Frameworks Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-05-05T12:34:04Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1299is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-06-25T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Supply Frameworks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Housing and Urban Development, acting through the Assistant Secretary for Policy Development and Research, to publish guidelines and best practices for State zoning and local zoning frameworks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:27Z"
    }
  ]
}
```
