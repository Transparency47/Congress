# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8460
- Title: Territorial Protection and Sovereignty Act
- Congress: 119
- Bill type: HR
- Bill number: 8460
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-06T20:34:28Z
- Update date including text: 2026-05-06T20:34:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8460",
    "number": "8460",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001116",
        "district": "9",
        "firstName": "Andrew",
        "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
        "lastName": "Clyde",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Territorial Protection and Sovereignty Act",
    "type": "HR",
    "updateDate": "2026-05-06T20:34:28Z",
    "updateDateIncludingText": "2026-05-06T20:34:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:03:05Z",
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "GA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "SC"
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
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8460ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8460\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Clyde (for himself, Mr. Fine , Mr. Carter of Georgia , Ms. Mace , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to repeal the authority to grant temporary protected status, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Territorial Protection and Sovereignty Act .\n#### 2. Repeal of temporary protected status\n##### (a) Repeal\nSection 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ) is repealed.\n##### (b) Existing grants\n**(1) In general**\nAny grant of temporary protected status that is in effect on the date of enactment of this Act shall terminate on the date of enactment of this Act.\n**(2) Departure**\nAn alien whose temporary protected status is terminated under paragraph (1) shall depart the United States not later than 60 days after the date of enactment of this Act, and shall cease to be considered lawfully present in the United States on and after the date that is 60 days after the date of enactment of this Act.",
      "versionDate": "2026-04-23",
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
        "name": "Immigration",
        "updateDate": "2026-05-06T20:34:27Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8460ih.xml"
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
      "title": "Territorial Protection and Sovereignty Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Territorial Protection and Sovereignty Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to repeal the authority to grant temporary protected status, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:28Z"
    }
  ]
}
```
