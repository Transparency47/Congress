# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6157
- Title: FORCE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6157
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-05-30T08:05:36Z
- Update date including text: 2026-05-30T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6157",
    "number": "6157",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FORCE Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:36Z",
    "updateDateIncludingText": "2026-05-30T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:03:45Z",
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
          "date": "2025-11-19T15:03:40Z",
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
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6157ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6157\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Panetta (for himself, Mr. Levin , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide benefits under the Medicare program for first responders at the age of 57.\n#### 1. Short title\nThis Act may be cited as the First Responders\u2019 Care Expansion Act of 2025 or the FORCE Act of 2025 .\n#### 2. Providing benefits under the Medicare program for first responders at the age of 57\n##### (a) In general\nTitle XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ) is amended by adding at the end the following new section:\n1899C. Medicare for first responders at age 57 (a) Option (1) In general Every individual who meets the requirements described in paragraph (2) shall be eligible to enroll under this section. (2) Eligibility The requirements described in this paragraph are the following: (A) Age The individual has attained 57 years of age, but has not attained 65 years of age. (B) First responder The individual has worked for a total of 10 years or longer in any occupation (or a combination of occupations) identified by any of the following codes (or successor codes) under the Standard Occupations Classification System established by the Bureau of Labor Statistics: (i) 33\u20131010. (ii) 33\u20131020. (iii) 33\u20132000. (iv) 33\u20133000 (other than any occupations identified under code 33\u20133040). (v) 33\u20139092. (C) Medicare eligibility (but for age) The individual is not otherwise entitled to benefits under part A or eligible to enroll under part A or part B but would be so entitled (or so eligible) if the individual were 65 years of age. (3) Part A, B, and D benefits and protections An individual enrolled under this section is entitled to the same benefits (and shall receive the same protections) under this title as an individual who is entitled to benefits under part A and enrolled under part B, including the ability to enroll in a prescription drug plan under part D or a Medicare Advantage plan (including such a plan that provides qualified prescription drug coverage (an MA\u2013PD plan)) and including access to the Medicare Beneficiary Ombudsman under section 1808(c). (b) Enrollment and coverage periods (1) Enrollment An individual eligible to enroll under this section may so enroll\u2014 (A) during the 1-month period prior to the individual becoming so eligible; or (B) at any time while such individual is so eligible. (2) Coverage An individual enrolled under this section shall be eligible for benefits provided under this section beginning with the first day of the first month beginning after the date such individual so enrolls and ending on the earlier of the following: (A) The date on which such individual elects to terminate enrollment under this section. (B) The date on which such individual becomes entitled to benefits under part A or eligible to enroll for benefits under part B. (c) Premium (1) Amount of monthly premiums The monthly premium payable for coverage for a month under this section for an individual is equal to\u2014 (A) the monthly premium that would apply to such individual for such month under section 1839 if such individual were enrolled under part B; plus (B) in the case of an individual who would not be entitled to benefits under part A for such month pursuant to section 226 if the individual were 65 years of age, the monthly premium that would apply to such individual for such month under section 1818 if such individual were enrolled under part A. (2) Additional premiums In the case of an individual enrolled under this section who elects to enroll in a Medicare Advantage plan under part C or a prescription drug plan under part D, the provisions of such part C or such part D, as applicable, relating to payment of premiums for individuals so enrolled shall apply to individuals enrolled under this section. (d) Payment of premiums (1) Payment Premiums for enrollment under this section shall be paid to the Secretary at such times, and in such manner, as the Secretary determines appropriate. (2) Deposit Amounts collected by the Secretary under this section shall be deposited in the Medicare First Responder Trust Fund established under subsection (e). (e) Medicare First Responder Trust Fund (1) In general There is hereby created on the books of the Treasury of the United States a trust fund to be known as the Medicare First Responder Trust Fund (in this subsection referred to as the Trust Fund ). The Trust Fund shall consist of such gifts and bequests as may be made as provided in section 201(i)(1) and such amounts as may be deposited in, or appropriated to, such fund as provided in this title. (2) Premiums Premiums collected under subsection (d) (not including any premium payable pursuant to paragraph (2) of such subsection) shall be transferred to the Trust Fund. (3) Incorporation of Provisions Subsections (b) through (i) of section 1841 shall apply with respect to the Trust Fund and this title in the same manner as they apply with respect to the Federal Supplementary Medical Insurance Trust Fund and part B, respectively, except that in applying such section 1841, any reference in such section to this part shall be construed to be a reference to this section and any reference in section 1841(h) to section 1840(d) and in section 1841(i) to sections 1840(b)(1) and 1842(g) are deemed to be references to comparable authority exercised under this section. (f) Clarification Nothing in this section shall affect the benefits or eligibility under this title of individuals who would otherwise be entitled to or eligible for benefits under this title or title XIX, or both. (g) Treatment in relation to the Affordable Care Act (1) Treatment as minimum essential coverage For purposes of applying section 5000A of the Internal Revenue Code of 1986, the coverage provided through enrollment under this section constitutes minimum essential coverage under subsection (f)(1)(A)(i) of such section. (2) Medicaid managed care States are prohibited from buying their Medicaid beneficiaries ages 57 to 64 who are eligible to enroll under this section into Medicare under this section, and individuals otherwise eligible for enrollment under a State plan under title XIX are prohibited from coverage under this title pursuant to enrollment under this section. The preceding sentence shall not apply to Medicaid beneficiaries whose Medicaid coverage or eligibility does not meet the definition of minimum essential coverage under a government-sponsored program under section 1.5000A\u20132 of title 26, Code of Federal Regulations (or any successor regulation). (3) Access to Medigap Coverage provided through medicare supplemental policies certified under section 1882 shall be made available to individuals eligible for enrollment pursuant to this section for enrollment, information, comparison, and otherwise as such a policy through any internet website described in paragraph (2). .\n##### (b) Medigap\nSection 1882 of the Social Security Act is amended by adding at the end the following new subsection:\n(aa) Development of New Standards for Certain Medicare Supplemental Policies relating to first responder coverage The Secretary shall request the National Association of Insurance Commissioners to review and revise the standards for benefit packages described in subsection (p)(1), to otherwise update standards to include requirements for each medicare supplemental policy that offers such a policy in a State, with respect to each year, to accept every individual in the State who is eligible for enrollment pursuant to section 1899C and who applies for such coverage for such year if the individual applies for enrollment in such policy during the 30-day period following the date of enrollment pursuant to section 1899C and to accept every such individual during a period of transition from enrollment pursuant to such section to enrollment under this title pursuant to eligibility other than under such section. Such revisions shall be made consistent with the rules applicable under subsection (p)(1)(E) with the reference to the 1991 NAIC Model Regulation deemed a reference to the NAIC Model Regulation as published in the Federal Register on December 4, 1998, and as subsequently updated by the National Association of Insurance Commissioners to reflect previous changes in law and the reference to date of enactment of this subsection deemed a reference to the date of enactment of this subsection (aa). .",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-11-21T13:02:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-19",
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
          "measure-id": "id119hr6157",
          "measure-number": "6157",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-19",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6157v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-11-19",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>First Responders' Care Expansion Act of 2025 or the FORCE Act of 2025</strong></p><p>This bill provides for Medicare coverage of first responders between the ages of 57 and 64 who do not otherwise already qualify for Medicare.</p>"
        },
        "title": "FORCE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6157.xml",
    "summary": {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>First Responders' Care Expansion Act of 2025 or the FORCE Act of 2025</strong></p><p>This bill provides for Medicare coverage of first responders between the ages of 57 and 64 who do not otherwise already qualify for Medicare.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6157"
    },
    "title": "FORCE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>First Responders' Care Expansion Act of 2025 or the FORCE Act of 2025</strong></p><p>This bill provides for Medicare coverage of first responders between the ages of 57 and 64 who do not otherwise already qualify for Medicare.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6157"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6157ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FORCE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "First Responders\u2019 Care Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "title": "FORCE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T10:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide benefits under the Medicare program for first responders at the age of 57.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-20T10:48:18Z"
    }
  ]
}
```
