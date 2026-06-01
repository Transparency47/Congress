# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/6?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/6
- Title: A concurrent resolution expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States.
- Congress: 119
- Bill type: SCONRES
- Bill number: 6
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2026-05-14T10:56:40Z
- Update date including text: 2026-05-14T10:56:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Referred to the Committee on Finance. (text: CR S374)
- 2025-01-24 - IntroReferral: Submitted in Senate
- Latest action: 2025-01-24: Submitted in Senate

## Actions

- 2025-01-24 - IntroReferral: Referred to the Committee on Finance. (text: CR S374)
- 2025-01-24 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/6",
    "number": "6",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A concurrent resolution expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States.",
    "type": "SCONRES",
    "updateDate": "2026-05-14T10:56:40Z",
    "updateDateIncludingText": "2026-05-14T10:56:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Finance. (text: CR S374)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
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
            "date": "2025-01-24T18:33:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-24T18:33:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "MN"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "CO"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ID"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "IL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "CT"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "WI"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "AZ"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OK"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "OR"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "SD"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "MI"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WY"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IN"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "MI"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "SD"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "KS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NE"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NH"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres6is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 6\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Crapo (for himself, Ms. Smith , Mr. Grassley , Mr. Hickenlooper , Mr. Risch , Ms. Klobuchar , Mr. Tillis , Mr. Durbin , Mr. Cramer , Mr. Blumenthal , Mr. Hoeven , Ms. Baldwin , Mr. Daines , Mr. Kelly , Mr. Lankford , Mr. Merkley , Mr. Thune , Mr. Peters , Ms. Lummis , and Mr. Young ) submitted the following concurrent resolution; which was referred to the Committee on Finance\nCONCURRENT RESOLUTION\nExpressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States.\nThat it is the sense of Congress that\u2014\n**(1)**\nthe fraternal benefit society model is a successful private sector economic and social support system that helps meet needs that would otherwise go unmet;\n**(2)**\nthe provision of payment for life, health, accident, or other benefits to the members of fraternal benefit societies in accordance with section 501(c)(8) of the Internal Revenue Code of 1986 is necessary to support the charitable and fraternal activities of the volunteer chapters within the communities of fraternal benefit societies;\n**(3)**\nfraternal benefit societies have adapted since 1909 to better serve their members and the public; and\n**(4)**\nthe exemption from taxation under section 501(c)(8) of the Internal Revenue Code of 1986 of fraternal benefit societies continues to generate significant returns to the United States, and the work of fraternal benefit societies should continue to be promoted.",
      "versionDate": "2025-01-24",
      "versionType": "IS"
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States.",
      "type": "HCONRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-01-28T17:14:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119sconres6",
          "measure-number": "6",
          "measure-type": "sconres",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-01-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sconres6v00",
            "update-date": "2025-01-30"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This concurrent resolution expresses the sense of Congress that tax-exempt fraternal benefit societies serve as a private economic and social support system,\u00a0providing benefits to their members\u00a0is necessary to support the charitable and fraternal activities of the volunteer chapters,\u00a0and their work should continue to be promoted.</p>"
        },
        "title": "A concurrent resolution expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sconres/BILLSUM-119sconres6.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This concurrent resolution expresses the sense of Congress that tax-exempt fraternal benefit societies serve as a private economic and social support system,\u00a0providing benefits to their members\u00a0is necessary to support the charitable and fraternal activities of the volunteer chapters,\u00a0and their work should continue to be promoted.</p>",
      "updateDate": "2025-01-30",
      "versionCode": "id119sconres6"
    },
    "title": "A concurrent resolution expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This concurrent resolution expresses the sense of Congress that tax-exempt fraternal benefit societies serve as a private economic and social support system,\u00a0providing benefits to their members\u00a0is necessary to support the charitable and fraternal activities of the volunteer chapters,\u00a0and their work should continue to be promoted.</p>",
      "updateDate": "2025-01-30",
      "versionCode": "id119sconres6"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres6is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A concurrent resolution expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-28T01:48:24Z"
    },
    {
      "title": "A concurrent resolution expressing the sense of Congress that tax-exempt fraternal benefit societies have historically provided and continue to provide critical benefits to the people and communities of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-25T11:56:22Z"
    }
  ]
}
```
