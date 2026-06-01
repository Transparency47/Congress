# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7191
- Title: Fatigued Pilot Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 7191
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-02-02T14:35:22Z
- Update date including text: 2026-02-02T14:35:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7191",
    "number": "7191",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Fatigued Pilot Protection Act",
    "type": "HR",
    "updateDate": "2026-02-02T14:35:22Z",
    "updateDateIncludingText": "2026-02-02T14:35:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:02:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7191ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7191\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Ms. Scholten (for herself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Aviation Administration to update regulations relating to the application of certain flight and duty limitations and rest requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fatigued Pilot Protection Act .\n#### 2. Flight and duty limitations and rest requirements applicability\nNot later than 180 days after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall update such regulations as are necessary to ensure that the flight and duty limitations and rest requirements described in part 117 of title 14, Code of Federal Regulations, shall apply to any flightcrew member or certificate holder conducting any operation under part 121 of such title.",
      "versionDate": "2026-01-21",
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
        "updateDate": "2026-02-02T14:35:22Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7191ih.xml"
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
      "title": "Fatigued Pilot Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fatigued Pilot Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-28T07:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Aviation Administration to update regulations relating to the application of certain flight and duty limitations and rest requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-28T07:48:22Z"
    }
  ]
}
```
