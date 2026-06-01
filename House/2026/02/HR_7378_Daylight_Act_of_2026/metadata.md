# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7378?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7378
- Title: Daylight Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7378
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-04-02T17:26:20Z
- Update date including text: 2026-04-02T17:26:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7378",
    "number": "7378",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "Daylight Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T17:26:20Z",
    "updateDateIncludingText": "2026-04-02T17:26:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7378ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7378\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Steube introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Calder Act to permanently adjust American time, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Daylight Act of 2026 .\n#### 2. Permanent adjustment to American time\n##### (a) In general\nSection 1 of the Act of March 19, 1918 (commonly known as the Calder Act ) ( 15 U.S.C. 261 ), is amended, in the second sentence\u2014\n**(1)**\nby striking Except as provided in section 3(a) of the Uniform Time Act of 1966 ( 15 U.S.C. 260a ), the and inserting The ;\n**(2)**\nby striking 4 hours and inserting 3.5 hours ;\n**(3)**\nby striking 5 hours and inserting 4.5 hours ;\n**(4)**\nby striking 6 hours and inserting 5.5 hours ;\n**(5)**\nby striking 7 hours and inserting 6.5 hours ;\n**(6)**\nby striking 8 hours and inserting by 7.5 hours ;\n**(7)**\nby striking 9 hours and inserting 8.5 hours ;\n**(8)**\nby striking 10 hours; and inserting 9.5 hours; ;\n**(9)**\nby striking 11 hours and inserting 10.5 hours ; and\n**(10)**\nby striking 10 hours. and inserting 10.5 hours. .\n##### (b) Repeal of daylight savings time\nSection 3 of the Uniform Time Act of 1966 ( 15 U.S.C. 260a ) is hereby repealed.\n#### 3. Effective date\nThis Act, including the amendments made by this Act, shall take effect on the day that is 90 days after the date of enactment of this Act.",
      "versionDate": "2026-02-04",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-18T17:52:23Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7378ih.xml"
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
      "title": "Daylight Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T06:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Daylight Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Calder Act to permanently adjust American time, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T06:03:26Z"
    }
  ]
}
```
