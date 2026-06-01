# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5081
- Title: Telehealth Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 5081
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2025-12-11T09:07:28Z
- Update date including text: 2025-12-11T09:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-02 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5081",
    "number": "5081",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Telehealth Modernization Act",
    "type": "HR",
    "updateDate": "2025-12-11T09:07:28Z",
    "updateDateIncludingText": "2025-12-11T09:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "actionDate": "2025-09-02",
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
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:03:20Z",
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
          "date": "2025-09-02T16:03:15Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5081ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5081\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Mr. Carter of Georgia (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to extend certain telehealth flexibilities under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Telehealth Modernization Act .\n#### 2. Extension of certain telehealth flexibilities\n##### (a) Removing geographic requirements and expanding originating sites for telehealth services\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended\u2014\n**(1)**\nin paragraph (2)(B)(iii), by striking ending September 30, 2025 and inserting ending September 30, 2027 ; and\n**(2)**\nin paragraph (4)(C)(iii), by striking ending on September 30, 2025 and inserting ending on September 30, 2027 .\n##### (b) Expanding practitioners eligible To furnish telehealth services\nSection 1834(m)(4)(E) of the Social Security Act ( 42 U.S.C. 1395m(m)(4)(E) ) is amended by striking ending on September 30, 2025 and inserting ending on September 30, 2027 .\n##### (c) Extending telehealth services for federally qualified health centers and rural health clinics\nSection 1834(m)(8) of the Social Security Act ( 42 U.S.C. 1395m(m)(8) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking ending on September 30, 2025 and inserting ending on September 30, 2027 ;\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nin the subparagraph heading, by inserting before fiscal year 2026 after rule ;\n**(B)**\nin clause (i), by striking during the periods for which subparagraph (A) applies and inserting before October 1, 2025 ; and\n**(C)**\nin clause (ii), by inserting furnished to an eligible telehealth individual before October 1, 2025 after telehealth services ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) Payment rule for fiscal years 2026 and 2027 (i) In general A telehealth service furnished to an eligible telehealth individual by a Federally qualified health center or rural health clinic on or after October 1, 2025, and before October 1, 2027, shall be paid as a Federally qualified health center service or rural health clinic service (as applicable) under the prospective payment system established under section 1834(o) or the methodology for all-inclusive rates established under section 1833(a)(3), respectively. (ii) Treatment of costs Costs associated with the furnishing of telehealth services by a Federally qualified health center or rural health clinic on or after October 1, 2025, and before October 1, 2027, shall be considered allowable costs for purposes of the prospective payment system established under section 1834(o) and the methodology for all-inclusive rates established under section 1833(a)(3), as applicable. .\n##### (d) Delaying in-Person requirements under Medicare for mental health services furnished through telehealth and telecommunications technology\n**(1) Delay in requirements for mental health services furnished through telehealth**\nSection 1834(m)(7)(B)(i) of the Social Security Act ( 42 U.S.C. 1395m(m)(7)(B)(i) ) is amended, in the matter preceding subclause (I), by striking on or after October 1, 2025 and inserting on or after October 1, 2027 .\n**(2) Mental health visits furnished by rural health clinics**\nSection 1834(y)(2) of the Social Security Act ( 42 U.S.C. 1395m(y)(2) ) is amended by striking October 1, 2025 and inserting October 1, 2027 .\n**(3) Mental health visits furnished by Federally qualified health centers**\nSection 1834(o)(4)(B) of the Social Security Act ( 42 U.S.C. 1395m(o)(4)(B) ) is amended by striking October 1, 2025 and inserting October 1, 2027 .\n##### (e) Allowing for the furnishing of audio-Only telehealth services\nSection 1834(m)(9) of the Social Security Act ( 42 U.S.C. 1395m(m)(9) ) is amended by striking ending on September 30, 2025 and inserting ending on September 30, 2027 .\n##### (f) Extending use of telehealth To conduct face-to-Face encounter prior to recertification of eligibility for hospice care\nSection 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ) is amended\u2014\n**(1)**\nby striking ending on September 30, 2025 and inserting ending on September 30, 2027 ; and\n**(2)**\nby inserting , except that this subclause shall not apply in the case of such an encounter with an individual occurring on or after September 30, 2025, if such individual is located in an area that is subject to a moratorium on the enrollment of hospice programs under this title pursuant to section 1866(j)(7), if such individual is receiving hospice care from a provider that is subject to enhanced oversight under this title pursuant to section 1866(j)(3), or if such encounter is performed by a hospice physician or nurse practitioner who is not enrolled under section 1866(j) and is not an opt-out physician or practitioner (as defined in section 1802(b)(6)(D)) before the semicolon.\n#### 3. Requiring modifier for use of telehealth to conduct face-to-face encounter prior to recertification of eligibility for hospice care\nSection 1814(a)(7)(D)(i)(II) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(D)(i)(II) ), as amended by section 2(f), is further amended by inserting , but only if, in the case of such an encounter occurring on or after January 1, 2026, any hospice claim includes 1 or more modifiers or codes (as specified by the Secretary) to indicate that such encounter was conducted via telehealth after as determined appropriate by the Secretary .\n#### 4. Extending acute hospital care at home waiver flexibilities\n##### (a) In general\nSection 1866G(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc\u20137(a)(1) ) is amended by striking 2025 and inserting 2030 .\n##### (b) Requiring additional study and report on acute hospital care at home waiver flexibilities\nSection 1866G of the Social Security Act ( 42 U.S.C. 1395cc\u20137 ), as amended by subsection (a), is further amended\u2014\n**(1)**\nin subsection (b), in the subsection heading, by striking Study and inserting Initial study ;\n**(2)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively; and\n**(3)**\nby inserting after subsection (b) the following new subsection:\n(c) Subsequent study and report (1) In general Not later than September 30, 2028, the Secretary shall conduct a study to\u2014 (A) analyze, to the extent practicable, the criteria established by hospitals under the Acute Hospital Care at Home initiative to determine which individuals may be furnished services under such initiative; and (B) analyze and compare (both within and between hospitals participating in the initiative, and relative to comparable hospitals that do not participate in the initiative, for relevant parameters such as diagnosis-related groups)\u2014 (i) quality of care furnished to individuals with similar conditions and characteristics in the inpatient setting and through the Acute Hospital Care at Home initiative, including health outcomes, hospital readmission rates (including readmissions both within and beyond 30 days post-discharge), hospital mortality rates, length of stay, infection rates, composition of care team (including the types of labor used, such as contracted labor), the ratio of nursing staff, transfers from the hospital to the home, transfers from the home to the hospital (including the timing, frequency, and causes of such transfers), transfers and discharges to post-acute care settings (including the timing, frequency, and causes of such transfers and discharges), and patient and caregiver experience of care; (ii) clinical conditions treated and diagnosis-related groups of discharges from inpatient settings relative to discharges from the Acute Hospital Care at Home initiative; (iii) costs incurred by the hospital for furnishing care in inpatient settings relative to costs incurred by the hospital for furnishing care through the Acute Hospital Care at Home initiative, including costs relating to staffing, equipment, food, prescriptions, and other services, as determined by the Secretary; (iv) the quantity, mix, and intensity of services (such as in-person visits and virtual contacts with patients and the intensity of such services) furnished in inpatient settings relative to the Acute Hospital Care at Home initiative, and, to the extent practicable, the nature and extent of family or caregiver involvement; (v) socioeconomic information on individuals treated in comparable inpatient settings relative to the initiative, including racial and ethnic data, income, housing, geographic proximity to the brick-and-mortar facility and whether such individuals are dually eligible for benefits under this title and title XIX; and (vi) the quality of care, outcomes, costs, quantity and intensity of services, and other relevant metrics between individuals who entered into the Acute Hospital Care at Home initiative directly from an emergency department compared with individuals who entered into the Acute Hospital Care at Home initiative directly from an existing inpatient stay in a hospital. (2) Selection bias In conducting the study under paragraph (1), the Secretary shall, to the extent practicable, analyze and compare individuals who participate and do not participate in the initiative controlling for selection bias or other factors that may impact the reliability of data. (3) Report Not later than September 30, 2028, the Secretary of Health and Human Services shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report on the study conducted under paragraph (1). .\n#### 5. Enhancing certain program integrity requirements for DME under Medicare\n##### (a) Durable medical equipment\n**(1) In general**\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ) is amended by adding at the end the following new paragraph:\n(23) Master List inclusion and claim review for certain items (A) Master List inclusion Beginning January 1, 2028, for purposes of the Master List described in section 414.234(b) of title 42, Code of Federal Regulations (or any successor regulation), an item for which payment may be made under this subsection shall be treated as having aberrant billing patterns (as such term is used for purposes of such section) if the Secretary determines that, without explanatory contributing factors (such as furnishing emergent care services), a substantial number of claims for such items under this subsection are for such items ordered by a physician or practitioner who has not previously (during a period of not less than 24 months, as established by the Secretary) furnished to the individual involved any item or service for which payment may be made under this title. (B) Claim review With respect to items furnished on or after January 1, 2028, that are included on the Master List pursuant to subparagraph (A) , if such an item is not subject to a determination of coverage in advance pursuant to paragraph (15)(C), the Secretary may conduct prepayment review of claims for payment for such item. .\n**(2) Conforming amendment for prosthetic devices, orthotics, and prosthetics**\nSection 1834(h)(3) of the Social Security Act ( 42 U.S.C. 1395m(h)(3) ) is amended by inserting , and paragraph (23) of subsection (a) shall apply to prosthetic devices, orthotics, and prosthetics in the same manner as such provision applies to items for which payment may be made under such subsection before the period at the end.\n##### (b) Report on identifying clinical diagnostic laboratory tests at high risk for fraud and effective mitigation measures\nNot later than January 1, 2026, the Inspector General of the Department of Health and Human Services shall submit to Congress a report assessing fraud risks relating to claims for clinical diagnostic laboratory tests for which payment may be made under section 1834A of the Social Security Act ( 42 U.S.C. 1395m\u20131 ) and effective tools for reducing such fraudulent claims. The report may include information regarding\u2014\n**(1)**\nwhich, if any, clinical diagnostic laboratory tests are identified as being at high risk of fraudulent claims, and an analysis of the factors that contribute to such risk;\n**(2)**\nwith respect to a clinical diagnostic laboratory test identified under paragraph (1) as being at high risk of fraudulent claims\u2014\n**(A)**\nthe amount payable under such section 1834A with respect to such test;\n**(B)**\nthe number of such tests furnished to individuals enrolled under part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. );\n**(C)**\nwhether an order for such a test was more likely to come from a provider with whom the individual involved did not have a prior relationship, as determined on the basis of prior payment experience; and\n**(D)**\nthe frequency with which a claim for payment under such section 1834A included the payment modifier identified by code 59 or 91;\n**(3)**\nsuggested strategies for reducing the number of fraudulent claims made with respect to tests so identified as being at high risk, including\u2014\n**(A)**\nan analysis of whether the Centers for Medicare & Medicaid Services can detect aberrant billing patterns with respect to such tests in a timely manner;\n**(B)**\nany strategies for identifying and monitoring the providers who are outliers with respect to the number of such tests that such providers order; and\n**(C)**\ntargeted education efforts to mitigate improper billing for such tests; and\n**(4)**\nsuch other information as the Inspector General determines appropriate.\n#### 6. Guidance on furnishing services via telehealth to individuals with limited English proficiency\n##### (a) In general\nNot later than 1 year after the date of the enactment of this section, the Secretary of Health and Human Services, in consultation with 1 or more entities from each of the categories described in paragraphs (1) through (7) of subsection (b) , shall issue and disseminate, or update and revise as applicable, guidance for the entities described in such subsection on the following:\n**(1)**\nBest practices on facilitating and integrating use of interpreters during a telemedicine appointment.\n**(2)**\nBest practices on providing accessible instructions on how to access telecommunications systems (as such term is used for purposes of section 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) )) for individuals with limited English proficiency.\n**(3)**\nBest practices on improving access to digital patient portals for individuals with limited English proficiency.\n**(4)**\nBest practices on integrating the use of video platforms that enable multi-person video calls furnished via a telecommunications system for purposes of providing interpretation during a telemedicine appointment for an individual with limited English proficiency.\n**(5)**\nBest practices for providing patient materials, communications, and instructions in multiple languages, including text message appointment reminders and prescription information.\n##### (b) Entities described\nFor purposes of subsection (a) , an entity described in this subsection is an entity in 1 or more of the following categories:\n**(1)**\nHealth information technology service providers, including\u2014\n**(A)**\nelectronic medical record companies;\n**(B)**\nremote patient monitoring companies; and\n**(C)**\ntelehealth or mobile health vendors and companies.\n**(2)**\nHealth care providers, including\u2014\n**(A)**\nphysicians; and\n**(B)**\nhospitals.\n**(3)**\nHealth insurers.\n**(4)**\nLanguage service companies.\n**(5)**\nInterpreter or translator professional associations.\n**(6)**\nHealth and language services quality certification organizations.\n**(7)**\nPatient and consumer advocates, including such advocates that work with individuals with limited English proficiency.\n#### 7. In-home cardiopulmonary rehabilitation flexibilities\n##### (a) In general\nSection 1861(eee)(2) of the Social Security Act ( 42 U.S.C. 1395x(eee)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)(ii), by inserting (including, with respect to items and services furnished through audio and video real-time communications technology (excluding audio-only) on or after September 30, 2025, and before January 1, 2027, in the home of an individual who is an outpatient of the hospital) after outpatient basis ; and\n**(2)**\nin subparagraph (B), by inserting (including, with respect to items and services furnished through audio and video real-time communications technology on or after September 30, 2025, and before January 1, 2027, the virtual presence of such physician, physician assistant, nurse practitioner, or clinical nurse specialist) after under the program .\n##### (b) Program instruction authority\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by this section by program instruction or otherwise.\n#### 8. Inclusion of virtual diabetes prevention program suppliers in MDPP Expanded Model\n##### (a) In general\nNot later than January 1, 2026, the Secretary shall revise the regulations under parts 410 and 424 of title 42, Code of Federal Regulations, to provide that, for the period beginning January 1, 2026, and ending December 31, 2030\u2014\n**(1)**\nan entity may participate in the MDPP by offering only online MDPP services via synchronous or asynchronous technology or telecommunications if such entity meets the conditions for enrollment as an MDPP supplier (as specified in section 424.205(b) of title 42, Code of Federal Regulations (or a successor regulation));\n**(2)**\nif an entity participates in the MDPP in the manner described in paragraph (1) \u2014\n**(A)**\nthe administrative location of such entity shall be the address of the entity on file under the Diabetes Prevention Recognition Program; and\n**(B)**\nin the case of online MDPP services furnished by such entity to an MDPP beneficiary who was not located in the same State as the entity at the time such services were furnished, the entity shall not be prohibited from submitting a claim for payment for such services solely by reason of the location of such beneficiary at such time; and\n**(3)**\nno limit is applied on the number of times an individual may enroll in the MDPP.\n##### (b) Definitions\nIn this section:\n**(1) MDPP**\nThe term MDPP means the Medicare Diabetes Prevention Program conducted under section 1115A of the Social Security Act ( 42 U.S.C. 1315a ), as described in the final rule published in the Federal Register entitled Medicare and Medicaid Programs; CY 2024 Payment Policies Under the Physician Fee Schedule and Other Changes to Part B Payment and Coverage Policies; Medicare Shared Savings Program Requirements; Medicare Advantage; Medicare and Medicaid Provider and Supplier Enrollment Policies; and Basic Health Program (88 Fed. Reg. 78818 (November 16, 2023)) (or a successor regulation).\n**(2) Regulatory terms**\nThe terms Diabetes Prevention Recognition Program , full CDC DPRP recognition , MDPP beneficiary , MDPP services , and MDPP supplier have the meanings given each such term in section 410.79(b) of title 42, Code of Federal Regulations.\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.",
      "versionDate": "2025-09-02",
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
        "actionDate": "2025-09-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2709",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Telehealth Modernization Act",
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
        "updateDate": "2025-09-22T15:32:22Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5081ih.xml"
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
      "title": "Telehealth Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-04T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Telehealth Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-04T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to extend certain telehealth flexibilities under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-04T04:48:23Z"
    }
  ]
}
```
