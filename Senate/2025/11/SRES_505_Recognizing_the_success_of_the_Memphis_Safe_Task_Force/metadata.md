# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/505
- Title: A resolution recognizing the success of the Memphis Safe Task Force.
- Congress: 119
- Bill type: SRES
- Bill number: 505
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2025-11-25T20:10:06Z
- Update date including text: 2025-11-25T20:10:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8243)
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S8243)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/505",
    "number": "505",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "A resolution recognizing the success of the Memphis Safe Task Force.",
    "type": "SRES",
    "updateDate": "2025-11-25T20:10:06Z",
    "updateDateIncludingText": "2025-11-25T20:10:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S8243)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T21:55:35Z",
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
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres505is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 505\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mrs. Blackburn (for herself and Mr. Hagerty ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the success of the Memphis Safe Task Force.\nThat the Senate\u2014\n**(1)**\nrecognizes the monumental success that has already been achieved because of the Memphis Safe Task Force and President Donald J. Trump\u2019s decisive leadership; and\n**(2)**\ncommends President Trump, the most pro-law enforcement President in the history of the United States, for his work to make America safe again.",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-11-25T20:10:06Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres505is.xml"
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
      "title": "A resolution recognizing the success of the Memphis Safe Task Force.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T04:33:22Z"
    },
    {
      "title": "A resolution recognizing the success of the Memphis Safe Task Force.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T11:56:19Z"
    }
  ]
}
```
