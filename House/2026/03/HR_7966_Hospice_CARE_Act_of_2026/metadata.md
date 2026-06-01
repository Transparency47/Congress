# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7966?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7966
- Title: Hospice CARE Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7966
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-05-22T08:08:37Z
- Update date including text: 2026-05-22T08:08:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7966",
    "number": "7966",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001156",
        "district": "38",
        "firstName": "Linda",
        "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
        "lastName": "S\u00e1nchez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Hospice CARE Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:37Z",
    "updateDateIncludingText": "2026-05-22T08:08:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T14:02:05Z",
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
          "date": "2026-03-17T14:02:00Z",
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
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CT"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "WA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7966ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7966\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Ms. S\u00e1nchez introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to ensure the integrity of hospice care furnished under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hospice Care Accountability, Reform, and Enforcement Act of 2026 or the Hospice CARE Act of 2026 .\n#### 2. Ensuring the integrity of hospice care furnished under the Medicare program\n##### (a) Mandatory temporary moratorium on enrollment\n**(1) In general**\nSection 1866(j) of the Social Security Act ( 42 U.S.C. 1395cc(j) ) is amended by adding at the end the following new paragraph:\n(10) Mandatory temporary moratorium on enrollment of hospice programs (A) In general Except as provided in subparagraphs (B) and (C), the Secretary shall impose a nationwide temporary moratorium on the enrollment of new hospice programs under this title for the 5-year period beginning on the date of the enactment of this paragraph. (B) Exemption for certain hospices (i) In general The Secretary may exempt a hospice program seeking to enroll under this title from the moratorium described in subparagraph (A) if the Secretary determines that such program will furnish hospice care to individuals entitled to benefits under part A in an area with insufficient access to such care (as specified by the Secretary, taking into account the considerations described in clause (ii)). (ii) Considerations described For purposes of clause (i), the considerations described in this clause are, with respect to a hospice program seeking to enroll under this title, the following: (I) The specific geographic area that such program intends to serve. (II) The current availability of hospice care in such area. (III) Any evidence of unmet need for hospice care in such area (such as wait times for such care, the extent to which such area (or a population in such area) is considered underserved, and evidence that existing hospice programs are provided a substandard quality of care in such area). (IV) The program\u2019s plan to address any identified gaps in the provision of hospice care in such area. (C) Authority to lift moratorium The Secretary may lift the moratorium imposed under subparagraph (A) within a State (or geographic region of a State) specified by the Secretary in the same manner as the Secretary may lift a temporary moratorium (as described in paragraph (7)) under section 424.570(d) of title 42, Code of Federal Regulations (or a successor regulation). (D) Application of prepayment medical review during the temporary moratorium in certain circumstances (i) In general Subject to clause (ii), the Secretary shall apply prepayment medical review to hospice care consisting of routine home care furnished during the 5-year period beginning on the date of the enactment of this paragraph by an applicable hospice program to a covered individual. (ii) Termination of application of prepayment medical review (I) In general The Secretary shall terminate the application of prepayment medical review under clause (i) with respect to hospice care furnished by an applicable hospice program to a covered individual if the Secretary determines that, during the period in which such care so furnished by such program was subject to such review, such care was subject to a low rate of denial (as specified by the Secretary) under such review. (II) Revocation of termination The Secretary may revoke any termination of prepayment medical review under subclause (I) if determined appropriate by the Secretary. (iii) Definitions For purposes of this subparagraph: (I) Applicable hospice program The term applicable hospice program means a hospice program with a history of claim submissions with respect to hospice care furnished under this title that is aberrant (such as by demonstrating that such program is an outlier with respect to live discharges) compared to such history of claim submissions of similarly situated hospice programs, as determined by the Secretary. (II) Covered individual The term covered individual means an individual receiving hospice care under this title during the second 90-day period described in section 1812(d)(1) (or during any subsequent period) applicable to such individual. (E) Revalidation of enrollment information (i) In general During the 6-month period beginning on the date of the enactment of this paragraph and notwithstanding any applicable revalidation cycle under section 424.515 of title 42, Code of Federal Regulations (or a successor regulation), the Secretary shall revalidate the enrollment information of each hospice program enrolled under this title in accordance with the requirements applicable to revalidations of such information under such section. (ii) Publication of ownership information Not later than 1 year after the date of the enactment of this paragraph, the Secretary shall publish on a public website of the Centers for Medicare & Medicaid Services ownership interest and managing control information collected pursuant to revalidations described in clause (i) for each hospice program enrolled under this title. (iii) Report Not later than January 1, 2028, the Secretary, acting through the Assistant Secretary for Planning and Evaluation, shall submit to Congress a report on hospice ownership and control trends and the role of private equity in ownership and control of hospice programs. Such report shall include\u2014 (I) validation, to the extent feasible, of the ownership and control information reported on form CMS\u2013855A (or any successor form); (II) an analysis of hospice cost report data by ownership type; (III) recommendations on ways to improve the integrity of the ownership and control information reported by hospices during the enrollment process under this title; and (IV) to the extent practicable, recommendations on policies to promote health care competition. (F) Implementation The Secretary shall implement this paragraph through program instruction or other forms of subregulatory guidance. .\n**(2) Authority to provide exemptions to temporary moratoria**\nSection 1866(j)(7) of the Social Security Act ( 42 U.S.C. 1395cc(j)(7) ) is amended\u2014\n**(A)**\nin subparagraph (A), by adding at the end the following new sentence: The Secretary may exempt a provider of services or supplier that would otherwise be subject to a moratorium imposed under the preceding sentence from such moratorium if determined appropriate by the Secretary. ; and\n**(B)**\nin subparagraph (C)(iii)\u2014\n**(i)**\nin subclause (I), by striking and at the end;\n**(ii)**\nin subclause (II), by striking the period and inserting ; and ; and\n**(iii)**\nby adding at the end the following new subclause:\n(III) is not subject to an exemption described in such subparagraph. .\n##### (b) Extension of oversight of newly-Enrolled hospice programs\n**(1) In general**\nSection 1866(j)(3)(A) of the Social Security Act ( 42 U.S.C. 1395cc(j)(3)(A) ) is amended by inserting (or, in the case of a hospice program, not more than 2 years) after 1 year .\n**(2) Mandatory application of enhanced oversight for certain hospice programs**\nSection 1866(j)(3) of the Social Security Act ( 42 U.S.C. 1395cc(j)(3) ) is amended\u2014\n**(A)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(B)**\nby inserting after subparagraph (A) the following new subparagraph:\n(B) Mandatory application to certain hospice programs The procedures established by the Secretary under subparagraph (A) shall provide that any hospice program enrolling under this title that would, but for application of subparagraph (B) or (C) of paragraph (10), have been prohibited from so enrolling be subject to the enhanced oversight described in such subparagraph for a period of not less than 30 days. .\n##### (c) Increase in survey frequency for certain hospice programs\nSection 1822(a) of the Social Security Act ( 42 U.S.C. 1395i\u20136(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby inserting , with respect to such a survey conducted with respect to a hospice program that is not included on the list established under paragraph (5), after local survey agency, or ; and\n**(B)**\nby inserting (or, in the case of a hospice program that is included on the list established under paragraph (5), not less frequently than once every 18 months) after 36 months ;\n**(2)**\nby redesignating paragraph (5) as paragraph (6);\n**(3)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Hospice programs subject to increased survey frequency (A) In general The Secretary shall establish a list of hospice programs subject to increased survey frequency under paragraph (1) in accordance with the provisions of this paragraph. (B) Inclusion on list (i) In general The Secretary shall include a hospice program on the list established under subparagraph (A) if such program is not participating in the special focus program under subsection (b) and such hospice program meets either of the following criteria: (I) The program first submitted a claim for an item or service under this title during the 5-year period ending on the date of the enactment of this paragraph. (II) The program first submits a claim for an item or service under this title on or after such date of enactment. (ii) Discretionary inclusion The Secretary may include a hospice program on the list established under subparagraph (A)\u2014 (I) if claims data submitted by such program indicates that such program is not providing the full scope of hospice care services payable under this title; (II) if the Secretary determines that such program is an outlier with respect to live discharges; or (III) for any other reason determined appropriate by the Secretary. (C) Removal from list The Secretary shall remove a hospice program included in the list established under subparagraph (A)\u2014 (i) if\u2014 (I) such program has been subject to 2 surveys under this subsection while included on such list; and (II) neither such survey resulted in such program being cited for a deficiency for failure to comply with a condition of participation relating to quality of care; or (ii) if such program is placed in the special focus program established under subsection (b). ; and\n**(4)**\nin paragraph (6), as so redesignated, by striking each fiscal year (beginning with fiscal year 2022) and inserting each of fiscal years 2022 through 2026, and of $15,000,000 for fiscal year 2027 and for each subsequent fiscal year, .\n##### (d) Prohibition on payment for failure To meet quality data reporting requirements\nSection 1814(i)(5) of the Social Security Act ( 42 U.S.C. 1395f(i)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin the header, by striking Reduction in update for ;\n**(B)**\nin clause (i)\u2014\n**(i)**\nin the header, by striking In general and inserting Fiscal years 2014 through 2027 ;\n**(ii)**\nby inserting through fiscal year 2027 after each subsequent fiscal year ; and\n**(iii)**\nby adding at the end the following new sentence: The application of the preceding sentence may result in the market basket percentage increase under paragraph (1)(C)(ii)(VII) or paragraph (1)(C)(iii), as applicable, being less than 0.0 for a fiscal year, and may result in payment rates under this subsection for a fiscal year being less than such payment rates for the preceding fiscal year. ; and\n**(C)**\nby amending clause (ii) to read as follows:\n(ii) Subsequent fiscal years For purposes of fiscal year 2028 and each subsequent fiscal year, no payment may be made under this title to a hospice program that does not submit data to the Secretary in accordance with subparagraph (C) with respect to such fiscal year. ; and\n**(2)**\nin subparagraph (B), by striking subparagraph (A) and inserting subparagraph (A)(i) .\n##### (e) Ensuring independence of physician certifications of terminal illness\nSection 1814(a)(7)(A)(i) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(A)(i) ) is amended\u2014\n**(1)**\nin subclause (I), by inserting or, with respect to certifications under this clause occurring on or after October 1, 2027, in the case such individual fails to designate such an attending physician (or in the case such attending physician is employed by the hospice program at which such individual will receive such care or otherwise has a significant ownership interest in, or a significant financial relationship with, such program (as determined by the Secretary)), by a physician, physician assistant, or nurse practitioner that does not have such a significant ownership interest in, or such a significant financial relationship with, such program (as determined by the Secretary) before , and ; and\n**(2)**\nin the matter following subclause (II), by striking physician\u2019s and inserting physician\u2019s, physician assistant\u2019s, nurse practitioner\u2019s, .\n##### (f) Allowing additional providers To certify terminal illness\n**(1) In general**\nSection 1814(a)(7)(A)(i)(I) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(A)(i)(I) ) is amended by striking (which for purposes of this subparagraph does not include a nurse practitioner or a physician assistant) .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall apply with respect to certifications of terminal illnesses made on or after October 1, 2027.\n##### (g) Allowable use of supporting material in medical review of hospice care\nSection 1814(a) of the Social Security Act ( 42 U.S.C. 1395f(a) ) is amended by adding at the end the following new sentence: For purposes of conducting medical review of hospice care furnished to an individual, in addition to using documentation in the medical record of such individual\u2019s attending physician (as defined in section 1861(dd)) or of the physician, physician assistant, or nurse practitioner otherwise making the certification described in paragraph (7)(A)(i)(I) with respect to such individual, the Secretary may use documentation in the medical record of the hospice program furnishing such care as supporting material, as determined appropriate by the Secretary. .\n##### (h) Prohibition on certain changes in majority ownership\nWith respect to any change in the majority ownership of a hospice program occurring during the 5-year period beginning on the date of the enactment of this Act, the Secretary of Health and Human Services shall apply section 424.550(b) of title 42, Code of Federal Regulations (or a successor regulation), as if the references to 36 months in paragraph (1) of such section were references to 60 months .\n##### (i) Advanced notice of changes in ownership or control\nSection 1822 of the Social Security Act ( 42 U.S.C. 1395i\u20136 ) is amended by adding at the end the following new subsection:\n(d) Advanced notice of changes in ownership or control (1) In general Beginning January 1, 2028, in the case a change occurs in\u2014 (A) the persons with an ownership or control interest (as defined in section 1124(a)(3)) in the hospice program; (B) the persons who are officers, directors, agents, or managing employees (as defined in section 1126(b)) of the hospice program; (C) the corporation, association, or other company responsible for the management of the hospice program; (D) the individual who is the administrator of the hospice program; or (E) the individual who is the medical director of the hospice program; such program shall provide notice at the time of the change (or, in the case such change is with respect to a person described in subparagraph (A), at least 90 days before the effective date of the change) to the Secretary, the appropriate State or local survey agency, or appropriate approved accreditation agency of the change and of the identity of each new person, company, or individual described in the respective subparagraph. (2) Enforcement (A) In general In the case that the Secretary determines that a hospice program has violated paragraph (1), the Secretary may\u2014 (i) impose a civil monetary penalty in an amount not to exceed $1,000,000 per violation; and (ii) if determined appropriate by the Secretary, terminate such program\u2019s enrollment under this title. (B) Procedures The provisions of section 1128A (other than subsections (a) and (b) of such section) shall apply to a civil monetary penalty imposed under subparagraph (A) in the same manner as such provisions apply to a penalty or proceeding under such section. .\n##### (j) Required provision of addendum of noncovered services\nSection 1812(d)(1) of the Social Security Act ( 42 U.S.C. 1395d(d)(1) ) is amended by adding at the end the following new sentence: With respect to such an election made on or after October 1, 2027, in the case such program determines that there are items and services being furnished to such individual that are not related to the treatment of the individual\u2019s condition with respect to which a diagnosis of terminal illness has been made, such election shall include an addendum that specifies such items and services and includes such additional information as may be specified by the Secretary. Such program shall provide an updated addendum described in the preceding sentence to such individual if, while such election is in effect with respect to such individual, such program makes any alteration to the addendum provided to such individual at the time of such election. .\n##### (k) Medical review of hospice outliers and care unrelated to terminal condition\n**(1) In general**\n**(A) Medical review**\nSection 1814(a)(7) of the Social Security Act ( 42 U.S.C. 1395f(a)(7) ) is amended\u2014\n**(i)**\nin subparagraph (D), by striking and at the end;\n**(ii)**\nin subparagraph (E), by inserting before the date of the enactment of subparagraph (F), after subparagraph, ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(F) beginning on the date that is 5 years after the date of the enactment of this subparagraph, in the case of hospice care provided an individual for more than 90 days by a hospice program with aberrant billing patterns (as determined by the Secretary), the hospice care provided to such individual is subject to prepayment medical review (in accordance with procedures established by the Secretary); and .\n**(B) Technical expert panel**\n**(i) In general**\nThe Secretary of Health and Human Services shall establish a technical expert panel for purposes of establishing standards for identifying a hospice program with a history of aberrant billing patterns under section 1814(a)(7)(F) of the Social Security Act, as added by subparagraph (A). In making recommendations with respect to such standards, such panel shall take into account the results of prepayment medical reviews conducted under section 1866(j)(10)(D) of such Act, as added by subsection (a).\n**(ii) FACA waiver**\nThe provisions of chapter 10 of title 5, United States Code, shall not apply to the panel established under clause (i).\n**(2) Prepayment medical review requirement**\nSection 1812(d)(2) of the Social Security Act ( 42 U.S.C. 1395d(d)(2) ) is amended by adding at the end the following new subparagraph:\n(E) Notwithstanding any other provision of this title, in the case of items and services (other than items and services described in the matter following clause (ii)(II) of subparagraph (A)) furnished on or after October 1, 2027, to an individual with an election in effect under paragraph (1) by a provider of services or supplier, if such provider of services or supplier indicates that such items and services are unrelated to the individual\u2019s condition with respect to which a diagnosis of terminal illness has been made, no payment may be made under this title for such items and services before the Secretary has conducted a medical review of such items and services to determine whether such items and services are unrelated to such condition. Such review shall include a review of any addendum described in paragraph (1) included in such election. .\n**(3) Funding**\nThe Secretary of Health and Human Services shall provide for the transfer, from the Federal Hospital Insurance Trust Fund established under section 1817 of the Social Security Act ( 42 U.S.C. 1395i ) to the Centers for Medicare & Medicaid Services Program Management Account, of $20,000,000 for fiscal year 2027, to remain available until expended, for purposes of carrying out the amendments made by this subsection.\n##### (l) Provision of explanation of benefits upon hospice election\n**(1) In general**\nSection 1806 of the Social Security Act ( 42 U.S.C. 1395b\u20137 ) is amended by adding at the end the following new subsection:\n(d) Provision of explanation of benefits upon hospice election The Secretary shall furnish to each individual who makes an election described in section 1812(d)(1), not later than 15 days after such individual makes such election, a notice that\u2014 (1) specifies\u2014 (A) the effective date of such election; (B) the hospice program that will be furnishing hospice care to such individual; (C) the telephone number and address of such program; (D) the physician, physician assistant, or nurse practitioner who made the certification described in section 1814(a)(7)(A)(i)(I) with respect to such individual; (E) the toll-free telephone number of the medicare administrative contractor responsible for processing claims for such care; (2) informs such individual of the waiver of rights described in section 1812(d)(2)(A); (3) includes a statement which indicates that, because errors do occur and because Medicare waste, fraud, and abuse is a significant problem, such individual should carefully check the individual\u2019s hospice election information and if such individual suspects Medicare waste, fraud, or abuse with respect to the provision of such care, the individual should contact the toll-free phone number 1\u2013800\u2013MEDICARE and a toll-free phone number maintained by the Inspector General of the Department of Health and Human Services for the receipt of complaints and information about waste, fraud, and abuse in the provision or billing of services under this title; and (4) includes any other information determined appropriate by the Secretary. .\n**(2) Funding**\nThe Secretary of Health and Human Services shall provide for the transfer from the Federal Hospital Insurance Trust Fund established under section 1817 of the Social Security Act ( 42 U.S.C. 1395i ) to the Centers for Medicare & Medicaid Services Program Management Account of $10,000,000 for fiscal year 2027, to remain available until expended, for purposes of carrying out the amendment made by paragraph (1).\n**(3) Effective date**\nThe amendment made by paragraph (1) shall apply to individuals making elections described in section 1812(d)(1) of the Social Security Act ( 42 U.S.C. 1395d(d)(1) ) on or after the date that is 1 year after the date of the enactment of this Act.\n##### (m) Medical review of hospice care contractor requirements\n**(1) In general**\nThe Secretary of Health and Human Services (in this subsection referred to as the Secretary ) shall require any entity performing medical review under contract with Secretary of hospice care furnished under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ) to, with respect to such reviews performed on or after January 1, 2028, utilize only individuals who have received specialized instruction on the philosophy behind hospice care and medical prognostication (as specified by the Secretary) in performing such reviews. In so specifying such instruction and in updating such instruction, the Secretary shall consult with hospice programs as to the content of such instruction.\n**(2) Publication**\nThe Secretary shall make any instruction specified for purposes of paragraph (1) publicly available on the website of the Centers for Medicare & Medicaid Services.\n**(3) Report**\nNot later than October 1, 2028, the Secretary shall submit to Congress a report on activities relating to the medical review of hospice care furnished under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ). Such report shall include\u2014\n**(A)**\nwith respect to the medical review of hospice care performed during the period beginning on January 1, 2020, and ending on December 31, 2025, the accuracy rates of such reviews when performed by\u2014\n**(i)**\nmedicare administrative contractors;\n**(ii)**\nrecovery audit contractors;\n**(iii)**\nsupplemental medical review contractors; and\n**(iv)**\nuniform program integrity contractors;\n**(B)**\nthe total number of hospice claims submitted during the period described in subparagraph (A) subject to medical review;\n**(C)**\nthe percentage of such claims that were denied and appealed and the percentage of such claims so appealed that were overturned on appeal, broken down by the type of contractor conducting review of such claims and by each level of appeal;\n**(D)**\na list of medical review projects relating to hospice care undertaken by contractors described in subparagraph (A); and\n**(E)**\nactions the Secretary will take to reduce the audit burden on hospice programs with claims selected for medical review under multiple projects described in subparagraph (D) and to minimize the number of denials of claims for hospice care that are overturned on appeal.\n##### (n) Requiring face-to-Face encounters before recertifications of terminal illness\nSection 1814(a)(7) of the Social Security Act ( 42 U.S.C. 1395f(a)(7) ) is amended\u2014\n**(1)**\nin subparagraph (D)\u2014\n**(A)**\nby inserting , and before October 1, 2027 after 2011 ; and\n**(B)**\nby striking and at the end; and\n**(2)**\nby adding at the end the following new subparagraph:\n(F) on and after October 1, 2027, not more than 30 days before each recertification described in subparagraph (A)(ii) is made with respect to an individual, a hospice physician, hospice nurse practitioner, or hospice physician assistant has a face-to-face encounter (which may, with respect to any such recertification made for a 60-day period described in such subparagraph, be conducted via telehealth, but only if a registered nurse, licensed practical nurse, or home health aide employed by the hospice program furnishing hospice care to such individual is physically present with such individual during such encounter) with such individual to gather clinical findings to determine such individual\u2019s continue eligibility for hospice care; and .\n##### (o) Ensuring medical director and physician availability\n**(1) In general**\nSection 1861(dd) of the Social Security Act ( 42 U.S.C. 1395x(dd) ) is amended\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (F), by striking and at the end;\n**(ii)**\nby redesignating subparagraph (G) as subparagraph (I); and\n**(iii)**\nby inserting after subparagraph (F) the following new subparagraphs:\n(G) has a medical director responsible for the medical component of hospice care provided by such program who\u2014 (i) is a doctor of medicine or osteopathy licensed to practice in the State in which such program is located; and (ii) subject to paragraph (6), is not the medical director of more than 1 other hospice program; (H) ensures that the medical director described in subparagraph (G) or a physician member of the group described in subparagraph (B) is available for immediate consultation (which may be through telehealth) when hospice care is provided in an individual\u2019s home; and ; and\n**(B)**\nby adding at the end the following new paragraph:\n(6) The Secretary may waive the requirement described in paragraph (2)(G)(ii) with respect to the medical director of a hospice program if determined appropriate by the Secretary on a case-by-case basis. In determining whether to grant a waiver under the preceding sentence, the Secretary shall take into consideration\u2014 (A) the average daily census for each hospice program with respect to which such director is medical director; (B) the geographic areas served by such programs; and (C) any other information determined appropriate by the Secretary. .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall apply beginning January 1, 2029.\n##### (p) Report on hospice accrediting organizations\nNot later than 2 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the Secretary of Health and Human Services\u2019 (in this subsection referred to as the Secretary ) oversight of hospice program accrediting organizations. Such report shall include the following:\n**(1)**\nAn analysis of deficiencies relating to quality of care found pursuant to surveys conducted under section 1822(a) of the Social Security Act ( 42 U.S.C. 1395i\u20136(a) ) following complaints when such surveys were of hospice programs accredited by such an organization and such surveys were conducted by such an organization compared to such deficiencies so found following such complaints when such surveys were of hospice programs certified by State or local survey agencies and such surveys were conducted by such agencies.\n**(2)**\nA list of hospice programs determined by the Secretary not to be in compliance with all requirements applicable to such programs, along with a list of the accrediting organization of each such program.\n**(3)**\nA list of hospice programs that have been deactivated, terminated, or investigated due to concerns relating to waste, fraud, or abuse, along with a list of the accrediting organization of each such program.\n**(4)**\nAn analysis of any conflicts of interest of hospice program accrediting organizations.\n**(5)**\nPerformance data for hospice program accrediting organizations.\n#### 3. Payment reforms for hospice care furnished under the Medicare program\n##### (a) Adjusting payments for hospice care\n**(1) In general**\nSection 1814(i)(1)(C) of the Social Security Act ( 42 U.S.C. 1395f(i)(1)(C) ) is amended\u2014\n**(A)**\nin clause (iii)\u2014\n**(i)**\nby moving such clause 6 ems to the left;\n**(ii)**\nby striking With respect to and inserting Except as provided under clauses (viii) through (x), with respect to ;\n**(iii)**\nby inserting in a setting (as specified by the Secretary for purposes of clause (vii)) after hospice care furnished ;\n**(iv)**\nby inserting for such setting after payment rates in effect ; and\n**(v)**\nby striking under this clause and inserting under this subparagraph ;\n**(B)**\nin clause (iv), by striking clause (ii)(VII) or (iii) each place such phrase appears and inserting clause (iii) or (iv) of paragraph (2)(D) or clause (ii)(VII), (iii), (viii), (ix), or (x) in each such place; and\n**(C)**\nby adding at the end the following new clauses:\n(vii) Prior to the beginning of a specified fiscal year (as defined in clause (xi)), the Secretary shall specify percentages by which the payment rates for hospice care consisting of services other than routine home care (and, for specified years beginning on or after October 1, 2034, for hospice care consisting of routine home care and other services included in hospice care) in effect for the preceding fiscal year shall be adjusted in such specified fiscal year to align such rates with the costs of such care. In specifying such percentages\u2014 (I) the Secretary shall take into account changes in the average cost of such care and such other factors as determined appropriate by the Secretary; and (II) the Secretary may specify different percentages for such care based on the setting (as specified by the Secretary) in which such care is furnished. (viii) (I) With respect to routine home care furnished during fiscal year 2030, the payment rates for such care shall be equal to the sum of\u2014 (aa) a per diem amount (which may include an a case mix adjustment to account for variations in cost among different units of service) reflecting the cost of routine home care not consisting of direct patient care for nursing care, physical therapy, occupational therapy, speech-language pathology services, medical social services (other than counseling services), home health aide services, and physician services (other than such services that are considered administrative services); and (bb) subject to such frequency limits as may be specified by the Secretary, a per visit amount (which may vary depending on the type and duration of the visit, as determined appropriate by the Secretary) reflecting the cost of routine home care consisting of direct patient care excluded from the per diem amount established under item (aa) (other than, in the case of such care furnished at a skilled nursing facility or nursing facility (as defined in section 1919(a)), the component of such rates attributable to home health aide services). (II) With respect to routine home care furnished during fiscal year 2031 or a subsequent fiscal year, the payment rates for such care shall be equal to the sum of\u2014 (aa) the per diem amount attributable to hospice care described in subclause (I)(aa) in effect under this clause for the preceding fiscal year, adjusted, in the case of a specified fiscal year, by the percentages specified pursuant to clause (vii) for such specified fiscal year, increased by the market basket percentage increase (as defined in section 1886(b)(3)(B)(iii)) for the fiscal year (reduced in accordance with clause (iv)); and (bb) the per visit amount for hospice care described in subclause (I)(bb) in effect under this clause for the preceding fiscal year, adjusted, in the case of a specified fiscal year, by the percentages specified pursuant to clause (vii) for such specified fiscal year, increased by such market basked percentage increase for the fiscal year (reduced in accordance with clause (iv)). (III) For purposes of this clause, the term visit means, with respect to an individual receiving hospice care from a hospice program, in-person contact with such individual by staff of such program (or by others under arrangements with such program), not including any such contact conducted via telehealth or any other form of telecommunications technology. (ix) (I) With respect to routine home care consisting of specified hospice care (as defined in subclause (II)) furnished by, or under arrangements made by, a hospice program during the period beginning on October 1, 2027, and ending on September 30, 2032, in lieu of the rates otherwise payable under this subparagraph for such routine home care, the Secretary shall pay to the hospice program furnishing such care an amount equal to 400 percent of the amount payable for routine home care furnished in fiscal year 2027, increased by the market basket percentage increase (as defined in section 1886(b)(3)(B)(iii)) for the fiscal year (reduced in accordance with clause (iv)), or such other amount determined appropriate by the Secretary (which may vary based on the type of service furnished) for each day during which such specified hospice care was furnished. (II) For purposes of subclause (I), the term specified hospice care means any of the following items and services: (aa) Palliative chemotherapy or radiation furnished under the supervision of an oncologist and in accordance with accepted clinical guidelines. (bb) Palliative radiation therapy furnished under the supervision of an oncologist and in accordance with accepted clinical guidelines. (cc) Subject to such frequency limitations as the Secretary may establish, palliative blood transfusions furnished to an individual diagnosed with a blood cancer and furnished under the supervision of an oncologist and in accordance with accepted clinical guidelines. (dd) Palliative dialysis furnished under the supervision of a nephrologist, but only if\u2014 (AA) the individual receiving such palliative dialysis was receiving dialysis treatments prior to making the election under section 1812(d); and (BB) such individual has received fewer than 10 sessions of such palliative in-center or home hemodialysis or the equivalent for peritoneal dialysis or other modalities (or, in the case such individual has received 10 or more such sessions or the equivalent of such sessions, such session or equivalent of such session is subject to prior authorization). (x) With respect to hospice care consisting of services other than routine home care furnished during 2030 or a subsequent fiscal year, the payment rates for such care shall be equal to the rates in effect for such care for the preceding fiscal year, adjusted, in the case of a specified fiscal year, by the percentages specified pursuant to clause (vii) for such specified fiscal year, increased by the market basket percentage increase (as defined in section 1886(b)(3)(B)(iii)) for the fiscal year (reduced in accordance with clause (iv)). (xi) For purposes of this subparagraph, the term specified fiscal year means fiscal years 2030, 2035, and 2040. (xii) (I) The Secretary shall, with respect to cost reporting periods beginning during an applicable fiscal year (as defined in subclause (III)), conduct an audit of a representative sample of cost reports submitted by hospice programs. (II) The Secretary shall, for each applicable fiscal year, convene a technical expert panel for purposes of reviewing the methodology and results of the audit conducted under subclause (I) with respect to such applicable fiscal year. (III) For purposes of this clause, the term applicable fiscal year means fiscal years 2026, 2031, and 2036. (IV) The provisions of chapter 10 of title 5, United States Code, shall not apply to the panel established under subclause (II). (V) The Secretary shall provide for the transfer, from the Federal Hospital Insurance Trust Fund established under section 1817 to the Centers for Medicare & Medicaid Services Program Management Account, of $10,000,000 for each of fiscal years 2027, 2032, and 2037, to remain available until expended, for purposes of carrying out this clause. .\n**(2) Outlier payments**\nSection 1814(i) of the Social Security Act ( 42 U.S.C. 1395f(i) ) is amended\u2014\n**(A)**\nby redesignating paragraph (7) as paragraph (8); and\n**(B)**\nby inserting after paragraph (6) the following new paragraph:\n(7) (A) Subject to subparagraph (B), with respect to routine home care furnished during a fiscal year beginning on or after October 1, 2032, the Secretary may, if determined appropriate by the Secretary, provide an additional payment for types of such care (such as specified hospice care (as defined in paragraph (1)(C)(ix))) specified by the Secretary to account for unusual variations in the type or amount of such routine home care. (B) (i) The total amount of additional payments estimated to be made under subparagraph (A) for routine home care furnished during a fiscal year may not exceed 5 percent of the total amount of payments estimated to be made for such care furnished during such fiscal year without application of this paragraph for such fiscal year. (ii) The total amount of additional payments estimated to be made under subparagraph (A) for routine home care furnished during a fiscal year to an individual hospice program may not exceed 10 percent of the total amount of payments estimated to be made for such care furnished during such fiscal year by such program without application of this paragraph for such fiscal year. (C) The Secretary shall reduce any per diem rate applicable under paragraph (1) to routine home care furnished during the first fiscal year for which payments are made under subparagraph (A) by such proportion as will result, not taking into account any additional payments made under subparagraph (A) for such care furnished during such fiscal year, in an aggregate reduction of 5 percent in payment for such care furnished during such fiscal year. .\n**(3) Plan of care requirements**\n**(A) In general**\nSection 1814(a)(7)(B) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(B) ) is amended by inserting and, with respect to the establishment of such plan, in the case such plan includes the furnishing of specified hospice care (as defined in subsection (i)(1)(C)(x)(II)), by a nephrologist (if such care is care described in item (dd) of such subsection) or by an oncologist (if such care is care described in any of items (aa) through (cc) of such subsection) who does not have a significant ownership interest in, or a significant financial relationship with, such hospice program, as determined by the Secretary, and, with respect to the periodic review of such plan, in the case such plan includes the furnishing of specified hospice care (as defined in subsection (i)(1)(C)(x)(II)), by the nephrologist supervising the furnishing of such care (if such care is described in item (dd) of such subsection) or by the oncologist supervising the furnishing of such care (if such care is described in any of items (aa) through (cc) of such subsection) after of the hospice program .\n**(B) Effective date**\nThe amendment made by subparagraph (A) shall apply with respect to written plans for providing hospice care developed or reviewed on or after October 1, 2027.\n**(4) Excluding home health aide services and homemaker from the definition of hospice care in certain circumstances**\n**(A) In general**\nSection 1861(dd)(1)(D)(i) of the Social Security Act ( 42 U.S.C. 1395x(dd)(1)(D)(i) ) is amended by inserting in the case such individual is not residing in a skilled nursing facility or a nursing facility, before services of a .\n**(B) Homemaker services**\nSection 1861(dd)(1)(D)(ii) of the Social Security Act ( 42 U.S.C. 1395x(dd)(1)(D)(ii) ) is amended by inserting (but only if such individual is not residing in a skilled nursing facility or a nursing facility (as defined in section 1919(a)) or, if such individual is residing in such a skilled nursing facility or nursing facility, only if such services are provided on a volunteer basis in accordance with paragraph (2)(E)) after homemaker services .\n**(C) Effective date**\nThe amendments made by subparagraphs (A) and (B) shall apply to items and services furnished on or after October 1, 2029.\n**(5) Conforming adjustment to payment cap**\nSection 1814(i)(2)(B) of the Social Security Act ( 42 U.S.C. 1395f(i)(2)(B) ) is amended\u2014\n**(A)**\nin clause (i), by striking clause (ii) and inserting clauses (ii) through (iv) ;\n**(B)**\nin clause (ii), by inserting , subject to clause (iii), after subparagraph (A) ;\n**(C)**\nby striking clause (iii) and inserting the following new clause:\n(iii) For purposes of subparagraph (A), in the case of a specified fiscal year (as defined in paragraph (1)(C)(xi)), the cap amount for such year is the cap amount under this subparagraph for the preceding fiscal year, adjusted by the estimated percentage change in the total amount of payment made under this part for hospice care attributable to application of the amendments made by section 3(a)(1) of the Hospice CARE Act of 2026 for such specified fiscal year and then increased by the market basket percentage increase (as defined in section 1886(b)(3)(B)(iii)) for such specified fiscal year (reduced in accordance with paragraph (1)(C)(iv)). ; and\n**(D)**\nby adding at the end the following new clause:\n(iv) For purposes of subparagraph (A), subject to clause (iii), for a fiscal year beginning on or after October 1, 2035, the cap amount for such year is the cap amount under this subparagraph for the preceding fiscal year, increased by the market basket percentage increase (as defined in section 1886(b)(3)(B)(iii)) for such fiscal year (reduced in accordance with paragraph (1)(C)(iv)). .\n##### (b) Wage adjusting caps\n**(1) In general**\nSection 1814(i)(2) of the Social Security Act ( 42 U.S.C. 1395f(i)(2) ), as amended by subsection (a), is further amended\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking cap amount for the year (computed under subparagraph (B)) and inserting wage-adjusted cap (as defined in subparagraph (B)) for such program and year ; and\n**(ii)**\nby striking subparagraph (C) and inserting subparagraph (E) ;\n**(B)**\nby redesignating subparagraphs (B) through (D) as subparagraphs (D) through (F), respectively;\n**(C)**\nby inserting after subparagraph (A) the following new subparagraphs:\n(B) For purposes of subparagraph (A), the term wage-adjusted cap means, with respect to a hospice program and a year, the product of\u2014 (i) the wage index ratio (as computed under subparagraph (C)) for such program and year; and (ii) the cap amount for such year (as computed under subparagraph (D)). (C) For purposes of subparagraph (B), the wage index ratio for a hospice program and a year is the ratio of\u2014 (i) the aggregate payments to such program for such year under paragraph (1); to (ii) the aggregate payments to such program for such year under such paragraph that would have been made had such payments not been subject to any wage adjustment. ;\n**(D)**\nin subparagraph (D), as so redesignated\u2014\n**(i)**\nby striking subparagraph (A) each place it appears and inserting subparagraph (B) in each such place; and\n**(ii)**\nby adding at the end the following new clause:\n(v) Notwithstanding the preceding provisions of this subparagraph, for a fiscal year beginning on or after October 1, 2026, the cap amount otherwise determined under this subparagraph for such fiscal year shall be decreased by the same percentage reduction (if any) applied to the amount of payment made under this part for such fiscal year under an order issued pursuant to section 251 of the Balanced Budget and Emergency Deficit Control Act of 1985. Any reduction to the cap amount for a fiscal year under the preceding sentence shall not be taken into account for purposes of determining the cap amount for any succeeding fiscal year. ; and\n**(E)**\nby adding at the end the following new subparagraph:\n(G) Not later than 1 year after the date of the enactment of this subparagraph, and annually thereafter, the Secretary shall submit to Congress and make public on the website of the Centers for Medicare & Medicaid Services a report on the calculation of hospice programs\u2019 cap amounts under this paragraph. Such report shall contain, with respect to each of the 5 most recent accounting years for which data is available and each hospice program receiving payments under this section for hospice care furnished during such year, the following: (i) Such program\u2019s cap amount determined under such section. (ii) The percentage of such program\u2019s cap amount paid to such program for such care. (iii) In the case payments to such program exceeded such cap, any amount recouped by the Secretary with respect to such program. (iv) The live discharge rate of such program. .\n**(2) Implementation**\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by paragraph (1) by program instruction or otherwise.\n**(3) Effective date**\nThe amendments made by subparagraphs (A) through (C) of paragraph (1) shall apply with respect to payment for hospice care furnished during fiscal years beginning on or after October 1, 2027.\n##### (c) Modification of requirements relating to short-Term inpatient care\n**(1) In general**\nSection 1861(dd) of the Social Security Act ( 42 U.S.C. 1395x(dd) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (G), by striking consecutively over longer than five days and inserting for more than 5 days during any 90-day election period (or 60-day election period, as applicable) described in section 1812(d)(1) ; and\n**(ii)**\nin the flush matter following subparagraph (I), by adding at the end the following new sentence: In the case of an individual who receives short-term inpatient care described in subparagraph (G) consisting of respite care during an election period and the furnishing of such care is immediately preceded by a hospital stay (which may include a stay for observation) during which such individual made an election described in section 1812(d)(1) for the first time during such individual\u2019s lifetime (or if such care is immediately preceded by the furnishing of hospice care consisting of general inpatient care and such general inpatient care is immediately preceded by such a hospital stay), the first continuous 15 days of such care shall not be taken into account for purposes of applying the limitation on the number of days during which such care may be furnished during an election period under such subparagraph, but only if such individual does not have sufficient caregiver support to be discharged to the individual\u2019s home. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)(iii)\u2014\n**(I)**\nby striking provides assurances satisfactory to the Secretary that and inserting ensures that the sum of ; and\n**(II)**\nby striking 20 percent and inserting 10 percent (or a higher percent (not to exceed 20 percent) specified by the Secretary if determined necessary by the Secretary to ensure sufficient access to such inpatient care) ; and\n**(ii)**\nby adding at the end the following flush sentence:\nFor purposes of subparagraph (A)(iii), the Secretary shall ensure that the limitation described in such subparagraph is applied, to the extent practicable, on a real-time basis. .\n**(2) Allowing respite care to be furnished in residential care facilities**\nNot later than October 1, 2027, the Secretary of Health and Human Services (in this paragraph referred to as the Secretary ) shall revise section 418.108 of title 42, Code of Federal Regulations (or a successor regulation), to allow short-term inpatient care consisting of respite care (as described in section 1861(dd)(1)(G) of the Social Security Act ( 42 U.S.C. 1395x(dd)(1)(G) )) to be furnished in residential care facilities (as defined by the Secretary) that only provide care to individuals receiving hospice care (as specified by the Secretary) and that meet such standards relating to health and safety as the Secretary may specify (which may be based on State licensure requirements applicable to such facilities).\n**(3) Effective date**\nThe amendments made by paragraph (1) shall apply to hospice care furnished on or after October 1, 2027.\n##### (d) Hospital discharge planning requirements\n**(1) In general**\nSection 1861(ee)(2)(D) of the Social Security Act ( 42 U.S.C. 1395x(ee)(2)(D) ) is amended\u2014\n**(A)**\nby inserting , home health services, after including hospice care ;\n**(B)**\nby striking including the availability of home health services through individuals and entities and inserting the following:\nincluding\u2014 (i) in the case of individuals who are likely to need home health services, the availability of such services through home health agencies ;\n**(C)**\nby striking listed by the hospital as available and, in the case of individuals who are likely to need post-hospital extended care services, and inserting the following:\nlisted by the hospital as available; (ii) in the case of individuals who are likely to need post-hospital extended care services, ;\n**(D)**\nby striking the period and inserting ; and ; and\n**(E)**\nby adding at the end the following new clause:\n(iii) in the case of individuals who are likely eligible for hospice care, the availability of such care (including the availability of respite care described in subsection (dd)(1)(G)) through hospice programs that participate in the program under this title and that serve the area in which the patient resides. .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall apply with respect to discharges occurring on or after October 1, 2027.\n##### (e) Payment for respite care furnished in the home\n**(1) In general**\nSection 1861(dd)(1) of the Social Security Act ( 42 U.S.C. 1395x(dd)(1) ) is amended\u2014\n**(A)**\nin subparagraph (H), by striking and at the end;\n**(B)**\nby redesignating subparagraph (I) as subparagraph (J); and\n**(C)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) short-term home respite care furnished to an individual on or after October 1, 2029, that\u2014 (i) is furnished in the place of residence used as such individual\u2019s home (other than a skilled nursing facility, a nursing facility (as defined in section 1919(a)), an assisted living facility (as defined by the Secretary), or another facility specified by the Secretary); (ii) is furnished on an intermittent, nonroutine, and occasional basis; (iii) is furnished for not more than 120 hours during any 90-day period described in section 1812(d)(1) (or, in the case such individual is 60-day period described in such section, for not more than 80 hours during such period); and (iv) meets such other requirements as the Secretary may specify. .\n**(2) Payment rates**\nSection 1814(i)(1)(C) of the Social Security Act ( 42 U.S.C. 1395f(i)(1)(C) ), as amended by subsection (a), is further amended\u2014\n**(A)**\nin clause (iii), by striking through (x) and inserting through (x) and clause (xiii) ; and\n**(B)**\nby adding at the end the following new clause:\n(xiii) With respect to short-term home respite care furnished to an individual during fiscal year 2030 or a subsequent fiscal year, the rates payable for such care shall be equal to the sum of the per diem rate established for routine home care for such fiscal year and an hourly rate established by the Secretary, except that in no case may such rate payable for such short-term home respite care furnished in a 24-hour period exceed the rate of payment for general inpatient care furnished during such a period. .",
      "versionDate": "2026-03-17",
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
        "actionDate": "2026-03-17",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4118",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Hospice CARE Act of 2026",
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
        "updateDate": "2026-04-20T19:26:49Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7966ih.xml"
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
      "title": "Hospice CARE Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hospice Care Accountability, Reform, and Enforcement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "title": "Hospice CARE Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to ensure the integrity of hospice care furnished under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T04:48:32Z"
    }
  ]
}
```
