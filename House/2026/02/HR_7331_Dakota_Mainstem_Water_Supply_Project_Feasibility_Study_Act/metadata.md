# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7331?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7331
- Title: Dakota Mainstem Water Supply Project Feasibility Study Act
- Congress: 119
- Bill type: HR
- Bill number: 7331
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-04-30T08:06:45Z
- Update date including text: 2026-04-30T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-22 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-29 - Committee: Subcommittee Hearings Held
- Latest action: 2026-02-03: Introduced in House

## Actions

- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-22 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-04-29 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7331",
    "number": "7331",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
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
    "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:45Z",
    "updateDateIncludingText": "2026-04-30T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-29T18:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-04-22T19:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7331ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7331\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Mr. Johnson of South Dakota introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to the Dakota Mainstem Regional Water System service area in the States of South Dakota, Iowa, Nebraska, and Minnesota, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dakota Mainstem Water Supply Project Feasibility Study Act .\n#### 2. Definitions\nIn this Act:\n**(1) Dakota Mainstem Regional Water System**\nThe term Dakota Mainstem Regional Water System means the Dakota Mainstem Regional Water System, Inc., a nonprofit corporation established and operated substantially in accordance with the reclamation feasibility standards to serve as a non-Federal project entity for purposes of the cooperative agreement entered into under section 3(a)(1).\n**(2) Reclamation feasibility standards**\nThe term reclamation feasibility standards means the eligibility criteria and feasibility study requirements described in part 404 of title 43, Code of Federal Regulations (or successor regulations).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Dakota Mainstem water supply project feasibility study\n##### (a) Study\n**(1) In general**\nThe Secretary, in consultation with the Dakota Mainstem Regional Water System, through a cooperative agreement, may undertake a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to the Dakota Mainstem Regional Water System service area in the States of South Dakota, Iowa, Nebraska, and Minnesota.\n**(2) Requirement**\nThe study under paragraph (1) shall comply with the reclamation feasibility standards.\n##### (b) Federal share\nThe Federal share of the total costs of carrying out the feasibility study under this section shall not exceed 50 percent.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $10,000,000.\n##### (d) Termination of authority\nThe authority provided by this section expires on the date that is 10 years after the date of enactment of this Act.",
      "versionDate": "2026-02-03",
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
        "actionDate": "2026-03-17",
        "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held."
      },
      "number": "3736",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
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
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:58:43Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7331ih.xml"
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
      "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to the Dakota Mainstem Regional Water System service area in the States of South Dakota, Iowa, Nebraska, and Minnesota, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T08:33:58Z"
    }
  ]
}
```
