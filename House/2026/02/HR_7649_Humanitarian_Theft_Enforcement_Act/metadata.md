# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7649
- Title: Humanitarian Theft Enforcement Act
- Congress: 119
- Bill type: HR
- Bill number: 7649
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-03-28T08:06:15Z
- Update date including text: 2026-03-28T08:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 45 - 1.
- Latest action: 2026-02-23: Introduced in House

## Actions

- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 45 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7649",
    "number": "7649",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Humanitarian Theft Enforcement Act",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:15Z",
    "updateDateIncludingText": "2026-03-28T08:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 45 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-02-23",
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
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-23",
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
            "date": "2026-03-26T16:26:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-23T17:00:30Z",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7649ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7649\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Mr. McCormick introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo ensure that persons found responsible for the unauthorized diversion or destruction of United States humanitarian assistance are liable to the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humanitarian Theft Enforcement Act .\n#### 2. Humanitarian theft enforcement\n##### (a) Liability\nNotwithstanding any other provision of law or regulation, any foreign person or entity the Secretary of State determines is responsible for the unauthorized diversion or destruction of United States humanitarian assistance, including humanitarian assistance funded by the United States that is provided by an international organization, is liable to the United States for the value of the assistance the Secretary determines was so diverted or destroyed.\n##### (b) Recovery\nUpon determining that a foreign person or entity is responsible for the unauthorized diversion or destruction of assistance in the manner described in subsection (a), the Secretary of State should take appropriate steps to recover the value of such assistance from the foreign person or entity.\n##### (c) Crediting of funds\nNotwithstanding any other provision of law, any funds received by the Secretary of State pursuant to a determination under this section may be credited to an appropriate account of the Department of State and shall remain available until expended. The Secretary of State may transfer such funds to an appropriate account of another Federal department or agency if the diverted or destroyed assistance was funded by such agency.\n##### (d) Waiver\nThe Secretary of State may waive any liability incurred pursuant to subsection (a) if the Secretary determines that such a waiver is in the national interest.",
      "versionDate": "2026-02-23",
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
        "updateDate": "2026-03-02T16:01:59Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7649ih.xml"
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
      "title": "Humanitarian Theft Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T08:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Humanitarian Theft Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T08:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that persons found responsible for the unauthorized diversion or destruction of United States humanitarian assistance are liable to the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T08:48:39Z"
    }
  ]
}
```
