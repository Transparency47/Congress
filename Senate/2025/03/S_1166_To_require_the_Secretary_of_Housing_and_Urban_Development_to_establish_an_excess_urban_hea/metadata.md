# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1166?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1166
- Title: Excess Urban Heat Mitigation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1166
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2026-01-21T06:42:14Z
- Update date including text: 2026-01-21T06:42:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1166",
    "number": "1166",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Excess Urban Heat Mitigation Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T06:42:14Z",
    "updateDateIncludingText": "2026-01-21T06:42:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T15:12:45Z",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-27",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1166is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1166\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Gallego (for himself, Mr. Markey , Mr. Wyden , Mr. Merkley , Mr. Sanders , Mr. Booker , and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of Housing and Urban Development to establish an excess urban heat mitigation grant program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Excess Urban Heat Mitigation Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nHeat stress is a leading weather-related cause of death in the United States, with more than 600 people killed in the United States by extreme heat every year, and many more experiencing respiratory problems and heat-related illness.\n**(2)**\nUrban areas are likely to experience higher temperatures than surrounding areas due to design-related attributes of the built environment, including manmade factors such as low solar reflectance, low vegetation and tree cover, high building density, high impervious surface cover, and waste heat emissions.\n**(3)**\nUnderserved communities are disproportionately impacted by extreme heat. In the United States, low-income census blocks have 15.2 percent less tree cover and an average land surface temperature that is 1.5 degrees Celsius hotter than high-income blocks.\n**(4)**\nStudies show that in 97 percent of the largest urbanized areas in the United States, people of color live in census tracts with higher surface urban heat intensity than non-Hispanic Whites, indicating that heat exposure is unequally distributed by race.\n**(5)**\nUrban heat is not only a public health threat but also an economic one, as rising heat leads to increased roadway maintenance costs, higher residential and commercial summer energy costs, and lost labor productivity, as well as the cost to patients and health care infrastructure for heat-related hospitalizations and emergency department visits.\n**(6)**\nExcess urban heat causes increased energy consumption, elevated emission of air pollutants and greenhouse gases, and impaired water quality.\n**(7)**\nHeat waves are expected to not only occur more frequently in the United States but also be of longer duration, lasting 10 to 20 days longer by the end of the century.\n**(8)**\nSolutions exist that communities can implement now to mitigate the challenge of urban heat. One example is the planting of urban trees to offset or reverse the urban heat island effect. Studies in multiple cities in the United States have shown that urban trees can offset projected increases in heat-related mortality in 2050 by 40 to 99 percent.\n#### 3. Definitions\nIn this Act:\n**(1) Covered census tract**\nThe term covered census tract means a census tract with a poverty rate of not less than 20 percent, as measured by the 5-year data series available from the American Community Survey of the Bureau of the Census for the period of 2019 through 2023, including such a census tract that includes an area that was designated as hazardous or definitely declining in maps drawn by the Home Owners\u2019 Loan Corporation.\n**(2) Covered grant**\nThe term covered grant means a grant awarded under section 4(a).\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State (as defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ));\n**(B)**\na metropolitan planning organization;\n**(C)**\na unit of general local government (as defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ));\n**(D)**\nan Indian tribe (as defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ));\n**(E)**\na territorial government;\n**(F)**\na nonprofit organization working in coordination with an entity described in subparagraphs (A) through (E); and\n**(G)**\na consortium of nonprofit organizations.\n**(4) Eligible project**\nThe term eligible project \u2014\n**(A)**\nmeans a project designed to mitigate or manage heat in an urban area by\u2014\n**(i)**\nworking to mitigate the causes of higher temperatures; or\n**(ii)**\nmanaging the impacts of higher temperatures or other extreme weather events; and\n**(B)**\nincludes the implementation, construction, or maintenance of\u2014\n**(i)**\ntree planting and maintenance with, wherever possible, preference for\u2014\n**(I)**\nnative tree species;\n**(II)**\ntree species with high shade production and carbon sequestration; and\n**(III)**\ntree species that are valuable for food production;\n**(ii)**\ncool pavements;\n**(iii)**\ncool roofs;\n**(iv)**\ngreen roofs;\n**(v)**\nbus and other transit stop shelters;\n**(vi)**\nshade structures;\n**(vii)**\ncooling centers with, wherever possible, preference for\u2014\n**(I)**\ncooling centers that collaborate with existing community centers and spaces;\n**(II)**\ncooling centers with year-round accessibility, and\n**(III)**\ncooling centers that utilize renewable energy;\n**(viii)**\ncommunity gardens, including agroforestry practices;\n**(ix)**\noutreach to communities about resources available under this section;\n**(x)**\nlocal heat mitigation and management education efforts;\n**(xi)**\nurban forestry master plans;\n**(xii)**\nurban tree canopy assessments;\n**(xiii)**\narboriculture training;\n**(xiv)**\nmaintenance of existing urban trees; or\n**(xv)**\nother actions the Secretary determines appropriate to mitigate or manage excess urban heat.\n**(5) Environmental justice**\nThe term environmental justice means the fair treatment and meaningful involvement of all people regardless of race, color, culture, national origin, income, and educational levels with respect to the development, implementation, and enforcement of protective environmental laws, regulations, and policies.\n**(6) Excess urban heat effect**\nThe term excess urban heat effect means the phenomenon of local urban warming, resulting from manmade factors such as low solar reflectance, low tree cover, high building density, high impervious surface cover, and waste heat emissions.\n**(7) Extreme heat**\nThe term extreme heat means a prolonged period of excessively hot weather, with temperatures well above climatological normals for a given location and season.\n**(8) Nonprofit organization**\nThe term nonprofit organization means an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code.\n**(9) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(10) Urban area**\nThe term urban area has the meaning given the term in section 101(a) of title 23, United States Code.\n**(11) Urban forestry master plan**\nThe term urban forestry master plan means a strategic plan that establishes the overall vision, goals, objectives, and implementation tools to evaluate, maintain and expand the urban tree canopy with the intention of building resilience to extreme weather events, reducing the urban heat island effect, mitigating stormwater runoff, reducing nutrient runoff, addressing air quality, and preserving biodiversity.\n**(12) Urban tree canopy assessment**\nThe term urban tree canopy assessment means a measure of a community\u2019s tree canopy coverage as a percentage of the total land area that serves as a baseline for setting community tree canopy goals and measuring progress.\n#### 4. Urban Heat Mitigation and Management Grant Program\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary, acting through the Office of Community Planning and Development, in coordination with the Administrator of the Environmental Protection Agency, the Chief of the Forest Service, and the Director of the Climate Program Office of the National Oceanic and Atmospheric Administration, shall establish an urban heat mitigation and management grant program to award grants to eligible entities to implement eligible projects.\n##### (b) Set-Aside\nNot less than 75 percent of the amounts of covered grants awarded for a fiscal year shall be awarded to eligible entities to implement projects in a covered census tract.\n##### (c) Technical assistance\n**(1) In general**\nNot more than 3 percent of amounts appropriated to carry out this section may be used to provide technical assistance to eligible entities applying for or implementing a covered grant.\n**(2) Preference**\nIn providing technical assistance under paragraph (1), the Secretary shall give preference to eligible entities that intend to serve communities\u2014\n**(A)**\nlocated in a covered census tract; or\n**(B)**\nwith lower-tree canopy and higher maximum daytime summer temperatures compared to surrounding communities, as determined by the Secretary, based on publicly available information.\n**(3) Inclusions**\nTechnical assistance provided under paragraph (1) may include\u2014\n**(A)**\nassistance developing a complete application;\n**(B)**\nfinancial analysis and budget development;\n**(C)**\nsupport for project integration;\n**(D)**\nassessment of project readiness; and\n**(E)**\ntechnical assistance implementing activities once a covered grant is received.\n##### (d) Application\n**(1) In general**\nAn eligible entity desiring a covered grant shall submit to the Secretary an application, at such time and in such manner as required by the Secretary in guidance, that includes, at a minimum\u2014\n**(A)**\nhow the eligible entity will use the covered grant;\n**(B)**\nhow the eligible projects funded will combat extreme heat or excess urban heat effects and improve quality of life for impacted communities;\n**(C)**\na robust engagement plan that\u2014\n**(i)**\noutlines how the eligible entity will meaningfully and inclusively engage with the communities in which the eligible projects take place throughout project implementation; and\n**(ii)**\ndemonstrates how the eligible entity plans to\u2014\n**(I)**\nfoster meaningful, reciprocal relationships with community-based organizations;\n**(II)**\nengage in respectful, good-faith consultation with diverse community stakeholders; and\n**(III)**\nempower members of the community to participate in decision making; and\n**(D)**\nhow the eligible entity will address the intersection between human health, environment, and built environment.\n**(2) Guidance**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue the guidance described in paragraph (1).\n##### (e) Matching requirement\n**(1) In general**\nExcept as provided in paragraph (2), the Federal share of the cost of an eligible project carried out with amounts from a covered grant shall be not more than 80 percent.\n**(2) Waiver**\nThe Secretary may increase the maximum Federal share described in paragraph (1) from 80 percent to 100 percent for an eligible project carried out by an eligible entity that demonstrates economic hardship, as determined by the Secretary.\n##### (f) Priority\nIn awarding covered grants, the Secretary shall give priority to an eligible entity that serves\u2014\n**(1)**\na community located in a covered census tract; or\n**(2)**\na community with lower tree canopy and higher maximum daytime summer temperatures compared to surrounding communities, as determined by the Secretary, based on publicly available information.\n##### (g) Reporting requirement\nThe Secretary shall submit an annual report to Congress that identifies the recipients of covered grants and the geographic and economic distribution of those recipients.\n##### (h) Oversight\n**(1) In general**\nIn order to ensure the effectiveness of projects that are carried out using covered grants, the Secretary shall use not more than 5 percent of any amounts appropriated to carry out this section to establish an oversight board to help\u2014\n**(A)**\nselect recipients of covered grants; and\n**(B)**\nreview the progress made by recipients of covered grants on a yearly basis.\n**(2) Evaluation**\nThe board established under paragraph (1) shall\u2014\n**(A)**\ndevelop and apply a rubric to evaluate the success of projects carried out using covered grants in reaching their objective to combat the causes and effects of excess urban heat; and\n**(B)**\nserve the Secretary in an advisory capacity.\n**(3) Membership**\n**(A) In general**\nMembers of the board established under paragraph (1) may include\u2014\n**(i)**\nrepresentatives from the Environmental Protection Agency, particularly from the Heat Island Reduction Program;\n**(ii)**\nrepresentatives from the Department of Health and Human Services, particularly from the Office of Climate Change and Health Equity;\n**(iii)**\nrepresentatives from the Department of Energy, particularly from the Office of Energy Efficiency and Renewable Energy;\n**(iv)**\nrepresentatives from the Department of Agriculture, particularly from the Urban and Community Forestry Program;\n**(v)**\nsubject to subparagraph (B), representatives from nonprofit organizations with proven leadership in urban heat mitigation or environmental justice, as determined by the Secretary; and\n**(vi)**\nsubject to subparagraph (B), representatives from academia and research studying the effects of and mitigation of excess urban heat, environmental justice, or related areas.\n**(B) Certification required**\nIn order to be a member of the board established under paragraph (1), a representative described in clause (v) or (vi) of subparagraph (A) of this paragraph shall certify that the representative does not possess any conflict of interest with respect to projects being considered for a covered grant or being carried out using a covered grant.\n##### (i) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $30,000,000 for each of fiscal years 2026 through 2033.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-06-04",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "3703",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Excess Urban Heat Mitigation Act of 2025",
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
        "updateDate": "2025-04-11T12:35:05Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1166is.xml"
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
      "title": "Excess Urban Heat Mitigation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Excess Urban Heat Mitigation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Housing and Urban Development to establish an excess urban heat mitigation grant program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:21Z"
    }
  ]
}
```
