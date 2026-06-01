# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7772?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7772
- Title: LIGHT Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 7772
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-24T20:07:08Z
- Update date including text: 2026-03-24T20:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-03 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7772",
    "number": "7772",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "LIGHT Safety Act",
    "type": "HR",
    "updateDate": "2026-03-24T20:07:08Z",
    "updateDateIncludingText": "2026-03-24T20:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-03T17:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7772ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7772\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Ms. Perez introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Transportation to revise the Federal Motor Vehicle Safety Standards to establish a maximum allowable brightness standard for low beam headlamps on motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Limiting Intense Glare for Highway and Two-lane Safety Act or the LIGHT Safety Act .\n#### 2. Lamps, reflective devices, and associated equipment\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue a final rule to revise Federal Motor Vehicle Safety Standard Number 108 (49 C.F.R. 571.108; relating to lamps, reflective devices, and associated equipment) to establish a maximum allowable brightness standard for low beam headlamps on motor vehicles that is expressed in lumens or another appropriate (as determined by the Secretary) photometric measurement.\n##### (b) Secretary defined\nIn this section, the term Secretary means the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration.",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-24T20:07:08Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7772ih.xml"
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
      "title": "LIGHT Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIGHT Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Limiting Intense Glare for Highway and Two-lane Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to revise the Federal Motor Vehicle Safety Standards to establish a maximum allowable brightness standard for low beam headlamps on motor vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:21Z"
    }
  ]
}
```
