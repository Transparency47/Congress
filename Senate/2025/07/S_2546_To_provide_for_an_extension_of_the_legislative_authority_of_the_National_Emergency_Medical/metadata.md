# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2546?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2546
- Title: A bill to provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs.
- Congress: 119
- Bill type: S
- Bill number: 2546
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2546",
    "number": "2546",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A bill to provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
            "date": "2025-12-17T14:30:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-30T20:08:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:21Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "MO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NH"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "LA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "MA"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "WY"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-15",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2546is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2546\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Coons (for himself, Mr. Schmitt , Mrs. Shaheen , Mr. Cassidy , Ms. Warren , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs.\n#### 1. Extension of legislative authority for memorial establishment\nSection 1(b) of Public Law 115\u2013275 (132 Stat. 4164; 40 U.S.C. 8903 note) is amended by striking the period at the end and inserting , except that any reference in section 8903(e) of that title to the expiration at the end of, or extension beyond, a 7-year period shall be considered to be a reference to an expiration on, or extension beyond, November 3, 2032. .",
      "versionDate": "2025-07-30",
      "versionType": "Introduced in Senate"
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
            "name": "Art, artists, authorship",
            "updateDate": "2025-12-11T20:05:19Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-12-11T20:05:26Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-12-11T20:05:10Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2026-01-07T17:16:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-02-06T21:00:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-30",
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
          "measure-id": "id119s2546",
          "measure-number": "2546",
          "measure-type": "s",
          "orig-publish-date": "2025-07-30",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2546v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-07-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill extends the authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia that honors\u00a0the commitment and service of emergency medical services.</p>"
        },
        "title": "A bill to provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2546.xml",
    "summary": {
      "actionDate": "2025-07-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill extends the authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia that honors\u00a0the commitment and service of emergency medical services.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s2546"
    },
    "title": "A bill to provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs."
  },
  "summaries": [
    {
      "actionDate": "2025-07-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill extends the authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia that honors\u00a0the commitment and service of emergency medical services.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s2546"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2546is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:33Z"
    },
    {
      "title": "A bill to provide for an extension of the legislative authority of the National Emergency Medical Services Memorial Foundation to establish a commemorative work in the District of Columbia and its environs.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T10:56:22Z"
    }
  ]
}
```
