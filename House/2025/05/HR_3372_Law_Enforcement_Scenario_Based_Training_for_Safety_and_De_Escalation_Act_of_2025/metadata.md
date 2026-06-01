# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3372
- Title: Law Enforcement Scenario-Based Training for Safety and De-Escalation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3372
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2025-05-23T14:23:47Z
- Update date including text: 2025-05-23T14:23:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H2059)
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H2059)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3372",
    "number": "3372",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Law Enforcement Scenario-Based Training for Safety and De-Escalation Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-23T14:23:47Z",
    "updateDateIncludingText": "2025-05-23T14:23:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2059)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NE"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MD"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3372ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3372\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mrs. Sykes (for herself, Mr. Fitzpatrick , Mr. Bacon , and Mr. Ivey ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo develop a scenario-based training curriculum for law enforcement personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Law Enforcement Scenario-Based Training for Safety and De-Escalation Act of 2025 .\n#### 2. Law enforcement scenario-based training curriculum\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Attorney General, acting through the Director of the Office of Community Oriented Policing Services, shall develop a scenario-based training curriculum for use in accordance with the grant program under section 3.\n##### (b) Curriculum\nIn developing the curriculum under subsection (a), the Attorney General shall\u2014\n**(1)**\ndevelop a scenario-based training curriculum that addresses\u2014\n**(A)**\nimproving community-police relations;\n**(B)**\nofficer safety;\n**(C)**\nofficer resilience;\n**(D)**\nsituational awareness;\n**(E)**\nphysical and emotional responses to stress;\n**(F)**\ncritical decision making and problem solving;\n**(G)**\nde-escalation;\n**(H)**\nuse of force and deadly force; and\n**(I)**\ncrisis intervention;\n**(2)**\nconsult with relevant professional law enforcement associations, community-based organizations, and defense and national security agencies in the development and dissemination of the curriculum;\n**(3)**\nprovide expertise and technical assistance to entities seeking to implement the curriculum;\n**(4)**\nevaluate best practices of scenario-based training methods and curriculum content to maintain state-of-the-art expertise in scenario-based learning methodology; and\n**(5)**\ndevelop a certification process for entities that have successfully implemented the curriculum.\n#### 3. Law enforcement scenario-based training grant program\n##### (a) In general\nBeginning on the date that is 1 year after the date of enactment of this Act, the Attorney General, acting through the Director of the Office of Community Oriented Policing Services, shall be authorized to make grants to States, units of local government, Indian Tribal governments, other public and private entities, and multi-jurisdictional or regional consortia to provide law enforcement personnel with access to a scenario-based training curriculum that is substantially similar to the curriculum developed under section 2.\n##### (b) Application\nAn applicant seeking a grant under this section shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may reasonably require.\n##### (c) Reports\n**(1) Grantee reports**\nOn the date that is 1 year after receiving a grant under this section, each grant recipient shall submit to the Attorney General a report on\u2014\n**(A)**\nany benefits of, and barriers to, delivering the curriculum to law enforcement personnel; and\n**(B)**\nrecommendations for improving the access of law enforcement personnel to scenario-based training.\n**(2) Office of Community Oriented Policing Services reports**\nNot later than 1 year after initially awarding grants under this section, and annually thereafter, the Attorney General, acting through the Director of the Office of Community Oriented Policing Services, shall submit to Congress a report on\u2014\n**(A)**\nthe number of entities that received grants under this section;\n**(B)**\nthe cumulative number and proportion of law enforcement personnel in each State that received training under the scenario-based training curriculum described in section 2, or a curriculum that is substantially similar to that curriculum;\n**(C)**\nany benefits of, and barriers to, delivering such curriculum to law enforcement personnel;\n**(D)**\nrecommendations for improving the curriculum developed under section 2; and\n**(E)**\nrecommendations for improving the grant program under this section.\n##### (d) Funding\nNo additional funds are authorized to be appropriated to carry out this Act. The Attorney General shall carry out this Act using unobligated amounts that are otherwise made available to the Department of Justice.\n#### 4. Definitions\nIn this Act:\n**(1) Community-based organizations**\nThe term community-based organization means a grassroots organization that\u2014\n**(A)**\nworks in communities to improve police accountability and transparency; and\n**(B)**\nhas a national presence and membership.\n**(2) Professional law enforcement association**\nThe term professional law enforcement association means a law enforcement membership association that works for the needs of Federal, State, local, or Indian Tribal law enforcement groups and with the civilian community on matters of common interest.\n**(3) Scenario-based training**\nThe term scenario-based training means the use of live-action simulations and role playing to place law enforcement personnel in an interactive learning environment to replicate real-life scenarios or teach particular skills or techniques.\n**(4) State**\nThe term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, and any possession of the United States.",
      "versionDate": "2025-05-13",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-23T14:23:47Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3372ih.xml"
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
      "title": "Law Enforcement Scenario-Based Training for Safety and De-Escalation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Law Enforcement Scenario-Based Training for Safety and De-Escalation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To develop a scenario-based training curriculum for law enforcement personnel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:29Z"
    }
  ]
}
```
