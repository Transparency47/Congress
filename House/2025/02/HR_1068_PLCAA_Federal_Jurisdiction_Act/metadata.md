# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1068?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1068
- Title: PLCAA Federal Jurisdiction Act
- Congress: 119
- Bill type: HR
- Bill number: 1068
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-12-05T22:50:04Z
- Update date including text: 2025-12-05T22:50:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1068",
    "number": "1068",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "PLCAA Federal Jurisdiction Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:50:04Z",
    "updateDateIncludingText": "2025-12-05T22:50:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:06:05Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "AZ"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "AZ"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1068ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1068\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Ms. Hageman (for herself, Mr. Crane , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Protection of Lawful Commerce in Arms Act to provide for the removal and dismissal of qualified civil liability actions.\n#### 1. Short title\nThis Act may be cited as the Protection of Lawful Commerce in Arms Act Federal Jurisdiction Act or the PLCAA Federal Jurisdiction Act .\n#### 2. Removal and dismissal of qualified civil liability actions\nSection 3 of the Protection of Lawful Commerce in Arms Act ( 15 U.S.C. 7902 ) is amended by adding at the end the following:\n(c) Removal and dismissal (1) Removal In any civil action in a State court in which a defendant that is a manufacturer, seller, or trade association asserts that the civil action is a qualified civil liability action, that defendant may remove the civil action to the district court of the United States for the district and division embracing the place where the civil action is pending. (2) Dismissal The district court of the United States to which a civil action is removed under paragraph (1) may\u2014 (A) determine whether the civil action is a qualified civil liability action; and (B) dismiss the civil action accordingly. .",
      "versionDate": "2025-02-06",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "484",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PLCAA Federal Jurisdiction Act",
      "type": "S"
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
            "name": "Civil actions and liability",
            "updateDate": "2025-07-03T12:53:50Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-07-03T12:54:04Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-07-03T12:54:11Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2025-07-03T12:53:55Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-07-03T12:54:17Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-07-03T12:54:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-09T11:41:29Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1068ih.xml"
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
      "title": "PLCAA Federal Jurisdiction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T02:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLCAA Federal Jurisdiction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protection of Lawful Commerce in Arms Act Federal Jurisdiction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Protection of Lawful Commerce in Arms Act to provide for the removal and dismissal of qualified civil liability actions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:18Z"
    }
  ]
}
```
