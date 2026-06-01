# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4686
- Title: LIFT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4686
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-10-25T08:05:48Z
- Update date including text: 2025-10-25T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4686",
    "number": "4686",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "LIFT Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:48Z",
    "updateDateIncludingText": "2025-10-25T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:16:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T21:29:08Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4686ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4686\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mrs. Kiggans of Virginia (for herself, Mr. Finstad , Mr. Wittman , Mr. McCormick , Mr. Fine , Mr. Shreve , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to expand Beyond Visual Line of Sight operations for unmanned aircraft systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Local Innovation for Flight Technologies Act of 2025 or the LIFT Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress has the meaning given the term in section 44801 of title 49, United States Code.\n**(2) Unmanned aircraft system**\nThe term unmanned aircraft system has the meaning given the term in section 44801 of title 49, United States Code.\n#### 3. Expanding unmanned aircraft systems operations\n##### (a) In general\nThe Secretary of Transportation shall\u2014\n**(1)**\nnot later than 30 days after the date of enactment of this Act, issue a proposed rule enabling routine Beyond Visual Line of Sight (hereinafter referred to as BVLOS ) operations for unmanned aircraft systems; and\n**(2)**\nnot later than 6 months after the date of enactment of this Act, issue a final rule based on the proposed rulemaking issued under paragraph (1).\n##### (b) Safety metrics\nThe Secretary of Transportation shall\u2014\n**(1)**\nnot later than 30 days after the date of enactment of this Act, establish metrics for assessing the performance and safety of BVLOS operations of unmanned aircraft systems; and\n**(2)**\nnot later than 180 days of the date of enactment of this Act, identify and describe any additional regulatory barriers and challenges to such BVLOS implementation and submit to the Director of the Office of Science and Technology Policy recommendations for\u2014\n**(A)**\naddressing the barriers and challenges expeditiously; and\n**(B)**\npotential regulation or legislative action.\n#### 4. Examination of applicable international requirements\nThe Secretary of Transportation shall\u2014\n**(1)**\nexplore options to ensure that unmanned aircraft systems operating over the high seas within flight informational regions for which the United States is responsible for operational control may operate without being subject to the requirements applicable to manned aircraft engaging in international navigation as referenced in the Convention on International Civil Aviation;\n**(2)**\nidentify potential barriers for the operation described in paragraph (1); and\n**(3)**\nsubmit to the appropriate committees of Congress\u2014\n**(A)**\na report on the findings under paragraphs (1) and (2); and\n**(B)**\nappropriate legislative recommendations necessary to enable such operation.\n#### 5. Use of artificial intelligence in waiver determinations\n##### (a) In general\nNot later than 120 days after the date of enactment of this Act, the Secretary of Transportation shall initiate the deployment of artificial intelligence tools to assist in and expedite the review of unmanned aircraft system waiver applications under part 107 of title 14, Code of Federal Regulations.\n##### (b) Capability of artificial intelligence tools\nThe artificial intelligence tools described in subsection (a) shall\u2014\n**(1)**\nsupport performance- and risk-based evaluation of proposed operations;\n**(2)**\nidentify materially similar precedents and recommend consistent mitigation measures;\n**(3)**\nassist the Administrator of the Federal Aviation Administration in identifying categories of unmanned aircraft system operations with sufficient safety data or recurring approval patterns that may warrant further rulemaking to eliminate the need for individualized waivers; and\n**(4)**\nbe used in accordance with guidance on Federal use of artificial intelligence, as detailed in Office of Management and Budget Memorandum M\u201325\u201321.\n##### (c) Additional waiver review\nIn conducting the deployment of artificial intelligence tools required under subsection (a), the Secretary of Transportation shall examine the extent to which such artificial intelligence tools could be used to review exemption petitions for applicants seeking to operate pursuant to section 44807 of title 49, United States Code.\n#### 6. Establishment of an electric vertical takeoff and landing pilot program\n##### (a) In general\nThe Secretary of Transportation, in coordination with the Director of the Office of Science and Technology Policy, shall establish the electric Vertical Takeoff and Landing (hereinafter referred to as eVTOL ) integration pilot program to provide grants to State, local, Tribal, and territorial governments to carry out projects to accelerate the deployment of safe eVTOL operations in the United States.\n##### (b) Request for proposals\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary shall issue a public request for proposals for the program established under subsection (a) to State, local, Tribal, and territorial governments.\n**(2) Submission requirements**\nSuch proposals shall be submitted not later than 90 days after the request is issued under subsection (a) and include a private sector partner with demonstrated experience in eVTOL aircraft development, manufacturing, and operations.\n##### (c) Selection of projects\nNot later than 180 days after the request is issued under subsection (a), the Secretary may select eligible pilot projects that propose to begin eVTOL operations not later than 90 days after the date on which any agreement for a pilot project is established. Selection criteria shall include\u2014\n**(1)**\nthe use of eVTOL aircraft and technologies developed or offered by a United States-based entity;\n**(2)**\noverall representation of economic and geographic operations and proposed models of public-private partnership; and\n**(3)**\noverall representation of the operations to be conducted, including advanced air mobility, medical response, cargo transport, and rural access.\n##### (d) Project agreements\n**(1) Agreement contents**\nThe Secretary shall execute agreements with applicants selected under subsection (c) that contain\u2014\n**(A)**\nproject goals;\n**(B)**\nregulatory needs;\n**(C)**\ntimelines;\n**(D)**\ninformation sharing and data exchange mechanisms; and\n**(E)**\nresponsibilities.\n##### (e) Reporting\n**(1) Implementation report**\nNot later than 180 days after the selection of pilot program participants under subsection (c), the Secretary shall submit to the Director of the Office of Science and Technology Policy and the appropriate committees of Congress an initial implementation report containing a summary of early-stage planning, interagency coordination, and any immediate regulatory or legislative challenges identified.\n**(2) Annual report**\nNot later than 1 year after the date on which the Secretary submits the initial implementation report under paragraph (1), and annually thereafter until the date specified in subsection (f), the Secretary shall submit to the Director and the appropriate committees of Congress a report that includes\u2014\n**(A)**\nthe progress of the pilot program;\n**(B)**\nany evaluation of program goals and outcomes;\n**(C)**\nrecommendations for the permanent integration of eVTOL operations into the national airspace; and\n**(D)**\nany proposed future initiatives to maintain United States leadership in eVTOL flight.\n##### (f) Sunset\nThe Secretary shall cease to provide grants under the pilot program established under this section on the date that is 3 years after the date the first pilot project becomes operational, unless the Secretary determines that an extension is warranted in the national interest.\n##### (g) Information use and sharing\nThe Secretary shall\u2014\n**(1)**\nuse the information and experience yielded by the pilot program to inform the development of regulations, initiatives, and plans to enable safe eVTOL operations; and\n**(2)**\nas appropriate, share such information with the Secretary of Defense, the Attorney General, the Secretary of Homeland Security, and the heads of other relevant agencies.\n#### 7. Prioritization of unmanned aircraft systems manufactured in the United States\nThe Secretary of Transportation shall prioritize the integration of unmanned aircraft systems manufactured in the United States into the national airspace system over unmanned aircraft systems manufactured outside of the United States to the maximum extent permitted by law.",
      "versionDate": "2025-07-23",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-17T17:11:57Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4686ih.xml"
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
      "title": "LIFT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIFT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Local Innovation for Flight Technologies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to expand Beyond Visual Line of Sight operations for unmanned aircraft systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:30Z"
    }
  ]
}
```
