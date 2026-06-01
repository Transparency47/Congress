# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6702?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6702
- Title: MOVE Act
- Congress: 119
- Bill type: HR
- Bill number: 6702
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-02-03T09:05:36Z
- Update date including text: 2026-02-03T09:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6702",
    "number": "6702",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "MOVE Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:36Z",
    "updateDateIncludingText": "2026-02-03T09:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:40:35Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6702ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6702\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Ms. Titus introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the National Highway Traffic Safety Administration to conduct a study and develop a public education program on micromobility technologies, high speed personal transportation devices, and certain road users, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Micromobility Oversight and Vulnerability Evaluation Act or the MOVE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nVulnerable road users represent a disproportionate number of highway deaths and injuries.\n**(2)**\nVulnerable road users should be informed on interactions with the built environment.\n**(3)**\nLittle is known about the impacts of micromobility transportation affecting road user safety.\n#### 3. Micromobility oversight and vulnerability evaluation\n##### (a) Study\n**(1) In general**\nThe Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, shall conduct a study on the effect of personal and platform-based micromobility technologies and high speed personal transportation devices on injuries and deaths of individuals, with a focus on children and young adults.\n**(2) Crash data**\nIn conducting the study under paragraph (1), the Secretary shall review any relevant crash data, including the technology or device type and speed involved in crashes, the type of infrastructure on which crashes occurred, and if vehicles were involved in crashes, the speed of such vehicles.\n##### (b) Best practices and public education program\nBased on the findings from the study conducted under subsection (a), the Secretary shall\u2014\n**(1)**\ndevelop best practices for nonmotorized road users with respect to micromobility technologies and high speed personal transportation devices, including best practices based on\u2014\n**(A)**\ntechnology or device type;\n**(B)**\nmotor power of the technology or device;\n**(C)**\nmaximum speed of the technology or device on a paved level surface when powered solely by a motor; and\n**(D)**\nState laws that may govern operator age, helmet use, insurance, or registration requirements;\n**(2)**\ndevelop a mobility education program containing\u2014\n**(A)**\nsuch best practices on how nonmotorized road users may safely navigate streets; and\n**(B)**\nconsumer information on\u2014\n**(i)**\nmaximum speed of the technology or device when powered solely by a motor;\n**(ii)**\nwhether the technology or device is intended by the manufacturer to be easily modified to attain speeds faster than 20 miles per hour;\n**(iii)**\nwhether the technology or device is a class 1 or class 2 electric bicycle (as defined in section 217(j) of title 23, United States Code); and\n**(iv)**\ninformation on State laws that may govern operator age, helmet use, insurance or registration requirements; and\n**(3)**\nincorporate the Safe System Approach into the best practices and education program developed under this subsection.\n##### (c) National priority safety programs\nSection 405(g)(5)(C) of title 23, United States Code, is amended\u2014\n**(1)**\nin clause (iii) by striking and at the end; and\n**(2)**\nby adding at the end the following:\n(v) nonmotorized road user safety with respect to emerging micromobility technology issues; and .\n##### (d) Definitions\nIn this section:\n**(1) High speed personal transportation device**\n**(A) In general**\nThe term high speed personal transportation device means a motor-driven cycle or any other personal transportation device intended for use on public highways that\u2014\n**(i)**\nis powered by an electric motor of greater than 750 watts; or\n**(ii)**\nhas a maximum speed of more than 20 miles per hour on a paved level surface when powered solely by a motor.\n**(B) Exclusion**\nThe term high speed personal transportation device does not included a motorcycle, passenger vehicle, or vehicle built upon a truck chassis.\n**(2) Micromobility technology**\nThe term micromobility technology means a small, low-speed, personal transportation device, including an electric bicycle (as defined in section 217(j) of title 23, United States Code), electric scooter, self-balancing electric unicycle, electric skateboard, or other similar vehicle that is\u2014\n**(A)**\nelectric or human-powered;\n**(B)**\nprimarily used for a short-distance trip or urban travel; and\n**(C)**\nhas a maximum speed of not more than 20 miles per hour on a paved level surface when powered solely by a motor.\n**(3) Nonmotorized road user**\nThe term nonmotorized road user has the meaning given such term in section 405(g) of title 23, United States Code.",
      "versionDate": "2025-12-12",
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
        "updateDate": "2026-01-08T19:42:57Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6702ih.xml"
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
      "title": "MOVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MOVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Micromobility Oversight and Vulnerability Evaluation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the National Highway Traffic Safety Administration to conduct a study and develop a public education program on micromobility technologies, high speed personal transportation devices, and certain road users, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:27Z"
    }
  ]
}
```
