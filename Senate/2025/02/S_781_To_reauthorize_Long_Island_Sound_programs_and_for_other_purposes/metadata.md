# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/781?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/781
- Title: Long Island Sound Restoration and Stewardship Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 781
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-04-15T15:01:04Z
- Update date including text: 2026-04-15T15:01:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/781",
    "number": "781",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T15:01:04Z",
    "updateDateIncludingText": "2026-04-15T15:01:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T17:39:51Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s781is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 781\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mrs. Gillibrand (for herself, Mr. Schumer , Mr. Blumenthal , and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo reauthorize Long Island Sound programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Long Island Sound Restoration and Stewardship Reauthorization Act of 2025 .\n#### 2. Reauthorization of Long Island Sound Programs\n##### (a) Long island sound grants\nSection 119(h) of the Federal Water Pollution Control Act ( 33 U.S.C. 1269(h) ) is amended by striking 2019 through 2023 and inserting 2025 through 2029 .\n##### (b) Long island sound stewardship grants\nSection 11(a) of the Long Island Sound Stewardship Act of 2006 ( 33 U.S.C. 1269 note; Public Law 109\u2013359 ) is amended, in the matter preceding paragraph (1), by striking 2019 through 2023 and inserting 2025 through 2029 .\n##### (c) Technical amendment\nSection 119(g) of the Federal Water Pollution Control Act ( 33 U.S.C. 1269(g) ) is amended by redesignating paragraph (4) as paragraph (3).",
      "versionDate": "2025-02-27",
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
      "number": "288",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-05-16T17:46:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s781",
          "measure-number": "781",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s781v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Long Island Sound Restoration and Stewardship Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the Environmental Protection Agency's Long Island Sound programs through FY2029. The programs, which include\u00a0a stewardship grant program, focus on conserving and restoring the estuary off the coast of New York and Connecticut.</p>"
        },
        "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s781.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Long Island Sound Restoration and Stewardship Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the Environmental Protection Agency's Long Island Sound programs through FY2029. The programs, which include\u00a0a stewardship grant program, focus on conserving and restoring the estuary off the coast of New York and Connecticut.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s781"
    },
    "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Long Island Sound Restoration and Stewardship Reauthorization Act of 2025</strong></p><p>This bill reauthorizes the Environmental Protection Agency's Long Island Sound programs through FY2029. The programs, which include\u00a0a stewardship grant program, focus on conserving and restoring the estuary off the coast of New York and Connecticut.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s781"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s781is.xml"
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
      "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Long Island Sound Restoration and Stewardship Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize Long Island Sound programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:22Z"
    }
  ]
}
```
