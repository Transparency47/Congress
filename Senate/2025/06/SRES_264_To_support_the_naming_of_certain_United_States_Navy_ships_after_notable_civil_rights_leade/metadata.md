# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/264
- Title: A resolution to support the naming of certain United States Navy ships after notable civil rights leaders and to strongly encourage the Department of Defense not to change the names of such ships.
- Congress: 119
- Bill type: SRES
- Bill number: 264
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2025-07-16T15:11:28Z
- Update date including text: 2025-07-16T15:11:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S3256)
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Referred to the Committee on Armed Services. (text: CR S3256)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/264",
    "number": "264",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A resolution to support the naming of certain United States Navy ships after notable civil rights leaders and to strongly encourage the Department of Defense not to change the names of such ships.",
    "type": "SRES",
    "updateDate": "2025-07-16T15:11:28Z",
    "updateDateIncludingText": "2025-07-16T15:11:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Armed Services. (text: CR S3256)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T17:40:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sponsorshipDate": "2025-06-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres264is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 264\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Schiff (for himself and Mr. Padilla ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nTo support the naming of certain United States Navy ships after notable civil rights leaders and to strongly encourage the Department of Defense not to change the names of such ships.\nThat the Senate\u2014\n**(1)**\nstrongly supports the naming of John Lewis-class fleet replacement oilers after the aforementioned civil rights leaders as a fitting tribute to honor their contributions to the advancement of civil rights; and\n**(2)**\nstrongly encourages the Department of Defense not to take any action to change the names of any of the ships referred to in paragraph (1).",
      "versionDate": "2025-06-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-16T15:11:28Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres264is.xml"
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
      "title": "A resolution to support the naming of certain United States Navy ships after notable civil rights leaders and to strongly encourage the Department of Defense not to change the names of such ships.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:17Z"
    },
    {
      "title": "A resolution to support the naming of certain United States Navy ships after notable civil rights leaders and to strongly encourage the Department of Defense not to change the names of such ships.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-06T10:56:17Z"
    }
  ]
}
```
