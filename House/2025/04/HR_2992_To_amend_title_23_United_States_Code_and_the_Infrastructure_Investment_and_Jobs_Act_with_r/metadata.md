# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2992?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2992
- Title: To amend title 23, United States Code, and the Infrastructure Investment and Jobs Act with respect to vehicle roadside crashes, work zone safety, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2992
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-04-24T08:06:54Z
- Update date including text: 2026-04-24T08:06:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-24 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-24 - Committee: Referred to the Subcommittee on Highways and Transit.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2992",
    "number": "2992",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001125",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Carter, Troy A. [D-LA-2]",
        "lastName": "Carter",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "To amend title 23, United States Code, and the Infrastructure Investment and Jobs Act with respect to vehicle roadside crashes, work zone safety, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-24T08:06:54Z",
    "updateDateIncludingText": "2026-04-24T08:06:54Z"
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
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-24T21:19:01Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
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
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IN"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NV"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "PA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MI"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2992ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2992\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Carter of Louisiana (for himself, Mr. Yakym , Ms. Titus , and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, and the Infrastructure Investment and Jobs Act with respect to vehicle roadside crashes, work zone safety, and for other purposes.\n#### 1. Vehicle and work zone roadside accidents\n##### (a) Highway Safety and Improvement Program\nSection 148(c)(2) of title 23, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)(vi) by striking and pedestrians, and inserting pedestrians, and occupants and pedestrians associated with disabled vehicles ;\n**(2)**\nin subparagraph (B)(i) by inserting , and occupants and pedestrians associated with disabled vehicles after pedestrians ; and\n**(3)**\nin subparagraph (D)(vi) by striking and pedestrians and inserting pedestrians, and occupants and pedestrians associated with disabled vehicles .\n##### (b) Injury health data\nSection 24108(c)(2) of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ) is amended by inserting , including roadside deaths and work zone deaths after fatalities .\n##### (c) Review of Move Over or Slow Down Law public awareness\nSection 24109(a) of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ) is amended by inserting or motorist, disabled vehicle, worker, vehicle or machinery in a work zone after authorized emergency vehicle .\n##### (d) Disabled vehicle crash working group\n**(1) In general**\nThe Secretary of Transportation, in conjunction with the Occupational Safety and Health Administration and other relevant agencies, shall convene a working group of industry and nongovernment entities, including representatives of high-risk communities, high traffic risk professions, such as truckers, traffic incident responders and first responders, and other relevant stakeholders, including State and local highway safety experts, insurers, medical and public health experts, law enforcement and other first responders, and technology and automobile manufacturers.\n**(2) Duties**\nThe working group convened under paragraph (1) shall collect, analyze, compile, and publish accurate, detailed data on disabled roadside vehicle crashes, along with a strategic plan to identify and implement solutions for fatal and non-fatal injury crashes, adoption of better data sharing with the National Highway Traffic Safety Administration, including local adoption of the Model Minimum Uniform Crash Criteria, and annual updates on awareness and intervention activities and results.\n##### (e) Work zone crash working group\n**(1) In general**\nThe Secretary of Transportation, in conjunction with the Occupational Safety and Health Administration, Federal Highway Administration, and other relevant agencies, shall convene a working group of industry and nongovernment entities, including contractors, pavers, engineers, construction labor unions, traffic safety industry professionals, State transportation officials, and others in the road building community.\n**(2) Duties**\nThe working group convened under paragraph (1) shall collect, analyze, compile, and publish accurate, detailed data on work zone crashes, along with a strategic plan to identify and implement solutions for fatal and non-fatal injury crashes, increased use and effectiveness of work zone safety contingency funds, adoption of better data sharing with the National Highway Traffic Safety Administration, including local adoption of the Model Minimum Uniform Crash Criteria, and annual updates on awareness and intervention activities and results.\n##### (f) Review of use and effectiveness of work zone safety contingency funds\nThe Administrator of the Federal Highways Administration shall submit to Congress an annual report on the use and effectiveness of work zone safety contingency funds described in section 120(c)(3)(B)(vi) of title 23, United States Code, that includes the following:\n**(1)**\nHow many and which States have utilized the authority to use such funds.\n**(2)**\nHow much funding each State dedicated to such funds.\n**(3)**\nAny other pertinent information about such funds and recommendations to improve the implementation of such funds nationwide.",
      "versionDate": "2025-04-24",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3871",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preventing Roadside and Work Zone Deaths Act of 2026",
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
        "updateDate": "2025-05-20T14:24:36Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2992ih.xml"
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
      "title": "To amend title 23, United States Code, and the Infrastructure Investment and Jobs Act with respect to vehicle roadside crashes, work zone safety, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:32Z"
    },
    {
      "title": "To amend title 23, United States Code, and the Infrastructure Investment and Jobs Act with respect to vehicle roadside crashes, work zone safety, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:05:42Z"
    }
  ]
}
```
