# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/74?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/74
- Title: Freedom for Families Act
- Congress: 119
- Bill type: HR
- Bill number: 74
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-20T17:45:31Z
- Update date including text: 2025-11-20T17:45:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/74",
    "number": "74",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Freedom for Families Act",
    "type": "HR",
    "updateDate": "2025-11-20T17:45:31Z",
    "updateDateIncludingText": "2025-11-20T17:45:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:17:30Z",
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
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr74ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 74\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Burlison ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for tax-advantaged distributions from health savings accounts during family or medical leave, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom for Families Act .\n#### 2. Distributions from health savings accounts during periods of qualified caregiving\n##### (a) In general\nParagraphs (1) and (2) of section 223(f) of the Internal Revenue Code of 1986 are amended to read as follows:\n(1) Exclusion of amounts used for qualified medical expenses or distributed during periods of qualified caregiving Any amount paid or distributed out of a health savings account shall not be includible in gross income if it is\u2014 (A) used exclusively to pay qualified medical expenses of any account beneficiary, or (B) paid or distributed during a period of qualified caregiving. (2) Inclusion of amounts neither used for qualified medical expenses nor distributed during periods of qualified caregiving Any amount paid or distributed out of a health savings account shall be included in the gross income of the account beneficiary if it is not described in paragraph (1). .\n##### (b) Definition of period of qualified caregiving\nSection 223(f) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(9) Period of qualified caregiving For purposes of this section, the term period of qualified caregiving means any period during which an individual is on leave or not employed by reason of a situation described in subparagraphs (A) through (E) of section 102(a)(1) of the Family and Medical Leave Act of 1993. .\n##### (c) Conforming amendments\n**(1)**\nSection 223(d)(1) of such Code is amended by inserting or the expenses incurred during a period of qualified caregiving of the account beneficiary after paying the qualified medical expenses of the account beneficiary .\n**(2)**\nSection 223(f)(4) of such Code is amended in the heading by striking distributions not used for qualified medical expenses and inserting certain distributions .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to taxable years beginning after the date of the enactment of this Act.\n#### 3. No high deductible health plan required for health savings accounts\n##### (a) In general\nSection 223(a) of the Internal Revenue Code of 1986 is amended by striking who is an eligible individual for any month during the taxable year .\n##### (b) Conforming amendments\n**(1)**\nSection 223(b) of such Code is amended by striking paragraphs (7) and (8).\n**(2)**\nSection 223 of such Code is amended by striking subsection (c).\n##### (c) Increase in contribution limit for health savings accounts\n**(1) In general**\nSection 223(b)(1) of the Internal Revenue Code of 1986 is amended by striking the sum of the monthly and all that follows through eligible individual and inserting $9,000 (twice such amount in the case of a joint return) .\n**(2) Conforming amendments**\n**(A)**\nSection 223(b) of such Code is amended by striking paragraphs (2), (3), and (5) and by redesignating paragraphs (4) and (6) as paragraphs (2) and (3), respectively.\n**(B)**\nSection 223(b)(2) of such Code (as redesignated by subparagraph (A)) is amended by striking the last sentence.\n**(C)**\nSection 223(d)(1)(A)(ii) is amended by striking the sum of and all that follows through the period at the end and inserting the dollar amount in effect under subsection (b)(1). .\n**(D)**\nSection 223(g)(1) of such Code is amended\u2014\n**(i)**\nby striking Each dollar amount in subsections (b)(2) and (c)(2)(A) and inserting The dollar amount in subsection (b)(1) ;\n**(ii)**\nby striking thereof and all that follows through calendar year 2003 . and inserting calendar year 1997 . ; and\n**(iii)**\nby striking under subsections (b)(2) and (c)(2)(A) and inserting under subsection (b)(1) .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to months in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-11-07",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5933",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HSAs For Heroes Act",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-02-14T19:13:07Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-02-14T19:13:07Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-02-14T19:13:07Z"
          },
          {
            "name": "Income tax exclusion",
            "updateDate": "2025-02-14T19:13:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-01-31T16:14:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr74",
          "measure-number": "74",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr74v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Freedom for Families Act</strong></p><p>This bill allows individuals to establish and contribute to a health savings account (HSA) without being enrolled in a high-deductible health plan (HDHP), increases HSA contribution limits, and allows tax-free distributions from an HSA during a period of qualified caregiving.</p><p>Under current law, individuals may establish and contribute to an HSA if they are covered under an HSA-eligible HDHP. For 2025, HSA contributions are limited to $4,300 for self-only coverage or $8,550 for family coverage (adjusted annually). Individuals who are at least\u00a055 years\u00a0old may make an additional HSA contribution of up to $1,000 per year. Further, under current law, HSA distributions are tax-free if used to pay for qualified medical expenses.\u00a0</p><p>The bill eliminates the HDHP coverage requirement for purposes of an HSA.</p><p>The bill also increases the HSA annual contribution limit to $9,000 for individuals or $18,000 for joint filers\u00a0(adjusted annually)\u00a0and eliminates the additional contribution for individuals\u00a0who are at least 55 years old.</p><p>Finally, the bill excludes HSA distributions during a period of qualified caregiving from gross income. The bill defines <em>period of qualified caregiving</em> as any period during which an individual is on leave or not employed due to</p><ul><li>the birth or adoption of a child;</li><li>placement of a foster child;</li><li>caring for a family member with a serious health condition;</li><li>an inability to work due to a serious health condition; or</li><li>certain emergencies related to a spouse, child, or parent on covered active duty with the Armed Forces.\u00a0</li></ul>"
        },
        "title": "Freedom for Families Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr74.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom for Families Act</strong></p><p>This bill allows individuals to establish and contribute to a health savings account (HSA) without being enrolled in a high-deductible health plan (HDHP), increases HSA contribution limits, and allows tax-free distributions from an HSA during a period of qualified caregiving.</p><p>Under current law, individuals may establish and contribute to an HSA if they are covered under an HSA-eligible HDHP. For 2025, HSA contributions are limited to $4,300 for self-only coverage or $8,550 for family coverage (adjusted annually). Individuals who are at least\u00a055 years\u00a0old may make an additional HSA contribution of up to $1,000 per year. Further, under current law, HSA distributions are tax-free if used to pay for qualified medical expenses.\u00a0</p><p>The bill eliminates the HDHP coverage requirement for purposes of an HSA.</p><p>The bill also increases the HSA annual contribution limit to $9,000 for individuals or $18,000 for joint filers\u00a0(adjusted annually)\u00a0and eliminates the additional contribution for individuals\u00a0who are at least 55 years old.</p><p>Finally, the bill excludes HSA distributions during a period of qualified caregiving from gross income. The bill defines <em>period of qualified caregiving</em> as any period during which an individual is on leave or not employed due to</p><ul><li>the birth or adoption of a child;</li><li>placement of a foster child;</li><li>caring for a family member with a serious health condition;</li><li>an inability to work due to a serious health condition; or</li><li>certain emergencies related to a spouse, child, or parent on covered active duty with the Armed Forces.\u00a0</li></ul>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr74"
    },
    "title": "Freedom for Families Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom for Families Act</strong></p><p>This bill allows individuals to establish and contribute to a health savings account (HSA) without being enrolled in a high-deductible health plan (HDHP), increases HSA contribution limits, and allows tax-free distributions from an HSA during a period of qualified caregiving.</p><p>Under current law, individuals may establish and contribute to an HSA if they are covered under an HSA-eligible HDHP. For 2025, HSA contributions are limited to $4,300 for self-only coverage or $8,550 for family coverage (adjusted annually). Individuals who are at least\u00a055 years\u00a0old may make an additional HSA contribution of up to $1,000 per year. Further, under current law, HSA distributions are tax-free if used to pay for qualified medical expenses.\u00a0</p><p>The bill eliminates the HDHP coverage requirement for purposes of an HSA.</p><p>The bill also increases the HSA annual contribution limit to $9,000 for individuals or $18,000 for joint filers\u00a0(adjusted annually)\u00a0and eliminates the additional contribution for individuals\u00a0who are at least 55 years old.</p><p>Finally, the bill excludes HSA distributions during a period of qualified caregiving from gross income. The bill defines <em>period of qualified caregiving</em> as any period during which an individual is on leave or not employed due to</p><ul><li>the birth or adoption of a child;</li><li>placement of a foster child;</li><li>caring for a family member with a serious health condition;</li><li>an inability to work due to a serious health condition; or</li><li>certain emergencies related to a spouse, child, or parent on covered active duty with the Armed Forces.\u00a0</li></ul>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr74"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr74ih.xml"
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
      "title": "Freedom for Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T07:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom for Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow for tax-advantaged distributions from health savings accounts during family or medical leave, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T07:03:42Z"
    }
  ]
}
```
