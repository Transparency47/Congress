# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/422?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/422
- Title: Expressing support for recognizing the month of May as "Excellence in Education: Merit Day Celebration".
- Congress: 119
- Bill type: HRES
- Bill number: 422
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-05-15 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Submitted in House
- Latest action: 2025-05-15: Submitted in House

## Actions

- 2025-05-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-05-15 - IntroReferral: Submitted in House
- 2025-05-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/422",
    "number": "422",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Expressing support for recognizing the month of May as \"Excellence in Education: Merit Day Celebration\".",
    "type": "HRES",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres422ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 422\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Owens submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for recognizing the month of May as Excellence in Education: Merit Day Celebration .\nThat the House of Representatives\u2014\n**(1)**\nexpresses its full support for recognizing Excellence in Education: Merit Day Celebration , to honor those who contribute to the advancement of merit-based educational systems and their role in ensuring the success of future generations of students across the Nation; and\n**(2)**\nrespectfully requests that the Clerk of the House transmit an enrolled copy of this resolution to relevant educational organizations, administrators, and policymakers to encourage widespread recognition and participation in the Excellence in Education: Merit Day Celebration.",
      "versionDate": "2025-05-15",
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
        "name": "Education",
        "updateDate": "2025-05-22T18:03:05Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres422ih.xml"
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
      "title": "Expressing support for recognizing the month of May as \"Excellence in Education: Merit Day Celebration\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T08:48:19Z"
    },
    {
      "title": "Expressing support for recognizing the month of May as \"Excellence in Education: Merit Day Celebration\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T08:06:34Z"
    }
  ]
}
```
