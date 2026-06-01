# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5265
- Title: SAFE Ride Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5265
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-01-21T09:05:33Z
- Update date including text: 2026-01-21T09:05:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5265",
    "number": "5265",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "SAFE Ride Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:33Z",
    "updateDateIncludingText": "2026-01-21T09:05:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sponsorshipDate": "2026-01-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5265ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5265\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, to establish an electric bike safety program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SAFE Ride Act of 2025 .\n#### 2. Funding for electric bike safety program\n##### (a) Establishment\nThe Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, shall establish a grant program to provide funds to States that have in effect an electric bike safety program.\n##### (b) Eligibility\nTo be eligible for a grant under this section, a State shall demonstrate to the Secretary that such State\u2014\n**(1)**\nhas successful enforcement of the safety requirements for operation of shared e-bike systems;\n**(2)**\nprovides to the public educational materials or programs on helmet use and safe riding specific to e-bikes, including the use of the curricula developed under subsection (c)(2);\n**(3)**\nimplements helmet safety laws modeled after the national standards established under subsection (c)(1);\n**(4)**\ncollects data on e-bike accidents, including by requiring shared mobility operators to report such data by demographic, and report such data to the Secretary;\n**(5)**\nsupports local law enforcement efforts to implement and enforce the actions described in paragraphs (1) and (3); and\n**(6)**\nwill provide grant funding and guidance to local law enforcement entities to address unsafe underage riding, including collection of penalties, impounding of unsafe vehicles, and educational outreach.\n##### (c) National standards; safety curricula\nThe Secretary shall\u2014\n**(1)**\nestablish national standards that recommend helmet use for e-bike riders under the age of 18; and\n**(2)**\ndevelop, and make available to the public, curricula on safety of e-bike usage, including helmet safety.\n##### (d) Guidelines\nThe Secretary shall establish such guidelines as are necessary to carry out this section.",
      "versionDate": "2025-09-10",
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
        "updateDate": "2025-09-24T14:23:29Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5265ih.xml"
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
      "title": "SAFE Ride Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Ride Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration, to establish an electric bike safety program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:29Z"
    }
  ]
}
```
