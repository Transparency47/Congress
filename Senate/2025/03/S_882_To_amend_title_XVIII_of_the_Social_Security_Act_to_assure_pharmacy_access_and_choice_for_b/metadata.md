# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/882?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/882
- Title: Patients Before Middlemen Act
- Congress: 119
- Bill type: S
- Bill number: 882
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-02-19T22:16:57Z
- Update date including text: 2026-02-19T22:16:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/882",
    "number": "882",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Patients Before Middlemen Act",
    "type": "S",
    "updateDate": "2026-02-19T22:16:57Z",
    "updateDateIncludingText": "2026-02-19T22:16:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T17:42:31Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "OK"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "VA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "KS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "VT"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NV"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s882is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 882\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mrs. Blackburn (for herself, Ms. Hassan , Mr. Lankford , Mr. Warner , Mr. Marshall , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to assure pharmacy access and choice for beneficiaries under prescription drug plans and MA\u2013PD plans and to establish requirements of pharmacy benefit managers under Medicare part D.\n#### 1. Short title\nThis Act may be cited as the Patients Before Middlemen Act .\n#### 2. Assuring pharmacy access and choice for Medicare beneficiaries\n##### (a) In general\nSection 1860D\u20134(b)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(1) ) is amended by striking subparagraph (A) and inserting the following:\n(A) In general (i) Participation of any willing pharmacy A PDP sponsor offering a prescription drug plan shall permit any pharmacy that meets the standard contract terms and conditions under such plan to participate as a network pharmacy of such plan. (ii) Contract terms and conditions (I) In general Notwithstanding any other provision of law, for plan years beginning on or after January 1, 2028, in accordance with clause (i), contract terms and conditions offered by such PDP sponsor shall be reasonable and relevant according to standards established by the Secretary under subclause (II). (II) Standards Not later than the first Monday in April of 2027, the Secretary shall establish standards for reasonable and relevant contract terms and conditions for purposes of this clause. (III) Request for information Not later than April 1, 2026, for purposes of establishing the standards under subclause (II), the Secretary shall issue a request for information to seek input on trends in prescription drug plan and network pharmacy contract terms and conditions, current prescription drug plan and network pharmacy contracting practices, whether pharmacy reimbursement and dispensing fees paid by PDP sponsors to network pharmacies sufficiently cover the ingredient and operational costs of such pharmacies, the use and application of pharmacy quality measures by PDP sponsors for network pharmacies, PDP sponsor restrictions or limitations on the dispensing of covered part D drugs by network pharmacies (or any subsets of such pharmacies), PDP sponsor auditing practices for network pharmacies, areas in current regulations or program guidance related to contracting between prescription drug plans and network pharmacies requiring clarification or additional specificity, factors for consideration in determining the reasonableness and relevance of contract terms and conditions between prescription drug plans and network pharmacies, and other issues as determined appropriate by the Secretary. .\n##### (b) Essential retail pharmacies\nSection 1860D\u201342 of the Social Security Act ( 42 U.S.C. 1395w\u2013152 ) is amended by adding at the end the following new subsection:\n(e) Essential retail pharmacies (1) In general With respect to plan years beginning on or after January 1, 2028, the Secretary shall publish reports, at least once every 2 years until 2034, and periodically thereafter, that provide information, to the extent feasible, on\u2014 (A) trends in ingredient cost reimbursement, dispensing fees, incentive payments and other fees paid by PDP sponsors offering prescription drug plans and MA organizations offering MA\u2013PD plans under this part to essential retail pharmacies (as defined in paragraph (2)) with respect to the dispensing of covered part D drugs, including a comparison of such trends between essential retail pharmacies and pharmacies that are not essential retail pharmacies; (B) trends in amounts paid to PDP sponsors offering prescription drug plans and MA organizations offering MA\u2013PD plans under this part by essential retail pharmacies with respect to the dispensing of covered part D drugs, including a comparison of such trends between essential retail pharmacies and pharmacies that are not essential retail pharmacies; (C) trends in essential retail pharmacy participation in pharmacy networks and preferred pharmacy networks for prescription drug plans offered by PDP sponsors and MA\u2013PD plans offered by MA organizations under this part, including a comparison of such trends between essential retail pharmacies and pharmacies that are not essential retail pharmacies; (D) trends in the number of essential retail pharmacies, including variation in such trends by geographic region or other factors; (E) a comparison of cost-sharing for covered part D drugs dispensed by essential retail pharmacies that are network pharmacies for prescription drug plans offered by PDP sponsors and MA\u2013PD plans offered by MA organizations under this part and cost-sharing for covered part D drugs dispensed by other network pharmacies for such plans located in similar geographic areas that are not essential retail pharmacies; (F) a comparison of the volume of covered part D drugs dispensed by essential retail pharmacies that are network pharmacies for prescription drug plans offered by PDP sponsors and MA\u2013PD plans offered by MA organizations under this part and such volume of dispensing by network pharmacies for such plans located in similar geographic areas that are not essential retail pharmacies, including information on any patterns or trends in such comparison specific to certain types of covered part D drugs, such as generic drugs or drugs specified as specialty drugs by a PDP sponsor under a prescription drug plan or an MA organization under an MA\u2013PD plan; and (G) a comparison of the information described in subparagraphs (A) through (F) between essential retail pharmacies that are network pharmacies for prescription drug plans offered by PDP sponsors under this part and essential retail pharmacies that are network pharmacies for MA\u2013PD plans offered by MA organizations under this part. (2) Definition of essential retail pharmacy In this subsection, the term essential retail pharmacy means, with respect to a plan year, a retail pharmacy that\u2014 (A) is not a pharmacy that is an affiliate as defined in paragraph (4); and (B) is located in\u2014 (i) a medically underserved area (as designated pursuant to section 330(b)(3)(A) of the Public Health Service Act); (ii) a rural area in which there is no other retail pharmacy within 10 miles, as determined by the Secretary; (iii) a suburban area in which there is no other retail pharmacy within 2 miles, as determined by the Secretary; or (iv) an urban area in which there is no other retail pharmacy within 1 mile, as determined by the Secretary. (3) List of essential retail pharmacies (A) Publication of list of essential retail pharmacies For each plan year (beginning with plan year 2028), the Secretary shall publish, on a publicly available internet website of the Centers for Medicare & Medicaid Services, a list of pharmacies that meet the criteria described in subparagraphs (A) and (B) of paragraph (2) to be considered an essential retail pharmacy. (B) Required submissions from pdp sponsors For each plan year (beginning with plan year 2028), each PDP sponsor offering a prescription drug plan and each MA organization offering an MA\u2013PD plan shall submit to the Secretary, for the purposes of determining retail pharmacies that meet the criterion specified in subparagraph (A) of paragraph (2), a list of retail pharmacies that are affiliates of such sponsor or organization, or are affiliates of a pharmacy benefit manager acting on behalf of such sponsor or organization, at a time, and in a form and manner, specified by the Secretary. (C) Reporting by pdp sponsors and ma organizations For each plan year beginning with plan year 2027, each PDP sponsor offering a prescription drug plan and each MA organization offering an MA\u2013PD plan under this part shall submit to the Secretary information on incentive payments and other fees paid by such sponsor or organization to pharmacies, insofar as any such payments or fees are not otherwise reported, at a time, and in a form and manner, specified by the Secretary. (D) Implementation Notwithstanding any other provision of law, the Secretary may implement this paragraph by program instruction or otherwise. (E) Nonapplication of paperwork reduction act Chapter 35 of title 44, United States Code, shall not apply to the implementation of this paragraph. (4) Definition of affiliate In this subsection, the term affiliate means any entity that is owned by, controlled by, or related under a common ownership structure with a pharmacy benefit manager or a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)). .\n##### (c) Enforcement\n**(1) In general**\nSection 1860D\u20134(b)(1) of the Social Security Act ( 42 U.S.C. 1395w\u2013104(b)(1) ) is amended by adding at the end the following new subparagraph:\n(F) Enforcement of standards for reasonable and relevant contract terms and conditions (i) Allegation submission process (I) In general Not later than January 1, 2028, the Secretary shall establish a process through which a pharmacy may submit to the Secretary an allegation of a violation by a PDP sponsor offering a prescription drug plan of the standards for reasonable and relevant contract terms and conditions under subparagraph (A)(ii), or of subclause (VIII) of this clause. (II) Frequency of submission (aa) In general Except as provided in item (bb), the allegation submission process under this clause shall allow pharmacies to submit any allegations of violations described in subclause (I) not more frequently than once per plan year per contract between a pharmacy and a PDP sponsor. (bb) Allegations relating to contract modifications In the case where a contract between a pharmacy and a PDP sponsor is modified following the submission of allegations by a pharmacy with respect to such contract and plan year, the allegation submission process under this clause shall allow such pharmacy to submit an additional allegation related to those modifications with respect to such contract and plan year. (III) Access to relevant documents and materials A PDP sponsor subject to an allegation under this clause\u2014 (aa) shall provide documents or materials, as specified by the Secretary, including contract offers made by such sponsor to such pharmacy or correspondence related to such offers, to the Secretary at a time, and in a form and manner, specified by the Secretary; and (bb) shall not prohibit or otherwise limit the ability of a pharmacy to submit such documents or materials to the Secretary for the purpose of submitting an allegation or providing evidence for such an allegation under this clause. (IV) Standardized template The Secretary shall establish a standardized template for pharmacies to use for the submission of allegations described in subclause (I). Such template shall require that the submission include a certification by the pharmacy that the information included is accurate, complete, and true to the best of the knowledge, information, and belief of such pharmacy. (V) Preventing frivolous allegations In the case where the Secretary determines that a pharmacy has submitted frivolous allegations under this clause on a routine basis, the Secretary may temporarily prohibit such pharmacy from using the allegation submission process under this clause, as determined appropriate by the Secretary. (VI) Exemption from freedom of information act Allegations submitted under this clause shall be exempt from disclosure under section 552 of title 5, United States Code. (VII) Rule of construction Nothing in this clause shall be construed as limiting the ability of a pharmacy to pursue other legal actions or remedies, consistent with applicable Federal or State law, with respect to a potential violation of a requirement described in this subparagraph. (VIII) Anti-retaliation and anti-coercion Consistent with applicable Federal or State law, a PDP sponsor shall not\u2014 (aa) retaliate against a pharmacy for submitting any allegations under this clause; or (bb) coerce, intimidate, threaten, or interfere with the ability of a pharmacy to submit any such allegations. (ii) Investigation The Secretary shall investigate, as determined appropriate by the Secretary, allegations submitted pursuant to clause (i). (iii) Enforcement (I) In general In the case where the Secretary determines that a PDP sponsor offering a prescription drug plan has violated the standards for reasonable and relevant contract terms and conditions under subparagraph (A)(ii), the Secretary may use authorities under sections 1857(g) and 1860D\u201312(b)(3)(E) to impose civil monetary penalties or other intermediate sanctions. (II) Application of civil monetary penalties The provisions of section 1128A (other than subsections (a) and (b)) shall apply to a civil monetary penalty under this clause in the same manner as such provisions apply to a penalty or proceeding under section 1128A(a). .\n**(2) Conforming amendment**\nSection 1857(g)(1) of the Social Security Act ( 42 U.S.C. 1395w\u201327(g)(1) ) is amended\u2014\n**(A)**\nin subparagraph (J), by striking or after the semicolon;\n**(B)**\nby redesignating subparagraph (K) as subparagraph (L);\n**(C)**\nby inserting after subparagraph (J), the following new subparagraph:\n(K) fails to comply with the standards for reasonable and relevant contract terms and conditions under subparagraph (A)(ii) of section 1860D\u20134(b)(1); or ;\n**(D)**\nin subparagraph (L), as redesignated by subparagraph (B), by striking through (J) and inserting through (K) ; and\n**(E)**\nin the flush matter following subparagraph (L), as so redesignated, by striking subparagraphs (A) through (K) and inserting subparagraphs (A) through (L) .\n##### (d) Accountability of pharmacy benefit managers for violations of reasonable and relevant contract terms and conditions\n**(1) In general**\nSection 1860D\u201312(b) of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ) is amended by adding at the end the following new paragraph:\n(9) Accountability of pharmacy benefit managers for violations of reasonable and relevant contract terms and conditions For plan years beginning on or after January 1, 2028, each contract entered into with a PDP sponsor under this part with respect to a prescription drug plan offered by such sponsor shall provide that any pharmacy benefit manager acting on behalf of such sponsor has a written agreement with the PDP sponsor under which the pharmacy benefit manager agrees to reimburse the PDP sponsor for any amounts paid by such sponsor under section 1860D\u20134(b)(1)(F)(iii)(I) to the Secretary as a result of a violation described in such section if such violation is related to a responsibility delegated to the pharmacy benefit manager by such PDP sponsor. .\n**(2) MA\u2013PD plans**\nSection 1857(f)(3) of the Social Security Act ( 42 U.S.C. 1395w\u201327(f)(3) ) is amended by adding at the end the following new subparagraph:\n(F) Accountability of pharmacy benefit managers for violations of reasonable and relevant contract terms For plan years beginning on or after January 1, 2028, section 1860D\u201312(b)(9). .\n##### (e) Biennial report on enforcement and oversight of pharmacy access requirements\nSection 1860D\u201342 of the Social Security Act ( 42 U.S.C. 1395w\u2013152 ), as amended by subsection (b), is amended by adding at the end the following new subsection:\n(f) Biennial report on enforcement and oversight of pharmacy access requirements (1) In general Not later than 2 years after the date of enactment of this subsection, and at least once every 2 years thereafter, the Secretary shall publish a report on enforcement and oversight actions and activities undertaken by the Secretary with respect to the requirements under section 1860D\u20134(b)(1). (2) Limitation A report under paragraph (1) shall not disclose\u2014 (A) identifiable information about individuals or entities unless such information is otherwise publicly available; or (B) trade secrets with respect to any entities. .\n#### 3. Requirements of pharmacy benefit managers under Medicare part D\n##### (a) Prescription drug plans\nSection 1860D\u201312 of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ) is amended by adding at the end the following new subsection:\n(h) Requirements relating to pharmacy benefit managers For plan years beginning on or after January 1, 2028: (1) Agreements with pharmacy benefit managers Each contract entered into with a PDP sponsor under this part with respect to a prescription drug plan offered by such sponsor shall provide that any pharmacy benefit manager acting on behalf of such sponsor has a written agreement with the PDP sponsor under which the pharmacy benefit manager, and any affiliates of such pharmacy benefit manager, as applicable, agree to meet the following requirements: (A) No income other than bona fide service fees (i) In general The pharmacy benefit manager and any affiliate of such pharmacy benefit manager shall not derive any remuneration with respect to any services provided on behalf of any entity or individual, in connection with the utilization of covered part D drugs, from any such entity or individual other than bona fide service fees, subject to clauses (ii) and (iii). (ii) Incentive payments For the purposes of this subsection, an incentive payment (as determined by the Secretary) paid by a PDP sponsor to a pharmacy benefit manager that is performing services on behalf of such sponsor shall be deemed a bona fide service fee (even if such payment does not otherwise meet the definition of such term under paragraph (7)(B)) if such payment is a flat dollar amount, is consistent with fair market value (as specified by the Secretary), is related to services actually performed by the pharmacy benefit manager or affiliate of such pharmacy benefit manager, on behalf of the PDP sponsor making such payment, in connection with the utilization of covered part D drugs, and meets additional requirements, if any, as determined appropriate by the Secretary. (iii) Clarification on rebates and discounts used to lower costs for covered part d drugs Rebates, discounts, and other price concessions received by a pharmacy benefit manager or an affiliate of a pharmacy benefit manager from manufacturers, even if such price concessions are calculated as a percentage of a drug\u2019s price, shall not be considered a violation of the requirements of clause (i) if they are fully passed through to a PDP sponsor and are compliant with all regulatory and subregulatory requirements related to direct and indirect remuneration for manufacturer rebates under this part, including in cases where a PDP sponsor is acting as a pharmacy benefit manager on behalf of a prescription drug plan offered by such PDP sponsor. (iv) Evaluation of remuneration arrangements Components of subsets of remuneration arrangements (such as fees or other forms of compensation paid to or retained by the pharmacy benefit manager or affiliate of such pharmacy benefit manager), as determined appropriate by the Secretary, between pharmacy benefit managers or affiliates of such pharmacy benefit managers, as applicable, and other entities involved in the dispensing or utilization of covered part D drugs (including PDP sponsors, manufacturers, pharmacies, and other entities as determined appropriate by the Secretary) shall be subject to review by the Secretary, in consultation with the Office of the Inspector General of the Department of Health and Human Services, as determined appropriate by the Secretary. The Secretary, in consultation with the Office of the Inspector General, shall review whether remuneration under such arrangements is consistent with fair market value (as specified by the Secretary) through reviews and assessments of such remuneration, as determined appropriate. (v) Disgorgement The pharmacy benefit manager shall disgorge any remuneration paid to such pharmacy benefit manager or an affiliate of such pharmacy benefit manager in violation of this subparagraph to the PDP sponsor. (vi) Additional requirements The pharmacy benefit manager shall\u2014 (I) enter into a written agreement with any affiliate of such pharmacy benefit manager, under which the affiliate shall identify and disgorge any remuneration described in clause (v) to the pharmacy benefit manager; and (II) attest, subject to any requirements determined appropriate by the Secretary, that the pharmacy benefit manager has entered into a written agreement described in subclause (I) with any relevant affiliate of the pharmacy benefit manager. (B) Transparency regarding guarantees and cost performance evaluations The pharmacy benefit manager shall\u2014 (i) define, interpret, and apply, in a fully transparent and consistent manner for purposes of calculating or otherwise evaluating pharmacy benefit manager performance against pricing guarantees or similar cost performance measurements related to rebates, discounts, price concessions, or net costs, terms such as\u2014 (I) generic drug , in a manner consistent with the definition of the term under section 423.4 of title 42, Code of Federal Regulations, or a successor regulation; (II) brand name drug , in a manner consistent with the definition of the term under section 423.4 of title 42, Code of Federal Regulations, or a successor regulation; (III) specialty drug ; (IV) rebate ; and (V) discount ; (ii) identify any drugs, claims, or price concessions excluded from any pricing guarantee or other cost performance measure in a clear and consistent manner; and (iii) where a pricing guarantee or other cost performance measure is based on a pricing benchmark other than the wholesale acquisition cost (as defined in section 1847A(c)(6)(B)) of a drug, calculate and provide a wholesale acquisition cost-based equivalent to the pricing guarantee or other cost performance measure. (C) Provision of information (i) In general Not later than July 1 of each year, beginning in 2028, the pharmacy benefit manager shall submit to the PDP sponsor, and to the Secretary, a report, in accordance with this subparagraph, and shall make such report available to such sponsor at no cost to such sponsor in a format specified by the Secretary under paragraph (5). Each such report shall include, with respect to such PDP sponsor and each plan offered by such sponsor, the following information with respect to the previous plan year: (I) A list of all drugs covered by the plan that were dispensed including, with respect to each such drug\u2014 (aa) the brand name, generic or non-proprietary name, and National Drug Code; (bb) the number of plan enrollees for whom the drug was dispensed, the total number of prescription claims for the drug (including original prescriptions and refills, counted as separate claims), and the total number of dosage units of the drug dispensed; (cc) the number of prescription claims described in item (bb) by each type of dispensing channel through which the drug was dispensed, including retail, mail order, specialty pharmacy, long term care pharmacy, home infusion pharmacy, or other types of pharmacies or providers; (dd) the average wholesale acquisition cost, listed as cost per day\u2019s supply, cost per dosage unit, and cost per typical course of treatment (as applicable); (ee) the average wholesale price for the drug, listed as price per day\u2019s supply, price per dosage unit, and price per typical course of treatment (as applicable); (ff) the total out-of-pocket spending by plan enrollees on such drug after application of any benefits under the plan, including plan enrollee spending through copayments, coinsurance, and deductibles; (gg) total rebates paid by the manufacturer on the drug as reported under the Detailed DIR Report (or any successor report) submitted by such sponsor to the Centers for Medicare & Medicaid Services; (hh) all other direct or indirect remuneration on the drug as reported under the Detailed DIR Report (or any successor report) submitted by such sponsor to the Centers for Medicare & Medicaid Services; (ii) the average pharmacy reimbursement amount paid by the plan for the drug in the aggregate and disaggregated by dispensing channel identified in item (cc); (jj) the average National Average Drug Acquisition Cost (NADAC); and (kk) total manufacturer-derived revenue, inclusive of bona fide service fees, attributable to the drug and retained by the pharmacy benefit manager and any affiliate of such pharmacy benefit manager. (II) In the case of a pharmacy benefit manager that has an affiliate that is a retail, mail order, or specialty pharmacy, with respect to drugs covered by such plan that were dispensed, the following information: (aa) The percentage of total prescriptions that were dispensed by pharmacies that are an affiliate of the pharmacy benefit manager for each drug. (bb) The interquartile range of the total combined costs paid by the plan and plan enrollees, per dosage unit, per course of treatment, per 30-day supply, and per 90-day supply for each drug dispensed by pharmacies that are not an affiliate of the pharmacy benefit manager and that are included in the pharmacy network of such plan. (cc) The interquartile range of the total combined costs paid by the plan and plan enrollees, per dosage unit, per course of treatment, per 30-day supply, and per 90-day supply for each drug dispensed by pharmacies that are an affiliate of the pharmacy benefit manager and that are included in the pharmacy network of such plan. (dd) The lowest total combined cost paid by the plan and plan enrollees, per dosage unit, per course of treatment, per 30-day supply, and per 90-day supply, for each drug that is available from any pharmacy included in the pharmacy network of such plan. (ee) The difference between the average acquisition cost of the affiliate, such as a pharmacy or other entity that acquires prescription drugs, that initially acquires the drug and the amount reported under subclause (I)(jj) for each drug. (ff) A list inclusive of the brand name, generic or non-proprietary name, and National Drug Code of covered part D drugs subject to an agreement with a covered entity under section 340B of the Public Health Service Act for which the pharmacy benefit manager or an affiliate of the pharmacy benefit manager had a contract or other arrangement with such a covered entity in the service area of such plan. (III) Where a drug approved under section 505(c) of the Federal Food, Drug, and Cosmetic Act (referred to in this subclause as the listed drug ) is covered by the plan, the following information: (aa) A list of currently marketed generic drugs approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act pursuant to an application that references such listed drug that are not covered by the plan, are covered on the same formulary tier or a formulary tier typically associated with higher cost-sharing than the listed drug, or are subject to utilization management that the listed drug is not subject to. (bb) The estimated average beneficiary cost-sharing under the plan for a 30-day supply of the listed drug. (cc) Where a generic drug listed under item (aa) is on a formulary tier typically associated with higher cost-sharing than the listed drug, the estimated average cost-sharing that a beneficiary would have paid for a 30-day supply of each of the generic drugs described in item (aa), had the plan provided coverage for such drugs on the same formulary tier as the listed drug. (dd) A written justification for providing more favorable coverage of the listed drug than the generic drugs described in item (aa). (ee) The number of currently marketed generic drugs approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act pursuant to an application that references such listed drug. (IV) Where a reference product (as defined in section 351(i) of the Public Health Service Act) is covered by the plan, the following information: (aa) A list of currently marketed biosimilar biological products licensed under section 351(k) of the Public Health Service Act pursuant to an application that refers to such reference product that are not covered by the plan, are covered on the same formulary tier or a formulary tier typically associated with higher cost-sharing than the reference product, or are subject to utilization management that the reference product is not subject to. (bb) The estimated average beneficiary cost-sharing under the plan for a 30-day supply of the reference product. (cc) Where a biosimilar biological product listed under item (aa) is on a formulary tier typically associated with higher cost-sharing than the reference product, the estimated average cost-sharing that a beneficiary would have paid for a 30-day supply of each of the biosimilar biological products described in item (aa), had the plan provided coverage for such products on the same formulary tier as the reference product. (dd) A written justification for providing more favorable coverage of the reference product than the biosimilar biological product described in item (aa). (ee) The number of currently marketed biosimilar biological products licensed under section 351(k) of the Public Health Service Act, pursuant to an application that refers to such reference product. (V) Total gross spending on covered part D drugs by the plan, not net of rebates, fees, discounts, or other direct or indirect remuneration. (VI) The total amount retained by the pharmacy benefit manager or an affiliate of such pharmacy benefit manager in revenue related to utilization of covered part D drugs under that plan, inclusive of bona fide service fees. (VII) The total spending on covered part D drugs net of rebates, fees, discounts, or other direct and indirect remuneration by the plan. (VIII) An explanation of any benefit design parameters under such plan that encourage plan enrollees to fill prescriptions at pharmacies that are an affiliate of such pharmacy benefit manager, such as mail and specialty home delivery programs, and retail and mail auto-refill programs. (IX) The following information: (aa) A list of all brokers, consultants, advisors, and auditors that receive compensation from the pharmacy benefit manager or an affiliate of such pharmacy benefit manager for referrals, consulting, auditing, or other services offered to PDP sponsors related to pharmacy benefit management services. (bb) The amount of compensation provided by such pharmacy benefit manager or affiliate to each such broker, consultant, advisor, and auditor. (cc) The methodology for calculating the amount of compensation provided by such pharmacy benefit manager or affiliate, for each such broker, consultant, advisor, and auditor. (X) A list of all affiliates of the pharmacy benefit manager. (XI) A summary document submitted in a standardized template developed by the Secretary that includes such information described in subclauses (I) through (X). (ii) Written explanation of contracts or agreements with drug manufacturers (I) In general The pharmacy benefit manager shall, not later than 30 days after the finalization of any contract or agreement between such pharmacy benefit manager or an affiliate of such pharmacy benefit manager and a drug manufacturer (or subsidiary, agent, or entity affiliated with such drug manufacturer) that makes rebates, discounts, payments, or other financial incentives related to one or more covered part D drugs or other prescription drugs, as applicable, of the manufacturer directly or indirectly contingent upon coverage, formulary placement, or utilization management conditions on any other covered part D drugs or other prescription drugs, as applicable, submit to the PDP sponsor a written explanation of such contract or agreement. (II) Requirements A written explanation under subclause (I) shall\u2014 (aa) include the manufacturer subject to the contract or agreement, all covered part D drugs and other prescription drugs, as applicable, subject to the contract or agreement and the manufacturers of such drugs, and a high-level description of the terms of such contract or agreement and how such terms apply to such drugs; and (bb) be certified by the Chief Executive Officer, Chief Financial Officer, or General Counsel of such pharmacy benefit manager, or affiliate of such pharmacy benefit manager, as applicable, or an individual delegated with the authority to sign on behalf of one of these officers, who reports directly to the officer. (III) Definition of other prescription drugs For purposes of this clause, the term other prescription drugs means prescription drugs covered as supplemental benefits under this part or prescription drugs paid outside of this part. (D) Audit rights (i) In general Not less than once a year, at the request of the PDP sponsor, the pharmacy benefit manager shall allow for an audit of the pharmacy benefit manager to ensure compliance with all terms and conditions under the written agreement described in this paragraph and the accuracy of information reported under subparagraph (C). (ii) Auditor The PDP sponsor shall have the right to select an auditor. The pharmacy benefit manager shall not impose any limitations on the selection of such auditor. (iii) Provision of information The pharmacy benefit manager shall make available to such auditor all records, data, contracts, and other information necessary to confirm the accuracy of information provided under subparagraph (C), subject to reasonable restrictions on how such information must be reported to prevent redisclosure of such information. (iv) Timing The pharmacy benefit manager must provide information under clause (iii) and other information, data, and records relevant to the audit to such auditor within 6 months of the initiation of the audit and respond to requests for additional information from such auditor within 30 days after the request for additional information. (v) Information from affiliates The pharmacy benefit manager shall be responsible for providing to such auditor information required to be reported under subparagraph (C) or under clause (iii) of this subparagraph that is owned or held by an affiliate of such pharmacy benefit manager. (2) Enforcement (A) In general Each PDP sponsor shall\u2014 (i) disgorge to the Secretary any amounts disgorged to the PDP sponsor by a pharmacy benefit manager under paragraph (1)(A)(v); (ii) require, in a written agreement with any pharmacy benefit manager acting on behalf of such sponsor or affiliate of such pharmacy benefit manager, that such pharmacy benefit manager or affiliate reimburse the PDP sponsor for any civil money penalty imposed on the PDP sponsor as a result of the failure of the pharmacy benefit manager or affiliate to meet the requirements of paragraph (1) that are applicable to the pharmacy benefit manager or affiliate under the agreement; and (iii) require, in a written agreement with any such pharmacy benefit manager acting on behalf of such sponsor or affiliate of such pharmacy benefit manager, that such pharmacy benefit manager or affiliate be subject to punitive remedies for breach of contract for failure to comply with the requirements applicable under paragraph (1). (B) Reporting of alleged violations The Secretary shall make available and maintain a mechanism for manufacturers, PDP sponsors, pharmacies, and other entities that have contractual relationships with pharmacy benefit managers or affiliates of such pharmacy benefit managers to report, on a confidential basis, alleged violations of paragraph (1)(A) or subparagraph (C). (C) Anti-retaliation and anti-coercion Consistent with applicable Federal or State law, a PDP sponsor shall not\u2014 (i) retaliate against an individual or entity for reporting an alleged violation under subparagraph (B); or (ii) coerce, intimidate, threaten, or interfere with the ability of an individual or entity to report any such alleged violations. (3) Certification of compliance (A) In general Each PDP sponsor shall furnish to the Secretary (at a time and in a manner specified by the Secretary) an annual certification of compliance with this subsection, as well as such information as the Secretary determines necessary to carry out this subsection. (B) Implementation Notwithstanding any other provision of law, the Secretary may implement this paragraph by program instruction or otherwise. (4) Rule of construction Nothing in this subsection shall be construed as\u2014 (A) prohibiting flat dispensing fees or reimbursement or payment for ingredient costs (including customary, industry-standard discounts directly related to drug acquisition that are retained by pharmacies or wholesalers) to entities that acquire or dispense prescription drugs; or (B) modifying regulatory requirements or sub-regulatory program instruction or guidance related to pharmacy payment, reimbursement, or dispensing fees. (5) Standard formats (A) In general Not later than June 1, 2027, the Secretary shall specify standard, machine-readable formats for pharmacy benefit managers to submit annual reports required under paragraph (1)(C)(i). (B) Implementation Notwithstanding any other provision of law, the Secretary may implement this paragraph by program instruction or otherwise. (6) Confidentiality (A) In general Information disclosed by a pharmacy benefit manager, an affiliate of a pharmacy benefit manager, a PDP sponsor, or a pharmacy under this subsection that is not otherwise publicly available or available for purchase shall not be disclosed by the Secretary or a PDP sponsor receiving the information, except that the Secretary may disclose the information for the following purposes: (i) As the Secretary determines necessary to carry out this part. (ii) To permit the Comptroller General to review the information provided. (iii) To permit the Director of the Congressional Budget Office to review the information provided. (iv) To permit the Executive Director of the Medicare Payment Advisory Commission to review the information provided. (v) To the Attorney General for the purposes of conducting oversight and enforcement under this title. (vi) To the Inspector General of the Department of Health and Human Services in accordance with its authorities under the Inspector General Act of 1978 (section 406 of title 5, United States Code), and other applicable statutes. (B) Restriction on use of information The Secretary, the Comptroller General, the Director of the Congressional Budget Office, and the Executive Director of the Medicare Payment Advisory Commission shall not report on or disclose information disclosed pursuant to subparagraph (A) to the public in a manner that would identify\u2014 (i) a specific pharmacy benefit manager, affiliate, pharmacy, manufacturer, wholesaler, PDP sponsor, or plan; or (ii) contract prices, rebates, discounts, or other remuneration for specific drugs in a manner that may allow the identification of specific contracting parties or of such specific drugs. (7) Definitions For purposes of this subsection: (A) Affiliate The term affiliate means, with respect to any pharmacy benefit manager or PDP sponsor, any entity that, directly or indirectly\u2014 (i) owns or is owned by, controls or is controlled by, or is otherwise related in any ownership structure to such pharmacy benefit manager or PDP sponsor; or (ii) acts as a contractor, principal, or agent to such pharmacy benefit manager or PDP sponsor, insofar as such contractor, principal, or agent performs any of the functions described under subparagraph (C). (B) Bona fide service fee The term bona fide service fee means a fee that is reflective of the fair market value (as specified by the Secretary, through notice and comment rulemaking) for a bona fide, itemized service actually performed on behalf of an entity, that the entity would otherwise perform (or contract for) in the absence of the service arrangement and that is not passed on in whole or in part to a client or customer, whether or not the entity takes title to the drug. Such fee must be a flat dollar amount and shall not be directly or indirectly based on, or contingent upon\u2014 (i) drug price, such as wholesale acquisition cost or drug benchmark price (such as average wholesale price); (ii) the amount of discounts, rebates, fees, or other direct or indirect remuneration with respect to covered part D drugs dispensed to enrollees in a prescription drug plan, except as permitted pursuant to paragraph (1)(A)(ii); (iii) coverage or formulary placement decisions or the volume or value of any referrals or business generated between the parties to the arrangement; or (iv) any other amounts or methodologies prohibited by the Secretary. (C) Pharmacy benefit manager The term pharmacy benefit manager means any person or entity that, either directly or through an intermediary, acts as a price negotiator or group purchaser on behalf of a PDP sponsor or prescription drug plan, or manages the prescription drug benefits provided by such sponsor or plan, including the processing and payment of claims for prescription drugs, the performance of drug utilization review, the processing of drug prior authorization requests, the adjudication of appeals or grievances related to the prescription drug benefit, contracting with network pharmacies, controlling the cost of covered part D drugs, or the provision of related services. Such term includes any person or entity that carries out one or more of the activities described in the preceding sentence, irrespective of whether such person or entity calls itself a pharmacy benefit manager . .\n##### (b) MA\u2013PD plans\nSection 1857(f)(3) of the Social Security Act ( 42 U.S.C. 1395w\u201327(f)(3) ), as amended by section 2(d)(2), is amended by adding at the end the following new subparagraph:\n(G) Requirements relating to pharmacy benefit managers For plan years beginning on or after January 1, 2028, section 1860D\u201312(h). .\n##### (c) Nonapplication of Paperwork Reduction Act\nChapter 35 of title 44, United States Code, shall not apply to the implementation of this subsection.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
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
        "updateDate": "2025-03-25T15:49:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119s882",
          "measure-number": "882",
          "measure-type": "s",
          "orig-publish-date": "2025-03-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s882v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Patients Before Middlemen Act</strong></p><p>This bill establishes certain standards and reporting requirements for prescription drug plan (PDP) sponsors, pharmacy benefit managers (PBMs), and pharmacies under the Medicare prescription drug benefit and Medicare Advantage.</p><p>Specifically, the Centers for Medicare & Medicaid Services (CMS) must develop reasonable and relevant standards for contracts between PDP sponsors and pharmacies. The CMS must seek input from interested stakeholders when developing these standards. PDP sponsors are subject to civil penalties for violating these standards; PBMs must reimburse PDP sponsors for civil penalties that result from their responsibilities.</p><p>The bill also requires the CMS to report periodically on essential retail pharmacies (i.e., pharmacies that serve as the only pharmacy within a certain radius) with respect to costs, contracts, and other specified information, particularly in relation to other types of pharmacies.</p><p>Additionally, PBMs may not receive any income other than flat, bona fide service fees. PBMs must turn over any excess amounts they receive to PDP sponsors; PDP sponsors must turn over these amounts to the CMS. In addition, PBMs must report to PDP sponsors and to the CMS an itemized list of prescription drugs that were dispensed during the previous year and related data about costs, claims, affiliated pharmacies, and other specified information. PDP sponsors may audit PBMs to ensure compliance with these requirements and must annually certify their compliance; PBMs are responsible for any associated civil penalties for violations.</p><p>The bill's changes generally apply beginning in 2028.</p>"
        },
        "title": "Patients Before Middlemen Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s882.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Patients Before Middlemen Act</strong></p><p>This bill establishes certain standards and reporting requirements for prescription drug plan (PDP) sponsors, pharmacy benefit managers (PBMs), and pharmacies under the Medicare prescription drug benefit and Medicare Advantage.</p><p>Specifically, the Centers for Medicare & Medicaid Services (CMS) must develop reasonable and relevant standards for contracts between PDP sponsors and pharmacies. The CMS must seek input from interested stakeholders when developing these standards. PDP sponsors are subject to civil penalties for violating these standards; PBMs must reimburse PDP sponsors for civil penalties that result from their responsibilities.</p><p>The bill also requires the CMS to report periodically on essential retail pharmacies (i.e., pharmacies that serve as the only pharmacy within a certain radius) with respect to costs, contracts, and other specified information, particularly in relation to other types of pharmacies.</p><p>Additionally, PBMs may not receive any income other than flat, bona fide service fees. PBMs must turn over any excess amounts they receive to PDP sponsors; PDP sponsors must turn over these amounts to the CMS. In addition, PBMs must report to PDP sponsors and to the CMS an itemized list of prescription drugs that were dispensed during the previous year and related data about costs, claims, affiliated pharmacies, and other specified information. PDP sponsors may audit PBMs to ensure compliance with these requirements and must annually certify their compliance; PBMs are responsible for any associated civil penalties for violations.</p><p>The bill's changes generally apply beginning in 2028.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s882"
    },
    "title": "Patients Before Middlemen Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Patients Before Middlemen Act</strong></p><p>This bill establishes certain standards and reporting requirements for prescription drug plan (PDP) sponsors, pharmacy benefit managers (PBMs), and pharmacies under the Medicare prescription drug benefit and Medicare Advantage.</p><p>Specifically, the Centers for Medicare & Medicaid Services (CMS) must develop reasonable and relevant standards for contracts between PDP sponsors and pharmacies. The CMS must seek input from interested stakeholders when developing these standards. PDP sponsors are subject to civil penalties for violating these standards; PBMs must reimburse PDP sponsors for civil penalties that result from their responsibilities.</p><p>The bill also requires the CMS to report periodically on essential retail pharmacies (i.e., pharmacies that serve as the only pharmacy within a certain radius) with respect to costs, contracts, and other specified information, particularly in relation to other types of pharmacies.</p><p>Additionally, PBMs may not receive any income other than flat, bona fide service fees. PBMs must turn over any excess amounts they receive to PDP sponsors; PDP sponsors must turn over these amounts to the CMS. In addition, PBMs must report to PDP sponsors and to the CMS an itemized list of prescription drugs that were dispensed during the previous year and related data about costs, claims, affiliated pharmacies, and other specified information. PDP sponsors may audit PBMs to ensure compliance with these requirements and must annually certify their compliance; PBMs are responsible for any associated civil penalties for violations.</p><p>The bill's changes generally apply beginning in 2028.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s882"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s882is.xml"
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
      "title": "Patients Before Middlemen Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Patients Before Middlemen Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to assure pharmacy access and choice for beneficiaries under prescription drug plans and MA-PD plans and to establish requirements of pharmacy benefit managers under Medicare part D.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T05:33:26Z"
    }
  ]
}
```
