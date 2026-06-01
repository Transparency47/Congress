# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6276
- Title: Dredging Coordination Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 6276
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-01-07T09:05:49Z
- Update date including text: 2026-01-07T09:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-22 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-22 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6276",
    "number": "6276",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Dredging Coordination Improvement Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:49Z",
    "updateDateIncludingText": "2026-01-07T09:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-22",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-22T18:28:09Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "MS"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "TX"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6276ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6276\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Mullin (for himself, Mr. Ezell , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Secretary of the Army to consult with stakeholders in determining the scope of contracts entered into for the purposes of maintenance dredging, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dredging Coordination Improvement Act .\n#### 2. Maintenance dredging requirements\n##### (a) Consultation and prioritization\nIn determining the scope and performance timeline to be included in any contract entered into on or after the date of enactment of this Act with an entity to carry out maintenance dredging, the Secretary\u2014\n**(1)**\nshall\u2014\n**(A)**\nconsult with stakeholders, including the applicable non-Federal sponsor and other relevant entities determined by the Secretary; and\n**(B)**\nthe extent practicable, prioritize the completion of maintenance dredging in waters used for commercial and navigation activities, maintenance dredging that is needed for emergencies, maintenance dredging that is needed to accommodate environmental windows (as defined by the Secretary), and maintenance dredging that supports other activities in which there is an important national interest before the completion of maintenance dredging in waters used primarily for other activities, such as recreation, or for purposes other than to facilitate commerce or navigation; and\n**(2)**\nnotwithstanding paragraph (1), may determine the scope and performance timeline to be included in such contract without consultation with stakeholders that are not a party to such contract, if the Secretary determines that an emergency exists or there is an important national interest at stake.\n##### (b) Communication\nUpon receiving information about changes with respect to the performance of maintenance dredging and determining that such changes are reasonably likely to affect the period of performance of a contract for such dredging, the Secretary shall notify the applicable non-Federal sponsor of such changes not later than the third business day after the date on which the Secretary received such information.\n##### (c) Capability numbers\nWith respect to any maintenance dredging activity, the Secretary shall, upon request, make the respective capability numbers for such activities available to the non-Federal sponsor of such activity.\n##### (d) Secretary defined\nIn this section, the term Secretary means the Secretary of the Army, acting through the Chief of Engineers",
      "versionDate": "2025-11-21",
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
        "updateDate": "2025-12-18T16:24:36Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6276ih.xml"
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
      "title": "Dredging Coordination Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dredging Coordination Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Army to consult with stakeholders in determining the scope of contracts entered into for the purposes of maintenance dredging, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T09:18:39Z"
    }
  ]
}
```
