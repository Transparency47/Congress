# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5650?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5650
- Title: Weatherization Resilience and Adaptation Program Act
- Congress: 119
- Bill type: HR
- Bill number: 5650
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-02-25T09:06:31Z
- Update date including text: 2026-02-25T09:06:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5650",
    "number": "5650",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Weatherization Resilience and Adaptation Program Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:31Z",
    "updateDateIncludingText": "2026-02-25T09:06:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-30T16:07:05Z",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "LA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MI"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5650ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5650\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Mullin (for himself, Mr. Carter of Louisiana , Mr. Doggett , Mr. Huffman , Ms. Kamlager-Dove , Ms. Norton , Mr. Panetta , Mr. Peters , Ms. Tlaib , and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of the Interior to establish a grant program to assist primarily low-income individuals in making their homes and property more resilient to the impacts of climate change, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Weatherization Resilience and Adaptation Program Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nHuman accelerated climate change is causing significant shifts in global surface and atmospheric temperatures, accelerating the frequency of extreme weather events around the globe.\n**(2)**\nExtreme weather events create environmental hazards such as excessive flooding, fire, heat, wind, and drought that have catastrophic impacts on frontline communities, who experience the worst and most immediate impacts of our climate crisis and often bear the brunt of such events seasonally, creating a cyclical pattern of disruption and destruction.\n**(3)**\nIndividuals can take steps to prevent and mitigate the worst impacts of extreme weather events on their home and property by implementing resilience and adaptation best practices, but the cost of these solutions puts them out of reach for many households.\n**(4)**\nLow-income homeowners and individuals who reside in affordable housing disproportionately live in areas that face the greatest threat from extreme weather events, yet can least afford the changes to their property to make them more resilient to disasters and adapted to the changing climate.\n#### 3. Definitions\nIn this Act, the following definitions apply:\n**(1) Climate change**\nThe term climate change means long-term shifts in temperatures and weather patterns.\n**(2) Climate-driven hazards**\nThe term climate-driven hazards means hazards, such as floods, wildfires, landslides, extreme heat, extreme wind, and atmospheric rivers that have a human, economic, and ecological impact with increased frequency.\n**(3) Director**\nThe term Director means the Director of National Institute of Standards and Technology.\n**(4) Eligible program participant**\nThe term eligible program participant means\u2014\n**(A)**\na State;\n**(B)**\na federally recognized Indian Tribe; and\n**(C)**\na Native Hawaiian organization.\n**(5) Eligible property owners**\nThe term eligible property owner means\u2014\n**(A)**\na low-income property owner;\n**(B)**\nan owner of a property of which the deed, ground lease, or a loan for the improvement thereof has a restriction or covenant related to housing affordability which will not expire for at least 5 years following the receipt of funds awarded under this Act;\n**(C)**\nan owner of a multifamily dwelling building where more than 50 percent of dwelling units are occupied by residents whose rent is subsidized under a covered housing program listed in section 41411(a)(3) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12491(a)(3) ); and\n**(D)**\nan owner of a property used as a community of manufactured homes.\n**(6) Low-income**\nThe term low-income means income in relation to family size that is at or below 300 percent of the poverty level determined in accordance with criteria established by the Director of the Office of Management and Budget, except that the Secretary may allow an eligible program participant to use a higher level if, after receiving a justification from such eligible program participant, the Secretary determines that such a higher level is necessary to carry out the purposes of this part and is consistent with the eligibility criteria established in this Act.\n**(7) Manufactured home**\nThe term manufactured home has the meaning given that term under section 603(6) of the Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402(6) ).\n**(8) Natural solutions**\nThe term natural solutions means ways of adapting or making property more resilient to climate-driven hazards by making changes that imitate naturally occurring ecological functions that mitigate such hazards.\n**(9) Resilience and adaptation standards**\nThe term resilience and adaptation standards means a set of building, landscaping, and construction guidelines for how property owners may preemptively mitigate the impacts of extreme precipitation, flooding, wildfires, heat, and other hazards attributable to global climate change in their dwellings and surrounding non-dwelling property.\n**(10) Secretary**\nThe term Secretary refers to the Secretary of the Interior.\n**(11) State**\nThe term State means\u2014\n**(A)**\na State;\n**(B)**\nthe District of Columbia; and\n**(C)**\nany territory or possession of the United States.\n#### 4. Grant program\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall establish a grant program to award grants to eligible program participants to assist eligible property owners with dwelling and property adaptations to increase their ability to withstand climate-driven hazards.\n##### (b) Application\nEligible program participants applying for a grant under this section shall\u2014\n**(1)**\nsubmit to the Secretary an application\u2014\n**(A)**\nat such time and in such manner as the Secretary determines appropriate; and\n**(B)**\ncontaining a description of\u2014\n**(i)**\nthe eligible activities to be undertaken with the grant funds;\n**(ii)**\nhow eligible program participants will prioritize eligible property owners in awarding funding based on factors that take into account varying levels of disaster risk and means;\n**(iii)**\nhow eligible property owners awarded funding will be required to report on their use of funds; and\n**(iv)**\nother information, as the Secretary determines appropriate; and\n**(2)**\nif awarded funding under this Act, accept and process applications for funding from eligible property owners using an online system accessible on a smartphone or personal electronic device in addition to accepting and processing applications through a paper format.\n##### (c) Use of funds\n**(1) Eligible program participants**\nEligible program participants\u2014\n**(A)**\nshall use funds awarded under this Act to award grants to eligible property owners for resilience and adaptation activities to mitigate the impacts of climate change, including related modifications needed to maintain the existing accessibility of a property to individuals with disabilities, as the Secretary may determine after the consultation prescribed under section 5(a);\n**(B)**\nshall be required to conduct outreach to educate eligible property owners, regardless of whether such property owners have received funds awarded under this Act, about how they can make structural improvements to their homes and property;\n**(C)**\nmay use up to 15 percent of funds awarded under this Act for expenses related to administering such funds and for the outreach required under subparagraph (B);\n**(D)**\nshall not add additional eligibility requirements that materially change who is eligible for funding under this Act or add procedural burdens that limit property owners from applying for, and receiving, funding according to rules promulgated under section 5 of this Act;\n**(E)**\nshall only award grants for activities related to buildings, assets, or land located in areas where climate-driven hazards are more likely to occur as a result of climate change; and\n**(F)**\nwhen awarding grants to the owner of a multifamily building\u2014\n**(i)**\nmay require financial participation from such owner as a condition of awarding a grant for an activity with respect to that multifamily building;\n**(ii)**\nin the case of projects funded under this Act that involve the displacement of a resident from any occupied housing unit, shall only award a grant on the condition that such owner\u2014\n**(I)**\nprovides, at the option of the resident, a suitable and habitable housing unit that is, with respect to the housing unit from which the resident is displaced\u2014\n**(aa)**\nof a comparable size;\n**(bb)**\nlocated in the same local community or a community with reduced hazard risk; and\n**(cc)**\noffered under similar costs, conditions, and terms; and\n**(II)**\nensures that resident displaced are provided with the ability to return to their former unit, or a comparable unit located in the same multifamily dwelling following the completion of the grant-funded project; and\n**(iii)**\nshall only award a grant on the condition that such owner refrains from\u2014\n**(I)**\nraising rent on dwelling units in such multifamily building as a result of any improvements paid for by funding awarded under this Act; and\n**(II)**\nincreasing rent on such dwelling units for any reason for at least 2 years unless specific rent increases during those 2 years were stipulated in agreements made prior to the awarding of funding under this Act to which such owner is a party.\n**(2) Eligible property owners**\nEligible property owners shall use funds awarded under this Act to\u2014\n**(A)**\nmake changes to existing buildings or other assets as necessary to meet the purpose of the program established under this section; and\n**(B)**\nimplement natural solutions to adapt land to changing conditions.\n#### 5. Rulemaking\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall promulgate rules to carry out this Act in consultation with\u2014\n**(1)**\nthe Secretary of Housing and Urban Development;\n**(2)**\nthe Secretary of Health and Human Services;\n**(3)**\nthe Administrator of the Environmental Protection Agency;\n**(4)**\nthe Administrator of the Federal Emergency Management Agency; and\n**(5)**\nthe heads of such other Federal departments and agencies as the Secretary determines appropriate.\n##### (b) Required provisions\nThe Secretary shall ensure that regulations promulgated pursuant to this section include provisions that\u2014\n**(1)**\nin coordination with the Director, prescribe resilience and adaptation standards;\n**(2)**\nprovide guidance to eligible program participants in the implementation of this Act;\n**(3)**\ncreate audits and annual reporting requirements as may be necessary or appropriate to determine whether an eligible program participant has carried out activities using grant funds\u2014\n**(A)**\nin a timely and effective manner; and\n**(B)**\nin accordance with the requirements of this Act and other applicable laws; and\n**(4)**\ndevelop and make publicly available performance targets for public review, which shall include spending thresholds for each year from the date on which funds are obligated by the Secretary to the grantee until such time all funds have been expended.\n#### 6. Standards\n##### (a) Publication\nNot later than 1 year after the date of the enactment of this Act, the Director shall develop and publish on the National Institute of Standards and Technology website resilience and adaptation standards, after consultation with\u2014\n**(1)**\nrelevant Federal departments and agencies as the Director determines appropriate; and\n**(2)**\nprivate sector organizations as the Director determines appropriate.\n##### (b) Requirements\nThe resilience and adaptation standards published under this section shall take into consideration\u2014\n**(1)**\nthe cost of building materials;\n**(2)**\nfair labor standards;\n**(3)**\nvariation in impacts of climate change, geographical and topographical location, and pre-existing weatherization projects; and\n**(4)**\nnatural solutions.\n#### 7. Authorization of appropriations\nThere is authorized to be appropriated to carry out this Act\u2014\n**(1)**\nto the Secretary, $250,000,000 for each of fiscal years 2026 through 2031; and\n**(2)**\nto the Director, $2,000,000 for each of fiscal years 2026 through 2028.",
      "versionDate": "2025-09-30",
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-15T19:38:32Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5650ih.xml"
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
      "title": "Weatherization Resilience and Adaptation Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Weatherization Resilience and Adaptation Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to establish a grant program to assist primarily low-income individuals in making their homes and property more resilient to the impacts of climate change, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:30Z"
    }
  ]
}
```
