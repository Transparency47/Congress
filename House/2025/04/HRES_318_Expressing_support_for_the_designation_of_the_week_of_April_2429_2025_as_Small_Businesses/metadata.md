# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/318
- Title: Expressing support for the designation of the week of April 24-29, 2025, as "Small Businesses in For-Hire Transportation Week".
- Congress: 119
- Bill type: HRES
- Bill number: 318
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-04-11T11:57:22Z
- Update date including text: 2025-04-11T11:57:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Small Business.
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-09 - IntroReferral: Submitted in House
- Latest action: 2025-04-09: Submitted in House

## Actions

- 2025-04-09 - IntroReferral: Referred to the House Committee on Small Business.
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/318",
    "number": "318",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Expressing support for the designation of the week of April 24-29, 2025, as \"Small Businesses in For-Hire Transportation Week\".",
    "type": "HRES",
    "updateDate": "2025-04-11T11:57:22Z",
    "updateDateIncludingText": "2025-04-11T11:57:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres318ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 318\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mrs. Miller of West Virginia submitted the following resolution; which was referred to the Committee on Small Business\nRESOLUTION\nExpressing support for the designation of the week of April 24\u201329, 2025, as Small Businesses in For-Hire Transportation Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of Small Businesses in For-Hire Transportation Week in honor of the commitment and essential services provided by the for-hire transportation industry; and\n**(2)**\nrecognizes the efforts of small business in the for-hire transportation industry to promote safety and support for our communities.",
      "versionDate": "2025-04-09",
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
        "name": "Commerce",
        "updateDate": "2025-04-11T11:57:22Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres318ih.xml"
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
      "title": "Expressing support for the designation of the week of April 24-29, 2025, as \"Small Businesses in For-Hire Transportation Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T10:18:20Z"
    },
    {
      "title": "Expressing support for the designation of the week of April 24-29, 2025, as \"Small Businesses in For-Hire Transportation Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T08:06:49Z"
    }
  ]
}
```
