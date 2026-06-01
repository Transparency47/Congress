# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6414?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6414
- Title: CARE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6414
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-05T16:43:13Z
- Update date including text: 2026-01-05T16:43:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6414",
    "number": "6414",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "T000165",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
        "lastName": "Tiffany",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "CARE Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-05T16:43:13Z",
    "updateDateIncludingText": "2026-01-05T16:43:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:05:20Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "WI"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "WI"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "TN"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6414ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6414\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Tiffany (for himself, Mr. Wied , Mr. Van Orden , Mr. Ogles , and Mr. Gooden ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo limit resettlement in certain States or localities.\n#### 1. Short title\nThis Act may be cited as the Community Assent for Refugee Entry Act of 2025 or the CARE Act of 2025 .\n#### 2. Limitation on refugee resettlement\nSection 412 of the Immigration and Nationality Act ( 8 U.S.C. 1522 ) is amended by adding at the end the following:\n(g) Limitation on resettlement Notwithstanding any other provision of this section, for a fiscal year, the resettlement of any refugee may not be provided for\u2014 (1) in any State where the Governor of that State, or the State legislature, has taken any action formally disapproving of resettlement in that State; or (2) in any locality where the chief executive of that locality\u2019s government, or the local legislature, has taken any action formally disapproving of resettlement in that locality. .",
      "versionDate": "2025-12-03",
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
        "updateDate": "2026-01-05T16:43:13Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6414ih.xml"
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
      "title": "CARE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Assent for Refugee Entry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit resettlement in certain States or localities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T08:18:29Z"
    }
  ]
}
```
