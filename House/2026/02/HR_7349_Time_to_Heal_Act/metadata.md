# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7349?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7349
- Title: Time to Heal Act
- Congress: 119
- Bill type: HR
- Bill number: 7349
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-23T16:27:57Z
- Update date including text: 2026-02-23T16:27:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7349",
    "number": "7349",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Time to Heal Act",
    "type": "HR",
    "updateDate": "2026-02-23T16:27:57Z",
    "updateDateIncludingText": "2026-02-23T16:27:57Z"
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
          "date": "2026-02-04T15:05:25Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7349ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7349\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Barrett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to give individuals with deceased spouses the same exclusion of gain from the sale of a principal residence as is allowed to married couples, regardless of how much time has passed since such death.\n#### 1. Short title\nThis Act may be cited as the Time to Heal Act .\n#### 2. Special rule for certain home sales by individuals with deceased spouses\n##### (a) In general\nSection 121(b)(4) of the Internal Revenue Code of 1986 is amended to read as follows:\n(4) Special rule for certain sales by individuals with deceased spouses In the case of a sale or exchange of property by an individual whose spouse is deceased on the date of such sale or exchange, paragraph (1) shall be applied by substituting $500,000 for $250,000 if\u2014 (A) the requirements of paragraph (2)(A) were met immediately before such date of death, and (B) such individual has not remarried at any time after such date of death and before the close of the taxable year in which such sale occurs. .\n##### (b) Effective date\nThe amendment made by this section shall apply to sales and exchanges made in taxable years beginning after the date of the enactment of this Act.",
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
        "name": "Taxation",
        "updateDate": "2026-02-23T16:27:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7349ih.xml"
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
      "title": "Time to Heal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Time to Heal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to give individuals with deceased spouses the same exclusion of gain from the sale of a principal residence as is allowed to married couples, regardless of how much time has passed since such death.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:38Z"
    }
  ]
}
```
