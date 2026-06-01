# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5795
- Title: Deportation Disclosure Act
- Congress: 119
- Bill type: HR
- Bill number: 5795
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2025-11-26T15:18:05Z
- Update date including text: 2025-11-26T15:18:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-10-21: Introduced in House

## Actions

- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5795",
    "number": "5795",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Deportation Disclosure Act",
    "type": "HR",
    "updateDate": "2025-11-26T15:18:05Z",
    "updateDateIncludingText": "2025-11-26T15:18:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:00:35Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "AZ"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5795ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5795\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo make orders of removal publicly available, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deportation Disclosure Act .\n#### 2. Publicly available orders of removal\nSection 240 of the Immigration and Nationality Act ( 8 U.S.C. 1229a ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (f); and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Publication of final orders of removal The Secretary of Homeland Security shall publish on the website of the Department of Homeland Security the name of each individual who has received a final order of removal after the date of enactment of this subsection, along with\u2014 (1) a photograph of the individual; (2) any aliases of the individual; and (3) the last known State in which the individual resided. .",
      "versionDate": "2025-10-21",
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
        "updateDate": "2025-11-26T15:18:05Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5795ih.xml"
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
      "title": "Deportation Disclosure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deportation Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make orders of removal publicly available, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-31T04:18:18Z"
    }
  ]
}
```
