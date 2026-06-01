# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3729?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3729
- Title: PBM Reporting Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 3729
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-20T18:20:13Z
- Update date including text: 2026-02-20T18:20:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3729",
    "number": "3729",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "PBM Reporting Transparency Act",
    "type": "S",
    "updateDate": "2026-02-20T18:20:13Z",
    "updateDateIncludingText": "2026-02-20T18:20:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
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
          "date": "2026-01-29T17:45:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "NV"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3729is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3729\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Warner (for himself, Mr. Tillis , Ms. Cortez Masto , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the Medicare Payment Advisory Commission (MedPAC) submit to Congress two reports on agreements with pharmacy benefit managers with respect to prescription drug plans and MA\u2013PD plans.\n#### 1. Short title\nThis Act may be cited as the PBM Reporting Transparency Act .\n#### 2. MedPAC reports on agreements with pharmacy benefit managers with respect to prescription drug plans and MA\u2013PD plans\nThe Medicare Payment Advisory Commission shall submit to Congress the following reports:\n**(1) Initial report**\nNot later than the first March 15 occurring after the date that is 2 years after the date on which the Secretary makes the data available to the Commission, a report regarding agreements with pharmacy benefit managers with respect to prescription drug plans and MA\u2013PD plans. Such report shall include, to the extent practicable\u2014\n**(A)**\na description of trends and patterns, including relevant averages, totals, and other figures for the types of information submitted;\n**(B)**\nan analysis of any differences in agreements and their effects on plan enrollee out-of-pocket spending and average pharmacy reimbursement, and other impacts; and\n**(C)**\nany recommendations the Commission determines appropriate.\n**(2) Final report**\nNot later than 2 years after the date on which the Commission submits the initial report under paragraph (1), a report describing any changes with respect to the information described in paragraph (1) over time, together with any recommendations the Commission determines appropriate.",
      "versionDate": "2026-01-29",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-02-20T18:20:13Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3729is.xml"
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
      "title": "PBM Reporting Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PBM Reporting Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Medicare Payment Advisory Commission (MedPAC) submit to Congress two reports on agreements with pharmacy benefit managers with respect to prescription drug plans and MA-PD plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:32Z"
    }
  ]
}
```
