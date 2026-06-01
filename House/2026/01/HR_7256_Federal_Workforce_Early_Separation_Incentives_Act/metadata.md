# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7256?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7256
- Title: Federal Workforce Early Separation Incentives Act
- Congress: 119
- Bill type: HR
- Bill number: 7256
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-18T15:24:53Z
- Update date including text: 2026-05-18T15:24:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7256",
    "number": "7256",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Federal Workforce Early Separation Incentives Act",
    "type": "HR",
    "updateDate": "2026-05-18T15:24:53Z",
    "updateDateIncludingText": "2026-05-18T15:24:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
            "date": "2026-02-04T14:58:01Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-27T17:30:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7256ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7256\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Langworthy introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend section 3523 of title 5, United States Code, to increase the limit on voluntary separation incentive payments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Workforce Early Separation Incentives Act .\n#### 2. Voluntary separation incentive payment limit increase\nSection 3523(b)(3) of title 5, United States Code, is amended by striking be equal to and all that follows and inserting be an amount determined by the agency head, not to exceed 6 month\u2019s pay at the rate received immediately before separation, as determined in the same manner as the limit on total severance pay under section 5595(c); .",
      "versionDate": "2026-01-27",
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
        "item": {
          "name": "Government employee pay, benefits, personnel management",
          "updateDate": "2026-05-18T15:24:53Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-03T22:08:59Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7256ih.xml"
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
      "title": "Federal Workforce Early Separation Incentives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-28T09:23:23Z"
    },
    {
      "title": "Federal Workforce Early Separation Incentives Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 3523 of title 5, United States Code, to increase the limit on voluntary separation incentive payments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-28T09:18:19Z"
    }
  ]
}
```
