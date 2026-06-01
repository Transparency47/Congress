# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1326?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1326
- Title: Denouncing corruption in all its forms.
- Congress: 119
- Bill type: HRES
- Bill number: 1326
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:18:33Z
- Update date including text: 2026-05-30T08:18:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-29 - IntroReferral: Submitted in House
- Latest action: 2026-05-29: Submitted in House

## Actions

- 2026-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1326",
    "number": "1326",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Denouncing corruption in all its forms.",
    "type": "HRES",
    "updateDate": "2026-05-30T08:18:33Z",
    "updateDateIncludingText": "2026-05-30T08:18:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
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
      "actionCode": "1025",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
          "date": "2026-05-29T16:02:15Z",
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
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1326ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1326\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2026 Mr. Crow (for himself, Ms. Ocasio-Cortez , and Mr. Levin ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nDenouncing corruption in all its forms.\nThat the House of Representatives denounces corruption in all its forms and opposes the implementation of policies that benefit special interests and corrupt politicians at the expense of the American people.",
      "versionDate": "2026-05-29",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1326ih.xml"
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
      "title": "Denouncing corruption in all its forms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:18:33Z"
    },
    {
      "title": "Denouncing corruption in all its forms.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:00Z"
    }
  ]
}
```
