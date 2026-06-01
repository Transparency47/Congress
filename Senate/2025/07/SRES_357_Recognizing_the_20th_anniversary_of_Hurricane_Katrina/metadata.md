# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/357
- Title: A resolution recognizing the 20th anniversary of Hurricane Katrina.
- Congress: 119
- Bill type: SRES
- Bill number: 357
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-16T22:34:34Z
- Update date including text: 2025-09-16T22:34:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S5007: 1)
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S5007: 1)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/357",
    "number": "357",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A resolution recognizing the 20th anniversary of Hurricane Katrina.",
    "type": "SRES",
    "updateDate": "2025-09-16T22:34:34Z",
    "updateDateIncludingText": "2025-09-16T22:34:34Z"
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
      "text": "Referred to the Committee on the Judiciary. (text: CR S5007: 1)",
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
          "date": "2025-07-31T20:32:38Z",
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres357is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 357\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Cassidy (for himself and Mr. Kennedy ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the 20th anniversary of Hurricane Katrina.\nThat the Senate\u2014\n**(1)**\ncommemorates the victims of Hurricane Katrina;\n**(2)**\ncommends the courageous efforts of those who assisted in the recovery efforts;\n**(3)**\nrecognizes the contributions of the communities in Louisiana and across the United States for providing shelter and assistance to survivors; and\n**(4)**\nreaffirms its commitment to protecting the Gulf Coast region from future storms.",
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
        "name": "Emergency Management",
        "updateDate": "2025-09-16T22:34:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres357is.xml"
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
      "title": "A resolution recognizing the 20th anniversary of Hurricane Katrina.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:36Z"
    },
    {
      "title": "A resolution recognizing the 20th anniversary of Hurricane Katrina.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:19Z"
    }
  ]
}
```
