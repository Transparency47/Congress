# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7430
- Title: FAIR AIR Act
- Congress: 119
- Bill type: HR
- Bill number: 7430
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-25T18:36:32Z
- Update date including text: 2026-02-25T18:36:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7430",
    "number": "7430",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "FAIR AIR Act",
    "type": "HR",
    "updateDate": "2026-02-25T18:36:32Z",
    "updateDateIncludingText": "2026-02-25T18:36:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:05:05Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7430ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7430\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Gosar (for himself and Mr. Crane ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend MAP-21 to extend the deadline for the conversion of commercial air tour aircraft operating in Grand Canyon National Park to quiet aircraft technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Air Improvements for Rural Access and Industry Resilience Act or the FAIR AIR Act .\n#### 2. Deadline for conversion to quiet technology aircraft\nSection 35001(b)(1) of the MAP-21 ( 49 U.S.C. 40128 note(b)(1)) is amended by striking Not later than 15 years after the date of enactment of this Act, and inserting Not later than December 31, 2032, .",
      "versionDate": "2026-02-09",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-02-25T18:36:32Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7430ih.xml"
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
      "title": "FAIR AIR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T08:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR AIR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Air Improvements for Rural Access and Industry Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend MAP-21 to extend the deadline for the conversion of commercial air tour aircraft operating in Grand Canyon National Park to quiet aircraft technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T08:48:31Z"
    }
  ]
}
```
