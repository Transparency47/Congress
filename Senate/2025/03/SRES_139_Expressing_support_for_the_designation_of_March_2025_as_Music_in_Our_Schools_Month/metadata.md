# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/139
- Title: A resolution expressing support for the designation of March 2025 as "Music in Our Schools Month".
- Congress: 119
- Bill type: SRES
- Bill number: 139
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-03-09T18:25:35Z
- Update date including text: 2026-03-09T18:25:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1875)
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1875)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/139",
    "number": "139",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "A resolution expressing support for the designation of March 2025 as \"Music in Our Schools Month\".",
    "type": "SRES",
    "updateDate": "2026-03-09T18:25:35Z",
    "updateDateIncludingText": "2026-03-09T18:25:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1875)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-26T19:09:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres139is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 139\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Booker (for himself and Mr. Padilla ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of March 2025 as Music in Our Schools Month .\nThat the Senate\u2014\n**(1)**\nsupports the designation of March 2025 as Music in Our Schools Month ; and\n**(2)**\nrecognizes\u2014\n**(A)**\nthe fundamental importance of music to the culture of the United States;\n**(B)**\nthe long history of music as an integral part of the schools in the United States;\n**(C)**\nthe disparate access to high-quality music education that exists across the United States; and\n**(D)**\nthe need to do more to support the teaching and learning of music in public schools.",
      "versionDate": "2025-03-26",
      "versionType": "IS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "257",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of March 2025 as \"Music in Our Schools Month\".",
      "type": "HRES"
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
        "updateDate": "2025-03-31T15:41:32Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres139is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing support for the designation of March 2025 as \"Music in Our Schools Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:49Z"
    },
    {
      "title": "A resolution expressing support for the designation of March 2025 as \"Music in Our Schools Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T10:56:24Z"
    }
  ]
}
```
