# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2764?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2764
- Title: Tax Cut for Workers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2764
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-04-01T21:14:51Z
- Update date including text: 2026-04-01T21:14:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2764",
    "number": "2764",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "E000296",
        "district": "3",
        "firstName": "Dwight",
        "fullName": "Rep. Evans, Dwight [D-PA-3]",
        "lastName": "Evans",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Tax Cut for Workers Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-01T21:14:51Z",
    "updateDateIncludingText": "2026-04-01T21:14:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:04:20Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "AZ"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CT"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-09",
      "state": "DC"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "AL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NV"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2764ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2764\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Evans of Pennsylvania (for himself, Mr. Khanna , Ms. Ansari , Ms. Crockett , Ms. DeLauro , Mrs. Foushee , Mr. McGovern , Mr. Nadler , Ms. Norton , Ms. Ocasio-Cortez , Mrs. Ramirez , Ms. S\u00e1nchez , Ms. Scanlon , Ms. Sewell , Ms. Simon , Mr. Thanedar , Ms. Titus , Ms. Tlaib , and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand, and make permanent certain modifications of, the earned income credit.\n#### 1. Short title\nThis Act may be cited as the Tax Cut for Workers Act of 2025 .\n#### 2. Permanent extension of earned income credit rules for individuals without qualifying children\n##### (a) Decrease in minimum age for credit\n**(1) In general**\nSubclause (II) of section 32(c)(1)(A)(ii) of the Internal Revenue Code of 1986 is amended by striking age 25 and inserting the applicable minimum age .\n**(2) Applicable minimum age**\nParagraph (1) of section 32(c) of such Code is amended by adding at the end the following new subparagraph:\n(F) Applicable minimum age For purposes of this paragraph\u2014 (i) In general The term applicable minimum age means\u2014 (I) except as otherwise provided in this clause, age 19, (II) in the case of a student (as defined in section 152(f)(2)), other than a qualified former foster youth or a qualified homeless youth, age 24, and (III) in the case of a qualified former foster youth or a qualified homeless youth, age 18. (ii) Qualified former foster youth For purposes of this subparagraph, the term qualified former foster youth means an individual who\u2014 (I) on or after the date that such individual attained age 14, was in foster care provided under the supervision or administration of an entity administering (or eligible to administer) a plan under part B or part E of title IV of the Social Security Act (without regard to whether Federal assistance was provided with respect to such child under such part E), and (II) provides (in such manner as the Secretary may provide) consent for entities which administer a plan under part B or part E of title IV of the Social Security Act to disclose to the Secretary information related to the status of such individual as a qualified former foster youth. (iii) Qualified homeless youth For purposes of this subparagraph, the term qualified homeless youth means, with respect to any taxable year, an individual who certifies, in a manner as provided by the Secretary, that such individual is either an unaccompanied youth who is a homeless child or youth, or is unaccompanied, at risk of homelessness, and self-supporting. .\n##### (b) Elimination of maximum age for credit\nSubclause (II) of section 32(c)(1)(A)(ii) of the Internal Revenue Code of 1986 is amended by striking but not attained age 65 .\n##### (c) Increase in credit and phaseout percentages\nThe table contained in paragraph (1) of section 32(b) of the Internal Revenue Code of 1986 is amended by striking 7.65 each place it appears and inserting 15.3 .\n##### (d) Increase in earned income and phaseout amounts\nThe table contained in subparagraph (A) of section 32(b)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking $4,220 and inserting $9,820 , and\n**(2)**\nby striking $5,280 and inserting $11,610 .\n##### (e) Inflation adjustments\n**(1) In general**\nParagraph (1) of section 32(j) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) In general In the case of any taxable year beginning after\u2014 (A) 2021, in the case of the dollar amount in subsection (i)(1), (B) 2026, in the case of the dollar amounts in the third row of the table in subsection (b)(2)(A), and (C) 2015, in any other case, each of the dollar amounts in subsections (b)(2) and (i)(1) shall be increased by an amount equal to the inflation amount. .\n**(2) Inflation amount**\nSubsection (j) of section 32 of such Code is amended by adding at the end the following new paragraph:\n(3) Inflation amount For purposes of paragraph (1), the inflation amount with respect to any dollar amount for any taxable year is the amount equal to\u2014 (A) such dollar amount, multiplied by (B) the percentage (if any) by which\u2014 (i) the CPI (as defined in section 1(f)(4)) for the calendar year preceding the year in which the taxable year begins, exceeds (ii) the CPI (as so defined) for\u2014 (I) in the case of amounts in the third row of the table in subsection (b)(2)(A), 2025, (II) in the case of any other amount in subsection (b)(2)(A), 1995, (III) in the case of the $5,000 amount in subsection (b)(2)(B), 2008, and (IV) in the case of the $10,000 amount in subsection (i)(1), 2020. .\n##### (f) Conforming amendment\nSection 32 of the Internal Revenue Code of 1986 is amended by striking subsection (n).\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Application of earned income credit to possessions of the United States\n##### (a) Puerto Rico\nSubparagraph (B) of section 7530(a)(1) of the Internal Revenue Code of 1986 is amended by striking in the case of calendar years 2021 through 2025, .\n##### (b) Possessions with mirror code tax systems\nSubparagraph (B) of section 7530(b)(1) of the Internal Revenue Code of 1986 is amended by striking in the case of calendar years 2021 through 2025, .\n##### (c) American Samoa\nSubparagraph (B) of section 7530(c)(1) of the Internal Revenue Code of 1986 is amended by striking in the case of calendar years 2021 through 2025, .\n#### 4. Election to use prior year earned income\n##### (a) In general\nParagraph (2) of section 32(c) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Election to use prior year earned income (i) In general If the earned income of the taxpayer for any taxable year is less than the earned income of the taxpayer for the preceding taxable year, the credit allowed under subsection (a) may, at the election of the taxpayer, be determined by substituting\u2014 (I) such earned income for such preceding taxable year, for (II) such earned income for the taxable year for which such credit is being determined. (ii) Application to joint returns For purposes of clause (i), in the case of a joint return, the earned income of the taxpayer for the preceding taxable year shall be the sum of the earned income of each spouse for such taxable year. (iii) Special rules (I) Errors treated as mathematical errors For purposes of section 6213, an incorrect use on a return of earned income pursuant to clause (i) shall be treated as a mathematical or clerical error. (II) No effect on determination of gross income, etc Except as otherwise provided in this subparagraph, this title shall be applied without regard to any substitution under clause (i). .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4042",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep Your Pay Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1372",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tax Cut for Workers Act of 2025",
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
        "updateDate": "2025-05-09T18:03:36Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2764ih.xml"
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
      "title": "Tax Cut for Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tax Cut for Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand, and make permanent certain modifications of, the earned income credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T03:18:22Z"
    }
  ]
}
```
