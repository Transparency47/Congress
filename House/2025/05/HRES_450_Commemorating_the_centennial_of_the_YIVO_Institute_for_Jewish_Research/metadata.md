# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/450?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/450
- Title: Commemorating the centennial of the YIVO Institute for Jewish Research.
- Congress: 119
- Bill type: HRES
- Bill number: 450
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-06-20T13:23:46Z
- Update date including text: 2025-06-20T13:23:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House
- Latest action: 2025-05-29: Submitted in House

## Actions

- 2025-05-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-29 - IntroReferral: Submitted in House
- 2025-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/450",
    "number": "450",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Commemorating the centennial of the YIVO Institute for Jewish Research.",
    "type": "HRES",
    "updateDate": "2025-06-20T13:23:46Z",
    "updateDateIncludingText": "2025-06-20T13:23:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:00:40Z",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres450ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 450\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Goldman of New York (for himself, Mr. Nadler , Ms. Clarke of New York , and Mr. Suozzi ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCommemorating the centennial of the YIVO Institute for Jewish Research.\nThat the House of Representatives\u2014\n**(1)**\ncommemorates the centennial of the YIVO Institute for Jewish Research, honoring its 100 years of dedicated service to preserving and promoting the rich history, culture, and language of East European Jewry during this Jewish American Heritage Month; and\n**(2)**\nrecognizes YIVO\u2019s invaluable historical and ongoing contributions to Jewish scholarship, Holocaust remembrance, and cultural preservation, which have profoundly enriched the intellectual and cultural fabric of the United States and the world.",
      "versionDate": "2025-05-29",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-20T13:23:46Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres450ih.xml"
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
      "title": "Commemorating the centennial of the YIVO Institute for Jewish Research.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T09:18:18Z"
    },
    {
      "title": "Commemorating the centennial of the YIVO Institute for Jewish Research.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T08:05:35Z"
    }
  ]
}
```
