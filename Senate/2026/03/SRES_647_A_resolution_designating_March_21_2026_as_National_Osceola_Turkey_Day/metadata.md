# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/647
- Title: A resolution designating March 21, 2026, as "National Osceola Turkey Day".
- Congress: 119
- Bill type: SRES
- Bill number: 647
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-13T12:19:23Z
- Update date including text: 2026-04-13T12:19:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1095)
- 2026-03-17 - IntroReferral: Submitted in Senate
- 2026-03-27 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-03-27 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1690)
- 2026-03-27 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-03-27 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2026-03-17: Submitted in Senate

## Actions

- 2026-03-17 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1095)
- 2026-03-17 - IntroReferral: Submitted in Senate
- 2026-03-27 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-03-27 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1690)
- 2026-03-27 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2026-03-27 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/647",
    "number": "647",
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
    "title": "A resolution designating March 21, 2026, as \"National Osceola Turkey Day\".",
    "type": "SRES",
    "updateDate": "2026-04-13T12:19:23Z",
    "updateDateIncludingText": "2026-04-13T12:19:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1690)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-27",
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
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1095)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-03-17",
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
            "date": "2026-03-27T06:32:12Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-17T20:25:52Z",
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres647is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 647\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Scott of Florida (for himself and Mrs. Moody ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating March 21, 2026, as National Osceola Turkey Day .\nThat the Senate\u2014\n**(1)**\ndesignates March 21, 2026, as National Osceola Turkey Day ; and\n**(2)**\nencourages the people of the United States to observe National Osceola Turkey Day with appropriate ceremonies and activities.",
      "versionDate": "2026-03-17",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres647ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 647\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Scott of Florida (for himself and Mrs. Moody ) submitted the following resolution; which was referred to the Committee on the Judiciary\nMarch 27 (legislative day, March 26), 2026 Committee discharged; considered and agreed to\nRESOLUTION\nDesignating March 21, 2026, as National Osceola Turkey Day .\nThat the Senate\u2014\n**(1)**\ndesignates March 21, 2026, as National Osceola Turkey Day ; and\n**(2)**\nencourages the people of the United States to observe National Osceola Turkey Day with appropriate ceremonies and activities.",
      "versionDate": "2026-03-27",
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
        "actionDate": "2025-03-24",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1807; text: CR S1806)"
      },
      "number": "134",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating March 15, 2025, as \"National Osceola Turkey Day\".",
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
            "updateDate": "2026-03-30T17:59:00Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2026-03-30T17:59:00Z"
          },
          {
            "name": "Florida",
            "updateDate": "2026-03-30T17:59:00Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2026-03-30T17:59:00Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2026-04-03T15:38:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-27",
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
          "measure-id": "id119sres647",
          "measure-number": "647",
          "measure-type": "sres",
          "orig-publish-date": "2026-03-27",
          "originChamber": "SENATE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres647v55",
            "update-date": "2026-04-13"
          },
          "action-date": "2026-03-27",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution designates March 21, 2026, as National Osceola Turkey Day.</p>"
        },
        "title": "A resolution designating March 21, 2026, as \"National Osceola Turkey Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres647.xml",
    "summary": {
      "actionDate": "2026-03-27",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates March 21, 2026, as National Osceola Turkey Day.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119sres647"
    },
    "title": "A resolution designating March 21, 2026, as \"National Osceola Turkey Day\"."
  },
  "summaries": [
    {
      "actionDate": "2026-03-27",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution designates March 21, 2026, as National Osceola Turkey Day.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119sres647"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres647is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres647ats.xml"
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
      "title": "A resolution designating March 21, 2026, as \"National Osceola Turkey Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:48:38Z"
    },
    {
      "title": "A resolution designating March 21, 2026, as \"National Osceola Turkey Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T10:56:21Z"
    }
  ]
}
```
