# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5669?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5669
- Title: PAW Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5669
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-11-21T16:15:53Z
- Update date including text: 2025-11-21T16:15:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5669",
    "number": "5669",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "PAW Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-21T16:15:53Z",
    "updateDateIncludingText": "2025-11-21T16:15:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "WY"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5669ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5669\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Van Drew (for himself, Ms. Hageman , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the surviving spouse filing status to individuals whose spouses have died within the last five taxable years.\n#### 1. Short title\nThis Act may be cited as the Protect American Widows Act of 2025 or the PAW Act of 2025 .\n#### 2. Surviving spouse definition expanded\n##### (a) In general\nSection 2(a)(1)(A) of the Internal Revenue Code of 1986 is amended by striking two taxable years and inserting five taxable years .\n##### (b) Effective date\nThe amendments made by this section shall apply to returns filed for taxable years beginning after December 31, 2024.",
      "versionDate": "2025-09-30",
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
        "name": "Taxation",
        "updateDate": "2025-11-21T16:15:53Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5669ih.xml"
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
      "title": "PAW Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAW Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect American Widows Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the surviving spouse filing status to individuals whose spouses have died within the last five taxable years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T05:48:32Z"
    }
  ]
}
```
