# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3641
- Title: Wounded Warrior Bill of Rights Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3641
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-06-20T12:48:38Z
- Update date including text: 2025-06-20T12:48:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3641",
    "number": "3641",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
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
    "title": "Wounded Warrior Bill of Rights Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-20T12:48:38Z",
    "updateDateIncludingText": "2025-06-20T12:48:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:03:00Z",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "GA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NJ"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3641ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3641\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Mast (for himself, Mr. McCormick , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo clarify and improve accountability for certain members of the Armed Forces during consideration for medical separation in the Integrated Disability Evaluation System of the Department of Defense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wounded Warrior Bill of Rights Act of 2025 .\n#### 2. Accountability for certain members of the Armed Forces during the Integrated Disability Evaluation System\n##### (a) Findings\nCongress finds the following:\n**(1)**\nMembers of the Armed Forces are the brave men and women who voluntarily put themselves in harm\u2019s way, while fighting the enemies of freedom around the world so that all citizens of the United States and countless citizens of other nations can enjoy the blessings of liberty in peace. We owe those members not only a debt of gratitude, but our willingness to ensure every single member receives excellent health care and just treatment in the medical separation process when they\u2019ve become ill or injured in the line of duty. This is critically important, not only for the present state of readiness in the Armed Forces, but for potential recruitment of future warfighters as elucidated by President George Washington when he stated, The willingness with which our young people are likely to serve in any war, no matter how justified, shall be directly proportional to how they perceive veterans of early wars were treated and appreciated by our nation. .\n**(2)**\nWounded Warriors remain members of an Armed Force under the jurisdiction of the Secretary of a military department and determinations regarding their physical ability is the responsibility of the chain of command of the member, rather than the personnel within or under the direction of the Defense Health Agency. That responsibility through the jurisdiction of the military chain of command is effective during the entirety of the process of the Integrated Disability Evaluation System of the Department of Defense, or successor system, instead of vesting for practical purposes only at the end of such process.\n**(3)**\nSection 1214 of title 10, United States Code, guarantees that [n]o member of the Armed Forces may be retired or separated for physical disability without a full and fair hearing if he demands it .\n**(4)**\nSection 1216(b) of such title grants the Secretary concerned all powers, functions, and duties incident to the determination of fitness for active duty of any member of an Armed Force under his jurisdiction .\n**(5)**\nSections 7013(b), 8013(b), and 9013(b) of such title assigns responsibility for and grants the authority necessary to conduct the administration of the morale and welfare of personnel to the Secretary of the Army, the Secretary of the Navy, and the Secretary of the Air Force respectively.\n##### (b) Declaration of policy regarding accountability for Wounded Warriors\nIt is the policy of Congress that\u2014\n**(1)**\ndeterminations of fitness for duty or physical capability to perform a military occupational specialty of a member of the Armed Forces under the jurisdiction of the Secretary of a military department are the responsibility of such Secretary;\n**(2)**\ndeterminations of fitness for a Wounded Warrior may be assessed by medical professionals outside the military department of the Wounded Warrior and may be influenced by precedents across other entities of the Department of Defense, including the Defense Health Agency, but ultimately, such determination remains a decision of the Secretary of the military department concerned;\n**(3)**\nthe full authority for a determination described in paragraph (1) or (2) resides in the military chain of command and not the chain of responsibility of the Defense Health Agency; and\n**(4)**\nat no point during the medical evaluation of a Wounded Warrior shall the Wounded Warrior be denied the protections, privileges, or right to due process afforded under the laws, regulations, or other applicable guidance of the military department of the Wounded Warrior.\n##### (c) Clarification of responsibilities regarding the Integrated Disability Evaluation System\nSubsection (i) of section 1073c of title 10, United States Code, is amended to read as follows:\n(h) Authorities reserved to Secretaries of the military departments (1) Notwithstanding the responsibilities and authorities of the Director of the Defense Health Agency with respect to the administration of military medical treatment facilities under this section, the Secretary of each military department shall maintain authority over and responsibility for any member of the Armed Forces under the jurisdiction of the military department concerned while the member is being considered by a medical evaluation board or during any other part of the implementation of the Integrated Disability Evaluation System of the Department of Defense, or successor system. (2) Responsibility of the Secretary of a military department under paragraph (1) shall include the following: (A) Responsibility for administering the morale and welfare of each member of the Armed Forces under the jurisdiction of such Secretary. (B) Responsibility for determinations of fitness for active duty of each such member. (C) Complete operational and administrative control of each such member at every stage of the implementation of the Integrated Disability Evaluation System, or successor system, from the beginning of the medical evaluation board to the conclusion of the physical evaluation board, including the authority to pause for a reasonable amount of time or completely withdraw the member from such system if the military commander with jurisdiction over the Wounded Warrior finds that any policies, procedures, regulations, or other related guidance has not been followed in the case of the member. .\n##### (d) Opportunity for due process hearing in the military chain of command\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall update the policies and procedures applicable to the implementation of the Integrated Disability Evaluation System of the Department of Defense, or successor system, to ensure that appeals made by Wounded Warriors under the jurisdiction of the Secretary concerned include (if the member demands it) a full and fair hearing on such determination, to be conducted by the Secretary concerned.\n**(2) Characterization of appeal**\nAn appeal made under paragraph (1) is separate from and in addition to any appellate options available to a Wounded Warrior under the Integrated Disability Evaluation System of the Department of Defense, or successor system.\n**(3) Timely manner**\n**(A) In general**\nUpon request by Wounded Warrior, the military commander with jurisdiction over the Wounded Warrior shall process an appeal under paragraph (1).\n**(B) Adjudication**\nNot later than 90 days after the initiation by a Wounded Warrior of an appeal under paragraph (1) the military commander with jurisdiction over the Wounded Warrior, and every echelon of command all the way up to the general court-martial convening authority if the commander denies the appeal, shall complete adjudication of the appeal.\n##### (e) Briefing\nNot later than February 1, 2026, the Secretary of Defense shall provide to the appropriate congressional committees a briefing on the status of the implementation of this section and the amendments made by this section.\n##### (f) Definitions\nIn this section:\n**(1)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services of the Senate; and\n**(B)**\nthe Committee on Armed Services of the House of Representatives.\n**(2)**\nThe term Secretary concerned has the meaning given that term in section 101 of title 10, United States Code.\n**(3)**\nThe term Wounded Warrior means a member of the Armed Forces being processed for potential medical separation at any point in the Integrated Disability Evaluation System of the Department of Defense, or successor system.",
      "versionDate": "2025-05-29",
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
        "updateDate": "2025-06-20T12:48:38Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3641ih.xml"
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
      "title": "Wounded Warrior Bill of Rights Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T08:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wounded Warrior Bill of Rights Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T08:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify and improve accountability for certain members of the Armed Forces during consideration for medical separation in the Integrated Disability Evaluation System of the Department of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T08:48:23Z"
    }
  ]
}
```
