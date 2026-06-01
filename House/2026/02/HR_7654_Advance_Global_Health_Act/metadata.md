# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7654
- Title: Advance Global Health Act
- Congress: 119
- Bill type: HR
- Bill number: 7654
- Origin chamber: House
- Introduced date: 2026-02-24
- Update date: 2026-04-23T19:06:50Z
- Update date including text: 2026-04-23T19:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 41 - 2.
- Latest action: 2026-02-24: Introduced in House

## Actions

- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Introduced in House
- 2026-02-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 41 - 2.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7654",
    "number": "7654",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Advance Global Health Act",
    "type": "HR",
    "updateDate": "2026-04-23T19:06:50Z",
    "updateDateIncludingText": "2026-04-23T19:06:50Z"
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
      "text": "Ordered to be Reported by the Yeas and Nays: 41 - 2.",
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
      "actionDate": "2026-02-24",
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
      "actionDate": "2026-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-24",
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
            "date": "2026-03-26T16:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-24T15:00:30Z",
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
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7654ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7654\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2026 Mr. Lawler (for himself and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo authorize the consolidation of reports required to be submitted by the Bureau of Global Health Security and Diplomacy of the Department of State, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advance Global Health Act .\n#### 2. Authorization for consolidation\n##### (a) Annual consolidation\nOn and after the date of the enactment of this Act and except as provided in subsection (b), each report required to be submitted to Congress or to any committee of Congress that is produced by the Bureau of Global Health Security and Diplomacy of the Department of State shall be consolidated into a single annual report that is submitted not later than September 30 of each year. Such consolidated report shall be submitted in a machine-searchable format and contain all statutorily required information.\n##### (b) Exceptions\nThe consolidation required by subsection (a) shall be subject to the following exceptions:\n**(1)**\nWith respect to any report that cannot be consolidated into the annual report during the 1-year period beginning on the date of the enactment of this Act without the loss of required information, the Ambassador at Large for the Bureau of Global Health Security and Diplomacy shall include a notice in the consolidated annual report naming the excluded report and certifying that the report shall be made available on the statutorily required due date.\n**(2)**\nAny report required to be submitted on a quarterly basis and any report required in advance of the expenditure of funds related to the budget of the Department may not be consolidated into the annual report under subsection (a).\n##### (c) Rule of construction\nNothing in this Act may be construed to waive, alter, or affect any requirement to provide congressional notification.",
      "versionDate": "2026-02-24",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-23T19:06:34Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-23T19:06:41Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2026-04-23T19:06:50Z"
          },
          {
            "name": "World health",
            "updateDate": "2026-04-23T19:06:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-02-27T16:37:27Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7654ih.xml"
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
      "title": "Advance Global Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advance Global Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the consolidation of reports required to be submitted by the Bureau of Global Health Security and Diplomacy of the Department of State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T09:18:38Z"
    }
  ]
}
```
