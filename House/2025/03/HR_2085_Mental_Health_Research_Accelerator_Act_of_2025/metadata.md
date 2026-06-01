# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2085
- Title: Mental Health Research Accelerator Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2085
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-04-28T08:06:50Z
- Update date including text: 2026-04-28T08:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2085",
    "number": "2085",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Mental Health Research Accelerator Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:50Z",
    "updateDateIncludingText": "2026-04-28T08:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:06:00Z",
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "IN"
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
      "sponsorshipDate": "2026-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2085ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2085\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Thompson of California (for himself and Mr. Kelly of Pennsylvania ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for a credit against tax for expenses for translational research regarding neurodegenerative diseases and psychiatric conditions.\n#### 1. Short title\nThis Act may be cited as the Mental Health Research Accelerator Act of 2025 .\n#### 2. Expenses for certain translational research\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Expenses for certain translational research (a) Allowance of credit For purposes of section 38, the translational research credit determined under this section for any taxable year shall be an amount equal to 25 percent of the amounts paid or incurred by the taxpayer during such taxable year which are necessary for translational research regarding neurodegenerative diseases and psychiatric conditions. (b) Limitation (1) Taxpayer limitation The credit allowed under this section to a taxpayer for a taxable year beginning in any calendar year shall not exceed the portion of the limitation amount allocated to the taxpayer under this subsection reduced by the amount of credit allowed to the taxpayer under this section for all prior taxable years. (2) Aggregate national limitation (A) In general There is a translational research credit limitation for each calendar year as follows: (i) $1,000,000,000 for 2026. (ii) $2,000,000,000 for each of years 2027 through 2030. (iii) $1,000,000,000 for 2031. (B) Allocation of limitation As expeditiously as possible, the Secretary shall allocate among applicants selected by the Secretary the limitation under subparagraph (A) for all years. (C) Carryover of unused limitation If the translational research credit limitation for any calendar year exceeds the aggregate amount allocated under subparagraph (A) for such year, such limitation for the succeeding calendar year shall be increased by the amount of such excess. (D) Regulations The Secretary shall (in consultation with the Secretary of Health and Humans Services, the Administrator of the Food and Drug Administration, and the Director of the National Institutes of Health) prescribe regulations as may be necessary to carry out the purposes of this section, including establishing the application process and the criteria for allocation under subparagraph (B). Such regulations shall include the following: (i) Amounts shall be allocated based on scientific merit. (ii) Projects should include all phases of the research continuum. (iii) An emphasis on new therapeutics and devices targeted at central nervous system disorders and in the neurological and psychiatric fields. (iv) Standards for repurposing existing drugs and devices for new purposes. (v) Standards for public-private partnerships with priority given to collaborative efforts and sharing of intellectual property held by tax exempt entities involved in the project. (c) Transfer of credit (1) In general If, with respect to a credit under subsection (a) for any taxable year\u2014 (A) a tax-exempt entity would be the taxpayer (but for this paragraph), and (B) such entity elects the application of this paragraph for such taxable year with respect to all (or any portion specified in such election) of such credit, the eligible project partner specified in such election, and not the tax-exempt entity, shall be treated as the taxpayer for purposes of this title with respect to such credit (or such portion thereof). (2) Definitions For purposes of this subsection\u2014 (A) Tax-exempt entity The term tax-exempt entity means\u2014 (i) a Federal, State, Indian tribal government (as defined in section 7701(a)(4)), or local government entity, or any political subdivision, agency, or instrumentality thereof, and (ii) an organization described in section 501(c)(3) and exempt from tax under section 501(a). (B) Eligible project partner The term eligible project partner means any person who\u2014 (i) is identified in the application for allocation of credit under this section as a project partner, and (ii) participates in, or provides funding for, the research with respect to which limitation was allocated by the Secretary under subsection (b). (3) Special rules (A) In general In the case of a credit under subsection (a) which is determined at the partnership level\u2014 (i) for purposes of paragraph (1)(A), a tax-exempt entity shall be treated as the taxpayer with respect to such entity\u2019s distributive share of such credit, and (ii) the term eligible project partner shall include any partner of the partnership. (B) Taxable year in which credit taken into account In the case of any credit (or portion thereof) with respect to which an election is made under paragraph (1), such credit shall be taken into account in the first taxable year of the eligible project partner ending with, or after, the tax-exempt entity\u2019s taxable year with respect to which the credit was determined. (d) Coordination with credit for increasing research expenditures (1) In general Except as provided in paragraph (2), any expenses taken into account under this section shall not be taken into account for purposes of determining the credit allowable under section 41 for such taxable year. (2) Expenses included in determining base period research expenses Any expenses taken into account under this section which are qualified research expenses (within the meaning of section 41(b)) shall be taken into account in determining base period research expenses for purposes of applying section 41 to subsequent taxable years. (e) Termination No credit shall be allowed under this section for any taxable year beginning after December 31, 2035. .\n##### (b) Deduction disallowed\nSection 280C of such Code is amended by adding at the end the following new subsection:\n(i) Credit for certain translational research No deduction shall be allowed for that portion of the expenses taken into account under section 45BB otherwise allowable as a deduction for the taxable year which is equal to the amount of the credit determined for such taxable year under such section. .\n##### (c) Credit made part of general business credit\nSection 38(b) of the Internal Revenue Code of 1986 is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the credit determined under section 45BB. .\n##### (d) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Expenses for certain translational research.\n##### (e) Effective date\nThe amendments made by this subsection shall take effect on the date of the enactment of this Act.",
      "versionDate": "2025-03-11",
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
        "updateDate": "2025-05-08T19:05:00Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2085ih.xml"
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
      "title": "Mental Health Research Accelerator Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mental Health Research Accelerator Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for a credit against tax for expenses for translational research regarding neurodegenerative diseases and psychiatric conditions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:39Z"
    }
  ]
}
```
