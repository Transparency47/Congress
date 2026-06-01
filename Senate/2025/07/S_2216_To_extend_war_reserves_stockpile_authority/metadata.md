# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2216?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2216
- Title: Weapons Resupply, Stockpile, and Alliance–Israel Act
- Congress: 119
- Bill type: S
- Bill number: 2216
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2025-07-29T21:54:52Z
- Update date including text: 2025-07-29T21:54:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2216",
    "number": "2216",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Weapons Resupply, Stockpile, and Alliance\u2013Israel Act",
    "type": "S",
    "updateDate": "2025-07-29T21:54:52Z",
    "updateDateIncludingText": "2025-07-29T21:54:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-09T14:39:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2216is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2216\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Banks (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo extend war reserves stockpile authority.\n#### 1. Short title\nThis Act may be cited as the Weapons Resupply, Stockpile, and Alliance\u2013Israel Act .\n#### 2. Extension of war reserves stockpile authority\nSection 12001(d) of the Department of Defense Appropriations Act, 2005 ( Public Law 108\u2013287 ; 118 Stat. 1011) is amended by striking after January 1, 2027 and inserting after January 1, 2029 .",
      "versionDate": "2025-07-09",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-07-29T21:54:52Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2216is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Weapons Resupply, Stockpile, and Alliance\u2013Israel Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Weapons Resupply, Stockpile, and Alliance\u2013Israel Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend war reserves stockpile authority.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:22Z"
    }
  ]
}
```
