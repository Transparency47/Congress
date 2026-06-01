# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7941?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7941
- Title: Pay TSA Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7941
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-05-16T08:08:06Z
- Update date including text: 2026-05-16T08:08:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-17 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-03-17 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7941",
    "number": "7941",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Pay TSA Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:06Z",
    "updateDateIncludingText": "2026-05-16T08:08:06Z"
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
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T19:52:23Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "IN"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "MI"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "IA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "VA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "NE"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7941ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7941\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Langworthy (for himself, Mr. Lawler , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo ensure the passenger security fee paid by airline passengers is used exclusively for aviation security, establish a Transportation Security Trust Fund to support the operations and personnel of the Transportation Security Administration, and ensure continuity of aviation security operations during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay TSA Act of 2026 .\n#### 2. Transportation security funding\n##### (a) Repeal of diversion of passenger security fees\nSection 44940 of title 49, United States Code, is amended\u2014\n**(1)**\nby striking subsection (f); and\n**(2)**\nby striking subsection (i).\n##### (b) Transportation Security Trust Fund\n**(1) Establishment**\nThere is established in the Department of Homeland Security a fund to be known as the Transportation Security Trust Fund (referred to in this Act as the Fund ).\n**(2) Deposits**\nAmounts collected from fees imposed under section 44940 of title 49, United States Code (commonly known as the 9/11 Security Fee ), shall be deposited into the Fund and available without further appropriation and without fiscal year limitation.\n**(3) Use of funds**\nAmounts in the Fund shall be available to the Administrator of the Transportation Security Administration for activities to strengthen aviation security, including relating to the following:\n**(A)**\nSalaries, benefits, training, and workforce support for Administration personnel.\n**(B)**\nPassenger and baggage screening operations.\n**(C)**\nAviation security checkpoint and screening technology.\n**(D)**\nAirport security infrastructure and equipment.\n**(E)**\nResearch, development, and deployment of advanced aviation security systems.\n**(4) Restriction on diversion of funds**\nAmounts deposited in the Fund\u2014\n**(A)**\nshall be used only for the aviation security purposes specified in paragraph (3); and\n**(B)**\nmay not be transferred to the general fund of the Treasury or used for deficit reduction or other non-aviation security purposes.\n##### (c) Availability of funds during a lapse in appropriations\n**(1) Availability**\n**(A) In general**\nIf during any period during any fiscal year the discretionary appropriations Act providing funding for the Transportation Security Administration, or continuing appropriations for the Transportation Security Administration, are not enacted into law, amounts in the Fund shall be available without further appropriation or fiscal year limitation to the Administrator of the Transportation Security Administration for the continuation of programs, projects, and activities necessary to maintain aviation security operations.\n**(B) Aviation Security Capital Fund**\nNotwithstanding section 44923(h) of title 49, United States Code, during any period described in subparagraph (A), amounts available in the Aviation Security Capital Fund established under such section 44923(h) shall be available to the Administrator of the Transportation Security Administration to carry out the activities described in such subparagraph, subject to the priorities described in this subsection.\n**(2) Priority for TSA personnel**\n**(A) In general**\nIn carrying out paragraph (1), the Administrator of the Transportation Security Administration shall prioritize the use of funds made available pursuant to paragraph (1) for the following:\n**(i)**\nSalaries, benefits, and overtime compensation of Transportation Security Officers and other personnel necessary to conduct passenger and baggage screening and aviation security operations.\n**(ii)**\nStaffing levels required to maintain the safe and efficient operation of aviation security screening checkpoints and related security functions.\n**(iii)**\nOther operational expenses directly supporting frontline aviation security personnel.\n**(B) Application**\nAmounts made available under this paragraph shall first be applied to carry out subparagraph (A)(i).\n**(3) Secondary uses for security infrastructure and technology**\nAfter the funding requirements described in paragraph (2) have been satisfied, remaining amounts made available pursuant to paragraph (1) may be used for the following:\n**(A)**\nThe procurement, deployment, and sustainment of aviation security checkpoint technology.\n**(B)**\nBaggage screening equipment and related aviation security infrastructure.\n**(C)**\nMaintenance and modernization of airport security systems.\n**(D)**\nGrants to airports for aviation security technology improvements.\n**(4) Rate for operations**\nFunds made available under this subsection shall be provided at a rate for operations not greater than the rate for operations provided for the Transportation Security Administration programs, projects, and activities described in this subsection during the immediately preceding fiscal year.\n**(5) Duration of authority**\nThe authority provided under this subsection shall remain in effect for the period beginning on the first day of a lapse in appropriations and ending on the date on which\u2014\n**(A)**\nthe applicable regular appropriation Act providing funding for the Transportation Security Administration is enacted into law; or\n**(B)**\ncontinuing appropriations for the Transportation Security Administration are enacted into law.\n**(6) Terms and conditions**\nFunds made available under this subsection shall be subject to the terms, conditions, and limitations applicable to the Transportation Security Administration programs, projects, and activities on the date immediately preceding the date on which the applicable lapse of appropriations occurs for the immediately preceding fiscal year.\n##### (d) Aviation security technology and infrastructure account\n**(1) Establishment**\nThere is established in the Fund an account to be known as the Aviation Security Technology and Infrastructure Account (referred to in this subsection as the Account ).\n**(2) Purpose**\nThe purpose of the Account is to support the modernization, procurement, deployment, and sustainment of aviation security technology and infrastructure necessary to enhance the safety and efficiency of passenger and baggage screening operations.\n**(3) Availability of funds**\nAmounts in the Account shall be available until expended to the Administrator of the Transportation Security Administration for aviation security technology and infrastructure investments only after the funding requirements necessary to support Transportation Security Administration personnel and operational aviation security activities have been satisfied, including the compensation and staffing requirements described in subsection (c)(2).\n**(4) Authorized uses**\nAmounts made available under this subsection may be used for the following:\n**(A)**\nProcurement, deployment, and sustainment of aviation security checkpoint technology.\n**(B)**\nComputed tomography screening systems and related screening equipment.\n**(C)**\nCredential authentication technology and related passenger screening systems.\n**(D)**\nAirport security screening infrastructure and associated equipment.\n**(E)**\nExit lane and perimeter security technology.\n**(F)**\nGrants to airports for aviation security technology deployment and modernization.",
      "versionDate": "2026-03-16",
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
        "updateDate": "2026-04-02T19:26:38Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7941ih.xml"
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
      "title": "Pay TSA Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay TSA Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-01T07:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure the passenger security fee paid by airline passengers is used exclusively for aviation security, establish a Transportation Security Trust Fund to support the operations and personnel of the Transportation Security Administration, and ensure continuity of aviation security operations during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-01T07:18:21Z"
    }
  ]
}
```
