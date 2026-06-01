# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3792
- Title: Water Project Navigators Act
- Congress: 119
- Bill type: S
- Bill number: 3792
- Origin chamber: Senate
- Introduced date: 2026-02-05
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in Senate
- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-02-05: Introduced in Senate

## Actions

- 2026-02-05 - IntroReferral: Introduced in Senate
- 2026-02-05 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3792",
    "number": "3792",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Water Project Navigators Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T18:56:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:34Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3792is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3792\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2026 Mr. Hickenlooper (for himself and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide for the establishment of a Water Project Navigators Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Project Navigators Act .\n#### 2. Definitions\nIn this Act:\n**(1) Disadvantaged community**\nExcept as otherwise defined by the Secretary of the Interior based on current methodologies, the term disadvantaged community means a community (including a city, town, county, or reasonably isolated and divisible segment of a larger municipality) with an annual median income that is less than the statewide annual median income for the State in which the community is located, according to the most recent decennial census.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State;\n**(B)**\nan Indian Tribe;\n**(C)**\nany acequia, land grant-merced, local government, water supplier, special district, conservation district, or municipal water district located in an eligible State;\n**(D)**\nany State, regional, or local authority located in an eligible State, the members of which include 1 or more organizations with water or power delivery authority;\n**(E)**\na nonprofit conservation organization with a demonstrated history of working in partnership with 1 or more entities described in any of subparagraphs (A) through (D); or\n**(F)**\na combination of entities described in subparagraphs (A) through (E).\n**(3) Eligible State**\nThe term eligible State means\u2014\n**(A)**\na State or territory described in the first section of the Act of June 17, 1902 ( 43 U.S.C. 391 ; 32 Stat. 388, chapter 1093);\n**(B)**\nthe State of Alaska;\n**(C)**\nthe State of Hawaii; and\n**(D)**\nthe Commonwealth of Puerto Rico.\n**(4) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(5) Multi-benefit water project**\nThe term multi-benefit water project means any project in an eligible State that\u2014\n**(A)**\nenhances the overall resilience of a community or region to climate-related impacts on water supplies, including through activities\u2014\n**(i)**\nto increase water use efficiency;\n**(ii)**\nto reduce consumptive use of water;\n**(iii)**\nto promote system conservation;\n**(iv)**\nto reduce water supply-demand imbalances;\n**(v)**\nto promote water recycling and other advanced water treatments to augment water supplies;\n**(vi)**\nto improve management or delivery of water resources;\n**(vii)**\nto address risks to water infrastructure from weather-related events and climate change;\n**(viii)**\nto provide or improve access to safe drinking water in communities that lack reliable access to adequate clean water supplies;\n**(ix)**\nto promote investment in the economies of rural communities, Tribal communities, or disadvantaged communities through water projects;\n**(x)**\nto enhance water-based recreational opportunities for the benefit of community members and the local recreational economy; or\n**(xi)**\nto encourage sustainable surface water or groundwater management; and\n**(B)**\nprovides benefits to ecosystems and watersheds, including through activities\u2014\n**(i)**\nto conserve or enhance fish and wildlife habitat;\n**(ii)**\nto protect or improve water quality;\n**(iii)**\nto improve watershed health and function;\n**(iv)**\nto protect against invasive species;\n**(v)**\nto restore aspects of the natural ecosystem; or\n**(vi)**\nto maintain sustainable groundwater supplies for multiple uses, including for riparian or wetland ecosystems.\n**(6) Natural feature**\nThe term natural feature means a feature that is created through the action of physical, geological, biological, and chemical processes over time.\n**(7) Nature-based feature**\nThe term nature-based feature means a feature that is created by human design, engineering, and construction to provide a means to reduce water supply and demand imbalances or drought or flood risk by acting in concert with natural processes.\n**(8) Program**\nThe term Program means the Water Project Navigators Program established under section 3(a).\n**(9) Rural community**\nThe term rural community means a community or group of communities, each of which has a population of not more than 50,000 inhabitants, which may include Indian Tribes, Tribal organizations, dispersed homesites, and rural areas.\n**(10) Secretary**\nThe term Secretary means the Secretary of the Interior (acting through the Commissioner of Reclamation).\n#### 3. Water Project Navigators Program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a program to support the development and implementation of multi-benefit water projects within eligible States, to be known as the Water Project Navigators Program .\n##### (b) Authority\nIn carrying out the Program, the Secretary may award grants or cooperative agreements to eligible entities to support the creation or continuation of multi-benefit water project navigator positions.\n##### (c) Criteria and guidelines; priority\n**(1) Criteria and guidelines**\n**(A) In general**\nThe Secretary shall develop criteria and guidelines for awarding grants and cooperative agreements under the Program that consider\u2014\n**(i)**\nthe potential of the eligible entity to accelerate development and implementation of multi-benefit water projects within\u2014\n**(I)**\nthe jurisdiction or service area of the eligible entity; or\n**(II)**\nin the case of an eligible entity that is a nongovernmental applicant, an area in which the eligible entity has a demonstrated history of productive engagement with the community and stakeholders;\n**(ii)**\nany history of development of multi-benefit water projects by the eligible entity; and\n**(iii)**\nany potential multi-benefit water projects identified to meet needs in the area to be served by the multi-benefit water project navigator that the eligible entity has not yet implemented due to lack of capacity.\n**(B) Public comment**\nBefore finalizing the criteria and guidelines developed under subparagraph (A), the Secretary shall make the criteria and guidelines available for public comment.\n**(2) Priority**\nIn awarding grants or cooperative agreements under the Program, the Secretary shall prioritize applications from eligible entities that would directly serve Indian Tribes, disadvantaged communities, rural communities, and other eligible entities with limited resources and capacity to develop multi-benefit water projects, including\u2014\n**(A)**\napplications from eligible entities\u2014\n**(i)**\nwith a demonstrated intent and ability to incorporate improvements to the condition of a natural feature or nature-based feature in multi-benefit water projects designed under the Program;\n**(ii)**\nwith demonstrated support from multiple stakeholders, including Indian Tribes, representatives of irrigated agricultural production, hydroelectric production, municipal and industrial water users, local governments, community-based organizations, and nonprofit conservation organizations;\n**(iii)**\nthat may promote job creation and retention in Tribal communities, disadvantaged communities, and rural communities; and\n**(iv)**\nwith the capability to work in coordination with other projects that have been funded under, or help advance the objectives of, other Department of the Interior programs, including programs focused on drought resilience and watershed health; and\n**(B)**\napplications that address any other priorities that the Secretary determines to be appropriate.\n**(3) Prohibition**\nThe Secretary may not award a grant or cooperative agreement under the Program that would fund activities to meet existing environmental mitigation or compliance obligations under Federal or State law.\n##### (d) Duties of navigators\nA multi-benefit water project navigator funded under the Program shall assist the eligible entity in planning, developing, and implementing multi-benefit water projects, including\u2014\n**(1)**\ngrant writing;\n**(2)**\nproject management;\n**(3)**\ntechnical assistance, such as feasibility, design, preliminary environmental review, and engineering; and\n**(4)**\nany other necessary activities.\n##### (e) Duration of grants and cooperative agreements\n**(1) Limitation**\nSubject to paragraph (2), a grant or cooperative agreement under the Program shall be limited to a period of not more than 3 years.\n**(2) Continuation and extension**\nAt the discretion of the Secretary, the Secretary may issue a continuation grant or extend a cooperative agreement awarded under the Program for not more than 2 additional years, with additional funding to be awarded, as determined to be appropriate by the Secretary, if the recipient of the grant or cooperative agreement has demonstrated satisfactory performance with implementation of the proposal under the initial grant or cooperative agreement, as determined by the Secretary.\n##### (f) Continuous enrollment\nThe Secretary shall make funding opportunities for the Program available on a regular basis.\n##### (g) Cost share\n**(1) In general**\nExcept as provided in paragraph (3), the Federal share of the cost of any activity awarded a grant or cooperative agreement under the Program shall not exceed 75 percent of the cost of the activity carried out under the grant or cooperative agreement.\n**(2) Form of non-Federal cost share**\nThe non-Federal share of the cost of an activity awarded a grant or cooperative agreement under the Program may be in the form of cash or in-kind contributions.\n**(3) Reduction; waiver**\nWith respect to a grant or cooperative agreement awarded to an Indian Tribe, acequia, land grant-merced, disadvantaged community, or any other eligible entity working in partnership with or on behalf of those entities, the Secretary may reduce or waive the non-Federal share of the cost of any activity that is the subject of the grant or cooperative agreement if the Secretary determines that contribution of the non-Federal share would result in a financial hardship for the entity.\n##### (h) Coordination\nIn administering the Program, the Secretary shall coordinate, to the maximum extent practicable, with other Federal, Tribal, State, and local government technical assistance programs to enhance multi-benefit water project development.\n##### (i) Compliance\nA multi-benefit water project navigator funded under the Program shall comply with all applicable Federal and State laws in carrying out the duties of the multi-benefit water project navigator under the Program.\n##### (j) Report to Congress\nNot later than 5 years after the date of enactment of this Act, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives a report that describes\u2014\n**(1)**\nthe ways in which the Program assists the Secretary in\u2014\n**(A)**\nreducing basin-wide or aquifer-wide water supply-demand imbalances;\n**(B)**\nenhancing drought and ecosystem resilience; and\n**(C)**\nsupporting multi-benefit water project development and capacity building by disadvantaged communities, Indian Tribes, rural communities, and other eligible entities; and\n**(2)**\nthe benefits that the Program provides, including, to the maximum extent practicable, a quantitative analysis of the multiple benefits advanced under the Program.\n#### 4. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act $15,000,000 for each of fiscal years 2027 through 2032, to remain available until expended.",
      "versionDate": "2026-02-05",
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
        "actionDate": "2026-02-05",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "7408",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Water Project Navigators Act",
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
        "name": "Water Resources Development",
        "updateDate": "2026-02-27T21:33:46Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3792is.xml"
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
      "title": "Water Project Navigators Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Water Project Navigators Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the establishment of a Water Project Navigators Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:25Z"
    }
  ]
}
```
