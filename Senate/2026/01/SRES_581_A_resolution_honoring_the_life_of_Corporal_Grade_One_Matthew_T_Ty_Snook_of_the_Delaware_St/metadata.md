# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/581
- Title: A resolution honoring the life of Corporal Grade One Matthew T. "Ty" Snook of the Delaware State Police.
- Congress: 119
- Bill type: SRES
- Bill number: 581
- Origin chamber: Senate
- Introduced date: 2026-01-13
- Update date: 2026-02-04T22:54:32Z
- Update date including text: 2026-02-04T22:54:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in Senate
- 2026-01-13 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-13 - IntroReferral: Submitted in Senate
- 2026-02-03 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-02-03 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S473; text: CR 1/13/2026 S163)
- 2026-02-03 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-02-03 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2026-01-13: Submitted in Senate

## Actions

- 2026-01-13 - IntroReferral: Referred to the Committee on the Judiciary.
- 2026-01-13 - IntroReferral: Submitted in Senate
- 2026-02-03 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-02-03 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S473; text: CR 1/13/2026 S163)
- 2026-02-03 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-02-03 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/581",
    "number": "581",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001303",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
        "lastName": "Blunt Rochester",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A resolution honoring the life of Corporal Grade One Matthew T. \"Ty\" Snook of the Delaware State Police.",
    "type": "SRES",
    "updateDate": "2026-02-04T22:54:32Z",
    "updateDateIncludingText": "2026-02-04T22:54:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S473; text: CR 1/13/2026 S163)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-01-13",
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
      "actionCode": "10025",
      "actionDate": "2026-01-13",
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
      "text": "Submitted in Senate",
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
            "date": "2026-02-03T22:18:25Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-01-13T19:38:50Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres581is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 581\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2026 Ms. Blunt Rochester (for herself and Mr. Coons ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the life of Corporal Grade One Matthew T. Ty Snook of the Delaware State Police.\nThat the Senate\u2014\n**(1)**\nhonors the life and service of Corporal Grade One Matthew T. Ty Snook of the Delaware State Police;\n**(2)**\nexpresses its deepest condolences to the family of Corporal Grade One Snook, including his wife, Lauren Snook, his daughter, Letty Snook, his parents, Matthew and Karen Snook, his brother, Joshua Snook, and his sister, Kassi Dunphy;\n**(3)**\nrecognizes the noble acts Corporal Grade One Snook performed in the line of duty, sacrificing his own life on December 23, 2025, to save the lives of others; and\n**(4)**\nreaffirms its support for law enforcement officers and public servants who dedicate their lives to keeping our communities safe.",
      "versionDate": "2026-01-13",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres581ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 581\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2026 Ms. Blunt Rochester (for herself and Mr. Coons ) submitted the following resolution; which was referred to the Committee on the Judiciary\nFebruary 3, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nHonoring the life of Corporal Grade One Matthew T. Ty Snook of the Delaware State Police.\nThat the Senate\u2014\n**(1)**\nhonors the life and service of Corporal Grade One Matthew T. Ty Snook of the Delaware State Police;\n**(2)**\nexpresses its deepest condolences to the family of Corporal Grade One Snook, including his wife, Lauren Snook, his daughter, Letty Snook, his parents, Matthew and Karen Snook, his brother, Joshua Snook, and his sister, Kassi Dunphy;\n**(3)**\nrecognizes the noble acts Corporal Grade One Snook performed in the line of duty, sacrificing his own life on December 23, 2025, to save the lives of others; and\n**(4)**\nreaffirms its support for law enforcement officers and public servants who dedicate their lives to keeping our communities safe.",
      "versionDate": "2026-02-03",
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
            "updateDate": "2026-02-04T18:08:49Z"
          },
          {
            "name": "Delaware",
            "updateDate": "2026-02-04T18:08:41Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2026-02-04T18:08:29Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-04T22:54:32Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres581is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres581ats.xml"
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
      "title": "A resolution honoring the life of Corporal Grade One Matthew T. \"Ty\" Snook of the Delaware State Police.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-15T04:03:18Z"
    },
    {
      "title": "A resolution honoring the life of Corporal Grade One Matthew T. \"Ty\" Snook of the Delaware State Police.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T11:56:17Z"
    }
  ]
}
```
