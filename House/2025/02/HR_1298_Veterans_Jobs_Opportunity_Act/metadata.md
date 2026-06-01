# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1298?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1298
- Title: Veterans Jobs Opportunity Act
- Congress: 119
- Bill type: HR
- Bill number: 1298
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-02-19T14:50:05Z
- Update date including text: 2026-02-19T14:50:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1298",
    "number": "1298",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Veterans Jobs Opportunity Act",
    "type": "HR",
    "updateDate": "2026-02-19T14:50:05Z",
    "updateDateIncludingText": "2026-02-19T14:50:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:08:45Z",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1298ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1298\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Davis of North Carolina (for himself and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a small business start-up tax credit for veterans creating businesses in underserved communities.\n#### 1. Short title\nThis Act may be cited as the Veterans Jobs Opportunity Act .\n#### 2. Veteran small business start-up credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Veteran small business start-up credit (a) In general For purposes of section 38, the veteran small business start-up credit determined under this section for any taxable year is an amount equal to 15 percent of so much of the qualified start-up expenditures paid or incurred by the taxpayer during such taxable year with respect to an applicable veteran-owned business as does not exceed $50,000. (b) Definitions For purposes of this section\u2014 (1) Applicable veteran-owned small business The term applicable veteran-owned small business means a small business\u2014 (A) owned and controlled by 1 or more veterans or spouses of veterans, and (B) the principal place of business of which is in an underserved community. (2) Ownership and control The term owned and controlled means\u2014 (A) with respect to any of the individuals described in paragraph (1)(A), that the conduct of any trade or business of the small business is not a passive activity (as defined in section 469(c)), and (B) with respect to the small business\u2014 (i) such small business is a sole proprietorship, (ii) if such small business is a corporation, ownership (by vote or value) by the individuals described in paragraph (1)(A) of greater than 50 percent of the stock in such corporation, or (iii) if such small business is a partnership, ownership by the individuals described in paragraph (1)(A) of greater than 50 percent of the profits interests or capital interests in such partnership. (3) Qualified start-up expenditures The term qualified start-up expenditures means\u2014 (A) any start-up expenditures (as defined in section 195(c)), and (B) any amounts paid or incurred during the taxable year for the purchase or lease of real property, or the purchase of personal property, placed in service during the taxable year and used in the active conduct of a trade or business. (4) Small business (A) In general The term small business means, with respect to any taxable year, any person engaged in a trade or business in the United States if\u2014 (i) the gross receipts of such person for the preceding taxable year did not exceed $5,000,000, or (ii) in the case of a person to which clause (i) does not apply, such person employed not more than 50 full-time employees during the preceding taxable year. (B) Full-time employee For purposes of subparagraph (A)(ii), an employee shall be considered full-time if such employee is employed at least 30 hours per week for 20 or more calendar weeks in the taxable year. (5) Underserved community The term underserved community means any area located within\u2014 (A) a HUBZone (as defined in section 3(p) of the Small Business Act ( 15 U.S.C. 632(p) ), as in effect on the date of enactment of this section), (B) an empowerment zone, or enterprise community, designated under section 1391 (and without regard to whether or not such designation remains in effect), (C) an area of low income or moderate income (as recognized by the Federal Financial Institutions Examination Council), or (D) a county with persistent poverty (as classified by the Economic Research Service of the Department of Agriculture). (6) Veteran or spouse of veteran The term veteran or spouse of a veteran has the meaning given such term by section 7(a)(31)(G)(ii) of the Small Business Act ( 15 U.S.C. 636(a)(31)(G)(ii) , as in effect on the date of enactment of this section). (c) Special rules For purposes of this section\u2014 (1) Election to take credit No credit shall be allowed under subsection (a) for any expenditures unless the taxpayer elects to have this section apply to such expenditures. (2) Year of election The taxpayer may elect the application of this section only for the first 2 taxable years for which ordinary and necessary expenses paid or incurred in carrying on such trade or business are allowable as a deduction by the taxpayer under section 162. (3) Controlled groups and common control All persons treated as a single employer under subsections (a) and (b) of section 52 shall be treated as 1 person. (4) No double benefit If a credit is determined under this section with respect to any property, the basis of such property shall be reduced by the amount of the credit attributable to such property. .\n##### (b) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Veteran small business start-up credit. .\n##### (c) Part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting plus , and by adding at the end the following new paragraph:\n(42) the veteran small business start-up credit determined under section 45BB. .\n##### (d) Report by Treasury Inspector General for Tax Administration\nEvery fourth year after the date of the enactment of this Act, the Treasury Inspector General for Tax Administration shall include in one of the semiannual reports under section 5 of the Inspector General Act of 1978 with respect to such year, an evaluation of the credit allowed under section 45BB of the Internal Revenue Code of 1986 (as added by this section), including an evaluation of the success of, and accountability with respect to, such credit.\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2443",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans Jobs Opportunity Act",
      "type": "S"
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
        "updateDate": "2025-05-06T14:05:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1298",
          "measure-number": "1298",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1298v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Jobs Opportunity Act</strong></p><p>This bill allows veteran-owned small businesses in underserved communities to claim a tax credit for qualified start-up expenses in the amount of 15% (up to $50,000) of such expenses. (Conditions and limitations apply.)</p><p>Under the bill, a business qualifies for the veteran small business start-up tax credit if it</p><ul><li>is owned and controlled by one or more veterans (or spouses of veterans);</li><li>is located in a Historically Underutilized Business Zone (HUBZone) program area, empowerment zone or enterprise community, an area of low or moderate income, or county with persistent poverty; and</li><li>has gross receipts for the prior tax year of $5 million or less (or employed 50 or fewer full-time employees in the prior tax year).</li></ul><p>The bill generally defines <em>qualified start-up expenses</em> as amounts incurred or paid to</p><ul><li>investigate the creation or acquisition of the business,</li><li>create the business,</li><li>engage in activities for the production of income before the day the business opens, and</li><li>purchase\u00a0or lease real property (or purchase personal property)\u00a0for use in the active conduct of a trade or business.</li></ul><p>However, under the bill, the veteran small business start-up tax credit is allowed only in the first two tax years for which a business may claim a tax deduction for ordinary and necessary trade or business expenses.</p><p>Finally, the bill requires the\u00a0Treasury Inspector General for Tax Administration to provide an evaluation of the veteran small business start-up tax credit to Congress every four years.</p>"
        },
        "title": "Veterans Jobs Opportunity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1298.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Jobs Opportunity Act</strong></p><p>This bill allows veteran-owned small businesses in underserved communities to claim a tax credit for qualified start-up expenses in the amount of 15% (up to $50,000) of such expenses. (Conditions and limitations apply.)</p><p>Under the bill, a business qualifies for the veteran small business start-up tax credit if it</p><ul><li>is owned and controlled by one or more veterans (or spouses of veterans);</li><li>is located in a Historically Underutilized Business Zone (HUBZone) program area, empowerment zone or enterprise community, an area of low or moderate income, or county with persistent poverty; and</li><li>has gross receipts for the prior tax year of $5 million or less (or employed 50 or fewer full-time employees in the prior tax year).</li></ul><p>The bill generally defines <em>qualified start-up expenses</em> as amounts incurred or paid to</p><ul><li>investigate the creation or acquisition of the business,</li><li>create the business,</li><li>engage in activities for the production of income before the day the business opens, and</li><li>purchase\u00a0or lease real property (or purchase personal property)\u00a0for use in the active conduct of a trade or business.</li></ul><p>However, under the bill, the veteran small business start-up tax credit is allowed only in the first two tax years for which a business may claim a tax deduction for ordinary and necessary trade or business expenses.</p><p>Finally, the bill requires the\u00a0Treasury Inspector General for Tax Administration to provide an evaluation of the veteran small business start-up tax credit to Congress every four years.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr1298"
    },
    "title": "Veterans Jobs Opportunity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Jobs Opportunity Act</strong></p><p>This bill allows veteran-owned small businesses in underserved communities to claim a tax credit for qualified start-up expenses in the amount of 15% (up to $50,000) of such expenses. (Conditions and limitations apply.)</p><p>Under the bill, a business qualifies for the veteran small business start-up tax credit if it</p><ul><li>is owned and controlled by one or more veterans (or spouses of veterans);</li><li>is located in a Historically Underutilized Business Zone (HUBZone) program area, empowerment zone or enterprise community, an area of low or moderate income, or county with persistent poverty; and</li><li>has gross receipts for the prior tax year of $5 million or less (or employed 50 or fewer full-time employees in the prior tax year).</li></ul><p>The bill generally defines <em>qualified start-up expenses</em> as amounts incurred or paid to</p><ul><li>investigate the creation or acquisition of the business,</li><li>create the business,</li><li>engage in activities for the production of income before the day the business opens, and</li><li>purchase\u00a0or lease real property (or purchase personal property)\u00a0for use in the active conduct of a trade or business.</li></ul><p>However, under the bill, the veteran small business start-up tax credit is allowed only in the first two tax years for which a business may claim a tax deduction for ordinary and necessary trade or business expenses.</p><p>Finally, the bill requires the\u00a0Treasury Inspector General for Tax Administration to provide an evaluation of the veteran small business start-up tax credit to Congress every four years.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr1298"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1298ih.xml"
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
      "title": "Veterans Jobs Opportunity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Jobs Opportunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a small business start-up tax credit for veterans creating businesses in underserved communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:23Z"
    }
  ]
}
```
