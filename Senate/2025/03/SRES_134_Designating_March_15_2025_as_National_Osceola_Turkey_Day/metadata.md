# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/134
- Title: A resolution designating March 15, 2025, as "National Osceola Turkey Day".
- Congress: 119
- Bill type: SRES
- Bill number: 134
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2026-04-24T22:13:21Z
- Update date including text: 2026-04-24T22:13:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-03-24 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1807; text: CR S1806)
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-03-24 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1807; text: CR S1806)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/134",
    "number": "134",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution designating March 15, 2025, as \"National Osceola Turkey Day\".",
    "type": "SRES",
    "updateDate": "2026-04-24T22:13:21Z",
    "updateDateIncludingText": "2026-04-24T22:13:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1807; text: CR S1806)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres134ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 134\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mr. Scott of Florida (for himself and Mrs. Moody ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating March 15, 2025, as National Osceola Turkey Day .\nThat the Senate\u2014\n**(1)**\ndesignates March 15, 2025, as National Osceola Turkey Day ; and\n**(2)**\nencourages the people of the United States to observe National Osceola Turkey Day with appropriate ceremonies and activities.",
      "versionDate": "2025-03-24",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-27",
        "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1690)"
      },
      "number": "647",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating March 21, 2026, as \"National Osceola Turkey Day\".",
      "type": "SRES"
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
            "name": "Birds",
            "updateDate": "2025-04-07T11:38:47Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-04-07T11:38:54Z"
          },
          {
            "name": "Florida",
            "updateDate": "2025-04-07T11:39:02Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2025-04-07T11:39:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-03-31T13:06:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119sres134",
          "measure-number": "134",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres134v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates March 15, 2025, as National Osceola Turkey Day.</p>"
        },
        "title": "A resolution designating March 15, 2025, as \"National Osceola Turkey Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres134.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates March 15, 2025, as National Osceola Turkey Day.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119sres134"
    },
    "title": "A resolution designating March 15, 2025, as \"National Osceola Turkey Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates March 15, 2025, as National Osceola Turkey Day.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119sres134"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres134ats.xml"
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
      "title": "A resolution designating March 15, 2025, as \"National Osceola Turkey Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T10:56:18Z"
    },
    {
      "title": "A resolution designating March 15, 2025, as \"National Osceola Turkey Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T10:56:18Z"
    }
  ]
}
```
