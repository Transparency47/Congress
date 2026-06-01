# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6458
- Title: Electronic Filing Improvement and Logistical Efficiency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6458
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:06:57Z
- Update date including text: 2026-05-16T08:06:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6458",
    "number": "6458",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Electronic Filing Improvement and Logistical Efficiency Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:06:57Z",
    "updateDateIncludingText": "2026-05-16T08:06:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:05:00Z",
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6458ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6458\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. Malliotakis (for herself, Mr. Morelle , and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to improve the electronic filing process for employment taxes.\n#### 1. Short title\nThis Act may be cited as the Electronic Filing Improvement and Logistical Efficiency Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nbusinesses and their third-party representatives should be able to file all employment tax forms and schedules, including amended returns, electronically;\n**(2)**\nthe current prevalence and reliance on paper by both the Internal Revenue Service and private sector businesses for quarterly and annual employment tax return filings is not sustainable and must be addressed immediately;\n**(3)**\nthe obstacles to electronic filing are both structural and behavioral; and\n**(4)**\nthe Internal Revenue Service must streamline the process for filing employment returns electronically, making it as easy and efficient as possible, while the internal revenue laws must incentivize the use of electronic filing to help rapidly overcome longstanding taxpayer behaviors.\n#### 3. Electronic filing for employment tax returns\nNot later than 1 year after the date of the enactment of this Act, the Internal Revenue Service shall\u2014\n**(1)**\nmake available to employers fully-automated electronic process for satisfying all filing and payment requirements (including amended returns) for taxes imposed under subtitle C of the Internal Revenue Code,\n**(2)**\nfirst focus on making available pursuant to paragraph (1) the adjusted employer\u2019s quarterly Federal tax return or claim for refund (Form 941\u2013X), and\n**(3)**\nmake all necessary technical and business changes to the electronic filing process to ensure that the process is fully automated on the front- and back-end and that electronic filing is the most convenient and efficient means of meeting such filing and payment requirements.\n#### 4. Electronic filing tax credit for employers\n##### (a) In general\nSubchapter D of chapter 21 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n3135. Electronic filing credit for employers (a) In general In the case of any employer required to make a quarterly return of the taxes imposed by subtitle C, there shall be allowed as a credit against applicable employment taxes with respect to such employer an amount equal to\u2014 (1) $1,000 for the calendar quarter for which the return and payment of such taxes are for the first time all made electronically, and (2) in the year following the year in which a credit is first determined for a calendar quarter under paragraph (1), $1,000 for 1 such calendar quarter elected by the employer in such year for which the return and payment of such taxes are all made electronically. (b) Credit limited to employment taxes; carry forward (1) Limit The credit allowed by subsection (a) with respect to any calendar quarter shall not exceed the applicable employment taxes for such calendar quarter on the wages paid with respect to the employment of all employees of the employer. (2) Carryforward If the amount of the credit under subsection (a) exceeds the limitation of paragraph (1) for any calendar quarter, such excess shall be treated as a credit allowed under subsection (a) against the applicable employment taxes for the following calendar quarter. (c) Definition and special rules (1) Recapture (A) In general In the case of an employer allowed a credit under subsection (a) against an applicable employment tax for any calendar quarter, if the employer for any subsequent calendar quarter fails to make the return and payment of applicable employment taxes electronically, such tax shall for such subsequent calendar quarter be increased by the amount of such credit so allowed. (B) No credit following recapture In the case of an employer with respect to which subparagraph (A) applies for any quarter, no credit shall be allowed under subsection (a) for any subsequent quarter. (2) Exception for extraordinary circumstances (A) Extraordinary circumstances A taxpayer shall not be treated as failing to make the return and payment of applicable employment taxes electronically for purposes of paragraph (1) under such circumstances as the Secretary may by exception provide, including an employer\u2019s lack of ready access to broadband or convenient online services due to rural or other geographic barriers or emergency situations where electronic filing and payment would cause undue hardship. (B) Deemed compliance for certain bulk filers For purposes of this section, in the case of a third party provider, including a payroll service provider, who for the 1-year period preceding the filing of any return to which paragraph (1)(A) would apply (without regard to this subparagraph) filed electronically at least 99 percent of all returns described in subsection (a) that were made by the provider during such period, no credit shall be recaptured under paragraph (1)(A) by reason of such return. (d) Applicable employment taxes For purposes of this section, the term applicable employment taxes means the following: (1) The taxes imposed by subsections (a) and (b) of section 3111. (2) So much of the taxes imposed by section 3221 as are attributable to the rates in effect under subsections (a) and (b) of section 3111. (e) Special rules (1) Aggregation rule All persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (m) or (o) of section 414, shall be treated as one employer for purposes of this section. (2) Governmental entities No credit shall be allowed under this section to the Government of the United States, the government of any State or political subdivision thereof, or to any agency or instrumentality of any of the foregoing. The preceding sentence shall not apply to any organization described in section 501(c)(1) and exempt from tax under section 501(a). .\n##### (b) Clerical amendment\nThe table of sections for subchapter D of chapter 21 of such Code is amended by adding at the end the following new item:\nSec. 3135. Electronic filing credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to calendar quarters beginning after the date of the enactment of this Act.\n#### 5. User fee for paper filing of employment taxes\n##### (a) In general\nChapter 25 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n3513. User fees (a) In general The Secretary shall impose a user fee of $250 on each submission other than by electronic means of any quarterly or annual return required with respect to the collection of the tax imposed by chapter 21 or 23A. (b) Special rules For purpose of this section\u2014 (1) Exception The Secretary shall establish procedures for granting exceptions to the fee imposed by subsection (a) where electronic filing is not feasible, including for under any of the following circumstances: (A) Any employer not required to make a quarterly return of the taxes imposed by subtitle C. (B) First and second-time submissions filed other than by electronic means shall have the user fee waived, with a written notification sent to the employer outlining the electronic submission requirement. (C) Employers who do not have ready access to broadband or convenient online services due to rural or other geographic barriers. (D) Certain emergency situations where electronic filing and payment would cause undue hardship. (E) Recent victims of identity theft or cybercrimes where submissions other than by electronic means might be necessary or desirable. (F) Such other circumstances as may be provided by the Secretary in regulations or other guidance. Any person qualifying for an exception under this section or other applicable law shall be provided alternative submission options such as a paper filing. (2) Certain bulk filers In the case of a third party provider, including a payroll service provider, who for the 1-year period preceding the filing of any return to which subsection (a) applies filed electronically at least 99 percent of all returns described in subsection (a) that were made by the provider during such period, no user fee shall be imposed with respect to such return under subsection (a). .\n##### (b) Clerical amendment\nThe table of sections for chapter 25 of such Code is amended by adding at the end the following new item:\nSec. 3135. User fees. .\n##### (c) Effective date\nThe amendments made by this section shall apply to returns required to be made for periods ending later than 2 years after the date of the enactment of this Act.",
      "versionDate": "2025-12-04",
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
        "updateDate": "2026-01-06T16:01:07Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6458ih.xml"
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
      "title": "Electronic Filing Improvement and Logistical Efficiency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Electronic Filing Improvement and Logistical Efficiency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to improve the electronic filing process for employment taxes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:48:20Z"
    }
  ]
}
```
