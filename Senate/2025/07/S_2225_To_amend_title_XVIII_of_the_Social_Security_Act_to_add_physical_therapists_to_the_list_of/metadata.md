# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2225?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2225
- Title: Prevent Interruptions in Physical Therapy Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2225
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2026-05-12T11:03:32Z
- Update date including text: 2026-05-12T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2225",
    "number": "2225",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Prevent Interruptions in Physical Therapy Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T11:03:32Z",
    "updateDateIncludingText": "2026-05-12T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-09",
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
            "date": "2025-07-09T19:29:50Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-09T19:29:50Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "AR"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "ND"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "IA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "DE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "TN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "LA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "WV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2225is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2225\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Luj\u00e1n (for himself, Mr. Boozman , Mr. Cramer , and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to add physical therapists to the list of providers allowed to utilize locum tenens arrangements under Medicare.\n#### 1. Short title\nThis Act may be cited as the Prevent Interruptions in Physical Therapy Act of 2025 .\n#### 2. Allowing physical therapists to utilize locum tenens arrangements under Medicare\n##### (a) In general\nThe first sentence of section 1842(b)(6) of the Social Security Act ( 42 U.S.C. 1395u(b)(6) ) is amended by striking , and (J) and all that follows through physicians\u2019 services furnished by physicians. and inserting , and (J) in the case of outpatient physical therapy services furnished by physical therapists, subparagraph (D) of this sentence shall apply to such services and therapists in the same manner as such subparagraph applies to physicians\u2019 services furnished by physicians. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply to items and services furnished after the date of the enactment of this Act.",
      "versionDate": "2025-07-09",
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
        "actionDate": "2025-02-24",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1517",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Prevent Interruptions in Physical Therapy Act of 2025",
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
            "name": "Contracts and agency",
            "updateDate": "2026-04-27T17:58:19Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-27T17:58:19Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2026-04-27T17:58:19Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2026-04-27T17:58:19Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2026-04-27T17:58:19Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2026-04-27T17:58:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-09-04T15:27:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-09",
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
          "measure-id": "id119s2225",
          "measure-number": "2225",
          "measure-type": "s",
          "orig-publish-date": "2025-07-09",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2225v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Prevent Interruptions in Physical Therapy Act of 2025</strong><strong></strong></p><p>This bill allows a physical therapist to receive payment under Medicare for services provided to the physical therapist's patients by another physical therapist through a qualifying temporary arrangement, regardless of the geographic area or population served. Currently, physical therapists may only receive payment with respect to such arrangements for services provided in medically underserved, rural, or health professional shortage areas.</p>"
        },
        "title": "Prevent Interruptions in Physical Therapy Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2225.xml",
    "summary": {
      "actionDate": "2025-07-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prevent Interruptions in Physical Therapy Act of 2025</strong><strong></strong></p><p>This bill allows a physical therapist to receive payment under Medicare for services provided to the physical therapist's patients by another physical therapist through a qualifying temporary arrangement, regardless of the geographic area or population served. Currently, physical therapists may only receive payment with respect to such arrangements for services provided in medically underserved, rural, or health professional shortage areas.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2225"
    },
    "title": "Prevent Interruptions in Physical Therapy Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prevent Interruptions in Physical Therapy Act of 2025</strong><strong></strong></p><p>This bill allows a physical therapist to receive payment under Medicare for services provided to the physical therapist's patients by another physical therapist through a qualifying temporary arrangement, regardless of the geographic area or population served. Currently, physical therapists may only receive payment with respect to such arrangements for services provided in medically underserved, rural, or health professional shortage areas.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2225"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2225is.xml"
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
      "title": "Prevent Interruptions in Physical Therapy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prevent Interruptions in Physical Therapy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to add physical therapists to the list of providers allowed to utilize locum tenens arrangements under Medicare.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:32Z"
    }
  ]
}
```
