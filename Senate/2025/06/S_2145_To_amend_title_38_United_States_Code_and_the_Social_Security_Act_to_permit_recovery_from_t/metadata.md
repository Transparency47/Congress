# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2145
- Title: GUARD Veterans’ Health Care Act
- Congress: 119
- Bill type: S
- Bill number: 2145
- Origin chamber: Senate
- Introduced date: 2025-06-23
- Update date: 2026-01-10T07:33:59Z
- Update date including text: 2026-01-10T07:33:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in Senate
- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-06-23: Introduced in Senate

## Actions

- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2145",
    "number": "2145",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "GUARD Veterans\u2019 Health Care Act",
    "type": "S",
    "updateDate": "2026-01-10T07:33:59Z",
    "updateDateIncludingText": "2026-01-10T07:33:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T22:32:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2145is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2145\nIN THE SENATE OF THE UNITED STATES\nJune 23, 2025 Ms. Warren (for herself, Mr. Blumenthal , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, and the Social Security Act to permit recovery from the Department of Veterans Affairs of costs from Medicare Advantage and Medicare prescription drug plans and to modify the authority for recovery by the United States of reasonable charges for certain care or services furnished to veterans for non-service-connected disabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarantee Utilization of All Reimbursements for Delivery of Veterans\u2019 Health Care Act or the GUARD Veterans\u2019 Health Care Act .\n#### 2. Cost-recovery from Medicare Advantage and Medicare prescription drug plans\n##### (a) Cost recovery\n**(1) In general**\nSubchapter III of chapter 17 of title 38, United States Code, is amended by inserting after section 1729B the following new section:\n1729C. Cost-recovery from Medicare Advantage and Medicare prescription drug plans (a) In general Notwithstanding sections 1814(c), 1835(d), and 1862(a)(3) of the Social Security Act ( 42 U.S.C. 1395f(c) , 1395n(d), and 1395y(a)(3)), if the Secretary provides under this chapter any health care item or service (including for a service-connected disability or a non-service-connected disability) covered under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), including outpatient and inpatient care, prescription drugs, medical devices, lab testing, and items or services delivered in post-acute and long-term care settings, to any individual who is enrolled in a Medicare Advantage plan, including an MA\u2013PD plan, offered by a MA organization under part C of such title or a prescription drug plan offered by a PDP sponsor under part D of such title, such organization or sponsor shall, to the extent such item or service is covered under such Medicare Advantage plan or prescription drug plan, reimburse the Secretary for such item or service regardless of any additional documentation, utilization management, or other administrative requirement the plan may impose on the item or service. (b) Recovery of amounts (1) In general The Secretary shall recover amounts required to be reimbursed under subsection (a) through the use of procedures under section 1729 of this title to the same extent as those procedures are used to recover amounts authorized to be recovered under that section. (2) Amount and process Except as provided in paragraph (1), recovery under that paragraph of amounts reimbursed under subsection (a) shall be in such an amount, and occur in accordance with such procedures, as the Secretary shall prescribe for purposes of this section. (c) Application The provisions of subsection (a) shall apply to Medicare Advantage and prescription drug plan years beginning on or after January 1, 2026. (d) Treatment of amounts Amounts reimbursed to the Secretary under subsection (a) shall be deposited in the Department of Veterans Affairs Medical Care Collections Fund under section 1729A of this title. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1729B the following new item:\n1729C. Cost-recovery from Medicare Advantage and Medicare prescription drug plans. .\n##### (b) Medicare conforming amendments\n**(1) Part A**\nSection 1814(c) of the Social Security Act ( 42 U.S.C. 1395f(c) ) is amended by inserting and section 1729C of title 38, United States Code after section 1880 .\n**(2) Part B**\nSection 1835(d) of the Social Security Act ( 42 U.S.C. 1395n(d) ) is amended by inserting and section 1729C of title 38, United States Code after section 1880 .\n**(3) Exclusions from coverage**\nSection 1862(a)(3) of the Social Security Act ( 42 U.S.C. 1395y(a)(3) ) is amended by inserting in the case of items and services and prescription drugs for which reimbursement is made under section 1729C of title 38, United States Code, after section 1880(e), .\n#### 3. Modification of authority for recovery by United States of reasonable charges for certain care or services furnished to veterans for non-service-connected disabilities\nSection 1729 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) (A) Subject to the provisions of this section, the United States has the right to recover or collect the reasonable charges for care or services that the United States is required by law to furnish or pay for under this chapter for a non-service-connected disability. (B) The United States has the right to recover or collect from a third party the reasonable charges for care or services furnished as described in subparagraph (A) to the extent that the recipient or provider of the care or services would be eligible to receive payment from a third party. (C) The right to recover or collect reasonable charges for care or services under this section shall apply to any and all causes of action or recovery rights in tort or under any policy, plan, or contract providing benefits for health care or injury, which accrue to the individual to whom the care or services were furnished, or to the legal representatives of the individual, as a result of the non-service-connected disability that necessitated the care or services. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (D), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (E)(2), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(F) that is incurred by an individual who is entitled to care (or payment of expenses of care) under circumstances creating a tort liability upon a third party. ;\n**(2)**\nin subsection (b), by amending paragraph (2) to read as follows:\n(2) (A) The United States may take any action necessary to enforce the subrogation interests of the United States under this section, including by intervening or joining in an action or proceeding. (B) A proceeding under this section may not be brought after the end of the six-year period beginning on the last day on which the care or services for which recovery is sought are furnished. Notwithstanding the previous sentence, subject to section 2415 of title 28, and except as otherwise provided by law, any action for money damages under this section brought by the United States or an officer or agency thereof that is founded upon a tort shall be barred unless the complaint is filed within three years after the right of action first accrues. ;\n**(3)**\nin subsection (c)(1), by inserting or penalty after claim ;\n**(4)**\nby redesignating subsections (h) and (i) as subsections (l) and (m), respectively;\n**(5)**\nby inserting after subsection (f) the following new subsections:\n(g) (1) Not later than 45 days after receipt of a claim to recover or collect the reasonable charges for care or services described in subsection (a), or in the case of a tort, not later than 45 days after settlement, judgment, award, liability determination, or resolution relating to the cause of action, a third party shall\u2014 (A) pay a clean claim for reimbursement in accordance with this section; (B) pay the amount agreed to in writing by the Department; or (C) provide notice of the date the third party received the claim and include a statement that\u2014 (i) the third party refuses to reimburse all or part of the claim and specify each reason for the refusal to pay; or (ii) additional information is necessary to determine if all or part of the claim will be reimbursed and what specific additional information is necessary. (2) Paragraph (1) shall not apply to a claim if there is a good faith dispute about the legitimacy of the claim. (3) (A) If any third party fails to comply with paragraph (1), such third party shall be required to pay interest to the United States at the rate established by the Secretary of the Treasury under section 3717 of title 31 per month on the amount of the claim that remains unpaid at the end of the 45-day period specified in such paragraph. (B) The interest paid pursuant to subparagraph (A) shall be included in any late reimbursement from a third party without requiring the Secretary to make any additional claim for such interest. (4) (A) Upon receiving a request for additional information by a third party pursuant to paragraph (1)(C)(ii), the Secretary shall provide the additional information, if determined relevant by the Secretary, not later than 45 days after receipt of the request for additional information. (B) Failure to furnish relevant information within the time required under subparagraph (A) shall not invalidate or reduce any claim in connection with such information. (C) (i) Not later than 15 days after receipt of additional relevant information under subparagraph (A), a third party shall pay a clean claim in accordance with this subsection or send a written or electronic notice that\u2014 (I) such third party refuses to reimburse all or part of the claim; and (II) specifies each reason for refusal to pay. (ii) Any third party that fails to comply with clause (i) shall pay interest to the United States on any amount of the claim that remains unpaid at the rate established by the Secretary of the Treasury under section 3717 of title 31. (5) A third party shall not be entitled to request a refund to correct a payment error to the Department if the request by the third party for such payment correction is submitted more than 18 months after the date that the Department received payment from the third party. (6) Any claim by the Department under this section shall not be subject to non-Department claims processes, policies, or forms. (h) The recovery rights of the United States under this section are not limited to the amounts paid to non-Department providers and are not subject to non-Department fee schedules or non-Department reimbursement rates, including those administered under workers\u2019 compensation plans or automobile accident reparations insurance. (i) (1) A third party shall\u2014 (A) determine whether a recipient of care or services covered by this section (including a recipient whose claim is unresolved) has received benefits under this chapter; and (B) submit the information described in paragraph (2) with respect to the recipient to the Secretary in a form and manner (including frequency) specified by the Secretary. (2) The information required to be submitted under this paragraph with respect to a recipient of care or services is\u2014 (A) the identity of the recipient; and (B) such other information as the Secretary shall specify in order to enable the Secretary to make an appropriate determination concerning coordination of benefits, including any applicable recovery claim. (3) A third party shall submit the information required under paragraph (1)(B) with respect to a recipient of care or services covered by this section (including a recipient whose claim is unresolved) not later than 30 days, or such other time period as prescribed by the Secretary, after the date on which the third party knows or has reason to know that the recipient has received benefits under this chapter. (4) A third party shall not distribute proceeds of a settlement, judgment, award, or other payment in connection with a recipient of care or services covered by this section (including a recipient whose claim is unresolved), regardless of whether there has been a determination or admission of liability, without satisfaction of a claim by the Department. (j) (1) A third party that fails to comply with the requirements under this section, including any regulations prescribed to implement this section, with respect to any individual receiving care furnished or paid for by the Department as described in this section, shall be subject to a civil penalty in an amount published on a website of the Department for each day of noncompliance with respect to each claim violation. A civil penalty under this paragraph shall be in addition to any other penalties prescribed by law. (2) (A) A third party that willfully fails or refuses to pay a clean claim under this section, including any regulations prescribed to implement this section, with respect to any individual receiving care furnished or paid for by the Department as described in this section, shall be subject to paying the higher of triple the amount of the claim or an amount not to exceed $50,000, which may be adjusted for inflation, for each claim violation. (B) A penalty under subparagraph (A) is in addition to any other penalty under this subsection and any other penalty prescribed by law. (C) Before enforcing any penalty under this paragraph with respect to a third party, the Secretary shall provide to the third party written notice of the amount due and a 30-day opportunity to pay the clean claim, including penalties, interests, and costs. (3) Notwithstanding any other applicable civil or criminal remedies, the United States shall have a cause of action for damages (which shall be in an amount double the amount otherwise provided) in the case of a third party that fails to provide payment, or appropriate reimbursement, for the reasonable value of the care or services furnished, to be furnished, paid for, or to be paid for in accordance with a clean claim. (k) Notwithstanding any other provision of law, the Secretary may implement this paragraph by prescribing regulations, program instructions, or otherwise. ; and\n**(6)**\nin subsection (m), as redesignated by paragraph (4)\u2014\n**(A)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (C), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (D), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following new subparagraphs:\n(E) a person or entity responsible in tort for damages incurred as a result of negligence; or (F) a person or entity responsible for payment of medical expenses other than under a health-plan contract, including medical expenses coverage, medical payments coverage, or underinsured motorist coverage. ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(4) The term clean claim means a claim to recover or collect reasonable charges under subsection (a) that can be processed without obtaining additional information. (5) The term non-service-connected disability includes\u2014 (A) a non-service-connected disability, injury, illness, health care need, or condition; and (B) an aggravation or exacerbation of a service-connected disability. .",
      "versionDate": "2025-06-23",
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
        "actionDate": "2025-12-03",
        "text": "Committee Hearings Held"
      },
      "number": "4077",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GUARD Veterans\u2019 Health Care Act",
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
            "name": "Administrative remedies",
            "updateDate": "2025-12-08T19:42:34Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-12-08T19:42:34Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-08T19:42:34Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-12-08T19:42:34Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-12-08T19:42:34Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-12-08T19:42:34Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-12-08T19:42:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-09T15:29:13Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2145is.xml"
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
      "title": "GUARD Veterans\u2019 Health Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GUARD Veterans\u2019 Health Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guarantee Utilization of All Reimbursements for Delivery of Veterans\u2019 Health Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, and the Social Security Act to permit recovery from the Department of Veterans Affairs of costs from Medicare Advantage and Medicare prescription drug plans and to modify the authority for recovery by the United States of reasonable charges for certain care or services furnished to veterans for non-service-connected disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:26Z"
    }
  ]
}
```
