# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5556?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5556
- Title: Flight Refund Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 5556
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-04-28T08:06:39Z
- Update date including text: 2026-04-28T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-24 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-24 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5556",
    "number": "5556",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S000168",
        "district": "27",
        "firstName": "Maria",
        "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
        "lastName": "Salazar",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Flight Refund Fairness Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:39Z",
    "updateDateIncludingText": "2026-04-28T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-24",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
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
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-24T21:48:13Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "MO"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "NV"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "FL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "CA"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
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
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "WI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5556ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5556\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Ms. Salazar (for herself, Mr. Alford , Ms. Titus , Mr. Webster of Florida , Mr. Panetta , and Ms. Van Duyne ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require air carriers to transfer funds to a ticket agent for cancelled or significantly delayed or changed flights within the time required for air carriers and ticket agents to provide refunds to passengers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flight Refund Fairness Act .\n#### 2. Refunds for cancelled or significantly delayed or changed flights\nSection 42305(e) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), in the matter preceding subparagraph (A), by striking promptly and inserting , not later than the date described in subsection (b), ; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nby striking A refund and inserting the following:\n(A) Timing In providing refunds under this subsection, a ticket agent shall provide such a refund to an individual not later than 7 days after the ticket agent receives the funds transferred by the air carrier or foreign air carrier. (B) Alternatives A refund ; and\n**(B)**\nin subparagraph (B), as designated by paragraph (2), by striking subsections (b) and and inserting subsection .",
      "versionDate": "2025-09-23",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-18T17:54:09Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5556ih.xml"
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
      "title": "Flight Refund Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flight Refund Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require air carriers to transfer funds to a ticket agent for cancelled or significantly delayed or changed flights within the time required for air carriers and ticket agents to provide refunds to passengers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:26Z"
    }
  ]
}
```
