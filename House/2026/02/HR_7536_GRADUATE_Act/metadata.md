# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7536
- Title: GRADUATE Act
- Congress: 119
- Bill type: HR
- Bill number: 7536
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-03-10T08:05:35Z
- Update date including text: 2026-03-10T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7536",
    "number": "7536",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "GRADUATE Act",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:35Z",
    "updateDateIncludingText": "2026-03-10T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:01:10Z",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "DC"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "AL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "ME"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "IL"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7536ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7536\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Goldman of New York (for himself, Ms. Jacobs , Mr. Garcia of California , Ms. Norton , Mr. Figures , and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the deduction for student loan interest to include payments toward principal, and to increase the value of the deduction.\n#### 1. Short title\nThis Act may be cited as the Generating Relief for Academic Debt Using Assisted Tax Efficiency Act or the GRADUATE Act .\n#### 2. Education loan deduction\n##### (a) In general\nSection 221 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by striking Interest on education loans and inserting Education loans ,\n**(2)**\nby amending subsection (a) to read as follows:\n(a) Allowance of deduction In the case of an individual, there shall be allowed as a deduction for the taxable year an amount equal to the amounts paid by the taxpayer during the taxable year on any qualified education loan. ,\n**(3)**\nby amending subsection (b) to read as follows:\n(b) Maximum deduction (1) In general Except as provided in paragraph (2), the deduction allowed by subsection (a) for the taxable year shall not exceed an amount equal to the sum of\u2014 (A) $10,000, plus (B) $500 multiplied by the number of dependents of the taxpayer for such taxable year. (2) Limitation based on modified adjusted gross income (A) In general The amount which would (but for this paragraph) be allowable as a deduction under this section shall be reduced (but not below zero) by the amount determined under subparagraph (B). (B) Amount of reduction The amount determined under this subparagraph is the amount which bears the same ratio to the amount which would be so taken into account as\u2014 (i) the excess of\u2014 (I) the taxpayer\u2019s modified adjusted gross income for such taxable year, over (II) $125,000 ($250,000 in the case of a joint return), bears to (ii) $25,000 ($50,000 in the case of a joint return). (C) Modified adjusted gross income The term modified adjusted gross income means adjusted gross income determined\u2014 (i) without regard to this section and sections 85(c), 911, 931, and 933, and (ii) after application of sections 86, 135, 137, 219, and 469. , and\n**(4)**\nin subsection (f)(1)\u2014\n**(A)**\nby striking after 2002 and inserting after 2026 ,\n**(B)**\nby striking $50,000 and $100,000 and inserting $125,000 and $250,000 , and\n**(C)**\nin subparagraph (B), by striking calendar year 2001 and inserting calendar year 2025 .\n##### (b) Conforming amendment\nSection 62(a)(17) of such Code is amended to read as follows:\n(17) Education loan payments The deduction allowed by section 221. .\n##### (c) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-02-27T19:06:50Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7536ih.xml"
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
      "title": "GRADUATE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T06:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRADUATE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Generating Relief for Academic Debt Using Assisted Tax Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the deduction for student loan interest to include payments toward principal, and to increase the value of the deduction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T06:18:36Z"
    }
  ]
}
```
