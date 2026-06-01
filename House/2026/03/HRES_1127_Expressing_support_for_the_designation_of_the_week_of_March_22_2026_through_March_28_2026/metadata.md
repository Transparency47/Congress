# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1127?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1127
- Title: Expressing support for the designation of the week of March 22, 2026, through March 28, 2026, as "National Cleaning Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1127
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-03-26T20:07:51Z
- Update date including text: 2026-03-26T20:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-19 - IntroReferral: Submitted in House
- 2026-03-19 - IntroReferral: Submitted in House
- Latest action: 2026-03-19: Submitted in House

## Actions

- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-03-19 - IntroReferral: Submitted in House
- 2026-03-19 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1127",
    "number": "1127",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Expressing support for the designation of the week of March 22, 2026, through March 28, 2026, as \"National Cleaning Week\".",
    "type": "HRES",
    "updateDate": "2026-03-26T20:07:51Z",
    "updateDateIncludingText": "2026-03-26T20:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-19T13:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1127ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1127\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. LaHood (for himself and Mr. Krishnamoorthi ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of the week of March 22, 2026, through March 28, 2026, as National Cleaning Week .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the commitment and essential services provided by the cleaning industry in maintaining clean and sanitary conditions; and\n**(2)**\nsupports the designation of National Cleaning Week to continue to promote safe and clean environments at work, in schools, and at home.",
      "versionDate": "2026-03-19",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "247",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as \"National Cleaning Week\".",
      "type": "HRES"
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
        "name": "Commerce",
        "updateDate": "2026-03-26T20:07:51Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1127ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for the designation of the week of March 22, 2026, through March 28, 2026, as \"National Cleaning Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T08:18:20Z"
    },
    {
      "title": "Expressing support for the designation of the week of March 22, 2026, through March 28, 2026, as \"National Cleaning Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T08:06:40Z"
    }
  ]
}
```
