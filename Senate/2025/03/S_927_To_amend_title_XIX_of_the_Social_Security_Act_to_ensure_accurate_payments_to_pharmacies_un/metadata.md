# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/927?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/927
- Title: Protecting Pharmacies in Medicaid Act
- Congress: 119
- Bill type: S
- Bill number: 927
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-03-09T20:27:24Z
- Update date including text: 2026-03-09T20:27:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/927",
    "number": "927",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Protecting Pharmacies in Medicaid Act",
    "type": "S",
    "updateDate": "2026-03-09T20:27:24Z",
    "updateDateIncludingText": "2026-03-09T20:27:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T15:46:46Z",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "KS"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s927is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 927\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Welch (for himself, Mr. Marshall , Mr. Warner , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to ensure accurate payments to pharmacies under Medicaid and to prevent the use of abusive spread pricing practices under Medicaid.\n#### 1. Short title\nThis Act may be cited as the Protecting Pharmacies in Medicaid Act .\n#### 2. Ensuring accurate payments to pharmacies under Medicaid\n##### (a) In general\nSection 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)\u2014\n**(A)**\nby redesignating clause (ii) as clause (iii); and\n**(B)**\nby striking and after the semicolon at the end of clause (i) and all that precedes it through (1) and inserting the following:\n(1) Determining pharmacy actual acquisition costs The Secretary shall conduct a survey of retail community pharmacy drug prices and applicable non-retail pharmacy drug prices to determine national average drug acquisition cost benchmarks (as such term is defined by the Secretary) as follows: (A) Use of vendor The Secretary may contract services for\u2014 (i) with respect to retail community pharmacies, the determination of retail survey prices of the national average drug acquisition cost for covered outpatient drugs that represent a nationwide average of consumer purchase prices for such drugs, net of all discounts, rebates, and other price concessions (to the extent any information with respect to such discounts, rebates, and other price concessions is available) based on a monthly survey of such pharmacies; and (ii) with respect to applicable non-retail pharmacies\u2014 (I) the determination of survey prices, separate from the survey prices described in clause (i), of the non-retail national average drug acquisition cost for covered outpatient drugs that represent a nationwide average of consumer purchase prices for such drugs, net of all discounts, rebates, and other price concessions (to the extent any information with respect to such discounts, rebates, and other price concessions is available) based on a monthly survey of such pharmacies; and (II) at the discretion of the Secretary, for each type of applicable non-retail pharmacy, the determination of survey prices, separate from the survey prices described in clause (i) or subclause (I) of this clause, of the national average drug acquisition cost for such type of pharmacy for covered outpatient drugs that represent a nationwide average of consumer purchase prices for such drugs, net of all discounts, rebates, and other price concessions (to the extent any information with respect to such discounts, rebates, and other price concessions is available) based on a monthly survey of such pharmacies; and ;\n**(2)**\nin subparagraph (B) of paragraph (1), by striking subparagraph (A)(ii) and inserting subparagraph (A)(iii) ;\n**(3)**\nin subparagraph (D) of paragraph (1), by striking clauses (ii) and (iii) and inserting the following:\n(ii) The vendor must update the Secretary no less often than monthly on the survey prices for covered outpatient drugs. (iii) The vendor must differentiate, in collecting and reporting survey data, for all cost information collected, whether a pharmacy is a retail community pharmacy or an applicable non-retail pharmacy, including whether such pharmacy is an affiliate (as defined in subsection (k)(14)), and, in the case of an applicable non-retail pharmacy, which type of applicable non-retail pharmacy it is using the relevant pharmacy type indicators included in the guidance required by subsection (d)(2) of section 2 of the Protecting Pharmacies in Medicaid Act . ;\n**(4)**\nby adding at the end of paragraph (1) the following:\n(F) Survey reporting In order to meet the requirement of section 1902(a)(54), a State shall require that any retail community pharmacy or applicable non-retail pharmacy in the State that receives any payment, reimbursement, administrative fee, discount, rebate, or other price concession related to the dispensing of covered outpatient drugs to individuals receiving benefits under this title, regardless of whether such payment, reimbursement, administrative fee, discount, rebate, or other price concession is received from the State or a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)) directly or from a pharmacy benefit manager or another entity that has a contract with the State or a managed care entity or other specified entity (as so defined), shall respond to surveys conducted under this paragraph. (G) Survey information Information on national drug acquisition prices obtained under this paragraph shall be made publicly available in a form and manner to be determined by the Secretary and shall include at least the following: (i) The monthly response rate to the survey including a list of pharmacies not in compliance with subparagraph (F). (ii) The sampling methodology and number of pharmacies sampled monthly. (iii) Information on price concessions to pharmacies, including discounts, rebates, and other price concessions, to the extent that such information may be publicly released and has been collected by the Secretary as part of the survey. (H) Penalties (i) In general Subject to clauses (ii), (iii), and (iv), the Secretary shall enforce the provisions of this paragraph with respect to a pharmacy through the establishment of civil money penalties applicable to a retail community pharmacy or an applicable non-retail pharmacy. (ii) Basis for penalties The Secretary shall impose a civil money penalty established under this subparagraph on a retail community pharmacy or applicable non-retail pharmacy if\u2014 (I) the retail pharmacy or applicable non-retail pharmacy refuses or otherwise fails to respond to a request for information about prices in connection with a survey under this subsection; (II) knowingly provides false information in response to such a survey; or (III) otherwise fails to comply with the requirements established under this paragraph. (iii) Parameters for penalties (I) In general A civil money penalty established under this subparagraph may be assessed with respect to each violation, and with respect to each non-compliant retail community pharmacy (including a pharmacy that is part of a chain) or non-compliant applicable non-retail pharmacy (including a pharmacy that is part of a chain), in an amount not to exceed $100,000 for each such violation. (II) Considerations In determining the amount of a civil money penalty imposed under this subparagraph, the Secretary may consider the size, business structure, and type of pharmacy involved, as well as the type of violation and other relevant factors, as determined appropriate by the Secretary. (iv) Rule of application The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil money penalty under this subparagraph in the same manner as such provisions apply to a civil money penalty or proceeding under section 1128A(a). (I) Limitation on use of applicable non-retail pharmacy pricing information No State shall use pricing information reported by applicable non-retail pharmacies under subparagraph (A)(ii) to develop or inform payment methodologies for retail community pharmacies. ;\n**(5)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by inserting , including payment rates and methodologies for determining ingredient cost reimbursement under managed care entities or other specified entities (as such terms are defined in section 1903(m)(9)(D)), after under this title ; and\n**(B)**\nin subparagraph (B), by inserting and the basis for such dispensing fees before the semicolon;\n**(6)**\nby redesignating paragraph (4) as paragraph (5);\n**(7)**\nby inserting after paragraph (3) the following new paragraph:\n(4) Oversight (A) In general The Inspector General of the Department of Health and Human Services shall conduct periodic studies of the survey data reported under this subsection, as appropriate, including with respect to substantial variations in acquisition costs or other applicable costs, as well as with respect to how internal transfer prices and related party transactions may influence the costs reported by pharmacies that are affiliates (as defined in subsection (k)(14)) or are owned by, controlled by, or related under a common ownership structure with a wholesaler, distributor, or other entity that acquires covered outpatient drugs relative to costs reported by pharmacies not affiliated with such entities. The Inspector General shall provide periodic updates to Congress on the results of such studies, as appropriate, in a manner that does not disclose trade secrets or other proprietary information. (B) Appropriation There is appropriated to the Inspector General of the Department of Health and Human Services, out of any money in the Treasury not otherwise appropriated, $5,000,000 for fiscal year 2026, to remain available until expended, to carry out this paragraph. ; and\n**(8)**\nin paragraph (5), as so redesignated\u2014\n**(A)**\nby inserting , and $9,000,000 for fiscal year 2026 and each fiscal year thereafter, after 2010 ; and\n**(B)**\nby inserting Funds appropriated under this paragraph for fiscal year 2026 and any subsequent fiscal year shall remain available until expended. after the period.\n##### (b) Definitions\nSection 1927(k) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking In the section and inserting In this section ; and\n**(2)**\nby adding at the end the following new paragraphs:\n(12) Applicable non-retail pharmacy The term applicable non-retail pharmacy means a pharmacy that is licensed as a pharmacy by the State and that is not a retail community pharmacy, including a pharmacy that dispenses prescription medications to patients primarily through mail and specialty pharmacies. Such term does not include nursing home pharmacies, long-term care facility pharmacies, hospital pharmacies, clinics, charitable or not-for-profit pharmacies, government pharmacies, or low dispensing pharmacies (as defined by the Secretary). (13) Affiliate The term affiliate means any entity that is owned by, controlled by, or related under a common ownership structure with a pharmacy benefit manager or a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)). .\n##### (c) Effective date\n**(1) In general**\nSubject to paragraph (2), the amendments made by this section shall take effect on the first day of the first quarter that begins on or after the date that is 6 months after the date of enactment of this Act.\n**(2) Delayed application to applicable non-retail pharmacies**\nThe pharmacy survey requirements established by the amendments to section 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ) made by this section shall apply to retail community pharmacies beginning on the effective date described in paragraph (1), but shall not apply to applicable non-retail pharmacies until the first day of the first quarter that begins on or after the date that is 18 months after the date of enactment of this Act.\n##### (d) Identification of applicable non-Retail pharmacies\n**(1) In general**\nNot later than January 1, 2027, the Secretary of Health and Human Services shall, in consultation with stakeholders as appropriate, publish guidance specifying pharmacies that meet the definition of applicable non-retail pharmacies (as such term is defined in subsection (k)(12) of section 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ), as added by subsection (b)), and that will be subject to the survey requirements under subsection (f)(1) of such section, as amended by subsection (a).\n**(2) Inclusion of pharmacy type indicators**\nThe guidance published under paragraph (1) shall include pharmacy type indicators to distinguish between different types of applicable non-retail pharmacies, such as pharmacies that dispense prescriptions primarily through the mail and pharmacies that dispense prescriptions that require special handling or distribution. An applicable non-retail pharmacy may be identified through multiple pharmacy type indicators.\n##### (e) Implementation\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by this section by program instruction or otherwise.\n**(2) Nonapplication of Administrative Procedure Act**\nImplementation of the amendments made by this section shall be exempt from the requirements of section 553 of title 5, United States Code.\n##### (f) Nonapplication of paperwork reduction act\nChapter 35 of title 44, United States Code, shall not apply to any data collection undertaken by the Secretary of Health and Human Services under section 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ), as amended by this section.\n#### 3. Preventing the use of abusive spread pricing in Medicaid\n##### (a) In general\nSection 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ) is amended\u2014\n**(1)**\nin subsection (e), by adding at the end the following new paragraph:\n(6) Transparent prescription drug pass-through pricing required (A) In general A contract between the State and a pharmacy benefit manager (referred to in this paragraph as a PBM ), or a contract between the State and a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D) and collectively referred to in this paragraph as the entity ) that includes provisions making the entity responsible for coverage of covered outpatient drugs dispensed to individuals enrolled with the entity, shall require that payment for such drugs and related administrative services (as applicable), including payments made by a PBM on behalf of the State or entity, is based on a transparent prescription drug pass-through pricing model under which\u2014 (i) any payment made by the entity or the PBM (as applicable) for such a drug\u2014 (I) is limited to\u2014 (aa) ingredient cost; and (bb) a professional dispensing fee that is not less than the professional dispensing fee that the State would pay if the State were making the payment directly in accordance with the State plan; (II) is passed through in its entirety (except as reduced under Federal or State laws and regulations in response to instances of waste, fraud, or abuse) by the entity or PBM to the pharmacy or provider that dispenses the drug; and (III) is made in a manner that is consistent with sections 447.502, 447.512, 447.514, and 447.518 of title 42, Code of Federal Regulations (or any successor regulation) as if such requirements applied directly to the entity or the PBM, except that any payment by the entity or the PBM for the ingredient cost of such drug purchased by a covered entity (as defined in subsection (a)(5)(B)) may exceed the actual acquisition cost (as defined in 447.502 of title 42, Code of Federal Regulations, or any successor regulation) for such drug if\u2014 (aa) such drug was subject to an agreement under section 340B of the Public Health Service Act; (bb) such payment for the ingredient cost of such drug does not exceed the maximum payment that would have been made by the entity or the PBM for the ingredient cost of such drug if such drug had not been purchased by such covered entity; and (cc) such covered entity reports to the Secretary (in a form and manner specified by the Secretary), on an annual basis and with respect to payments for the ingredient costs of such drugs so purchased by such covered entity that are in excess of the actual acquisition costs for such drugs, the aggregate amount of such excess; (ii) payment to the entity or the PBM (as applicable) for administrative services performed by the entity or PBM is limited to an administrative fee that reflects the fair market value (as defined by the Secretary) of such services; (iii) the entity or the PBM (as applicable) makes available to the State, and the Secretary upon request in a form and manner specified by the Secretary, all costs and payments related to covered outpatient drugs and accompanying administrative services (as described in clause (ii)) incurred, received, or made by the entity or the PBM, broken down (as specified by the Secretary), to the extent such costs and payments are attributable to an individual covered outpatient drug, by each such drug, including any ingredient costs, professional dispensing fees, administrative fees (as described in clause (ii)), post-sale and post-invoice fees, discounts, or related adjustments such as direct and indirect remuneration fees, and any and all other remuneration, as defined by the Secretary; and (iv) any form of spread pricing whereby any amount charged or claimed by the entity or the PBM (as applicable) that exceeds the amount paid to the pharmacies or providers on behalf of the State or entity, including any post-sale or post-invoice fees, discounts, or related adjustments such as direct and indirect remuneration fees or assessments, as defined by the Secretary, (after allowing for an administrative fee as described in clause (ii)) is not allowable for purposes of claiming Federal matching payments under this title. (B) Publication of information The Secretary shall publish, not less frequently than on an annual basis and in a manner that does not disclose the identity of a particular covered entity or organization, information received by the Secretary pursuant to subparagraph (A)(iii)(III) that is broken out by State and by each of the following categories of covered entity within each such State: (i) Covered entities described in subparagraph (A) of section 340B(a)(4) of the Public Health Service Act. (ii) Covered entities described in subparagraphs (B) through (K) of such section. (iii) Covered entities described in subparagraph (L) of such section. (iv) Covered entities described in subparagraph (M) of such section. (v) Covered entities described in subparagraph (N) of such section. (vi) Covered entities described in subparagraph (O) of such section. ; and\n**(2)**\nin subsection (k), as amended by section 2(b), by adding at the end the following new paragraph:\n(14) Pharmacy benefit manager The term pharmacy benefit manager means any person or entity that, either directly or through an intermediary, acts as a price negotiator or group purchaser on behalf of a State, managed care entity (as defined in section 1903(m)(9)(D)), or other specified entity (as so defined), or manages the prescription drug benefits provided by a State, managed care entity, or other specified entity, including the processing and payment of claims for prescription drugs, the performance of drug utilization review, the processing of drug prior authorization requests, the managing of appeals or grievances related to the prescription drug benefits, contracting with pharmacies, controlling the cost of covered outpatient drugs, or the provision of services related thereto. Such term includes any person or entity that acts as a price negotiator (with regard to payment amounts to pharmacies and providers for a covered outpatient drug or the net cost of the drug) or group purchaser on behalf of a State, managed care entity, or other specified entity or that carries out 1 or more of the other activities described in the preceding sentence, irrespective of whether such person or entity calls itself a pharmacy benefit manager. .\n##### (b) Conforming amendments\nSection 1903(m) of such Act ( 42 U.S.C. 1396b(m) ) is amended\u2014\n**(1)**\nin paragraph (2)(A)(xiii)\u2014\n**(A)**\nby striking and (III) and inserting (III) ;\n**(B)**\nby inserting before the period at the end the following: , and (IV) if the contract includes provisions making the entity responsible for coverage of covered outpatient drugs, the entity shall comply with the requirements of section 1927(e)(6) ; and\n**(C)**\nby moving the margin 2 ems to the left; and\n**(2)**\nby adding at the end the following new paragraph:\n(10) No payment shall be made under this title to a State with respect to expenditures incurred by the State for payment for services provided by an other specified entity (as defined in paragraph (9)(D)(iii)) unless such services are provided in accordance with a contract between the State and such entity which satisfies the requirements of paragraph (2)(A)(xiii). .\n##### (c) Effective date\nThe amendments made by this section shall apply to contracts between States and managed care entities, other specified entities, or pharmacy benefit managers that have an effective date beginning on or after the date that is 18 months after the date of enactment of this Act.\n##### (d) Implementation\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary of Health and Human Services may implement the amendments made by this section by program instruction or otherwise.\n**(2) Nonapplication of administrative procedure act**\nImplementation of the amendments made by this section shall be exempt from the requirements of section 553 of title 5, United States Code.\n##### (e) Nonapplication of paperwork reduction act\nChapter 35 of title 44, United States Code, shall not apply to any data collection undertaken by the Secretary of Health and Human Services under section 1927(e) of the Social Security Act ( 42 U.S.C. 1396r\u20138(e) ), as amended by this section.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
        "updateDate": "2025-05-07T14:14:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s927",
          "measure-number": "927",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s927v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Pharmacies in Medicaid Act</strong></p><p>This bill provides funds beginning in FY2026 for the Centers for Medicare & Medicaid Services to survey retail and non-retail pharmacies (e.g., mail-order pharmacies) to determine average prices of covered outpatient drugs under Medicaid. Pharmacies that fail to participate in the surveys are subject to civil penalties.</p><p>The bill additionally provides funds for FY2026 for the Office of the Inspector General of the Department of Health and Human Services to study the results of the survey and report accordingly to Congress.</p><p>The bill also requires pass-through pricing models, and prohibits spread-pricing, for payment arrangements with pharmacy benefit managers under Medicaid.</p>"
        },
        "title": "Protecting Pharmacies in Medicaid Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s927.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Pharmacies in Medicaid Act</strong></p><p>This bill provides funds beginning in FY2026 for the Centers for Medicare & Medicaid Services to survey retail and non-retail pharmacies (e.g., mail-order pharmacies) to determine average prices of covered outpatient drugs under Medicaid. Pharmacies that fail to participate in the surveys are subject to civil penalties.</p><p>The bill additionally provides funds for FY2026 for the Office of the Inspector General of the Department of Health and Human Services to study the results of the survey and report accordingly to Congress.</p><p>The bill also requires pass-through pricing models, and prohibits spread-pricing, for payment arrangements with pharmacy benefit managers under Medicaid.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119s927"
    },
    "title": "Protecting Pharmacies in Medicaid Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Pharmacies in Medicaid Act</strong></p><p>This bill provides funds beginning in FY2026 for the Centers for Medicare & Medicaid Services to survey retail and non-retail pharmacies (e.g., mail-order pharmacies) to determine average prices of covered outpatient drugs under Medicaid. Pharmacies that fail to participate in the surveys are subject to civil penalties.</p><p>The bill additionally provides funds for FY2026 for the Office of the Inspector General of the Department of Health and Human Services to study the results of the survey and report accordingly to Congress.</p><p>The bill also requires pass-through pricing models, and prohibits spread-pricing, for payment arrangements with pharmacy benefit managers under Medicaid.</p>",
      "updateDate": "2026-03-09",
      "versionCode": "id119s927"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s927is.xml"
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
      "title": "Protecting Pharmacies in Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Pharmacies in Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to ensure accurate payments to pharmacies under Medicaid and to prevent the use of abusive spread pricing practices under Medicaid.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:28Z"
    }
  ]
}
```
