# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/428
- Title: Expressing support for the designation of May 2025 as "Moving Month".
- Congress: 119
- Bill type: HRES
- Bill number: 428
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2025-06-20T12:28:57Z
- Update date including text: 2025-06-20T12:28:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-19 - IntroReferral: Submitted in House
- 2025-05-19 - IntroReferral: Submitted in House
- Latest action: 2025-05-19: Submitted in House

## Actions

- 2025-05-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-19 - IntroReferral: Submitted in House
- 2025-05-19 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/428",
    "number": "428",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "M001233",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
        "lastName": "Messmer",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Expressing support for the designation of May 2025 as \"Moving Month\".",
    "type": "HRES",
    "updateDate": "2025-06-20T12:28:57Z",
    "updateDateIncludingText": "2025-06-20T12:28:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T16:01:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres428ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 428\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Mr. Messmer submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May 2025 as Moving Month .\nThat the House of Representatives\u2014\n**(1)**\nthanks the moving and storage industry of the United States; and\n**(2)**\npromotes the professional services of moving and storage companies by encouraging the public to recognize Moving Month .",
      "versionDate": "2025-05-19",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-06-20T12:28:57Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres428ih.xml"
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
      "title": "Expressing support for the designation of May 2025 as \"Moving Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T08:18:49Z"
    },
    {
      "title": "Expressing support for the designation of May 2025 as \"Moving Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T08:05:45Z"
    }
  ]
}
```
