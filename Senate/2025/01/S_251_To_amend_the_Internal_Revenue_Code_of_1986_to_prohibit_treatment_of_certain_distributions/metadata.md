# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/251?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/251
- Title: Protecting Life in Health Savings Accounts Act
- Congress: 119
- Bill type: S
- Bill number: 251
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-12-05T21:58:51Z
- Update date including text: 2025-12-05T21:58:51Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/251",
    "number": "251",
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
    "title": "Protecting Life in Health Savings Accounts Act",
    "type": "S",
    "updateDate": "2025-12-05T21:58:51Z",
    "updateDateIncludingText": "2025-12-05T21:58:51Z"
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
          "date": "2025-01-24T20:14:26Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s251is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 251\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Lee (for himself, Mr. Banks , Mr. Daines , Mrs. Hyde-Smith , Mr. Hagerty , Mr. Cramer , Mrs. Blackburn , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to prohibit treatment of certain distributions and reimbursements for certain abortions as qualified medical expenses.\n#### 1. Short title\nThis Act may be cited as the Protecting Life in Health Savings Accounts Act .\n#### 2. Distributions for certain abortions not qualified\n##### (a) HSAs\n**(1) In general**\nSubparagraph (A) of section 223(d)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following: Such term shall not include any amount paid for an abortion (other than an excluded abortion). .\n**(2) Excluded abortion**\nSection 223(d)(2) of such Code is amended by adding at the end the following new subparagraph:\n(E) Excluded abortion For purposes of this paragraph, the term excluded abortion means any abortion\u2014 (i) with respect to a pregnancy that is the result of an act of rape or incest, or (ii) with respect to which the woman suffers from a physical disorder, physical injury, or physical illness, including a life-endangering physical condition caused by or arising from the pregnancy itself, that would, as certified by a physician, place the woman in danger of death unless the abortion is performed. .\n##### (b) Archer MSAs\nSubparagraph (A) of section 220(d)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following: Such term shall not include any amount paid for an abortion (other than an excluded abortion (as defined in section 223(d)(2)(E)). .\n##### (c) Health flexible spending arrangements and health reimbursement arrangements\nSection 106 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(h) Prohibition on reimbursements for abortions For purposes of this section and section 105, reimbursement for expenses incurred for an abortion (other than an excluded abortion (as defined in section 223(d)(2)(E)) shall not be treated as a reimbursement for medical expenses. .\n##### (d) Retiree health accounts\nSection 401(h) of the Internal Revenue Code of 1986 is amended by inserting (other than an expense for an abortion (other than an excluded abortion (as defined in section 223(d)(2)(E)))) after sickness, accident, hospitalization, and medical expenses in the matter preceding paragraph (1).\n##### (e) Effective dates\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to amounts paid with respect to taxable years beginning after December 31, 2025.\n**(2) Reimbursements**\nThe amendment made by subsection (c) shall apply to expenses incurred with respect to taxable years beginning after December 31, 2025.",
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
        "actionDate": "2025-01-24",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "720",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Life in Health Savings Accounts Act",
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
        "updateDate": "2025-04-07T16:08:48Z"
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
          "measure-id": "id119s251",
          "measure-number": "251",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s251v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Life in Health Savings Accounts Act</strong></p><p>This bill excludes expenses paid for an abortion from qualified medical expenses eligible for reimbursement from certain tax-exempt savings accounts. (Some exceptions apply.)</p><p>Under the bill, amounts paid for an abortion, other than an excluded abortion, are not qualified medical expenses eligible for reimbursement from a health savings account, Archer medical savings account, health flexible spending arrangement, health reimbursement arrangement, or retiree health account.</p><p>The bill defines <em>excluded abortion</em> as any abortion (1) related to a pregnancy that is the result of rape or incest; or (2)\u00a0performed because a woman is suffering from a physical disorder, injury, or illness (including a life-endangering physical condition caused by or arising from the pregnancy itself) that would, as certified by a physician, place the woman in danger of death if an abortion were not performed.</p>"
        },
        "title": "Protecting Life in Health Savings Accounts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s251.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life in Health Savings Accounts Act</strong></p><p>This bill excludes expenses paid for an abortion from qualified medical expenses eligible for reimbursement from certain tax-exempt savings accounts. (Some exceptions apply.)</p><p>Under the bill, amounts paid for an abortion, other than an excluded abortion, are not qualified medical expenses eligible for reimbursement from a health savings account, Archer medical savings account, health flexible spending arrangement, health reimbursement arrangement, or retiree health account.</p><p>The bill defines <em>excluded abortion</em> as any abortion (1) related to a pregnancy that is the result of rape or incest; or (2)\u00a0performed because a woman is suffering from a physical disorder, injury, or illness (including a life-endangering physical condition caused by or arising from the pregnancy itself) that would, as certified by a physician, place the woman in danger of death if an abortion were not performed.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s251"
    },
    "title": "Protecting Life in Health Savings Accounts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Life in Health Savings Accounts Act</strong></p><p>This bill excludes expenses paid for an abortion from qualified medical expenses eligible for reimbursement from certain tax-exempt savings accounts. (Some exceptions apply.)</p><p>Under the bill, amounts paid for an abortion, other than an excluded abortion, are not qualified medical expenses eligible for reimbursement from a health savings account, Archer medical savings account, health flexible spending arrangement, health reimbursement arrangement, or retiree health account.</p><p>The bill defines <em>excluded abortion</em> as any abortion (1) related to a pregnancy that is the result of rape or incest; or (2)\u00a0performed because a woman is suffering from a physical disorder, injury, or illness (including a life-endangering physical condition caused by or arising from the pregnancy itself) that would, as certified by a physician, place the woman in danger of death if an abortion were not performed.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s251"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s251is.xml"
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
      "title": "Protecting Life in Health Savings Accounts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Life in Health Savings Accounts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to prohibit treatment of certain distributions and reimbursements for certain abortions as qualified medical expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:40Z"
    }
  ]
}
```
