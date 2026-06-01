# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/431?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/431
- Title: A resolution supporting the goals and objectives of Choose Respect Day.
- Congress: 119
- Bill type: SRES
- Bill number: 431
- Origin chamber: Senate
- Introduced date: 2025-10-03
- Update date: 2025-12-01T11:52:47Z
- Update date including text: 2025-12-01T11:52:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-03: Introduced in Senate
- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6929-6930; text: CR S6935)
- Latest action: 2025-10-03: Introduced in Senate

## Actions

- 2025-10-03 - IntroReferral: Introduced in Senate
- 2025-10-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6929-6930; text: CR S6935)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/431",
    "number": "431",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A resolution supporting the goals and objectives of Choose Respect Day.",
    "type": "SRES",
    "updateDate": "2025-12-01T11:52:47Z",
    "updateDateIncludingText": "2025-12-01T11:52:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6929-6930; text: CR S6935)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-03",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres431ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 431\nIN THE SENATE OF THE UNITED STATES\nOctober 3, 2025 Mr. Sullivan (for himself and Mr. Schiff ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nSupporting the goals and objectives of Choose Respect Day.\nThat the Senate\u2014\n**(1)**\nsupports the goals and objectives of Choose Respect Day; and\n**(2)**\nencourages all private citizens, organizations, and Federal, State, and local governmental and legislative entities to recognize Choose Respect Day through proclamations, activities, and educational efforts in furtherance of changing the culture around the tolerance of domestic violence.",
      "versionDate": "2025-10-03",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-18T19:29:06Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-11-18T19:29:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-17T17:16:36Z"
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
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres431ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution supporting the goals and objectives of Choose Respect Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:56:15Z"
    },
    {
      "title": "A resolution supporting the goals and objectives of Choose Respect Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:56:15Z"
    }
  ]
}
```
