# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/783?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/783
- Title: Reaffirming German-American friendship and supporting continued cooperation between the United States and Germany.
- Congress: 119
- Bill type: HRES
- Bill number: 783
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-11-19T19:43:30Z
- Update date including text: 2025-11-19T19:43:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House
- Latest action: 2025-09-30: Submitted in House

## Actions

- 2025-09-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/783",
    "number": "783",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Reaffirming German-American friendship and supporting continued cooperation between the United States and Germany.",
    "type": "HRES",
    "updateDate": "2025-11-19T19:43:30Z",
    "updateDateIncludingText": "2025-11-19T19:43:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres783ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 783\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Thompson of Pennsylvania (for himself and Mr. Keating ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nReaffirming German-American friendship and supporting continued cooperation between the United States and Germany.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and highlights the importance of the alliance between the United States and Germany in\u2014\n**(A)**\nan enduring shared commitment to our free and democratic societies;\n**(B)**\nexpanding and deepening economic prosperity for the United States and Europe; and\n**(C)**\nprotecting and defending our security, freedom, and common values;\n**(2)**\nrecognizes the strong personal, cultural, and historical ties between our populations and governments, and the importance of our common set of fundamental values as guiding principles for tackling the growing global challenges of the 21st century; and\n**(3)**\nreaffirms the deep and historical friendship between the Government and people of the United States and the Government and people of Germany.",
      "versionDate": "2025-09-30",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T19:43:30Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres783ih.xml"
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
      "title": "Reaffirming German-American friendship and supporting continued cooperation between the United States and Germany.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T08:48:28Z"
    },
    {
      "title": "Reaffirming German-American friendship and supporting continued cooperation between the United States and Germany.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:05:36Z"
    }
  ]
}
```
