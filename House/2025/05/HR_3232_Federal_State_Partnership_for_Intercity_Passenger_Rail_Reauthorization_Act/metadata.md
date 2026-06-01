# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3232?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3232
- Title: Federal-State Partnership for Intercity Passenger Rail Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 3232
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2025-09-10T08:06:33Z
- Update date including text: 2025-09-10T08:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-07 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-05-07: Introduced in House

## Actions

- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-07 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3232",
    "number": "3232",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Federal-State Partnership for Intercity Passenger Rail Reauthorization Act",
    "type": "HR",
    "updateDate": "2025-09-10T08:06:33Z",
    "updateDateIncludingText": "2025-09-10T08:06:33Z"
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
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
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
          "date": "2025-05-07T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-07T21:24:05Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NV"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3232ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3232\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Cohen (for himself, Ms. Titus , and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to authorize appropriations for the Federal-State partnership for intercity passenger rail grant program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal-State Partnership for Intercity Passenger Rail Reauthorization Act .\n#### 2. Authorization of appropriations for Federal-State partnership for intercity passenger rail grants\nSection 24911(h) of title 49, United States Code, is amended to read as follows:\n(h) Authorization of appropriations (1) In general There is authorized to be appropriated to the Secretary for use carrying out this section $7,500,000,000 for each of fiscal years 2027 through 2031, to remain available until expended. (2) Project management oversight expenses The Secretary may use up to 2 percent of amounts appropriated under paragraph (1) in a fiscal year to carry out project management oversight with respect to any grant program under this title authorized to be carried out in such fiscal year. .",
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
        "updateDate": "2025-05-22T16:06:04Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3232ih.xml"
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
      "title": "To amend title 49, United States Code, to authorize appropriations for the Federal-State partnership for intercity passenger rail grant program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:24Z"
    },
    {
      "title": "Federal-State Partnership for Intercity Passenger Rail Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T03:39:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal-State Partnership for Intercity Passenger Rail Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    }
  ]
}
```
