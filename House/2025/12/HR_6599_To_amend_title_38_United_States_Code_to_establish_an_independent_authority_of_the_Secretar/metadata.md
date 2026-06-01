# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6599?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6599
- Title: Leasing and Infrastructure Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6599
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-21T08:08:50Z
- Update date including text: 2026-05-21T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6599",
    "number": "6599",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001195",
        "district": "8",
        "firstName": "Jason",
        "fullName": "Rep. Smith, Jason [R-MO-8]",
        "lastName": "Smith",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Leasing and Infrastructure Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:50Z",
    "updateDateIncludingText": "2026-05-21T08:08:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
        "item": [
          {
            "date": "2026-05-20T13:25:19Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:44:55Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-10T15:04:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6599ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6599\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Smith of Missouri introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish an independent authority of the Secretary of Veterans Affairs to enter into leases for major medical facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leasing and Infrastructure Act of 2025 .\n#### 2. Independent authority of the Secretary of Veterans Affairs to enter into leases for major medical facilities; establishment of Veterans Leasing Fund\n##### (a) Independent authority\nSection 8103 of title 38, United States Code, is amended by adding at the end the following new subsections:\n(i) Independent leasing authority (1) Notwithstanding section 3307 of title 40, the Secretary may enter into a lease for any major medical facility (as defined in section 8104 of this title) without delegation from the Administrator of General Services, if the prospectus for such a lease has been\u2014 (A) approved by the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate; and (B) transmitted concurrently to\u2014 (i) the Committee on Transportation and Infrastructure of the House of Representatives; and (ii) the Committee on Environment and Public Works of the Senate. (2) (A) The firm term of a lease under this subsection may not exceed 20 years. No lease under this subsection may be extended beyond the firm term unless\u2014 (i) such extension is authorized in the prospectus; or (ii) Congress approves such extension. (B) For purposes of this paragraph, the term firm term means the initial, non-cancellable lease period approved in the prospectus. (3) A lease under this subsection\u2014 (A) may be executed only to the extent and in the amount provided in advance in the Veterans Leasing Fund established by subsection (j); and (B) shall be scored and funded in accordance with Office of Management and Budget Circular A\u201311. (4) (A) In exercising the authority under this subsection, the Secretary shall, for each purpose-built medical facility constructed pursuant to a lease awarded under this subsection in each locality, submit to Congress accurate, market-based cost estimates. Such estimates shall\u2014 (i) account for construction costs, material costs, and land acquisition costs; and (ii) be informed by qualified sources, including licensed appraisers, valuation experts, professional estimating firms, or commercial real estate firms. (B) The Secretary may also request technical assistance from the Administrator of General Services with respect to market surveys, cost estimation, or lease scoring. (C) If, at any point in the procurement process (including during cost estimation, the expression of interest phase, or upon receipt of pricing from offerors) projected costs exceed approved estimates by more than ten percent, or exceed any congressional budget authority, the Secretary shall, not later than 30 days after the date on which the Secretary is notified of such projected costs, submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate, the Committee on Transportation and Infrastructure of the House of Representatives, and the Committee on Environment and Public Works a notification that such projected costs exceed approved estimates or congressional budget authority, as the case may be. (j) Veterans leasing fund (1) There is established in the Treasury a revolving fund to be known as the Veterans Leasing Fund (in this subsection referred to as the Fund ). (2) There shall be deposited in the Fund\u2014 (A) amounts appropriated for the purpose of carrying out the independent leasing authority under subsection (i); and (B) amounts transferred, on a reimbursable or nonreimbursable basis, from the Medical Facilities account of the Department (or any successor account) for the payment of annual rent, taxes, or operating costs for leases executed under subsection (i). (3) Amounts in the Fund are hereby made available as contract authority to enter into obligations to carry out subsection (i), including obligations in advance of receipts. (4) The Secretary may obligate amounts in the Fund for rental payments, tenant improvements, real-estate taxes, operating expenses, and pre-award due diligence costs, including design, environmental, and professional service fees associated with leases entered into pursuant to subsection (i). (5) The Secretary shall include, in the annual budget justification materials submitted to Congress in support of the Department\u2014 (A) the projected unobligated balance of the Fund; (B) new obligations; and (C) collections for the year covered by such budget justification materials and the four fiscal years succeeding such year. (k) One-Year target for lease awards; annual report (1) The Secretary shall, to the maximum extent practicable, award a lease for a major medical facility not later than not later than the end of the one year period beginning on the date on which the Secretary issues a solicitation for the lease agreement. (2) The Secretary shall revise internal guidance, milestone reviews, and approval workflows to\u2014 (A) support the requirement under paragraph (1); and (B) eliminate duplicative or sequential reviews that delay procurement. (3) A contracting officer may not issue a solicitation described in paragraph (1) unless, before the date of issuance, the officer has placed in the official contract file a written certification that\u2014 (A) sufficient funds are obligated to cover all due diligence and pre-award professional services reasonably anticipated for the project, including environmental, geotechnical, title, survey, appraisal, brokerage, and architectural-engineering services; and (B) each such service is available for task-order issuance within 30 days under an existing indefinite-delivery, indefinite-quantity contract or other competitively-awarded vehicle. (4) Obligations under paragraph (3) may be made from the Veterans Leasing Fund established in subsection (j) or from other appropriations for medical facilities that are available for the applicable fiscal year. (5) (A) As part of the public notice during the expression of interest phase of the acquisition process, the Secretary shall require each prospective developer to provide price estimates, including the cost of land, to enable the Department to evaluate whether projected costs are at or below the unserviced shell rent authorized in the approved prospectus. (B) (i) If such estimates exceed such amount authorized, the Secretary shall, not later than 14 days after the date on which the Secretary completes such evaluation, submit to Congress a notification that such estimates exceed such authorized amount. (ii) Not later than 45 days after the date on which the Secretary submits the notification under clause (i), the Department shall finalize a plan to address the discrepancy between such estimates and such authorized amount, which may include\u2014 (I) reducing the scope of the project; (II) requesting additional budget authority; or (III) postponing, or canceling the project, as appropriate. (C) To the maximum extent practicable, the Secretary shall, not later than 60 days after the date on which the Secretary submits the notification under subparagraph (B), notify prospective offerors of the potential effect to procurement timelines, including the estimated release date of the request for lease proposals. (6) The Secretary shall include, in any request for a lease proposal made pursuant to the leasing authority under subsection (i)\u2014 (A) a summary of the procurement milestones applicable to such request; and (B) a statement that a reimbursement under paragraph (7) would become effective on the date that is one year after the date on which the Secretary issued such request. (7) (A) If the Secretary does not award a lease pursuant to a request for a lease proposal before the date that is one year after the date on which the Secretary issued such request, the Secretary shall be required to reimburse each prospective lessor in the competitive range for costs directly associated with the delay in awarding the lease. (B) Any reimbursement under subparagraph (A) shall be calculated based on one percent annually (paid in equal monthly installments of one-twelfth of one percent) of the average land acquisition cost, as proposed by all offerors remaining in the competitive range under the request. (C) Payment of such reimbursements under this paragraph shall cease\u2014 (i) immediately upon the award of the lease; or (ii) the date on which the project is cancelled, if applicable. (D) The Secretary shall issue guidance establishing documentation requirements and procedures for administering reimbursements under this paragraph. (8) Not later than March 1 of each year, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes\u2014 (A) a list of each major medical facility lease for which a request was issued during the preceding calendar year; (B) a statement of whether the lease was awarded within the one year period described in paragraph (1); and (C) for any lease not awarded within such period, an explanation of the reasons the lease was not awarded during such period. (9) Not later than 90 days after the date of the enactment of this subsection, the Secretary shall issue internal guidance that establishes the policies and thresholds the Secretary determines necessary to administer the requirements of this subsection. (l) Revisions To design guides (1) Not later than 180 days after the date of enactment of this subsection, and not less frequently than once every five years thereafter, the Secretary shall revise the design guides of the Department applicable to outpatient clinics and other leased medical facilities. (2) In carrying out paragraph (1), the Secretary shall consult with subject matter experts, including health care professionals and representatives of the private health care industry. (3) Any revision to design guides conducted pursuant to this section shall not be over-engineered or unnecessarily prescriptive specifications unless required for clinical safety, functional performance, or applicable building codes. (m) Mitigation of risk premiums (1) The Secretary may include in a lease agreement under this chapter terms that mitigate risk premiums to the Department, including\u2014 (A) post-occupancy self-insurance arrangements by the Department; (B) reimbursement to a prospective lessor for reasonable holding costs incurred as a result of delays attributable to the Department in excess of established procurement milestones; (C) authorization to structure major medical facility leases as triple-net leases (NNN) or modified-gross leases, as appropriate, to align with prevailing commercial market practices; and (D) definitions of the terms shell work and tenant improvements to ensure cost allocation is consistent with prevailing commercial market standards. (2) Not later than 180 days after the date of enactment of this subsection, the Secretary shall issue guidance with respect to the use of such terms in lease agreements under this chapter. In such guidance, the Secretary shall ensure\u2014 (A) heating, ventilation, and air conditioning system capacity is included in the definition of shell work ; and (B) heating, ventilation, and air conditioning distribution and controls required to meet tenant-specific needs are included in the definition of tenant improvements , unless otherwise negotiated. (3) For purposes of this subsection, the term triple-net lease means a lease under which the lessee is responsible for payment of real estate taxes, insurance, utilities, janitorial services, and routine operating costs. (n) Consolidation of documentation The Secretary shall consolidate internal documentation required to support lease decisions under this chapter into a single decision memorandum, to the maximum extent practicable. Such memorandum shall include project justification, site selection rationale, estimated costs, design summary, and other information necessary for internal approval and submission to Congress. .\n##### (b) Conforming amendment\nSection 8104(a)(3)(B)(i) of title 38, United States Code, is amended by striking through the General Services Administration under section 3307(a) of title 40 .\n##### (c) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Veterans Leasing Fund established under section 8103 of title 38, United States Code, (as amended by this Act), such amounts as may be specifically authorized for lease obligations under subsection (i) of such section (as added by this Act).\n**(2) Deposit of future appropriations**\nAny amounts appropriated for lease obligations for a fiscal year shall be deposited in the Veterans Leasing Fund.\n#### 3. Cost estimation requirements for major medical facility leases\nSection 8104(b)(2) of such title is amended\u2014\n**(1)**\nby striking Whenever and inserting (A) Whenever ;\n**(2)**\nby redesignating subparagraphs (A) through (E) as clauses (i) through (v), respectively;\n**(3)**\nin subparagraph (A), as designated by paragraph (1)\u2014\n**(A)**\nin clause (v), as so redesignated\u2014\n**(i)**\nby redesignating clauses (i) through (iii) as subclauses (I) through (III), respectively; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(B)**\nby adding at the end the following new clause:\n(vi) A market-based cost estimate for the facility to be leased that includes an evaluation of\u2014 (I) local land values; (II) applicable construction costs; and (III) other cost factors the Secretary determines relevant to build-to-suit facilities. ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(B) (i) The Secretary shall adopt and apply a standardized methodology for estimating the full life-cycle cost of major medical facility leases and prospectus-level leases. (ii) Such methodology shall include, at a minimum\u2014 (I) base rent projections over the full lease term; (II) tenant improvement and buildout costs based on current medical facility standards; (III) estimated operating expenses, including utilities, maintenance, and security; (IV) annual escalation factors tied to construction cost indices, labor rates, and market trends; (V) cost assumptions for option periods or potential renewal terms; and (VI) geographic adjustments using current regional market data to reflect location-specific construction and leasing conditions. (iii) To reflect inflation and market escalation, the Secretary shall annually adjust each cost estimate for a lease submitted to Congress for authorization or prospectus approval during the period beginning on the date on which the Secretary submits the first cost estimate for the lease and ending on the projected award date for the lease. In adjusting a cost estimate pursuant to this subparagraph, the Secretary shall use such medical construction or real estate indices as the Secretary determines appropriate. (iv) If the Secretary does not award a lease during the one year period beginning on the date on which the Secretary completes a cost estimate for the lease pursuant to this paragraph, the Secretary shall update and revalidate such cost estimate prior to obligating any funds for the lease or submitting such cost estimate to Congress. .\n#### 4. Development of streamlined procurement model; report\nNot later than 180 days after the date of enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Comptroller General of the United States, the Director of the Office of Management and Budget, and private sector stakeholders, shall develop a revised process for the procurement of major medical facility leases under chapter 81 of title 38, United States Code, and submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes a description of such revised process.",
      "versionDate": "2025-12-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-08T16:58:11Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6599ih.xml"
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
      "title": "To amend title 38, United States Code, to establish an independent authority of the Secretary of Veterans Affairs to enter into leases for major medical facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:18Z"
    },
    {
      "title": "Leasing and Infrastructure Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Leasing and Infrastructure Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:20Z"
    }
  ]
}
```
