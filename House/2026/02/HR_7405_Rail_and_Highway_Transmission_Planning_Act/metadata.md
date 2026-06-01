# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7405?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7405
- Title: Rail and Highway Transmission Planning Act
- Congress: 119
- Bill type: HR
- Bill number: 7405
- Origin chamber: House
- Introduced date: 2026-02-05
- Update date: 2026-05-05T08:05:57Z
- Update date including text: 2026-05-05T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-05: Introduced in House

## Actions

- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7405",
    "number": "7405",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
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
    "title": "Rail and Highway Transmission Planning Act",
    "type": "HR",
    "updateDate": "2026-05-05T08:05:57Z",
    "updateDateIncludingText": "2026-05-05T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-05",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-05",
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
          "date": "2026-02-05T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "VA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7405ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7405\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2026 Mr. Mullin introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Energy to conduct a study on using highway rights-of-way and rail rights-of-way as locations on which to construct high-voltage transmission infrastructure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rail and Highway Transmission Planning Act .\n#### 2. Sense of Congress; Purpose\n##### (a) Sense of Congress\nIt is the sense of Congress that transportation rights-of-way, including highway and rail rights-of-way, should be utilized in ways that serve the public interest, including accommodating new electric transmission infrastructure.\n##### (b) Purpose\nThe purpose of this Act is to accelerate the development of high-voltage transmission infrastructure by identifying opportunities to co-locate such projects within existing transportation rights-of-way, with the goal of alleviating energy capacity constraints and delivering more affordable, reliable electricity for consumers.\n#### 3. Study on placing high-voltage transmission infrastructure on rail and highway rights-of-ways\n##### (a) Study\nThe Secretary of Energy, in consultation with the Secretary of Transportation, the Federal Energy Regulatory Commission, and each director of a National Laboratory determined relevant by the Secretary of Energy, shall conduct a study evaluating the potential benefits and challenges of using covered rights-of-way as locations on which to construct high-voltage transmission infrastructure.\n##### (b) Elements\nIn carrying out the study under subsection (a), the Secretary of Energy shall\u2014\n**(1)**\nconduct a review of projects completed or being carried out to develop high-voltage electric transmission infrastructure on a covered right-of-way in the United States, including an assessment of any challenges with respect to safety, engineering, property rights, or other matters encountered while carrying out such projects and how each such challenge was addressed;\n**(2)**\nbased on the results of the review under paragraph (1), determine best practices with respect to the planning, permitting, financing, and developing of high-voltage electric transmission infrastructure on a covered right-of-way;\n**(3)**\ngenerate, or consolidate from available sources, data on covered rights-of-way to evaluate the technical feasibility of building high-voltage transmission lines on each such covered right-of-way;\n**(4)**\nusing data generated or consolidated under paragraph (3), identify each covered right-of-way suitable for the construction of high-voltage transmission lines considering\u2014\n**(A)**\nwith respect to the geographic region of each covered right-of-way evaluated, the need for transmission infrastructure to alleviate energy transmission capacity constraints or congestion in the geographic region;\n**(B)**\nthe technical feasibility of building high-voltage transmission lines on each such covered right-of-way; and\n**(C)**\nany other considerations determined appropriate by the Secretary;\n**(5)**\nwith respect to each covered right-of-way identified under paragraph (4)\u2014\n**(A)**\nevaluate the suitability of various high-voltage transmission configurations, accounting for the infrastructure needs of each such configuration, including\u2014\n**(i)**\nhigh-voltage alternating current;\n**(ii)**\nhigh-voltage direct current;\n**(iii)**\npoint-to-point high-voltage direct current;\n**(iv)**\nmulti-terminal bi-directional high-voltage direct current systems;\n**(v)**\noverhead lines;\n**(vi)**\nunderground lines; and\n**(vii)**\nany other relevant configuration, as determined by the Secretary;\n**(B)**\nidentify and examine any potential challenges unique to transmission development in the covered right-of-way;\n**(C)**\ndetermine the costs and benefits of constructing high-voltage transmission infrastructure in the covered right-of-way, including any cost or time savings expected to be realized with respect to land acquisition or obtaining any requisite permits, and compare such costs and benefits to the average costs and benefits of constructing similar high-voltage transmission infrastructure on lands that are not a covered right-of-way;\n**(D)**\nidentify\u2014\n**(i)**\nany potential funding mechanisms and financing opportunities available for entities to use for the construction of high-voltage transmission infrastructure on the right-of-way; and\n**(ii)**\nany potential financial benefits for stakeholders in such construction, including owners of property abutting the right-of-way or otherwise implicated by the construction; and\n**(E)**\nanalyze how, if at all, the construction of high-voltage transmission infrastructure on the covered right-of-way is likely to support improvements in grid reliability, streamline the interconnection queue, increase energy transmission capacity, contribute to reduced energy costs for energy consumers, and improve highway or rail safety and efficiency;\n**(6)**\nevaluate the effects, if any, of constructing and operating high-voltage transmission lines on covered rights-of-way on the environment, railroad operations, and communities near the right-of-way, including\u2014\n**(A)**\nelectromagnetic interference with rail safety, rail signaling equipment, and rail communication equipment; and\n**(B)**\nthe potential for safety or operational interference while performing maintenance, rehabilitation work, or expansion of transportation infrastructure on covered rights-of-way;\n**(7)**\ndevelop\u2014\n**(A)**\nan interagency action plan with respect to the construction and operation of high-voltage transmission lines on covered rights-of-way; and\n**(B)**\nfor use facilitating the construction of high-voltage transmission infrastructure on a covered right-of-way, resources for use by\u2014\n**(i)**\nFederal, State, and local governmental agencies; and\n**(ii)**\nutilities, railroad carriers, and other relevant stakeholders, as identified by the Secretary; and\n**(8)**\nconsult utilities, railroad carriers, and any relevant stakeholders, as identified by the Secretary.\n##### (c) Publication\n**(1) Rolling publication of study elements**\nAs soon as is practicable after each element of the study described in subsection (b) is complete, the Secretary shall publish the results of the element and any data developed or consolidated in the completion of the element.\n**(2) Report**\nNot later than 3 years after the date of enactment of this Act, the Secretary shall\u2014\n**(A)**\nsubmit to Congress a report detailing the results of the study under subsection (a), including all data underpinning such results, which shall be presented in a machine-readable format; and\n**(B)**\npublish such report and such data.\n**(3) Form**\nAll information, data, and reports published pursuant to this subsection\u2014\n**(A)**\nshall be published on a publicly accessible website of the Department of Energy; and\n**(B)**\nmay be published with redactions of any data the publication of which the Secretary determine poses a national security risk.\n##### (d) Definitions\nIn this section:\n**(1) Covered right-of-way**\nThe term covered right-of-way means\u2014\n**(A)**\na highway right-of-way, including a right-of-way of a State highway and a right-of-way of the National Highway System; or\n**(B)**\na rail right-of-way, including a right-of-way of an abandoned railroad.\n**(2) Highway; National Highway System**\nThe terms highway and National Highway System have the meanings given such terms, respectively, in section 101 of title 23, United States Code.\n**(3) National Laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(4) Railroad carrier**\nThe term railroad carrier has the meaning given such term in section 20102 of title 49, United States Code.",
      "versionDate": "2026-02-05",
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
        "name": "Energy",
        "updateDate": "2026-02-26T18:31:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7405ih.xml"
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
      "title": "Rail and Highway Transmission Planning Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rail and Highway Transmission Planning Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Energy to conduct a study on using highway rights-of-way and rail rights-of-way as locations on which to construct high-voltage transmission infrastructure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:32Z"
    }
  ]
}
```
