# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/253
- Title: Abortion Is Not Health Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 253
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-03-03T19:24:39Z
- Update date including text: 2025-03-03T19:24:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/253",
    "number": "253",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Abortion Is Not Health Care Act of 2025",
    "type": "S",
    "updateDate": "2025-03-03T19:24:39Z",
    "updateDateIncludingText": "2025-03-03T19:24:39Z"
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
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T20:11:01Z",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IN"
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MS"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s253is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 253\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Lee (for himself, Mr. Banks , Mr. Daines , Mrs. Hyde-Smith , Mr. Hagerty , Mr. Cramer , Mrs. Blackburn , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide that amounts paid for an abortion are not taken into account for purposes of the deduction for medical expenses.\n#### 1. Short title\nThis Act may be cited as the Abortion Is Not Health Care Act of 2025 .\n#### 2. Amounts paid for abortion not taken into account in determining deduction for medical expenses\n##### (a) In general\nSection 213 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(f) Amounts paid for abortion not taken into account (1) In general An amount paid during the taxable year for an abortion shall not be taken into account under subsection (a). (2) Exceptions Paragraph (1) shall not apply in the case of an abortion with respect to\u2014 (A) a woman suffering from a physical disorder, physical injury, or physical illness, including a life-endangering physical condition caused by or arising from the pregnancy itself, that would, as certified by a physician, place the woman in danger of death unless an abortion is performed, or (B) a pregnancy that is the result of an act of rape or incest. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "73",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Abortion Is Not Health Care Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-03-01T13:12:50Z"
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
          "measure-id": "id119s253",
          "measure-number": "253",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s253v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Abortion Is Not Health Care Act of 2025</strong></p><p>This bill excludes amounts paid for an abortion from the itemized tax deduction for qualified medical and dental expenses, subject to exceptions.\u00a0</p><p>Under current law, individuals who itemize their tax deductions may deduct qualified medical and dental expenses to the extent that such expenses exceed 7.5% of the individual\u2019s adjusted gross income for the tax year. Further, under current law, the calculation of the itemized tax deduction for medical and dental expenses may include amounts paid for a legal abortion.</p><p>Under the bill, amounts paid for an abortion may not be claimed as part of the itemized deduction for medical and dental expenses. However, under the bill, amounts paid for an abortion may be included in the itemized deduction for medical and dental expenses if (1) the pregnancy is the result of rape or incest; or (2) a woman is suffering from a physical disorder, injury, or illness (including a life-endangering\u00a0physical condition caused by or arising from\u00a0the pregnancy itself) that\u00a0would, as certified by a physician,\u00a0place the woman in danger of death if an abortion were not performed.</p>"
        },
        "title": "Abortion Is Not Health Care Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s253.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Abortion Is Not Health Care Act of 2025</strong></p><p>This bill excludes amounts paid for an abortion from the itemized tax deduction for qualified medical and dental expenses, subject to exceptions.\u00a0</p><p>Under current law, individuals who itemize their tax deductions may deduct qualified medical and dental expenses to the extent that such expenses exceed 7.5% of the individual\u2019s adjusted gross income for the tax year. Further, under current law, the calculation of the itemized tax deduction for medical and dental expenses may include amounts paid for a legal abortion.</p><p>Under the bill, amounts paid for an abortion may not be claimed as part of the itemized deduction for medical and dental expenses. However, under the bill, amounts paid for an abortion may be included in the itemized deduction for medical and dental expenses if (1) the pregnancy is the result of rape or incest; or (2) a woman is suffering from a physical disorder, injury, or illness (including a life-endangering\u00a0physical condition caused by or arising from\u00a0the pregnancy itself) that\u00a0would, as certified by a physician,\u00a0place the woman in danger of death if an abortion were not performed.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119s253"
    },
    "title": "Abortion Is Not Health Care Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Abortion Is Not Health Care Act of 2025</strong></p><p>This bill excludes amounts paid for an abortion from the itemized tax deduction for qualified medical and dental expenses, subject to exceptions.\u00a0</p><p>Under current law, individuals who itemize their tax deductions may deduct qualified medical and dental expenses to the extent that such expenses exceed 7.5% of the individual\u2019s adjusted gross income for the tax year. Further, under current law, the calculation of the itemized tax deduction for medical and dental expenses may include amounts paid for a legal abortion.</p><p>Under the bill, amounts paid for an abortion may not be claimed as part of the itemized deduction for medical and dental expenses. However, under the bill, amounts paid for an abortion may be included in the itemized deduction for medical and dental expenses if (1) the pregnancy is the result of rape or incest; or (2) a woman is suffering from a physical disorder, injury, or illness (including a life-endangering\u00a0physical condition caused by or arising from\u00a0the pregnancy itself) that\u00a0would, as certified by a physician,\u00a0place the woman in danger of death if an abortion were not performed.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119s253"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s253is.xml"
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
      "title": "Abortion Is Not Health Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Abortion Is Not Health Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide that amounts paid for an abortion are not taken into account for purposes of the deduction for medical expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:20Z"
    }
  ]
}
```
