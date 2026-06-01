# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3521?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3521
- Title: Clinical Trial Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 3521
- Origin chamber: House
- Introduced date: 2025-05-20
- Update date: 2026-05-21T19:45:36Z
- Update date including text: 2026-05-21T19:45:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-20: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-20: Introduced in House

## Actions

- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3521",
    "number": "3521",
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
    "title": "Clinical Trial Modernization Act",
    "type": "HR",
    "updateDate": "2026-05-21T19:45:36Z",
    "updateDateIncludingText": "2026-05-21T19:45:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-20",
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
          "date": "2025-05-20T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-20T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "AZ"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "TN"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3521ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3521\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2025 Mr. Ruiz (for himself and Mr. Pfluger ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo modernize clinical trials and remove barriers for participation in clinical trials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clinical Trial Modernization Act .\n#### 2. Definition\nFor purposes of this Act, the term underrepresented population has the meaning given such term by the National Institutes of Health for purposes of the Toolkit for Patient-Focused Therapy Development (as published on April 1, 2024), in addition to such populations recognized by the Food and Drug Administration.\n#### 3. Grants to encourage clinical trial enrollment by underrepresented populations\n##### (a) In general\nThe Secretary may issue grants to and enter into contracts with entities to support community education, outreach, and recruitment activities for clinical trials with respect to devices and drugs, including vaccines, for diseases or conditions that have a disproportionate impact on underrepresented populations. Such activities may include\u2014\n**(1)**\nworking with community clinical trial sites, including community health centers, academic health centers, sites in rural communities, and other facilities;\n**(2)**\ntraining health care personnel, including potential clinical trial investigators, with a focus on significantly increasing the number of underrepresented populations of health care personnel who are clinical trial investigators at the community sites for ongoing clinical trials;\n**(3)**\nengaging community stakeholders to encourage participation in clinical trials, especially in underrepresented populations; and\n**(4)**\nfostering partnerships with community-based organizations serving underrepresented populations, including employee unions and frontline health care workers.\n##### (b) Priority for grant and contract awards\nIn awarding grants and contracts under this section, the Secretary shall prioritize entities that\u2014\n**(1)**\ndevelop educational, recruitment, and training materials in multiple languages; or\n**(2)**\nundertake clinical trial outreach efforts in communities that are traditionally underrepresented in clinical trials, such as tribal areas.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated for fiscal years 2025 and 2026 such sums as may be necessary to carry out this section.\n#### 4. Encouragement of clinical trial participation by underrepresented populations through payment of study participant clinical trial expenses and provision of digital health technologies\n##### (a) In general\nSection 1128A(i)(6)(F) of the Social Security Act (42 U.S.C. 1320a\u20137a(i)(6)(F)) is amended by striking under regulations); and inserting the following: \u201cunder regulations, including\u2014\n(i) remuneration offered or transferred to an individual while participating in a clinical trial, as defined in subsection (d) of the first section 2709 of the Public Health Service Act for expenses incurred as part of the trial, other than patient cost-sharing obligations, including without limitation travel, transportation, and meal expenses, so long as such remuneration is made available to all study participants and facilitates inclusion of patients from all relevant demographic and socioeconomic populations and geographies including rural communities; and (ii) the free provision to an individual of digital health technologies where\u2014 (I) the use of the digital health technologies is intended to facilitate the participation of underrepresented patient populations; and (II) the digital health technologies are necessary for participation in such trial; .\n##### (b) Conforming amendment to the anti-Kickback statute\nSection 1128B(b)(3) of the Social Security Act (42 U.S.C. 1320a\u20137b(b)(3)) is amended\u2014\n**(1)**\nby striking and at the end of subparagraph (K);\n**(2)**\nby striking the period at the end of subparagraph (L) and inserting ; and ;\n**(3)**\nby aligning the left margin of each of subparagraphs (J) and (K) with the left margin of subparagraph (I); and\n**(4)**\nby inserting after subparagraph (L) the following new subparagraphs:\n(M) any remuneration offered or transferred to an individual while participating in a clinical trial (as defined in subsection (d) of the first section 2709 of the Public Health Service Act) for expenses incurred as part of the trial, other than patient cost-sharing obligations, including without limitation travel, transportation, and meal expenses, so long as such remuneration is made available to all study participants and facilitates inclusion of patients from all relevant demographic and socioeconomic populations and geographies, including rural communities; and (N) the free provision to an individual of digital health technologies where\u2014 (i) the use of the digital health technologies is intended to facilitate in any phase of a clinical trial (as so defined) the participation of underrepresented patient populations; and (ii) the digital health technologies are necessary to such participation. .\n##### (c) Effective date\nThe amendments made by this section shall apply to remuneration provided on or after the date of enactment of this Act.\n#### 5. Encouragement of clinical trial accessibility through support of clinical trial cost-sharing\nThe payment of patient cost-sharing obligations associated with participation in a clinical trial (as defined in subsection (d) of the first section 2709 of the Public Health Service Act) or for which a diversity action plan is required pursuant to sections 505(z) or 520(g)(9) of the Federal Food, Drug, and Cosmetic Act by drug or device manufacturers or their agents for their clinical trial participants shall not be considered a violation of section 1128A of the Social Security Act ( 42 U.S.C. 1320a\u20137a ) (commonly known as the Civil Monetary Penalties Law ), section 1128B of the Social Security Act ( 42 U.S.C. 1320a\u20137b ), or sections 3729 through 3733 of title 31, United States Code (commonly known as the False Claims Act ), provided that the following requirements are met:\n**(1)**\nThe trial and any coverage of items or services provided in the trial is consistent with all applicable coverage rules by any Federal health care programs providing coverage and reimbursement for beneficiaries participating in the trial as study subjects, including but not limited to, any existing trial qualification requirements imposed by the Centers for Medicare & Medicaid Services for Medicare coverage of the trial.\n**(2)**\nThe proposed arrangement for the payment of patient cost-sharing obligations is a reasonable means of facilitating enrollment of an underrepresented set of subjects or reducing the likelihood of attrition in the trial by removing a potential financial barrier to participation in the trial.\n**(3)**\nAny sponsor payments of participating patient cost-sharing obligations must be available throughout the entirety of the clinical trial.\n**(4)**\nAny sponsor payments of participating patient cost-sharing obligations are not contingent on the future use or purchase of any product or service.\n**(5)**\nAny sponsor payments of participating patient cost-sharing obligations will not be provided in excess of the patient\u2019s cost-sharing obligations under relevant Federal health care programs.\n**(6)**\nA participating patient receiving cost-sharing assistance from a sponsor will be required to agree not to accept other financial assistance to cover the patient\u2019s cost-sharing obligations.\n**(7)**\nAny sponsor payments of participating patient cost-sharing obligations will cease upon the patient\u2019s disenrollment from the clinical trial or the conclusion of the clinical trial, whichever is first.\n**(8)**\nThe proposed arrangement for the payment of patient cost-sharing obligations includes the following elements to protect against improper increased costs or inappropriate utilization of items and services reimbursed in whole or in part under Federal health care programs:\n**(A)**\nThe availability of cost-sharing subsidies will not be advertised, but may be disclosed as required or permitted by law in the informed consent forms, protocol, or other documentation associated with the study.\n**(B)**\nParticipating Federal health care program beneficiaries must satisfy formal, objective, and predetermined enrollment criteria and execute an informed consent document.\n**(C)**\nThe sponsor must enter into a written agreement with investigators that requires the investigators to comply with the written protocol for the study and to be subject to oversight and monitoring by an institutional review board or other similar body providing independent oversight for the trial.\n**(D)**\nTotal enrollment for the trial is capped.\n#### 6. Exclusion from gross income for remuneration provided by sponsors of approved clinical trials to participants\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139J. Remuneration provided by sponsors of approved clinical trials to participants (a) In general Gross income shall not include the value of any payment received by an individual from participation in an approved clinical trial (as defined in subsection (d) of the first section 2709 of the Public Health Service Act). (b) Limitation The amount excluded from gross income under subsection (a) for any taxable year shall not exceed $2,000. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 140 the following new item:\nSec. 139J. Remuneration provided by sponsors of approved clinical trials to participants. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of enactment of this Act.\n#### 7. Rule of construction\nNothing in section 4 or section 5 of this Act shall be construed to limit or narrow in any way any other protections from liability under section 1128A or 1128B of the Social Security Act (42 U.S.C. 1320a\u20137a; 1320a\u20137b) or sections 3729 through 3733 of title 31, United States Code, whether such other protections are set forth in statute, regulation, or any form of guidance, that may apply to any practice or arrangement encouraging participation in or accessibility of clinical trials.",
      "versionDate": "2025-05-20",
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
        "actionDate": "2026-04-29",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4440",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Clinical Trial Modernization Act",
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
        "name": "Health",
        "updateDate": "2025-05-29T15:18:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-20",
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
          "measure-id": "id119hr3521",
          "measure-number": "3521",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-20",
          "originChamber": "HOUSE",
          "update-date": "2026-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3521v00",
            "update-date": "2026-03-11"
          },
          "action-date": "2025-05-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Clinical Trial Modernization Act</strong></p><p>This bill authorizes a grant program and provides certain exemptions to support the participation of individuals in clinical trials.</p><p>Specifically, the bill authorizes a grant program to support outreach, education, and recruitment\u00a0efforts for clinical trials that may benefit certain underrepresented populations or communities in need, such as rural or tribal areas.</p><p>The bill also exempts from anti-kickback laws for federal health care programs (1) remuneration that is offered to cover participants' expenses to participate in clinical trials, (2) the provision of free digital health technologies to support participation of underrepresented populations in clinical trials, and (3) payment for participants' cost-sharing obligations in relation to clinical trials.</p><p>Finally, the bill exempts up to $2,000 in remuneration that is received for participating in a clinical trial from income tax.</p>"
        },
        "title": "Clinical Trial Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3521.xml",
    "summary": {
      "actionDate": "2025-05-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Clinical Trial Modernization Act</strong></p><p>This bill authorizes a grant program and provides certain exemptions to support the participation of individuals in clinical trials.</p><p>Specifically, the bill authorizes a grant program to support outreach, education, and recruitment\u00a0efforts for clinical trials that may benefit certain underrepresented populations or communities in need, such as rural or tribal areas.</p><p>The bill also exempts from anti-kickback laws for federal health care programs (1) remuneration that is offered to cover participants' expenses to participate in clinical trials, (2) the provision of free digital health technologies to support participation of underrepresented populations in clinical trials, and (3) payment for participants' cost-sharing obligations in relation to clinical trials.</p><p>Finally, the bill exempts up to $2,000 in remuneration that is received for participating in a clinical trial from income tax.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr3521"
    },
    "title": "Clinical Trial Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Clinical Trial Modernization Act</strong></p><p>This bill authorizes a grant program and provides certain exemptions to support the participation of individuals in clinical trials.</p><p>Specifically, the bill authorizes a grant program to support outreach, education, and recruitment\u00a0efforts for clinical trials that may benefit certain underrepresented populations or communities in need, such as rural or tribal areas.</p><p>The bill also exempts from anti-kickback laws for federal health care programs (1) remuneration that is offered to cover participants' expenses to participate in clinical trials, (2) the provision of free digital health technologies to support participation of underrepresented populations in clinical trials, and (3) payment for participants' cost-sharing obligations in relation to clinical trials.</p><p>Finally, the bill exempts up to $2,000 in remuneration that is received for participating in a clinical trial from income tax.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr3521"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3521ih.xml"
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
      "title": "Clinical Trial Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clinical Trial Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modernize clinical trials and remove barriers for participation in clinical trials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:24Z"
    }
  ]
}
```
