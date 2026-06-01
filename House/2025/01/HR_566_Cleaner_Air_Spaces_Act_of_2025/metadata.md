# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/566?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/566
- Title: Cleaner Air Spaces Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 566
- Origin chamber: House
- Introduced date: 2025-01-20
- Update date: 2026-04-16T08:06:38Z
- Update date including text: 2026-04-16T08:06:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-20: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-20: Introduced in House

## Actions

- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Introduced in House
- 2025-01-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-20",
    "latestAction": {
      "actionDate": "2025-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/566",
    "number": "566",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Cleaner Air Spaces Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:38Z",
    "updateDateIncludingText": "2026-04-16T08:06:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-20",
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
      "actionDate": "2025-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-20",
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
          "date": "2025-01-20T15:01:15Z",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "NV"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "MA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CO"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "CO"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-01-20",
      "state": "WA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "OH"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr566ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 566\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2025 Mr. Peters (for himself, Ms. Jacobs , Ms. Titus , Mr. Moulton , Mr. Khanna , Mr. Panetta , Mr. Costa , Mr. Neguse , Ms. Pettersen , Mr. Mullin , Mr. Garamendi , Mr. Swalwell , Ms. DeGette , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to provide grants to air pollution control agencies to implement a cleaner air space program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cleaner Air Spaces Act of 2025 .\n#### 2. Cleaner air space program grant\n##### (a) In general\nSubject to the availability of appropriations, the Administrator shall provide grants to air pollution control agencies to implement a cleaner air space program in accordance with this section.\n##### (b) Grant requirements\n**(1) Amounts**\nUnder this section, the Administrator may not provide a grant to an air pollution control agency in an amount that exceeds $3,000,000.\n**(2) Grants for Tribes**\nThe Administrator shall provide at least one grant to a Tribal agency that has jurisdiction over air quality.\n##### (c) Application\n**(1) In general**\nTo apply for a grant provided under this section, an air pollution control agency shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator determines appropriate, including a proposal for the implementation of a cleaner air space program.\n**(2) Proposal for cleaner air space program requirements**\nA proposal for the implementation of a cleaner air space program under paragraph (1) shall include the following:\n**(A)**\nCertification of partnering with a community-based organization.\n**(B)**\nDetails on the responsibilities of all parties involved with the cleaner air space program, including the responsibilities of\u2014\n**(i)**\nthe air pollution control agency; and\n**(ii)**\nany community-based organizations for which the air pollution control agency is partnering with under subparagraph (A).\n**(C)**\nInformation regarding which geographic population or community of covered households may be receiving eligible air filtration units under such cleaner air space program.\n**(D)**\nInformation on how the air pollution control agency plans to\u2014\n**(i)**\ndistribute educational materials related to eligible air filtration units; and\n**(ii)**\nadvertise the availability of clean air centers.\n**(E)**\nInformation on how such air pollution control agency plans to establish a clean air center, including\u2014\n**(i)**\nthe facility in which a clean air center may be established; and\n**(ii)**\nthe capacity and ventilation characteristics of such facility.\n**(F)**\nA description of the costs that may be associated with the program, including any administrative costs.\n##### (d) Cleaner air space program requirements\nSubject to partnership requirement under subsection (e), an air pollution control agency implementing a cleaner air space program pursuant to subsection (a) shall\u2014\n**(1)**\nestablish at least one clean air center that is\u2014\n**(A)**\nlocated in an area at risk of being exposed to wildland fire smoke;\n**(B)**\naccessible to individuals that reside in covered households; and\n**(C)**\nopen, accessible, and staffed during wildland fire smoke events with the option of being open, accessible, and staffed before or after wildland fire smoke events;\n**(2)**\nadvertise to the public\u2014\n**(A)**\nduring a wildland fire smoke event, the availability of a clean air center; and\n**(B)**\nthe local cleaner air space program that such air pollution control agency is implementing, including information about such local cleaner air space program, the availability of free air filtration units (if applicable), eligibility requirements to receive such free air filtration unit, and information on who to contact for more information with respect to such local cleaner air space program;\n**(3)**\nat no cost to covered households\u2014\n**(A)**\ndistribute a minimum of 1,000 eligible air filtration units to such covered households; and\n**(B)**\nprovide one air filter replacement for each eligible air filtration unit distributed under subparagraph (A);\n**(4)**\ndistribute educational materials that include information on how to best utilize an eligible air filtration unit to create a clean air room in a home;\n**(5)**\ncollect, and provide to the Administrator, information on\u2014\n**(A)**\neach type of eligible air filtration unit distributed under such cleaner air space program;\n**(B)**\nthe number of eligible air filtration unit so distributed; and\n**(C)**\nthe cost of each type of eligible air filtration unit so distributed; and\n**(6)**\nnot later than 6 months after providing an eligible air filtration unit to a covered household, conduct an anonymous survey of an individual of such covered household that received the eligible air filtration unit through the cleaner air space program on\u2014\n**(A)**\nwhether such individual understood how to properly set up a clean air room and how to utilize the air filtration unit;\n**(B)**\nhow often such individual utilized the air filtration unit;\n**(C)**\nthe largest barriers to properly utilizing the air filtration unit or creating a clean air room;\n**(D)**\nwhether such individual reported better air conditions in the clean air room of such individual compared to other parts of the home of such individual; and\n**(E)**\nhow the implementation of the cleaner air space program could improve.\n##### (e) Partnership\nIn implementing a cleaner air space program under subsection (a), an air pollution control agency shall partner with at least one community-based organization to carry out the requirements of such cleaner air space program under subsection (d).\n##### (f) Report\nNot later than 3 years after the date of the enactment of this Act, the Administrator shall submit to Congress a report that includes\u2014\n**(1)**\ninformation on each cleaner air space program implemented using a grant provided under subsection (a), including\u2014\n**(A)**\nthe name of the air pollution control agency that received such grant; and\n**(B)**\nthe information described in subsection (d)(5) collected by such air pollution control agency;\n**(2)**\nresponses from the survey described in subsection (d)(6); and\n**(3)**\nrecommendations on\u2014\n**(A)**\nwhether the cleaner air space program should be expanded; and\n**(B)**\nhow the cleaner air space program can be improved.\n##### (g) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Air pollution control agency**\nThe term air pollution control agency has the meaning given such term in section 302 of the Clean Air Act ( 42 U.S.C. 7602 ).\n**(3) Clean air center**\nThe term clean air center means one or more clean air rooms in a publicly accessible building.\n**(4) Clean air room**\nThe term clean air room means a room that is designed to keep levels of harmful air pollutants as low as possible during wildland fire smoke events.\n**(5) Covered household**\nThe term covered household means a household that\u2014\n**(A)**\nis located in a low-income community; and\n**(B)**\nincludes a person who\u2014\n**(i)**\nis at high risk of experiencing a wildland fire smoke event; and\n**(ii)**\nis vulnerable to negative health effects caused by wildland fire smoke due to factors such as an underlying health condition, a disability, or age.\n**(6) Eligible air filtration unit**\nThe term eligible air filtration unit means an air filtration unit that\u2014\n**(A)**\nis certified by Association of Home Appliance Manufacturers to have a Clean Air Delivery Rate of at least 97 for smoke;\n**(B)**\nis certified under the Energy Star program established by section 324A of the Energy Policy and Conservation Act ( 42 U.S.C. 6294a );\n**(C)**\ndoes not emit ozone; and\n**(D)**\nuses a true high-efficiency particulate air filter rated to remove 99.97 percent of particles measuring 0.3 micrometers or greater.\n**(7) Low-income community**\nThe term low-income community has the meaning given such term in section 45D of the Internal Revenue Code ( 26 U.S.C. 45D ).\n##### (h) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Administrator to carry out this section $30,000,000 for the period of fiscal years 2026 through 2028.\n**(2) Administrative expenses**\nOf the funds made available under paragraph (1), the Administrator may use not more than 10 percent of such funds on expenses relating to administering the cleaner air space program.",
      "versionDate": "2025-01-20",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Air quality",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Environmental technology",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-08-05T17:21:46Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-08-05T17:21:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-02-20T15:15:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-20",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr566",
          "measure-number": "566",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-20",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr566v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Cleaner Air Spaces Act of 2025</strong></p><p>This bill requires the Environmental Protection Agency to provide grants to air pollution control agencies, including at least one tribal agency with jurisdiction over air quality, to implement cleaner air space programs\u00a0(i.e., programs to provide clean air to the public during wildland fire smoke events). Generally, such programs must be located in areas at risk of exposure to wildland fire smoke and must help provide educational materials, clean air centers (i.e., one or more clean air rooms in a publicly accessible building), and air filtration systems to certain households. Clean air rooms are rooms designed to keep levels of harmful air pollutants as low as possible during wildland fire smoke events.</p><p>Under the bill, air pollution control agencies must partner with at least one community-based organization in implementing such programs.</p>"
        },
        "title": "Cleaner Air Spaces Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr566.xml",
    "summary": {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cleaner Air Spaces Act of 2025</strong></p><p>This bill requires the Environmental Protection Agency to provide grants to air pollution control agencies, including at least one tribal agency with jurisdiction over air quality, to implement cleaner air space programs\u00a0(i.e., programs to provide clean air to the public during wildland fire smoke events). Generally, such programs must be located in areas at risk of exposure to wildland fire smoke and must help provide educational materials, clean air centers (i.e., one or more clean air rooms in a publicly accessible building), and air filtration systems to certain households. Clean air rooms are rooms designed to keep levels of harmful air pollutants as low as possible during wildland fire smoke events.</p><p>Under the bill, air pollution control agencies must partner with at least one community-based organization in implementing such programs.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr566"
    },
    "title": "Cleaner Air Spaces Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cleaner Air Spaces Act of 2025</strong></p><p>This bill requires the Environmental Protection Agency to provide grants to air pollution control agencies, including at least one tribal agency with jurisdiction over air quality, to implement cleaner air space programs\u00a0(i.e., programs to provide clean air to the public during wildland fire smoke events). Generally, such programs must be located in areas at risk of exposure to wildland fire smoke and must help provide educational materials, clean air centers (i.e., one or more clean air rooms in a publicly accessible building), and air filtration systems to certain households. Clean air rooms are rooms designed to keep levels of harmful air pollutants as low as possible during wildland fire smoke events.</p><p>Under the bill, air pollution control agencies must partner with at least one community-based organization in implementing such programs.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr566"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr566ih.xml"
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
      "title": "Cleaner Air Spaces Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cleaner Air Spaces Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to provide grants to air pollution control agencies to implement a cleaner air space program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:18Z"
    }
  ]
}
```
