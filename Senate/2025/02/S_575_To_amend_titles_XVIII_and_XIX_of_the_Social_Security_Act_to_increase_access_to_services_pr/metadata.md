# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/575
- Title: I CAN Act
- Congress: 119
- Bill type: S
- Bill number: 575
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-05T21:32:34Z
- Update date including text: 2025-12-05T21:32:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/575",
    "number": "575",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "I CAN Act",
    "type": "S",
    "updateDate": "2025-12-05T21:32:34Z",
    "updateDateIncludingText": "2025-12-05T21:32:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
        "item": {
          "date": "2025-02-13T18:00:33Z",
          "name": "Referred To"
        }
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WY"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "DE"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "VT"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s575is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 575\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Merkley (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to increase access to services provided by advanced practice registered nurses under the Medicare and Medicaid programs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Improving Care and Access to Nurses Act or the I CAN Act .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Removal of Barriers to Practice on Nurse Practitioners\nSec. 101. Expanding access to cardiac rehabilitation programs and pulmonary rehabilitation programs under Medicare program.\nSec. 102. Permitting nurse practitioners and physician assistants to satisfy Medicare documentation requirement for coverage of certain shoes for individuals with diabetes.\nSec. 103. Improvements to the assignment of beneficiaries under the Medicare shared savings program.\nSec. 104. Expanding the availability of medical nutrition therapy service Medicare program.\nSec. 105. Preserving access to home infusion therapy.\nSec. 106. Increasing access to hospice care services.\nSec. 107. Streamlining care delivery in skilled nursing facilities and nursing facilities; authorizing Medicare and Medicaid inpatient hospital patients to be under the care of a nurse practitioner.\nSec. 108. Improving access to Medicaid clinic services.\nTITLE II\u2014Removal of Barriers to Practice on Certified Registered Nurse Anesthetists\nSec. 201. Clarifying that certified registered nurse anesthetists can be reimbursed by Medicare for evaluation and management services.\nSec. 202. Revision of conditions of payment relating to services ordered and referred by certified registered nurse anesthetists.\nSec. 203. Special payment rule for teaching student registered nurse anesthetists.\nSec. 204. Removing unnecessary and costly supervision of certified registered nurse anesthetists.\nSec. 205. CRNA services as a Medicaid-required benefit.\nTITLE III\u2014Removal of Barriers to Practice on Certified Nurse-Midwives\nSec. 301. Improving access to training in maternity care.\nSec. 302. Improving Medicare patient access to home health services provided by certified nurse-midwives.\nSec. 303. Improving access to DMEPOS for Medicare beneficiaries.\nSec. 304. Technical changes to qualifications and conditions with respect to the services of certified nurse-midwives.\nTITLE IV\u2014Improving Federal Health Programs for All Advanced Practice Registered Nurses\nSec. 401. Revising the local coverage determination process under the Medicare program.\nSec. 402. Locum tenens.\nTITLE V\u2014Effective Date\nSec. 501. Effective date.\nI\nRemoval of Barriers to Practice on Nurse Practitioners\n#### 101. Expanding access to cardiac rehabilitation programs and pulmonary rehabilitation programs under Medicare program\n##### (a) Cardiac rehabilitation programs\nSection 1861(eee) of the Social Security Act ( 42 U.S.C. 1395x(eee) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking a physician\u2019s office and inserting the office setting ; and\n**(B)**\nin subparagraph (C), by inserting after physician the following: (as defined in subsection (r)(1)) or a physician assistant, nurse practitioner, or clinical nurse specialist (as those terms are defined in subsection (aa)(5)) ;\n**(2)**\nin paragraph (3)(A), by striking physician-prescribed exercise and inserting exercise prescribed by a physician (as defined in subsection (r)(1)) or a physician assistant, nurse practitioner, or clinical nurse specialist (as those terms are defined in subsection (aa)(5)) ; and\n**(3)**\nin paragraph (5), by inserting after physician the following: (as defined in subsection (r)(1)) or a physician assistant, nurse practitioner, or clinical nurse specialist (as those terms are defined in subsection (aa)(5)) .\n##### (b) Pulmonary rehabilitation programs\nSection 1861(fff) of the Social Security Act ( 42 U.S.C. 1395x(fff) ) is amended\u2014\n**(1)**\nin paragraph (2)(A), by striking physician-prescribed exercise and inserting exercise prescribed by a physician (as defined in subsection (r)(1)) or a physician assistant, nurse practitioner, or clinical nurse specialist (as those terms are defined in subsection (aa)(5)) ; and\n**(2)**\nin paragraph (3), by inserting after physician the following: (as defined in subsection (r)(1)) or a physician assistant, nurse practitioner, or clinical nurse specialist (as those terms are defined in subsection (aa)(5)) .\n#### 102. Permitting nurse practitioners and physician assistants to satisfy Medicare documentation requirement for coverage of certain shoes for individuals with diabetes\nSection 1861(s)(12) of the Social Security Act ( 42 U.S.C. 1395x(s)(12) ) is amended\u2014\n**(1)**\nin subparagraph (A), by inserting , nurse practitioner, or physician assistant after physician ; and\n**(2)**\nin subparagraph (C), by inserting , nurse practitioner, or physician assistant after each occurrence of physician .\n#### 103. Improvements to the assignment of beneficiaries under the Medicare shared savings program\nSection 1899(c)(1) of the Social Security Act ( 42 U.S.C. 1395jjj(c)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and at the end;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(C) in the case of performance years beginning on or after January 1, 2026, primary care services provided under this title by an ACO professional described in subsection (h)(1)(B). .\n#### 104. Expanding the availability of medical nutrition therapy service Medicare program\nSection 1861(vv)(1) of the Social Security Act ( 42 U.S.C. 1395x(vv)(1) ) is amended by inserting or a nurse practitioner, a clinical nurse specialist, or a physician assistant (as such terms are defined in subsection (aa)(5)) before the period at the end.\n#### 105. Preserving access to home infusion therapy\n##### (a) Allowing applicable providers To establish home infusion therapy plans\nSection 1861(iii)(1)(B) of the Social Security Act ( 42 U.S.C. 1395x(iii)(1)(B) ) is amended\u2014\n**(1)**\nby striking a physician (as defined in subsection (r)(1)) and inserting an applicable provider (as defined in paragraph (3)(A)) ; and\n**(2)**\nby striking a physician (as so defined) and inserting an applicable provider (as so defined) .\n##### (b) Conforming amendment\nSection 1834(u)(6) of the Social Security Act ( 42 U.S.C. 1395m(u)(6) ) is amended by striking physician and inserting applicable provider (as defined in section 1861(iii)(3)(A)) .\n#### 106. Increasing access to hospice care services\n##### (a) In general\nSection 1814(a)(7)(A) of the Social Security Act ( 42 U.S.C. 1395f(a)(7)(A) ) is amended\u2014\n**(1)**\nin clause (i)\u2014\n**(A)**\nin subclause (I), by striking a nurse practitioner or ;\n**(B)**\nin subclause (II), by inserting or nurse practitioner after physician ; and\n**(C)**\nin the flush matter following subclause (II), by inserting , nurse practitioner\u2019s, after physician\u2019s ; and\n**(2)**\nin clause (ii), by striking or physician and inserting , physician, or nurse practitioner .\n##### (b) Hospice care definition\nSection 1861(dd)(1)(C) of the Social Security Act ( 42 U.S.C. 1395x(dd)(1)(C) ) is amended by inserting or nurse practitioner after physician .\n##### (c) Nurse practitioner billing\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Health and Human Services shall revise section 418.304 of title 42, Code of Federal Regulations, to allow nurse practitioners to bill for services not described in paragraph (a) of such section in the same manner as physicians may bill for such services in accordance with paragraph (b) of such section. Such revision shall provide that such services furnished by a nurse practitioner shall be payable at the percent of the physician fee schedule specified in section 1833(a)(1)(O) of the Social Security Act ( 42 U.S.C. 1395l(a)(1)(O) ).\n#### 107. Streamlining care delivery in skilled nursing facilities and nursing facilities; authorizing Medicare and Medicaid inpatient hospital patients to be under the care of a nurse practitioner\n##### (a) Medicare\n**(1) Certification of post-hospital extended care services**\nSection 1814(a)(2) of the Social Security Act ( 42 U.S.C. 1395f(a)(2) ) is amended, in the matter preceding subparagraph (A), by striking , or a nurse practitioner, and inserting or a nurse practitioner (in accordance with State law), or .\n**(2) Certification authority for nurse practitioners**\nSection 1814(a)(3) of the Social Security Act ( 42 U.S.C. 1395f(a)(3) ) is amended by inserting or nurse practitioner after physician .\n**(3) Supervision requirement in skilled nursing facility services and resident's rights**\nSection 1819 of the Social Security Act ( 42 U.S.C. 1395i\u20133(b)(6) ) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (2)(B), by inserting or nurse practitioner after attending physician ; and\n**(ii)**\nin paragraph (6)\u2014\n**(I)**\nin the heading, by striking Physician supervision and inserting Supervision ; and\n**(II)**\nin subparagraph (A), by inserting or a nurse practitioner, in accordance with State law after physician ; and\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin subparagraph (1)(A)(i), by inserting or nurse practitioner after attending physician ;\n**(ii)**\nin the flush matter at the end of subparagraph (2)(A), by inserting or nurse practitioner after physician in each occurrence; and\n**(iii)**\nin subparagraph (3)(A), by inserting or nurse practitioner after physician .\n**(4) Administration of part B**\nSection 1842(b)(2)(C) of the Social Security Act ( 42 U.S.C. 1395u(b)(2)(C) ) is amended, in the second sentence\u2014\n**(A)**\nby inserting or a nurse practitioner after a physician ; and\n**(B)**\nby striking or a nurse practitioner working in collaboration with that physician, or both .\n**(5) Provision of medical and other health services**\nSection 1861(s)(2)(K)(ii) of the Social Security Act ( 42 U.S.C. 1395x(s)(2)(K)(ii) ) is amended by striking or clinical nurse specialist (as defined in subsection (aa)(5)) working in collaboration (as defined in subsection (aa)(6)) with a physician (as defined in subsection (r)(1)) and inserting (as defined in subsection (aa)(5)(A)), or by a clinical nurse specialist (as defined in subsection (aa)(5)(B)) working in collaboration with a physician (as defined in subsection (r)(1)), .\n**(6) Privileges for nurse practitioners**\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(A)**\nin subsection (e)(4), by inserting (or nurse practitioner, in accordance with State law) after physician ;\n**(B)**\nin subsection (f)(1), by inserting or nurse practitioner after physician ; and\n**(C)**\nin each of subparagraphs (B) and (F) of subsection (ee)(2), by inserting or nurse practitioner after physician .\n##### (b) Medicaid\n**(1) Certification authority for nurse practitioners**\nSection 1902(a)(44) of the Social Security Act ( 42 U.S.C. 1396a(a)(44) ) is amended to read as follows:\n(44) in each case for which payment for inpatient hospital services, skilled nursing facility services, services in an intermediate care facility described in section 1905(d), or inpatient mental hospital services is made under the State plan\u2014 (A) a physician or nurse practitioner (or, in the case of skilled nursing facility services or intermediate care facility services, a physician or nurse practitioner, or a clinical nurse specialist who is not an employee of the facility but is working in collaboration with a physician) certifies at the time of admission, or, if later, the time the individual applies for medical assistance under the State plan (and a physician or nurse practitioner, or a physician assistant under the supervision of a physician, or, in the case of skilled nursing facility services or intermediate care facility services, a physician or nurse practitioner, or a clinical nurse specialist who is not an employee of the facility but is working in collaboration with a physician, recertifies, where such services are furnished over a period of time, in such cases, at least as often as required under section 1903(g)(6) (or, in the case of services that are services provided in an intermediate care facility, every year), and accompanied by such supporting material, appropriate to the case involved, as may be provided in regulations of the Secretary), that such services are or were required to be given on an inpatient basis because the individual needs or needed such services, and (B) such services were furnished under a plan established and periodically reviewed and evaluated by a physician or nurse practitioner, or, in the case of skilled nursing facility services or intermediate care facility services, by a physician or nurse practitioner, or a clinical nurse specialist who is not an employee of the facility but is working in collaboration with a physician; .\n**(2) Nursing facility services supervision and clinical records**\nSection 1919(b)(6)(A) of the Social Security Act ( 42 U.S.C. 1396r(b)(6)(A) ) is amended to read as follows:\n(A) require that the health care of every resident be provided under the supervision of a physician or nurse practitioner (or, at the option of a State, under the supervision of a clinical nurse specialist or physician assistant who is not an employee of the facility but who is working in collaboration with a physician); .\n#### 108. Improving access to Medicaid clinic services\nSection 1905(a)(9) of the Social Security Act ( 42 U.S.C. 1396d(a)(9) ) is amended by adding or nurse practitioner after physician in both places that it appears.\nII\nRemoval of Barriers to Practice on Certified Registered Nurse Anesthetists\n#### 201. Clarifying that certified registered nurse anesthetists can be reimbursed by Medicare for evaluation and management services\nSection 1861(bb)(1) of the Social Security Act ( 42 U.S.C. 1395x(bb)(1) ) is amended by inserting , including pre-anesthesia evaluation and management services, after and related care .\n#### 202. Revision of conditions of payment relating to services ordered and referred by certified registered nurse anesthetists\nNot later than 3 months after the date of enactment of this Act, the Secretary of Health and Human Services shall revise section 410.69 of title 42, Code of Federal Regulations, to clarify that, for purposes of payment under part B of title XVIII of the Social Security Act\u2014\n**(1)**\ncertified registered nurse anesthetists are authorized to order, certify, and refer services to the extent allowed under the law of the State in which the services are furnished; and\n**(2)**\npayment shall be made under such part for such services so ordered, certified, or referred by certified registered nurse anesthetists.\n#### 203. Special payment rule for teaching student registered nurse anesthetists\nSection 1848(a)(6) of the Social Security Act ( 42 U.S.C. 1395w\u20134(a)(6) ) is amended, in the matter preceding subparagraph (A), by inserting or student registered nurse anesthetists after physician residents .\n#### 204. Removing unnecessary and costly supervision of certified registered nurse anesthetists\nSection 1861(bb)(2) of the Social Security Act ( 42 U.S.C. 1395x(bb)(2) ) is amended\u2014\n**(1)**\nin the second sentence, by inserting , but may not require that certified registered nurse anesthetists provide services under the supervision of a physician after certification of nurse anesthetists ; and\n**(2)**\nin the third sentence, by inserting under the supervision of an anesthesiologist after an anesthesiologist assistant .\n#### 205. CRNA services as a Medicaid-required benefit\n##### (a) In general\nSection 1905(a)(5) of the Social Security Act ( 42 U.S.C. 1396d(a)(5) ) is amended\u2014\n**(1)**\nby striking and (B) and inserting (B) ; and\n**(2)**\nby inserting before the semicolon at the end the following: , and (C) services furnished by a certified registered nurse anesthetist (as defined in section 1861(bb)(2)), which such certified registered nurse anesthetist is authorized to perform under State law (or the State regulatory mechanism as provided by State law) .\n##### (b) Payment\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) is amended\u2014\n**(1)**\nin paragraph (86), by striking and at the end;\n**(2)**\nin paragraph (87), by striking the period and inserting ; and ; and\n**(3)**\nby inserting after paragraph (87) the following new paragraph:\n(88) provide for payment for the services of a certified registered nurse anesthetist (as defined in section 1861(bb)(1)) in amounts no lower than the amounts, using the same methodology, used for payment for amounts under section 1833(a)(1)(H). .\nIII\nRemoval of Barriers to Practice on Certified Nurse-Midwives\n#### 301. Improving access to training in maternity care\n##### (a) Medicare payments for supervision by certified nurse-Midwives\nParagraph (1) of section 1861(gg) of the Social Security Act ( 42 U.S.C. 1395x(gg) ) is amended to read as follows:\n(1) The term certified nurse-midwife services means\u2014 (A) such services furnished by a certified nurse-midwife (as defined in paragraph (2)); and (B) such services (and such supplies and services furnished as an incident to the nurse-midwife's service) which\u2014 (i) the certified nurse-midwife is legally authorized to perform under State law (or the State regulatory mechanism provided by State law) as would otherwise be covered if furnished by a physician; (ii) are furnished under the supervision of a certified-nurse midwife by an intern or resident-in-training (as described in subsection (b)(6)); (iii) would otherwise be described in subparagraph (A) if furnished by a certified nurse-midwife; and (iv) would otherwise be covered if furnished under the supervision of a physician. .\n##### (b) Clarifying permissibility of using certain grants for clinical training by certified nurse-Midwives\nSection 811(a)(1) of the Public Health Service Act ( 42 U.S.C. 296j(a)(1) ) is amended by inserting , including clinical training, after projects .\n#### 302. Improving Medicare patient access to home health services provided by certified nurse-midwives\n##### (a) In general\nSection 1835(a) of the Social Security Act ( 42 U.S.C. 1395n(a) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting or a certified nurse-midwife (as defined in section 1861(gg)), after or a physician assistant (as defined in section 1861(aa)(5)) who is working in accordance with State law, ; and\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nin each of clauses (ii) and (iii), by striking or a physician assistant (as the case may be) and inserting a physician assistant, or a certified nurse-midwife (as the case may be) ; and\n**(ii)**\nin clause (iv), by\u2014\n**(I)**\ninserting or by a certified nurse-midwife (as defined in section 1861(gg)) after (but in no case later than the date that is 6 months after the date of the enactment of the CARES Act) ; and\n**(II)**\nby striking (as defined in section 1861(gg)) ; and\n**(2)**\nin the matter following paragraph (2), by striking or physician assistant (as the case may be) and inserting physician assistant, or certified nurse-midwife (as the case may be) each place it appears.\n##### (b) Conforming amendments\nSection 1895 of the Social Security Act ( 42 U.S.C. 1395(fff) ) is amended\u2014\n**(1)**\nin subsection (c)(1), by inserting the certified nurse-midwife (as defined in section 1861(gg)), after clinical nurse specialist (as those terms are defined in section 1861(aa)(5)), ; and\n**(2)**\nin subsection (e)(1)(A), by striking a physician a nurse practitioner or clinical nurse specialist, and inserting a physician, a nurse practitioner, a clinical nurse specialist, a certified nurse-midwife, .\n#### 303. Improving access to DMEPOS for Medicare beneficiaries\nSection 1834(a) of the Social Security Act ( 42 U.S.C. 1395m(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(E)(ii) by striking or a clinical nurse specialist (as those terms are defined in section 1861(aa)(5)) and inserting , a clinical nurse specialist (as those terms are defined in section 1861(aa)(5)), or a certified nurse-midwife (as defined in section 1861(gg)) ; and\n**(2)**\nin paragraph (11)(B)(ii)\u2014\n**(A)**\nby striking or a clinical nurse specialist (as those terms are defined in section 1861(aa)(5)) and inserting a clinical nurse specialist (as those terms are defined in section 1861(aa)(5)), or a certified nurse-midwife (as defined in section 1861(gg)) ; and\n**(B)**\nby striking or specialist and inserting specialist, or nurse-midwife .\n#### 304. Technical changes to qualifications and conditions with respect to the services of certified nurse-midwives\nSection 1861(gg)(2) of the Social Security Act ( 42 U.S.C. 1395x(gg)(2) ) is amended by striking , or has been certified by an organization recognized by the Secretary and inserting and has been certified by the American Midwifery Certification Board (or a successor organization) .\nIV\nImproving Federal Health Programs for All Advanced Practice Registered Nurses\n#### 401. Revising the local coverage determination process under the Medicare program\n##### (a) In general\nSection 1862(l)(5) of the Social Security Act ( 42 U.S.C. 1395y(l)(5) ) is amended\u2014\n**(1)**\nin subparagraph (D), by adding at the end the following new clauses:\n(vi) Identification of any medical or scientific experts whose advice was obtained by such contractor during the development of such determination, whether or not such contractor relied on such advice in developing such determination. (vii) A hyperlink to any written communication between such contractor and another entity that such contractor relied on when developing such determination. (viii) A hyperlink to any rule, guideline, protocol, or other criterion that such contractor relied on when developing such determination. ; and\n**(2)**\nby adding at the end the following new subparagraphs:\n(E) Prohibition on imposition of practitioner qualifications The Secretary shall prohibit a Medicare administrative contractor that develops a local coverage determination from imposing such determination on any coverage limitation with respect to the qualifications of a physician (as defined in section 1861(r)) or a practitioner described in section 1842(b)(18)(C) who may furnish the item or service that is the subject of such determination. (F) Civil monetary penalty A Medicare administrative contractor that develops a local coverage determination that fails to make information described in subparagraph (D) available as required by the Secretary under such subparagraph or comply with the prohibition under subparagraph (E) is subject to a civil monetary penalty of not more than $10,000 for each such failure. The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil money penalty under the previous sentence in the same manner as such provisions apply to a penalty or proceeding under section 1128A(a). .\n##### (b) Timing of review\nSection 1869(f)(2) of the Social Security Act ( 42 U.S.C. 1395ff(f)(2) ) is amended by adding at the end the following new subparagraph:\n(D) Timing of review An aggrieved party may file a complaint described in subparagraph (A) with respect to a local coverage determination on or after the date that such determination is posted, in accordance with section 1862(l)(5)(D), on the Internet website of the Medicare administrative contractor making such determination, whether or not such determination has taken effect. .\n##### (c) Effective date\nThe amendments made by this section shall apply to local coverage determinations made available on the internet website of a Medicare administrative contractor and on the Medicare internet website on or after the date of the enactment of this Act.\n#### 402. Locum tenens\nSection 1842(b)(6) of the Social Security Act ( 42 U.S.C. 1395u(b)(6) ) is amended, in the first sentence\u2014\n**(1)**\nby striking and (J) and inserting (J) ; and\n**(2)**\nby inserting before the period at the end the following: , and (K) in the case of services furnished by a certified registered nurse anesthetist (as defined in section 1861(bb)(2)), nurse practitioner, or clinical nurse specialist (as defined in section 1861(aa)(5)), or a certified nurse midwife (as defined in section 1861(gg)(2)), subparagraph (D) of this sentence shall apply to such services and such anesthetist, practitioner, specialist, or nurse-midwife in the same manner as such subparagraph applies to physicians\u2019 services furnished by physicians .\nV\nEffective Date\n#### 501. Effective date\nThe provisions of, including the amendments made by, this Act (other than sections 103 and 401) shall apply with respect to items and services furnished on or after the date that is 90 days after the date of the enactment of this Act. Notwithstanding any other provision of law, the Secretary of Health and Human Services shall implement such provisions, including such amendments, through interim final rule or subregulatory guidance if the Secretary determines such implementation to be necessary for purposes of complying with the preceding sentence or with any other effective date provided in this Act.",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-25",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "717",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Increasing Access to Quality Cardiac Rehabilitation Care Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-13",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1317",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "I CAN Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Blood and blood diseases",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-06-13T19:10:51Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2025-06-13T19:10:50Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-06-13T19:10:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T15:02:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s575",
          "measure-number": "575",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s575v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Improving Care and Access to Nurses Act or the I CAN Act</b></p> <p>This bill allows other health care providers besides physicians (e.g., nurses) to provide certain services under Medicare and Medicaid. </p> <p>Among other changes, the bill (1) allows a nurse practitioner or physician assistant to fulfill documentation requirements for Medicare coverage of special shoes for diabetic individuals; (2) expedites the ability of physician assistants, nurse practitioners, and clinical nurse specialists to supervise Medicare cardiac, intensive cardiac, and pulmonary rehabilitation programs; and (3) allows nurse practitioners to certify the need for inpatient hospital services under Medicare and Medicaid.</p>"
        },
        "title": "I CAN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s575.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Improving Care and Access to Nurses Act or the I CAN Act</b></p> <p>This bill allows other health care providers besides physicians (e.g., nurses) to provide certain services under Medicare and Medicaid. </p> <p>Among other changes, the bill (1) allows a nurse practitioner or physician assistant to fulfill documentation requirements for Medicare coverage of special shoes for diabetic individuals; (2) expedites the ability of physician assistants, nurse practitioners, and clinical nurse specialists to supervise Medicare cardiac, intensive cardiac, and pulmonary rehabilitation programs; and (3) allows nurse practitioners to certify the need for inpatient hospital services under Medicare and Medicaid.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119s575"
    },
    "title": "I CAN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Improving Care and Access to Nurses Act or the I CAN Act</b></p> <p>This bill allows other health care providers besides physicians (e.g., nurses) to provide certain services under Medicare and Medicaid. </p> <p>Among other changes, the bill (1) allows a nurse practitioner or physician assistant to fulfill documentation requirements for Medicare coverage of special shoes for diabetic individuals; (2) expedites the ability of physician assistants, nurse practitioners, and clinical nurse specialists to supervise Medicare cardiac, intensive cardiac, and pulmonary rehabilitation programs; and (3) allows nurse practitioners to certify the need for inpatient hospital services under Medicare and Medicaid.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119s575"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s575is.xml"
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
      "title": "I CAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "I CAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Care and Access to Nurses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles XVIII and XIX of the Social Security Act to increase access to services provided by advanced practice registered nurses under the Medicare and Medicaid programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:15Z"
    }
  ]
}
```
