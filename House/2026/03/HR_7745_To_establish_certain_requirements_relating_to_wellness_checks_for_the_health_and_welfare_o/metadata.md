# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7745
- Title: To establish certain requirements relating to wellness checks for the health and welfare of certain members of the Armed Forces, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 7745
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-05-20T08:08:28Z
- Update date including text: 2026-05-20T08:08:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-03-02: Introduced in House

## Actions

- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7745",
    "number": "7745",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To establish certain requirements relating to wellness checks for the health and welfare of certain members of the Armed Forces, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:28Z",
    "updateDateIncludingText": "2026-05-20T08:08:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:01:30Z",
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
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "NC"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "FL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "TN"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "TN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "NY"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "WA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7745ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7745\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Mr. Arrington (for himself, Mr. McDowell , Mrs. Luna , Mr. Rose , Mr. Van Epps , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo establish certain requirements relating to wellness checks for the health and welfare of certain members of the Armed Forces, and for other purposes.\n#### 1. Requirements relating to wellness checks for health and welfare of certain members of the Armed Forces\n##### (a) Wellness checks\n**(1) Wellness checks required**\nThe Secretary of Defense shall issue such regulations, policies, and procedures as may be necessary to require that, whenever appropriate following a member of the Armed Forces sustaining any significant injury or illness or being on sick call, a wellness check is conducted to account for the health and welfare of such member.\n**(2) Methods of contact**\nIn conducting a wellness check for a member of the Armed Forces pursuant to paragraph (1), if the member does not respond to such check conducted via an electronic or telephone communication method, the individual conducting the check shall progress to an in-person method of contact.\n**(3) Result of failure to locate**\nIf, as a result of a wellness check conducted pursuant to paragraph (1) for a member of the Armed Forces, the individual conducting such check is unable to locate such member, the individual shall refer to the applicable regulations, policies, and procedures of the Department of Defense regarding the determination and reporting of such member as missing, absent unknown, absent without leave, or duty status-whereabouts unknown.\n##### (b) Implementation by unit commanders\nIn carrying out subsection (a), the Secretary of Defense shall ensure that each unit commander coordinates with the judge advocates assigned or attached to, or performing duty with, the unit under the command of such commander for assistance in the implementation of any regulation, policy, or procedure required under subsection (a) with respect to such unit.\n##### (c) Additional actions by unit commanders\nOn a routine basis, each unit commander shall\u2014\n**(1)**\nreview the requirements contained in the document titled Commander's Critical Information Requirements , dated January 2020, or such successor document, to ensure such requirements\u2014\n**(A)**\nhave been issued or updated during the three-year period preceding any such review;\n**(B)**\nreflect such medical issues or safety incidents of members of the Armed Forces that the commander deems sufficiently significant; and\n**(C)**\nhave been distributed to the unit under the command of such commander; and\n**(2)**\nhost confidential wellness meetings with subordinate commanders at which such commanders may discuss with one or more medical officers assigned to such unit any significant injuries or illnesses affecting members of the Armed Forces serving in or with such unit.\n##### (d) Training courses\nEach Secretary concerned, and the Secretary of Defense with respect to civilian personnel of the Department of Defense, shall develop and implement training courses to ensure each member of an Armed Force under the jurisdiction of that Secretary (or each civilian employee of the Department of Defense, respectively) is aware of the importance of accountability with respect to health and welfare and of the significant negative outcomes that may occur when accountability procedures fail. Such courses shall be offered at leadership and supervisor trainings and shall include content relating to the conduct of wellness checks in accordance with subsection (a) and other related actions.\n##### (e) Secretary concerned defined\nIn this section, the term Secretary concerned has the meaning given such term in section 101(a) of title 10, United States Code.",
      "versionDate": "2026-03-02",
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
        "actionDate": "2025-09-30",
        "text": "Received in the Senate."
      },
      "number": "3838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Streamlining Procurement for Effective Execution and Delivery and National Defense Authorization Act for Fiscal Year 2026",
      "type": "HR"
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
        "updateDate": "2026-03-19T20:08:46Z"
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
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7745ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish certain requirements relating to wellness checks for the health and welfare of certain members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T04:48:29Z"
    },
    {
      "title": "To establish certain requirements relating to wellness checks for the health and welfare of certain members of the Armed Forces, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T09:05:27Z"
    }
  ]
}
```
