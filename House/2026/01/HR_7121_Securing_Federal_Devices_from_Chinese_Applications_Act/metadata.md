# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7121
- Title: Securing Federal Devices from Chinese Applications Act
- Congress: 119
- Bill type: HR
- Bill number: 7121
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-02-11T09:06:14Z
- Update date including text: 2026-02-11T09:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7121",
    "number": "7121",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Securing Federal Devices from Chinese Applications Act",
    "type": "HR",
    "updateDate": "2026-02-11T09:06:14Z",
    "updateDateIncludingText": "2026-02-11T09:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:05Z",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "NE"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7121ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7121\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Shreve (for himself and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the download or use of a Chinese application on any Federal Government device.\n#### 1. Short title\nThis Act may be cited as the Securing Federal Devices from Chinese Applications Act .\n#### 2. Chinese applications prohibited on Federal Government devices\n##### (a) Prohibition\nA covered application may not be downloaded or used on a Federal Government device, unless the head of an agency determines that such use is for ensuring appropriate and controlled access to fulfill a research or intelligence function required by law.\n##### (b) Excepted use of covered applications\nNot later than 270 days after the date of the enactment of this section, the head of each agency shall issue guidance with respect to an exception made under subsection (a)\u2014\n**(1)**\nthat ensures safeguards for cybersecurity; and\n**(2)**\nthat includes requirements for the development and documentation of risk mitigation actions for such exception.\n##### (c) Covered Application List\nNot later than 180 days after the date of the enactment of this section, and every 180 days thereafter, the Director of the Office of Management and Budget, in consultation with the Secretary of Homeland Security, the Secretary of Defense, and the Director of National Intelligence, shall issue guidance on how the list of covered applications will be created and periodically updated.\n##### (d) Deadline for removal\nThe head of each agency shall ensure that a covered application is removed from a Federal device within 60 days after the date on which the application is identified as a covered application pursuant to subsection (c).\n##### (e) Definitions\nIn this section:\n**(1) Agency**\nThe term agency \u2014\n**(A)**\nmeans any Executive department, military department, Government corporation, Government controlled corporation, or other establishment in the executive branch of the Federal Government (including the Executive Office of the President), or any independent regulatory agency; and\n**(B)**\ndoes not include the governments of the District of Columbia and of the territories and possessions of the United States, and their various subdivisions.\n**(2) Covered application**\nThe term covered application includes an application that is\u2014\n**(A)**\ndeveloped, owned, or controlled by\u2014\n**(i)**\nan entity headquartered in the People\u2019s Republic of China;\n**(ii)**\nan entity in which the government of the People\u2019s Republic of China, the Chinese Communist Party, or a person acting on their behalf, holds a controlling interest; or\n**(iii)**\na parent, subsidiary, or affiliate of such an entity; or\n**(B)**\ndetermined by the Secretary of Defense to pose an undue risk to the national security of the United States due to ownership, control, or influence by the People\u2019s Republic of China.\n**(3) Cybersecurity**\nThe term cybersecurity means the prevention of damage to, unauthorized use of, exploitation of, and, if needed, the restoration of electronic information and communications systems, and the information the systems contain, in order to strengthen the confidentiality, integrity, and availability of the systems.",
      "versionDate": "2026-01-15",
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
        "updateDate": "2026-02-06T14:33:28Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7121ih.xml"
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
      "title": "Securing Federal Devices from Chinese Applications Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Federal Devices from Chinese Applications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-04T04:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the download or use of a Chinese application on any Federal Government device.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-04T04:18:14Z"
    }
  ]
}
```
