# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/81?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/81
- Title: Authorizing the use of military force against certain Mexican cartels.
- Congress: 119
- Bill type: HJRES
- Bill number: 81
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-10-18T08:05:42Z
- Update date including text: 2025-10-18T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/81",
    "number": "81",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Authorizing the use of military force against certain Mexican cartels.",
    "type": "HJRES",
    "updateDate": "2025-10-18T08:05:42Z",
    "updateDateIncludingText": "2025-10-18T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "WI"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres81ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 81\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Steube submitted the following joint resolution; which was referred to the Committee on Foreign Affairs\nJOINT RESOLUTION\nAuthorizing the use of military force against certain Mexican cartels.\n#### 1. Authorization for the use of military force\n##### (a) Authorization for use of military force\nThe President is authorized to use the Armed Forces of the United States as the President determines necessary and appropriate against the covered cartels, any forces directly coordinated or affiliated with any covered cartel, and any successor organization or forces to any such covered cartel.\n##### (b) Covered cartel defined\nIn this resolution, the term covered cartel means the following:\n**(1)**\nTren de Aragua.\n**(2)**\nMara Salvatrucha (MS\u201313).\n**(3)**\nSinaloa Cartel.\n**(4)**\nJalisco New Generation Cartel.\n**(5)**\nNortheast Cartel.\n**(6)**\nMichoac\u00e1n family.\n**(7)**\nThe United cartels.\n**(8)**\nCartel del Golfo.\n**(9)**\nClan del Golfo.\n#### 2. Compliance with War Powers Resolution\n##### (a) Specific statutory authorization\nConsistent with section 8(a)(1) of the War Powers Resolution, the Congress declares that this section is intended to constitute specific statutory authorization within the meaning of section 5(b) of the War Powers Resolution.\n##### (b) Applicability of other requirements\nNothing in this joint resolution supersedes any requirement of the War Powers Resolution.",
      "versionDate": "2025-03-24",
      "versionType": "IH"
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
        "name": "International Affairs",
        "updateDate": "2025-05-13T17:13:32Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres81ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Authorizing the use of military force against certain Mexican cartels.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T08:18:29Z"
    },
    {
      "title": "Authorizing the use of military force against certain Mexican cartels.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T08:05:25Z"
    }
  ]
}
```
