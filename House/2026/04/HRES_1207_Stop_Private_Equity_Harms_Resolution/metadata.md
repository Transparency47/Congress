# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1207?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1207
- Title: Stop Private Equity Harms Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 1207
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-04-28T15:03:34Z
- Update date including text: 2026-04-28T15:03:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-22 - IntroReferral: Submitted in House
- Latest action: 2026-04-22: Submitted in House

## Actions

- 2026-04-22 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-04-22 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1207",
    "number": "1207",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stop Private Equity Harms Resolution",
    "type": "HRES",
    "updateDate": "2026-04-28T15:03:34Z",
    "updateDateIncludingText": "2026-04-28T15:03:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "actionCode": "1025",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
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
          "date": "2026-04-22T15:03:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1207ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1207\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Khanna submitted the following resolution; which was referred to the Committee on Financial Services\nRESOLUTION\nExpressing support for protecting Americans from the harmful effects of private equity.\nThat the House of Representatives recognizes the need for a comprehensive plan to protect Americans from the harmful effects of private equity which\u2014\n**(1)**\nraises staffing, safety standards, and pay in healthcare, child care, and nursing homes;\n**(2)**\nends the use of taxpayer dollars to help institutional investors buy homes, and guarantees a right to legal counsel for tenants facing eviction from private equity-owned housing;\n**(3)**\nrequires full transparency of private equity ownership and strengthens antitrust and competition reviews;\n**(4)**\nstops executives from using taxpayer dollars to unreasonably enrich themselves; and\n**(5)**\nsupports alternatives to private equity\u2014including nonprofit, community-based, cooperative, and independent providers\u2014to put people over profits in these critical sectors.",
      "versionDate": "2026-04-22",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-28T15:03:34Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1207ih.xml"
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
      "title": "Stop Private Equity Harms Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-24T23:42:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Private Equity Harms Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-24T23:42:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for protecting Americans from the harmful effects of private equity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:18:25Z"
    }
  ]
}
```
