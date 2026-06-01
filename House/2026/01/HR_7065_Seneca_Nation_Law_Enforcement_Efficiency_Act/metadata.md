# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7065?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7065
- Title: Seneca Nation Law Enforcement Efficiency Act
- Congress: 119
- Bill type: HR
- Bill number: 7065
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-04-02T19:00:04Z
- Update date including text: 2026-04-02T19:00:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-25 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-03-04 - Committee: Subcommittee Hearings Held
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-25 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-03-04 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7065",
    "number": "7065",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Seneca Nation Law Enforcement Efficiency Act",
    "type": "HR",
    "updateDate": "2026-04-02T19:00:04Z",
    "updateDateIncludingText": "2026-04-02T19:00:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
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
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T15:00:40Z",
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
                "date": "2026-03-04T15:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-25T15:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
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
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7065ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7065\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Langworthy introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo nullify the applicability of the Act of July 2, 1948, with respect to the reservations of the Seneca Nation of Indians in New York.\n#### 1. Short title\nThis Act may be cited as the Seneca Nation Law Enforcement Efficiency Act .\n#### 2. Nullification of effect of law\nSubject to written concurrence of the Attorney General of the United States and the Seneca Nation of Indians, the jurisdiction granted to the State of New York by the Act of July 2, 1948 (62 Stat. 1224, ch. 809; 25 U.S.C. 232 ) shall not apply with respect to the reservations of the Seneca Nation of Indians.",
      "versionDate": "2026-01-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Federal-Indian relations",
            "updateDate": "2026-04-02T18:59:51Z"
          },
          {
            "name": "Indian lands and resources rights",
            "updateDate": "2026-04-02T19:00:04Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2026-04-02T18:59:58Z"
          },
          {
            "name": "New York State",
            "updateDate": "2026-04-02T18:59:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2026-04-01T13:24:29Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7065ih.xml"
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
      "title": "Seneca Nation Law Enforcement Efficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Seneca Nation Law Enforcement Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-15T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify the applicability of the Act of July 2, 1948, with respect to the reservations of the Seneca Nation of Indians in New York.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-15T09:18:14Z"
    }
  ]
}
```
