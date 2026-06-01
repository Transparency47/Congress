# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/712
- Title: A resolution expressing the sense of the Senate in support of general elections in Venezuela.
- Congress: 119
- Bill type: SRES
- Bill number: 712
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-06T20:48:04Z
- Update date including text: 2026-05-06T20:48:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2176)
- 2026-04-30 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-30: Submitted in Senate

## Actions

- 2026-04-30 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2176)
- 2026-04-30 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/712",
    "number": "712",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A resolution expressing the sense of the Senate in support of general elections in Venezuela.",
    "type": "SRES",
    "updateDate": "2026-05-06T20:48:04Z",
    "updateDateIncludingText": "2026-05-06T20:48:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S2176)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
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
          "date": "2026-04-30T18:13:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres712is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 712\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Kaine (for himself and Mr. Scott of Florida ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate in support of general elections in Venezuela.\nThat it is the sense of the Senate that the United States should use all diplomatic tools to support internationally monitored, free and fair elections in Venezuela.",
      "versionDate": "2026-04-30",
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
        "name": "International Affairs",
        "updateDate": "2026-05-06T20:48:03Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres712is.xml"
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
      "title": "A resolution expressing the sense of the Senate in support of general elections in Venezuela.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T05:18:26Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate in support of general elections in Venezuela.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:32Z"
    }
  ]
}
```
