# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3113
- Title: Uniform School Mapping Act
- Congress: 119
- Bill type: HR
- Bill number: 3113
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-11-01T08:05:26Z
- Update date including text: 2025-11-01T08:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3113",
    "number": "3113",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Uniform School Mapping Act",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:26Z",
    "updateDateIncludingText": "2025-11-01T08:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "TN"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "FL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MD"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "VA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-06-13",
      "state": "FL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3113ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3113\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Mast (for himself, Mr. Green of Tennessee , Mr. Whitesides , and Mr. Tony Gonzales of Texas ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit Federal funds from being obligated or expended to procure certain emergency response maps, direct the Secretary of Homeland Security to develop a strategy to procure and distribute certain emergency response maps, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uniform School Mapping Act .\n#### 2. Funding prohibition and strategy with respect to certain emergency response maps\n##### (a) Funding prohibition\n**(1) In general**\nExcept as provided in paragraph (2), Federal funds made available for fiscal year 2026 or any fiscal year thereafter may not be obligated or expended to procure an emergency response map.\n**(2) Exception**\nParagraph (1) shall not apply to an emergency response map that satisfies the following requirements:\n**(A)**\nIs in a digital file format accessible through a standard or open-source file reader or image viewer on a laptop computer, tablet computer, smartphone, or other mobile platform.\n**(B)**\nIs not stored in a data center outside of the United States.\n**(C)**\nIntegrates with software utilized by any covered public safety agency that serves the site, or portion thereof, for which such map is procured.\n**(D)**\nCan be printed and shared electronically.\n**(E)**\nDisplays information oriented true north and on a coordinate grid.\n**(F)**\nDisplays any floor of such site or such portion through overlaid, aerial imagery.\n**(G)**\nLabels any of the following features of such site or such portion, as applicable:\n**(i)**\nAn access control point.\n**(ii)**\nA central utility control or building automation system.\n**(iii)**\nA courtyard, park, or field.\n**(iv)**\nAn exterior door.\n**(v)**\nA hallway.\n**(vi)**\nA hazard.\n**(vii)**\nA key box.\n**(viii)**\nA parking area.\n**(ix)**\nA road, or other structure, that immediately surrounds such site or such portion.\n**(x)**\nA room.\n**(xi)**\nA stairwell.\n**(xii)**\nA trauma kit.\n**(H)**\nHas been verified for accuracy by a walkthrough inspection of such site or such portion.\n**(I)**\nCan be updated.\n**(J)**\nAfter any funds to procure such map are expended, is made available to the following without a subscription fee or other restriction:\n**(i)**\nThe procurer of such map.\n**(ii)**\nEach such public safety agency.\n##### (b) Strategy\n**(1) In general**\nNot later than one year after the date of the enactment of this section, the Secretary, in consultation with the heads of relevant Federal agencies and departments, shall submit to the appropriate congressional committees a strategy for the Federal Government to carry out the following:\n**(A)**\nProcure an emergency response map that satisfies the requirements described in subsection (a)(2) for any site that is owned or leased by the Federal Government and determined to be critical by the Secretary.\n**(B)**\nDistribute such map to each covered public safety agency that serves such site.\n**(2) Briefing**\nNot later than 180 days after the date on which the Secretary submits the strategy pursuant to paragraph (1), the Secretary shall brief the appropriate congressional committees on such strategy.\n##### (c) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the following:\n**(A)**\nThe Committee on Homeland Security of the House of Representatives.\n**(B)**\nThe Committee on Homeland Security and Governmental Affairs of the Senate.\n**(C)**\nThe Committee on Appropriations of the House of Representatives.\n**(D)**\nThe Committee on Appropriations of the Senate.\n**(2) Covered public safety agency**\nThe term covered public safety agency means a public safety agency of the Federal Government or a SLTT entity (as such term is defined in section 2200 of the Homeland Security Act of 2002 ( 6 U.S.C. 650 )).\n**(3) Emergency response map**\nThe term emergency response map means a map of a site, or portion thereof, to be utilized by a covered public safety agency in responding to an emergency at such site or such portion.\n**(4) Secretary**\nThe term Secretary means the Secretary of Homeland Security, acting through the Director of the Cybersecurity and Infrastructure Security Agency.\n**(5) Site**\nThe term site means a building, campus, or facility.",
      "versionDate": "2025-04-30",
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
        "updateDate": "2025-05-29T15:49:22Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3113ih.xml"
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
      "title": "Uniform School Mapping Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Uniform School Mapping Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funds from being obligated or expended to procure certain emergency response maps, direct the Secretary of Homeland Security to develop a strategy to procure and distribute certain emergency response maps, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:29Z"
    }
  ]
}
```
