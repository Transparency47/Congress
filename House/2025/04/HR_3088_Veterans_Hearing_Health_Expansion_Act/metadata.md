# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3088?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3088
- Title: Veterans Hearing Health Expansion Act
- Congress: 119
- Bill type: HR
- Bill number: 3088
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-12-12T09:07:26Z
- Update date including text: 2025-12-12T09:07:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3088",
    "number": "3088",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Veterans Hearing Health Expansion Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:26Z",
    "updateDateIncludingText": "2025-12-12T09:07:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-12T15:46:33Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3088ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3088\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Barrett introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to include licensed hearing aid specialists under the Veterans Community Care Program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Hearing Health Expansion Act .\n#### 2. Inclusion of licensed hearing aid specialists in Veterans Community Care Program of the Department of Veterans Affairs\nSection 1703(c) of title 38, United States Code, is amended by\u2014\n**(1)**\nredesignating paragraphs (2) through (5) as paragraphs (3) through (6), respectively; and\n**(2)**\nby inserting after paragraph (1) the following new paragraph:\n(2) A hearing aid specialist licensed to furnish medical services in the State in which such hearing aid specialist is located. .",
      "versionDate": "2025-04-30",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:56:53Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3088ih.xml"
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
      "title": "Veterans Hearing Health Expansion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Hearing Health Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to include licensed hearing aid specialists under the Veterans Community Care Program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:26Z"
    }
  ]
}
```
