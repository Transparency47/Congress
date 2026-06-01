# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3000
- Title: Caring for Seniors Act
- Congress: 119
- Bill type: HR
- Bill number: 3000
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-24 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3000",
    "number": "3000",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Caring for Seniors Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-24T15:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3000ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3000\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Fitzpatrick (for himself and Mrs. Trahan ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo address the worsening long-term care workforce crisis and increase access to and affordability of long-term care.\n#### 1. Short title\nThis Act may be cited as the Caring for Seniors Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States population is aging more rapidly than ever before, with 10,000 Americans turning 65 each day. In 2034, for the first time, the Nation will have more people over the age of 65 than under the age of 18. The population experiencing the fastest growth are persons 85 and older, which is projected to grow 198 percent by 2060.\n**(2)**\nThe Department of Health and Human Services estimates that 70 percent of Americans over the age of 65 will require some form of long-term care in their lifetime. By 2050, the number of Americans requiring paid long-term care services will triple from 8,300,000 to 27,000,000.\n**(3)**\nAccording to 2020 Census data, more than 40 percent of baby boomers do not have any retirement savings, let alone savings for their long-term care needs. A recent report by the National Council on Aging found that up to 80 percent of older adults would be unable to afford 4 years in an assisted living community or more than 2 years of nursing home care. Put another way, 47,000,000 Americans aged 60 or above do not have the financial resources to cover the future care they may need.\n**(4)**\nCaring for America\u2019s aging seniors will be the single most expense domestic priority and is projected to deplete Federal and State Medicaid budgets. The United States spent over $400,000,000,000 on long-term care in 2020, nearly 10 percent of all national health care spending.\n**(5)**\nAccording to the Congressional Research Service, State and Federal programs account for 71.4 percent of all long-term care spending nationwide in 2021. Medicaid and Medicare are, respectively, the first and second-largest public payers, accounting for a combined 64.1 percent of all spending. Medicaid is by far the largest single funding source for long-term care, spending approximately $135,800,000,000 in 2020, a figure that is projected to reach $466,000,000,000 by 2050.\n**(6)**\nA 2023 report by AARP, indicates that at least 9 percent of seniors in skilled nursing homes nationwide have low-acuity levels that do not warrant high skilled care, but are forced into a skilled nursing home where assets can be depleted, and Medicaid can become the primary payer. The report by AARP indicated that this number is 20 percent in 5 States.\n**(7)**\nIn 2021, the Department of Veterans Affairs testified to Congress that if veterans in need of long-term care services could choose assisted living instead of a nursing home, $69,101 per veteran per year would be saved by the Department of Veterans Affairs.\n**(8)**\nStrengthening cost-effective models of long-term care services, providing incentives for Americans to better afford their care costs, and developing the workforce needed to care for the Nation\u2019s aging population will reduce Federal and State Medicaid spending.\n**(9)**\nCongregate care models of long-term care services, such as assisted living, are half the cost of nursing homes, and less than a third of round the clock home health aides.\n**(10)**\nAssisted living provides 24/7 personal care, chronic disease management, nutrition, room and board, and socialization. If assisted living were not an option, as many as 61 percent of senior residents may be forced into far-costlier skilled nursing facilities at a cost of $43,400,000,000 per year.\n**(11)**\nThe senior living industry lost approximately 400,000 jobs between 2020 and 2022, leaving the workforce far below prepandemic employment levels. In order to care for the United States aging population, the senior care industry will need to fill more than 20,200,000 jobs by 2040.\n#### 3. Addressing the long-term care workforce crisis\n##### (a) Workforce programs\n**(1) Expansion of DOL workforce programs**\nThe Secretary of Labor, acting jointly through the Assistant Secretary for Employment and Training and the National Director for the Office of Job Corps of the Employment and Training Administration, shall establish new and expand existing education and training grant programs to support the expansion of the direct care workforce for purposes of caring for a rapidly aging population and providing home and community-based services to older adults and people with disabilities. Such programs shall include support for core certification and training requirements for the direct care workforce of assisted living facilities.\n**(2) Expansion of HRSA workforce programs**\nThe Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, shall establish new and expand existing workforce education and training grant programs to address shortages in the direct care workforce serving the rapidly aging population and providing home and community-based services to older adults and people with disabilities. Such programs shall include support for core certification and training requirements for the direct care workforce of assisted living facilities.\n##### (b) Definitions\nIn this section:\n**(1) Assisted living facility**\nThe term assisted living facility means any licensed, registered, certified, listed, or State-regulated residence, managed residential community, building, or part of a building that provides, or contracts to provide, housing with supportive services on a continuing basis to individuals who\u2014\n**(A)**\nare elderly or have a mental health, developmental, or physical disability; and\n**(B)**\nare unrelated by blood or marriage to the owner or operator of the residence, community, building, or part of a building, if the owner or operator is an individual.\n**(2) Direct care workforce**\nThe term direct care workforce means a workforce that is composed of individuals who, in exchange for compensation, provide services at an assisted living facility to an individual who is elderly or who has a mental health, developmental, or physical disability, that promote such individual\u2019s independence, including\u2014\n**(A)**\nservices that enhance independence and community inclusion for such individual, including traveling with such individual, attending and assisting such individual while visiting friends and family, shopping, or socializing;\n**(B)**\nservices such as coaching and supporting such individual in communicating needs, achieving self-expression, pursuing personal goals, living independently, and participating actively in employment or voluntary roles in the community;\n**(C)**\nservices such as providing assistance with activities of daily living (such as feeding, bathing, toileting, and ambulation) and with tasks such as meal preparation, shopping, light housekeeping, and laundry; or\n**(D)**\nservices that support such individual at home, work, school, or any other community setting.\n#### 4. Senior Care Cost Reduction Program\nPart A of title III of the Older Americans Act of 1965 ( 42 U.S.C. 3021 et seq. ) is amended by adding at the end the following:\n317. Senior Care Cost Reduction Program (a) Establishment of program The Assistant Secretary, acting through the Administration, shall establish a Senior Care Cost Reduction Program for making allotments to States to administer monthly cost reduction amounts to assist low-income seniors to reside and receive services in assisted living facilities located in the State as an alternative to more costly institutional care. (b) State application In order to be eligible to receive an allotment under this section, the State shall submit an application to the Assistant Secretary at such time, in such manner, and accompanied by such information as the Assistant Secretary may reasonably require. (c) Cost reduction amount (1) Initial amount Upon establishment of the Program, the monthly amount provided by the State to eligible recipients shall be $1,000. (2) Adjustments in consumer price index Beginning one year after the establishment of the Program, and each subsequent year, the monthly amount required under paragraph (1) shall be increased by the percentage, if any, by which the Consumer Price Index for all urban consumers (all items; United States city average) for the most recent calendar year exceeds the Consumer Price Index for the previous calendar year, rounded to the nearest dollar. (d) Eligibility In order to be eligible for a cost reduction amount under this section, the individual must\u2014 (1) submit an application to and be approved by the relevant State agency tasked with administering the Program; (2) be at least 70 years old as of the date of application; (3) be accepted for admission as a resident in, or currently reside in, an assisted living facility which has been approved by the relevant State agency to participate in this Program; (4) be either a chronically ill individual (as defined in section 7702B(c)(2) of the Internal Revenue Code of 1986) or eligible to receive long-term services and supports under the relevant State\u2019s Medicaid program; and (5) be determined to be financially eligible, pursuant to subsection (e). (e) Financial eligibility An individual is financially eligible under this section only if the individual\u2019s\u2014 (1) net monthly income is less than the approved monthly fees for the services provided at the assisted living facility; (2) net annual income is not higher than 60 percent of the median income for the State in which the individual resides, as determined by the Secretary of Housing and Urban Development; and (3) resources are not greater than $19,000 if single, or $25,000 if married. (f) Implementation The Secretary, acting through the Assistant Secretary, may issue such regulations as may be necessary to carry out this section. (g) Assisted living facility defined As used in this section, the term assisted living facility means any licensed, registered, certified, listed, or State-regulated residence, managed residential community, building, or part of a building that provides, or contracts to provide, housing with supportive services on a continuing basis to individuals who\u2014 (1) are elderly or have a mental health, developmental, or physical disability; and (2) are unrelated by blood or marriage to the owner or operator of the residence, community, building, or part of a building, if the owner or operator is an individual. .\n#### 5. Authorization of appropriations\nAmounts that have been returned to or recovered by the Health Resources and Services Administration or the Department of the Treasury, including all amounts returned or recovered after the date of enactment of this Act, from amounts made available and disbursed to eligible health care providers for health care-related expenses or lost revenues attributable to coronavirus under the heading Public Health and Social Services Emergency Fund in title VIII of division B of Public Law 116\u2013136 , title I of division B of Public Law 116\u2013139 , and title III of division M of Public Law 116\u2013260 , are authorized to be appropriated to carry out this Act and the amendment made by this Act.",
      "versionDate": "2025-04-24",
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
        "name": "Health",
        "updateDate": "2025-05-28T10:28:28Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3000ih.xml"
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
      "title": "Caring for Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-24T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Caring for Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address the worsening long-term care workforce crisis and increase access to and affordability of long-term care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T10:03:15Z"
    }
  ]
}
```
