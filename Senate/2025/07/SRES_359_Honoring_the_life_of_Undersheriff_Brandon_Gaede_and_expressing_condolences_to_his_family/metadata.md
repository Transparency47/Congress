# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/359
- Title: A resolution honoring the life of Undersheriff Brandon Gaede and expressing condolences to his family.
- Congress: 119
- Bill type: SRES
- Bill number: 359
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-12T14:57:31Z
- Update date including text: 2025-09-12T14:57:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S5009: 1)
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S5009: 1)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/359",
    "number": "359",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A resolution honoring the life of Undersheriff Brandon Gaede and expressing condolences to his family.",
    "type": "SRES",
    "updateDate": "2025-09-12T14:57:31Z",
    "updateDateIncludingText": "2025-09-12T14:57:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S5009: 1)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T21:16:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres359is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 359\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Marshall (for himself and Mr. Moran ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the life of Undersheriff Brandon Gaede and expressing condolences to his family.\nThat the Senate\u2014\n**(1)**\nhighly respects and appreciates all that Undersheriff Brandon Gaede did to protect and serve his Kansas community;\n**(2)**\noffers condolences to the family of Brandon Gaede;\n**(3)**\npays tribute to Mr. Gaede's noble sacrifice in the line of duty; and\n**(4)**\ncalls on all levels of government to support the family of this fallen officer.",
      "versionDate": "2025-07-31",
      "versionType": "IS"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-12T14:57:31Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres359is.xml"
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
      "title": "A resolution honoring the life of Undersheriff Brandon Gaede and expressing condolences to his family.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:33Z"
    },
    {
      "title": "A resolution honoring the life of Undersheriff Brandon Gaede and expressing condolences to his family.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:22Z"
    }
  ]
}
```
