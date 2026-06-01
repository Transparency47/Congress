# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7576?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7576
- Title: AI Workforce Training Act
- Congress: 119
- Bill type: HR
- Bill number: 7576
- Origin chamber: House
- Introduced date: 2026-02-13
- Update date: 2026-05-22T08:07:22Z
- Update date including text: 2026-05-22T08:07:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-13: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-13: Introduced in House

## Actions

- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-13",
    "latestAction": {
      "actionDate": "2026-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7576",
    "number": "7576",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "AI Workforce Training Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:22Z",
    "updateDateIncludingText": "2026-05-22T08:07:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
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
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-13",
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
          "date": "2026-02-13T15:02:50Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "TX"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7576ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7576\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2026 Mr. Gottheimer (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a credit for workforce artificial intelligence training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI Workforce Training Act .\n#### 2. Tax credit for workforce artificial intelligence training\n##### (a) Establishment of credit\n**(1) In general**\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Credit for workforce artificial intelligence training (a) In general For purposes of section 38, the workforce artificial intelligence training credit determined under this section for any taxable year is an amount equal to 30 percent of the qualified artificial intelligence training expenses of the taxpayer for such taxable year. (b) Dollar limitation (1) In general The amount of the credit determined under subsection (a) for any taxpayer for any taxable year shall not exceed $2,500 for each employee of such taxpayer with respect to whom qualified artificial intelligence training expenses are paid or incurred by such taxpayer during such taxable year. (2) Inflation adjustment In the case of any taxable year beginning after 2026, the dollar amount specified in paragraph (1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (c) Qualified artificial intelligence training expenses (1) In general For purposes of this section, the term qualified artificial intelligence training expenses means, with respect to any taxpayer, amounts paid or incurred for\u2014 (A) any expenses required for the enrollment or attendance of any employee of such taxpayer at an accredited artificial intelligence training program, including workshops, certificate programs, and courses on prompt engineering, data literacy, machine learning fundamentals, or artificial intelligence ethics, (B) the wages of any such employee while such employee attends a program, workshop, or course described in paragraph (1), and (C) any expenses related to developing or providing in-house artificial intelligence training for any such employee. (2) Wages For purposes of paragraph (1), the term wages has the meaning given to such term in section 3306(b) (determined without regard to any dollar limitation contained in such section). (d) Denial of double benefit In the case of any qualified artificial intelligence training expenses with respect to which credit is allowed under subsection (a)\u2014 (1) no other credit or deduction shall be allowed for, or by reason of, any such expense to the extent of the amount of such credit, and (2) the basis of any property shall be reduced by the amount of such credit to the extent that such expenses were taken into account in determining such basis. (e) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations to prevent the abuse of the purposes of this section. .\n**(2) Clerical amendment**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\n45BB. Credit for workforce artificial intelligence training. .\n##### (b) Credit made part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the workforce artificial intelligence training credit determined under section 45BB. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Public outreach campaign; report to Congress\n##### (a) Public outreach campaign\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury, Secretary of Labor, and Secretary of Commerce (referred to in this section as the Secretaries ) shall jointly develop and carry out a public outreach campaign to promote the availability of the workforce artificial intelligence training credit under section 45BB of the Internal Revenue Code of 1986, as added by section 2. Such campaign shall include the publication of information on such credit, informational webinars for businesses, and distribution of multilingual informational materials through small business development centers, trade associations, and workforce boards.\n##### (b) Report to Congress\nNot later than 360 days after the date of the enactment of this Act, and annually thereafter, the Secretaries shall submit to Congress a report on the public outreach campaign carried out under subsection (a) and any measurable outcomes of such campaign.",
      "versionDate": "2026-02-13",
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
        "updateDate": "2026-03-11T22:57:28Z"
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
      "date": "2026-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7576ih.xml"
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
      "title": "AI Workforce Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T05:23:28Z"
    },
    {
      "title": "AI Workforce Training Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T05:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a credit for workforce artificial intelligence training, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T05:18:21Z"
    }
  ]
}
```
