# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/753?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/753
- Title: FIRE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 753
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-10-25T08:05:31Z
- Update date including text: 2025-10-25T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/753",
    "number": "753",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FIRE Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:31Z",
    "updateDateIncludingText": "2025-10-25T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "OR"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "IL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "DC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CO"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "HI"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr753ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 753\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Ms. Chu (for herself, Mrs. Kim , and Ms. Brownley ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the Administrator of the National Oceanic and Atmospheric Administration to maintain a program that improves wildfire forecasting and detection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fire Information and Reaction Enhancement Act of 2025 or the FIRE Act of 2025 .\n#### 2. Wildfire forecasting and detection\n##### (a) In general\n**(1) Establishment**\nThe Administrator of the National Oceanic and Atmospheric Administration, in collaboration with the United States weather industry and such academic entities as the Administrator considers appropriate, shall establish a program within such Administration to improve wildfire forecasting and detection.\n**(2) Goals**\nThe goals of the program under paragraph (1) shall be to develop and extend accurate wildfire forecasts and warnings in order to reduce loss of life, injury, property, and damage to the economy, with a focus on improving the following:\n**(A)**\nThe prediction of intensification and spread of wildfires.\n**(B)**\nThe forecast and communication of smoke dispersion from wildfires.\n**(C)**\nInformation dissemination and risk communication to create more effective watch and warning products.\n**(D)**\nThe early detection of wildfires to contain their growth and mitigate damages.\n**(3) Elements**\nIn order to meet the goals specified in paragraph (2), the Administrator of the National Oceanic and Atmospheric Administration is authorized to conduct development, testing, and deployment activities related to the following:\n**(A)**\nAdvanced satellite detection products.\n**(B)**\nGrid-based assessments and outlooks of fuel moisture and danger levels.\n**(C)**\nCoupled atmosphere and fire modeling systems.\n**(D)**\nSystems to link climate predictions to achievable land management decisions.\n**(E)**\nImproved spatial and temporal resolution observations in high latitudes.\n##### (b) Construction authorization\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Assistant Administrator for the Office of Oceanic and Atmospheric Research, in partnership with industry and academic partners, shall establish a program to create one or more weather research testbeds to develop improved detection of and forecast capabilities for wildfire events and their impacts.\n**(2) Resources**\nIn carrying out the program under paragraph (1), the Assistant Administrator for the Office of Oceanic and Atmospheric Research may not utilize resources for such testbeds from the National Oceanic and Atmospheric Administration cooperative institutes in existence as of the date of enactment of this Act.\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated $15,000,000 for fiscal year 2026 to carry out the program under paragraph (1).",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-03-03T17:07:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr753",
          "measure-number": "753",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr753v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fire Information and Reaction Enhancement Act of 2025 or the FIRE Act of 2025</strong></p><p>This bill establishes certain programs to improve wildfire forecasting and detection within the National Oceanic and Atmospheric Administration (NOAA).</p><p>Specifically, NOAA is directed to establish one or more weather research testbeds with industry and academic partners. (Testbeds are collaborative spaces where researchers and forecasters work together to integrate new observation systems into models, test and streamline data assimilation methods, and otherwise improve weather products and services for the benefit of the public.)</p><p>Further, NOAA is directed to establish an additional program to develop and extend accurate wildfire forecasts and warnings in order to reduce injury, loss of life, and property damage. Through this program, NOAA may develop, test, and deploy satellite detection, fuel moisture and danger assessments, and atmosphere and fire modeling, among other tools.\u00a0</p>"
        },
        "title": "FIRE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr753.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fire Information and Reaction Enhancement Act of 2025 or the FIRE Act of 2025</strong></p><p>This bill establishes certain programs to improve wildfire forecasting and detection within the National Oceanic and Atmospheric Administration (NOAA).</p><p>Specifically, NOAA is directed to establish one or more weather research testbeds with industry and academic partners. (Testbeds are collaborative spaces where researchers and forecasters work together to integrate new observation systems into models, test and streamline data assimilation methods, and otherwise improve weather products and services for the benefit of the public.)</p><p>Further, NOAA is directed to establish an additional program to develop and extend accurate wildfire forecasts and warnings in order to reduce injury, loss of life, and property damage. Through this program, NOAA may develop, test, and deploy satellite detection, fuel moisture and danger assessments, and atmosphere and fire modeling, among other tools.\u00a0</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr753"
    },
    "title": "FIRE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fire Information and Reaction Enhancement Act of 2025 or the FIRE Act of 2025</strong></p><p>This bill establishes certain programs to improve wildfire forecasting and detection within the National Oceanic and Atmospheric Administration (NOAA).</p><p>Specifically, NOAA is directed to establish one or more weather research testbeds with industry and academic partners. (Testbeds are collaborative spaces where researchers and forecasters work together to integrate new observation systems into models, test and streamline data assimilation methods, and otherwise improve weather products and services for the benefit of the public.)</p><p>Further, NOAA is directed to establish an additional program to develop and extend accurate wildfire forecasts and warnings in order to reduce injury, loss of life, and property damage. Through this program, NOAA may develop, test, and deploy satellite detection, fuel moisture and danger assessments, and atmosphere and fire modeling, among other tools.\u00a0</p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr753"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr753ih.xml"
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
      "title": "FIRE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:57Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIRE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fire Information and Reaction Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the National Oceanic and Atmospheric Administration to maintain a program that improves wildfire forecasting and detection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:21Z"
    }
  ]
}
```
