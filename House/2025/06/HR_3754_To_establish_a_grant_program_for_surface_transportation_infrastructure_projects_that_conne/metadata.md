# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3754?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3754
- Title: Don’t Miss Your Flight Act
- Congress: 119
- Bill type: HR
- Bill number: 3754
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2026-01-17T09:05:58Z
- Update date including text: 2026-01-17T09:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-06 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-06 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3754",
    "number": "3754",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Don\u2019t Miss Your Flight Act",
    "type": "HR",
    "updateDate": "2026-01-17T09:05:58Z",
    "updateDateIncludingText": "2026-01-17T09:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-06-06T20:27:10Z",
                "name": "Referred to"
              }
            },
            "name": "Aviation Subcommittee",
            "systemCode": "hspw05"
          },
          {
            "activities": {
              "item": {
                "date": "2025-06-06T14:38:58Z",
                "name": "Referred to"
              }
            },
            "name": "Highways and Transit Subcommittee",
            "systemCode": "hspw12"
          }
        ]
      },
      "systemCode": "hspw00",
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
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "NJ"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3754ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3754\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Cohen (for himself and Mr. Kustoff ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish a grant program for surface transportation infrastructure projects that connect to airports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Don\u2019t Miss Your Flight Act .\n#### 2. Grants for airport connection infrastructure\n##### (a) Definitions\nIn this section:\n**(1) Public airport**\nThe term public airport has the meaning given the term in section 47102 of title 49, United States Code.\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(3) State**\nThe term State means\u2014\n**(A)**\na State;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico; and\n**(D)**\nany other territory or possession of the United States.\n##### (b) Establishment\nThe Secretary shall establish and carry out a program to provide grants to entities described in subsection (c) for projects described in subsection (d).\n##### (c) Eligible entities\nAn entity eligible to receive a grant under this section is\u2014\n**(1)**\na State;\n**(2)**\nan Indian Tribe; or\n**(3)**\na unit of local government, including a public agency (as defined in section 47102 of title 49, United States Code) that has control over a public airport.\n##### (d) Eligible projects\n**(1) In general**\nA project eligible to be carried out with a grant under this section is a project described in paragraph (2) that\u2014\n**(A)**\nconnects to a public airport;\n**(B)**\nmakes improvements on land that is on, or within 5 miles of, that public airport; and\n**(C)**\nreduces congestion, expands capacity, provides access to under-connected areas, or rehabilitates roadway, rail, or transit infrastructure (including bridges, tunnels, and rolling stock).\n**(2) Projects described**\nA project referred to in paragraph (1) is\u2014\n**(A)**\na highway or bridge project eligible for assistance under title 23, United States Code;\n**(B)**\na public transportation project eligible for assistance under chapter 53 of title 49, United States Code; or\n**(C)**\na passenger rail transportation project eligible for assistance under title 49, United States Code.\n##### (e) Application\nTo be eligible to receive a grant under this section, an entity described in subsection (b) shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n##### (f) Requirement\nOf the amounts made available for each fiscal year to carry out this section, the Secretary shall use\u2014\n**(1)**\nnot less than 50 percent for projects described in subsection (d) that connect to airports that are large hub airports (as defined in section 47102 of title 49, United States Code) as of the date of enactment of this Act; and\n**(2)**\nnot less than 30 percent for projects described in subsection (d) that connect to airports that are medium hub airports (as defined in section 47102 of title 49, United States Code) as of the date of enactment of this Act.\n##### (g) Cost-Share\n**(1) In general**\nThe Federal share of the cost of a project carried out with a grant under this section shall be determined in accordance with section 120 of title 23, United States Code.\n**(2) Non-Federal share**\nNotwithstanding any other provision of law, an eligible entity may use toward the non-Federal share of the cost of a project carried out with a grant under this section\u2014\n**(A)**\ncredit assistance under the TIFIA program (as defined in section 601(a) of title 23, United States Code), if that credit assistance was provided for a project described in paragraph (12)(G) of that section; and\n**(B)**\nany passenger facility charges (as defined in section 40117(a) of title 49, United States Code) collected by the eligible entity.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated out of the Highway Trust Fund (other than the Mass Transit Account) $1,000,000,000 for each of fiscal years 2027 through 2031 to carry out this section.",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-06-05",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1966",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Don't Miss Your Flight Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-24T13:45:52Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3754ih.xml"
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
      "title": "Don\u2019t Miss Your Flight Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Don\u2019t Miss Your Flight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program for surface transportation infrastructure projects that connect to airports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:38Z"
    }
  ]
}
```
