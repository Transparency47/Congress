# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3848
- Title: CLOUD Aircraft Act
- Congress: 119
- Bill type: HR
- Bill number: 3848
- Origin chamber: House
- Introduced date: 2025-06-09
- Update date: 2025-07-16T15:19:12Z
- Update date including text: 2025-07-16T15:19:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-09: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-09: Introduced in House

## Actions

- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Introduced in House
- 2025-06-09 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3848",
    "number": "3848",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "CLOUD Aircraft Act",
    "type": "HR",
    "updateDate": "2025-07-16T15:19:12Z",
    "updateDateIncludingText": "2025-07-16T15:19:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-09",
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
      "actionDate": "2025-06-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T16:01:15Z",
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
      "sponsorshipDate": "2025-06-09",
      "state": "GA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "VA"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "OK"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "VA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3848ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3848\nIN THE HOUSE OF REPRESENTATIVES\nJune 9, 2025 Mr. Mills (for himself, Mr. McCormick , Mr. Vindman , Mr. Lucas , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to conduct a study on the feasibility of, and cost associated with, equipping all fixed wing and rotary wing aircraft of the Department of Defense that operate in highly trafficked domestic airspaces with air-to-air and air-to-ground collision detection systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Collision-Limiting Operational Upgrade for DOD Aircraft Act or the CLOUD Aircraft Act .\n#### 2. Department of Defense study on feasibility of equipping all military fixed wing and rotary wing aircraft with air-to-air and air-to-ground collision detection systems\n##### (a) Feasibility study required\nThe Secretary of Defense, in coordination with the Administrator of the Federal Aviation Administration, shall conduct a study on the feasibility of, and cost associated with, equipping all fixed wing and rotary wing aircraft of the Department of Defense that operate in highly trafficked domestic airspaces with air-to-air collision detection systems.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall submit to the appropriate committees of Congress a report on the results of the feasibility study required under subsection (a). Such report shall include the recommendations of the Secretary with respect to such results and a timeline for carrying out any such recommendations.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term air-to-air collision detection system \u2014\n**(A)**\nmeans an airborne system designed to detect and warn pilots of potential mid-air collisions with other aircraft equipped with transponders, allowing them to take evasive maneuvers to avoid a crash; and\n**(B)**\nis compatible with the system used by commercial aircraft that is commonly referred to as a traffic alert and collision avoidance system of a TCAS .\n**(2)**\nThe term air-to-ground collision detection system means a system that uses radar, digital terrain maps, and other sensors to warn pilots of potential collisions, and if a collision is likely, to notify the pilot through a series of alarms or to automatically take control of the aircraft to avoid the collision.\n**(3)**\nThe term appropriate committees of Congress means the Committee on Armed Services and the Committee on Transportation and Infrastructure of the House of Representatives.\n**(4)**\nThe term commercial service airport has the meaning given the term in section 47102 of title 49, United States Code.\n**(5)**\nThe term operate in highly trafficked domestic airspaces means, with respect to aircraft of the Department of Defense, that such aircraft are stationed on or near, and operate regular flight patterns within the surrounding class B, C, or D airspace of a commercial service airport.",
      "versionDate": "2025-06-09",
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
        "updateDate": "2025-07-16T15:19:12Z"
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
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3848ih.xml"
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
      "title": "CLOUD Aircraft Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLOUD Aircraft Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Collision-Limiting Operational Upgrade for DOD Aircraft Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to conduct a study on the feasibility of, and cost associated with, equipping all fixed wing and rotary wing aircraft of the Department of Defense that operate in highly trafficked domestic airspaces with air-to-air and air-to-ground collision detection systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:18Z"
    }
  ]
}
```
