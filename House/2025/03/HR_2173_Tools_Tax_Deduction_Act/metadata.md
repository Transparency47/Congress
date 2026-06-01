# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2173?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2173
- Title: Tools Tax Deduction Act
- Congress: 119
- Bill type: HR
- Bill number: 2173
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-10-01T08:06:08Z
- Update date including text: 2025-10-01T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2173",
    "number": "2173",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Tools Tax Deduction Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:08Z",
    "updateDateIncludingText": "2025-10-01T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:05:25Z",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2173ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2173\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Ms. Budzinski (for herself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for deductions for the performance of certain services by a taxpayer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tools Tax Deduction Act .\n#### 2. Allowance of deduction for certain expenses of being an employee\n##### (a) Above-the-Line deduction for certain expenses\nSection 62(a)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new sentence: The limitation under the preceding sentence shall not apply to deductions which are attributable to a trade or business consisting of the performance of services by the taxpayer as an employee if such deductions are for construction tools, personal protective clothing and gear, and other expenses in connection with such place of employment which are necessary for such individual to be able to work. .\n##### (b) Allowance of miscellaneous itemized deduction for other expenses of the trade or business of being an employee\nSection 67(g) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 2025.\u2014 Notwithstanding subsection (a), and inserting\n2025.\u2014 (1) In general Notwithstanding subsection (a), except as provided in paragraph (2), , and\n**(2)**\nby adding at the end the following:\n(2) Exceptions for expenses of the trade or business of being an employee (A) In general Paragraph (1) shall not apply to miscellaneous itemized deductions for any taxable year which are itemized deductions attributable to a trade or business carried on by the taxpayer which consists of the performance of services by the taxpayer as an employee. (B) Application of 2-percent test In applying subsection (a) for any taxable year to which this paragraph applies, only the itemized deductions described in subparagraph (A) shall be taken into account as miscellaneous itemized deductions. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-05-08T19:24:45Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2173ih.xml"
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
      "title": "Tools Tax Deduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tools Tax Deduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T07:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow for deductions for the performance of certain services by a taxpayer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T07:48:27Z"
    }
  ]
}
```
