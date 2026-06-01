# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1828?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1828
- Title: Safe Routes Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 1828
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2025-08-19T13:35:51Z
- Update date including text: 2025-08-19T13:35:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-07-23 - Committee: Committee on Environment and Public Works Senate Subcommittee on Transportation and Infrastructure. Hearings held.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-07-23 - Committee: Committee on Environment and Public Works Senate Subcommittee on Transportation and Infrastructure. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1828",
    "number": "1828",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Safe Routes Improvement Act",
    "type": "S",
    "updateDate": "2025-08-19T13:35:51Z",
    "updateDateIncludingText": "2025-08-19T13:35:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Subcommittee",
          "systemCode": "ssev08"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works Senate Subcommittee on Transportation and Infrastructure. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T15:25:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-23T19:08:07Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Transportation and Infrastructure Subcommittee",
          "systemCode": "ssev08"
        }
      },
      "systemCode": "ssev00",
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
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1828is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1828\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Cramer (for himself and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to require States to designate a coordinator of the safe routes to school program in the State, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Routes Improvement Act .\n#### 2. Safe routes to school\n##### (a) In general\nSection 208 of title 23, United States Code, is amended by adding at the end the following:\n(j) Safe routes to school coordinator (1) In general Each State shall designate a coordinator of the safe routes to school program in the State. (2) Duties (A) In general The duty of a coordinator under paragraph (1) shall be to serve as the point of contact for the safe routes to school program in the State. (B) Limitation The Secretary may not require a coordinator under paragraph (1) to carry out any other duties except as authorized by Congress. (3) Use of existing staff A State may designate an existing employee of the State as a coordinator under paragraph (1). (4) Contact information Each State shall provide contact information for the coordinator under paragraph (1) on the website of the State department of transportation. (5) Designation of position A vacancy in the position of coordinator under paragraph (1) shall be filled by not later than 180 days after the date on which the vacancy begins. (6) Use of existing funds A State may use amounts made available under section 133(h) or section 148 for the salary of the coordinator under paragraph (1). .\n##### (b) Conforming amendment\nSection 208(g) of title 23, United States Code, is amended by striking paragraph (3).",
      "versionDate": "2025-05-21",
      "versionType": "Introduced in Senate"
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
            "name": "Child safety and welfare",
            "updateDate": "2025-08-19T13:35:18Z"
          },
          {
            "name": "Educational facilities and institutions",
            "updateDate": "2025-08-19T13:35:26Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-08-19T13:35:34Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-08-19T13:35:12Z"
          },
          {
            "name": "Transportation programs funding",
            "updateDate": "2025-08-19T13:35:43Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-08-19T13:35:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-03T13:14:44Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1828is.xml"
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
      "title": "Safe Routes Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Routes Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to require States to designate a coordinator of the safe routes to school program in the State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:24Z"
    }
  ]
}
```
