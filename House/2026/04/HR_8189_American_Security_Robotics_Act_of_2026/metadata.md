# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8189
- Title: American Security Robotics Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8189
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-20T23:35:08Z
- Update date including text: 2026-04-20T23:35:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8189",
    "number": "8189",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001196",
        "district": "21",
        "firstName": "Elise",
        "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
        "lastName": "Stefanik",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "American Security Robotics Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-20T23:35:08Z",
    "updateDateIncludingText": "2026-04-20T23:35:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:33:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8189ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8189\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Ms. Stefanik introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit executive agencies from procuring or operating certain unmanned ground vehicle systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Security Robotics Act of 2026 .\n#### 2. Prohibition on the procurement and operation of covered unmanned ground vehicle systems\n##### (a) Definitions\nIn this section:\n**(1) Covered nation**\nThe term covered nation has the meaning given the term in section 4872(f) of title 10, United States Code.\n**(2) Covered foreign entity**\nThe term covered foreign entity means an entity that is\u2014\n**(A)**\ndomiciled in a covered nation;\n**(B)**\nsubject to the influence or control of the government of a covered nation, as determined by the Secretary of Homeland Security or the Secretary of Defense; or\n**(C)**\na subsidiary or affiliate of an entity described in subparagraph (A) or (B).\n**(3) Covered unmanned ground vehicle system**\nThe term covered unmanned ground vehicle system means an unmanned ground vehicle system manufactured or assembled by a covered foreign entity.\n**(4) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(5) Unmanned ground vehicle system**\nThe term unmanned ground vehicle system means a system that includes\u2014\n**(A)**\na mechanical device, including a remote surveillance vehicle, autonomous patrol technology, mobile robotics, or a humanoid robot, that\u2014\n**(i)**\nis capable of locomotion, navigation, or movement on the ground; and\n**(ii)**\noperates at a distance from a human operator or supervisor based on commands or in response to sensor data or any combination thereof;\n**(B)**\nthe payload of the mechanical device described in subparagraph (A); and\n**(C)**\nany external device used to control the mechanical device described in subparagraph (A).\n##### (b) Prohibition on procurement of covered unmanned ground vehicle systems\nExcept as provided under subsection (e), the head of an executive agency may not procure any covered unmanned ground vehicle system.\n##### (c) Prohibition on operation of covered unmanned ground vehicle systems\n**(1) In general**\nExcept as provided in subsection (e), beginning on the date that is one year after the date of the enactment of this Act, no executive agency may operate a covered unmanned ground vehicle system.\n**(2) Applicability to contracted services**\nThe prohibition under paragraph (1) applies to any covered unmanned ground vehicle system being used by an executive agency through a contract for the services of the covered unmanned ground vehicle system.\n##### (d) Prohibition on use of Federal funds for procurement or operation of covered unmanned ground vehicle systems\nExcept as provided in subsection (e), beginning on the date that is one year after the date of the enactment of this Act, no Federal funds awarded through a contract, grant, or cooperative agreement, or otherwise made available, may be used to procure or in connection with the operation of a covered unmanned ground vehicle system.\n##### (e) Exemption to prohibitions\n**(1) In general**\nThe head of an agency described in paragraph (2) is exempt from the prohibitions under subsections (b), (c), and (d) if\u2014\n**(A)**\nthe procurement or operation of the covered unmanned ground vehicle system is in the national interest of the United States; and\n**(B)**\n**(i)**\nthe sole purpose for the procurement or operation is\u2014\n**(I)**\nresearch, evaluation, training, testing, or analysis for electronic warfare, information warfare operations, cybersecurity, or the development of unmanned ground vehicle system or counter-unmanned ground vehicle system technology; or\n**(II)**\nconducting counter-terrorism or counterintelligence activities, protective missions, or Federal criminal or national security investigations, including forensic examinations; or\n**(ii)**\nthe covered unmanned ground vehicle system, as procured or as modified after procurement but before operational use\u2014\n**(I)**\ncan no longer transfer data to, or download data from, a covered foreign entity; and\n**(II)**\nposes no national security cybersecurity risk as determined by the head of the agency.\n**(2) Agencies described**\nThe agencies described in this paragraph are\u2014\n**(A)**\nthe Department of Homeland Security;\n**(B)**\nthe Department of Defense;\n**(C)**\nthe Department of State; and\n**(D)**\nthe Department of Justice.",
      "versionDate": "2026-04-02",
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
        "actionDate": "2026-03-26",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "4235",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "American Security Robotics Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-13T21:13:35Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8189ih.xml"
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
      "title": "American Security Robotics Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Security Robotics Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit executive agencies from procuring or operating certain unmanned ground vehicle systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:26Z"
    }
  ]
}
```
