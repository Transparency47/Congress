# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7771?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7771
- Title: Agency Wide Resource Synchronization and Enterprise Network for Authoritative Logistics Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7771
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-03-06T20:39:31Z
- Update date including text: 2026-03-06T20:39:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7771",
    "number": "7771",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Agency Wide Resource Synchronization and Enterprise Network for Authoritative Logistics Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-06T20:39:31Z",
    "updateDateIncludingText": "2026-03-06T20:39:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7771ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7771\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Nunn of Iowa introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Defense Production Act of 1950 to require the Chairperson of the Defense Production Act Committee to maintain a database of actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agency Wide Resource Synchronization and Enterprise Network for Authoritative Logistics Act of 2026 or the ARSENAL Act of 2026 .\n#### 2. Defense Production Act Committee database of actions\nSection 722 of the Defense Production Act of 1950 ( 50 U.S.C. 4567 ) is amended\u2014\n**(1)**\nby redesignating subsections (d) and (e) as subsections (e) and (f), respectively; and\n**(2)**\nby inserting after subsection (c) the following new subsection:\n(d) Duties The Chairperson shall maintain a database of the of priority ratings, allocations, or other assistance authorized under title I or title III, categorized by purpose. Such database shall be made available to all members of the Committee and shall allow for real-time updates by Committee members, subject to appropriate information security, confidentiality, and classification requirements, as determined by the Chairperson. .",
      "versionDate": "2026-03-03",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-06T20:39:31Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7771ih.xml"
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
      "title": "Agency Wide Resource Synchronization and Enterprise Network for Authoritative Logistics Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-04T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agency Wide Resource Synchronization and Enterprise Network for Authoritative Logistics Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-04T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Defense Production Act of 1950 to require the Chairperson of the Defense Production Act Committee to maintain a database of actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-04T09:18:58Z"
    }
  ]
}
```
