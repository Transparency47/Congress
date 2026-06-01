# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/317?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/317
- Title: Healthcare Freedom Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 317
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-04-29T17:06:39Z
- Update date including text: 2026-04-29T17:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/317",
    "number": "317",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Healthcare Freedom Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-29T17:06:39Z",
    "updateDateIncludingText": "2026-04-29T17:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-09T14:30:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MO"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AZ"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "OK"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr317ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 317\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Roy (for himself, Mr. Weber of Texas , Mr. Cline , Mr. Burlison , Mr. Clyde , Ms. Greene of Georgia , Mr. Biggs of Arizona , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to create health freedom accounts available to all individuals.\n#### 1. Short title\nThis Act may be cited as the Healthcare Freedom Act of 2025 .\n#### 2. Health freedom accounts\n##### (a) In general\nSection 223 of the Internal Revenue Code of 1986 is amended by striking health savings account and health savings accounts each place such terms appear and inserting health freedom account and health freedom accounts , respectively.\n##### (b) All individuals allowed deductions for contributions\nSection 223(a) of the Internal Revenue Code of 1986 is amended by striking who is an eligible individual for any month during the taxable year .\n##### (c) No limitation on purchasing health coverage from health freedom accounts\nSection 223(d)(2) of the Internal Revenue Code of 1986 is amended by striking subparagraphs (B) and (C) and the last sentence of subparagraph (A) and by adding at the end the following new subsection:\n(B) Additional expenses The term qualified medical expenses includes costs associated with direct primary care, health care sharing ministries, and medical cost sharing organizations. .\n##### (d) Transfers allowed to other health freedom accounts\nSection 223(f)(5) of the Internal Revenue Code of 1986 is amended to read as follows:\n(5) Rollover contribution An amount paid or distributed from a health freedom account is a rollover contribution to the extent the amount received is paid into any other health freedom account not later than the 60th day after the date of such payment or distribution. .\n##### (e) Increase in contribution limits\nSection 223(b)(1) of such Code is amended by striking the sum of the monthly and all that follows through eligible individual and inserting $12,000 (twice such amount in the case of a joint return) .\n##### (f) Conforming amendments\n**(1)**\nSection 223(b) of such Code is amended by striking paragraphs (2), (5), (7), and (8) and by redesignating paragraphs (3), (4), and (6) as paragraphs (2), (3), and (4), respectively.\n**(2)**\nSection 223(b)(2) of such Code (as redesignated by paragraph (2)) is amended to read as follows:\n(2) Additional contributions for individuals 55 or older In the case of an individual who has attained age 55 before the close of the taxable year, the limitation under paragraph (1) shall be increased by $5,000. .\n**(3)**\nSection 223(b)(3) of such Code (as redesignated by subparagraph (A)) is amended by striking the last sentence.\n**(4)**\nSection 223 of such Code is amended by striking subsection (c).\n**(5)**\nSection 223(d)(1)(A) of such Code is amended by striking will be accepted and all that follows through the period at the end and inserting will be accepted unless it is in cash. .\n**(6)**\nSection 223(f) of such Code is amended by striking paragraphs (7) and (8).\n**(7)**\nSection 223(g)(1) of such Code is amended\u2014\n**(A)**\nby striking Each dollar amount in subsections (b)(2) and (c)(2)(A) and inserting The dollar amount in subsection (b)(1) ;\n**(B)**\nby striking thereof and all that follows in subparagraph (B) through calendar year 2003 . and inserting calendar year 1997 . ; and\n**(C)**\nby striking under subsections (b)(2) and (c)(2)(A) and inserting under subsection (b)(1) .\n**(8)**\nThe table of sections for part VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended in the item relating to section 223 by striking savings and inserting freedom .\n##### (g) Effective date\nThe amendments made by this section shall apply with respect to months in taxable years beginning after the date of the enactment of this Act.\n#### 3. Exclusion for employer contributions to health freedom accounts\n##### (a) Employer exclusion\n**(1) In general**\nThe Internal Revenue Code of 1986 is amended by inserting after section 106 the following new section:\n106A. Contributions by employers to health freedom accounts In the case of any employee hired by an employer on or after the date that is 5 years after the date of the enactment of this section, gross income of such employee does not include amounts contributed by such employer to a health freedom account of such employee. .\n**(2) Exclusion for contributions by employer to accident and health plans**\nSection 106 of such Code is amended by adding at the end the following new subsection:\n(h) Termination In the case of any employee hired by an employer on or after the date that is 5 years after the date of the enactment of this section, this section shall not apply to coverage provided by such employer with respect to such employee. .\n**(3) Conforming amendment**\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by striking the item relating to section 106 and inserting the following:\nSec. 106A. Contributions by employers to health freedom accounts. .\n**(4) Effective date**\nThe amendments made by this subsection shall apply with respect to employees hired on or after the date that is 5 years after the date of the enactment of this Act.\n##### (b) Transition rule\n**(1) In general**\nSection 106(d)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) In general Amounts contributed by an employee\u2019s employer to any health freedom account (as defined in section 223(d)) of such employee shall be treated as employer-provided coverage for medical expenses under an accident or health plan. .\n**(2) In general**\nThe amendment made by this subsection shall apply with respect to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-02-15T13:30:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "House",
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
          "measure-id": "id119hr317",
          "measure-number": "317",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2026-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr317v00",
            "update-date": "2026-04-29"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Healthcare Freedom Act of 2025</strong></p><p>This bill renames health savings accounts (HSAs) as health freedom accounts (HFAs), modifies the eligibility requirements and contribution limits for such accounts, and expands the definition of qualified medical expenses. The bill also eliminates the exclusion from income of employer contributions to a health plan for certain individuals.</p><p>Under current law, individuals may establish and contribute to an HSA if covered under an HSA-eligible high-deductible health plan (HDHP). For 2025, HSA contributions are limited to $4,300 for self-only coverage or $8,550 for family coverage (adjusted annually). Individuals 55 or older may make an additional HSA contribution of up to $1,000 per year. Further, HSA distributions are tax-free if used to pay for qualified medical expenses.</p><p>The bill allows individuals to</p><ul><li>establish and contribute to an HFA without being enrolled in an HDHP,</li><li>contribute up to $12,000 ($24,000 for joint filers) per year to an HFA (adjusted annually), and</li><li>contribute an additional $5,000 per year to an\u00a0HFA if 55 or older.</li></ul><p>The bill also expands the definition of <em>qualified medical expenses</em> to include expenses related to direct primary care, health care sharing ministries, and medical cost sharing organizations.</p><p>For individuals hired at least five years after the bill's enactment (1) employer contributions to an\u00a0HFA may be excluded from the employee's income, and (2) the bill\u00a0eliminates the exclusion from income of employer contributions to other health plans. (Under current law, employer contributions to a health plan generally are not included in the individual\u2019s income.)</p>"
        },
        "title": "Healthcare Freedom Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr317.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthcare Freedom Act of 2025</strong></p><p>This bill renames health savings accounts (HSAs) as health freedom accounts (HFAs), modifies the eligibility requirements and contribution limits for such accounts, and expands the definition of qualified medical expenses. The bill also eliminates the exclusion from income of employer contributions to a health plan for certain individuals.</p><p>Under current law, individuals may establish and contribute to an HSA if covered under an HSA-eligible high-deductible health plan (HDHP). For 2025, HSA contributions are limited to $4,300 for self-only coverage or $8,550 for family coverage (adjusted annually). Individuals 55 or older may make an additional HSA contribution of up to $1,000 per year. Further, HSA distributions are tax-free if used to pay for qualified medical expenses.</p><p>The bill allows individuals to</p><ul><li>establish and contribute to an HFA without being enrolled in an HDHP,</li><li>contribute up to $12,000 ($24,000 for joint filers) per year to an HFA (adjusted annually), and</li><li>contribute an additional $5,000 per year to an\u00a0HFA if 55 or older.</li></ul><p>The bill also expands the definition of <em>qualified medical expenses</em> to include expenses related to direct primary care, health care sharing ministries, and medical cost sharing organizations.</p><p>For individuals hired at least five years after the bill's enactment (1) employer contributions to an\u00a0HFA may be excluded from the employee's income, and (2) the bill\u00a0eliminates the exclusion from income of employer contributions to other health plans. (Under current law, employer contributions to a health plan generally are not included in the individual\u2019s income.)</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr317"
    },
    "title": "Healthcare Freedom Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthcare Freedom Act of 2025</strong></p><p>This bill renames health savings accounts (HSAs) as health freedom accounts (HFAs), modifies the eligibility requirements and contribution limits for such accounts, and expands the definition of qualified medical expenses. The bill also eliminates the exclusion from income of employer contributions to a health plan for certain individuals.</p><p>Under current law, individuals may establish and contribute to an HSA if covered under an HSA-eligible high-deductible health plan (HDHP). For 2025, HSA contributions are limited to $4,300 for self-only coverage or $8,550 for family coverage (adjusted annually). Individuals 55 or older may make an additional HSA contribution of up to $1,000 per year. Further, HSA distributions are tax-free if used to pay for qualified medical expenses.</p><p>The bill allows individuals to</p><ul><li>establish and contribute to an HFA without being enrolled in an HDHP,</li><li>contribute up to $12,000 ($24,000 for joint filers) per year to an HFA (adjusted annually), and</li><li>contribute an additional $5,000 per year to an\u00a0HFA if 55 or older.</li></ul><p>The bill also expands the definition of <em>qualified medical expenses</em> to include expenses related to direct primary care, health care sharing ministries, and medical cost sharing organizations.</p><p>For individuals hired at least five years after the bill's enactment (1) employer contributions to an\u00a0HFA may be excluded from the employee's income, and (2) the bill\u00a0eliminates the exclusion from income of employer contributions to other health plans. (Under current law, employer contributions to a health plan generally are not included in the individual\u2019s income.)</p>",
      "updateDate": "2026-04-29",
      "versionCode": "id119hr317"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr317ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Healthcare Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T06:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T06:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to create health freedom accounts available to all individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T06:03:37Z"
    }
  ]
}
```
