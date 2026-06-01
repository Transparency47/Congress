# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7285?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7285
- Title: Bulletproof Law Enforcement Vehicles Act
- Congress: 119
- Bill type: HR
- Bill number: 7285
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-05-16T08:07:25Z
- Update date including text: 2026-05-16T08:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-02 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2026-02-02 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-02-02 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2026-02-02 - Committee: Referred to the Subcommittee on Oversight, Investigations, and Accountability.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7285",
    "number": "7285",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000594",
        "district": "23",
        "firstName": "Tony",
        "fullName": "Rep. Gonzales, Tony [R-TX-23]",
        "lastName": "Gonzales",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Bulletproof Law Enforcement Vehicles Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:25Z",
    "updateDateIncludingText": "2026-05-16T08:07:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Oversight, Investigations, and Accountability Subcommittee",
          "systemCode": "hshm09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight, Investigations, and Accountability.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:30:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2026-02-02T21:00:29Z",
                "name": "Referred to"
              }
            },
            "name": "Border Security and Enforcement Subcommittee",
            "systemCode": "hshm11"
          },
          {
            "activities": {
              "item": {
                "date": "2026-02-02T21:00:29Z",
                "name": "Referred to"
              }
            },
            "name": "Oversight, Investigations, and Accountability Subcommittee",
            "systemCode": "hshm09"
          }
        ]
      },
      "systemCode": "hshm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7285ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7285\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Tony Gonzales of Texas introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to authorize the use of certain financial assistance for vehicle security enhancement upgrades, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bulletproof Law Enforcement Vehicles Act .\n#### 2. DHS vehicle security enhancement upgrades\nSection 432 of the Homeland Security Act of 2002 ( 6 U.S.C. 240 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following new subsection:\n(e) Certain uses The Secretary shall authorize the use of financial assistance under subsection (d)(2) for vehicle security enhancement upgrades, including for bulletproof windows. .",
      "versionDate": "2026-01-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-20T16:44:33Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7285ih.xml"
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
      "title": "Bulletproof Law Enforcement Vehicles Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bulletproof Law Enforcement Vehicles Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to authorize the use of certain financial assistance for vehicle security enhancement upgrades, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:42Z"
    }
  ]
}
```
