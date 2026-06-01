# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/601
- Title: Estate Tax Rate Reduction Act
- Congress: 119
- Bill type: HR
- Bill number: 601
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-02-28T19:24:53Z
- Update date including text: 2025-02-28T19:24:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/601",
    "number": "601",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Estate Tax Rate Reduction Act",
    "type": "HR",
    "updateDate": "2025-02-28T19:24:53Z",
    "updateDateIncludingText": "2025-02-28T19:24:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-22T15:03:10Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr601ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 601\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Arrington (for himself and Mr. Bishop ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to reduce the rate of tax on estates, gifts, and generation-skipping transfers.\n#### 1. Short title\nThis Act may be cited as the Estate Tax Rate Reduction Act .\n#### 2. Reduction of rate of tax on estates, gifts, and generation-skipping transfers\n##### (a) In general\nSection 2001 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking subsection (c) and inserting the following:\n(c) Rate of tax For purposes of determining the tentative tax, the rate of tax shall be 20 percent of the amount with respect to which the tentative tax is computed. ; and\n**(2)**\nin subsection (g)(1), by striking rates of tax under subsection (c) and inserting rate of tax under subsection (c) .\n##### (b) Conforming amendments\n**(1)**\nSection 2056A(b)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subparagraph (B)(i), by striking highest ; and\n**(B)**\nin subparagraph (C), by striking highest .\n**(2)**\nSection 2107(a) of such Code is amended by striking the table contained in and inserting the rate of tax under .\n**(3)**\nSection 2201(a) of such Code is amended by striking the rate schedule set forth in section 2001(c) and inserting the rate of tax under section 2001(c) .\n**(4)**\nSection 2641 of such Code is amended to read as follows:\n2641. Applicable rate For purposes of this chapter, the term applicable rate means, with respect to any generation-skipping transfer, the product of\u2014 (1) the rate imposed by section 2001 on the estates of decedents dying at the time of the taxable distribution, taxable termination, or direct skip, as the case may be, and (2) the inclusion ratio with respect to the transfer. .\n**(5)**\nSection 2801(a)(1) of such Code is amended by striking the highest rate of tax specified in the table contained in and inserting the rate of tax under .\n**(6)**\nSection 6601(j)(2)(A)(i) of such Code is amended by striking the rate schedule set forth in .\n##### (c) Effective date\nThe amendments made by this section shall apply to estates of decedents dying, generation-skipping transfers, and gifts made, after December 31, 2024.\n##### (d) Budgetary effects\n**(1) PAYGO scorecard**\nThe budgetary effects of this section shall not be entered on either PAYGO scorecard maintained pursuant to section 4(d) of the Statutory Pay-As-You-Go Act of 2010 ( 2 U.S.C. 933(d) ).\n**(2) Senate PAYGO scorecard**\nThe budgetary effects of this section shall not be entered on any PAYGO scorecard maintained for purposes of section 4106 of H. Con. Res. 71 (115th Congress), the concurrent resolution on the budget for fiscal year 2018.",
      "versionDate": "2025-01-22",
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
        "updateDate": "2025-02-28T19:24:53Z"
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
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr601ih.xml"
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
      "title": "Estate Tax Rate Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Estate Tax Rate Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to reduce the rate of tax on estates, gifts, and generation-skipping transfers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T06:49:31Z"
    }
  ]
}
```
