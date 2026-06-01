# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/486?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/486
- Title: Mandatory Removal Proceedings Act
- Congress: 119
- Bill type: S
- Bill number: 486
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-03-03T01:59:38Z
- Update date including text: 2026-03-03T01:59:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/486",
    "number": "486",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Mandatory Removal Proceedings Act",
    "type": "S",
    "updateDate": "2026-03-03T01:59:38Z",
    "updateDateIncludingText": "2026-03-03T01:59:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
        "item": {
          "date": "2025-02-06T22:34:36Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "TX"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MO"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "LA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s486is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 486\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Lee (for himself, Mr. Cruz , Mr. Hawley , Mr. Cassidy , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Secretary of Homeland Security to immediately initiate removal proceedings for aliens whose visas are revoked on security or related grounds.\n#### 1. Short title\nThis Act may be cited as the Mandatory Removal Proceedings Act .\n#### 2. Mandatory initiation of removal proceedings for aliens whose visas are revoked on security or related grounds\nSection 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ) is amended\u2014\n**(1)**\nby striking After the issuance and inserting the following:\nVisa revocation .\u2014 (1) In general After ;\n**(2)**\nby striking his discretion and inserting in the discretion of the Secretary ;\n**(3)**\nby striking Attorney General and inserting Secretary of Homeland Security ;\n**(4)**\nby striking issuance: Provided, That carriers and inserting the following:\nissuance. (2) Exception Carriers ; and\n**(5)**\nby striking There shall be no means and inserting the following:\n(3) Mandatory removal proceedings If the visa of an alien is revoked pursuant to paragraph (1) as a result of a ground for removal described in section 237(a)(4), the Secretary of Homeland Security shall immediately initiate removal proceedings for such alien in accordance with section 236A. (4) Judicial review There shall be no means .",
      "versionDate": "2025-02-06",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-12T16:30:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s486",
          "measure-number": "486",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s486v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Mandatory Removal Proceedings Act</strong></p><p>This bill requires the immediate initiation of removal proceedings against a\u00a0non-U.S. national (<em>alien</em> under federal law) whose visa is revoked on security and related grounds.</p>"
        },
        "title": "Mandatory Removal Proceedings Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s486.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mandatory Removal Proceedings Act</strong></p><p>This bill requires the immediate initiation of removal proceedings against a\u00a0non-U.S. national (<em>alien</em> under federal law) whose visa is revoked on security and related grounds.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119s486"
    },
    "title": "Mandatory Removal Proceedings Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Mandatory Removal Proceedings Act</strong></p><p>This bill requires the immediate initiation of removal proceedings against a\u00a0non-U.S. national (<em>alien</em> under federal law) whose visa is revoked on security and related grounds.</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119s486"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s486is.xml"
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
      "title": "Mandatory Removal Proceedings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mandatory Removal Proceedings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Homeland Security to immediately initiate removal proceedings for aliens whose visas are revoked on security or related grounds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:41Z"
    }
  ]
}
```
