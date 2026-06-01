# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8487
- Title: Ensuring Excellence in Mental Health Act
- Congress: 119
- Bill type: HR
- Bill number: 8487
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-19T20:12:51Z
- Update date including text: 2026-05-19T20:12:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-23 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8487",
    "number": "8487",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Ensuring Excellence in Mental Health Act",
    "type": "HR",
    "updateDate": "2026-05-19T20:12:51Z",
    "updateDateIncludingText": "2026-05-19T20:12:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:03:50Z",
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
          "date": "2026-04-23T13:03:45Z",
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
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "MN"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "MO"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8487ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8487\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Ms. Matsui (for herself, Mr. Pfluger , Ms. Craig , Mr. Alford , Mr. Tonko , Mr. Fitzpatrick , and Mr. Goldman of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to adjust coverage and payment for certified community behavioral health clinic services under the Medicare and Medicaid programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Excellence in Mental Health Act .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title.\nSec.\u20022.\u2002Table of contents.\nTitle I\u2014Strengthening and providing cost-related payment for certified community behavioral health clinics under the Medicaid program\nSec.\u2002101.\u2002Coordination of Medicaid certified community behavioral health clinic services with CCBHC operating grant program; CCBHC accreditation option.\nSec.\u2002102.\u2002Establishing a prospective payment system for certified community behavioral health clinics.\nSec.\u2002103.\u2002Expanding CCBHC services within Medicaid demonstration program.\nSec.\u2002104.\u2002Expanding scope of CCBHC services covered under the Medicaid program.\nTitle II\u2014Coverage of certified community behavioral health clinic services under the Medicare program\nSec.\u2002201.\u2002Coverage of certified community behavioral health clinic services under the medicare program.\nSec.\u2002202.\u2002Payment for certified community behavioral health clinic services under the medicare program.\nSec.\u2002203.\u2002Non-application of Medicare part B deductible for CCBHC services.\nSec.\u2002204.\u2002Right to seek review of cost reports from Provider Reimbursement Review Board.\nSec.\u2002205.\u2002Extending safe harbor under Anti-Kickback Statute to waivers of CCBHC coinsurance.\nSec.\u2002206.\u2002Effective date.\nTitle III\u2014Community behavioral health clinic grants\nSec.\u2002301.\u2002Operating grants, technical assistance, data infrastructure, and accreditation for community behavioral health clinics.\nTitle IV\u2014Liability protection for certified community behavioral health clinic clinicians\nSec.\u2002401.\u2002Conferring protection under the Federal Tort Claims Act to clinicians in certified community behavioral health clinics.\nI\nStrengthening and providing cost-related payment for certified community behavioral health clinics under the Medicaid program\n#### 101. Coordination of Medicaid certified community behavioral health clinic services with CCBHC operating grant program; CCBHC accreditation option\nSection 1905(jj)(2) of the Social Security Act ( 42 U.S.C. 1396d(jj)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B)\u2014\n**(A)**\nby inserting (or providing or referring through formal relationships, as applicable) after furnishing ;\n**(B)**\nby striking described in paragraph (1) and inserting described in paragraph (1)(B) ; and\n**(C)**\nby striking and at the end;\n**(2)**\nin subparagraph (C), by striking the period at the end and inserting , and including any such data as the State, by agreement with the Secretary, shall access via the system described in section 340J\u20133 of the Public Health Service Act; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(D) beginning January 1, 2026, at the option of the State, has received accreditation by an accreditation body approved under section 340J\u20134 of the Public Health Service Act. .\n#### 102. Establishing a prospective payment system for certified community behavioral health clinics\n##### (a) In general\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended by adding at the end the following new subsection:\n(yy) Payment for services provided by certified community behavioral health clinics (1) In general Beginning with fiscal year 2026 with respect to services furnished on or after January 1, 2026, and for each succeeding fiscal year, if a State elects to make medical assistance available for certified community behavioral health clinic services under section 1905(a)(31), the State plan shall provide for payment for such services furnished by (or under arrangement with) a certified community behavioral health clinic described in section 1905(jj)(2) (in this subsection referred to as a clinic ) in accordance with the provisions of this subsection. (2) Prospective payment system (A) In general Subject to paragraph (4), a State shall provide for payment for certified community behavioral health clinic services furnished by (or under arrangement with) a clinic in the first fiscal year (or portion of a fiscal year) described in paragraph (1) for which a State elects to provide medical assistance for such services under section 1905(a)(31) under a prospective payment system developed by the State in accordance with this paragraph. (B) Unit of payment In establishing the system under subparagraph (A), the State shall apply as the unit of service\u2014 (i) daily visits; or (ii) monthly visits (excluding repeat visits from the same individual). (C) System design Under the system under subparagraph (A), the State may, consistent with the methodology described in guidance issued under section 223(b) of the Protecting Access to Medicare Act of 2014\u2014 (i) establish separate prospective payment system rates for special populations; (ii) use a system of outlier payments for a portion of costs of furnishing certified community behavioral health clinic services; or (iii) with respect to certified community behavioral health clinic services that are crisis services\u2014 (I) require that each cost report of a clinic segregate costs relating to mobile crisis teams, emergency crisis intervention services, or crisis stabilization from other components of the services described in section 1905(a)(31); and (II) provide for a prospective payment system rate for any or all of such crisis services that is distinct from the rate encompassing the remainder of the services described in section 1905(a)(31). (D) Payment basis Subject to subparagraph (E) , the State shall provide for computation of a prospective payment amount for an individual certified community behavioral health clinic under the system under subparagraph (A) as follows: (i) For the first fiscal year (or portion of a fiscal year) for which a State elects to provide medical assistance for such services under section 1905(a)(31), such amount\u2014 (I) in the case of a State that did not operate a demonstration program under section 223 of the Protecting Access to Medicare Act of 2014 during a base year corresponding to the fiscal year immediately preceding such first fiscal year (or portion of a fiscal year), shall be equal to 100 percent of the costs of the clinic which are reasonable and related to the furnishing of such services during such base year; and (II) in the case of a State that did operate a demonstration program under section 223 of the Protecting Access to Medicare Act of 2014 during such base year, shall be equal to, at the option of the State\u2014 (aa) the amount described in subclause (I) ; or (bb) the amount that would have otherwise applied with respect to such services under such demonstration. (ii) For each subsequent fiscal year for which a State elects to provide medical assistance for such services under section 1905(a)(31), such amount shall be, subject to subparagraph (F) , the amount calculated under this subparagraph for the preceding fiscal year\u2014 (I) increased by the percentage increase described in section 1834(aa)(3)(C) for the calendar year in which such preceding fiscal year began; and (II) adjusted to take into account any increase or decrease in the scope of such services furnished by the clinic during the fiscal year involved. (E) Establishment of initial fiscal year payment for new clinics For purposes of subparagraph (D) \u2014 (i) in the case of a certified community behavioral health clinic that does not have available complete actual cost data representing the provision of all certified community behavioral health clinic services provided in the base year described in clause (i)(I) of such subparagraph, the State may use estimated or projected data relating to specific services for which the clinics lack cost experience; and (ii) in the case of an entity that first enrolls under this title as a certified community behavioral health clinic in a year after the first fiscal year in which the State first provides for payment for the services described in section 1905(a)(31) in accordance with paragraph (1) \u2014 (I) for the first fiscal year in which the clinic furnishes such services, the amount determined by the State for such clinic shall be\u2014 (aa) determined on the basis of the amounts established under this paragraph for other such clinics located in the same or adjacent area (as defined by the Secretary) with a similar case load; or (bb) in the absence of any such clinic, based on the reasonable projected costs per visit of the clinic; (II) for the second fiscal year in which the clinic furnishes such services, the amount determined by the State for such clinic shall be determined under clause (i)(I) of such subparagraph on the basis of the reasonable and related costs and visits from the clinic\u2019s first fiscal year of operation; and (III) for the third and each subsequent fiscal year in which the clinic furnishes such services, the amount determined by the State for such clinic shall be determined under clause (ii) of such subparagraph. (F) Rebasing A State may periodically (but no less frequently than every third fiscal year after the first fiscal year described in subparagraph (D) ) rebase the prospective payment amount determined under subparagraph (D) such that costs from the fiscal year preceding the rebasing year, rather than costs from the base year described in clause (i)(I) of such subparagraph, shall be used in establishing a new cost-related rate for each clinic. Such rebasing shall include those clinics with initial rates determined under subparagraph (E) . (3) Administration in the case of managed care (A) In general In the case of services furnished by a certified community behavioral health clinic pursuant to a contract between the clinic and a managed care entity (as defined in section 1932(a)(1)(B)) or other specified entity (as defined in 1903(m)(9)(D)(iii)), the State shall provide for payment to the clinic by the State of a supplemental payment equal to the amount (if any) by which the amount determined under the preceding paragraphs of this subsection (or paragraph (4), as applicable) exceeds the amount of payments provided under the contract. Such supplemental payment shall be made pursuant to a payment schedule agreed to by the State and the clinic, but in no case less frequently than every 4 months. (B) Option to delegate PPS payment to managed care entities through an alternative payment methodology Notwithstanding subparagraph (A), nothing in this subsection shall be interpreted to preclude a State from amending its State plan to provide for an alternative payment methodology under paragraph (4), under which the State may delegate to a managed care entity, as defined in section 1932(a)(1)(B), the responsibility to pay the clinic at least the rate determined under the preceding subparagraphs (or paragraph (4), as applicable), provided that the State shall meet all requirements described in paragraph (4), and shall use oversight processes to ensure that each clinic is paid at least the amounts required under the preceding paragraphs of this subsection. (4) Alternative payment methodologies Notwithstanding any other provision of this subsection, the State plan may provide for payment in any fiscal year to a certified community behavioral health clinic for services described in paragraph (31) of section 1905(a) in an amount which is determined under an alternative payment methodology that\u2014 (A) is agreed to by the State and the clinic; and (B) results in payment to the clinic of an amount which is not less than the amount otherwise required to be paid to the clinic under this subsection. .\n##### (b) Requirement To use prospective payment system under benchmark or benchmark equivalent coverage\nSection 1937(b)(4) of the Social Security Act ( 42 U.S.C. 1396u\u20137(b)(4) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting ; coverage of CCBHC services after FQHC services ;\n**(2)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(3)**\nby striking this section, a State and inserting:\nthis section\u2014 (A) a State ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(B) in the case that a State provides for medical assistance for certified community behavioral health clinic services (as defined in section 1905(jj)(1)) through enrollment of an individual with benchmark coverage or benchmark equivalent coverage under this section, payment for such services shall be made in accordance with the requirements of section 1902(yy). .\n#### 103. Expanding CCBHC services within Medicaid demonstration program\n##### (a) Additional services within demonstration program\nSection 223 of the Protecting Access to Medicare Act of 2014 ( 42 U.S.C. 1396a note) is amended\u2014\n**(1)**\nin section (a)(2)(D)\u2014\n**(A)**\nby redesignating clauses (i) through (ix) as subclauses (I) through (IX), respectively, and adjusting the margins accordingly;\n**(B)**\nby striking Provision and all that follows through relationships with other providers: and inserting:\n(i) In general Provision (in a manner reflecting person-centered care) of\u2014 (I) the required CCBHC services (as defined in clause (ii)); and (II) the additional CCBHC services (as defined in clause (iii)). (ii) Required CCBHC services For purposes of clause (i), the term required CCBHC services means any of the following services which, if not available directly through the certified community behavioral health clinic, are provided or referred through formal relationships with other providers: ; and\n**(C)**\nby adding at the end the following new clause:\n(iii) Additional CCBHC services For purposes of clause (i), the term additional CCBHC services means services available directly through the certified community behavioral health clinic\u2014 (I) that are not required CCBHC services (as defined in clause (ii)); (II) that are appropriate to meet the health needs of the population served; and (III) which may include any of the primary health services defined in section 330 (b)(1)(A) of the Public Health Service Act. ;\n**(2)**\nin subsection (b)(1), by striking mental health services and inserting certified community behavioral health clinic services ; and\n**(3)**\nin subsection (e)\u2014\n**(A)**\nby redesignating paragraphs (1) through (4) as paragraphs (2) through (5), respectively; and\n**(B)**\nby inserting before paragraph (2), as so redesignated, the following new paragraph:\n(1) Certified community behavioral health clinic services The term certified community behavioral health clinic services means\u2014 (A) required CCBHC services (as defined in subsection (a)(2)(D)(ii)); and (B) additional CCBHC services (as defined in subsection (a)(2)(D)(iii)), to the extent that a certified community behavioral health clinic elects to furnish any such services. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to services furnished on or after October 1, 2026.\n#### 104. Expanding scope of CCBHC services covered under the Medicaid program\n##### (a) Additional services within CCBHC benefit\nSection 1905(jj) of the Social Security Act ( 42 U.S.C. 1396d(jj) ) is amended\u2014\n**(1)**\nin the subsection heading, by inserting ; certified community behavioral health clinic after Certified community behavioral health clinic services ; and\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin the paragraph heading, by striking In general and inserting Certified community behavioral health clinic services ;\n**(B)**\nby redesignating subparagraphs (A) through (I) as clauses (i) through (ix), respectively, and adjusting the margins accordingly;\n**(C)**\nby striking The term and all that follows through relationships with other providers: and inserting:\n(A) In general The term certified community behavioral health clinic services means\u2014 (i) the required CCBHC services (as defined in subparagraph (B)); and (ii) the additional CCBHC services (as defined in subparagraph (C)). (B) Required CCBHC services For purposes of subparagraph (A), the term required CCBHC services means any of the following services when furnished to an individual as a patient of a certified community behavioral health clinic (as defined in paragraph (2)), in a manner reflecting person-centered care and which, if not available directly through a certified community behavioral health clinic, may be provided or referred through formal relationships with other providers: ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(C) Additional CCBHC services For purposes of subparagraph (A), the term additional CCBHC services means services furnished to an individual as a patient of a certified community behavioral health clinic (as defined in paragraph (2)), in a manner reflecting person-centered care\u2014 (i) that are not required CCBHC services under subparagraph (B); (ii) that are appropriate to meet the health needs of the population served; and (iii) which may include any of the primary health services defined in section 330(b)(1) of the Public Health Service Act. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to services furnished on or after October 1, 2026.\nII\nCoverage of certified community behavioral health clinic services under the Medicare program\n#### 201. Coverage of certified community behavioral health clinic services under the medicare program\n##### (a) Coverage\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (JJ), by adding and at the end; and\n**(2)**\nby adding at the end the following new subparagraph:\n(KK) certified community behavioral health clinic services (as defined in subsection (aa)(8)) furnished on or after January 1, 2027. .\n##### (b) Definitions\nSection 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin the heading, by striking and Federally Qualified Health Center Services and inserting , Federally qualified health center services, and certified community behavioral health clinic services ; and\n**(2)**\nby adding at the end the following new paragraph:\n(8) The terms certified community behavioral health clinic services and certified community behavioral health clinic have the meaning given each such term in section 1905(jj). .\n#### 202. Payment for certified community behavioral health clinic services under the medicare program\n##### (a) In general\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(1)**\nby striking and (HH) and inserting (HH) ; and\n**(2)**\nby inserting before the semicolon at the end the following: , and (II) with respect to certified community behavioral health clinic services (as defined in section 1861(aa)(8)), the amounts paid shall be equal to 80 percent of the lesser of the actual charge or the amount determined under section 1834(aa) .\n##### (b) Development and implementation of prospective payment system\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Development and implementation of prospective payment system for certified community behavioral health clinics (1) In general The Secretary shall develop a prospective payment system for payment to certified community behavioral health clinic services (as defined in section 1861(aa)(8)) furnished by certified community behavioral health clinics (as defined in such section) under this title. In establishing such system, the Secretary\u2014 (A) shall take into account the type, intensity, and duration of services furnished by certified community behavioral health clinics; and (B) may incorporate such adjustments, including geographic adjustments, as the Secretary determines appropriate. (2) Unit of payment In establishing a prospective payment amount under the system under this subsection, the Secretary shall consider an appropriate unit of service and a general system design that provides for continued access to quality services. (3) Payment basis Under the system under this subsection, the Secretary shall provide for computation of a prospective payment amount for services furnished during a year as follows: (A) For 2027, such amount shall be based on the average costs of such clinics which are reasonable (as determined without the application of a per visit payment limit or productivity screen and prior to the application of section 1866(a)(2)(A)(ii)) and related to the furnishing of the services described in section 1905(jj)(1)(B), as determined on the basis of the most current audited cost report data for 2 consecutive fiscal years available to the Secretary. In the absence of complete actual cost data representing the provision of such services during the relevant fiscal years, certified community behavioral health clinics may, at the Secretary\u2019s discretion, submit estimated or projected data relating to specific services. (B) For 2028, such amount shall be equal to the amount determined under subparagraph (A) , increased by the percentage increase in the MEI (as defined in section 1842(i)(3)) for the year involved. (C) For 2029 and each subsequent year, such amount shall be equal to the amount determined under this paragraph for the preceding year, increased by the percentage increase in a market basket of certified community behavioral health clinic services designed by the Secretary (or, if such an index is not available, by the percentage increase in the federally-qualified health center market basket (as described in section 1834(o)(2)(B)(ii)(II))) for the year involved. (4) Periodic reevaluation of rates The Secretary may, from time to time, adjust the amounts that would otherwise be applicable under paragraph (3) for a year by a percentage determined appropriate by the Secretary to reflect such factors as changes in the intensity of services furnished within a unit of service, the average cost of providing care per unit of service, and other factors that the Secretary considers to be relevant. Such adjustment shall be made before the update under paragraph (2)(C) has been applied for the year. .\n#### 203. Non-application of Medicare part B deductible for CCBHC services\nSection 1833(b)(4) of the Social Security Act ( 42 U.S.C. 1395l(b)(4) ) is amended by inserting or certified community behavioral health clinic services after such deductible shall not apply to Federally qualified health center services .\n#### 204. Right to seek review of cost reports from Provider Reimbursement Review Board\nSection 1878(j) of the Social Security Act ( 42 U.S.C. 1395oo(j) ) is amended by striking and a Federally qualified health center and inserting , a Federally qualified health center, and a certified community behavioral health clinic .\n#### 205. Extending safe harbor under Anti-Kickback Statute to waivers of CCBHC coinsurance\nSection 1128B(b)(3)(D) of the Social Security Act (42 U.S.C. 1320a\u20137b(b)(3)(D)) is amended by inserting or a certified community behavioral health clinic after Federally qualified health care center .\n#### 206. Effective date\nThe amendments made by this title shall apply with respect to services furnished on or after January 1, 2026.\nIII\nCommunity behavioral health clinic grants\n#### 301. Operating grants, technical assistance, data infrastructure, and accreditation for community behavioral health clinics\nPart D of title III of the Public Health Service Act ( 42 U.S.C. 254b et seq. ) is amended by adding at the end the following new subpart:\nXIII Community behavioral health clinics 340J. Definitions In this subpart: (1) Certified community behavioral health clinic The term certified community behavioral health clinic has the meaning given such term in section 1905(jj)(2) of the Social Security Act. (2) Certified community behavioral health clinic services The term certified community behavioral health clinic services has the meaning given such term in section 1905(jj)(1) of the Social Security Act. 340J\u20131. Operating grants for community behavioral health clinics (a) In general The Secretary shall establish a grant program under which the Secretary shall award grants to eligible community behavioral health clinics to provide (in a manner reflecting person-centered care) certified community behavioral health clinic services that are required CCBHC services (as defined in section 1905(jj)(1)(B) of the Social Security Act). (b) Eligibility; selection (1) Eligibility An entity is eligible to receive a grant under subsection (a) if such entity is\u2014 (A) a certified community behavioral health clinic; or (B) a community behavioral health clinic that indicates in the grant application that the clinic will use the grant funds to meet the criteria established by the Secretary under section 223(a) of the Protecting Access to Medicare Act of 2014 as of March 2023, and any subsequent updates to such criteria. (2) Selection In selecting eligible entities to receive a grant under subsection (a), the Secretary\u2014 (A) may elect to impose as a condition for the receipt of a grant under this section that the entity be accredited, per section 340J\u20134(a); (B) may award a grant to an entity described in paragraph (1)(B) that specializes in providing services to children, youth, or veterans, if such entity demonstrates to the satisfaction of the Secretary that the entity can ensure access to care for all individuals in the relevant community served by the entity through referral or other formal arrangements with other providers of services; and (C) may establish additional conditions for the receipt of a grant under this section to\u2014 (i) ensure improved geographic distribution of community behavioral health clinics; (ii) prioritize the awarding of grants to eligible entities that serve communities with elevated behavioral health needs; (iii) prioritize eligible entities that are prepared to offer all required CCBHC services (as defined in section 1905(jj)(1)(B) of the Social Security Act); and (iv) ensure consistency in planning with State CCBHC programs. (c) Use of funds An eligible entity that receives a grant under subsection (a)\u2014 (1) shall use the grant funds\u2014 (A) to provide certified community behavioral health clinic services; and (B) in the case of an entity described in subparagraph (B) of subsection (b)(1), to meet the criteria described in such subparagraph; and (2) may use the grant funds\u2014 (A) to carry out other activities that\u2014 (i) reduce costs associated with the provision of certified community behavioral health clinic services; (ii) improve access to, and availability of, certified community behavioral health clinic services provided to individuals in the relevant community served by the community behavioral health clinic; (iii) enhance the quality and coordination of certified community behavioral health clinic services; or (iv) otherwise improve the health status of communities; and (B) to pay for\u2014 (i) the costs of acquiring and leasing buildings and equipment (including the costs of amortizing the principal of, and paying interest on, loans); (ii) costs relating to the purchase or lease of equipment, including data and information systems and behavioral health information technology to facilitate data reporting and other purposes; (iii) the costs of in-service staff training and other operational or infrastructure costs as the Secretary determines appropriate; or (iv) costs associated with expanding and modernizing existing buildings or constructing new buildings (including the costs of amortizing the principal of, and paying the interest on, loans), if such costs are specifically allowed for in the grant opportunity published by the Secretary. (d) Use of nongrant funds Amounts described in subsection (g)(1)(B), including any such funds in excess of those estimated under such subsection, shall be used as permitted under this section, and may be used for such other purposes as are not specifically prohibited under this section if such use furthers the objectives of the grant. (e) Term Grants awarded under subsection (a) shall be for a period of not more than 5 years. (f) Condition on receipt of funds The Secretary may not award a grant to an eligible entity under subsection (a) unless the entity provides assurances to the Secretary that, not later than 120 days after receiving notice that the entity has been selected under subsection (b)(2) to receive a grant, the entity will submit to the Secretary for approval an implementation plan that describes how the entity will\u2014 (1) provide certified community behavioral health clinic services; and (2) in the case of an entity described in subparagraph (B) of subsection (b)(1), to meet the criteria described in such subparagraph. (g) Amount of grant (1) In general Subject to paragraph (2), in determining the amount of a grant made in any fiscal year to an eligible entity under subsection (a), the Secretary shall take into account information provided by the entity with respect to the following: (A) The total State, local, and other operational funding provided to the entity for such fiscal year. (B) The fees, premiums, and third-party reimbursements that the entity reasonably expects to receive for items and services furnished during such fiscal year. (C) The costs to the entity of meeting the purposes and requirements of the grant program under this section during such fiscal year, as estimated by the Secretary based upon the anticipated costs to the entity of\u2014 (i) providing certified community behavioral health clinic services, including the anticipated costs of providing any individual certified community behavioral health service that the entity does not have experience providing at the time of submitting an application for such grant; and (ii) in the case of an entity described in subparagraph (B) of subsection (b)(1), meeting the criteria described in such subparagraph. (2) Payments The Secretary may award grants under subsection (a) in such form and manner as the Secretary determines appropriate (including by making grant amounts available in advance or through reimbursement, and including by making such amounts available in installments), and may adjust grant amounts to account for overpayments or underpayments. (h) Use of accreditation in monitoring grant progress Regardless of whether the Secretary elects under subsection (b) to use accreditation under section 340J\u20134(a) as a condition for the award of a grant under subsection (a), the Secretary may take such accreditation into account in determining whether an entity receiving such a grant is providing the services described in subsection (a) and, if applicable, meeting such criteria as are described in subsection (b)(2). (i) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section $552,500,000 for each of fiscal years 2026 through 2030. (2) Maintenance of funding The amount made available under paragraph (1) shall supplement (and not supplant) any other Federal funding made available for certified community behavioral health clinics. (j) Guidance for clinics serving specialized populations Not later than 1 year after the date of enactment of this section, the Secretary shall publish guidance clarifying how certified community behavioral health clinics that focus on distinct populations, such as children, youth, or veterans, may meet any relevant requirement to furnish appropriate treatment to all individuals. Such guidance shall not affect such clinics\u2019 qualification to participate in the demonstration program under section 223(d) of the Protecting Access to Medicare Act of 2014 or to furnish the services described under section 1905(a)(31) of the Social Security Act. 340J\u20132. Technical assistance (a) In general Not later than 180 days after the date of enactment of the Ensuring Excellence in Mental Health Act, the Secretary shall establish a program or programs through which the Secretary shall provide (either through the Department of Health and Human Services or by grant or contract) technical assistance, and such other assistance as the Secretary determines appropriate, to any of the following: (1) Entities receiving a grant under section 340J\u20131. (2) Entities participating in a demonstration program under section 223(d) of the Protecting Access to Medicare Act of 2014. (3) Certified community behavioral health clinics (as defined in sections 1861(aa)(8) and 1905(jj)(2) of the Social Security Act) furnishing services under title XVIII or title XIX of such Act. (4) Health or social service provider organizations pursuing or considering certified community behavioral health clinic status or partnering with certified community behavioral health clinics. (5) States and territories, for the purpose of assisting in the consideration of demonstration programs carried out under section 223(d) of the Protecting Access to Medicare Act of 2014, the planning and development of new State certified community behavioral health clinic programs, or the ongoing implementation and improvement of established State certified community behavioral health clinic programs. (6) Other stakeholders, for the purpose of facilitating the successful implementation of the certified community behavioral health clinic model. (b) Inclusions Assistance provided by the Secretary under subsection (a) may include technical and nonfinancial assistance, including, but not limited to\u2014 (1) fiscal and program management assistance; (2) operational and administrative support; and (3) the provision of information to the entities about the variety of resources available under this part and how those resources can be best used to meet the health and behavioral health needs of the communities served by the entities. (c) Authorization of appropriations There is authorized to be appropriated to carry out this section $8,000,000 for each of fiscal years 2026 through 2030. 340J\u20133. Data infrastructure for community behavioral health clinic reporting (a) In general Not later than 180 days after the date of enactment of the Ensuring Excellence in Mental Health Act, the Secretary shall establish a system under which the Secretary shall collect and analyze data on community behavioral health clinics. (b) Scope of data collection The system established under subsection (a) shall be used by the Secretary to collect and analyze data from\u2014 (1) entities that receive a grant under section 340J\u20131; and (2) certified community behavioral health clinics (as defined in sections 1861(aa)(8) and 1905(jj)(2) of the Social Security Act) furnishing services under title XVIII or title XIX of such Act. (c) Authorization of appropriations There is authorized to be appropriated to carry out this section $51,000,000 for each of fiscal years 2026 through 2030. 340J\u20134. Certified community behavioral health clinic accreditation (a) Accreditation standards A clinic is accredited as a certified community behavioral health clinic under this section if the clinic\u2014 (1) is accredited by an accreditation body approved by the Secretary under subsection (b); and (2) authorizes the accreditation body to submit to the Secretary (or such agency as the Secretary may designate) such records or other information as the Secretary may require. (b) Approval of accreditation bodies The Secretary may approve a private nonprofit organization to be an accreditation body for the accreditation of certified community behavioral health clinics under subsection (a) if\u2014 (1) the accreditation body agrees to inspect the clinic, using inspectors qualified to evaluate quality of care in a behavioral health service setting, with such frequency the Secretary determines appropriate; (2) the Secretary determines that the standards applied by the accreditation body in determining whether or not to accredit a clinic correspond to (and are not less restrictive than) the criteria described in section 340J\u20131(b)(1)(B); (3) the accreditation body has made adequate assurances that the standards of the accreditation body continue to be met by each clinic that it accredited; (4) the accreditation body agrees that, for the 3-year period following accreditation of a clinic, in the case that the accreditation body suspends, withdraws, or revokes such accreditation, denies an application to renew such accreditation, or takes any other disciplinary action with respect to such clinic, the accreditation body shall submit to the Secretary the name of such clinic not later than 30 days after such action is taken; (5) the accreditation body agrees that, in the case that its approval is withdrawn by the Secretary, the body will notify each clinic accredited by the body of the withdrawal within 10 days of the withdrawal; and (6) the accreditation body complies with such other requirements as the Secretary determines appropriate. (c) Oversight of accreditation bodies The Secretary may provide ongoing oversight of accrediting bodies approved under subsection (b). Such ongoing oversight may include the following actions: (1) Providing continual oversight and review of approved accreditation processes through regular communication with such bodies. (2) Providing additional review of individual certified community behavioral health clinic accreditations to assure alignment with the criteria established by the Secretary under section 223(a) of the Protecting Access to Medicare Act of 2014 and, in cases where potential issues are identified with individual certified community behavioral health clinic accreditations, to provide review of such issues. (3) Mediating disputes between providers seeking certified community behavioral health clinic accreditation and approved accreditation bodies. (4) Providing ongoing support and coordination across approved accreditation bodies. (5) In cases where an approved accreditation body is found to not provide accreditation in alignment with the criteria established by the Secretary under section 223(a) of the Protecting Access to Medicare Act of 2014, developing a process to terminate the approval provided under subsection (b) with respect to such body. (6) Periodically reviewing accreditation body processes and renewing the approval provided under subsection (b) with respect to such bodies. (7) Such other activities as the Secretary determines necessary for the oversight of accreditation bodies approved under subsection (b). .\nIV\nLiability protection for certified community behavioral health clinic clinicians\n#### 401. Conferring protection under the Federal Tort Claims Act to clinicians in certified community behavioral health clinics\nSection 224(g)(4) of the Public Health Service Act ( 42 U.S.C. 233(g)(4) ) is amended by inserting or a certified community behavioral health clinic (as defined in section 1905(jj)(2) of the Social Security Act) before the period at the end.",
      "versionDate": "2026-04-23",
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
        "updateDate": "2026-05-19T20:12:51Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8487ih.xml"
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
      "title": "Ensuring Excellence in Mental Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring Excellence in Mental Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to adjust coverage and payment for certified community behavioral health clinic services under the Medicare and Medicaid programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:41Z"
    }
  ]
}
```
