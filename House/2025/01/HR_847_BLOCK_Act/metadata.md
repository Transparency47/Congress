# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/847?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/847
- Title: BLOCK Act
- Congress: 119
- Bill type: HR
- Bill number: 847
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/847",
    "number": "847",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "BLOCK Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:00:40Z",
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
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr847ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 847\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Burchett introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo repeal certain formula grants under the Elementary and Secondary Education Act of 1965 and use such funds to award block grants to States, except as otherwise appropriated by Congress.\n#### 1. Short title\nThis Act may be cited as the Building Lasting Opportunities for Community K\u201312 Act or the BLOCK Act .\n#### 2. Block grants to States\nBeginning with fiscal year 2026, and each succeeding fiscal year thereafter, the Secretary of Education shall award block grants to each State in an amount that the State received under the provisions listed in section 3 for fiscal year 2025, except as otherwise appropriated by Congress.\n#### 3. Repeal of certain formula grants under the Elementary and Secondary Education Act of 1965\nOn October 1, 2025, the following provisions of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6301 et seq. ) shall be repealed:\n**(1)**\nGrants to local educational agencies under part A of title I ( 20 U.S.C. 6311 et seq. ).\n**(2)**\nState Assessment Grants under part B of title I ( 20 U.S.C. 6361 et seq. ).\n**(3)**\nMigrant Education under part C of title I ( 20 U.S.C. 6391 et seq. ).\n**(4)**\nNeglected and Delinquent under part D of title I ( 20 U.S.C. 6421 et seq. ).\n**(5)**\nSupporting Effective Instruction State Grants under part A of title II ( 20 U.S.C. 6611 et seq. ).\n**(6)**\nEnglish Language Acquisition under part A of title III ( 20 U.S.C. 6811 et seq. ).\n**(7)**\nStudent Support and Academic Enrichment Grants under part A of title IV ( 20 U.S.C. 7111 et seq. ).\n**(8)**\nThe 21st Century Community Learning Centers under part B of title IV ( 20 U.S.C. 7171 et seq. ).\n**(9)**\nRural Education under part B of title V ( 20 U.S.C. 7341 et seq. ).\n**(10)**\nIndian Education Formula Grants to Local Educational Agencies under subpart 1 of part A of title VI ( 20 U.S.C. 7421 et seq. ).\n#### 4. Definition of State\nIn this Act, the term State means the 50 States, the District of Columbia, and Puerto Rico.",
      "versionDate": "2025-01-31",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Academic performance and assessments",
            "updateDate": "2025-04-07T14:37:21Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-04-07T14:37:35Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2025-04-07T14:37:29Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-07T14:36:51Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-04-07T14:36:44Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-04-07T14:37:42Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-04-07T14:37:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-03T20:10:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr847",
          "measure-number": "847",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr847v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Building Lasting Opportunities for Community K\u201312 Act or the BLOCK Act</strong></p><p>This bill repeals on October 1, 2025, specified formula grants for programs\u00a0administered by the Department of Education (ED). Beginning with FY2026, ED must instead provide\u00a0block grants for these programs to each state based on amounts received in FY2025.</p><p>Specifically, the bill repeals the following allocation formulas for programs under the Elementary and Secondary Education Act of 1965:</p><ul><li>the Education for the Disadvantaged program (which includes Basic Grants, Concentration Grants, Targeted Grants, and Education Finance Incentive Grants);</li><li>State Assessment Grants;</li><li>the Migrant Education Program;</li><li>Prevention and Intervention Programs for Children and Youth Who Are Neglected, Delinquent, or At-Risk;</li><li>Supporting Effective Instruction State Grants;\u00a0</li><li>English Language Acquisition State Grants;</li><li>Student Support and Academic Enrichment Grants;</li><li>the 21st Century Community Learning Centers program;</li><li>the Rural Education Achievement Program (which includes both the Small, Rural School Achievement Program and the Rural and Low-Income School Program); and</li><li>Indian Education Formula Grants.</li></ul>"
        },
        "title": "BLOCK Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr847.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Building Lasting Opportunities for Community K\u201312 Act or the BLOCK Act</strong></p><p>This bill repeals on October 1, 2025, specified formula grants for programs\u00a0administered by the Department of Education (ED). Beginning with FY2026, ED must instead provide\u00a0block grants for these programs to each state based on amounts received in FY2025.</p><p>Specifically, the bill repeals the following allocation formulas for programs under the Elementary and Secondary Education Act of 1965:</p><ul><li>the Education for the Disadvantaged program (which includes Basic Grants, Concentration Grants, Targeted Grants, and Education Finance Incentive Grants);</li><li>State Assessment Grants;</li><li>the Migrant Education Program;</li><li>Prevention and Intervention Programs for Children and Youth Who Are Neglected, Delinquent, or At-Risk;</li><li>Supporting Effective Instruction State Grants;\u00a0</li><li>English Language Acquisition State Grants;</li><li>Student Support and Academic Enrichment Grants;</li><li>the 21st Century Community Learning Centers program;</li><li>the Rural Education Achievement Program (which includes both the Small, Rural School Achievement Program and the Rural and Low-Income School Program); and</li><li>Indian Education Formula Grants.</li></ul>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr847"
    },
    "title": "BLOCK Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Building Lasting Opportunities for Community K\u201312 Act or the BLOCK Act</strong></p><p>This bill repeals on October 1, 2025, specified formula grants for programs\u00a0administered by the Department of Education (ED). Beginning with FY2026, ED must instead provide\u00a0block grants for these programs to each state based on amounts received in FY2025.</p><p>Specifically, the bill repeals the following allocation formulas for programs under the Elementary and Secondary Education Act of 1965:</p><ul><li>the Education for the Disadvantaged program (which includes Basic Grants, Concentration Grants, Targeted Grants, and Education Finance Incentive Grants);</li><li>State Assessment Grants;</li><li>the Migrant Education Program;</li><li>Prevention and Intervention Programs for Children and Youth Who Are Neglected, Delinquent, or At-Risk;</li><li>Supporting Effective Instruction State Grants;\u00a0</li><li>English Language Acquisition State Grants;</li><li>Student Support and Academic Enrichment Grants;</li><li>the 21st Century Community Learning Centers program;</li><li>the Rural Education Achievement Program (which includes both the Small, Rural School Achievement Program and the Rural and Low-Income School Program); and</li><li>Indian Education Formula Grants.</li></ul>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr847"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr847ih.xml"
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
      "title": "BLOCK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BLOCK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Building Lasting Opportunities for Community K\u201312 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal certain formula grants under the Elementary and Secondary Education Act of 1965 and use such funds to award block grants to States, except as otherwise appropriated by Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:32Z"
    }
  ]
}
```
