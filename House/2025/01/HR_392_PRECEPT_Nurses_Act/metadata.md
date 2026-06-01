# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/392
- Title: PRECEPT Nurses Act
- Congress: 119
- Bill type: HR
- Bill number: 392
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-05-20T08:08:17Z
- Update date including text: 2026-05-20T08:08:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/392",
    "number": "392",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "PRECEPT Nurses Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:17Z",
    "updateDateIncludingText": "2026-05-20T08:08:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:03:05Z",
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
      "sponsorshipDate": "2025-01-14",
      "state": "NY"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "OH"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "LA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "KS"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "VA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MO"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "MI"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "HI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NV"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MS"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "KS"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "DC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NE"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "IL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "VT"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr392ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 392\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mrs. Kiggans of Virginia (for herself, Ms. Tenney , Mr. Joyce of Ohio , and Mr. Costa ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to create a tax credit for nurse preceptors.\n#### 1. Short title\nThis Act may be cited as the Providing Real-world Education and Clinical Experience by Precepting Tomorrow\u2019s Nurses Act or the PRECEPT Nurses Act .\n#### 2. Credit for nurse preceptors\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Credit for nurse preceptors (a) In general In the case of any eligible nurse preceptor, there shall be allowed as a credit against the tax imposed by this chapter for any taxable year an amount equal to $2,000. (b) Definitions For purposes of this section, with respect to any taxable year\u2014 (1) Eligible nurse preceptor The term eligible nurse preceptor means an individual who serves not less than 200 hours during the taxable year as a nurse preceptor in a community which is designated as a health professional shortage area under section 332 of the Public Health Service Act. The Secretary shall publish on an annual basis on the website of the Internal Revenue Service a list of the areas which are so designated. (2) Nurse preceptor The term nurse preceptor means a licensed registered nurse or health care provider (as defined in section 3000(3) of the Public Health Service Act ( 42 U.S.C. 300jj(3) )) who provides supervision and personalized experiential learning, training, instruction, and mentoring opportunities in the clinical practice of nursing (as defined by the applicable State Board of Nursing, applicable state agency, or written agreement between the relevant academic institution and clinical site) to a student of nursing, student of advanced practice registered nursing, or newly hired licensed nurse. (3) Relevant academic institution The term relevant academic institution means a school of nursing (as defined in section 801(2) of the Public Health Service Act ( 42 U.S.C. 296(2) )) in which a student of nursing or student of advanced practice registered nursing is enrolled. (4) Newly hired The term newly hired means within the first 6 months of employment. (5) Minimum required hours of preceptorship The term minimum required hours of preceptorship means 200 hours of serving as a nurse preceptor. (c) Reporting requirement (1) In general No credit shall be allowed under subsection (a) unless the eligible nurse preceptor has received a certification indicating that the eligible nurse preceptor has completed the minimum required hours of preceptorship for the taxable year. (2) Contents of certification A certification under paragraph (1) shall include\u2014 (A) a certification from the relevant partnering academic institution stating the number of hours the preceptor served as a nurse preceptor to a student of nursing or student of advanced practice registered nursing during the taxable year, or (B) a certification from the clinical site at which the preceptor is employed stating the number of hours the preceptor served as a nurse preceptor to a newly hired nurse during the taxable year. (3) Multiple certifications A nurse preceptor may receive multiple certifications from multiple entities under paragraph (2) to establish the completion of the minimum required hours of preceptorship. (d) Termination This section shall not apply to any taxable year beginning after December 31, 2032. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Credit for nurse preceptors. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n##### (d) Report and evaluation\n**(1) In general**\nFor taxable years beginning in calendar year 2026, and each calendar year thereafter through 2032, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall report to the relevant committees of Congress for taxable years beginning in such calendar year on the credit under section 25F of the Internal Revenue Code of 1986, as added by this section. Such report shall include\u2014\n**(A)**\nthe number of taxpayers claiming such credit for taxable years beginning in such calendar year,\n**(B)**\nthe total hours served and other aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor (as defined in section 25F(b) of such Code, as so added),\n**(C)**\nthe geographic distribution of taxpayers claiming such credit for the taxable year, and\n**(D)**\nsuch other information as determined relevant by the Secretary (or the Secretary\u2019s delegate).\n**(2) Evaluation**\nNot later than June 30, 2033, the Secretary of the Treasury (or the Secretary\u2019s delegate), in consultation with the Administrator of the Health Resources and Services Administration, shall provide to the relevant committees of Congress an evaluation of the effectiveness of the credit under section 25F of the Internal Revenue Code of 1986, as added by this section, in increasing the number of nurse preceptors in the United States.\n**(3) Relevant committees of Congress**\nFor purposes of this subsection, the term relevant committees of Congress means\u2014\n**(A)**\nthe Committee on Finance of the Senate,\n**(B)**\nthe Committee on Ways and Means of the House of Representatives,\n**(C)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate,\n**(D)**\nthe Committee on Education and Workforce of the House of Representatives, and\n**(E)**\nthe Committee on Energy and Commerce of the House of Representatives.",
      "versionDate": "2025-01-14",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "131",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PRECEPT Nurses Act",
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
        "updateDate": "2025-02-26T14:16:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr392",
          "measure-number": "392",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr392v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Providing Real-world Education and Clinical Experience by Precepting Tomorrow's Nurses Act or the PRECEPT Nurses Act</strong></p><p>This bill establishes a new, nonrefundable tax credit for eligible nurse preceptors, subject to limitations. The bill also requires the Internal Revenue Service (IRS) to report to Congress certain information about the tax credit for nurse preceptors.</p><p>Under the bill, a nonrefundable tax credit of $2,000 is allowed for an eligible nurse preceptor through 2032. An <em>eligible nurse preceptor</em> is defined as an individual who provides at least 200 certified hours of supervision and personalized experiential learning, training, instruction, and mentoring in the clinical practice of nursing to a nursing student, advanced practice registered nursing student, or newly hired licensed nurse in a community designated as a health professional shortage area.\u00a0</p><p>The bill also requires the IRS to report to Congress</p><ul><li>the number of taxpayers that claim the tax credit for nurse preceptors each year and the geographic distribution of such taxpayers,</li><li>aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor, and</li><li>the effectiveness of the tax credit in increasing the number of nurse preceptors in the United States.</li></ul>"
        },
        "title": "PRECEPT Nurses Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr392.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Providing Real-world Education and Clinical Experience by Precepting Tomorrow's Nurses Act or the PRECEPT Nurses Act</strong></p><p>This bill establishes a new, nonrefundable tax credit for eligible nurse preceptors, subject to limitations. The bill also requires the Internal Revenue Service (IRS) to report to Congress certain information about the tax credit for nurse preceptors.</p><p>Under the bill, a nonrefundable tax credit of $2,000 is allowed for an eligible nurse preceptor through 2032. An <em>eligible nurse preceptor</em> is defined as an individual who provides at least 200 certified hours of supervision and personalized experiential learning, training, instruction, and mentoring in the clinical practice of nursing to a nursing student, advanced practice registered nursing student, or newly hired licensed nurse in a community designated as a health professional shortage area.\u00a0</p><p>The bill also requires the IRS to report to Congress</p><ul><li>the number of taxpayers that claim the tax credit for nurse preceptors each year and the geographic distribution of such taxpayers,</li><li>aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor, and</li><li>the effectiveness of the tax credit in increasing the number of nurse preceptors in the United States.</li></ul>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr392"
    },
    "title": "PRECEPT Nurses Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Providing Real-world Education and Clinical Experience by Precepting Tomorrow's Nurses Act or the PRECEPT Nurses Act</strong></p><p>This bill establishes a new, nonrefundable tax credit for eligible nurse preceptors, subject to limitations. The bill also requires the Internal Revenue Service (IRS) to report to Congress certain information about the tax credit for nurse preceptors.</p><p>Under the bill, a nonrefundable tax credit of $2,000 is allowed for an eligible nurse preceptor through 2032. An <em>eligible nurse preceptor</em> is defined as an individual who provides at least 200 certified hours of supervision and personalized experiential learning, training, instruction, and mentoring in the clinical practice of nursing to a nursing student, advanced practice registered nursing student, or newly hired licensed nurse in a community designated as a health professional shortage area.\u00a0</p><p>The bill also requires the IRS to report to Congress</p><ul><li>the number of taxpayers that claim the tax credit for nurse preceptors each year and the geographic distribution of such taxpayers,</li><li>aggregated and averaged data on the preceptorships served by taxpayers as an eligible nurse preceptor, and</li><li>the effectiveness of the tax credit in increasing the number of nurse preceptors in the United States.</li></ul>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr392"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr392ih.xml"
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
      "title": "PRECEPT Nurses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PRECEPT Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Real-world Education and Clinical Experience by Precepting Tomorrow\u2019s Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to create a tax credit for nurse preceptors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:22Z"
    }
  ]
}
```
