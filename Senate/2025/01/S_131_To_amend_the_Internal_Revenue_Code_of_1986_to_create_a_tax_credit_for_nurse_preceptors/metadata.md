# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/131?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/131
- Title: PRECEPT Nurses Act
- Congress: 119
- Bill type: S
- Bill number: 131
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-05T22:06:54Z
- Update date including text: 2025-12-05T22:06:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/131",
    "number": "131",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "PRECEPT Nurses Act",
    "type": "S",
    "updateDate": "2025-12-05T22:06:54Z",
    "updateDateIncludingText": "2025-12-05T22:06:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T20:34:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "DE"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s131is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 131\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Kelly (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to create a tax credit for nurse preceptors.\n#### 1. Short title\nThis Act may be cited as the Providing Real-World Education and Clinical Experience by Precepting Tomorrow\u2019s Nurses Act or the PRECEPT Nurses Act .\n#### 2. Credit for nurse preceptors\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Credit for nurse preceptors (a) In general In the case of any eligible nurse preceptor, there shall be allowed as a credit against the tax imposed by this chapter for any taxable year an amount equal to $2,000. (b) Definitions For purposes of this section, with respect to any taxable year\u2014 (1) Eligible nurse preceptor The term eligible nurse preceptor means an individual who serves not less than 200 hours during the taxable year as a nurse preceptor in a community which is designated as a health professional shortage area under section 332 of the Public Health Service Act. The Secretary shall publish on an annual basis on the website of the Internal Revenue Service a list of the areas which are so designated. (2) Nurse preceptor The term nurse preceptor means a licensed registered nurse or health care provider (as defined in section 3000(3) of the Public Health Service Act ( 42 U.S.C. 300jj(3) )) who provides supervision and personalized experiential learning, training, instruction, and mentoring opportunities in the clinical practice of nursing (as defined by the applicable State Board of Nursing, applicable state agency, or written agreement between the relevant academic institution and clinical site) to a student of nursing, student of advanced practice registered nursing, or newly hired licensed nurse. (3) Relevant academic institution The term relevant academic institution means a school of nursing (as defined in section 801(2) of the Public Health Service Act ( 42 U.S.C. 296(2) )) in which a student of nursing or student of advanced practice registered nursing is enrolled. (4) Newly hired The term newly hired means within the first 6 months of employment. (5) Minimum required hours of preceptorship The term minimum required hours of preceptorship means 200 hours of serving as a nurse preceptor. (c) Reporting requirement (1) In general No credit shall be allowed under subsection (a) unless the eligible nurse preceptor has received a certification indicating that the eligible nurse preceptor has completed the minimum required hours of preceptorship for the taxable year. (2) Contents of certification A certification under paragraph (1) shall include\u2014 (A) a certification from the relevant partnering academic institution stating the number of hours the preceptor served as a nurse preceptor to a student of nursing or student of advanced practice registered nursing during the taxable year, or (B) a certification from the clinical site at which the preceptor is employed stating the number of hours the preceptor served as a nurse preceptor to a newly hired nurse during the taxable year. (3) Multiple certifications A nurse preceptor may receive multiple certifications from multiple entities under paragraph (2) to establish the completion of the minimum required hours of preceptorship. (d) Termination This section shall not apply to any taxable year beginning after December 31, 2032. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Credit for nurse preceptors. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n##### (d) Report and evaluation\n**(1) In general**\nBeginning with taxable year 2026 and ending with taxable year 2032, the Secretary of the Treasury (or such Secretary's delegate) shall report to the relevant committees of Congress for each taxable year on the credit under section 25F of the Internal Revenue Code of 1986, as added by this section. Such report shall include\u2014\n**(A)**\nthe number of taxpayers claiming such credit for the taxable year, and\n**(B)**\nthe total hours served and other aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor (as defined in section 25F(b) of such Code, as so added),\n**(C)**\nthe geographic distribution of taxpayers claiming such credit for the taxable year, and\n**(D)**\nsuch other information as determined relevant by the Secretary (or the Secretary's delegate).\n**(2) Evaluation**\nNot later than June 30, 2033, the Secretary of the Treasury (or the Secretary's delegate), in consultation with the Administrator of the Health Resources and Services Administration, shall provide to the relevant committees of Congress an evaluation of the effectiveness of the credit under section 25F of the Internal Revenue Code of 1986, as added by this section, in increasing the number of nurse preceptors in the United States.\n**(3) Relevant committees of Congress**\nFor purposes of this subsection, the term relevant committees of Congress means\u2014\n**(A)**\nthe Committee on Finance of the Senate,\n**(B)**\nthe Committee on Ways and Means of the House of Representatives,\n**(C)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate,\n**(D)**\nthe Committee on Education and Workforce of the House of Representatives, and\n**(E)**\nthe Committee on Energy and Commerce of the House of Representatives.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-14",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "392",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PRECEPT Nurses Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Government trust funds",
            "updateDate": "2025-07-02T13:12:27Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2025-07-02T13:12:19Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-07-02T13:12:46Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-07-02T13:12:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-26T15:30:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s131",
          "measure-number": "131",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s131v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Providing Real-World Education and Clinical Experience by Precepting Tomorrow's Nurses Act or the PRECEPT Nurses Act</strong></p><p>This bill establishes a new, nonrefundable tax credit for eligible nurse preceptors, subject to limitations. The bill also requires the Internal Revenue Service (IRS) to report to Congress certain information about the tax credit for nurse preceptors.</p><p>Under the bill, a nonrefundable tax credit of $2,000 is allowed for an eligible nurse preceptor through 2032. An <em>eligible nurse preceptor</em> is defined as an individual who provides at least 200 certified hours of supervision and personalized experiential learning, training, instruction, and mentoring in the clinical practice of nursing to a nursing student, advanced practice registered nursing student, or newly hired licensed nurse in a community designated as a health professional shortage area.\u00a0</p><p>The bill also requires the IRS to report to Congress</p><ul><li>the number of taxpayers that claim the tax credit for nurse preceptors each year and the geographic distribution of such taxpayers,</li><li>aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor, and</li><li>the effectiveness of the tax credit in increasing the number of nurse preceptors in the United States.</li></ul>"
        },
        "title": "PRECEPT Nurses Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s131.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Providing Real-World Education and Clinical Experience by Precepting Tomorrow's Nurses Act or the PRECEPT Nurses Act</strong></p><p>This bill establishes a new, nonrefundable tax credit for eligible nurse preceptors, subject to limitations. The bill also requires the Internal Revenue Service (IRS) to report to Congress certain information about the tax credit for nurse preceptors.</p><p>Under the bill, a nonrefundable tax credit of $2,000 is allowed for an eligible nurse preceptor through 2032. An <em>eligible nurse preceptor</em> is defined as an individual who provides at least 200 certified hours of supervision and personalized experiential learning, training, instruction, and mentoring in the clinical practice of nursing to a nursing student, advanced practice registered nursing student, or newly hired licensed nurse in a community designated as a health professional shortage area.\u00a0</p><p>The bill also requires the IRS to report to Congress</p><ul><li>the number of taxpayers that claim the tax credit for nurse preceptors each year and the geographic distribution of such taxpayers,</li><li>aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor, and</li><li>the effectiveness of the tax credit in increasing the number of nurse preceptors in the United States.</li></ul>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s131"
    },
    "title": "PRECEPT Nurses Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Providing Real-World Education and Clinical Experience by Precepting Tomorrow's Nurses Act or the PRECEPT Nurses Act</strong></p><p>This bill establishes a new, nonrefundable tax credit for eligible nurse preceptors, subject to limitations. The bill also requires the Internal Revenue Service (IRS) to report to Congress certain information about the tax credit for nurse preceptors.</p><p>Under the bill, a nonrefundable tax credit of $2,000 is allowed for an eligible nurse preceptor through 2032. An <em>eligible nurse preceptor</em> is defined as an individual who provides at least 200 certified hours of supervision and personalized experiential learning, training, instruction, and mentoring in the clinical practice of nursing to a nursing student, advanced practice registered nursing student, or newly hired licensed nurse in a community designated as a health professional shortage area.\u00a0</p><p>The bill also requires the IRS to report to Congress</p><ul><li>the number of taxpayers that claim the tax credit for nurse preceptors each year and the geographic distribution of such taxpayers,</li><li>aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor, and</li><li>the effectiveness of the tax credit in increasing the number of nurse preceptors in the United States.</li></ul>",
      "updateDate": "2025-04-24",
      "versionCode": "id119s131"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s131is.xml"
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
      "title": "PRECEPT Nurses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRECEPT Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Real-World Education and Clinical Experience by Precepting Tomorrow\u2019s Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to create a tax credit for nurse preceptors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:20Z"
    }
  ]
}
```
