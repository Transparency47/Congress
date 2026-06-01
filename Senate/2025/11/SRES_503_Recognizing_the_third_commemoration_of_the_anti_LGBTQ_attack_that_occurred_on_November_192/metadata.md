# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/503?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/503
- Title: A resolution recognizing the third commemoration of the anti-LGBTQ+ attack that occurred on November 19-20, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado.
- Congress: 119
- Bill type: SRES
- Bill number: 503
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-01-08T17:38:55Z
- Update date including text: 2026-01-08T17:38:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-07 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 11/19 S8242)
- 2026-01-07 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-07 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-01-07 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 11/19 S8242)
- 2026-01-07 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-01-07 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/503",
    "number": "503",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "A resolution recognizing the third commemoration of the anti-LGBTQ+ attack that occurred on November 19-20, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado.",
    "type": "SRES",
    "updateDate": "2026-01-08T17:38:55Z",
    "updateDateIncludingText": "2026-01-08T17:38:55Z"
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
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S90; text: CR 11/19 S8242)",
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
      "text": "Referred to the Committee on the Judiciary.",
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
        "item": [
          {
            "date": "2026-01-07T22:36:38Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-11-19T17:50:58Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres503is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 503\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Bennet (for himself and Mr. Hickenlooper ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the third commemoration of the anti-LGBTQ+ attack that occurred on November 19\u201320, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado.\nThat the Senate\u2014\n**(1)**\nrecognizes the 3 year remembrance of the anti-LGBTQ+ attack that occurred on November 19\u201320, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado; and\n**(2)**\nexpresses continued solidarity and support to the survivors of the Club Q shooting, the Colorado Springs LGBTQ+ community, and the families, friends, and loved ones affected by the tragedy.",
      "versionDate": "2025-11-19",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres503ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 503\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Bennet (for himself and Mr. Hickenlooper ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJanuary 7, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing the third commemoration of the anti-LGBTQ+ attack that occurred on November 19\u201320, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado.\nThat the Senate\u2014\n**(1)**\nrecognizes the 3 year remembrance of the anti-LGBTQ+ attack that occurred on November 19\u201320, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado; and\n**(2)**\nexpresses continued solidarity and support to the survivors of the Club Q shooting, the Colorado Springs LGBTQ+ community, and the families, friends, and loved ones affected by the tragedy.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-11-25T20:04:10Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres503is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres503ats.xml"
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
      "title": "A resolution recognizing the third commemoration of the anti-LGBTQ+ attack that occurred on November 19-20, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-22T04:33:23Z"
    },
    {
      "title": "A resolution recognizing the third commemoration of the anti-LGBTQ+ attack that occurred on November 19-20, 2022, at Club Q, an LGBTQ+ bar in Colorado Springs, Colorado.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T11:56:22Z"
    }
  ]
}
```
