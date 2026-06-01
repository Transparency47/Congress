# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/478
- Title: A resolution to authorize testimony, document production, and representation by the Senate Legal Counsel in the case of United States v. Kaminski.
- Congress: 119
- Bill type: SRES
- Bill number: 478
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-12-01T19:44:50Z
- Update date including text: 2025-12-01T19:44:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-30 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S7855; text: CR S7852)
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-30 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S7855; text: CR S7852)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/478",
    "number": "478",
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
    "title": "A resolution to authorize testimony, document production, and representation by the Senate Legal Counsel in the case of United States v. Kaminski.",
    "type": "SRES",
    "updateDate": "2025-12-01T19:44:50Z",
    "updateDateIncludingText": "2025-12-01T19:44:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S7855; text: CR S7852)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
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
      "sponsorshipDate": "2025-10-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres478ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 478\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Thune (for himself and Mr. Schumer ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nTo authorize testimony, document production, and representation by the Senate Legal Counsel in the case of United States v. Kaminski .\nThat Ian Madigan, a former employee of the office of former Senator Casey, and any other former employee of the Senator\u2019s office from whom relevant evidence may be necessary, are authorized to provide testimony and documents in the case of United States v. Kaminski , except concerning matter for which a privilege or objection should be asserted.\n#### 2.\nThe Senate Legal Counsel is authorized to represent Mr. Madigan and any other former employee of Senator Casey's office in connection with the testimony authorized in section one of this resolution.",
      "versionDate": "2025-10-30",
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
            "name": "Evidence and witnesses",
            "updateDate": "2025-11-18T18:52:46Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-11-18T18:53:55Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-11-18T18:52:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-11-17T18:04:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres478ats.xml"
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
      "title": "A resolution to authorize testimony, document production, and representation by the Senate Legal Counsel in the case of United States v. Kaminski.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-31T10:56:18Z"
    },
    {
      "title": "A resolution to authorize testimony, document production, and representation by the Senate Legal Counsel in the case of United States v. Kaminski.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-31T10:56:18Z"
    }
  ]
}
```
