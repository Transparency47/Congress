# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/1?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/1
- Title: A resolution establishing a Committee to Inform the President of the United States that a quorum of each House is assembled.
- Congress: 119
- Bill type: SRES
- Bill number: 1
- Origin chamber: Senate
- Introduced date: 2025-01-03
- Update date: 2025-04-22T13:38:06Z
- Update date including text: 2025-04-22T13:38:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in Senate
- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S5-6; text: CR S6)
- Latest action: 2025-01-03: Introduced in Senate

## Actions

- 2025-01-03 - IntroReferral: Introduced in Senate
- 2025-01-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent.
- 2025-01-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S5-6; text: CR S6)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/1",
    "number": "1",
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
    "title": "A resolution establishing a Committee to Inform the President of the United States that a quorum of each House is assembled.",
    "type": "SRES",
    "updateDate": "2025-04-22T13:38:06Z",
    "updateDateIncludingText": "2025-04-22T13:38:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment by Unanimous Consent. (consideration: CR S5-6; text: CR S6)",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres1ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 1\nIN THE SENATE OF THE UNITED STATES\nJanuary 3, 2025 Mr. Thune submitted the following resolution; which was considered and agreed to\nRESOLUTION\nEstablishing a Committee to Inform the President of the United States that a quorum of each House is assembled.\nThat a committee consisting of two Senators be appointed to join such committee as may be appointed by the House of Representatives to wait upon the President of the United States and inform him that a quorum of each House is assembled and that the Congress is ready to receive any communication he may be pleased to make.",
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
            "name": "Congressional operations and organization",
            "updateDate": "2025-01-15T18:32:58Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-01-15T18:33:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-13T12:52:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119sres1",
          "measure-number": "1",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "SENATE",
          "update-date": "2025-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres1v00",
            "update-date": "2025-04-22"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution establishes a committee to inform the President that a quorum of each chamber of Congress is assembled and that Congress is ready to receive communications from him.</p>"
        },
        "title": "A resolution establishing a Committee to Inform the President of the United States that a quorum of each House is assembled."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres1.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution establishes a committee to inform the President that a quorum of each chamber of Congress is assembled and that Congress is ready to receive communications from him.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119sres1"
    },
    "title": "A resolution establishing a Committee to Inform the President of the United States that a quorum of each House is assembled."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution establishes a committee to inform the President that a quorum of each chamber of Congress is assembled and that Congress is ready to receive communications from him.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119sres1"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres1ats.xml"
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
      "title": "A resolution establishing a Committee to Inform the President of the United States that a quorum of each House is assembled.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-04T11:56:15Z"
    },
    {
      "title": "A resolution establishing a Committee to Inform the President of the United States that a quorum of each House is assembled.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-04T11:56:15Z"
    }
  ]
}
```
