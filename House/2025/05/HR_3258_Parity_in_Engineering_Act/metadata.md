# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3258
- Title: Parity in Engineering Act
- Congress: 119
- Bill type: HR
- Bill number: 3258
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-06-12T08:06:45Z
- Update date including text: 2025-06-12T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-07 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-07 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3258",
    "number": "3258",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Parity in Engineering Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:06:45Z",
    "updateDateIncludingText": "2025-06-12T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-07T21:19:48Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MN"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "MN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3258ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3258\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Stauber (for himself and Ms. Craig ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to remove the exclusion of the State of Minnesota from certain contracting for engineering and design services requirements.\n#### 1. Short title\nThis Act may be cited as the Parity in Engineering Act .\n#### 2. Contracting for engineering and design services\nSection 112(b)(2)(F) of title 23, United States Code, is amended by striking the States of West Virginia or Minnesota and inserting the State of West Virginia .",
      "versionDate": "2025-05-07",
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
        "updateDate": "2025-05-22T16:06:42Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3258ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to remove the exclusion of the State of Minnesota from certain contracting for engineering and design services requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:18Z"
    },
    {
      "title": "Parity in Engineering Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parity in Engineering Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:23Z"
    }
  ]
}
```
