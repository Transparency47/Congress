# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3923?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3923
- Title: Wildfire Coordination Act
- Congress: 119
- Bill type: HR
- Bill number: 3923
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-11-26T09:05:51Z
- Update date including text: 2025-11-26T09:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-11 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-11 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3923",
    "number": "3923",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Wildfire Coordination Act",
    "type": "HR",
    "updateDate": "2025-11-26T09:05:51Z",
    "updateDateIncludingText": "2025-11-26T09:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:03:45Z",
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
          "date": "2025-06-11T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "UT"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3923ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3923\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Neguse (for himself and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of the Interior to establish the Wildfire Science and Technology Advisory Board, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Coordination Act .\n#### 2. Wildfire Science and Technology Advisory Board\n##### (a) Establishment\nThe Secretary of the Interior shall establish a permanent advisory committee to be known as the Wildfire Science and Technology Advisory Board (in this section referred to as the Board ).\n##### (b) Duties\nThe Board shall\u2014\n**(1)**\ncoordinate the operationalization within the Federal Government of wildfire research, including by\u2014\n**(A)**\nidentifying avenues for translating wildfire research into practical applications;\n**(B)**\nestablishing criteria and frameworks to prioritize wildfire research projects for operationalization;\n**(C)**\nfacilitating the transition of prioritized wildfire research into operational projects;\n**(D)**\nconnecting and supporting entities in wildfire research and operations;\n**(E)**\nproviding feedback to refine and enhance wildfire research outputs for practical application; and\n**(F)**\npartnering, as the Board determines appropriate, with private sector and federally-funded research centers to further the work of the Board;\n**(2)**\nencourage wildfire researchers and Federal agencies undertaking wildfire operations to include\u2014\n**(A)**\nrelevant disciplines, such as public health, meteorological science, and predictive modeling; and\n**(B)**\nconsideration of built and natural fire-prone environments; and\n**(3)**\ndisseminate information, including by\u2014\n**(A)**\nestablishing mechanisms, such as newsletters and publications, online portals, webinars, and workshops, to disseminate wildfire research findings, operational best practices, and resources to relevant stakeholders and practitioners; and\n**(B)**\npromoting activities of the Board to ensure visibility and accessibility to stakeholders.\n##### (c) Membership\n**(1) Number and appointment**\nThe Board shall be composed of the following members:\n**(A)**\nThe Secretary of the Interior (or the designee thereof).\n**(B)**\nThe Secretary of Agriculture (or the designee thereof).\n**(C)**\nThe Secretary of Commerce (or the designee thereof).\n**(D)**\nThe Chief of the Forest Service (or the designee thereof).\n**(E)**\nThe Director of the Bureau of Indian Affairs (or the designee thereof).\n**(F)**\nThe Director of the Bureau of Land Management (or the designee thereof).\n**(G)**\nThe Administrator of the Federal Emergency Management Agency (or the designee thereof, except that such designee may not be the member of the Board serving pursuant to subparagraph (H)).\n**(H)**\nThe United States Fire Administrator (or the designee thereof).\n**(I)**\nThe Director of the United States Fish and Wildlife Service (or the designee thereof).\n**(J)**\nThe Administrator of the National Oceanic and Atmospheric Administration (or the designee thereof).\n**(K)**\nThe Director of the National Park Service (or the designee thereof).\n**(L)**\nThe Director of the National Institute of Standards and Technology (or the designee thereof).\n**(M)**\nThe Director of the U.S. Geological Survey (or the designee thereof).\n**(N)**\nThe Director of the Office of Science and Technology Policy (or the designee thereof).\n**(O)**\nThe Director of the National Science Foundation (or designee thereof).\n**(P)**\nThe Administrator of the National Aeronautics and Space Administration (or designee thereof).\n**(Q)**\nThe Director of the Centers for Disease Control and Prevention (or designee thereof).\n**(R)**\nThe Administrator of the Environmental Protection Agency (or designee thereof).\n**(S)**\nNot more than 18 non-Federal members, to be appointed by the Secretary of the Interior, as follows:\n**(i)**\nAt least 1 representative from each of the following:\n**(I)**\nState government.\n**(II)**\nLocal government.\n**(III)**\nTribal government.\n**(ii)**\nRepresentatives of fire departments.\n**(iii)**\nRepresentatives of relevant private-sector entities, such as codes and standards-setting organizations, prescribed fire associations, and entities with expertise in wildfire science and wildfire risk identification, transfer, and mitigation.\n**(iv)**\nWildfire, forest health, or ecological restoration researchers.\n**(v)**\nPublic health experts.\n**(vi)**\nMeteorological scientists.\n**(vii)**\nPredictive modeling experts.\n**(viii)**\nSuch other members as the Secretary of the Interior deems appropriate.\n**(2) Terms**\n**(A) In general**\nEach member of the Board serving pursuant to paragraph (1)(S) shall be appointed for a term of 2 years.\n**(B) Vacancies**\nA vacancy on the Board shall be filled in the manner in which the original appointment was made.\n**(3) Pay and expenses**\n**(A) Prohibition on compensation**\nA member of the Board shall serve without compensation.\n**(B) Travel expenses**\nEach member of the Board shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code.\n**(4) Chairperson**\n**(A) In general**\nExcept as provided in subparagraph (B), the Chairperson shall rotate annually among the members of the Board serving pursuant to subparagraphs (A), (B), and (C) of paragraph (1), beginning with the member serving pursuant to paragraph (1)(A), followed by the member serving pursuant to paragraph (1)(B).\n**(B) Exception**\nFor any term, the members of the Board may designate a member of the Board to serve as the Chairperson of the Board in lieu of the official (or the designee thereof) who would otherwise serve as the Chairperson pursuant to subparagraph (A).\n**(5) Staff; temporary and intermittent services**\n**(A) Staff**\nThe Board may appoint personnel as it considers appropriate.\n**(B) Pay**\nThe Chairperson of the Board may fix the compensation of the personnel appointed under subparagraph (A) without regard to the provisions of chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to classification of positions and General Schedule pay rates, except that the rate of pay for such personnel may not exceed the annual rate of basic pay prescribed for level V of the Executive Schedule under section 5316 of such title.\n**(C) Detail of Federal employees**\nThe head of any Federal department or agency may detail any of the personnel of that department or agency to the Board. A detail under the preceding sentence shall be without reimbursement and without interruption or loss of civil service status or privilege.\n**(D) Procurement of temporary and intermittent services**\nThe Chairperson of the Board may procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals that do not exceed the daily equivalent of the annual rate of basic pay prescribed for level V of the Executive Schedule under section 5316 of that title.\n##### (d) Report\n**(1) In general**\nNot later than the date that is 2 years after the date of enactment of this Act, the Board shall submit a report to the relevant congressional committees, which shall\u2014\n**(A)**\ndetail the activities of the Board;\n**(B)**\ndiscuss progress on transitioning wildfire research into operations within the Federal Government;\n**(C)**\ndiscuss barriers to successfully transitioning wildfire research into operations within the Federal Government; and\n**(D)**\nprovide recommendations on future wildfire research priorities and operational needs.\n**(2) Relevant congressional committees**\nIn this subsection, the term relevant congressional committees means\u2014\n**(A)**\nthe Committees on Agriculture; Natural Resources; Science, Space, and Technology; and Transportation and Infrastructure of the House of Representatives; and\n**(B)**\nthe Committees on Agriculture, Nutrition, and Forestry; Commerce, Science, and Transportation; Energy and Natural Resources; Environment and Public Works; and Homeland Security and Governmental Affairs of the Senate.\n##### (e) Termination\nSection 1013(a)(2) of title 5, United States Code, shall not apply to the Board.\n##### (f) Funding\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated $10,000,000 to carry out this section, to remain available until expended.\n**(2) Additional funding**\nIn addition to the amounts made available pursuant to paragraph (1), the Federal members of the Board may, for purposes of carrying out this section, use amounts whose purpose is not otherwise specified by the appropriations laws available to the employing agencies of such members.",
      "versionDate": "2025-06-11",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-07-01T13:07:25Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3923ih.xml"
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
      "title": "Wildfire Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to establish the Wildfire Science and Technology Advisory Board, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T05:33:22Z"
    }
  ]
}
```
