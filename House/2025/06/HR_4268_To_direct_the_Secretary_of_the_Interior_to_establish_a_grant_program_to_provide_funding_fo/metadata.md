# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4268?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4268
- Title: Remembering Our Local Heroes Act
- Congress: 119
- Bill type: HR
- Bill number: 4268
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2026-01-31T09:05:23Z
- Update date including text: 2026-01-31T09:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4268",
    "number": "4268",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Remembering Our Local Heroes Act",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:23Z",
    "updateDateIncludingText": "2026-01-31T09:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "NH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "NJ"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4268ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4268\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Ms. Tenney (for herself and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to establish a grant program to provide funding for memorials honoring veterans, law enforcement officers, and firefighters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Remembering Our Local Heroes Act .\n#### 2. Grant program for memorials\n##### (a) In general\nNot later than 6 months after the date of the enactment of this Act, the Secretary shall establish a grant program to fund construction, restoration, renovation, and maintenance for covered memorials.\n##### (b) Eligible entities\n**(1) In general**\nIn carrying out the Program, the Secretary may award grants to units of local government and nonprofit organizations.\n**(2) Applications**\nTo be eligible for a grant under the Program, a unit of local government or nonprofit organization shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(3) Priority**\nIn awarding grants under the Program, the Secretary shall give priority to grants that will fund projects\u2014\n**(A)**\nfor which strong support is demonstrated from the local community; and\n**(B)**\nthat memorialize individuals or groups, living or deceased\u2014\n**(i)**\nwho are broadly viewed to have contributed positively, in a manner demonstrating exemplary public service, to their community or to the United States; or\n**(ii)**\nwho distinguished themselves through acts of bravery in which they risked their lives.\n##### (c) Use of funds\nGrant funds awarded under the Program may only be used for construction, restoration, renovation, or maintenance for covered memorials.\n##### (d) Limitation on grants\n**(1) In general**\nThe Secretary may not award more than 1 grant in a fiscal year with respect to any single\u2014\n**(A)**\nunit of local government or nonprofit organization; or\n**(B)**\ncovered memorial.\n**(2) Amount**\nNo grant awarded under the Program may exceed $100,000.\n##### (e) Matching requirement\n**(1) In general**\nThe recipient of a grant under the Program shall provide non-Federal matching funds equal to not less than 50 percent of the grant.\n**(2) In-kind support**\nThe non-Federal matching funds described in paragraph (1) may include in-kind support.\n##### (f) Authorization\nThere is authorized to be appropriated to the Secretary to carry out the Program $2,000,000 for each of fiscal years 2026 through 2030.\n##### (g) Definitions\nIn this section:\n**(1) Covered memorial**\n**(A) In general**\nThe term covered memorial means any statue, monument, sculpture, memorial, plaque, inscription, or other structure or landscape feature, including a garden or memorial grove that is\u2014\n**(i)**\nowned or administered by a unit of local government or nonprofit organization; and\n**(ii)**\ndesigned to perpetuate in a permanent manner the memory of individuals or groups, living or deceased, who\u2014\n**(I)**\nare veterans of the Armed Forces who served on or after April 6, 1917;\n**(II)**\nare members of the Armed Forces killed while on active duty as a result of injuries incurred in the line of duty on or after April 6, 1917;\n**(III)**\nhave served as law enforcement officers; or\n**(IV)**\nhave served as firefighters.\n**(B) Exception**\nThe term covered memorial does not include any item listed in subparagraph (A) that is located within the interior of a structure or a structure which is primarily used for other purposes.\n**(2) Program**\nThe term Program means the grant program established under this section.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(4) Unit of local government**\nThe term unit of local government means\u2014\n**(A)**\na unit of general government below the State level, including a city, county, municipality, town, township, or village;\n**(B)**\nthe Government of the District of Columbia;\n**(C)**\nthe government of, or a unit of general government within, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, the Virgin Islands of the United States, and any other territory or possession of the United States; or\n**(D)**\nthe Tribal Government of a federally recognized Indian Tribe.",
      "versionDate": "2025-06-30",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-31T16:23:28Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4268ih.xml"
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
      "title": "Remembering Our Local Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Remembering Our Local Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to establish a grant program to provide funding for memorials honoring veterans, law enforcement officers, and firefighters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T05:18:29Z"
    }
  ]
}
```
