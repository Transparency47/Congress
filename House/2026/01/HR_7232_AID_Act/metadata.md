# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7232?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7232
- Title: AID Act
- Congress: 119
- Bill type: HR
- Bill number: 7232
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-02-06T16:24:27Z
- Update date including text: 2026-02-06T16:24:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7232",
    "number": "7232",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "AID Act",
    "type": "HR",
    "updateDate": "2026-02-06T16:24:27Z",
    "updateDateIncludingText": "2026-02-06T16:24:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7232ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7232\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Ms. Stevens introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to provide a student loan allowance calculation for purposes of determining the student aid index.\n#### 1. Short title\nThis Act may be cited as the Alleviating Intergenerational Debt Act or the AID Act .\n#### 2. Student loan allowance calculation for award year 2027\u20132028 and each succeeding award year\n##### (a) In general\nSection 475(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1087oo(c) ), as amended by title VII of division FF of the FAFSA Simplification Act ( Public Law 116\u2013260 ), is further amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking and at the end of subparagraph (C);\n**(B)**\nby striking the period at the end of subparagraph (D) and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) beginning with award year 2027\u20132028, a student loan allowance, determined in accordance with paragraph (5). ; and\n**(2)**\nby adding at the end the following:\n(5) Student loan allowance (A) In general The student loan allowance is equal to the lesser of $4,000 or 15 percent of the single parent\u2019s outstanding student loan debt or married parents\u2019 combined outstanding student loan debt (as adjusted under section 478(i)). (B) Exceptions A single parent with an adjusted gross income of more than $200,000 (as adjusted under section 478(i)), or married parents with a combined adjusted gross income of more than $400,000 (as so adjusted), may not receive a student loan allowance under this paragraph. (C) Definitions In this paragraph: (i) Federal student loan The term Federal student loan means any loan made, insured, or guaranteed under this title. (ii) Outstanding student loan debt The term outstanding student loan debt , used with respect to a parent, means the total amount of principal, interest, and fees owed by such parent, as of the date of determination of the allowance under this paragraph, on Federal student loans. .\n##### (b) Adjustment\nSection 478 of the Higher Education Act of 1965 ( 20 U.S.C. 1087rr ), as amended by title VII of division FF of the FAFSA Simplification Act ( Public Law 116\u2013260 ), is further amended by adding at the end the following:\n(i) Student loan expense allowance For award year 2028\u20132029 and each succeeding award year, the Secretary shall publish in the Federal Register a revised table of student loan allowances for the purpose of section 475(c)(5). Such revised table shall be developed by increasing the dollar amounts specified in subparagraphs (A) and (B) of section 475(c)(5) by a percentage equal to the percentage increase in the Consumer Price Index, as defined in subsection (f), between April 2022 and the April in the year prior to the beginning of the award year and rounding the result to the nearest $10. .\n#### 3. Report to Congress\n##### (a) In general\nNot later than July 1, 2028, and on an annual basis thereafter, the Secretary of Education shall prepare and submit to Congress a report on the impacts of the amendments made by this Act, which shall include the following information with respect to the most recent award year for which information is available:\n**(1)**\nThe number and percentage of dependent students whose student aid index computations under subsection (a) of section 475 of the Higher Education Act of 1965 ( 20 U.S.C. 1087oo ) include the subtraction under subsection (c) of such section 475 of a student loan allowance determined under paragraph (5) of such subsection (c), as added by section 2, from the parents\u2019 total income, disaggregated\u2014\n**(A)**\nby students who are eligible for a Federal Pell Grant under section 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ) for such award year; and\n**(B)**\nby students who are not eligible for such a Federal Pell Grant.\n**(2)**\nThe average amount of the student loan allowance described in paragraph (1).",
      "versionDate": "2026-01-22",
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
        "name": "Education",
        "updateDate": "2026-02-06T16:24:26Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7232ih.xml"
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
      "title": "AID Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AID Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Alleviating Intergenerational Debt Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to provide a student loan allowance calculation for purposes of determining the student aid index.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T04:18:24Z"
    }
  ]
}
```
