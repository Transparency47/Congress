# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4679?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4679
- Title: FASTER Act
- Congress: 119
- Bill type: HR
- Bill number: 4679
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-16T08:07:59Z
- Update date including text: 2026-05-16T08:07:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-07-24 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-07-24 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4679",
    "number": "4679",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "FASTER Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:59Z",
    "updateDateIncludingText": "2026-05-16T08:07:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:10:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T20:22:19Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4679ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4679\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Johnson of South Dakota (for himself and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo direct the Secretary of Homeland Security to conduct a biennial survey of tactical infrastructure along the southern border, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Furthering American Security by Tempering Environmental Regulations Act or the FASTER Act .\n#### 2. Biennial survey of tactical infrastructure along the southern border\n##### (a) Biennial surveys\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act and biennially thereafter, the Secretary of Homeland Security shall conduct a survey of existing tactical infrastructure along the southern border. Each such survey shall include the following:\n**(A)**\nA measurement of the number of miles of the southern border that are without tactical infrastructure.\n**(B)**\nA description of any deficiencies in the structure of existing tactical infrastructure along the southern border.\n**(C)**\nA description of any deficiencies in technology along the southern border.\n**(2) Reports**\n**(A) In general**\nNot later than 90 days after the conclusion of each survey under paragraph (1), the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report containing the findings and results of such survey.\n**(B) Form**\nEach report under subparagraph (A) shall be submitted in unclassified format but may include a classified annex if the Secretary of Homeland Security determines such is appropriate.\n##### (b) Implementation of certain authority\nIf the Secretary of Homeland Security determines, pursuant to a survey under subsection (a), that there is a deficiency described paragraph (1) of such subsection, the Secretary shall take such actions as may be necessary, including exercising the authority provided pursuant to paragraph (1) of section 102(c) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1103 note), to waive all legal requirements to correct in an expedited manner such a deficiency.\n##### (c) Definition\nIn this section, the term deficiency , when used with respect to tactical infrastructure or technology, means that any such tactical infrastructure or technology, as the case may be\u2014\n**(1)**\nis not operational; or\n**(2)**\ncannot serve the intended function or purpose as a result of\u2014\n**(A)**\ndamage;\n**(B)**\ndeterioration; or\n**(C)**\nunmet maintenance or repair.",
      "versionDate": "2025-07-23",
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
        "name": "Immigration",
        "updateDate": "2025-09-17T16:47:24Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4679ih.xml"
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
      "title": "FASTER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T10:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FASTER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Furthering American Security by Tempering Environmental Regulations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to conduct a biennial survey of tactical infrastructure along the southern border, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T10:03:19Z"
    }
  ]
}
```
