# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4047?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4047
- Title: Kids in Classes Act
- Congress: 119
- Bill type: S
- Bill number: 4047
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-03-30T15:56:04Z
- Update date including text: 2026-03-30T15:56:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4047",
    "number": "4047",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Kids in Classes Act",
    "type": "S",
    "updateDate": "2026-03-30T15:56:04Z",
    "updateDateIncludingText": "2026-03-30T15:56:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-11T14:27:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4047is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4047\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Mr. Scott of South Carolina introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish an alternative use of certain Federal education funds when in-person instruction is not available.\n#### 1. Short title\nThis Act may be cited as the Kids in Classes Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nResearch indicates that children living in the poorest 20 percent of neighborhoods in the United States will experience the most negative and long-lasting effects of school closures.\n**(2)**\nResearchers predict that 1 year of school closures will cost ninth graders in the poorest communities a 25-percent decrease in their post-educational earning potential, even if that year of closure is followed by 3 years of normal schooling. By contrast, the same researchers predict no substantial losses for students from the richest 20 percent of neighborhoods.\n**(3)**\nLong periods of school closures during the COVID\u201319 pandemic deprive low-income students and students of color the equalizing force of education.\n**(4)**\nSchool closures will widen educational inequality and the learning gaps created by these closures will persist as students progress through high school, putting their future prospects at risk.\n**(5)**\nData shows that closed classrooms were disproportionately composed of disadvantaged students, as well as students with low mathematics scores, students with limited English proficiency, or students who qualify for a free or reduced priced lunch.\n**(6)**\nSchool shutdowns contribute to disproportionate learning loss for disadvantaged students, compounding existing gaps.\n#### 3. Use of title I funds if in-person instruction is not available\nSection 1112 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6312 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (6), by striking and after the semicolon;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(8) comply with the in-person instruction requirements described in subsection (f). ; and\n**(2)**\nby adding at the end the following:\n(f) In-Person instruction requirements (1) Definitions In this subsection: (A) Covered funding amount The term covered funding amount means the quotient of\u2014 (i) an amount equal to\u2014 (I) the funds provided under this part to a particular elementary school or secondary school; divided by (II) the number of students who attend that school; divided by (ii) the number of school days for which such funds have been provided. (B) Covered school The term covered school means a public elementary school or secondary school that receives funds provided under this part. (C) Qualified educational expenses The term qualified educational expenses means curriculum and curricular materials, books or instructional materials, technological educational materials, online educational materials, tutoring or educational classes outside the home, private school tuition, testing fees, diagnostic tools, and educational therapies for students with disabilities. (2) Distribution of covered funding Not later than the beginning of the first school year that begins after the date of enactment of the Kids in Classes Act , and notwithstanding any other provision of law, in order to be eligible to receive funds under this part, each local educational agency shall\u2014 (A) establish a failure to open direct payment plan in accordance with paragraph (3); and (B) agree to carry out such plan in the event that a covered school served by the local educational agency fails for more than 3 days during a school year, for reasons related to public health emergency or collective bargaining action, to make available in-person instruction for all students who wish to attend. (3) Failure to open direct payment plan (A) In general Each local educational agency shall establish a failure to open direct payment plan that establishes and explains how a parent of each child who attends a covered school served by the local educational agency will be directly paid, for use on qualified educational expenses, the amount described in subparagraph (B), if that covered school fails for more than 3 days during a school year, for reasons related to public health emergency or collective bargaining action, to make available in-person instruction for all students who wish to attend. (B) Amount of payment The amount of payment shall be an amount equal to\u2014 (i) the covered funding amount; multiplied by (ii) the number of days in which such school fails, for reasons related to public health emergency or collective bargaining action, to make available in-person instruction for all students who wish to attend. (C) Timing of payment To the greatest extent practicable, direct payments made to parents under this subsection shall be made to parents on each day that a covered school fails to open as described in subparagraph (A). (D) Receipts As part of the failure to open direct payment plan, each local educational agency shall require that parents receiving direct payments under this subsection\u2014 (i) submit receipts to the local educational agency to demonstrate that such direct payments have been spent on qualified educational expenses; or (ii) return any amounts of such direct payments that are not used for qualified educational expenses to the local educational agency not later than 30 days after the covered school has resumed in-person instruction. .",
      "versionDate": "2026-03-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-03-12",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "7918",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Kids in Classes Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-03-30T15:54:21Z"
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
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4047is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Kids in Classes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kids in Classes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish an alternative use of certain Federal education funds when in-person instruction is not available.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T04:03:30Z"
    }
  ]
}
```
