# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3221?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3221
- Title: ICELAND Act
- Congress: 119
- Bill type: HR
- Bill number: 3221
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2025-07-03T20:03:58Z
- Update date including text: 2025-07-03T20:03:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-06: Introduced in House

## Actions

- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3221",
    "number": "3221",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000597",
        "district": "1",
        "firstName": "Chellie",
        "fullName": "Rep. Pingree, Chellie [D-ME-1]",
        "lastName": "Pingree",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "ICELAND Act",
    "type": "HR",
    "updateDate": "2025-07-03T20:03:58Z",
    "updateDateIncludingText": "2025-07-03T20:03:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:03:40Z",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "NC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "GA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NV"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "TX"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3221ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3221\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Ms. Pingree (for herself and Mr. Murphy ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo include Iceland in the list of foreign states whose nationals are eligible for admission into the United States as E1 and E2 nonimmigrants if United States nationals are treated similarly by the Government of Iceland, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Iceland Commercial and Economic Leadership for Arctic and National Development Act or the ICELAND Act .\n#### 2. Nonimmigrant traders and investors\nFor purposes of clauses (i) and (ii) of section 101(a)(15)(E) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(E) ), Iceland shall be considered to be a foreign state described in such section if the Government of Iceland provides similar nonimmigrant status to nationals of the United States.",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-05-22T12:57:56Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3221ih.xml"
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
      "title": "ICELAND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ICELAND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Iceland Commercial and Economic Leadership for Arctic and National Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To include Iceland in the list of foreign states whose nationals are eligible for admission into the United States as E1 and E2 nonimmigrants if United States nationals are treated similarly by the Government of Iceland, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:48:38Z"
    }
  ]
}
```
