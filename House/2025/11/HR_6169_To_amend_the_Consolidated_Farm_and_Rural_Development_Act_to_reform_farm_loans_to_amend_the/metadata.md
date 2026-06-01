# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6169?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6169
- Title: Fair Credit for Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 6169
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-16T08:07:51Z
- Update date including text: 2026-05-16T08:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6169",
    "number": "6169",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000370",
        "district": "12",
        "firstName": "Alma",
        "fullName": "Rep. Adams, Alma S. [D-NC-12]",
        "lastName": "Adams",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Fair Credit for Farmers Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:51Z",
    "updateDateIncludingText": "2026-05-16T08:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-05T19:49:13Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6169ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6169\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Adams (for herself and Ms. McClellan ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to reform farm loans, to amend the Department of Agriculture Reorganization Act of 1994 to reform the National Appeals Division process, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Credit for Farmers Act .\n#### 2. Deferment of payments for borrowers of farm loans\n##### (a) Definitions\nIn this section:\n**(1) Covered producer**\nThe term covered producer means\u2014\n**(A)**\na limited resource farmer or rancher (as defined in section 718.2 of title 7, Code of Federal Regulations (as in effect on the date of enactment of this Act));\n**(B)**\na socially disadvantaged farmer or rancher (as defined in section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ));\n**(C)**\na beginning farmer or rancher (as defined in that section); and\n**(D)**\na veteran farmer or rancher (as defined in that section).\n**(2) Eligible borrower**\nThe term eligible borrower means a borrower that is a farmer or rancher that is\u2014\n**(A)**\ndelinquent, as described in the definition of the term delinquent borrower in section 761.2(b) of title 7, Code of Federal Regulations (as in effect on the date of enactment of this Act); or\n**(B)**\nfinancially distressed, as described in the definition of the term financially distressed borrower in section 761.2(b) of title 7, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(3) Farm loan**\nThe term farm loan means a direct or guaranteed\u2014\n**(A)**\nfarm ownership loan under subtitle A of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1922 et seq. );\n**(B)**\noperating loan under subtitle B of that Act ( 7 U.S.C. 1941 et seq. ); or\n**(C)**\nemergency loan under subtitle C of that Act ( 7 U.S.C. 1961 et seq. ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Deferment of payments on direct farm loans\n**(1) In general**\nThe Secretary shall\u2014\n**(A)**\ndefer payments of principal and interest due on direct farm loans by eligible borrowers during the 2-year period beginning on the date of enactment of this Act; and\n**(B)**\nextend by 2 years the maturity date and repayment period of each direct farm loan the payments on which are deferred under subparagraph (A).\n**(2) Exclusion**\nParagraph (1) does not apply to a direct farm loan the term of which is 12 months or less.\n**(3) Authority to exceed loan maturity dates**\nIn extending a date under paragraph (1)(B), the Secretary may exceed by not more than 2 years\u2014\n**(A)**\nthe maximum period of repayment described in section 307 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1927 ) for a farm ownership loan under subtitle A of that Act ( 7 U.S.C. 1922 et seq. );\n**(B)**\nthe maximum period of repayment described in section 316(b) of that Act ( 7 U.S.C. 1946(b) ) for an operating loan under subtitle B of that Act ( 7 U.S.C. 1941 et seq. ); and\n**(C)**\nthe maximum period of repayment described in section 324(d) of that Act ( 7 U.S.C. 1964(d) ) for an emergency loan under subtitle C of that Act ( 7 U.S.C. 1961 et seq. ).\n##### (c) Interest rate during deferral\nThe Secretary shall modify each direct farm loan of an eligible borrower that is outstanding as of the date of enactment of this Act such that the interest rate on all remaining principal of the farm loan is 0.125 percent during the 2-year period beginning on that date of enactment.\n##### (d) Waiver of guaranteed farm loan fees for covered producers\n**(1) In general**\nThe Secretary shall require lenders of guaranteed farm loans to covered producers to waive guarantee fees (as described in section 762.130(d)(4) of title 7, Code of Federal Regulations (as in effect on the date of enactment of this Act)) on those loans during the period\u2014\n**(A)**\nbeginning on the date of enactment of this Act; and\n**(B)**\nending not earlier than 2 years after that date of enactment.\n**(2) Extension**\nThe Secretary may extend a deadline under paragraph (1)(B) by an additional 180 days if the Secretary determines the extension to be necessary.\n#### 3. Farm loan reform\n##### (a) General reforms\n**(1) In general**\nSubtitle D of the Consolidated Farm and Rural Development Act is amended by inserting after section 374 ( 7 U.S.C. 2008i ) the following:\n375. Farmer program loan reform (a) Definitions In this section: (1) Adverse decision The term adverse decision has the meaning given the term in section 271 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6991 ). (2) Principal residence The term principal residence means the principal residence (as determined by the Secretary) of a borrower of a farmer program loan, including a residence and not more than 10 acres of adjoining land possessed and occupied by the borrower. (b) Determination letters and adverse decisions (1) In general In the case of any adverse decision relating to a farmer program loan, a Farm Service Agency program benefit, or the noninsured crop disaster assistance program established by section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ), the Secretary shall include in a determination letter provided to the applicant, to the maximum extent practicable\u2014 (A) a description of each reason known, or that reasonably should have been known, to the Secretary for that adverse decision; (B) a reference to each regulation and each relevant instruction in the Farm Loan Programs handbook, the Noninsured Crop Disaster Assistance Program handbook, or any other appropriate handbook published by the Farm Service Agency; and (C) instructions for accessing the Electronic Code of Federal Regulations and the handbooks described in subparagraph (B) online. (2) Effect of failure to state reasons If the Secretary issues any adverse decision relating to an application for a farmer program loan, a Farm Service Agency program benefit, or the noninsured crop disaster assistance program established by section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ) and does not include in a determination letter provided to the applicant a reason known or which should have reasonably been known to the Secretary for that adverse decision, the Secretary may not subsequently issue an adverse decision to that applicant on the basis of the same reason, known or which should have reasonably been known to the Secretary, unless the circumstances of the applicant have substantially changed since the issuance of the prior adverse decision. (c) Collateralization (1) Origination The Secretary may secure a direct farmer program loan with a principal residence only if the total value of other assets available to secure the farmer program loan does not provide adequate security (as defined in section 761.2(b) of title 7, Code of Federal Regulations (as in effect on the date of enactment of the Fair Credit for Farmers Act )) for the loan. (2) Partial release of principal residence security In the case of a farmer program loan secured in part by a principal residence, the Secretary shall initiate a partial release of the principal residence as security in accordance with subpart H of part 765 of title 7, Code of Federal Regulations (as in effect on the date of enactment of the Fair Credit for Farmers Act ), without any action required by the borrower, when the total value of other assets securing the farmer program loan is equal to 100 percent of the remaining loan amount. (3) Loan servicing (A) In general In the case of a farmer program loan borrower who is delinquent prior to restructuring the farmer program loan, the borrower shall execute and provide to the Secretary a lien on assets necessary to achieve not more than 100 percent collateralization of the loan value. (B) Best lien Except as provided in section 764.106 of title 7, Code of Federal Regulations (as in effect on the date of enactment of the Fair Credit for Farmers Act ), the Secretary shall take the best lien obtainable on assets described in subparagraph (A), subject to the condition that a primary residence shall be the last option available to the Secretary to achieve 100 percent collateralization of the loan value. (4) Prohibition on additional security The Secretary may not secure a direct farmer program loan with any property that provides security in excess of the amount of security value equal to the loan amount. (d) Eligibility requirements The Secretary shall not impose any limitation relating to the number of years in which a farmer program loan may be closed by a borrower. .\n**(2) Conforming amendment**\nSection 196(b) of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333(b) ) is amended by adding at the end the following:\n(5) Adverse decisions In the case of an adverse decision relating to an application under this subsection, section 375(b) of the Consolidated Farm and Rural Development Act shall apply. .\n##### (b) Farm loan eligibility\n**(1) Persons eligible for direct farm ownership loans**\nSection 302(b) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1922(b) ) is amended\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) In general The Secretary may make a direct loan under this subtitle only to a farmer or rancher who has at least 1 year of experience substantially participating in the management and business operations of a farm or ranch, as determined by the Secretary. ; and\n**(B)**\nby striking paragraphs (3) and (4) and inserting the following:\n(3) Waiver authority In the case of a qualified beginning farmer or rancher, the Secretary may waive the 1-year requirement described in paragraph (1) if the qualified beginning farmer or rancher\u2014 (A) has an established relationship with an individual who has experience in farming or ranching, or with a local farm or ranch operator or organization, approved by the Secretary, that is committed to mentoring the qualified beginning farmer or rancher; or (B) has other acceptable education or experience for an appropriate period of time, as determined by the Secretary. .\n**(2) Persons eligible for direct farm operating loans**\nSection 311 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1941 ) is amended by striking subsection (c).\n##### (c) Refinancing of debt with farm loans\n**(1) Allowed purposes of farm ownership loans**\nSection 303(a)(1) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1923(a)(1) ) is amended by striking subparagraph (E) and inserting the following:\n(E) refinancing the indebtedness of the farmer or rancher, if the farmer or rancher\u2014 (i) has used a direct loan under this subtitle to refinance indebtedness not more than 4 times previously; and (ii) is refinancing a debt obtained from a creditor other than the Secretary, including a guaranteed loan. .\n**(2) Allowed purposes of direct operating loans**\nSection 312(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1942(a) ) is amended by striking paragraph (9) and inserting the following:\n(9) refinancing the indebtedness of a borrower; or .\n##### (d) Effect of preferred lender certification\nSection 339(d)(4)(B) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1989(d)(4)(B) ) is amended\u2014\n**(1)**\nby striking institutions to and inserting the following:\ninstitutions\u2014 (i) to ; and\n**(2)**\nin clause (i) (as so designated)\u2014\n**(A)**\nby striking subsection relating and inserting subsection, relating ;\n**(B)**\nby striking worthiness, the and inserting worthiness or the ; and\n**(C)**\nby striking collection and liquidation of loans, and to and inserting the following:\nor collection of loans; and (ii) to .\n##### (e) Loan fund set-asides for beginning farmers and ranchers\nSection 346(b)(2) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1994(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i)(II), by inserting , to the extent practicable after April 1 of the fiscal year ; and\n**(B)**\nin clause (iii), by inserting , to the extent practicable after September 1 of the fiscal year ; and\n**(2)**\nin subparagraph (B)(iii), by inserting , to the extent practicable after April 1 of the fiscal year .\n##### (f) Removal of eligibility restriction based on previous debt write-down or other loss\nSection 373 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008h ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A)\u2014\n**(A)**\nby striking clause (i);\n**(B)**\nin clause (ii), by striking chapters 11, 12, or 13 of Title 11 of the and inserting chapter 11, 12, or 13 of title 11, ; and\n**(C)**\nby redesignating clauses (ii) and (iii) as clauses (i) and (ii), respectively; and\n**(2)**\nby striking subsection (c) and inserting the following:\n(c) Prohibition on eligibility restriction based on debt write-down or other loss The Secretary shall not restrict the eligibility of a borrower for a farm ownership or operating loan under subtitle A or B based on a previous debt write-down or other loss to the Secretary. .\n##### (g) Equitable relief\n**(1) In general**\nSection 366 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008a ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking (1) received and inserting (1)(A) received ;\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nby striking the period at the end and inserting ; or ; and\n**(II)**\nby striking (2) the Secretary and inserting (B) the Secretary ; and\n**(iii)**\nby adding at the end the following:\n(2) (A) received a benefit under any other program administered by an agency (as defined in section 271 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6991 )); and (B) the Secretary determines is not in compliance with the requirements of the provisions of law that authorize that program. ;\n**(B)**\nin subsection (b)(2), by inserting , including having made management or financial decisions for the farming or ranching operation of the farmer or rancher that were detrimental due to the erroneous nature of an official communication from the Department of Agriculture, regardless of whether a financial benefit was received or only promised before the period at the end;\n**(C)**\nin subsection (c)(1), by striking (a)(2) and inserting (a)(1)(B) ;\n**(D)**\nin subsection (e), by striking section in the matter preceding paragraph (1) and all that follows through shall not be in paragraph (2) and inserting section shall be ; and\n**(E)**\nby adding at the end the following:\n(f) Authority of National Appeals Division hearing officers (1) In general A hearing officer (as defined in section 271 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6991 )) may provide equitable relief under this section. (2) Review The Secretary may review a decision of a hearing officer (as so defined) to grant equitable relief pursuant to paragraph (1). (g) Cases in which an applicant is eligible (1) Definitions In this subsection: (A) Adverse decision The term adverse decision has the meaning given the term in section 271 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6991 ). (B) Applicant The term applicant means a person who submitted to, or attempted to submit to, the Farm Service Agency an application for\u2014 (i) a direct farm ownership, operating, or emergency loan under this title; or (ii) a Farm Service Agency program benefit. (2) Denial based on feasibility (A) In general A loan applicant shall be eligible for equitable relief under this section if\u2014 (i) the National Appeals Division determines that the Farm Service Agency was in error in denying the loan, benefit, or payment based on feasibility; (ii) the National Appeals Division has confirmed the accuracy of the projected income and projected expenses described in the original application submitted by the applicant; and (iii) the original application submitted by the applicant is no longer feasible due to the delay caused by the erroneous denial by the Farm Service Agency and the length of the appeals process. (B) Amount The amount of equitable relief under subparagraph (A) shall be the amount equal to the difference between\u2014 (i) the projected income described in the application; and (ii) the projected expenses described in the application. (3) Denial based on eligibility A loan applicant shall be eligible for equitable relief under this section if\u2014 (A) feasibility was not listed as a reason for an adverse decision in the determination letter provided to the applicant; (B) eligibility was listed as a reason for an adverse decision in the determination letter provided to the applicant; (C) the National Appeals Division determines that the Farm Service Agency was in error in denying the loan based on eligibility; and (D) the original application submitted by the applicant is no longer feasible due to the delay caused by the erroneous denial by the Farm Service Agency and the length of the appeals process. (4) Subsequently withdrawn adverse decision An applicant shall be eligible for equitable relief under this section if\u2014 (A) the Farm Service Agency issued an adverse decision on an application that the Farm Service Agency subsequently withdrew; and (B) the original application submitted by the applicant is no longer feasible due to the delay caused by the adverse decision. (5) Promised program benefits not received An applicant shall be eligible for equitable relief under this section if\u2014 (A) the Farm Service Agency indicated in an official communication made after the date of enactment of this subsection that the applicant could expect the loan, benefit, or payment, and then reversed its decision; and (B) the applicant acted in good faith. .\n**(2) Application**\nSubsection (g) of section 366 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008a )\u2014\n**(A)**\napplies only with respect to applications submitted or attempted to be submitted, and decisions or communications made, after the date of enactment of this Act; and\n**(B)**\ndoes not apply retroactively with respect to\u2014\n**(i)**\nany application submitted or attempted to be submitted, or decision or communication made, before that date of enactment; or\n**(ii)**\nany action, inaction, or consequence resulting from a decision or communication made before that date of enactment.\n#### 4. National appeals division reform\n##### (a) Burden of proof\nSection 277(c)(4) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6997(c)(4) ) is amended\u2014\n**(1)**\nby striking The appellant and inserting the following:\n(A) In general Except as provided in subparagraph (B), the appellant ; and\n**(2)**\nby adding at the end the following:\n(B) Appellants below income threshold (i) In general In the case of an appellant described in clause (ii), the agency shall bear the burden of proving by substantial evidence that the adverse decision of the agency was not erroneous. (ii) Appellants described An appellant referred to in clause (i) is an appellant\u2014 (I) the adjusted gross income of which for the previous year is not more than $300,000; or (II) the average annual adjusted gross income of which for the previous 5-year period is not more than $300,000. .\n##### (b) Implementation\nSection 280 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 7000 ) is amended\u2014\n**(1)**\nby redesignating subsection (b) as subsection (c); and\n**(2)**\nby inserting after subsection (a) the following:\n(b) Requirement In implementing a final determination in accordance with subsection (a), the head of an agency shall use the information used by the Division to make the final determination, without requiring additional information on which implementation would be conditioned, except as otherwise provided in the decision letter relating to the final determination. .",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-11-06",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3126",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fair Credit for Farmers Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T19:28:14Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6169ih.xml"
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
      "title": "Fair Credit for Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "title": "Fair Credit for Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to reform farm loans, to amend the Department of Agriculture Reorganization Act of 1994 to reform the National Appeals Division process, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T13:18:22Z"
    }
  ]
}
```
