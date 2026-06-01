# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6147?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6147
- Title: Expanding Health Care Options for First Responders Act
- Congress: 119
- Bill type: HR
- Bill number: 6147
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-04-17T08:07:08Z
- Update date including text: 2026-04-17T08:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6147",
    "number": "6147",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000601",
        "district": "1",
        "firstName": "Greg",
        "fullName": "Rep. Landsman, Greg [D-OH-1]",
        "lastName": "Landsman",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Expanding Health Care Options for First Responders Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:08Z",
    "updateDateIncludingText": "2026-04-17T08:07:08Z"
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
          "date": "2025-11-19T15:01:00Z",
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
          "date": "2025-11-19T15:00:50Z",
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
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "FL"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NJ"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6147ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6147\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Landsman introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide an option for first responders age 50 to 64 who are separated from service due to retirement or disability to buy into Medicare.\n#### 1. Short title\nThis Act may be cited as the Expanding Health Care Options for First Responders Act .\n#### 2. Medicare buy-in option for first responders 50 to 64 years of age who are separated from service due to retirement or disability\nTitle XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ) is amended by adding at the end the following new section:\n1899D. Medicare buy-in option for first responders 50 to 64 years of age who are separated from service due to retirement or disability (a) Option (1) In general Every individual who meets the requirements described in paragraph (3) shall be eligible to enroll under this section. (2) Part a, b, and d benefits An individual enrolled under this section is entitled to the same benefits (and shall receive the same protections) under this title as an individual who is entitled to benefits under part A and enrolled under parts B and D, including the ability to enroll in a Medicare Advantage plan that provides qualified prescription drug coverage (an MA\u2013PD plan). (3) Requirements for eligibility The requirements described in this paragraph are the following: (A) The individual is a resident of the United States. (B) The individual is\u2014 (i) a citizen or national of the United States; or (ii) an alien lawfully admitted for permanent residence. (C) The individual is not otherwise entitled to benefits under part A or eligible to enroll under part A or part B. (D) The individual has attained 50 years of age but has not attained 65 years of age. (E) The individual is a qualified first responder (as defined in paragraph (4)(B)). (4) Definitions In this section: (A) First responder The term first responder means\u2014 (i) a qualified law enforcement officer (as defined in section 926B(c) of title 18, United States Code); (ii) an employee described in clause (i) of section 72(t)(10)(B) of the Internal Revenue Code of 1986; or (iii) a Federal firefighter described in section 8331(21) or 8401(14) of title 5, United States Code. (B) Qualified first responder The term qualified first responder means a first responder who is separated from service due to retirement or disability. (b) Enrollment and coverage periods (1) In general The Secretary shall establish enrollment and coverage periods for individuals who enroll under this section. (2) Coordination Such periods shall be established in coordination with the enrollment and coverage periods for plans offered under an Exchange established under title I of the Patient Protection and Affordable Care Act and plans under parts C and D. If the Secretary determines appropriate, the Secretary may expand such enrollment periods beyond the enrollment periods under such an Exchange or under parts C and D. (3) Beginning of coverage and special enrollment periods The Secretary shall establish such periods so that coverage under this section shall first begin on January 1 of the first year beginning at least one year after the date of the enactment of this section and shall include special enrollment periods, in accordance with section 155.420 of title 45 of the Code of Federal Regulations, that are applicable to qualified health plans offered through an Exchange. (c) Premium (1) Amount of monthly premiums The Secretary shall (beginning for the first year that begins more than 1 year after the date of enactment of this section) determine a monthly premium for all individuals enrolled under this section. Such monthly premium shall be equal to 1\u204412 of the annual premium computed under paragraph (2)(B), which shall apply with respect to coverage provided under this section for any month in the succeeding year. (2) Annual premium (A) Combined per capita average for all medicare benefits The Secretary shall estimate the average, annual per capita amount for benefits and administrative expenses that will be payable under parts A, B, and D (including, as applicable, under part C) in the year for all individuals enrolled under this section. (B) Annual premium The annual premium under this subsection for months in a year is equal to the average, annual per capita amount estimated under subparagraph (A) for the year. (3) Increased premium for certain part c and d plans Nothing in this section shall preclude an individual from choosing a Medicare Advantage plan or a prescription drug plan which requires the individual to pay an additional amount (because of supplemental benefits or because it is a more expensive plan). In such case the individual would be responsible for the increased monthly premium. (d) Payment of premiums (1) In general Premiums for enrollment under this section shall be paid to the Secretary at such times, and in such manner, as the Secretary determines appropriate. (2) Deposit Amounts collected by the Secretary under this section shall be deposited in the Federal Hospital Insurance Trust Fund and the Federal Supplementary Medical Insurance Trust Fund (including the Medicare Prescription Drug Account within such Trust Fund) in such proportion as the Secretary determines appropriate. (e) Not eligible for medicare cost-Sharing assistance An individual enrolled under this section shall not be treated as enrolled under any part of this title for purposes of obtaining medical assistance for Medicare cost-sharing or otherwise under title XIX. (f) Treatment in relation to the affordable care act (1) Satisfaction of individual mandate For purposes of applying section 5000A of the Internal Revenue Code of 1986, the coverage provided under this section constitutes minimum essential coverage under subsection (f)(1)(A)(i) of such section 5000A. (2) Eligibility for premium assistance Coverage provided under this section\u2014 (A) shall be treated as coverage under a qualified health plan in the individual market enrolled in through the Exchange where the individual resides for all purposes of section 36B of the Internal Revenue Code of 1986 other than subsection (c)(2)(B) thereof; and (B) shall not be treated as eligibility for other minimum essential coverage for purposes of subsection (c)(2)(B) of such section 36B. The Secretary shall determine the applicable second lowest cost silver plan which shall apply to coverage under this section for purposes of section 36B of such Code. (3) Eligibility for cost-sharing subsidies For purposes of applying section 1402 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18071 )\u2014 (A) coverage provided under this section shall be treated as coverage under a qualified health plan in the silver level of coverage in the individual market offered through an Exchange; and (B) the Secretary shall be treated as the issuer of such plan. (4) Medicaid managed care States are prohibited from buying their Medicaid beneficiaries ages 50 to 64 into Medicare under this section, and individuals otherwise eligible for enrollment under a State plan under title XIX are prohibited from coverage under this title pursuant to enrollment under this section. The preceding sentence shall not apply to Medicaid beneficiaries whose Medicaid coverage or eligibility does not meet the definition of minimum essential coverage under a government-sponsored program under section 1.5000A\u20132 of title 26, Code of Federal Regulations (or any successor regulation). (5) Coordination with market reforms, etc Notwithstanding Treasury Notice 2015\u201317, no provision of law shall prevent an employer from maintaining an arrangement under which the employer pays or reimburses any portion of the premiums for coverage under this section for retired employees of the employer, or prevent such payment or reimbursement from being excluded from the gross income of the individual enrolled in such coverage for purposes of the Internal Revenue Code of 1986. (g) Guaranteed issue of medigap policies upon first enrollment and each subsequent enrollment In the case of an individual who enrolls under this section (including an individual who was previously enrolled under this section), paragraphs (2)(A), (2)(D), (3)(B)(ii), and (3)(B)(vi) of section 1882(s)\u2014 (1) shall be applied by substituting 50 for 65 ; (2) if the individual was enrolled under this section and subsequently disenrolls, shall apply each time the individual subsequently reenrolls under this section as if the individual had attained 50 years of age on the date of such reenrollment (and as if the individual had never previously enrolled in a Medicare supplemental policy); and (3) shall be applied as if this section had not been enacted (and as if the individual had never previously enrolled in a Medicare supplemental policy) when the individual attains 65 years of age. (h) Oversight There is established an advisory committee to be known as the Medicare Buy In Oversight Board to monitor and oversee the implementation of this section, including the experience of the individuals enrolling under this section. The Medicare Buy In Oversight Board shall have members that include representatives of insurers, actuaries, consumer advocacy organizations, and individuals representing the first responder community, and shall make periodic recommendations for the continual improvement of the implementation of this section as well as the relationship of enrollment under this section to other health care programs. (i) Outreach and enrollment (1) In general During the period that begins on January 1, 2027, and ends on December 31, 2029, the Secretary shall award grants to eligible entities for the following purposes: (A) Outreach and enrollment To carry out outreach, public education activities, and enrollment activities to raise awareness of the availability of, and encourage, enrollment under this section. (B) Assisting individuals\u2019 transition under this section To provide assistance to individuals to enroll under this section. (C) Raising awareness of premium assistance and cost-sharing reductions To distribute fair and impartial information concerning enrollment under this section and the availability of premium assistance tax credits under section 36B of the Internal Revenue Code of 1986 and cost-sharing reductions under section 1402 of the Patient Protection and Affordable Care Act, and to assist eligible individuals in applying for such tax credits and cost-sharing reductions. (2) Eligible entities (A) In general In this subsection, the term eligible entity means\u2014 (i) a State; (ii) a nonprofit community-based organization; or (iii) a nonprofit first responder organization. (B) Enrollment agents Such term includes a licensed independent insurance agent or broker that has an arrangement with a State, nonprofit community-based organization, or nonprofit first responder organization to enroll eligible individuals under this section. (C) Exclusions Such term does not include an entity that\u2014 (i) is a health insurance issuer; or (ii) receives any consideration, either directly or indirectly, from any health insurance issuer in connection with the enrollment of any individuals under this section. (3) Priority In awarding grants under this subsection, the Secretary shall give priority to awarding grants to States or eligible entities in States that have geographic rating areas at risk of having no qualified health plans in the individual market. (4) Funding For purposes of carrying out this subsection, there is appropriated to the Secretary, out of any moneys in the Treasury not otherwise appropriated, such sums as are necessary for calendar year 2026 and for each subsequent calendar year. (j) No effect on benefits for individuals otherwise eligible or on trust funds The Secretary shall implement the provisions of this section in such a manner to ensure that such provisions\u2014 (1) have no effect on the benefits under this title for individuals who are entitled to, or enrolled for, such benefits other than through this section; and (2) have no negative impact on the Federal Hospital Insurance Trust Fund or the Federal Supplementary Medical Insurance Trust Fund (including the Medicare Prescription Drug Account within such Trust Fund). (k) Consultation In promulgating regulations to implement this section, the Secretary shall consult with interested parties, including groups representing beneficiaries, health care providers, employers, insurance companies, and organizations representing first responders. .",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3221",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expanding Health Care Options for First Responders Act",
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
        "updateDate": "2025-12-01T19:21:20Z"
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
          "measure-id": "id119hr6147",
          "measure-number": "6147",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-19",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6147v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-11-19",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Expanding Health Care Options for First Responders Act</b></p> <p>This bill establishes a Medicare buy-in option for certain qualifying first responders.</p> <p>Specifically, the bill allows first responders aged 50 to 64 to enroll in Medicare if they are retired or otherwise separated from service due to a disability. The Centers for Medicare & Medicaid Services (CMS) must determine enrollment periods and set premiums for the buy-in option established under the bill, in accordance with specified requirements. The CMS must also award grants to states and nonprofit organizations for outreach and enrollment activities relating to the buy-in option.</p>"
        },
        "title": "Expanding Health Care Options for First Responders Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6147.xml",
    "summary": {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Expanding Health Care Options for First Responders Act</b></p> <p>This bill establishes a Medicare buy-in option for certain qualifying first responders.</p> <p>Specifically, the bill allows first responders aged 50 to 64 to enroll in Medicare if they are retired or otherwise separated from service due to a disability. The Centers for Medicare & Medicaid Services (CMS) must determine enrollment periods and set premiums for the buy-in option established under the bill, in accordance with specified requirements. The CMS must also award grants to states and nonprofit organizations for outreach and enrollment activities relating to the buy-in option.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6147"
    },
    "title": "Expanding Health Care Options for First Responders Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Expanding Health Care Options for First Responders Act</b></p> <p>This bill establishes a Medicare buy-in option for certain qualifying first responders.</p> <p>Specifically, the bill allows first responders aged 50 to 64 to enroll in Medicare if they are retired or otherwise separated from service due to a disability. The Centers for Medicare & Medicaid Services (CMS) must determine enrollment periods and set premiums for the buy-in option established under the bill, in accordance with specified requirements. The CMS must also award grants to states and nonprofit organizations for outreach and enrollment activities relating to the buy-in option.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6147"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6147ih.xml"
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
      "title": "Expanding Health Care Options for First Responders Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Health Care Options for First Responders Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide an option for first responders age 50 to 64 who are separated from service due to retirement or disability to buy into Medicare.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:48:35Z"
    }
  ]
}
```
