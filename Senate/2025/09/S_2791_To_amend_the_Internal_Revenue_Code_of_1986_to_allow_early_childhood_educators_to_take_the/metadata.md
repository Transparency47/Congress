# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2791?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2791
- Title: SEED Act
- Congress: 119
- Bill type: S
- Bill number: 2791
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2026-04-06T15:38:22Z
- Update date including text: 2026-04-06T15:38:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2791",
    "number": "2791",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "SEED Act",
    "type": "S",
    "updateDate": "2026-04-06T15:38:22Z",
    "updateDateIncludingText": "2026-04-06T15:38:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T19:30:25Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2791is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2791\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Bennet (for himself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow early childhood educators to take the educator expense deduction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Early-childhood Educators\u2019 Deductions Act or the SEED Act .\n#### 2. Educator expense deduction to include early childhood educators\n##### (a) In general\nSection 62 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a)(2)(D), by striking elementary and secondary in the heading and inserting early childhood, elementary, and secondary ;\n**(2)**\nin subsection (d)(1)(A), by striking kindergarten through grade 12 teacher and inserting, early childhood or kindergarten through grade 12 teacher, educator ; and\n**(3)**\nin subsection (d)(1)(B), by striking elementary education or secondary education and inserting early childhood education (through pre-kindergarten) or elementary or secondary education .\n##### (b) Effective date\nThe amendments made by this section shall apply to expenses incurred in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-09-11",
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
        "updateDate": "2025-09-29T18:53:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-11",
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
          "measure-id": "id119s2791",
          "measure-number": "2791",
          "measure-type": "s",
          "orig-publish-date": "2025-09-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2791v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-09-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting Early-childhood Educators' Deductions Act or the SEED Act</strong></p><p>This bill expands\u00a0eligibility for the above-the-line federal tax deduction for certain eligible educator expenses to include early childhood educators. (An above-the-line tax deduction is subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, kindergarten through grade 12 teachers, instructors, counselors, principals, or aides in schools that provide\u00a0elementary or secondary education are allowed an above-the-line tax deduction of up to $300 (in 2025 and adjusted annually) for certain unreimbursed professional development and classroom expenses. (Other conditions apply.)</p><p>The bill expands eligibility for the tax deduction for such educator expenses to include early childhood educators in schools that provide early childhood (pre-kindergarten) education.\u00a0</p>"
        },
        "title": "SEED Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2791.xml",
    "summary": {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Early-childhood Educators' Deductions Act or the SEED Act</strong></p><p>This bill expands\u00a0eligibility for the above-the-line federal tax deduction for certain eligible educator expenses to include early childhood educators. (An above-the-line tax deduction is subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, kindergarten through grade 12 teachers, instructors, counselors, principals, or aides in schools that provide\u00a0elementary or secondary education are allowed an above-the-line tax deduction of up to $300 (in 2025 and adjusted annually) for certain unreimbursed professional development and classroom expenses. (Other conditions apply.)</p><p>The bill expands eligibility for the tax deduction for such educator expenses to include early childhood educators in schools that provide early childhood (pre-kindergarten) education.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2791"
    },
    "title": "SEED Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Early-childhood Educators' Deductions Act or the SEED Act</strong></p><p>This bill expands\u00a0eligibility for the above-the-line federal tax deduction for certain eligible educator expenses to include early childhood educators. (An above-the-line tax deduction is subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, kindergarten through grade 12 teachers, instructors, counselors, principals, or aides in schools that provide\u00a0elementary or secondary education are allowed an above-the-line tax deduction of up to $300 (in 2025 and adjusted annually) for certain unreimbursed professional development and classroom expenses. (Other conditions apply.)</p><p>The bill expands eligibility for the tax deduction for such educator expenses to include early childhood educators in schools that provide early childhood (pre-kindergarten) education.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2791"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2791is.xml"
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
      "title": "SEED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SEED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Early-childhood Educators\u2019 Deductions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow early childhood educators to take the educator expense deduction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T03:48:13Z"
    }
  ]
}
```
