# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2235
- Title: Diesel Emissions Reduction Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2235
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2026-04-17T12:24:50Z
- Update date including text: 2026-04-17T12:24:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 226.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Ordered to be reported without amendment favorably.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Committee: Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.
- 2025-10-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 226.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2235",
    "number": "2235",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Diesel Emissions Reduction Act of 2025",
    "type": "S",
    "updateDate": "2026-04-17T12:24:50Z",
    "updateDateIncludingText": "2026-04-17T12:24:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 226.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-29",
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
      "text": "Committee on Environment and Public Works. Reported by Senator Capito without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
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
            "date": "2025-10-29T21:32:09Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-29T14:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-10T14:35:58Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "WV"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NJ"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "AK"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "DE"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2235is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2235\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Whitehouse (for himself, Mrs. Capito , Mr. Booker , Mr. Sullivan , Ms. Blunt Rochester , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Energy Policy Act of 2005 to reauthorize the diesel emissions reduction program.\n#### 1. Short title\nThis Act may be cited as the Diesel Emissions Reduction Act of 2025 .\n#### 2. Reauthorization of Diesel Emissions Reduction Act\nSection 797(a) of the Energy Policy Act of 2005 ( 42 U.S.C. 16137(a) ) is amended by striking 2024 and inserting 2029 .",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2235rs.xml",
      "text": "II\nCalendar No. 226\n119th CONGRESS\n1st Session\nS. 2235\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Whitehouse (for himself, Mrs. Capito , Mr. Booker , Mr. Sullivan , Ms. Blunt Rochester , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nOctober 29, 2025 Reported by Mrs. Capito , without amendment\nA BILL\nTo amend the Energy Policy Act of 2005 to reauthorize the diesel emissions reduction program.\n#### 1. Short title\nThis Act may be cited as the Diesel Emissions Reduction Act of 2025 .\n#### 2. Reauthorization of Diesel Emissions Reduction Act\nSection 797(a) of the Energy Policy Act of 2005 ( 42 U.S.C. 16137(a) ) is amended by striking 2024 and inserting 2029 .",
      "versionDate": "2025-10-29",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2140",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Diesel Emissions Reduction Act of 2025",
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
            "name": "Air quality",
            "updateDate": "2026-01-20T19:48:29Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2026-01-20T19:48:38Z"
          },
          {
            "name": "Motor fuels",
            "updateDate": "2026-01-20T19:48:44Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-01-20T19:48:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-07-29T15:03:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-10",
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
          "measure-id": "id119s2235",
          "measure-number": "2235",
          "measure-type": "s",
          "orig-publish-date": "2025-07-10",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": [
          {
            "@attributes": {
              "currentChamber": "SENATE",
              "summary-id": "id119s2235v25",
              "update-date": "2026-04-08"
            },
            "action-date": "2025-10-29",
            "action-desc": "Reported to Senate",
            "summary-text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>"
          },
          {
            "@attributes": {
              "currentChamber": "SENATE",
              "summary-id": "id119s2235v00",
              "update-date": "2026-04-17"
            },
            "action-date": "2025-07-10",
            "action-desc": "Introduced in Senate",
            "summary-text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>"
          }
        ],
        "title": "Diesel Emissions Reduction Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2235.xml",
    "summary": {
      "actionDate": "2025-10-29",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2235"
    },
    "title": "Diesel Emissions Reduction Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-29",
      "actionDesc": "Reported to Senate",
      "text": "<p><strong>Diesel Emissions Reduction Act of 2025 </strong></p><p>This bill reauthorizes through FY2029 a diesel emissions reduction program under which the Environmental Protection Agency provides grants, rebates, or loans for replacing diesel engines or retrofitting the engines with pollution control technologies.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s2235"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2235is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2235rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Diesel Emissions Reduction Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-31T04:23:13Z"
    },
    {
      "title": "Diesel Emissions Reduction Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Diesel Emissions Reduction Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Energy Policy Act of 2005 to reauthorize the diesel emissions reduction program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:33:23Z"
    }
  ]
}
```
