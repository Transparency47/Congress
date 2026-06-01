# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3600?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3600
- Title: LOOTER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3600
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-09-19T17:16:14Z
- Update date including text: 2025-09-19T17:16:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3600",
    "number": "3600",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "LOOTER Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-19T17:16:14Z",
    "updateDateIncludingText": "2025-09-19T17:16:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:04:00Z",
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
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "FL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-26",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3600ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3600\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Panetta (for himself, Mr. Bean of Florida , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to provide for the punishment of larceny during natural disasters.\n#### 1. Short title\nThis Act may be cited as the Law On Offender Transgressions during Emergencies and Recovery Act of 2025 or as the LOOTER Act of 2025 .\n#### 2. Larceny during natural disasters\n##### (a) In general\nChapter _ of title 18, United States Code, is amended by adding at the end the following:\n__. Larceny during natural disasters (a) Petit larceny Whoever, during any period where any county in a State is subject to an emergency declared pursuant to section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 ), commits petit larceny in that State (as defined under the law of the State in which the offense occurred) shall be fined under this title or imprisoned not more than 1 year, or both. (b) Grand larceny Whoever, during any period where any county in a State is subject to an emergency declared pursuant to section 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5191 ), commits grand larceny in that State (as defined under the law of the State in which the offense occurred) shall be fined under this title or imprisoned not more than 5 years, or both. .\n##### (b) Clerical amendment\nThe table of sections for such chapter is amended by adding at the end the following:\n__. Larceny during natural disasters. .",
      "versionDate": "2025-05-23",
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
        "updateDate": "2025-09-19T17:16:14Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3600ih.xml"
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
      "title": "LOOTER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-29T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LOOTER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-29T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Law On Offender Transgressions during Emergencies and Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-29T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to provide for the punishment of larceny during natural disasters.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-29T04:03:16Z"
    }
  ]
}
```
