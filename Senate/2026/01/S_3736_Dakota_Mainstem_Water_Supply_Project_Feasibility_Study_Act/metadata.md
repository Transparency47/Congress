# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3736?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3736
- Title: Dakota Mainstem Water Supply Project Feasibility Study Act
- Congress: 119
- Bill type: S
- Bill number: 3736
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-03-30T18:23:47Z
- Update date including text: 2026-03-30T18:23:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3736",
    "number": "3736",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
    "type": "S",
    "updateDate": "2026-03-30T18:23:47Z",
    "updateDateIncludingText": "2026-03-30T18:23:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-01-29T19:22:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:26Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3736is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3736\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Rounds (for himself and Mr. Thune ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to the Dakota Mainstem Regional Water System service area in the States of South Dakota, Iowa, Nebraska, and Minnesota, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dakota Mainstem Water Supply Project Feasibility Study Act .\n#### 2. Definitions\nIn this Act:\n**(1) Dakota Mainstem Regional Water System**\nThe term Dakota Mainstem Regional Water System means the Dakota Mainstem Regional Water System, Inc., a nonprofit corporation established and operated substantially in accordance with the reclamation feasibility standards to serve as a non-Federal project entity for purposes of the cooperative agreement entered into under section 3(a)(1).\n**(2) Reclamation feasibility standards**\nThe term reclamation feasibility standards means the eligibility criteria and feasibility study requirements described in part 404 of title 43, Code of Federal Regulations (or successor regulations).\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Dakota Mainstem water supply project feasibility study\n##### (a) Study\n**(1) In general**\nThe Secretary, in consultation with the Dakota Mainstem Regional Water System, through a cooperative agreement, may undertake a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to the Dakota Mainstem Regional Water System service area in the States of South Dakota, Iowa, Nebraska, and Minnesota.\n**(2) Requirement**\nThe study under paragraph (1) shall comply with the reclamation feasibility standards.\n##### (b) Federal share\nThe Federal share of the total costs of carrying out the feasibility study under this section shall not exceed 50 percent.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $10,000,000.\n##### (d) Termination of authority\nThe authority provided by this section expires on the date that is 10 years after the date of enactment of this Act.",
      "versionDate": "2026-01-29",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-03",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "7331",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-30T18:23:19Z"
          },
          {
            "name": "Iowa",
            "updateDate": "2026-03-30T18:23:34Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2026-03-30T18:23:42Z"
          },
          {
            "name": "Nebraska",
            "updateDate": "2026-03-30T18:23:38Z"
          },
          {
            "name": "South Dakota",
            "updateDate": "2026-03-30T18:23:30Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-03-30T18:23:47Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2026-03-30T18:23:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:57:10Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3736is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dakota Mainstem Water Supply Project Feasibility Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Interior to conduct a study to determine the feasibility of constructing a project to supply municipal, rural, and industrial water to the Dakota Mainstem Regional Water System service area in the States of South Dakota, Iowa, Nebraska, and Minnesota, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:37Z"
    }
  ]
}
```
