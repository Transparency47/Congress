# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4960?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4960
- Title: BENES 2.0 Act
- Congress: 119
- Bill type: HR
- Bill number: 4960
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2025-12-02T16:50:46Z
- Update date including text: 2025-12-02T16:50:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-12 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4960",
    "number": "4960",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "BENES 2.0 Act",
    "type": "HR",
    "updateDate": "2025-12-02T16:50:46Z",
    "updateDateIncludingText": "2025-12-02T16:50:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-12T13:01:45Z",
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
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4960ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4960\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Ruiz (for himself, Mr. Evans of Pennsylvania , Mr. Bilirakis , and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to establish a system to notify individuals approaching Medicare eligibility.\n#### 1. Short title\nThis Act may be cited as the Beneficiary Enrollment Notification and Eligibility Simplification 2.0 Act or the BENES 2.0 Act .\n#### 2. Beneficiary enrollment notification and eligibility simplification\n##### (a) Eligibility and enrollment notices\n**(1) As part of social security account statement for individuals attaining ages 60 to 65**\n**(A) In general**\nSection 1143(a) of the Social Security Act ( 42 U.S.C. 1320b\u201313(a) ) is amended by adding at the end the following new paragraph:\n(4) Medicare eligibility information (A) In general In the case of statements provided on or after the date that is 2 years after the date of the enactment of this paragraph to individuals who are attaining ages 60, 61, 62, 63, 64 and 65, the statement shall also include a notice containing the information described in subparagraph (B). (B) Contents of notice The notice required under subparagraph (A) shall include a clear, simple explanation of\u2014 (i) eligibility for benefits under the Medicare program under title XVIII, and in particular benefits under part B of such title; (ii) the reasons a late enrollment penalty for failure to timely enroll could be assessed and how such late enrollment penalty is calculated, in particular for benefits under such part B; (iii) the availability of relief from such late enrollment penalty and retroactive enrollment under section 1837(h) (including as such section is applied under sections 1818(c) and 1818A(c)(3)), with examples of circumstances under which such relief may be granted and examples of circumstances under which such relief would not be granted; (iv) coordination of benefits (including primary and secondary coverage scenarios) pursuant to section 1862(b), in particular for benefits under such part B; (v) enrollment, eligibility, and coordination of benefits under title XVIII with respect to populations, for whom there are special considerations, such as residents of Puerto Rico and veterans; and (vi) online resources and toll-free telephone numbers of the Social Security Administration and the Centers for Medicare & Medicaid Services (including 1\u2013800\u2013MEDICARE and the national toll-free number of the Social Security Administration) that provide information on eligibility for benefits under the Medicare program under title XVIII. (C) Development of notice (i) In general The Secretary, in coordination with the Commissioner of Social Security, and taking into consideration information collected pursuant to clause (ii), shall, not later than 12 months after the last day of the period for the request of information described in clause (ii), develop the notice to be provided pursuant to subparagraph (A). (ii) Request for information Not later than 6 months after the date of the enactment of this paragraph, the Secretary shall request written information, including recommendations, from stakeholders (including the groups described in subparagraph (D)) on the information to be included in the notice. (iii) Notice improvement Beginning 4 years after the date of the enactment of this paragraph, and not less than once every 2 years thereafter, the Secretary, in coordination with the Commissioner of Social Security, shall\u2014 (I) review the content of the notice to be provided under subparagraph (A); (II) request written information, including recommendations, on such notice through a request for information process as described in clause (ii); and (III) update and revise such notice as the Secretary deems appropriate. (D) Groups For purposes of subparagraph (C)(ii), the groups described in this subparagraph include the following: (i) Individuals who are 60 years of age or older. (ii) Veterans. (iii) Individuals with disabilities. (iv) Individuals with end stage renal disease. (v) Low-income individuals and families. (vi) Employers (including human resources professionals). (vii) States (including representatives of State-run Health Insurance Exchanges, Medicaid offices, and Departments of Insurance). (viii) State Health Insurance Assistance Programs. (ix) Health insurers. (x) Health insurance agents and brokers. (xi) Such other groups as specified by the Secretary. (E) Posting of notice on websites The Commissioner of Social Security and the Secretary shall post the notice required under subparagraph (A) on the public internet website of the Social Security Administration and on Medicare.gov (or a successor website), respectively. (F) No effect on obligation to mail statements Nothing in this paragraph shall be construed to relieve the Commissioner of Social Security from any requirement under subsection (c), including the requirement to mail a statement on an annual basis to each eligible individual who is not receiving benefits under title II and for whom a mailing address can be determined through such methods as the Commissioner determines to be appropriate. .\n**(B) Timing of statements**\nSection 1143(c)(2) of the Social Security Act ( 42 U.S.C. 1320b\u201313(c)(2) ) is amended by adding at the end the following new sentence: With respect to statements provided to individuals who are attaining age 65, as described in subsection (a)(4), such statements shall be mailed not earlier than 6 months and not later than 3 months before the individual attains such age. .\n**(2) Social security beneficiaries**\nTitle XI of the Social Security Act ( 42 U.S.C. 1301 et seq. ) is amended by inserting after section 1144 the following new section:\n1144A. Medicare enrollment notification and eligibility notices for Social Security beneficiaries prior to medicare eligibility (a) Notices (1) In general The Commissioner of Social Security shall distribute the notice to be provided pursuant to section 1143(a)(4), as may be modified under paragraph (2), to individuals entitled to monthly insurance benefits under title II in accordance with subsection (b). (2) Authority to modify notice The Secretary, in coordination with the Commissioner of Social Security, may modify the notice to be distributed under paragraph (1) as necessary to take into account the individuals described in such paragraph. (3) Posting of notice on websites The Commissioner of Social Security and the Secretary shall post the notice required to be distributed under paragraph (1) on the public internet website of the Social Security Administration and on Medicare.gov (or a successor website), respectively. (b) Timing Beginning not later than 2 years after the date of the enactment of this section, a notice required under subsection (a)(1) shall be mailed to an individual described in such subsection\u2014 (1) in the third month before the date on which such individual\u2019s initial enrollment period begins as provided under section 1837; and (2) in the case of an individual with respect to whom section 226(b) applies (except for an individual who will attain age 65 during the 24 month period described in such section), in the month before such date on which such individual\u2019s initial enrollment period so begins. .",
      "versionDate": "2025-08-12",
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
        "name": "Health",
        "updateDate": "2025-09-19T14:18:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-12",
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
          "measure-id": "id119hr4960",
          "measure-number": "4960",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-12",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4960v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-08-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Beneficiary Enrollment Notification and Eligibility Simplification 2.0 Act or the BENES 2.0 Act</b></p> <p>This bill requires Social Security account statements for individuals attaining ages 60 to 65 to include information about Medicare eligibility, late enrollment penalties, benefit coordination, and related resources. </p> <p>Statements with the required information must be mailed to individuals at least three months before they turn 65; the required information must also be mailed to those who are age 65 or over and are entitled to Social Security benefits three months before their initial Medicare enrollment period begins.</p>"
        },
        "title": "BENES 2.0 Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4960.xml",
    "summary": {
      "actionDate": "2025-08-12",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Beneficiary Enrollment Notification and Eligibility Simplification 2.0 Act or the BENES 2.0 Act</b></p> <p>This bill requires Social Security account statements for individuals attaining ages 60 to 65 to include information about Medicare eligibility, late enrollment penalties, benefit coordination, and related resources. </p> <p>Statements with the required information must be mailed to individuals at least three months before they turn 65; the required information must also be mailed to those who are age 65 or over and are entitled to Social Security benefits three months before their initial Medicare enrollment period begins.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4960"
    },
    "title": "BENES 2.0 Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-12",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Beneficiary Enrollment Notification and Eligibility Simplification 2.0 Act or the BENES 2.0 Act</b></p> <p>This bill requires Social Security account statements for individuals attaining ages 60 to 65 to include information about Medicare eligibility, late enrollment penalties, benefit coordination, and related resources. </p> <p>Statements with the required information must be mailed to individuals at least three months before they turn 65; the required information must also be mailed to those who are age 65 or over and are entitled to Social Security benefits three months before their initial Medicare enrollment period begins.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4960"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4960ih.xml"
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
      "title": "BENES 2.0 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BENES 2.0 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Beneficiary Enrollment Notification and Eligibility Simplification 2.0 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish a system to notify individuals approaching Medicare eligibility.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:18Z"
    }
  ]
}
```
