# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/335
- Title: Supporting the designation of the week of April 21 through April 25, 2025, as "National Home Visiting Week".
- Congress: 119
- Bill type: HRES
- Bill number: 335
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-05-29T12:57:25Z
- Update date including text: 2025-05-29T12:57:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-17 - IntroReferral: Submitted in House
- 2025-04-17 - IntroReferral: Submitted in House
- Latest action: 2025-04-17: Submitted in House

## Actions

- 2025-04-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-17 - IntroReferral: Submitted in House
- 2025-04-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/335",
    "number": "335",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
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
    "title": "Supporting the designation of the week of April 21 through April 25, 2025, as \"National Home Visiting Week\".",
    "type": "HRES",
    "updateDate": "2025-05-29T12:57:25Z",
    "updateDateIncludingText": "2025-05-29T12:57:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
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
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:32:05Z",
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "IL"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "IN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres335ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 335\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. LaHood (for himself, Mr. Davis of Illinois , Mr. Yakym , and Ms. Chu ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the designation of the week of April 21 through April 25, 2025, as National Home Visiting Week .\nThat the House of Representatives supports\u2014\n**(1)**\nthe designation of National Home Visiting Week ; and\n**(2)**\nthe goals and ideals of National Home Visiting Week.",
      "versionDate": "2025-04-17",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-05-20T14:48:14Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-05-20T14:48:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-05-29T12:57:25Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres335ih.xml"
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
      "title": "Supporting the designation of the week of April 21 through April 25, 2025, as \"National Home Visiting Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T08:18:20Z"
    },
    {
      "title": "Supporting the designation of the week of April 21 through April 25, 2025, as \"National Home Visiting Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T08:05:42Z"
    }
  ]
}
```
