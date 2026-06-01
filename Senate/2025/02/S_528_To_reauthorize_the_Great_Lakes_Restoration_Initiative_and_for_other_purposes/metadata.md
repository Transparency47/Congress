# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/528
- Title: GLRI Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 528
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-05-27T17:29:07Z
- Update date including text: 2026-05-27T17:29:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2026-04-15 - Committee: Committee on Environment and Public Works. Hearings held.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2026-04-15 - Committee: Committee on Environment and Public Works. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/528",
    "number": "528",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "GLRI Act of 2025",
    "type": "S",
    "updateDate": "2026-05-27T17:29:07Z",
    "updateDateIncludingText": "2026-05-27T17:29:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
            "date": "2026-04-15T17:58:51Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-11T21:16:22Z",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "IN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "MN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "OH"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "OH"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "IL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "MN"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "MI"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s528is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 528\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Peters (for himself, Mr. Young , Ms. Klobuchar , Mr. Moreno , Ms. Baldwin , Mr. Husted , Mr. Durbin , Ms. Smith , Mrs. Gillibrand , Mr. Fetterman , Ms. Slotkin , Mr. Schumer , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo reauthorize the Great Lakes Restoration Initiative, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Great Lakes Restoration Initiative Act of 2025 or the GLRI Act of 2025 .\n#### 2. Great lakes restoration initiative reauthorization\nSection 118(c)(7)(J)(i) of the Federal Water Pollution Control Act ( 33 U.S.C. 1268(c)(7)(J)(i) ) is amended\u2014\n**(1)**\nin subclause (V), by striking and at the end;\n**(2)**\nin subclause (VI), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(VII) $500,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-10",
        "text": "Referred to the Subcommittee on Water Resources and Environment."
      },
      "number": "284",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GLRI Act of 2025",
      "type": "HR"
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
            "name": "Aquatic ecology",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Great Lakes",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Illinois",
            "updateDate": "2026-05-27T17:28:17Z"
          },
          {
            "name": "Indiana",
            "updateDate": "2026-05-27T17:28:25Z"
          },
          {
            "name": "Lakes and rivers",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Marine pollution",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Michigan",
            "updateDate": "2026-05-27T17:28:32Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2026-05-27T17:28:38Z"
          },
          {
            "name": "New York State",
            "updateDate": "2026-05-27T17:28:45Z"
          },
          {
            "name": "Ohio",
            "updateDate": "2026-05-27T17:28:52Z"
          },
          {
            "name": "Pennsylvania",
            "updateDate": "2026-05-27T17:28:58Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-05-27T17:28:09Z"
          },
          {
            "name": "Wisconsin",
            "updateDate": "2026-05-27T17:29:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-03-12T17:22:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119s528",
          "measure-number": "528",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-03-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s528v00",
            "update-date": "2025-03-28"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Great Lakes Restoration Initiative Act of 2025 or the\u00a0GLRI Act of 2025</strong></p><p>This bill reauthorizes through FY2031 the Great Lakes Restoration Initiative, which carries out programs and projects to protect and restore the Great Lakes.</p>"
        },
        "title": "GLRI Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s528.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Great Lakes Restoration Initiative Act of 2025 or the\u00a0GLRI Act of 2025</strong></p><p>This bill reauthorizes through FY2031 the Great Lakes Restoration Initiative, which carries out programs and projects to protect and restore the Great Lakes.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s528"
    },
    "title": "GLRI Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Great Lakes Restoration Initiative Act of 2025 or the\u00a0GLRI Act of 2025</strong></p><p>This bill reauthorizes through FY2031 the Great Lakes Restoration Initiative, which carries out programs and projects to protect and restore the Great Lakes.</p>",
      "updateDate": "2025-03-28",
      "versionCode": "id119s528"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s528is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "GLRI Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GLRI Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Great Lakes Restoration Initiative Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Great Lakes Restoration Initiative, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:50Z"
    }
  ]
}
```
