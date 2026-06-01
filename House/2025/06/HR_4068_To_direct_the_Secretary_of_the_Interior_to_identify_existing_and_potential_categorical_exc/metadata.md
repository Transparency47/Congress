# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4068?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4068
- Title: Streamlining NEPA for Coal Act
- Congress: 119
- Bill type: HR
- Bill number: 4068
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2025-09-10T20:28:52Z
- Update date including text: 2025-09-10T20:28:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-02 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-09-03 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-02 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-09-03 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4068",
    "number": "4068",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001129",
        "district": "10",
        "firstName": "Mike",
        "fullName": "Rep. Collins, Mike [R-GA-10]",
        "lastName": "Collins",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Streamlining NEPA for Coal Act",
    "type": "HR",
    "updateDate": "2025-09-10T20:28:52Z",
    "updateDateIncludingText": "2025-09-10T20:28:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:00:50Z",
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
                "date": "2025-09-03T13:16:26Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-07-02T13:02:15Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4068ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4068\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Collins introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to identify existing and potential categorical exclusions related to the production and export of coal.\n#### 1. Short title\nThis Act may be cited as the Streamlining NEPA for Coal Act .\n#### 2. Identification of existing and potential categorical exclusions related to the production and export of coal\nNot later than 30 days after the date of enactment of this Act, the Secretary of the Interior shall identify to the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate any existing and potential categorical exclusions pursuant to the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), increased reliance on and adoption of which by other Federal agencies pursuant to section 109 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336c ) could further the production and export of coal.",
      "versionDate": "2025-06-23",
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
            "name": "Coal",
            "updateDate": "2025-09-10T20:28:27Z"
          },
          {
            "name": "Environmental Protection Agency (EPA)",
            "updateDate": "2025-09-10T20:28:52Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-09-10T20:28:41Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-09-10T20:28:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-07-14T15:31:14Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4068ih.xml"
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
      "title": "Streamlining NEPA for Coal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-03T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining NEPA for Coal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to identify existing and potential categorical exclusions related to the production and export of coal.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-03T07:48:25Z"
    }
  ]
}
```
