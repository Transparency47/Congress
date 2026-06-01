# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/659?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/659
- Title: A resolution celebrating the 100th anniversary of the American Shore and Beach Preservation Association.
- Congress: 119
- Bill type: SRES
- Bill number: 659
- Origin chamber: Senate
- Introduced date: 2026-03-23
- Update date: 2026-03-31T21:02:15Z
- Update date including text: 2026-03-31T21:02:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-23: Introduced in Senate
- 2026-03-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S1546)
- 2026-03-23 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-23: Submitted in Senate

## Actions

- 2026-03-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S1546)
- 2026-03-23 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-23",
    "latestAction": {
      "actionDate": "2026-03-23",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/659",
    "number": "659",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A resolution celebrating the 100th anniversary of the American Shore and Beach Preservation Association.",
    "type": "SRES",
    "updateDate": "2026-03-31T21:02:15Z",
    "updateDateIncludingText": "2026-03-31T21:02:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S1546)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-03-23T22:26:24Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres659is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 659\nIN THE SENATE OF THE UNITED STATES\nMarch 23, 2026 Mr. Whitehouse (for himself and Mr. Cassidy ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCelebrating the 100th anniversary of the American Shore and Beach Preservation Association.\nThat the Senate\u2014\n**(1)**\nrecognizes and celebrates the 100th anniversary of the American Shore and Beach Preservation Association (in this resolution referred to as the Association );\n**(2)**\ncommemorates the centennial of the Association, honoring a century of shore and beach preservation and progress; and\n**(3)**\ncongratulates the leaders and members of the Association on a century of dedication to the shores and beaches of the United States and recognizes the enduring importance of its mission.",
      "versionDate": "2026-03-23",
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
        "name": "Water Resources Development",
        "updateDate": "2026-03-31T21:02:15Z"
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
      "date": "2026-03-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres659is.xml"
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
      "title": "A resolution celebrating the 100th anniversary of the American Shore and Beach Preservation Association.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:33:41Z"
    },
    {
      "title": "A resolution celebrating the 100th anniversary of the American Shore and Beach Preservation Association.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T10:56:23Z"
    }
  ]
}
```
