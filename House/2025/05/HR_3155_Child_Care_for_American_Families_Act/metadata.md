# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3155?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3155
- Title: Child Care for American Families Act
- Congress: 119
- Bill type: HR
- Bill number: 3155
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-06-04T14:26:13Z
- Update date including text: 2025-06-04T14:26:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3155",
    "number": "3155",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Child Care for American Families Act",
    "type": "HR",
    "updateDate": "2025-06-04T14:26:13Z",
    "updateDateIncludingText": "2025-06-04T14:26:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:05:10Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3155ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3155\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Kustoff (for himself and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to enhance the employer-provided child care credit.\n#### 1. Short title\nThis Act may be cited as the Child Care for American Families Act .\n#### 2. Increase in employer-provided child care credit amount\n##### (a) In general\nSection 45F(a)(1) of the Internal Revenue Code of 1986 is amended by striking 25 percent and inserting the applicable percentage .\n##### (b) Applicable percentage\nSection 45F(a) of such Code, as amended by subsection (a), is amended\u2014\n**(1)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and by moving the margins of such subparagraphs 2 ems to the right,\n**(2)**\nby striking For purposes and inserting the following:\n(1) Credit allowed For purposes , and\n**(3)**\nby adding at the end the following new paragraph:\n(2) Applicable percentage (A) In general For purposes of paragraph (1)(A), the applicable percentage is\u2014 (i) except as otherwise provided in this paragraph, 40 percent, (ii) in the case of any qualified child care expenditures of an eligible small business, 50 percent, and (iii) in the case of any qualified child care expenditures paid or incurred in connection with a qualified child care facility located in an eligible area, 60 percent. (B) Eligible small business For purposes of subparagraph (A), the term eligible small business means, with respect to any taxable year, any taxpayer if the annual average number of employees employed by such person during either of the 2 preceding taxable years was 500 or fewer. For purposes of the preceding sentence, a preceding taxable year may be taken into account only if the taxpayer was in existence throughout the year. (C) Eligible area (i) In general For purposes of subparagraph (A), the term eligible area means\u2014 (I) a census tract described in section 45D(e), or (II) a rural county. (ii) Rural county (I) In general For purposes of this subparagraph, the term rural county means a county in which greater than 50 percent of the population of such county resides in census blocks that are designated as rural blocks (as determined by the Bureau of the Census according to the most recent decennial census). (II) Designation where no county For purposes of subclause (I), a rule similar to the rule of section 143(k)(2)(D) shall apply. .\n##### (c) Dollar limitation\nSection 45F(b) of such Code is amended to read as follows:\n(b) Dollar limitation (1) Aggregate limitation The credit allowable under subsection (a) for any taxable year shall not exceed $1,200,000. (2) Limitation with respect to qualified child care expenditures The aggregate amount of qualified child care expenditures which may be taken into account under this section for any taxable year shall not exceed $2,000,000. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 3. Guidance regarding multi-employer facilities\nSection 45F of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(g) Guidance The Secretary shall issue such guidance as may be necessary to carry out the purposes of this section, including guidance on the application of this section to multi-employer facilities. .\n#### 4. Dissemination of information\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall establish a public awareness program to inform taxpayers about\u2014\n**(1)**\nthe availability of the credit for employer-provided child care under section 45F of the Internal Revenue Code of 1986, and\n**(2)**\nfiling procedures for such credit.\n##### (b) Method\nIn carrying out this section, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall use appropriate means of communication to ensure awareness by all taxpayers who are eligible for the credit allowed under section 45F of the Internal Revenue Code of 1986.\n#### 5. GAO study on regulatory barriers affecting employer-provided child care\n##### (a) In general\nNot later than 12 months after the date of enactment of this Act, the Comptroller General of the United States shall submit to the applicable Congressional committees a report examining\u2014\n**(1)**\nState and local licensure and regulatory requirements affecting child care facilities;\n**(2)**\ncompliance costs and operational barriers for child care providers, particularly with respect to providers operating in multiple States; and\n**(3)**\nopportunities to reduce regulatory burdens while maintaining safety and quality standards, including how such improvements could enhance employer participation under section 45F of the Internal Revenue Code of 1986.\n##### (b) Recommendations\nThe report described in subsection (a) shall include recommendations for\u2014\n**(1)**\nupdating, expanding, or otherwise strengthening regulations affecting child care facilities;\n**(2)**\nenhancing uniformity across State regulatory frameworks to facilitate greater employer participation in providing high-quality child care;\n**(3)**\nreducing barriers for multi-employer facilities seeking to make use of the credit provided under section 45F of the Internal Revenue Code of 1986; and\n**(4)**\nreducing barriers for multi-state operators seeking to qualify for the credit provided under section 45F of the Internal Revenue Code of 1986.\n##### (c) Applicable Congressional committees\nFor purposes of this section, the term applicable Congressional committees means\u2014\n**(1)**\nthe Committees on Finance and Health, Education, Labor, and Pensions of the Senate; and\n**(2)**\nthe Committees on Ways and Means and Education and the Workforce of the House of Representatives.",
      "versionDate": "2025-05-01",
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
        "updateDate": "2025-06-04T14:26:13Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3155ih.xml"
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
      "title": "Child Care for American Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T09:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Care for American Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to enhance the employer-provided child care credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T09:03:55Z"
    }
  ]
}
```
