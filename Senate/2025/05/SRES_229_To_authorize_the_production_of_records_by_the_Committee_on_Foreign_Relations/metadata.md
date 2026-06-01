# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/229
- Title: A resolution to authorize the production of records by the Committee on Foreign Relations.
- Congress: 119
- Bill type: SRES
- Bill number: 229
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-06-02T14:30:03Z
- Update date including text: 2025-06-02T14:30:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-14 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2934; text: CR S2932)
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-14 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2934; text: CR S2932)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/229",
    "number": "229",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "A resolution to authorize the production of records by the Committee on Foreign Relations.",
    "type": "SRES",
    "updateDate": "2025-06-02T14:30:03Z",
    "updateDateIncludingText": "2025-06-02T14:30:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2934; text: CR S2932)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-14",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres229ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 229\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mr. Thune (for himself and Mr. Schumer ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nTo authorize the production of records by the Committee on Foreign Relations.\nThat the Chairman and Ranking Minority Member of the Committee on Foreign Relations, acting jointly, are authorized to provide to the Department of Justice for use in connection with United States v. Peter Biar Ajak committee records relating to a panel discussion attended by committee staff.",
      "versionDate": "2025-05-14",
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
            "name": "Congressional committees",
            "updateDate": "2025-06-02T14:29:55Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-02T14:28:54Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-06-02T14:30:03Z"
          },
          {
            "name": "Senate Committee on Foreign Relations",
            "updateDate": "2025-06-02T14:29:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-22T18:12:44Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres229ats.xml"
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
      "title": "A resolution to authorize the production of records by the Committee on Foreign Relations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T10:56:22Z"
    },
    {
      "title": "A resolution to authorize the production of records by the Committee on Foreign Relations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T10:56:22Z"
    }
  ]
}
```
