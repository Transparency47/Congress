# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/454
- Title: A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as "Bat Week".
- Congress: 119
- Bill type: SRES
- Bill number: 454
- Origin chamber: Senate
- Introduced date: 2025-10-16
- Update date: 2026-04-08T21:37:48Z
- Update date including text: 2026-04-08T21:37:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-16: Introduced in Senate
- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Referred to the Committee on Environment and Public Works. (text: CR S7158)
- 2025-10-28 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-28 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7787)
- 2025-10-28 - Discharge: Senate Committee on Environment and Public Works discharged by Unanimous Consent.
- 2025-10-28 - Committee: Senate Committee on Environment and Public Works discharged by Unanimous Consent.
- Latest action: 2025-10-16: Introduced in Senate

## Actions

- 2025-10-16 - IntroReferral: Introduced in Senate
- 2025-10-16 - IntroReferral: Referred to the Committee on Environment and Public Works. (text: CR S7158)
- 2025-10-28 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-10-28 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7787)
- 2025-10-28 - Discharge: Senate Committee on Environment and Public Works discharged by Unanimous Consent.
- 2025-10-28 - Committee: Senate Committee on Environment and Public Works discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-16",
    "latestAction": {
      "actionDate": "2025-10-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/454",
    "number": "454",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
    "type": "SRES",
    "updateDate": "2026-04-08T21:37:48Z",
    "updateDateIncludingText": "2026-04-08T21:37:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S7787)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Environment and Public Works discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Environment and Public Works discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-16",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Environment and Public Works. (text: CR S7158)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-16",
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
            "date": "2025-10-28T23:05:25Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-10-16T17:31:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NJ"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres454is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 454\nIN THE SENATE OF THE UNITED STATES\nOctober 16, 2025 Mr. Welch submitted the following resolution; which was referred to the Committee on Environment and Public Works\nRESOLUTION\nExpressing support for the designation of the week of October 24, 2025, to October 31, 2025, as Bat Week .\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of the week of October 24, 2025, to October 31, 2025, as Bat Week ;\n**(2)**\nencourages the observance of Bat Week with appropriate events and activities;\n**(3)**\nacknowledges the important role bats play as pollinators and pest control for agriculture; and\n**(4)**\nintends to\u2014\n**(A)**\ncontinue working to conserve bat species and their habitat; and\n**(B)**\nwork to defeat the disease known as white-nose syndrome.",
      "versionDate": "2025-10-16",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres454ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 454\nIN THE SENATE OF THE UNITED STATES\nOctober 16, 2025 Mr. Welch (for himself, Mr. Booker , and Mr. Van Hollen ) submitted the following resolution; which was referred to the Committee on Environment and Public Works\nOctober 28, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nExpressing support for the designation of the week of October 24, 2025, to October 31, 2025, as Bat Week .\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of the week of October 24, 2025, to October 31, 2025, as Bat Week ;\n**(2)**\nencourages the observance of Bat Week with appropriate events and activities;\n**(3)**\nacknowledges the important role bats play as pollinators and pest control for agriculture; and\n**(4)**\nintends to\u2014\n**(A)**\ncontinue working to conserve bat species and their habitat; and\n**(B)**\nwork to defeat the disease known as white-nose syndrome.",
      "versionDate": "2025-10-28",
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
        "actionDate": "2025-10-17",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "811",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
      "type": "HRES"
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
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-12-08T16:28:23Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-12-08T16:28:23Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-12-08T16:28:23Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-12-08T16:28:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-12-05T15:59:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-16",
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
          "measure-id": "id119sres454",
          "measure-number": "454",
          "measure-type": "sres",
          "orig-publish-date": "2025-10-16",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres454v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses support for the designation of the week of October 24-October 31, 2025, as Bat\u00a0Week and acknowledges the important role bats play as pollinators and pest control for agriculture.</p>"
        },
        "title": "A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres454.xml",
    "summary": {
      "actionDate": "2025-10-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses support for the designation of the week of October 24-October 31, 2025, as Bat\u00a0Week and acknowledges the important role bats play as pollinators and pest control for agriculture.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres454"
    },
    "title": "A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses support for the designation of the week of October 24-October 31, 2025, as Bat\u00a0Week and acknowledges the important role bats play as pollinators and pest control for agriculture.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119sres454"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres454is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres454ats.xml"
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
      "title": "A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:20Z"
    },
    {
      "title": "A resolution expressing support for the designation of the week of October 24, 2025, to October 31, 2025, as \"Bat Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T10:56:15Z"
    }
  ]
}
```
