# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/977?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/977
- Title: End Taxpayer Funding of Gender Experimentation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 977
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/977",
    "number": "977",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "End Taxpayer Funding of Gender Experimentation Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
            "date": "2025-03-12T16:55:47Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-12T16:55:47Z",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "MS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ND"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "MO"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "NC"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "SC"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "MT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "TN"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "IN"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "MS"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "UT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "WY"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s977is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 977\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Marshall (for himself, Mrs. Hyde-Smith , Mr. Cramer , Mr. Hawley , Mr. Budd , Mr. Graham , Mr. Sheehy , Mrs. Blackburn , Mr. Banks , Mr. Wicker , Mr. Lee , Ms. Lummis , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo prohibit taxpayer-funded gender transition procedures, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the End Taxpayer Funding of Gender Experimentation Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Prohibiting federally funded gender transition procedures\nSec. 101. Prohibiting taxpayer-funded gender transition procedures.\nSec. 102. Amendment to table of chapters.\nTITLE II\u2014Application under the Affordable Care Act\nSec. 201. Clarifying application of prohibition to premium credits and cost-sharing reductions under ACA.\nI\nProhibiting federally funded gender transition procedures\n#### 101. Prohibiting taxpayer-funded gender transition procedures\nTitle 1, United States Code, is amended by adding at the end the following new chapter:\n4 Prohibiting taxpayer-funded gender transition procedures Sec. 301. Prohibition on funding for gender transition procedures. 302. Prohibition on funding for health benefits plans that cover gender transition procedures. 303. Limitation on Federal facilities and employees. 304. Construction relating to separate coverage. 305. Construction relating to the use of non-Federal funds for health coverage. 306. Construction relating to complications arising from gender transition procedures. 307. Definitions. 301. Prohibition on funding for gender transition procedures No funds authorized or appropriated by Federal law, and none of the funds in any trust fund to which funds are authorized or appropriated by Federal law, shall be expended for any gender transition procedures. 302. Prohibition on funding for health benefits plans that cover gender transition procedures No funds authorized or appropriated by Federal law, and none of the funds in any trust fund to which funds are authorized or appropriated by Federal law, shall be expended for health benefits coverage that includes coverage of gender transition procedures. 303. Limitation on Federal facilities and employees No health care service furnished\u2014 (1) by or in a health care facility owned or operated by the Federal Government; or (2) by any physician or other individual employed by the Federal Government to provide health care services within the scope of the physician\u2019s or individual\u2019s employment, may include gender transition procedures. 304. Construction relating to separate coverage Nothing in this chapter shall be construed as prohibiting any individual, entity, or State or locality from purchasing separate coverage for gender transition procedures or health benefits coverage that includes gender transition procedures so long as such coverage is paid for entirely using only funds not authorized or appropriated by Federal law and such coverage shall not be purchased using matching funds required for a federally subsidized program, including a State\u2019s or locality\u2019s contribution of Medicaid matching funds. 305. Construction relating to the use of non-Federal funds for health coverage Nothing in this chapter shall be construed as restricting the ability of any non-Federal health benefits coverage provider from offering coverage for gender transition procedures, or the ability of a State or locality to contract separately with such a provider for such coverage, so long as only funds not authorized or appropriated by Federal law are used and such coverage shall not be purchased using matching funds required for a federally subsidized program, including a State\u2019s or locality\u2019s contribution of Medicaid matching funds. 306. Construction relating to complications arising from gender transition procedures Nothing in this chapter shall be construed to apply to the treatment of any infection, injury, disease, or disorder that has been caused by or exacerbated by the performance of a gender transition procedure. 307. Definitions For purposes of this chapter: (1) Female The term female , when used to refer to a natural person, means an individual who naturally has, had, will have, or would have, but for a congenital anomaly, historical accident, or intentional or unintentional disruption, the reproductive system that at some point produces, transports, and utilizes eggs for fertilization. (2) Gender transition The term gender transition means the process in which an individual goes from identifying with or presenting as his or her sex to identifying with or presenting a self-proclaimed identity that does not correspond with or is different from his or her sex, and may be accompanied with social, legal, or physical changes. (3) Gender transition procedure (A) In general The term gender transition procedure means any hormonal or surgical intervention for the purpose of gender transition, including\u2014 (i) gonadotropin-releasing hormone (GnRH) agonists or other puberty-blocking or suppressing drugs to stop or delay normal puberty; (ii) testosterone, estrogen, progesterone, or other androgens to an individual at doses that are supraphysiologic to what would normally be produced endogenously in a healthy individual of the same age and sex; (iii) castration; (iv) orchiectomy; (v) scrotoplasty; (vi) implantation of erection or testicular prostheses; (vii) vasectomy; (viii) hysterectomy; (ix) oophorectomy; (x) ovariectomy; (xi) reconstruction of the fixed part of the urethra with or without a metoidioplasty or a phalloplasty; (xii) metoidioplasty; (xiii) penectomy; (xiv) phalloplasty; (xv) vaginoplasty; (xvi) clitoroplasty (xvii) vaginectomy; (xviii) vulvoplasty; (xix) reduction thyrochondroplasty; (xx) chondrolaryngoplasty; (xxi) mastectomy; (xxii) tubal ligation; (xxiii) sterilization; (xxiv) any plastic, cosmetic, or aesthetic surgery that feminizes or masculinizes the facial or other physiological features of an individual; (xxv) any placement of chest implants to create feminine breasts; (xxvi) any placement of fat or artificial implants in the gluteal region; (xxvii) augmentation mammoplasty; (xxviii) liposuction; (xxix) lipofilling; (xxx) voice surgery; (xxxi) hair reconstruction; (xxxii) pectoral implants; and (xxxiii) the removal of any otherwise healthy or non-diseased body part or tissue. (B) Exclusions The term gender transition procedure does not include the following when furnished to an individual by a health care provider with the consent of such individual or, if applicable, such individual\u2019s parents or legal guardian: (i) Services to individuals born with a medically verifiable disorder of sex development, including an individual with external sex characteristics that are irresolvably ambiguous, such as an individual born with 46 XX chromosomes with virilization, an individual born with 46 XY chromosomes with undervirilization, or an individual born having both ovarian and testicular tissue. (ii) Services provided when a physician has otherwise diagnosed a disorder of sexual development in which the physician has determined through genetic or biochemical testing that the individual does not have normal sex chromosome structure, sex steroid hormone production, or sex steroid hormone action for a healthy individual of the same sex and age. (iii) The treatment of any infection, injury, disease, or disorder that has been caused by or exacerbated by the performance of gender transition procedures, whether or not the gender transition procedure was performed in accordance with State and Federal law or whether or not funding for the gender transition procedure is permissible under this section. (iv) Any procedure undertaken because the individual suffers from a physical disorder, physical injury, or physical illness (but not mental, behavioral, or emotional distress or a mental, behavioral, or emotional disorder) that would, as certified by a physician, place the individual in imminent danger of death or impairment of major bodily function, unless the procedure is performed. (v) Puberty suppression or blocking prescription drugs for the purpose of normalizing puberty for a minor experiencing precocious puberty. (vi) Male circumcision. (4) Male The term male , when used to refer to a natural person, means an individual who naturally has, had, will have, or would have, but for a congenital anomaly, historical accident, or intentional or unintentional disruption, the reproductive system that at some point produces, transports, and utilizes sperm for fertilization. (5) Sex The term sex , when referring to an individual\u2019s sex, means to refer to either male or female, as biologically determined. .\n#### 102. Amendment to table of chapters\nThe table of chapters for title 1, United States Code, is amended by adding at the end the following new item:\n4. Prohibiting taxpayer-funded gender transition procedures 301 .\nII\nApplication under the Affordable Care Act\n#### 201. Clarifying application of prohibition to premium credits and cost-sharing reductions under ACA\n##### (a) In general\n**(1) Disallowance of refundable credit and cost-sharing reductions for coverage under qualified health plan which provides coverage for gender procedures**\n**(A) In general**\nSubparagraph (A) of section 36B(c)(3) of the Internal Revenue Code of 1986 is amended by inserting before the period at the end the following: or any health plan that includes coverage for gender transition procedures, as defined in section 307 of title 1, United States Code (other than any procedure described in section 306 of such title) .\n**(B) Option to purchase or offer separate coverage or plan**\nParagraph (3) of section 36B(c) of such Code is amended by adding at the end the following new subparagraph:\n(C) Separate coverage or plan for gender transition procedures allowed (i) Option to purchase separate coverage or plan Nothing in subparagraph (A) shall be construed as prohibiting any individual from purchasing separate coverage for gender transition procedures described in such subparagraph, or a health plan that includes such gender transition procedures, so long as no credit is allowed under this section with respect to the premiums for such coverage or plan. (ii) Option to offer coverage or plan Nothing in subparagraph (A) shall restrict any non-Federal health insurance issuer offering a health plan from offering separate coverage for gender transition procedures described in such subparagraph, or a plan that includes such gender transition procedures, so long as premiums for such separate coverage or plan are not paid for with any amount attributable to the credit allowed under this section (or the amount of any advance payment of the credit under section 1412 of the Patient Protection and Affordable Care Act). .\n**(2) Disallowance of small employer health insurance expense credit for plan which includes coverage for gender transition procedures**\nSubsection (h) of section 45R of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking Any term and inserting the following:\n(1) In general Any term ; and\n**(B)**\nby adding at the end the following new paragraph:\n(2) Exclusion of health plans including coverage for gender transition procedures (A) In general In this section, the term qualified health plan does not include any health plan that includes coverage for gender transition procedures, as defined in section 307 of title 1, United States Code (other than any procedure described in section 306 of such title). (B) Separate coverage or plan for gender transition procedures allowed (i) Option to purchase separate coverage or plan Nothing in subparagraph (A) shall be construed as prohibiting any employer from purchasing for its employees separate coverage for gender transition procedures described in such subparagraph, or a health plan that includes such gender transition procedures, so long as no credit is allowed under this section with respect to the employer contributions for such coverage or plan. (ii) Option to offer coverage or plan Nothing in subparagraph (A) shall restrict any non-Federal health insurance issuer offering a health plan from offering separate coverage for gender transition procedures described in such subparagraph, or a plan that includes such gender transition procedures, so long as such separate coverage or plan is not paid for with any employer contribution eligible for the credit allowed under this section. .\n##### (b) Application to multi-State plans\nSection 1334(a) of Public Law 111\u2013148 ( 42 U.S.C. 18054(a) ) is amended by adding at the end the following new paragraph:\n(8) Coverage consistent with Federal policy regarding gender transition procedures In entering into contracts under this subsection, the Director shall ensure that no multi-State qualified health plan offered in an Exchange provides health benefits coverage for which the expenditure of Federal funds is prohibited under chapter 4 of title 1, United States Code. .\n##### (c) Effective date\nThe amendments made by subsection (a) shall apply to taxable years ending after the date that is 1 year after the date of enactment of this Act, but only with respect to plan years beginning after such date, and the amendment made by subsection (b) shall apply to plan years beginning after such date.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on the Judiciary, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2202",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Taxpayer Funding of Gender Experimentation Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-04-03T11:30:51Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s977is.xml"
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
      "title": "End Taxpayer Funding of Gender Experimentation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Taxpayer Funding of Gender Experimentation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit taxpayer-funded gender transition procedures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:38Z"
    }
  ]
}
```
