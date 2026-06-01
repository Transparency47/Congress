# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4344
- Title: Resilient LEO PNT Act
- Congress: 119
- Bill type: HR
- Bill number: 4344
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-10-01T08:05:43Z
- Update date including text: 2025-10-01T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4344",
    "number": "4344",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Resilient LEO PNT Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:05:43Z",
    "updateDateIncludingText": "2025-10-01T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "VA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4344ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4344\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Mullin (for himself and Mr. Wittman ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of the Air Force to carry out a capability demonstration project to obtain a resilient positioning, navigation, and timing capability demonstration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Resilient Low Earth Orbit Positioning, Navigation, and Timing Act or the Resilient LEO PNT Act .\n#### 2. Commercial Low Earth Orbit Resilient Positioning, Navigation, and Timing Capability Demonstration and Pathfinder Program\n##### (a) Pathfinder Program\nSubject to the availability of appropriations for such purpose, the Secretary of the Air Force shall carry out a capability demonstration project, to be known as the Commercial Low Earth Orbit Resilient Positioning, Navigation, and Timing Capability Demonstration in accordance with this section.\n##### (b) Contract with covered service provider\n**(1) Selection**\nAs soon as practicable after the date of the enactment of this Act, the Secretary shall\u2014\n**(A)**\ndevelop a list of covered service providers that can carry out a capability demonstration project with the technical capabilities described in subsection (c); and\n**(B)**\nseek to award a contract to at least one such covered service provider.\n**(2) Contract**\nThe contract awarded to a covered service provider under this subsection shall provide that such covered service provider carry out a capability demonstration project with the technical capabilities described in subsection (c) not later than 18 months after the date of the award of such contract.\n##### (c) Technical Capabilities\nThe capability demonstration delivered under subsection (b)(2) shall demonstrate a satellite system that has\u2014\n**(1)**\nthe ability to operate in the absence of Global Positioning System services;\n**(2)**\ncompatibility with user equipment that uses the civilian Global Positioning System L1 or L5 services without performing hardware modifications of receiver equipment;\n**(3)**\ngreater resistance to jamming and spoofing threats compared to existing Global Positioning System services, to an extent determined by the Secretary;\n**(4)**\nthe ability to provide timing accuracy of less than 10 nanoseconds and position accuracy of less than 30 centimeters for stationary and mobile users; and\n**(5)**\nthe ability to restore service if some or all satellites in the satellite system are disabled, in a cadence as determined by the Secretary that substantially decreases the time to service restoration compared to what is possible under existing Global Positioning System service.\n##### (d) Evaluation\nThe Secretary shall evaluate the covered service providers for the purposes of developing the list of covered service providers under subsection (b)(1) based on the requirements in section (c) and the following factors:\n**(1)**\nA demonstrated commercial business case.\n**(2)**\nTechnological readiness of space and ground network operations.\n**(3)**\nTechnological readiness of user equipment.\n**(4)**\nFeasibility of rapidly manufacturing satellites for deployment.\n**(5)**\nThe requisite authorization by the Federal Communications Commission.\n##### (e) Follow-On production contract or transaction\nNot later than 180 days after a determination by the Secretary that the capability demonstration project has been successfully completed, the Secretary shall, to the extent practicable, award a follow-on production contract or transaction (as defined in section 4022 of title 10, United States Code) to at least one covered service provider that carried out such successful capability demonstration project for the purpose of achieving operational deployment as determined by the Secretary.\n##### (f) Briefing and report\nNot later than two years after the date of the enactment of this Act, the Secretary shall provide a briefing and submit a report to the Committees on Armed Services of the House of Representatives and the Senate on the capability demonstration project described in this section that includes\u2014\n**(1)**\nthe list of covered service providers developed under subsection (b)(1);\n**(2)**\nan assessment of such providers and how the capability demonstration offered by each demonstrates the technical capabilities listed in subsection (c);\n**(3)**\nthe results of the pathfinder capability demonstration; and\n**(4)**\na strategy and timeline for deploying the system demonstration by the capability demonstration project to operational scale.\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term capability demonstration project means a prototype project pursuant to section 4022 of title 10, United States Code, that demonstrates resilient positioning, navigation, and timing capabilities by a low earth orbit system of satellites.\n**(2)**\nThe term covered service provider means a commercial entity that\u2014\n**(A)**\nhas its principal office located in the United States; and\n**(B)**\nprovides low earth orbit positioning, navigation, and timing services.\n**(3)**\nThe term nanosecond means a nanosecond in Universal Coordinated Time, as maintained by the United States Naval Observatory (UTC(USNO)).",
      "versionDate": "2025-07-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:09:27Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4344ih.xml"
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
      "title": "Resilient LEO PNT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Resilient LEO PNT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Resilient Low Earth Orbit Positioning, Navigation, and Timing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Air Force to carry out a capability demonstration project to obtain a resilient positioning, navigation, and timing capability demonstration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T07:48:22Z"
    }
  ]
}
```
