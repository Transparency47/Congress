# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2313
- Title: Celestial Time Standardization Act
- Congress: 119
- Bill type: HR
- Bill number: 2313
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-04-03T20:24:46Z
- Update date including text: 2026-04-03T20:24:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2313",
    "number": "2313",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Celestial Time Standardization Act",
    "type": "HR",
    "updateDate": "2026-04-03T20:24:46Z",
    "updateDateIncludingText": "2026-04-03T20:24:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
        "item": [
          {
            "date": "2025-04-29T21:09:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-25T14:02:35Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2313ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2313\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Ms. McClellan introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the Administrator of the National Aeronautics and Space Administration to develop celestial time standardization to support future operations and infrastructure on and around the Moon and other celestial bodies other than Earth, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Celestial Time Standardization Act .\n#### 2. Celestial time standardization\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nUnited States leadership of a sustained presence on the Moon and in deep space exploration is important for advancing science, exploration, commercial growth, and international partnership;\n**(2)**\nthe Artemis and Moon to Mars program of the National Aeronautics and Space Administration (NASA) will involve governmental, commercial, academic, and international partners where there is a need for interoperability between systems;\n**(3)**\nthe use of Coordinated Universal Time has challenges when used beyond Earth at other celestial bodies, due to relativistic effects;\n**(4)**\nthe United States should lead in developing time standardization for the Moon and other celestial bodies other than Earth to support interoperability and safe and sustainable operations; and\n**(5)**\ndevelopment of such standardization will advance United States leadership in setting standards for global competitiveness, and will benefit other spacefaring countries and entities.\n##### (b) Development of celestial time standardization\nThe Administrator of NASA, in consultation with the Director of the Office of Science and Technology Policy, shall carry out the following:\n**(1)**\nEnable the development of celestial time standardization, including by leading the study and definition of a coordinated lunar time.\n**(2)**\nDevelop a strategy to implement a coordinated lunar time that would support future operations and infrastructure on and around the Moon.\n**(3)**\nIn carrying out paragraphs (1) and (2)\u2014\n**(A)**\ncoordinate with relevant Federal entities, including the Department of Commerce, the Department of Defense, the Department of State, and the Department of Transportation; and\n**(B)**\nconsult with relevant\u2014\n**(i)**\nprivate sector entities;\n**(ii)**\nacademic entities; and\n**(iii)**\ninternational standards setting bodies and international partners.\n**(4)**\nIncorporate the following features of a coordinated lunar time, to the extent practicable, in the development of the strategy developed pursuant to paragraph (2):\n**(A)**\nTraceability to Coordinated Universal Time.\n**(B)**\nAccuracy sufficient to support precision navigation and science.\n**(C)**\nResilience to loss of contact with Earth.\n**(D)**\nScalability to space environments beyond the Earth-Moon system.\n##### (c) Briefing\nNot later than two years after the date of the enactment of this Act, the Administrator of NASA shall brief the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate on the strategy developed pursuant to subsection (b)(2), including relevant plans, timelines, and resources required for the implementation of a coordinated lunar time pursuant to such strategy.",
      "versionDate": "2025-03-25",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-04",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 0."
      },
      "number": "7273",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NASA Reauthorization Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-04",
        "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "933",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NASA Transition Authorization Act of 2025",
      "type": "S"
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
            "name": "Advisory bodies",
            "updateDate": "2025-05-12T16:09:13Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-12T16:10:30Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-05-12T16:10:55Z"
          },
          {
            "name": "Spacecraft and satellites",
            "updateDate": "2025-05-12T16:11:16Z"
          },
          {
            "name": "Time and calendar",
            "updateDate": "2025-05-12T16:08:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-04-03T12:07:24Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2313ih.xml"
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
      "title": "Celestial Time Standardization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Celestial Time Standardization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the National Aeronautics and Space Administration to develop celestial time standardization to support future operations and infrastructure on and around the Moon and other celestial bodies other than Earth, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T04:18:30Z"
    }
  ]
}
```
