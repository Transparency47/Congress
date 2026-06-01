# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1311?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1311
- Title: Expressing support for the designation of May 2026 as "Necrotizing Fasciitis Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1311
- Origin chamber: House
- Introduced date: 2026-05-21
- Update date: 2026-05-22T10:18:38Z
- Update date including text: 2026-05-22T10:18:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-21: Introduced in House
- 2026-05-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-21 - IntroReferral: Submitted in House
- Latest action: 2026-05-21: Submitted in House

## Actions

- 2026-05-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-21 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1311",
    "number": "1311",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of May 2026 as \"Necrotizing Fasciitis Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-22T10:18:38Z",
    "updateDateIncludingText": "2026-05-22T10:18:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-21",
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
      "actionCode": "1025",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
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
          "date": "2026-05-21T14:05:40Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1311ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1311\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2026 Mr. Harder of California submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May 2026 as Necrotizing Fasciitis Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Necrotizing Fasciitis Awareness Month ;\n**(2)**\nencourages Federal, State, and local agencies, health care providers, and community organizations to promote awareness of necrotizing fasciitis;\n**(3)**\nurges increased public education on the early signs and symptoms of necrotizing fasciitis to improve timely diagnosis and treatment; and\n**(4)**\nexpresses support for patients, survivors, families, and caregivers affected by necrotizing fasciitis.",
      "versionDate": "2026-05-21",
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
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1311ih.xml"
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
      "title": "Expressing support for the designation of May 2026 as \"Necrotizing Fasciitis Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T10:18:38Z"
    },
    {
      "title": "Expressing support for the designation of May 2026 as \"Necrotizing Fasciitis Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T08:08:38Z"
    }
  ]
}
```
