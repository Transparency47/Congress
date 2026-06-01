# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2726?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2726
- Title: Beautifying Federal Civic Architecture Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2726
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2026-04-01T23:54:57Z
- Update date including text: 2026-04-01T23:54:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2726",
    "number": "2726",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Beautifying Federal Civic Architecture Act of 2025",
    "type": "S",
    "updateDate": "2026-04-01T23:54:57Z",
    "updateDateIncludingText": "2026-04-01T23:54:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T18:12:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "KS"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "TN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "MS"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "TN"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2726is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2726\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Banks (for himself, Mr. Marshall , Mrs. Blackburn , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo prescribe Guiding Principles for Federal Architecture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Beautifying Federal Civic Architecture Act of 2025 .\n#### 2. Policy of the United States\nIt is the policy of the United States that\u2014\n**(1)**\napplicable Federal public buildings should\u2014\n**(A)**\nuplift and beautify public spaces;\n**(B)**\ninspire the human spirit;\n**(C)**\nennoble the United States;\n**(D)**\ncommand respect from the general public;\n**(E)**\nbe visually identifiable as civic buildings; and\n**(F)**\nas appropriate, respect regional architectural heritage;\n**(2)**\ndesigns for applicable Federal public buildings should be selected with substantial input from the local community;\n**(3)**\narchitecture, particularly traditional architecture and classical architecture, that meets the criteria described in paragraph (1) is the preferred architecture for applicable Federal public buildings;\n**(4)**\nin the District of Columbia, classical architecture is the preferred and default architecture for applicable Federal public buildings absent exceptional factors necessitating another kind of architecture;\n**(5)**\nwhere the architecture of applicable Federal public buildings diverges from the criteria described in paragraph (1), great care and consideration shall be taken to choose a design that\u2014\n**(A)**\ncommands respect from the general public; and\n**(B)**\nclearly conveys to the general public the dignity, enterprise, vigor, and stability of the system of self-government of the United States;\n**(6)**\nwhen renovating, reducing, or expanding applicable Federal public buildings that do not meet the criteria described in paragraph (1), the feasibility and potential expense of building redesign to meet that criteria should be examined; and\n**(7)**\nwhere feasible and economical, a redesign described in paragraph (6) should be given substantial consideration, especially with respect to the exterior of the applicable Federal public building.\n#### 3. Definitions\nIn this Act:\n**(1) 2025 dollars**\nThe term 2025 dollars means dollars adjusted for inflation using the Gross Domestic Product price deflator of the Bureau of Economic Analysis, with 2025 as the base year.\n**(2) Administration**\nThe term Administration means the General Services Administration.\n**(3) Administrator**\nThe term Administrator means the Administrator of General Services.\n**(4) Applicable Federal public building**\n**(A) In general**\nThe term applicable Federal public building means\u2014\n**(i)**\nany Federal courthouse;\n**(ii)**\nany Federal agency headquarters;\n**(iii)**\nany public building in the National Capital region (as defined in section 8702 of title 40, United States Code); and\n**(iv)**\nany other public building, the cost or expected cost to design, build, and finish of which is more than $50,000,000 in 2025 dollars.\n**(B) Exclusions**\nThe term applicable Federal public building does not include an infrastructure project or a land port of entry.\n**(5) Brutalist architecture**\nThe term Brutalist architecture means the style of architecture that grew out of the early 20th-century modernist movement that is characterized by a massive and block-like appearance with a rigid geometric style and large-scale use of exposed poured concrete.\n**(6) Classical architecture**\n**(A) In general**\nThe term classical architecture means the architectural tradition\u2014\n**(i)**\nderived from the forms, principles, and vocabulary of the architecture of Greek and Roman antiquity; and\n**(ii)**\nlater developed and expanded on by\u2014\n**(I)**\nRenaissance architects, including Alberti, Brunelleschi, Michelangelo, and Palladio;\n**(II)**\nEnlightenment masters, including Robert Adam, John Soane, and Christopher Wren;\n**(III)**\n19th Century architects, including Benjamin Henry Latrobe, Robert Mills, and Thomas U. Walter; and\n**(IV)**\n20th Century practitioners, including Julian Abele, Daniel Burnham, Rafael Carmoega, Charles F. McKim, John Russell Pope, Julia Morgan, and the firm of Delano and Aldrich.\n**(B) Inclusions**\nThe term classical architecture includes styles such as Neoclassical, Georgian, Federal, Greek Revival, Beaux-Arts, and Art Deco.\n**(7) Deconstructivist architecture**\nThe term Deconstructivist architecture means the style of architecture\u2014\n**(A)**\ngenerally known as deconstructivism ; and\n**(B)**\nthat emerged during the late 1980s and features fragmentation, disorder, discontinuity, distortion, skewed geometry, and the appearance of instability.\n**(8) General public**\nThe term general public means members of the public who are not\u2014\n**(A)**\nartists, architects, engineers, art or architecture critics, instructors or professors of art or architecture, or members of the building industry; or\n**(B)**\naffiliated with any interest group, trade association, or any other organization whose membership is financially affected by decisions involving the design, construction, or remodeling of public buildings.\n**(9) Officer**\nThe term officer has the meaning given the term in section 2104 of title 5, United States Code.\n**(10) Preferred architecture**\nThe term preferred architecture means the architecture described in section 2(3).\n**(11) Public building**\nThe term public building has the meaning given the term in section 3301(a) of title 40, United States Code.\n**(12) Traditional architecture**\nThe term traditional architecture includes\u2014\n**(A)**\nclassical architecture; and\n**(B)**\nthe historic humanistic architecture, including Gothic, Romanesque, Second Empire, Pueblo Revival, Spanish Colonial, and other Mediterranean styles of architecture historically rooted in various regions of the United States.\n#### 4. Guiding Principles for Federal Architecture\nTo the maximum extent practicable, all Federal agencies shall adhere to the following Guiding Principles for Federal Architecture (referred to in this Act as the Guiding Principles ):\n**(1) Preferred architectural style**\n**(A) In general**\nProvide requisite and adequate facilities in a preferred architectural style and form that is distinguished and reflects the dignity, enterprise, vigor, and stability of the Federal Government which, by its proven ability to meet those requirements, shall be classical architecture and traditional architecture, while not excluding the possibility of alternative architectural styles in appropriate circumstances.\n**(B) Requirements**\nIn carrying out subparagraph (A), each Federal agency shall ensure that\u2014\n**(i)**\nmajor emphasis is placed on the choice of design that embodies architectural excellence;\n**(ii)**\nspecific attention is paid to the possibilities of incorporating into that design qualities that reflect the regional architectural traditions of the area of the United States in which the applicable Federal public building is located;\n**(iii)**\nwhere appropriate, fine art is incorporated into that design, with emphasis on the work of living American artists;\n**(iv)**\nthe design adheres to sound construction practice and uses proven dependable materials, methods, and equipment; and\n**(v)**\napplicable Federal public buildings are economical to build, operate, and maintain and accessible to the handicapped.\n**(2) Flow of design**\n**(A) In general**\nDesign must flow from the needs of the Federal Government and the aspirations and preferences of the people of the United States to the architectural profession, and not vice versa.\n**(B) Requirements**\nIn carrying out subparagraph (A), each Federal agency shall\u2014\n**(i)**\nbe willing to pay additional costs to avoid excessive uniformity in the design of applicable Federal public buildings;\n**(ii)**\nwhere appropriate, carry out competitions for the design of applicable Federal public buildings; and\n**(iii)**\nprior to the awarding of important design contracts, seek the advice of distinguished architects practiced in classical architecture or traditional architecture.\n**(3) Building sites**\n**(A) In general**\nThe choice and development of the site of an applicable Federal public building shall be considered the first step of the design process, which shall be the made in cooperation with State and local agencies.\n**(B) Requirements**\nIn carrying out subparagraph (A), each Federal agency shall\u2014\n**(i)**\npay special attention to the general ensemble of streets and public places of which the applicable Federal public buildings will form a part; and\n**(ii)**\nwhere possible, ensure applicable Federal public buildings are located in a way so as to permit a generous development of landscape.\n#### 5. GSA requirements\n##### (a) In general\nThe Administrator shall\u2014\n**(1)**\nadhere to the policy of the United States described in section 2 and the Guiding Principles; and\n**(2)**\nexpeditiously update policies and procedures of the Administration\u2014\n**(A)**\nto incorporate the policy of the United States described in section 2 and the Guiding Principles; and\n**(B)**\nto advance the purpose of this Act.\n##### (b) Requirements\nIn adhering to the policy of the United States described in section 2 and the Guiding Principles, the Administrator shall\u2014\n**(1)**\nensure that architects employed by the Administration, whose duties include reviewing, assisting with, or approving the selection of architects or designs for applicable Federal public buildings, have formal training in, or substantial and significant experience with, classical architecture or traditional architecture;\n**(2)**\nestablish a position of Senior Advisor for Architectural Design in the Administration, which shall be filled by an individual with specialized experience in classical architecture or traditional architecture, the responsibilities of which shall be\u2014\n**(A)**\nto assist in the development of Administration procedures relating to carrying out this Act;\n**(B)**\nto advise on architectural standards; and\n**(C)**\nto provide guidance to the Administrator during design evaluations or design juries;\n**(3)**\nwhere the design of an applicable Federal public building is selected pursuant to a design-build competition under section 3309 of title 41, United States Code\u2014\n**(A)**\nlist experience with classical architecture or traditional architecture as specialized experience and technical competence in the phase-one solicitation; and\n**(B)**\ngive substantial weight to those factors when evaluating which offerors will be advanced to phase-two; and\n**(4)**\nconsistent with sections 4302 and 4312 of title 5, United States Code, make advancing the purposes and implementing the policies of this Act a critical performance element in the individual performance plans of the Chief Architect of the Administration and appropriate subordinate employees in the Public Buildings Service involved in selecting designs for applicable Federal public buildings.\n##### (c) Design competitions\nIn addition to the requirements described in subsection (b)(3), if the Administrator intends to select a building design for an applicable Federal building pursuant to a design competition, the Administrator shall\u2014\n**(1)**\nactively recruit architectural firms;\n**(2)**\nas applicable, recruit designers with experience in classical architecture and traditional architecture to enter the competition; and\n**(3)**\nto the maximum extent practicable, ensure that multiple design modes are advanced to the final evaluation round.\n##### (d) Notification\n**(1) In general**\nIf the Administrator proposes to approve a design for a new applicable Federal public building that diverges from the preferred architecture, including Brutalist architecture, Deconstructivist architecture, or any design derived from or related to those styles of architecture, the Administrator shall submit to the Assistant to the President for Domestic Policy, not later than 30 days before the date on which the Administrator could reject the design without incurring substantial expenditures, a notification in accordance with paragraph (2).\n**(2) Requirements**\nA notification submitted under paragraph (1) shall describe the reasons the Administrator proposes to approve a design described in that paragraph, including\u2014\n**(A)**\na detailed explanation of why the Administrator believes selecting the design is justified, with particular focus on whether the design is as beautiful and reflective of the dignity, enterprise, vigor, and stability of the system of self-government in the United States as alternative designs of comparable cost using preferred architecture;\n**(B)**\nthe total expected cost of adopting the proposed design, including estimated maintenance and replacement costs throughout the expected lifecycle of the design; and\n**(C)**\n**(i)**\na description of the designs using preferred architecture seriously considered for the project; and\n**(ii)**\nthe total expected cost of adopting those designs, including estimated maintenance and replacement costs throughout the expected lifecycles of those designs.\n#### 6. General provisions\n##### (a) Savings provision\nNothing in this Act impairs or otherwise affects\u2014\n**(1)**\nthe authority granted by law to an executive department or agency, or the head thereof; or\n**(2)**\nthe functions of the Director of the Office of Management and Budget relating to budgetary, administrative, or legislative proposals.\n##### (b) Implementation\nThis Act shall be implemented consistent with applicable law and subject to the availability of appropriations.\n##### (c) No creation of right or benefit\nNothing in this Act creates any right or benefit, substantive or procedural, enforceable at law or in equity by any party against the United States, including\u2014\n**(1)**\nits departments, agencies, or entities;\n**(2)**\nits officers, employees, or agents; or\n**(3)**\nany other person.\n#### 7. Annual report to Congress\nAnnually, the Administrator shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Accountability of the House of Representatives a report relating to the carrying out of this Act, detailing adherence to the policy of the United States described in section 2 and the Guiding Principles.",
      "versionDate": "2025-09-04",
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
        "actionDate": "2025-09-09",
        "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management."
      },
      "number": "5194",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Beautifying Federal Civic Architecture Act of 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-12T17:07:01Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2726is.xml"
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
      "title": "Beautifying Federal Civic Architecture Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Beautifying Federal Civic Architecture Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prescribe Guiding Principles for Federal Architecture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:26Z"
    }
  ]
}
```
