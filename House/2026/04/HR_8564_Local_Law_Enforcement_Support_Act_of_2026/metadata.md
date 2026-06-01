# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8564?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8564
- Title: Local Law Enforcement Support Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8564
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-22T08:08:30Z
- Update date including text: 2026-05-22T08:08:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8564",
    "number": "8564",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000812",
        "district": "2",
        "firstName": "Ann",
        "fullName": "Rep. Wagner, Ann [R-MO-2]",
        "lastName": "Wagner",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Local Law Enforcement Support Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:30Z",
    "updateDateIncludingText": "2026-05-22T08:08:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "NE"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NY"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "CO"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8564ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8564\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mrs. Wagner (for herself and Mr. Rutherford ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo expand funding opportunities for local law enforcement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Local Law Enforcement Support Act of 2026 .\n#### 2. Funding opportunities for Byrne JAG Program and COPS\nSection 100054(5) of Public Law 119\u201321 (139 Stat. 390) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (ii), by striking and ;\n**(B)**\nin clause (iii), by striking the period and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(iv) recruiting, hiring, training, and retaining law enforcement personnel; (v) acquiring protective equipment for law enforcement personnel; (vi) increasing capacity to combat digital crimes and enhancing capabilities to support cyber investigations including the acquisition of\u2014 (I) digital forensics equipment; and (II) digital evidence analytical software; (vii) supporting the use of drone and counter-drone law enforcement operations; (viii) expanding the availability of forensic technologies and other investigative equipment including the acquisition of\u2014 (I) ballistics analysis equipment compatible with the National Integrated Ballistic Information Network; (II) rapid DNA instruments (as defined by 34 U.S.C. 40702(c)(3) ); (III) video analytics software; and (IV) open-source intelligence analytical software; and (ix) enhancing communication with and providing services to victims of violent crime. .",
      "versionDate": "2026-04-28",
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
        "updateDate": "2026-05-06T20:02:54Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8564ih.xml"
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
      "title": "Local Law Enforcement Support Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T08:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Local Law Enforcement Support Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand funding opportunities for local law enforcement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T08:18:50Z"
    }
  ]
}
```
