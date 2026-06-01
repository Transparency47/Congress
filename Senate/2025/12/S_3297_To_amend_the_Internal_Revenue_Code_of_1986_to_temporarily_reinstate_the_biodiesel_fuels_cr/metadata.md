# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3297
- Title: CROP Act
- Congress: 119
- Bill type: S
- Bill number: 3297
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2025-12-19T20:15:38Z
- Update date including text: 2025-12-19T20:15:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3297",
    "number": "3297",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "CROP Act",
    "type": "S",
    "updateDate": "2025-12-19T20:15:38Z",
    "updateDateIncludingText": "2025-12-19T20:15:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T17:00:27Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3297is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3297\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to temporarily reinstate the biodiesel fuels credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Consumer Relief and Opportunities for Producers Act or the CROP Act .\n#### 2. Temporary reinstatement of biodiesel fuels credit\n##### (a) In general\nSection 40A(g) of the Internal Revenue Code of 1986 is amended by striking December 31, 2024 and inserting May 31, 2026 .\n##### (b) No double benefit\nSection 40A of the Internal Revenue Code of 1986, as amended by subsection (a), is further amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (h), and\n**(2)**\nby inserting after subsection (f) the following new subsection:\n(g) No double benefit Except as provided under subsection (b)(4)(D), no credit shall be determined under this section with respect to any fuel for which a credit determined under section 45Z is allowed under section 38. .\n##### (c) Conforming amendments\n**(1)**\nSection 6426(c)(6) of the Internal Revenue Code of 1986 is amended by striking December 31, 2024 and inserting May 31, 2026 .\n**(2)**\nSection 6427(e)(6)(B) of such Code is amended by striking December 31, 2024 and inserting May 31, 2026 .\n##### (d) Effective date\nThe amendments made by this section shall apply to fuel used or sold after November 30, 2025.",
      "versionDate": "2025-12-02",
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
        "name": "Taxation",
        "updateDate": "2025-12-19T20:15:38Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3297is.xml"
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
      "title": "CROP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CROP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Consumer Relief and Opportunities for Producers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to temporarily reinstate the biodiesel fuels credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:58Z"
    }
  ]
}
```
