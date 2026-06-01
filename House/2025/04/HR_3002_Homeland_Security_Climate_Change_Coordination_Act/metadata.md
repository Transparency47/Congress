# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3002
- Title: Homeland Security Climate Change Coordination Act
- Congress: 119
- Bill type: HR
- Bill number: 3002
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-03-03T09:05:27Z
- Update date including text: 2026-03-03T09:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-04-24 - Committee: Referred to the Subcommittee on Emergency Management and Technology.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-04-24 - Committee: Referred to the Subcommittee on Emergency Management and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3002",
    "number": "3002",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Homeland Security Climate Change Coordination Act",
    "type": "HR",
    "updateDate": "2026-03-03T09:05:27Z",
    "updateDateIncludingText": "2026-03-03T09:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Emergency Management and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-24T21:04:18Z",
              "name": "Referred to"
            }
          },
          "name": "Emergency Management and Technology Subcommittee",
          "systemCode": "hshm12"
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MS"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "LA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3002ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3002\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Goldman of New York (for himself, Mr. Thompson of Mississippi , Mr. Carter of Louisiana , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to establish a council within the Department of Homeland Security to coordinate departmental efforts to identify, address, and mitigate cross-functional impacts of global climate change with respect to the Department\u2019s programs and operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homeland Security Climate Change Coordination Act .\n#### 2. DHS climate coordinating council\n##### (a) In general\nSubtitle H of Title VIII of the Homeland Security Act of 2002 ( 6 U.S.C. 451 et seq. ) is amended by adding at the end the following new section:\n890E. Climate coordinating council. (a) Establishment There is established in the Department a council to coordinate departmental efforts to identify, address, and mitigate cross-functional impacts of global climate change with respect to the Department\u2019s programs, operations, missions, assets, and personnel (in this section referred to as the council ). (b) Size; composition The council shall be comprised of not fewer than 20 members. Such members shall include senior officials from the following: (1) The Office for Strategy, Policy, and Plans. (2) The Office of Regulatory Affairs. (3) U.S. Customs and Border Protection. (4) The Officer for Civil Rights and Civil Liberties. (5) The Federal Emergency Management Agency. (6) The Federal Law Enforcement Training Centers. (7) The Office of Intelligence and Analysis. (8) U.S. Immigration and Customs Enforcement. (9) The Management Directorate. (10) The Office of Partnership and Engagement. (11) The Office of Public Affairs. (12) The Office of Operations Coordination. (13) The Office of Privacy. (14) The Science and Technology Directorate. (15) The Transportation Security Administration. (16) The United States Coast Guard. (17) United States Citizenship and Immigration Services. (18) The United States Secret Service. (19) Any other office or component of the Department the Secretary determines appropriate. (c) Leadership The Secretary shall designate a senior official from among the entities specified in subsection (b) to lead the council. (d) Duties The council shall carry out the following: (1) Identify cross-functional impacts of global climate change with respect to the Department\u2019s programs, operations, missions, assets, and personnel. (2) Address and mitigate cross-functional impacts of global climate change to the Department by, among other things, developing risk-based climate change strategies and frameworks. (3) Make recommendations, as appropriate, for organizational and resource realignments, as necessary, to support the Department\u2019s risk-based climate change strategies and frameworks. (4) Oversee the implementation of departmental actions as required under Executive Order 14008, Tackling the Climate Crisis at Home and Abroad, and other related or successor orders. (e) Reports Not later than one year after the date of the enactment of this section and annually thereafter for ten years, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate, a report regarding the actions taken pursuant to this section. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after item relating to section 890D the following new item:\nSec. 890E. Climate coordinating council. .",
      "versionDate": "2025-04-24",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-20T12:58:29Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3002ih.xml"
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
      "title": "Homeland Security Climate Change Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homeland Security Climate Change Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to establish a council within the Department of Homeland Security to coordinate departmental efforts to identify, address, and mitigate cross-functional impacts of global climate change with respect to the Department's programs and operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:24Z"
    }
  ]
}
```
