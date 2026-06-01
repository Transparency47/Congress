# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7768?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7768
- Title: Tax Relief for Renters Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7768
- Origin chamber: House
- Introduced date: 2026-03-03
- Update date: 2026-04-21T08:05:44Z
- Update date including text: 2026-04-21T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-03: Introduced in House

## Actions

- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Introduced in House
- 2026-03-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7768",
    "number": "7768",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000601",
        "district": "1",
        "firstName": "Greg",
        "fullName": "Rep. Landsman, Greg [D-OH-1]",
        "lastName": "Landsman",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Tax Relief for Renters Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:44Z",
    "updateDateIncludingText": "2026-04-21T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-03",
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
      "actionDate": "2026-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T17:01:30Z",
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
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NJ"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7768ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7768\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2026 Mr. Landsman (for himself and Mr. Kean ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a deduction for certain amounts paid for rent for a primary residence.\n#### 1. Short title\nThis Act may be cited as the Tax Relief for Renters Act of 2026 .\n#### 2. Deduction for rent payments\n##### (a) In general\n**(1) Deduction allowed**\nPart VII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 226 as section 227 and by inserting after section 225 the following new section:\n226. Rent payments (a) In general There shall be allowed as a deduction an amount equal to 1/12 the qualified rent expenses of the taxpayer for the taxable year. (b) Qualified rent expenses For purposes of this section, the term qualified rent expenses means, with respect to a taxable year, amounts paid or incurred to lease the primary residence of the taxpayer during the taxable year. (c) Limitations (1) In general The deduction allowed under subsection (a) shall not exceed $4,000 for any individual in any taxable year. (2) Income limitation (A) In general No deduction shall be allowed under subsection (a) in the case of an individual whose adjusted gross income for the taxable year exceeds the threshold amount. (B) Threshold amount For purposes of this paragraph, the term threshold amount means\u2014 (i) in the case of a joint return or a surviving spouse, $125,000, (ii) in the case of married filing separately, $85,000, (iii) in the case of a head of household, $80,000, or (iv) in the case of any other individual, $75,000. (d) Inflation adjustment (1) In general In the case of any taxable year beginning after 2027, each of the dollar amounts in subsection (c) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2026 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding If any increase under paragraph (1) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. .\n**(2) Conforming amendment**\nThe table of sections for part VII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 225 the following new item:\nSec. 226. Rent payments. .\n##### (b) Deduction allowed to non-Itemizers\nSection 63(b) of such Code is amended by striking and at the end of paragraph (6), by striking the period at the end of paragraph (7) and inserting and , and by adding at the end the following new paragraph:\n(8) the deduction provided in section 226. .\n##### (c) Non-Application of certain limitations for itemizers\n**(1) Deduction not treated as a miscellaneous itemized deduction**\nSection 67(b) of such Code is amended by striking and at the end of paragraph (12), by striking the period at the end of paragraph (13) and inserting , and , and by adding at the end the following new paragraph:\n(14) the deduction under section 226 (relating to rent payments). .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-03-03",
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
        "updateDate": "2026-03-20T15:25:36Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7768ih.xml"
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
      "title": "Tax Relief for Renters Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Relief for Renters Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a deduction for certain amounts paid for rent for a primary residence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:25Z"
    }
  ]
}
```
