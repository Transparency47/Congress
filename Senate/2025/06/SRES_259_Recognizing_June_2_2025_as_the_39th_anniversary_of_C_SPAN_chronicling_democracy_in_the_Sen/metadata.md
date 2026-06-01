# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/259
- Title: A resolution recognizing June 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate.
- Congress: 119
- Bill type: SRES
- Bill number: 259
- Origin chamber: Senate
- Introduced date: 2025-06-02
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-02: Introduced in Senate
- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S3171-3172)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-06-18 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: 6/02/2025 CR S3171)
- 2025-06-18 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S3478)
- Latest action: 2025-06-02: Introduced in Senate

## Actions

- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S3171-3172)
- 2025-06-18 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-06-18 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: 6/02/2025 CR S3171)
- 2025-06-18 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-18 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S3478)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/259",
    "number": "259",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "A resolution recognizing June 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (text: 6/02/2025 CR S3171)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S3478)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (Sponsor introductory remarks on measure: CR S3171-3172)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-02",
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
            "date": "2025-06-18T19:13:37Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-02T19:55:53Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "OR"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres259is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 259\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Mr. Grassley (for himself, Ms. Klobuchar , Mr. Wyden , and Mr. Young ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing June 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate.\nThat the Senate recognizes\u2014\n**(1)**\nJune 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate; and\n**(2)**\nthe importance of continuous Senate coverage for all Americans and the need for live coverage to be accessible on all platforms.",
      "versionDate": "2025-06-02",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres259ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 259\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Mr. Grassley (for himself, Ms. Klobuchar , Mr. Wyden , and Mr. Young ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJune 18, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing June 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate.\nThat the Senate recognizes\u2014\n**(1)**\nJune 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate; and\n**(2)**\nthe importance of continuous Senate coverage for all Americans and the need for live coverage to be accessible on all platforms.",
      "versionDate": "2025-06-18",
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
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-06-20T18:20:47Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-20T18:20:40Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-06-20T18:21:01Z"
          },
          {
            "name": "Television and film",
            "updateDate": "2025-06-20T18:20:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-06-16T13:20:39Z"
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
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres259is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres259ats.xml"
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
      "title": "A resolution recognizing June 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:34Z"
    },
    {
      "title": "A resolution recognizing June 2, 2025, as the 39th anniversary of C-SPAN chronicling democracy in the Senate.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T10:56:17Z"
    }
  ]
}
```
