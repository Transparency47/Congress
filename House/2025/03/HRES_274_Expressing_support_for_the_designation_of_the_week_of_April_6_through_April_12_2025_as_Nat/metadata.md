# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/274
- Title: Expressing support for the designation of the week of April 6 through April 12, 2025, as "National Water Week".
- Congress: 119
- Bill type: HRES
- Bill number: 274
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2025-04-01T18:27:23Z
- Update date including text: 2025-04-01T18:27:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Submitted in House
- Latest action: 2025-03-31: Submitted in House

## Actions

- 2025-03-31 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-31 - IntroReferral: Submitted in House
- 2025-03-31 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/274",
    "number": "274",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "E000300",
        "district": "8",
        "firstName": "Gabe",
        "fullName": "Rep. Evans, Gabe [R-CO-8]",
        "lastName": "Evans",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Expressing support for the designation of the week of April 6 through April 12, 2025, as \"National Water Week\".",
    "type": "HRES",
    "updateDate": "2025-04-01T18:27:23Z",
    "updateDateIncludingText": "2025-04-01T18:27:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres274ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 274\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Evans of Colorado (for himself and Mr. Tonko ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of the week of April 6 through April 12, 2025, as National Water Week .\nThat the House of Representatives supports the designation of National Water Week .",
      "versionDate": "2025-03-31",
      "versionType": "IH"
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
        "name": "Environmental Protection",
        "updateDate": "2025-04-01T18:27:23Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres274ih.xml"
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
      "title": "Expressing support for the designation of the week of April 6 through April 12, 2025, as \"National Water Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T08:48:21Z"
    },
    {
      "title": "Expressing support for the designation of the week of April 6 through April 12, 2025, as \"National Water Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T08:05:58Z"
    }
  ]
}
```
