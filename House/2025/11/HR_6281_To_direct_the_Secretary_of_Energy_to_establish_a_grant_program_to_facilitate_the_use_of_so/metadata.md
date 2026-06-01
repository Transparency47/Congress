# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6281?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6281
- Title: CHARGE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6281
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-02-02T14:46:31Z
- Update date including text: 2026-02-02T14:46:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6281",
    "number": "6281",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "CHARGE Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-02T14:46:31Z",
    "updateDateIncludingText": "2026-02-02T14:46:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:00:45Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "CA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "MP"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "GU"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6281ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6281\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Smith of Washington (for himself, Mr. Valadao , Mrs. King-Hinds , Mr. Moylan , and Mr. Case ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Energy to establish a grant program to facilitate the use of solar energy systems and energy storage technologies at Federally qualified health centers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Health Access Through Resilient Grid Energy Act of 2025 or the CHARGE Act of 2025 .\n#### 2. Grant program for solar energy systems and energy storage technologies at Federally qualified health centers\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary, acting through the Assistant Secretary for Energy Efficiency and Renewable Energy of the Department of Energy, shall establish a program to award grants to eligible entities for the conduct of qualifying projects (in this section referred to as the program ).\n##### (b) Grants\n**(1) Application**\nThe Secretary may award a grant under the program if an applicant submits to the Secretary an application at such time, in such form, and containing such information as the Secretary determines appropriate, including a description of\u2014\n**(A)**\nthe qualifying project proposed to be conducted by the eligible entity using such grant amounts; and\n**(B)**\nas applicable, how the eligible entity plans to select any Federally qualified health center with respect to which such qualifying project will be conducted.\n**(2) Use of grant amounts**\nGrant amounts awarded under the program may only be used to conduct a qualifying project.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to implement the program $50,000,000 for each of fiscal years 2026 through 2030.\n##### (d) Definitions\nIn this section:\n**(1) Applicant**\nThe term applicant means an eligible entity that applies for a grant under the program.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na unit of State or local government;\n**(B)**\na Federally qualified health center;\n**(C)**\na nonprofit membership organization that operates at the national, regional, or State level and includes within its membership one or more Federally qualified health centers; or\n**(D)**\na provider consortia or network that is majority owned or majority controlled by one or more Federally qualified health centers.\n**(3) Energy storage technology**\nThe term energy storage technology has the meaning given that term in section 48E(c)(2) of the Internal Revenue Code of 1986.\n**(4) Federally qualified health center**\nThe term Federally qualified health center has the meaning given that term in section 1905(l)(2)(B) of the Social Security Act ( 42 U.S.C. 1396d(l)(2)(B) ).\n**(5) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(6) Solar energy system**\nThe term solar energy system \u2014\n**(A)**\nmeans an engineered assembly of components that capture solar radiation and convert such radiation into an energy source through technologies such as photovoltaic panels or solar thermal collectors; and\n**(B)**\nincludes any supporting infrastructure for the delivery of such energy for use.\n**(7) Qualifying project**\nThe term qualifying project means a project\u2014\n**(A)**\nto install at one or more Federally qualified health centers a solar energy system or an energy storage technology; or\n**(B)**\nto provide to one or more Federally qualified health centers technical assistance relating to the design, installation, operation, or use of a solar energy system or energy storage technology.",
      "versionDate": "2025-11-21",
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
        "updateDate": "2026-02-02T14:46:30Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6281ih.xml"
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
      "title": "CHARGE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHARGE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Health Access Through Resilient Grid Energy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Energy to establish a grant program to facilitate the use of solar energy systems and energy storage technologies at Federally qualified health centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:18Z"
    }
  ]
}
```
