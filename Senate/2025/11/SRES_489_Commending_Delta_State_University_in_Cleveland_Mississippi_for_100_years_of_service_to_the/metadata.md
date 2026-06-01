# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/489?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/489
- Title: A resolution commending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 489
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-04-01T19:33:44Z
- Update date including text: 2026-04-01T19:33:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-11-20 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-20 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-20 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-11-20 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S8400; text: CR 11/06/2025 S7965-7966)
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-11-20 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-20 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-11-20 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-11-20 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S8400; text: CR 11/06/2025 S7965-7966)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/489",
    "number": "489",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "A resolution commending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States.",
    "type": "SRES",
    "updateDate": "2026-04-01T19:33:44Z",
    "updateDateIncludingText": "2026-04-01T19:33:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S8400; text: CR 11/06/2025 S7965-7966)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
            "date": "2025-11-20T21:48:43Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-11-06T22:14:02Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres489is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 489\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mrs. Hyde-Smith (for herself and Mr. Wicker ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States.\nThat the Senate\u2014\n**(1)**\ncommends Delta State University for 100 years of service to the State of Mississippi and the United States;\n**(2)**\nrecognizes Delta State University for its academic, cultural, and athletic excellence; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe President of Delta State University, Dr. Daniel J. Ennis;\n**(B)**\nthe Provost and Vice President for Academic Affairs, Dr. Leslie Griffin; and\n**(C)**\nthe Director of Athletics, Mr. Mike Kinnison.",
      "versionDate": "2025-11-06",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres489ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 489\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mrs. Hyde-Smith (for herself and Mr. Wicker ) submitted the following resolution; which was referred to the Committee on the Judiciary\nNovember 20, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nCommending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States.\nThat the Senate\u2014\n**(1)**\ncommends Delta State University for 100 years of service to the State of Mississippi and the United States;\n**(2)**\nrecognizes Delta State University for its academic, cultural, and athletic excellence; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe President of Delta State University, Dr. Daniel J. Ennis;\n**(B)**\nthe Provost and Vice President for Academic Affairs, Dr. Leslie Griffin; and\n**(C)**\nthe Director of Athletics, Mr. Mike Kinnison.",
      "versionDate": "2025-11-20",
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
            "updateDate": "2025-12-02T19:27:33Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-12-02T19:27:12Z"
          },
          {
            "name": "Mississippi",
            "updateDate": "2025-12-02T19:27:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-11-24T16:32:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119sres489",
          "measure-number": "489",
          "measure-type": "sres",
          "orig-publish-date": "2025-11-20",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres489v55",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-11-20",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution commends Delta State University for its 100 years of service to Mississippi and the United States. It also recognizes Delta State University for its academic, cultural, and athletic excellence.</p>"
        },
        "title": "A resolution commending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres489.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution commends Delta State University for its 100 years of service to Mississippi and the United States. It also recognizes Delta State University for its academic, cultural, and athletic excellence.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres489"
    },
    "title": "A resolution commending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution commends Delta State University for its 100 years of service to Mississippi and the United States. It also recognizes Delta State University for its academic, cultural, and athletic excellence.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres489"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres489is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres489ats.xml"
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
      "title": "A resolution commending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:24Z"
    },
    {
      "title": "A resolution commending Delta State University in Cleveland, Mississippi, for 100 years of service to the State of Mississippi and the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T11:56:17Z"
    }
  ]
}
```
