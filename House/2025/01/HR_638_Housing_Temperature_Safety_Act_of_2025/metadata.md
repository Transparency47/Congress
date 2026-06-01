# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/638
- Title: Housing Temperature Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 638
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-04-08T15:28:42Z
- Update date including text: 2026-04-08T15:28:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/638",
    "number": "638",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Housing Temperature Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T15:28:42Z",
    "updateDateIncludingText": "2026-04-08T15:28:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-05",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr638ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 638\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require owners of covered federally assisted rental dwelling units to install temperature sensors in such units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Temperature Safety Act of 2025 .\n#### 2. Temperature Sensor Pilot Program\n##### (a) In general\nThe Secretary shall establish a temperature sensor 3-year pilot program to provide grants to public housing agencies and owners of covered federally assisted rental dwelling units to install and test the efficacy of temperature sensors in residential dwelling units to ensure such units remain in compliance with temperature requirements.\n##### (b) Application\nThe Secretary shall, not later than 180 days after the date of the enactment of this Act, establish eligibility criteria for participation in the pilot program established pursuant to subsection (a) and such criteria shall be designed to ensure\u2014\n**(1)**\nthe pilot program includes a diverse range of participants that represent different geographic regions, climate regions, unit sizes and types of housing; and\n**(2)**\nthe functionality of the temperature sensors that will be tested, including internet connectivity requirements.\n##### (c) Installation\nEach public housing agency or owner of a covered federally assisted rental dwelling unit that receives one or more temperature sensors under this Act shall, after receiving written permission from the resident of a dwelling unit, install such temperature sensor and monitor the data from such temperature sensor.\n##### (d) Collection of complaint records\n**(1) In general**\nEach public housing agency or owner of a covered federally assisted rental dwelling unit that receives one or more temperature sensors under this Act shall collect and retain information about temperature-related complaints and violations.\n**(2) Definitions**\nThe Secretary shall, not later than 180 days after the date of the enactment of this Act, define the terms temperature-related complaints and temperature-related violations for the purposes of this Act.\n##### (e) Data collection\n**(1) In general**\nData collected from temperature sensors provided to public housing agencies and owners of covered federally assisted rental dwelling units under this Act shall be retained until the Secretary notifies the public housing agency or owner that the pilot program and the evaluation of the pilot program are complete.\n**(2) Personally identifiable information**\nThe Secretary shall, not later than 180 days after the date of the enactment of this Act, establish standards for the protection of personally identifiably information collected during the pilot program by public housing agencies, owners of federally assisted rental dwelling units, and the Secretary.\n##### (f) Pilot program evaluation\n**(1) Interim evaluation**\nNot later than 12 months after the establishment of the pilot program under this Act, the Secretary shall publicly publish and submit to the Congress a report that\u2014\n**(A)**\nexamines the number of temperature-related complaints and violations in federally assisted rental dwelling units with temperature sensors, disaggregated by temperature sensor technology and climate region\u2014\n**(i)**\nthat occurred before the installation of such sensor, if known; and\n**(ii)**\nthat occurred after the installation of such sensor; and\n**(B)**\nidentifies any barriers to full utility of temperature sensor capabilities, including broadband internet access and tenant participation.\n**(2) Final evaluation**\nNot later than 36 months after the conclusion of the pilot program established by the Secretary under this Act, the Secretary shall publicly publish and submit to the Congress a report that\u2014\n**(A)**\nexamines the number of temperature-related complaints and violations in federally assisted rental dwelling units with temperature sensors, disaggregated by temperature sensor technology and climate region\u2014\n**(i)**\nthat occurred before the installation of such sensor; and\n**(ii)**\nthat occurred after the installation of such sensor;\n**(B)**\nidentifies any barriers to full utility of temperature sensor capabilities, including broadband internet access and tenant participation; and\n**(C)**\ncompare the utility of various temperature sensor technologies based on\u2014\n**(i)**\nclimate zones;\n**(ii)**\ncost;\n**(iii)**\nfeatures; and\n**(iv)**\nany other factors identified by the Secretary.\n##### (g) Definitions\nFor the purposes of this Act:\n**(1) Temperature sensor**\nThe term temperature sensor means an internet capable temperature reporting device able to measure ambient air temperature to the tenth degree Fahrenheit and Celsius.\n**(2) Covered federally assisted housing**\nThe term covered federally assisted rental dwelling unit means a residential dwelling unit that is made available for rental and for which assistance is provided, or that is part of a housing project for which assistance is provided, under\u2014\n**(A)**\nthe program for project-based rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f );\n**(B)**\nthe public housing program under the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. );\n**(C)**\nthe program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ); or\n**(D)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ).\n**(3) Owner**\nThe term owner means\u2014\n**(A)**\nwith respect to the program for project-based rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ), any private person or entity, including a cooperative, an agency of the Federal Government, or a public housing agency, having the legal right to lease or sublease dwelling units;\n**(B)**\nwith respect to public housing program under the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ), a public housing agency or an owner entity of public housing units as defined in section 905.108 of title 24, Code of Federal Regulations;\n**(C)**\nwith respect to the program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ), a private nonprofit organization as defined under section 202(k)(4) of the Housing Act of 1959; and\n**(D)**\nwith respect to the program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ), a private nonprofit organization as defined under section 811(k)(5) of section 811 of the Cranston-Gonzalez National Affordable Housing Act.\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n##### (h) Authorization of appropriations\nThere are authorized to be appropriated to the Secretary\u2014\n**(1)**\nsuch sums as may be necessary for the Secretary to provide grants to owners of covered federally assisted rental dwelling units participating in the pilot program established under this Act;\n**(2)**\nsuch sums as may be necessary for the Secretary to administer the pilot program established under this Act; and\n**(3)**\nsuch sums as may be necessary for the Secretary to provide technical assistance to owners of covered federally assisted rental dwelling units that are participating in the pilot program established under this Act.",
      "versionDate": "2025-01-22",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T15:28:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Housing for the elderly and disabled",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-13T13:42:29Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-03-13T13:42:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-02-24T19:14:58Z"
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
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr638ih.xml"
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
      "title": "Housing Temperature Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Temperature Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require owners of covered federally assisted rental dwelling units to install temperature sensors in such units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:28Z"
    }
  ]
}
```
