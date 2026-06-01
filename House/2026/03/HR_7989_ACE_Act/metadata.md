# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7989?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7989
- Title: ACE Act
- Congress: 119
- Bill type: HR
- Bill number: 7989
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-04-02T17:07:35Z
- Update date including text: 2026-04-02T17:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7989",
    "number": "7989",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "ACE Act",
    "type": "HR",
    "updateDate": "2026-04-02T17:07:35Z",
    "updateDateIncludingText": "2026-04-02T17:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:00:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7989ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7989\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Thompson of Pennsylvania (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the weights used to determine amounts for targeted grants and education finance incentive grants for local educational agencies under title I of the Elementary and Secondary Education Act of 1965.\n#### 1. Short title\nThis Act may be cited as the All Children are Equal Act or the ACE Act .\n#### 2. Findings\nSection 1125AA of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6336 ) is amended\u2014\n**(1)**\nby amending the heading to read as follows:\n1125AA. Increase grants per formula student as the percentage of economically disadvantaged children in a local educational agency increases ;\nand\n**(2)**\nby amending subsection (a) to read as follows:\n(a) Findings Congress makes the following findings: (1) The current Basic Grant Formula for the distribution of funds under this part does not adequately target funds for schools with the highest concentrations of economically disadvantaged students. (2) The current formulas for distributing Targeted and Education Finance Incentive Grants is intended to allocate more funds per formula student to local educational agencies with higher concentrations of such students. (3) These formula use two weighting systems, one based on the percentage of the aged 5\u201317 population in a local education agency that is eligible to receive funds under this title (percentage weighting), and another based on the absolute number of such students (number weighting). Whichever of these weighting systems results in the highest total weighted formula student count for a local educational agency is the weighting system used for that agency in the final allocation of Targeted and Education Finance Incentive Grant funds. (4) Since the amount available to be distributed through these formulas is fixed by congressional appropriation, any gain in allocation share by one local educational agency causes a loss to other local educational agencies. (5) The number weighting alternative is often favorable to very large local educational agencies, even if the agency\u2019s formula student percentage is low. But because smaller local education agencies simply do not have enough students to gain from number weighting, they are adversely affected under the number weighting alternative. (6) The Congressional Research Service has compared the funding allocations of each local education agency for school year 2021\u20132022 under the current dual weighting system with the funding allocation it would have that year if all local educational agencies had their student count weighted only by percentage weighting. (7) This data shows that the use of number weighting in these formulas has shifted funding from smaller to larger local educational agencies notwithstanding the level of poverty in either. This is contrary to the intent of Congress, which is to direct more funding per formula student to local educational agencies with high concentrations of poverty, as measured by the number of formula students as a percentage of the aged 5\u201317 population of the local educational agency. (8) The National Center for Education Statistics confirmed these findings in a statistical analysis report dated May 2019. (9) Congress has a responsibility to correct this unintended inequity by reducing the power of the number weighting system relative to the percentage weighting system so that local educational agencies with high percentages of poverty but low numbers of students are not disadvantaged under the formulas used for grants under this part. .\n#### 3. Targeted grants to local educational agencies\nSection 1125(c)(2)(A) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6335(c)(2)(A) ) is amended to read as follows:\n(A) In general For each fiscal year for which the Secretary uses local educational agency data, the weighted child count used to determine a local educational agency\u2019s grant under this section\u2014 (i) for each fiscal year through fiscal year 2025, is the larger of the two amounts determined under subparagraphs (B) and (C); and (ii) for fiscal year 2026 and each succeeding fiscal year, is the amount determined under subparagraph (B). .\n#### 4. Education Finance Incentive Grant Program\n##### (a) States with an equity Factor less than 0.10\nSection 1125A(d)(1)(B)(i) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6337(d)(1)(B)(i) ) is amended to read as follows:\n(i) In general For each fiscal year for which the Secretary uses local educational agency data, the weighted child count used to determine a local educational agency\u2019s grant under this section\u2014 (I) for each fiscal year through fiscal year 2025, is the larger of the two amounts determined under clauses (ii) and (iii); and (II) for fiscal year 2026 and each succeeding fiscal year, is the amount determined under clause (iii). .\n##### (b) States with an equity factor greater than or equal to 0.10 and less than 0.20\nSection 1125A(d)(2)(B)(i) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6337(d)(2)(B)(i) ) is amended to read as follows:\n(i) In general For each fiscal year for which the Secretary uses local educational agency data, the weighted child count used to determine a local educational agency\u2019s grant under this section\u2014 (I) for each fiscal year through fiscal year 2025, is the larger of the two amounts determined under clauses (ii) and (iii); and (II) for fiscal year 2026 and each succeeding fiscal year, is the amount determined under clause (iii). .\n##### (c) States with an equity factor greater than or equal to 0.20\nSection 1125A(d)(3)(B)(i) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6337(d)(3)(B)(i) ) is amended to read as follows:\n(i) In general For each fiscal year for which the Secretary uses local educational agency data, the weighted child count used to determine a local educational agency\u2019s grant under this section\u2014 (I) for each fiscal year through fiscal year 2025, is the larger of the two amounts determined under clauses (ii) and (iii); and (II) for fiscal year 2026 and each succeeding fiscal year, is the amount determined under clause (iii). .",
      "versionDate": "2026-03-18",
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
        "updateDate": "2026-04-02T17:07:35Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7989ih.xml"
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
      "title": "ACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T06:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "All Children are Equal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the weights used to determine amounts for targeted grants and education finance incentive grants for local educational agencies under title I of the Elementary and Secondary Education Act of 1965.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T06:33:36Z"
    }
  ]
}
```
