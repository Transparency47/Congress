# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/362?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/362
- Title: A resolution to provide for the printing of the Senate Manual for the One Hundred Nineteenth Congress.
- Congress: 119
- Bill type: SRES
- Bill number: 362
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-24T17:11:53Z
- Update date including text: 2025-09-24T17:11:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-07-31 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S5171; text: CR S5010)
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-07-31 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S5171; text: CR S5010)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/362",
    "number": "362",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M000355",
        "district": "",
        "firstName": "Mitch",
        "fullName": "Sen. McConnell, Mitch [R-KY]",
        "lastName": "McConnell",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "A resolution to provide for the printing of the Senate Manual for the One Hundred Nineteenth Congress.",
    "type": "SRES",
    "updateDate": "2025-09-24T17:11:53Z",
    "updateDateIncludingText": "2025-09-24T17:11:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S5171; text: CR S5010)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres362ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 362\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. McConnell (for himself and Mr. Padilla ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nTo provide for the printing of the Senate Manual for the One Hundred Nineteenth Congress.\nThat a revised edition of the Senate Manual for the One Hundred Nineteenth Congress be prepared by the Committee on Rules and Administration and printed as a Senate document, and that 1,200 additional copies shall be printed and bound for the use of the Senate, bound and delivered as may be directed by the Committee on Rules and Administration.",
      "versionDate": "2025-07-31",
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
            "name": "Books and print media",
            "updateDate": "2025-09-15T13:45:06Z"
          },
          {
            "name": "Congressional operations and organization",
            "updateDate": "2025-09-15T13:45:06Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-09-15T13:45:06Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-09-15T13:45:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-09-12T16:28:36Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres362ats.xml"
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
      "title": "A resolution to provide for the printing of the Senate Manual for the One Hundred Nineteenth Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:25Z"
    },
    {
      "title": "A resolution to provide for the printing of the Senate Manual for the One Hundred Nineteenth Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T10:56:25Z"
    }
  ]
}
```
