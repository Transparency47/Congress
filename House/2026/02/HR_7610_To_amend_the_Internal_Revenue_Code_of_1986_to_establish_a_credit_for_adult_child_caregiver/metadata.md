# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7610?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7610
- Title: To amend the Internal Revenue Code of 1986 to establish a credit for adult child caregivers.
- Congress: 119
- Bill type: HR
- Bill number: 7610
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-02-25T18:40:01Z
- Update date including text: 2026-02-25T18:40:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7610",
    "number": "7610",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to establish a credit for adult child caregivers.",
    "type": "HR",
    "updateDate": "2026-02-25T18:40:01Z",
    "updateDateIncludingText": "2026-02-25T18:40:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:33:35Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7610ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7610\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mrs. Dingell (for herself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a credit for adult child caregivers.\n#### 1. Findings\nCongress makes the following findings:\n**(1)**\nOnce formed, multigenerational families tend to live together over time and utilize less paid and unpaid formal support. Adult child proximity may be more directly linked with reduced need for formal care than availability of a spouse.\n**(2)**\nOlder adults in multigenerational homes experience less depression and isolation, and show improved cognition with concurrent hearing loss.\n**(3)**\nAn older adult with dementia and disability co-residing with an adult child has a 50 percent lower risk of transitioning from the community to a nursing home in the subsequent 2 years, compared to older adults supported by children living outside the home.\n#### 2. Multigenerational home caregiver credit\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Multigenerational home caregiver credit (a) Allowance of credit In the case of an eligible individual, there shall be allowed as a credit against the tax imposed by this subtitle for the taxable year an amount equal to $2,000 for each qualified relative with respect to the individual. (b) Eligible individual For purposes of this section\u2014 (1) In general The term eligible individual with respect to any taxable year means an individual\u2014 (A) who has attained age 18, or has attained age 16 and is legally emancipated, as of the last day of such taxable year, (B) who is a United States citizen, (C) who has the same principal place of abode as a qualified relative for not less than 6 months during the taxable year, (D) who provides a total of not less than 10 hours per week of the assistance required by such qualified relative pursuant to paragraph (2)(A)(iii), and (E) who includes with the return of tax for the taxable year an attestation signed by a licensed health care provider that, to the best of the provider's knowledge, the qualified relative meets the requirements of clauses (iii) and (iv) of paragraph (2)(A). (2) Qualified relative (A) In general The term qualified relative with respect to an individual means an individual\u2014 (i) who bears a relationship described in subparagraph (B) to such individual or to such individual's spouse, (ii) who has attained age 55 as of the last day of the taxable year, (iii) who is unable to perform (without substantial assistance from another individual) at least\u2014 (I) 1 activity of daily living (as defined in section 7702B(c)(2)(B)), and (II) 3 instrumental activities of daily living, requiring a total of not less than 10 hours per week of assistance with such activities, and (iv) with respect to whom the period during which clause (iii) applies has lasted or will last for not less than 180 days or the life of the individual, whichever is shorter. (B) Relationship For purposes of subparagraph (A), a relationship described in this subparagraph is a relationship described in subparagraph (C), (D), (F), or (G) of section 152(d)(2), except that only a father-in-law or mother-in-law shall be taken into account for purposes of subparagraph (G) thereof. (C) Instrumental activities of daily living (i) In general The term instrumental activities of daily living includes meal planning and preparation, managing finances, shopping for food, clothing, and other essential items, performing essential household chores, communicating by phone or other media, and traveling around and participating in the community. (ii) Coordination In prescribing regulations or other guidance for purposes of clause (i), the Secretary shall to the extent practicable coordinate with the Secretary of Health and Human Services to ensure consistency with programs under chapter 7 of the Social Security Act. (3) Special rule for qualified relatives dying during the taxable year In the case of the death of an individual who would be a qualified relative with respect to the taxpayer but for subparagraph (C) of paragraph (1) (determined without regard to this paragraph), such subparagraph shall be applied for the taxable year in which such individual died by substituting 3 months for 6 months . (c) Limitations (1) Limitation based on adjusted gross income The $2,000 amount in subsection (a) shall be reduced (but not below zero) by 1 percent of the excess of the taxpayer\u2019s adjusted gross income over $75,000 ($150,000 in the case of a joint return). (2) Only 1 taxpayer may claim qualified relative In the case of an individual who is the qualified relative by reason of whom the credit under this section is allowed, the credit under this section shall be allowed to only 1 taxpayer with respect to such individual for any taxable year. If (but for this paragraph) such individual is a qualified relative of more than 1 taxpayer for the taxable year, such individual shall be treated as the qualified relative of the taxpayer with the highest adjusted gross income. (3) Limitation on qualified relatives Not more than 2 qualified relatives with respect to the taxpayer may be taken into account for purposes of the credit under this section for any taxable year. (4) Married individuals must file joint return If the taxpayer is a married individual (within the meaning of section 7703), this section shall apply only if the taxpayer and the taxpayer's spouse file a joint return for the taxable year. (5) Coordination with child and dependent care credit The amount of the credit determined under subsection (a) (after the application of paragraph (1)) with respect to any qualified relative shall be reduced (but not below zero) by the amount of any credit allowed under section 21 with respect to such qualified relative. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Multigenerational home caregiver credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-02-20",
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3295",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a credit for adult child caregivers.",
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
        "updateDate": "2026-02-25T18:40:01Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7610ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a credit for adult child caregivers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T05:48:34Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to establish a credit for adult child caregivers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T09:05:25Z"
    }
  ]
}
```
