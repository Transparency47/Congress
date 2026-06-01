# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/477
- Title: A resolution designating the first full week in May as "Tardive Dyskinesia Awareness Week".
- Congress: 119
- Bill type: SRES
- Bill number: 477
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-12-02T16:33:17Z
- Update date including text: 2025-12-02T16:33:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7851-7852)
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7851-7852)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/477",
    "number": "477",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A resolution designating the first full week in May as \"Tardive Dyskinesia Awareness Week\".",
    "type": "SRES",
    "updateDate": "2025-12-02T16:33:17Z",
    "updateDateIncludingText": "2025-12-02T16:33:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S7851-7852)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T17:02:37Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres477is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 477\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Mullin (for himself and Mr. Padilla ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating the first full week in May as Tardive Dyskinesia Awareness Week .\nThat the Senate\u2014\n**(1)**\ndesignates the first full week in May as Tardive Dyskinesia Awareness Week ; and\n**(2)**\nin recognition and support of Tardive Dyskinesia Awareness Week\u2014\n**(A)**\nunderscores the importance of early detection and intervention to improve outcomes for individuals living with mental health conditions and individuals prescribed antipsychotics; and\n**(B)**\nsupports efforts to raise awareness about the causes and symptoms of tardive dyskinesia and the importance of routine tardive dyskinesia screening.",
      "versionDate": "2025-10-30",
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
        "updateDate": "2025-12-02T16:33:17Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres477is.xml"
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
      "title": "A resolution designating the first full week in May as \"Tardive Dyskinesia Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-01T03:48:21Z"
    },
    {
      "title": "A resolution designating the first full week in May as \"Tardive Dyskinesia Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T10:56:15Z"
    }
  ]
}
```
