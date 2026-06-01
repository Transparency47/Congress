# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5817
- Title: Disqualifying Dual Loyalty Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5817
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-05-20T08:08:14Z
- Update date including text: 2026-05-20T08:08:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5817",
    "number": "5817",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Disqualifying Dual Loyalty Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:14Z",
    "updateDateIncludingText": "2026-05-20T08:08:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MD"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NC"
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
      "sponsorshipDate": "2026-01-27",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5817ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5817\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Fine introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo prohibit the election to Congress of any person holding foreign citizenship.\n#### 1. Short title\nThis Act may be cited as the Disqualifying Dual Loyalty Act of 2025 .\n#### 2. Prohibition on election of any person holding foreign citizenship\nNo person, without regard to whether that person is a United States national, may be elected to the office of Representative or Senator if that person is a national of any country other than the United States.",
      "versionDate": "2025-10-24",
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
        "name": "Congress",
        "updateDate": "2025-12-03T17:47:20Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5817ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disqualifying Dual Loyalty Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T04:23:16Z"
    },
    {
      "title": "Disqualifying Dual Loyalty Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the election to Congress of any person holding foreign citizenship.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T04:18:13Z"
    }
  ]
}
```
