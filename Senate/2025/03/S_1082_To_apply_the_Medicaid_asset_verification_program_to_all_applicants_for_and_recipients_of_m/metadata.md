# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1082?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1082
- Title: Safeguarding Medicaid Act
- Congress: 119
- Bill type: S
- Bill number: 1082
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S1778-1779)
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S1778-1779)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1082",
    "number": "1082",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Safeguarding Medicaid Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S1778-1779)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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
        "item": [
          {
            "date": "2025-03-14T20:55:32Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-14T20:55:32Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "LA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OK"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WY"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "KS"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "MO"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1082is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1082\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Barrasso (for himself, Mr. Kennedy , Mr. Lankford , Mr. Wicker , Ms. Lummis , Mrs. Blackburn , Mr. Marshall , Mr. Scott of Florida , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo apply the Medicaid asset verification program to all applicants for, and recipients of, medical assistance in all States and territories, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Medicaid Act .\n#### 2. Application of medicaid asset test to all applicants for, and recipients of, medical assistance in all States and territories\n##### (a) In general\nSection 1940 of the Social Security Act ( 42 U.S.C. 1396w ) is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (4); and\n**(2)**\nin subsection (b)(1)(A), by striking on the basis of being aged, blind, or disabled .\n##### (b) Rules\nThe Secretary of Health and Human Services shall promulgate such rules as are necessary to implement the amendments made by subsection (a).\n##### (c) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by subsection (a) shall take effect on the date that is 1 year after the date of enactment of this Act.\n**(2) Phase-in of implementation**\n**(A) In general**\nDuring the 1-year period that begins on the date of enactment of this Act, the Secretary of Health and Human Services shall require States to submit and implement a plan for an electronic integrated asset verification program that meets the requirements of section 1940 of the Social Security Act (as amended by subsection (a)).\n**(B) Implementation before effective date**\nNothing in this subsection or section 1940 of the Social Security Act ( 42 U.S.C. 1396w ) shall be construed as prohibiting a State from implementing an asset verification program that meets the requirements of such section (as amended by subsection (a)) in advance of the effective date specified under paragraph (1).\n**(C) Delay of effective date**\nIf a State requests a delay of the effective date specified under paragraph (1) on the basis of ongoing economic hardship limitations, as determined by the chief executive officer of the State, the Secretary of Health and Human Services may delay such effective date for up to 365 days.\n#### 3. Medicaid resources eligibility requirement\n##### (a) In general\nSection 1902(e)(14)(C) of the Social Security Act ( 42 U.S.C. 1396a(e)(14)(C) ) is amended to read as follows:\n(C) Resources test requirement (i) In general Except as provided in clause (iii), notwithstanding any other provision of this title, in the case of an individual with respect to whom a determination of income eligibility for medical assistance under the State plan or under any waiver of such plan is required, the State shall also apply a resources eligibility test that meets the requirement of clause (ii). (ii) Requirement A State resources eligibility test meets the requirement of this clause if the test precludes eligibility for any individual whose resources (as determined under section 1613 for purposes of the supplemental security income program) exceed the maximum amount of resources that an individual may have and obtain benefits under that program, or such amount as the State shall establish. (iii) No effect on continuous eligibility requirements for pregnant and postpartum women or children Nothing in this subparagraph shall affect the application of paragraph (6), (12), or (16) of this subsection (relating to continuous eligibility for pregnant and postpartum women and children under the age of 19). .\n##### (b) Conforming amendment\nSection 1902(e)(6) of the Social Security Act ( 42 U.S.C. 1396a(e)(6) ) is amended by inserting or resources after income each place it appears.\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date that is 2 years after the date of enactment of this Act.\n#### 4. Requiring CMS to track State asset verification of Federal Medicaid programs\n##### (a) Tracking asset verification program savings\nNot later than 2 years after the date of the enactment of this Act, the Secretary of Health and Human Services, acting through the Centers for Medicare & Medicaid Services, shall create a Federal tracking system of the savings in Federal expenditures on the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) that are associated with the asset verification program requirement added under section 2(a).\n##### (b) Reports to Congress\n**(1) In general**\nBeginning with the first year that begins on or after the date of enactment of this Act, each State shall submit to the Secretary, as part of the triennial review required under the Payment Error Rate Measurement program of the Centers for Medicare & Medicaid Services, a report, that the Secretary shall make publicly available, on the activities of the State relating to eligibility determinations and renewals conducted during the year for which the report is submitted, and which includes, with respect to such year, the following information:\n**(A)**\nThe number of eligibility renewals initiated, and asset checks conducted, beneficiaries renewed on a total and ex parte basis.\n**(B)**\nThe number of asset checks conducted out of the number of new applications initiated and the number of applicants determined eligible after such checks.\n**(C)**\nSuch other information related to eligibility determinations and renewals during such month, as identified by the Secretary.\n**(2) Application to territories**\nFor purposes of applying the reporting requirements of paragraph (1) to Puerto Rico, the Virgin Islands, Guam, the Northern Mariana Islands, and American Samoa, the Secretary shall promulgate regulations to modify such requirements so that they are similar to the reporting requirements that apply under such paragraph to the 50 States and the District of Columbia but are reasonable given the circumstances of each such territory.\n##### (c) Enforcement and corrective action\n**(1) In general**\nThe Secretary may assess a State\u2019s compliance with all Federal requirements applicable to eligibility determinations, redeterminations, and Medicaid payment error rate measurement (PERM) reporting requirements, and, if the Secretary determines that a State did not comply with any such requirements during the 180-day period preceding the assessment, the Secretary may require the State to submit and implement a corrective action plan in accordance with paragraph (2).\n**(2) Corrective action plan**\nA State that receives a written notice from the Secretary that the Secretary has determined that the State is not in compliance with a requirement described in paragraph (1) shall\u2014\n**(A)**\nnot later than 90 days after receiving such notice, submit a corrective action plan to the Secretary;\n**(B)**\nnot later than 90 days after the date on which such corrective action plan is submitted to the Secretary, receive approval or disapproval for the plan from the Secretary; and\n**(C)**\nbegin implementation of such corrective action plan not later than 90 days after such approval.",
      "versionDate": "2025-03-14",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-04-09T14:15:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119s1082",
          "measure-number": "1082",
          "measure-type": "s",
          "orig-publish-date": "2025-03-14",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1082v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safeguarding Medicaid Act</strong></p><p>This bill requires states and territories to implement asset verification programs to determine an individual's Medicaid eligibility.\u00a0</p><p>Currently, states, the District of Columbia, and Puerto Rico are required to have asset verification\u00a0programs to determine an individual's eligibility for Medicaid if the individual is age 65 or older, blind, or disabled. The bill applies this requirement to all states and territories and to all individuals seeking Medicaid eligibility.\u00a0</p><p>The bill also requires state Medicaid programs to implement resource tests to determine an individual's Medicaid eligibility (currently, such tests are prohibited except for those age 65 or older or who are blind or disabled). The resource test must conform with the resource test for determining an individual's eligibility for Supplemental Security Income, unless the state specifies a different threshold.</p><p>The Centers for Medicare & Medicaid Services (CMS) must create a system to track any federal savings due to implementation of the required asset verification programs.\u00a0</p><p>States that do not comply with federal requirements regarding Medicaid eligibility determinations must submit corrective action plans to the CMS.</p><p>\u00a0</p>"
        },
        "title": "Safeguarding Medicaid Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1082.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguarding Medicaid Act</strong></p><p>This bill requires states and territories to implement asset verification programs to determine an individual's Medicaid eligibility.\u00a0</p><p>Currently, states, the District of Columbia, and Puerto Rico are required to have asset verification\u00a0programs to determine an individual's eligibility for Medicaid if the individual is age 65 or older, blind, or disabled. The bill applies this requirement to all states and territories and to all individuals seeking Medicaid eligibility.\u00a0</p><p>The bill also requires state Medicaid programs to implement resource tests to determine an individual's Medicaid eligibility (currently, such tests are prohibited except for those age 65 or older or who are blind or disabled). The resource test must conform with the resource test for determining an individual's eligibility for Supplemental Security Income, unless the state specifies a different threshold.</p><p>The Centers for Medicare & Medicaid Services (CMS) must create a system to track any federal savings due to implementation of the required asset verification programs.\u00a0</p><p>States that do not comply with federal requirements regarding Medicaid eligibility determinations must submit corrective action plans to the CMS.</p><p>\u00a0</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s1082"
    },
    "title": "Safeguarding Medicaid Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguarding Medicaid Act</strong></p><p>This bill requires states and territories to implement asset verification programs to determine an individual's Medicaid eligibility.\u00a0</p><p>Currently, states, the District of Columbia, and Puerto Rico are required to have asset verification\u00a0programs to determine an individual's eligibility for Medicaid if the individual is age 65 or older, blind, or disabled. The bill applies this requirement to all states and territories and to all individuals seeking Medicaid eligibility.\u00a0</p><p>The bill also requires state Medicaid programs to implement resource tests to determine an individual's Medicaid eligibility (currently, such tests are prohibited except for those age 65 or older or who are blind or disabled). The resource test must conform with the resource test for determining an individual's eligibility for Supplemental Security Income, unless the state specifies a different threshold.</p><p>The Centers for Medicare & Medicaid Services (CMS) must create a system to track any federal savings due to implementation of the required asset verification programs.\u00a0</p><p>States that do not comply with federal requirements regarding Medicaid eligibility determinations must submit corrective action plans to the CMS.</p><p>\u00a0</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s1082"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1082is.xml"
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
      "title": "Safeguarding Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguarding Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to apply the Medicaid asset verification program to all applicants for, and recipients of, medical assistance in all States and territories, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:23Z"
    }
  ]
}
```
