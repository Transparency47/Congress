# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7157
- Title: Supporting Teachers Through Tax Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 7157
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-02-18T19:54:25Z
- Update date including text: 2026-02-18T19:54:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7157",
    "number": "7157",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000110",
        "district": "6",
        "firstName": "Cleo",
        "fullName": "Rep. Fields, Cleo [D-LA-6]",
        "lastName": "Fields",
        "party": "D",
        "state": "LA"
      }
    ],
    "title": "Supporting Teachers Through Tax Fairness Act",
    "type": "HR",
    "updateDate": "2026-02-18T19:54:25Z",
    "updateDateIncludingText": "2026-02-18T19:54:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
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
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:01:45Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7157ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7157\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mr. Fields introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income up to the first $50,000 wages from employment as a K\u201312 public school teacher.\n#### 1. Short title\nThis Act may be cited as the Supporting Teachers Through Tax Fairness Act .\n#### 2. K\u201312 public school teacher exclusion\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139M. K\u201312 public school teacher wages (a) In general In the case of an individual, gross income shall not include so much of the wages received by such individual with respect to employment as an eligible educator as does not exceed $50,000. (b) Definitions and special rules For purposes of this section\u2014 (1) Eligible educator (A) In general The term eligible educator means, with respect to any taxable year, an individual who for at least 900 hours during a school year ending during the taxable year is a kindergarten through grade 12 teacher, instructor, counselor, or aide in a public elementary or secondary school. (B) Public school (i) In general The term elementary or secondary school means any school which provides elementary education or secondary education (including a charter school), as determined under State law. (ii) Public school The term public elementary or secondary school means any school which provides such education at public expense, under public supervision and direction, and without tuition charge. (2) Increased limit for certain schools (A) In general Subsection (a) shall be applied by substituting $65,000 for $50,000 with respect to an individual in the case of each of the following: (i) An eligible educator who meets the 900 hour requirement under paragraph (1)(A) for the taxable year with respect to a school not less than 75 percent of the students of which are eligible for free or reduced-cost lunches under the school lunch program established under the National School Lunch Act. (ii) An eligible educator who meets the 900 hour requirement under paragraph (1)(A) for the taxable year with respect to a school located in a rural area. (iii) An eligible educator who meets the 900 hour requirement under paragraph (1)(A) for the taxable year as a teacher, instructor, or aid in special education or science, technology, engineering, or mathematics. (B) Rural area For purposes of this paragraph, the term rural area any area other than\u2014 (i) city or town that has a population of greater than 50,000 inhabitants, and (ii) any urbanized area contiguous and adjacent to a city or town described in clause (i). (3) Wages The term wages means all remuneration for services performed by an employee for the employee\u2019s employer, but only to the extent includible in gross income of the individual. (c) Regulations The Secretary shall prescribe such rules as may be necessary to carry out the purposes of this section, including a process through which elementary and secondary schools can provide to eligible educators and the Secretary statements demonstrating an individual as having met for any period the requirements of subsection (b)(1)(A) and any of the requirements of clause (i), (ii), or (iii) of subsection (b)(2)(A). .\n##### (b) Conforming amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting before the item relating to section 140 the following new item:\nSec. 139M. K\u201312 public school teacher wages. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-01-20",
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
        "updateDate": "2026-02-18T19:54:25Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7157ih.xml"
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
      "title": "Supporting Teachers Through Tax Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Teachers Through Tax Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from gross income up to the first $50,000 wages from employment as a K-12 public school teacher.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:24Z"
    }
  ]
}
```
