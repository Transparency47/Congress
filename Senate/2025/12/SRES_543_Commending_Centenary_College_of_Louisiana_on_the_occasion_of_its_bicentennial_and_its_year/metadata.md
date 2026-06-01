# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/543?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/543
- Title: A resolution commending Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 543
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-08T21:09:12Z
- Update date including text: 2026-01-08T21:09:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-07 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 12/11/2025 S8677)
- 2026-01-07 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-07 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-07 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 12/11/2025 S8677)
- 2026-01-07 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-07 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/543",
    "number": "543",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A resolution commending Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States.",
    "type": "SRES",
    "updateDate": "2026-01-08T21:09:12Z",
    "updateDateIncludingText": "2026-01-08T21:09:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 12/11/2025 S8677)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-01-07",
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
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
        "item": [
          {
            "date": "2026-01-07T22:36:40Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-12-11T20:24:04Z",
            "name": "Referred To"
          }
        ]
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
      "sponsorshipDate": "2025-12-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres543is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 543\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Kennedy (for himself and Mr. Cassidy ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommending Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States.\nThat the Senate\u2014\n**(1)**\ncommends Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States;\n**(2)**\nrecognizes Centenary College of Louisiana for its dedication and longstanding contributions to higher education in the State of Louisiana and the Northwest Louisiana community; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe President of Centenary College of Louisiana, the Honorable Dr. Christopher L. Holoman;\n**(B)**\nthe Provost and Vice President for Academic Affairs of Centenary College of Louisiana, the Honorable Dr. Karen Soul; and\n**(C)**\nthe Centenary College of Louisiana Bicentennial Planning Committee.",
      "versionDate": "2025-12-11",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres543ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 543\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Kennedy (for himself and Mr. Cassidy ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJanuary 7, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nCommending Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States.\nThat the Senate\u2014\n**(1)**\ncommends Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States;\n**(2)**\nrecognizes Centenary College of Louisiana for its dedication and longstanding contributions to higher education in the State of Louisiana and the Northwest Louisiana community; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe President of Centenary College of Louisiana, the Honorable Dr. Christopher L. Holoman;\n**(B)**\nthe Provost and Vice President for Academic Affairs of Centenary College of Louisiana, the Honorable Dr. Karen Soul; and\n**(C)**\nthe Centenary College of Louisiana Bicentennial Planning Committee.",
      "versionDate": "2026-01-07",
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
            "name": "Congressional tributes",
            "updateDate": "2026-01-08T21:09:12Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-01-08T21:09:04Z"
          },
          {
            "name": "Louisiana",
            "updateDate": "2026-01-08T21:09:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-12-15T19:44:45Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres543is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres543ats.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution commending Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T03:18:26Z"
    },
    {
      "title": "A resolution commending Centenary College of Louisiana on the occasion of its bicentennial and its years of service to the State of Louisiana and the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T11:56:22Z"
    }
  ]
}
```
