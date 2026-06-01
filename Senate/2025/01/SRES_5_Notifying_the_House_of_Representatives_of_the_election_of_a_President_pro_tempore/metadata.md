# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/5?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/5
- Title: A resolution notifying the House of Representatives of the election of a President pro tempore.
- Congress: 119
- Bill type: SRES
- Bill number: 5
- Origin chamber: Senate
- Introduced date: 2025-01-03
- Update date: 2026-01-05T13:38:00Z
- Update date including text: 2026-01-05T13:38:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, text, titles

## Timeline

- 2025-01-03: Introduced in Senate
- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6; text: CR S6)
- 2025-01-06 - Floor: Message on Senate action sent to the House.
- Latest action: 2025-01-03: Introduced in Senate

## Actions

- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6; text: CR S6)
- 2025-01-06 - Floor: Message on Senate action sent to the House.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/5",
    "number": "5",
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
    "title": "A resolution notifying the House of Representatives of the election of a President pro tempore.",
    "type": "SRES",
    "updateDate": "2026-01-05T13:38:00Z",
    "updateDateIncludingText": "2026-01-05T13:38:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S6; text: CR S6)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-03",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres5ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 5\nIN THE SENATE OF THE UNITED STATES\nJanuary 3, 2025 Mr. Thune submitted the following resolution; which was considered and agreed to\nRESOLUTION\nNotifying the House of Representatives of the election of a President pro tempore.\nThat the House of Representatives be notified of the election of the Honorable Charles E. Grassley as President of the Senate pro tempore.",
      "versionDate": "2025-01-03",
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
            "name": "Congressional leadership",
            "updateDate": "2025-01-15T18:36:27Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-15T18:36:36Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-15T18:36:53Z"
          },
          {
            "name": "Senate",
            "updateDate": "2025-01-15T18:36:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2026-01-05T13:38:00Z"
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
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres5ats.xml"
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
      "title": "A resolution notifying the House of Representatives of the election of a President pro tempore.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-04T11:56:18Z"
    },
    {
      "title": "A resolution notifying the House of Representatives of the election of a President pro tempore.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-04T11:56:18Z"
    }
  ]
}
```
