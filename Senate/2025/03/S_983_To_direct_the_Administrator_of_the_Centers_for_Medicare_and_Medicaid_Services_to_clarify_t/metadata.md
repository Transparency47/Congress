# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/983?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/983
- Title: Hearing Device Coverage Clarification Act
- Congress: 119
- Bill type: S
- Bill number: 983
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-02-19T22:27:08Z
- Update date including text: 2026-02-19T22:27:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/983",
    "number": "983",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Hearing Device Coverage Clarification Act",
    "type": "S",
    "updateDate": "2026-02-19T22:27:08Z",
    "updateDateIncludingText": "2026-02-19T22:27:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:29:19Z",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s983is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 983\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Ms. Klobuchar (for herself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo direct the Administrator of the Centers for Medicare & Medicaid Services to clarify that implanted active middle ear hearing devices are prosthetics and are not subject to the hearing aid coverage exclusion under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Hearing Device Coverage Clarification Act .\n#### 2. Active middle ear implant coverage\n##### (a) In general\nNot later than 60 days after the date of enactment of this Act, the Administrator of the Centers for Medicare & Medicaid Services shall clarify that implanted active middle ear hearing devices are prosthetics that are not subject to the hearing aid coverage exclusion under section 1862(a)(7) of the Social Security Act ( 42 U.S.C. 1395y(a)(7) ).\n##### (b) Prosthetic defined\nThe term prosthetic has the meaning given such term in section 414.202 of title 42, Code of Federal Regulations (or a successor regulation).",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-06",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1921",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hearing Device Coverage Clarification Act",
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
        "name": "Health",
        "updateDate": "2025-03-31T16:03:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s983",
          "measure-number": "983",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s983v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Hearing Device Coverage Clarification Act</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services to specify that implanted active middle ear hearing devices are prosthetics (not hearing aids) and are covered under Medicare.</p>"
        },
        "title": "Hearing Device Coverage Clarification Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s983.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hearing Device Coverage Clarification Act</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services to specify that implanted active middle ear hearing devices are prosthetics (not hearing aids) and are covered under Medicare.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s983"
    },
    "title": "Hearing Device Coverage Clarification Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hearing Device Coverage Clarification Act</strong></p><p>This bill requires the Centers for Medicare & Medicaid Services to specify that implanted active middle ear hearing devices are prosthetics (not hearing aids) and are covered under Medicare.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s983"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s983is.xml"
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
      "title": "Hearing Device Coverage Clarification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hearing Device Coverage Clarification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Administrator of the Centers for Medicare & Medicaid Services to clarify that implanted active middle ear hearing devices are prosthetics and are not subject to the hearing aid coverage exclusion under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:06Z"
    }
  ]
}
```
