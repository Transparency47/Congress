# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2667?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2667
- Title: Flexible Savings Arrangements for a Healthy Robust America Act
- Congress: 119
- Bill type: HR
- Bill number: 2667
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-02-13T15:46:13Z
- Update date including text: 2026-02-13T15:46:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2667",
    "number": "2667",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Flexible Savings Arrangements for a Healthy Robust America Act",
    "type": "HR",
    "updateDate": "2026-02-13T15:46:13Z",
    "updateDateIncludingText": "2026-02-13T15:46:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:02:15Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2667ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2667\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Bean of Florida (for himself, Mr. Panetta , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow distributions from a health flexible spending arrangement or health reimbursement arrangement directly to a health savings account in connection with establishing coverage under a high deductible health plan.\n#### 1. Short title\nThis Act may be cited as the Flexible Savings Arrangements for a Healthy Robust America Act .\n#### 2. FSA and HRA terminations or conversions to fund HSAs\n##### (a) In general\nSection 106(e)(2) of the Internal Revenue Code of 1986 is amended to read as follows:\n(2) Qualified HSA distribution For purposes of this subsection\u2014 (A) In general The term qualified HSA distribution means, with respect to any employee, a distribution from a health flexible spending arrangement or health reimbursement arrangement of such employee directly to a health savings account of such employee if\u2014 (i) such distribution is made in connection with such employee establishing coverage under a high deductible health plan (as defined in section 223(c)(2)) after a significant period of not having such coverage, and (ii) such arrangement is described in section 223(c)(1)(B)(iii) with respect to the portion of the plan year after such distribution is made. (B) Dollar limitation The aggregate amount of distributions from health flexible spending arrangements and health reimbursement arrangements of any employee which may be treated as qualified HSA distributions in connection with an establishment of coverage described in subparagraph (A)(i) shall not exceed the dollar amount in effect under section 125(i)(1) (twice such amount in the case of coverage which is described in section 223(b)(2)(B)). .\n##### (b) Partial reduction of limitation on deductible HSA contributions\nSection 223(b)(4) of such Code is amended by striking and at the end of subparagraph (B), by striking the period at the end of subparagraph (C) and inserting , and , and by inserting after subparagraph (C) the following new subparagraph:\n(D) so much of any qualified HSA distribution (as defined in section 106(e)(2)) made to a health savings account of such individual during the taxable year as does not exceed the aggregate increases in the balance of the arrangement from which such distribution is made which occur during the portion of the plan year which precedes such distribution (other than any balance carried over to such plan year and determined without regard to any decrease in such balance during such portion of the plan year). .\n##### (c) Conversion to HSA-Compatible arrangement for remainder of plan year\nSection 223(c)(1)(B)(iii) of such Code is amended to read as follows:\n(iii) coverage under a health flexible spending arrangement or health reimbursement arrangement for the portion of the plan year after a qualified HSA distribution (as defined in section 106(e)(2) determined without regard to subparagraph (A)(ii) thereof) is made, if the terms of such arrangement which apply for such portion of the plan year are such that, if such terms applied for the entire plan year, then such arrangement would not be taken into account under subparagraph (A)(ii) of this paragraph for such plan year. .\n##### (d) Inclusion of qualified HSA distributions on W\u20132\n**(1) In general**\nSection 6051(a) of such Code is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) the amount of any qualified HSA distribution (as defined in section 106(e)(2)) with respect to such employee. .\n**(2) Conforming amendment**\nSection 6051(a)(12) of such Code is amended by inserting (other than any qualified HSA distribution, as defined in section 106(e)(2)) before the comma at the end.\n##### (e) Effective date\nThe amendments made by this section shall apply to distributions made after December 31, 2025, in taxable years ending after such date.",
      "versionDate": "2025-04-07",
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
        "actionDate": "2025-12-09",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, Education and Workforce, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6512",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Putting Patients First Healthcare Freedom Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T17:31:08Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2667ih.xml"
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
      "title": "Flexible Savings Arrangements for a Healthy Robust America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flexible Savings Arrangements for a Healthy Robust America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow distributions from a health flexible spending arrangement or health reimbursement arrangement directly to a health savings account in connection with establishing coverage under a high deductible health plan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T04:48:23Z"
    }
  ]
}
```
