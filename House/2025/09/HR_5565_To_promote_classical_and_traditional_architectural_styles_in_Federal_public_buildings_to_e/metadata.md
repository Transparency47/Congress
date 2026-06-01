# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5565?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5565
- Title: Make Federal Architecture Beautiful Again Act
- Congress: 119
- Bill type: HR
- Bill number: 5565
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-12-02T20:09:02Z
- Update date including text: 2025-12-02T20:09:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5565",
    "number": "5565",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Make Federal Architecture Beautiful Again Act",
    "type": "HR",
    "updateDate": "2025-12-02T20:09:02Z",
    "updateDateIncludingText": "2025-12-02T20:09:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:21:32Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5565ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5565\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Burchett introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo promote classical and traditional architectural styles in Federal public buildings to enhance civic pride, reflect national heritage, and ensure aesthetic excellence in government infrastructure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Make Federal Architecture Beautiful Again Act .\n#### 2. Definitions\nIn this Act:\n**(1) 2025 dollars**\nThe term 2025 dollars means dollars adjusted for inflation using the Bureau of Economic Analysis\u2019s Gross Domestic Product price deflator and using 2025 as the base year.\n**(2) Administration**\nThe term Administration means the General Services Administration.\n**(3) Administrator**\nThe term Administrator means the Administrator of General Services.\n**(4) Applicable Federal public building**\nThe term applicable Federal public building means\u2014\n**(A)**\nall Federal courthouse and agency headquarters;\n**(B)**\nall Federal public buildings in the National Capital Region; and\n**(C)**\nall other Federal public buildings that cost or are expected to cost more than 50,000,000 in 2025 dollars to design, build, and finish, but does not include infrastructure projects or land ports of entry.\n**(5) Brutalist architecture**\nThe term Brutalist architecture means the style of architecture that grew out of the early 20th-century modernist movement that is characterized by a massive and block-like appearance with a rigid geometric style and large-scale use of exposed poured concrete.\n**(6) Classical architecture**\n**(A) In general**\nThe term classical architecture means the architectural tradition\u2014\n**(i)**\nderived from the forms, principles, and vocabulary of the architecture of Greek and Roman antiquity; and\n**(ii)**\nlater developed and expanded on by\u2014\n**(I)**\nRenaissance architects, including Alberti, Brunelleschi, Michelangelo, and Palladio;\n**(II)**\nEnlightenment masters, including Robert Adam, John Soane, and Christopher Wren;\n**(III)**\n19th Century architects, including Benjamin Henry Latrobe, Robert Mills, and Thomas U. Walter; and\n**(IV)**\n20th Century practitioners, including Julian Abele, Daniel Burnham, Rafael Carmoega, Charles F. McKim, John Russell Pope, Julia Morgan, and the firm of Delano and Aldrich.\n**(B) Inclusions**\nThe term classical architecture encompasses styles such as Neoclassical, Georgian, Federal, Greek Revival, Beaux-Arts, and Art Deco.\n**(7) Deconstructivist architecture**\nThe term Deconstructivist architecture means the style of architecture\u2014\n**(A)**\ngenerally known as deconstructivism ; and\n**(B)**\nthat emerged during the late 1980s that features fragmentation, disorder, discontinuity, distortion, skewed geometry, and the appearance of instability.\n**(8) General public**\nThe term general public means members of the public who are not\u2014\n**(A)**\nartists, architects, engineers, art or architecture critics, instructors or professors of art or architecture, or members of the building industry; or\n**(B)**\naffiliated with any interest group, trade association, or any other organization whose membership is financially affected by decisions involving the design, construction, or remodeling of public buildings.\n**(9) Preferred architecture**\nThe term preferred architecture means the architecture described in section 3(3).\n**(10) Public building**\nThe term public building has the meaning given such term in section 3301(a) of title 40, United States Code.\n**(11) Traditional architecture**\nThe term traditional architecture means\u2014\n**(A)**\nclassical architecture; and\n**(B)**\nthe historic humanistic architecture, including\u2014\n**(i)**\nGothic;\n**(ii)**\nRomanesque;\n**(iii)**\nSecond Empire;\n**(iv)**\nPueblo Revival;\n**(v)**\nSpanish Colonial; and\n**(vi)**\nother Mediterranean styles of architecture historically rooted in various regions of America.\n#### 3. Policy of the United States\nIt is the policy of the United States that\u2014\n**(1)**\napplicable Federal public buildings should\u2014\n**(A)**\nuplift and beautify public spaces;\n**(B)**\ninspire the human spirit;\n**(C)**\nennoble the United States;\n**(D)**\ncommand respect from the general public;\n**(E)**\nbe visually identifiable as civic buildings; and\n**(F)**\nas appropriate, respect regional architectural heritage;\n**(2)**\nbuilding designs should be selected with substantial input from the local community;\n**(3)**\narchitecture, particularly traditional and classical architecture, that meets the criteria described in paragraph (1), is the preferred architecture for applicable Federal public buildings;\n**(4)**\nin the District of Columbia, classical architecture shall be the preferred and default architecture for Federal public buildings absent exceptional factors necessitating another kind of architecture;\n**(5)**\nwhere the architecture of applicable Federal public buildings diverges from the preferred architecture set forth in paragraph (1), great care and consideration must be taken to choose a design that\u2014\n**(A)**\ncommands respect from the general public; and\n**(B)**\nclearly conveys to the general public the dignity, enterprise, vigor, and stability America\u2019s system of self-government;\n**(6)**\nwhen renovating, reducing, or expanding applicable Federal public buildings that do not meet the criteria described in paragraph (1), the feasibility and potential expense of building redesign to meet those criteria should be examined; and\n**(7)**\nwhere feasible and economical, such redesign should be given substantial consideration, especially with regard to the building\u2019s exterior.\n#### 4. Guiding principles for Federal architecture\nAgencies shall, to the extent practicable, adhere to the following Guiding Principles for Federal Architecture:\n**(1)**\nProvide requisite and adequate facilities in an architectural style and form that is distinguished and will reflect the dignity, enterprise, vigor, and stability of the American National Government, including through the use of the following:\n**(A)**\nBy their proven ability to meet these requirements, classical and traditional architecture are preferred modes of architectural design. This preference does not exclude the possibility of alternative styles in appropriate circumstances.\n**(B)**\nMajor emphasis should be placed on the choice of design that embody architectural excellence.\n**(C)**\nSpecific attention should be paid to the possibilities of incorporating into such designs qualities that reflect the regional architectural traditions of that part of the Nation in which buildings are located.\n**(D)**\nWhere appropriate, fine art should be incorporated in the designs, with emphasis on the work of living American artists.\n**(E)**\nDesigns shall adhere to sound construction practice and utilize materials, methods, and equipment proven dependability.\n**(F)**\nBuildings shall be economical to build, operate, and maintain, and should be accessible to the handicapped.\n**(2)**\nDesign must flow from the needs of the Government and the aspirations and preferences of the American people to the architectural profession, and not vice versa, including through the use of the following:\n**(A)**\nThe Government should be willing to pay some additional cost to avoid excessive uniformity in design of Federal buildings.\n**(B)**\nCompetitions for the design of Federal buildings should be held where appropriate.\n**(C)**\nThe advice of distinguished architects practiced in classical or traditional architecture ought to, as a rule, be sought prior to the award of important design contracts.\n**(3)**\nThe choice and development of the building site should be considered the first step of the design process, including through the use of the following:\n**(A)**\nThis choice should be made in cooperation with local agencies.\n**(B)**\nSpecial attention should be paid to the general ensemble of streets and public places of which Federal buildings will form a part.\n**(C)**\nWhere possible, buildings should be located so as to permit a generous development of landscape.\n#### 5. GSA requirements\n##### (a) In general\nThe Administrator shall adhere to the policy of the United States described in sections 3 and 4 and shall expeditiously update GSA policies and procedures to incorporate such policies and principles and advance the purpose of this Act.\n##### (b) Requirements\nThe Administrator shall\u2014\n**(1)**\nensure that GSA architects whose duties include reviewing, assisting with, or approving the selection of architects or designs for applicable Federal public buildings have formal training in, or substantial and significant experience with, classical or traditional architecture;\n**(2)**\ncreate the position of senior advisor for architectural design, for an individual with specialized experience in classical architecture, to help develop GSA procedures, advise on architectural standards, and provide guidance during design evaluations or design juries;\n**(3)**\nwhere the design of an applicable Federal public building is selected pursuant to a design-build competition under section 3309 of title 41, United States Code, list experience with classical or traditional architecture as specialized experience and technical competence in the phase-1 solicitation, and give substantial weight to these factors when evaluating which offerors will be advanced to phase 2; and\n**(4)**\nconsistent with sections 4302 and 4312 of title 5, United States Code, make advancing the purposes and implementing the policies of this Act a critical performance element in the individual performance plans of the GSA Chief Architect and appropriate subordinate employees in the GSA Public Buildings Service involved in selecting designs for applicable Federal public buildings.\n##### (c) Requirements for design competition\nWhere GSA intends to select a building design pursuant to a design competition, the Administrator shall\u2014\n**(1)**\nactively recruit architectural firms and, as applicable, designers with experience in classical and traditional architecture to enter such competition; and\n**(2)**\nto the extent practicable, ensure that multiple design modes are advanced to the final evaluation round of such competition.\n##### (d) Notification\nIn the event the Administrator proposes to approve a design for a new applicable Federal public building that diverges from the preferred architecture, including Brutalist or Deconstructivist architecture or any design derived from or related to these types of architecture, the Administrator shall notify the President through the Assistant to the President for Domestic Policy not less than 30 days before GSA could reject such design without incurring substantial expenditures. Such notification shall set forth the reasons the Administrator proposes to approve such design, including\u2014\n**(1)**\na detailed explanation of why the Administrator believes selecting such design is justified, with particular focus on whether such design is as beautiful and reflective of the dignity, enterprise, vigor, and stability of the American system of self-government as alternative designs of comparable cost of using preferred architecture;\n**(2)**\nthe total expected cost of adopting the proposed design, including estimated maintenance and replacement costs throughout its expected lifecycle; and\n**(3)**\na description of the designs using preferred architecture seriously considered for such project and the total expected cost of adopting such designs, including estimated maintenance and replacement costs throughout their expected lifecycles.",
      "versionDate": "2025-09-26",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-02T20:09:02Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5565ih.xml"
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
      "title": "Make Federal Architecture Beautiful Again Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Make Federal Architecture Beautiful Again Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote classical and traditional architectural styles in Federal public buildings to enhance civic pride, reflect national heritage, and ensure aesthetic excellence in government infrastructure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:22Z"
    }
  ]
}
```
