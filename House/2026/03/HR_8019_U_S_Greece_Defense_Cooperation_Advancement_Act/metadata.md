# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8019
- Title: U.S.-Greece Defense Cooperation Advancement Act
- Congress: 119
- Bill type: HR
- Bill number: 8019
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-22T21:35:25Z
- Update date including text: 2026-05-22T21:35:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 3.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8019",
    "number": "8019",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "U.S.-Greece Defense Cooperation Advancement Act",
    "type": "HR",
    "updateDate": "2026-05-22T21:35:25Z",
    "updateDateIncludingText": "2026-05-22T21:35:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
        "item": [
          {
            "date": "2026-05-13T15:33:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-19T13:00:10Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DE"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "RI"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "GA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8019ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8019\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Pappas (for himself, Mr. Bilirakis , Ms. Titus , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo authorize International Military Education and Training Assistance for Greece.\n#### 1. Short Title\nThis Act may be cited as the U.S.-Greece Defense Cooperation Advancement Act .\n#### 2. International Military Education and Training Assistance for Greece\n##### (a) In general\nThe President is authorized to provide assistance under chapter 5 of part II of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2347 et seq. ; relating to International Military Education and Training (IMET)) to Greece for the following purposes:\n**(1)**\nTraining of future leaders.\n**(2)**\nFostering a better understanding of the United States.\n**(3)**\nEstablishing a rapport between the United States Armed Forces and Greece\u2019s military to build partnerships for the future.\n**(4)**\nEnhancing interoperability and capabilities for joint operations.\n**(5)**\nFocusing on professional military education, civilian control of the military, and protection of human rights.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to $1,800,000 for each of fiscal years 2027 through 2031 to carry out this section.",
      "versionDate": "2026-03-19",
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
        "name": "International Affairs",
        "updateDate": "2026-04-09T17:19:53Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8019ih.xml"
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
      "title": "U.S.-Greece Defense Cooperation Advancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "U.S.-Greece Defense Cooperation Advancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize International Military Education and Training Assistance for Greece.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:32Z"
    }
  ]
}
```
