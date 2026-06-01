# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6178
- Title: Increasing Access to Lung Cancer Screening Act
- Congress: 119
- Bill type: HR
- Bill number: 6178
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-02-24T09:05:50Z
- Update date including text: 2026-02-24T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6178",
    "number": "6178",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Increasing Access to Lung Cancer Screening Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:50Z",
    "updateDateIncludingText": "2026-02-24T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:03:20Z",
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
          "date": "2025-11-20T15:03:15Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "NJ"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "OR"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6178ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6178\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Castor of Florida (for herself, Mr. Fitzpatrick , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XIX of the Social Security Act to require coverage under State plans under the Medicaid program for annual lung cancer screening with no cost sharing for individuals for whom screening is recommended by U.S. Preventive Services Task Force guidelines, to expand coverage under Medicaid of counseling and pharmacotherapy for cessation of tobacco use, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Increasing Access to Lung Cancer Screening Act .\n#### 2. Medicaid coverage of annual lung cancer screening with no cost sharing for certain individuals\n##### (a) In general\nSection 1905(a)(4) of the Social Security Act ( 42 U.S.C. 1396d(a)(4) ) is amended\u2014\n**(1)**\nby striking and before (F) ; and\n**(2)**\nby inserting before the semicolon at the end the following: ; and (G) an annual lung cancer screening for individuals who are eligible under the plan and for whom such screening is recommended under guidelines published by the United States Preventive Services Task Force, without regard to prior authorization .\n##### (b) No cost sharing\n**(1) In general**\nSubsections (a)(2) and (b)(2) of section 1916 of the Social Security Act ( 42 U.S.C. 1396o ) are each amended\u2014\n**(A)**\nin subparagraph (G), by adding at the end , or ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(H) lung cancer screening for which payment may be made under the State plan pursuant section to 1905(a)(4)(G); .\n**(2) Application to alternative cost sharing**\nSection 1916A(b)(3)(B) of the Social Security Act ( 42 U.S.C. 1396o\u20131(b)(3)(B) ) is amended by adding at the end the following new clause:\n(xiv) Lung cancer screening for which payment may be made under the State plan pursuant to section 1905(a)(4)(G). .\n##### (c) Application to Medicaid managed care organizations\nSection 1932(b) of the Social Security Act ( 42 U.S.C. 1396u\u20132(b) ) is amended by adding at the end the following new paragraph:\n(9) Lung cancer screening Each contract with a medicaid managed care organization under section 1903(m) shall require the organization to provide coverage for lung cancer screening for which payment may be made under the State plan pursuant to section 1905(a)(4)(G) without regard to prior authorization. .\n##### (d) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n**(2) Exception if State legislation required**\nIn the case of a State plan for medical assistance under title XIX of the Social Security Act which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by the amendments made by this section, the State plan shall not be regarded as failing to comply with the requirements of such title solely on the basis of its failure to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that begins after the date of the enactment of this Act. For purposes of the previous sentence, in the case of a State that has a 2-year legislative session, each year of such session shall be deemed to be a separate regular session of the State legislature.\n#### 3. Expanding coverage under Medicaid of Counseling and Pharmacotherapy for Cessation of Tobacco Use to all Medicaid individuals\n##### (a) In general\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended\u2014\n**(1)**\nin subsection (a)(4)(D)\u2014\n**(A)**\nby striking by pregnant women ; and\n**(B)**\nby inserting without regard to prior authorization after (as defined in subsection (bb)) ; and\n**(2)**\nin subsection (bb)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking the first place it appears by pregnant women ; and\n**(ii)**\nby striking by pregnant women who and inserting by individuals who ;\n**(B)**\nin paragraph (2)(A), by striking with respect to pregnant women ; and\n**(C)**\nin paragraph (2)(B), by striking by pregnant women .\n##### (b) Conforming amendments\n**(1)**\nSection 1927(d)(2)(F) of the Social Security Act ( 42 U.S.C. 1396r\u20138(d)(2)(F) ) is amended by striking , in the case of pregnant women .\n**(2)**\nSection 1916 of the Social Security Act ( 42 U.S.C. 1396o ), as amended by section 1, is further amended in each of subsections (a)(2) and (b)(2)\u2014\n**(A)**\nin subparagraph (B), by striking , and counseling and pharmacotherapy for cessation of tobacco use by pregnant women (as defined in section 1905(bb)) and covered outpatient drugs (as defined in subsection (k)(2) of section 1927 and including nonprescription drugs described in subsection (d)(2) of such section) that are prescribed for purposes of promoting, and when used to promote, tobacco cessation by pregnant women in accordance with the Guideline referred to in section 1905(bb)(2)(A) ;\n**(B)**\nin subparagraph (H), at the end by adding or ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(I) counseling and pharmacotherapy for cessation of tobacco use (as defined in section 1905(bb)) and covered outpatient drugs (as defined in subsection (k)(2) of section 1927 and including nonprescription drugs described in subsection (d)(2) of such section) that are prescribed for purposes of promoting, and when used to promote, tobacco cessation in accordance with the Guideline referred to in section 1905(bb)(2)(A); and .\n**(3)**\nSection 1916A(b)(3)(B) of such Act ( 42 U.S.C. 1396o\u20131(b)(3)(B) ), as amended by section 1, is further amended\u2014\n**(A)**\nin clause (iii), by striking , and counseling and pharmacotherapy for cessation of tobacco use by pregnant women (as defined in section 1905(bb)) ; and\n**(B)**\nby adding at the end the following new clause:\n(xv) Counseling and pharmacotherapy for cessation of tobacco use (as defined in section 1905(bb)). .\n##### (c) Application to Medicaid managed care organizations\nSection 1932(b) of the Social Security Act ( 42 U.S.C. 1396u\u20132(b) ), as amended by section 1, is further amended by adding at the end the following new paragraph:\n(10) Cessation of Tobacco Use Each contract with a medicaid managed care organization under section 1903(m) shall require the organization to provide coverage for counseling and pharmacotherapy for cessation of tobacco use without regard to prior authorization. .\n##### (d) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n**(2) Exception if State legislation required**\nIn the case of a State plan for medical assistance under title XIX of the Social Security Act which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by the amendments made by this section, the State plan shall not be regarded as failing to comply with the requirements of such title solely on the basis of its failure to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that begins after the date of the enactment of this Act. For purposes of the previous sentence, in the case of a State that has a 2-year legislative session, each year of such session shall be deemed to be a separate regular session of the State legislature.\n#### 4. Coverage under Medicare and private health insurance of annual lung cancer screening without utilization management requirements\n##### (a) Medicare\n**(1) In general**\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(z) Special rule for annual lung cancer screening Notwithstanding any other provision of this title, in the case of an annual lung cancer screening for which benefits are provided under this part for any individual for whom such screening is recommended in accordance with guidelines issued by the Secretary, such benefits shall be provided without application of any prior authorization. .\n**(2) Application under Medicare Advantage**\nSection 1852(a)(1)(B) of the Social Security Act ( 42 U.S.C. 1395w\u201322(a)(1)(B) ) is amended by adding at the end the following new clause:\n(vii) Prohibition of application of certain requirements for annual lung cancer screening In the case of an annual lung cancer screening for which benefits are provided under part B for any individual for whom such screening is recommended in accordance with guidelines issued by the Secretary for purposes of section 1834(z), an MA plan may not impose any prior authorization with respect to the coverage of such screening under such plan. .\n**(3) Effective date**\nThe amendments made by this subsection shall apply with respect to services furnished on or after January 1, 2026.\n##### (b) Individual and group health insurance markets\n**(1) In general**\nSection 2713 of the Public Health Service Act ( 42 U.S.C. 300gg\u2013(3) ) is amended by adding at the end the following new subsection:\n(d) Prohibition of application of certain requirements for annual lung cancer screening A group health plan and a health insurance issuer offering group or individual health insurance coverage may not impose any prior authorization with respect to the benefits under such plan or coverage for an annual lung cancer screening for any individual for whom such screening is recommended by the United States Preventive Services Task Force. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply with respect to plan years beginning on or after January 1, 2026.\n#### 5. Lung cancer screening education and outreach\n##### (a) In general\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ), in consultation with patient and lung cancer advocacy groups, shall conduct an education and outreach campaign for purposes of informing individuals and health care providers of\u2014\n**(1)**\nthe importance of lung cancer screenings; and\n**(2)**\nthe categories of individuals who should receive such screenings.\n##### (b) Manner of outreach\nThe Secretary may carry out the campaign described in subsection (a) directly, by contract, through the issuance of grants, or otherwise. In carrying out such campaign, the Secretary shall ensure that the campaign is targeted to reach individuals at high risk of lung cancer.\n##### (c) Funding\nThere are authorized to be appropriated $10,000,000 for each of fiscal years 2026 through 2030 for purposes of carrying out this section.\n#### 6. Report\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall conduct a study and submit to Congress a report on the demographics of individuals diagnosed with lung cancer and individuals screened for such cancer. Such report shall identify\u2014\n**(1)**\nany segments of the population diagnosed with lung cancer but not captured in current screening eligibility guidelines (such as firefighters, veterans, and women under 50 years of age); and\n**(2)**\nactions the Federal Government could take to improve screening for such cancer among such segments.",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-11-24T17:46:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6178",
          "measure-number": "6178",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6178v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Increasing Access to Lung Cancer Screening Act</b></p> <p>This bill provides for coverage without prior authorization requirements of annual lung cancer screenings under Medicaid, Medicare, and private health insurance for individuals for whom screenings are recommended under U.S. Preventive Services Task Force guidelines. It also expands Medicaid coverage of counseling and pharmacotherapy for cessation of tobacco use to all individuals, rather than only pregnant women. </p> <p>The Department of Health and Human Services must conduct outreach on the importance of lung cancer screenings and who should be screened, and the Government Accountability Office must report on the demographics of those diagnosed with lung cancer and recommend ways the federal government can improve screenings.</p>"
        },
        "title": "Increasing Access to Lung Cancer Screening Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6178.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Increasing Access to Lung Cancer Screening Act</b></p> <p>This bill provides for coverage without prior authorization requirements of annual lung cancer screenings under Medicaid, Medicare, and private health insurance for individuals for whom screenings are recommended under U.S. Preventive Services Task Force guidelines. It also expands Medicaid coverage of counseling and pharmacotherapy for cessation of tobacco use to all individuals, rather than only pregnant women. </p> <p>The Department of Health and Human Services must conduct outreach on the importance of lung cancer screenings and who should be screened, and the Government Accountability Office must report on the demographics of those diagnosed with lung cancer and recommend ways the federal government can improve screenings.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6178"
    },
    "title": "Increasing Access to Lung Cancer Screening Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Increasing Access to Lung Cancer Screening Act</b></p> <p>This bill provides for coverage without prior authorization requirements of annual lung cancer screenings under Medicaid, Medicare, and private health insurance for individuals for whom screenings are recommended under U.S. Preventive Services Task Force guidelines. It also expands Medicaid coverage of counseling and pharmacotherapy for cessation of tobacco use to all individuals, rather than only pregnant women. </p> <p>The Department of Health and Human Services must conduct outreach on the importance of lung cancer screenings and who should be screened, and the Government Accountability Office must report on the demographics of those diagnosed with lung cancer and recommend ways the federal government can improve screenings.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6178"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6178ih.xml"
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
      "title": "Increasing Access to Lung Cancer Screening Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Increasing Access to Lung Cancer Screening Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to require coverage under State plans under the Medicaid program for annual lung cancer screening with no cost sharing for individuals for whom screening is recommended by U.S. Preventive Services Task Force guidelines, to expand coverage under Medicaid of counseling and pharmacotherapy for cessation of tobacco use, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T13:18:21Z"
    }
  ]
}
```
