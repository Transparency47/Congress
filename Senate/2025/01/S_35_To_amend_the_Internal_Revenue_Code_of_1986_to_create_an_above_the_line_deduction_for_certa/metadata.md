# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/35?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/35
- Title: Homeowners Premium Tax Reduction Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 35
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2025-09-10T20:29:41Z
- Update date including text: 2025-09-10T20:29:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/35",
    "number": "35",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Homeowners Premium Tax Reduction Act of 2025",
    "type": "S",
    "updateDate": "2025-09-10T20:29:41Z",
    "updateDateIncludingText": "2025-09-10T20:29:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
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
      "actionDate": "2025-01-08",
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
          "date": "2025-01-08T18:51:07Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s35is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 35\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to create an above the line deduction for certain homeowners insurance premiums.\n#### 1. Short title\nThis Act may be cited as the Homeowners Premium Tax Reduction Act of 2025 .\n#### 2. Deduction for homeowners insurance premiums\n##### (a) In general\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Homeowners insurance premiums (a) Allowance of deduction In the case of an individual, there shall be allowed as a deduction an amount equal to so much of the qualified insurance premiums paid or incurred during the taxable year as does not exceed $10,000. (b) Qualified insurance premiums For purposes of this section, with respect to an individual, the term qualified insurance premiums means annual policy premiums paid or incurred for homeowners insurance with respect to the principal residence of the individual. (c) Principal residence For purposes of this section, the term principal residence has the same meaning as when used in section 121. .\n##### (b) Deduction allowed in determining adjusted gross income\nSection 62(a) of the Internal Revenue Code of 1986 is amended by inserting after paragraph (21) the following new paragraph:\n(22) Homeowners insurance premiums The deduction allowed by section 224. .\n##### (c) Clerical amendment\nThe table of sections for part VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by striking the item relating to section 224 and by inserting after the item relating to section 223 the following new items:\nSec. 224. Homeowners insurance premiums. Sec. 225. Cross reference. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-01-08",
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
            "name": "Income tax deductions",
            "updateDate": "2025-09-10T20:29:31Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2025-09-10T20:29:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-14T18:55:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s35",
          "measure-number": "35",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s35v00",
            "update-date": "2025-03-12"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Homeowners Premium Tax Reduction Act of 2025\u00a0</strong></p><p>This bill establishes a new deduction of up to $10,000 claimed against gross income (above-the-line tax deduction) for annual policy premiums paid or incurred for homeowners insurance on an individual's principal residence.\u00a0</p>"
        },
        "title": "Homeowners Premium Tax Reduction Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s35.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Homeowners Premium Tax Reduction Act of 2025\u00a0</strong></p><p>This bill establishes a new deduction of up to $10,000 claimed against gross income (above-the-line tax deduction) for annual policy premiums paid or incurred for homeowners insurance on an individual's principal residence.\u00a0</p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119s35"
    },
    "title": "Homeowners Premium Tax Reduction Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Homeowners Premium Tax Reduction Act of 2025\u00a0</strong></p><p>This bill establishes a new deduction of up to $10,000 claimed against gross income (above-the-line tax deduction) for annual policy premiums paid or incurred for homeowners insurance on an individual's principal residence.\u00a0</p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119s35"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s35is.xml"
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
      "title": "Homeowners Premium Tax Reduction Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Homeowners Premium Tax Reduction Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to create an above the line deduction for certain homeowners insurance premiums.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:18Z"
    }
  ]
}
```
