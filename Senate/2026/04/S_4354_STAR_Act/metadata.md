# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4354
- Title: STAR Act
- Congress: 119
- Bill type: S
- Bill number: 4354
- Origin chamber: Senate
- Introduced date: 2026-04-21
- Update date: 2026-05-14T16:04:12Z
- Update date including text: 2026-05-14T16:04:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in Senate
- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-04-21: Introduced in Senate

## Actions

- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4354",
    "number": "4354",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "STAR Act",
    "type": "S",
    "updateDate": "2026-05-14T16:04:12Z",
    "updateDateIncludingText": "2026-05-14T16:04:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T19:09:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4354is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4354\nIN THE SENATE OF THE UNITED STATES\nApril 21, 2026 Ms. Hirono (for herself and Mr. Reed ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to allow certain funds to be used for incremental costs of incorporating art into facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Saving Transit Art Resources Act or the STAR Act .\n#### 2. Allowing art\n##### (a) In general\nSection 5323(h) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting or after the semicolon;\n**(2)**\nby striking paragraph (2); and\n**(3)**\nby redesignating paragraph (3) as paragraph (2).\n##### (b) No special rule\nSection 5309 of title 49, United States Code, is amended\u2014\n**(1)**\nby striking subsection (p); and\n**(2)**\nby redesignating subsections (q) and (r) as subsections (p) and (q), respectively.",
      "versionDate": "2026-04-21",
      "versionType": "Introduced in Senate"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-05-14T16:04:12Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4354is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "STAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T06:53:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T06:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Saving Transit Art Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T06:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to allow certain funds to be used for incremental costs of incorporating art into facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T06:48:29Z"
    }
  ]
}
```
