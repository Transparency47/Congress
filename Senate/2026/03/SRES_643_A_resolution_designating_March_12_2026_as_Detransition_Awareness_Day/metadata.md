# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/643
- Title: A resolution designating March 12, 2026, as "Detransition Awareness Day".
- Congress: 119
- Bill type: SRES
- Bill number: 643
- Origin chamber: Senate
- Introduced date: 2026-03-16
- Update date: 2026-03-23T20:10:27Z
- Update date including text: 2026-03-23T20:10:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in Senate
- 2026-03-16 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1057)
- 2026-03-16 - IntroReferral: Submitted in Senate
- Latest action: 2026-03-16: Submitted in Senate

## Actions

- 2026-03-16 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1057)
- 2026-03-16 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/643",
    "number": "643",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "A resolution designating March 12, 2026, as \"Detransition Awareness Day\".",
    "type": "SRES",
    "updateDate": "2026-03-23T20:10:27Z",
    "updateDateIncludingText": "2026-03-23T20:10:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1057)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T20:02:08Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres643is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 643\nIN THE SENATE OF THE UNITED STATES\nMarch 16, 2026 Mrs. Blackburn submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating March 12, 2026, as Detransition Awareness Day .\nThat the Senate\u2014\n**(1)**\ndesignates March 12, 2026, as Detransition Awareness Day ; and\n**(2)**\ncelebrates and commits to fostering the biological reality of young men and women.",
      "versionDate": "2026-03-16",
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
        "name": "Health",
        "updateDate": "2026-03-23T20:10:27Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres643is.xml"
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
      "title": "A resolution designating March 12, 2026, as \"Detransition Awareness Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:48:40Z"
    },
    {
      "title": "A resolution designating March 12, 2026, as \"Detransition Awareness Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T10:56:18Z"
    }
  ]
}
```
