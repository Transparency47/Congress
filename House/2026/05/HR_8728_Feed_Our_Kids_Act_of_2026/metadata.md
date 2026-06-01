# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8728?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8728
- Title: Feed Our Kids Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8728
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-30T08:05:48Z
- Update date including text: 2026-05-30T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8728",
    "number": "8728",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Feed Our Kids Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:48Z",
    "updateDateIncludingText": "2026-05-30T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
          "date": "2026-05-11T14:31:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CO"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8728ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8728\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Gottheimer (for himself, Mr. Soto , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Nutrition Act of 1966 and the Richard B. Russell National School Lunch Act to make breakfasts and lunches free for all children, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Feed Our Kids Act of 2026 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Effective date.\nTITLE I\u2014School Breakfast Program\nSec. 101. Free school breakfast program.\nTITLE II\u2014School Lunch Program\nSec. 201. Apportionment to States.\nSec. 202. Nutritional and other program requirements.\nSec. 203. Special assistance program.\nSec. 204. Price for a paid lunch.\nSec. 205. Summer food service program for children.\nSec. 206. Child and adult care food program.\nSec. 207. Meals and supplements for children in afterschool care.\nSec. 208. Pilot projects.\nSec. 209. Fresh fruit and vegetable program.\nSec. 210. Training, technical assistance, and Food Service Management Institute.\nSec. 211. Reimbursement of school meal delinquent debt program.\nSec. 212. Conforming amendments.\nTITLE III\u2014Report\nSec. 301. Report on free school meal programs.\n#### 2. Effective date\nUnless otherwise provided, this Act, and the amendments made by this Act, shall take effect 1 year after the date of enactment of this Act.\nI\nSchool Breakfast Program\n#### 101. Free school breakfast program\n##### (a) In general\nSection 4(a) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773(a) ) is amended, in the first sentence\u2014\n**(1)**\nby striking is hereby and inserting are ; and\n**(2)**\nby inserting to provide free breakfast to all children enrolled at those schools before in accordance .\n##### (b) Apportionment to States\nSection 4(b) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773(b) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)(i), by striking subclause (II) and inserting the following:\n(II) the national average payment for free breakfasts, as specified in subparagraph (B). ;\n**(B)**\nby striking subparagraph (B) and inserting the following:\n(B) Payment amounts (i) In general The national average payment for each free breakfast shall be $2.80, adjusted annually for inflation in accordance with clause (ii) and rounded in accordance with clause (iii). (ii) Inflation adjustment (I) In general The annual inflation adjustment under clause (i) shall reflect changes in the cost of operating the free breakfast program under this section, as indicated by the change in the Consumer Price Index for food away from home for all urban consumers. (II) Basis Each inflation annual adjustment under clause (i) shall reflect the changes in the Consumer Price Index for food away from home for the most recent 12-month period for which that data is available. (iii) Rounding On July 1, 2026, and annually thereafter, the national average payment rate for free breakfast shall be\u2014 (I) adjusted to the nearest lower-cent increment; and (II) based on the unrounded amounts for the preceding 12-month period. ;\n**(C)**\nby striking subparagraphs (C) and (E); and\n**(D)**\nby redesignating subparagraph (D) as subparagraph (C);\n**(2)**\nby striking paragraphs (2) and (3);\n**(3)**\nby redesignating paragraphs (4) and (5) as paragraphs (2) and (3), respectively; and\n**(4)**\nin paragraph (3) (as so redesignated), by striking paragraph (3) or (4) and inserting paragraph (2) .\n##### (c) State disbursement to schools\nSection 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ) is amended by striking subsection (c) and inserting the following:\n(c) State disbursement to schools Funds apportioned and paid to any State for the purpose of this section shall be disbursed by the State educational agency to schools selected by the State educational agency to assist those schools in operating a breakfast program. .\n##### (d) No collection of debt\n**(1) In general**\nNotwithstanding any other provision of the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) or any other provision of law, effective beginning on the date of enactment of this Act, as a condition of participation in the breakfast program under section 4 of that Act ( 42 U.S.C. 1773 ), a school\u2014\n**(A)**\nshall not collect any debt owed to the school for unpaid meal charges; and\n**(B)**\nshall continue to accrue debt for unpaid meal charges\u2014\n**(i)**\nfor the purpose of receiving reimbursement under section 211; and\n**(ii)**\nuntil the effective date specified in section 2.\n**(2) Child Nutrition Act of 1966**\n**(A) In general**\nSection 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ) is amended by striking subsection (d) and inserting the following:\n(d) No collection of debt A school participating in the free breakfast program under this section shall not collect any debt owed to the school for unpaid meal charges. .\n**(B) Conforming amendment**\nSection 23(a) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1793(a) ) is amended by striking school in severe need, as described in section 4(d)(1) and inserting the following:\nschool\u2014 (1) that has a free breakfast program under section 4 or seeks to initiate a free breakfast program under that section; and (2) of which not less than 40 percent of the students are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) .\n##### (e) Nutritional and other program requirements\nSection 4(e) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773(e) ) is amended\u2014\n**(1)**\nin paragraph (1)(A), in the second sentence, by striking free or and all that follows through the period at the end and inserting free to all children enrolled at a school participating in the school breakfast program. ; and\n**(2)**\nin paragraph (2), in the second sentence, by striking the full charge to the student for a breakfast meeting the requirements of this section or .\n##### (f) Prohibition on breakfast shaming, meal denial\n**(1) In general**\nEffective beginning on the date of enactment of this Act, a school or school food authority\u2014\n**(A)**\nshall not\u2014\n**(i)**\nphysically segregate for the purpose of debt shaming or otherwise discriminate against any child participating in the breakfast program under section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ); or\n**(ii)**\novertly identify a child described in clause (i) by a special token or ticket, an announced or published list of names, or any other means; and\n**(B)**\nshall provide the program meal to any child eligible under the program.\n**(2) Child Nutrition Act of 1966**\nSection 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ) is amended by adding at the end the following:\n(f) Prohibition on breakfast shaming A school or school food authority shall not\u2014 (1) physically segregate for the purpose of debt shaming or otherwise discriminate against any child participating in the free breakfast program under this section; or (2) overtly identify a child described in paragraph (1) by a special token or ticket, an announced or published list of names, or any other means. .\n##### (g) Department of Defense Overseas Dependents' Schools\nSection 20(b) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1789(b) ) is amended by striking by this section and all that follows through the period at the end and inserting by this section. .\n##### (h) Conforming amendments\nThe Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) is amended\u2014\n**(1)**\nby striking or reduced price each place it appears;\n**(2)**\nby striking and reduced price each place it appears; and\n**(3)**\nby striking a reduced price each place it appears.\nII\nSchool Lunch Program\n#### 201. Apportionment to States\nSection 4(b) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1753(b) ) is amended\u2014\n**(1)**\nby striking paragraph (2) and inserting the following:\n(2) Payment amounts (A) In general The national average payment for each free lunch shall be $4.63, adjusted annually for inflation in accordance with subparagraph (C) and rounded in accordance with subparagraph (D). (B) Additional payment for local food (i) Definition of locally-sourced farm product In this subparagraph, the term locally-sourced farm product means a farm product that\u2014 (I) is marketed to consumers\u2014 (aa) directly; or (bb) through intermediated channels (such as food hubs and cooperatives); and (II) with respect to the school food authority purchasing the farm product, is produced and distributed\u2014 (aa) in the State in which the school food authority is located; or (bb) not more than 250 miles from the location of the school food authority. (ii) Additional payment eligibility During a school year, a school food authority shall receive an additional payment described in clause (iii) if the State certifies that the school food authority served meals (including breakfasts, lunches, suppers, and supplements) during the last school year of which not less than 25 percent were made with locally sourced farm products. (iii) Payment amount (I) In general The additional payment amount under this subparagraph shall be\u2014 (aa) $0.30 for each free lunch and supper; (bb) $0.21 for each free breakfast; and (cc) $0.08 for each free supplement. (II) Adjustments Each additional payment amount under subclause (I) shall be adjusted annually in accordance with subparagraph (C) and rounded in accordance with subparagraph (D). (iv) Disbursement The State agency shall disburse funds made available under this clause to school food authorities eligible to receive additional reimbursement. (C) Inflation adjustment (i) In general The annual inflation adjustment under subparagraphs (A) and (B)(iii) shall reflect changes in the cost of operating the free lunch program under this Act, as indicated by the change in the Consumer Price Index for food away from home for all urban consumers. (ii) Basis Each annual inflation adjustment under subparagraphs (A) and (B)(iii) shall reflect the changes in the Consumer Price Index for food away from home for the most recent 12-month period for which that data is available. (D) Rounding On July 1, 2026, and annually thereafter, the national average payment rate for free lunch and the additional payment amount for free breakfast, lunch, supper, and supplement under subparagraph (B) shall be\u2014 (i) adjusted to the nearest lower-cent increment; and (ii) based on the unrounded amounts for the preceding 12-month period. ; and\n**(2)**\nby striking paragraph (3).\n#### 202. Nutritional and other program requirements\n##### (a) Elimination of free lunch eligibility requirements\n**(1) In general**\nSection 9 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758 ) is amended by striking subsection (b) and inserting the following:\n(b) Eligibility All children enrolled in a school that participates in the school lunch program under this Act shall be eligible to receive free lunch under this Act. .\n**(2) Conforming amendments**\n**(A)**\nSection 9 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758 ) is amended\u2014\n**(i)**\nin subsection (c), in the third sentence, by striking or at a reduced cost ; and\n**(ii)**\nin subsection (e), by striking , reduced price, .\n**(B)**\nSection 28 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1769i ) is amended\u2014\n**(i)**\nby striking subsection (b); and\n**(ii)**\nby redesignating subsection (c) as subsection (b).\n**(C)**\nSection 17(d)(2)(A) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(d)(2)(A) ) is amended\u2014\n**(i)**\nby striking clause (i); and\n**(ii)**\nby redesignating clauses (ii) and (iii) as clauses (i) and (ii), respectively.\n**(D)**\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended by striking paragraph (7) and inserting the following:\n(7) provide safeguards which restrict the use or disclosure of information concerning applicants and recipients to purposes directly connected with the administration of the plan; .\n**(E)**\nSection 1154(a)(2)(A)(i) of title 10, United States Code, is amended by striking in accordance with section 9(b)(1) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758(b)(1) ) .\n**(F)**\nSection 4301 of the Food, Conservation, and Energy Act of 2008 ( 42 U.S.C. 1758a ) is repealed.\n##### (b) No collection of debt\n**(1) In general**\nNotwithstanding any other provision of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) or any other provision of law, effective beginning on the date of enactment of this Act, as a condition of participation in the school lunch program under that Act, a school\u2014\n**(A)**\nshall not collect any debt owed to the school for unpaid meal charges; and\n**(B)**\nshall continue to accrue debt for unpaid meal charges\u2014\n**(i)**\nfor the purpose of receiving reimbursement under section 211; and\n**(ii)**\nuntil the effective date specified in section 2.\n**(2) National School Lunch Act**\nSection 9 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758 ) is amended by striking subsection (d) and inserting the following:\n(d) No collection of debt A school participating in the school lunch program under this Act shall not collect any debt owed to the school for unpaid meal charges. .\n##### (c) Prohibition on lunch shaming\nSection 9 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1758 ) is amended by adding at the end the following:\n(m) Prohibition on lunch shaming A school participating in the school lunch program under this Act shall not\u2014 (1) physically segregate for the purpose of debt shaming or otherwise discriminate against any child participating in the school lunch program under this Act; or (2) overtly identify a child described in paragraph (1) by a special token or ticket, an announced or published list of names, or any other means. .\n#### 203. Special assistance program\n##### (a) In general\nSection 11 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1759a ) is repealed.\n##### (b) Conforming amendments\n**(1)**\nSection 6 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1755 ) is amended\u2014\n**(A)**\nin subsection (a)(2), by striking sections 11 and 13 and inserting section 13 ; and\n**(B)**\nin subsection (e)(1), in the matter preceding subparagraph (A), by striking section 4, this section, and section 11 and inserting this section and section 4 .\n**(2)**\nSection 7(d) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1756(d) ) is amended by striking or 11 .\n**(3)**\nSection 8(g) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1757(g) ) is amended by striking and under section 11 of this Act .\n**(4)**\nSection 12(f) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1760(f) ) is amended by striking 11, .\n**(5)**\nSection 7(a) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1766(a) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking 4, 11, and 17 and inserting 4 and 17 ; and\n**(B)**\nin paragraph (2)(A), by striking sections 4 and 11 and inserting section 4 .\n**(6)**\nSection 1101(j)(3) of the Families First Coronavirus Response Act ( 7 U.S.C. 2011 note; Public Law 116\u2013127 ) is amended\u2014\n**(A)**\nby striking or served under section 11(a)(1) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1760(d) , 1759(a)(1)) and inserting of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1760(d) ) ; and\n**(B)**\nby striking or reduced price .\n#### 204. Price for a paid lunch\nSection 12 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1760 ) is amended\u2014\n**(1)**\nin subsection (l)(4)\u2014\n**(A)**\nby striking subparagraph (D); and\n**(B)**\nby redesignating subparagraphs (E) through (M) as subparagraphs (D) through (L), respectively;\n**(2)**\nby striking subsection (p); and\n**(3)**\nby redesignating subsections (q) and (r) as subsections (p) and (q), respectively.\n#### 205. Summer food service program for children\nSection 13 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1761 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)(A)(i)\u2014\n**(i)**\nin subclause (I), by striking have been determined eligible for free or reduced price school meals under this Act and the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) and inserting are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ;\n**(ii)**\nin subclause (II), by striking are eligible for free or reduced price school meals under this Act and the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) and inserting are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ;\n**(iii)**\nin subclause (III)(bb), by striking meet the income standards for free or reduced price school meals under this Act and the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) and inserting are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ;\n**(iv)**\nin subclause (IV), by striking are eligible for free or reduced price school meals under this Act and the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) and inserting are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ; and\n**(v)**\nin subclause (V), by striking are eligible for free or reduced price school meals under this Act and the Child Nutrition Act of 1966 ( 42 U.S.C. 1771 et seq. ) and inserting are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ;\n**(B)**\nin paragraph (2), by adding at the end the following:\n(C) Waiver If the Secretary determines that a program requirement under this section limits the access of children to meals served under this section, the Secretary may waive that program requirement. (D) Eligibility All children shall be eligible to participate in the program under this section. ;\n**(C)**\nin paragraph (5), by striking only for and all that follows through the period at the end and inserting for meals served to all children. ; and\n**(D)**\nin paragraph (13)\u2014\n**(i)**\nin subparagraph (C)(ii), by striking eligible for a free or reduced price lunch under this Act or a free or reduced price breakfast under section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ) and inserting an economically disadvantaged student (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ; and\n**(ii)**\nin subparagraph (D)(ii), by striking eligible for free or reduced price lunch under this Act or free or reduced price breakfast under section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ) and inserting economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ;\n**(2)**\nin subsection (b)(2), by striking may only serve and all that follows through migrant children ;\n**(3)**\nby striking subsection (c) and inserting the following:\n(c) Payments (1) In general Payments shall be made to service institutions for meals served\u2014 (A) during the months of May through September; (B) during school vacation at any time during an academic school year; (C) during a teacher in-service day; and (D) on days that school is closed due to a natural disaster, building repair, court order, or similar cause, as determined by the Secretary. (2) Limitation on payments A service institution shall receive payments under this section for not more than 3 meals and 1 supplement per child per day. ; and\n**(4)**\nin subsection (f)(3), by striking , except that and all that follows through section .\n#### 206. Child and adult care food program\nSection 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 ) is amended\u2014\n**(1)**\nin subsection (a)(2), by striking subparagraph (B) and inserting the following:\n(B) any other private organization providing nonresidential child care or day care outside school hours for school children; ;\n**(2)**\nby striking subsection (c) and inserting the following:\n(c) Free meals Notwithstanding any other provision of law\u2014 (1) all meals and supplements served under the program authorized under this section shall be provided for free to participants of the program; and (2) an institution that serves those meals and supplements shall be reimbursed\u2014 (A) in the case of breakfast, at the rate established for free breakfast under section 4(b)(1)(B)(i) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773(b)(1)(B)(i) ); (B) in the case of lunch, at the rate established for free lunch under section 4(b)(2)(A); and (C) in the case of a supplemental meal, $1.20, adjusted for inflation in accordance with section 4(b)(2)(C). ;\n**(3)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (2), by striking subparagraph (B) and inserting the following:\n(B) Limitation to reimbursements An institution may claim reimbursement under this paragraph for not more than 3 meals and 1 supplement per day per child. ;\n**(B)**\nby striking paragraph (3); and\n**(C)**\nby redesignating paragraph (4) as paragraph (3);\n**(4)**\nin subsection (o)\u2014\n**(A)**\nby striking paragraph (4); and\n**(B)**\nby redesignating paragraphs (5) and (6) as paragraphs (4) and (5), respectively; and\n**(5)**\nin subsection (r)\u2014\n**(A)**\nin the subsection heading, by striking Program for at-risk school children and inserting Afterschool meal and snack program ;\n**(B)**\nby striking at-risk school each place it appears and inserting eligible ;\n**(C)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by striking at-risk school and inserting eligible ; and\n**(ii)**\nin subparagraph (B), by striking operated and all that follows through the period at the end and inserting a period; and\n**(D)**\nin paragraph (4)(A), by striking only for and all that follows through the period at the end and inserting the following:\nfor\u2014 (i) not more than 1 meal and 1 supplement per child per day served on a regular school day; and (ii) not more than 3 meals and 1 supplement per child per day served on any day other than a regular school day. .\n#### 207. Meals and supplements for children in afterschool care\n##### (a) In general\nSection 17A of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766a ) is amended\u2014\n**(1)**\nin the section heading, by striking Meal supplements and inserting Meals and supplements ;\n**(2)**\nin subsection (a)(1), by striking meal supplements and inserting free meals and supplements ;\n**(3)**\nin subsection (b), by inserting meals and before supplements ;\n**(4)**\nby striking subsection (c) and inserting the following:\n(c) Reimbursement (1) In general (A) Meals A free meal provided under this section to a child shall be reimbursed at a rate of $4.63, adjusted annually for inflation in accordance with paragraph (3)(A) and rounded in accordance with paragraph (3)(B). (B) Supplements A free supplement provided under this section to a child shall be reimbursed at the rate at which free supplements are reimbursed under section 17(c)(2)(C). (2) Limitation to reimbursements An institution may claim reimbursement under this section for not more than 1 meal and 1 supplement per day per child served on a regular school day. (3) Inflation; rounding (A) Inflation adjustment (i) In general The annual inflation adjustment under paragraph (1)(A) shall reflect changes in the cost of operating the program under this section, as indicated by the change in the Consumer Price Index for food away from home for all urban consumers. (ii) Basis Each inflation annual adjustment under paragraph (1)(A) shall reflect the changes in the Consumer Price Index for food away from home for the most recent 12-month period for which that data is available. (B) Rounding On July 1, 2026, and annually thereafter, the reimbursement rate for a free meal under this section shall be\u2014 (i) adjusted to the nearest lower-cent increment; and (ii) based on the unrounded amounts for the preceding 12-month period. ; and\n**(5)**\nby adding at the end the following:\n(e) Prohibition on meal shaming A school participating in the program under this section shall not\u2014 (1) physically segregate for the purpose of debt shaming or otherwise discriminate against any child participating in the program under this section; or (2) overtly identify a child described in paragraph (1) by a special token or ticket, an announced or published list of names, or any other means. .\n##### (b) No collection of debt\n**(1) In general**\nNotwithstanding any other provision of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) or any other provision of law, effective beginning on the date of enactment of this Act, as a condition of participation in the program under section 17A of that Act, a school\u2014\n**(A)**\nshall not collect any debt owed to the school for unpaid meal supplement charges; and\n**(B)**\nshall continue to accrue debt for unpaid meal supplement charges\u2014\n**(i)**\nfor the purpose of receiving reimbursement under section 211; and\n**(ii)**\nuntil the effective date specified in section 2.\n**(2) National School Lunch Act**\nSection 17A of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766a ) is amended by adding at the end the following:\n(f) No collection of debt A school participating in the program under this section shall not collect any debt owed to the school for unpaid meal or meal supplement charges. .\n#### 208. Pilot projects\nSection 18 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1769 ) is amended\u2014\n**(1)**\nin subsection (g)(5), by striking subparagraph (B) and inserting the following:\n(B) serve a high proportion of economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )); ;\n**(2)**\nin subsection (h)(1)(A)(ii), by striking eligible for free or reduced price meals under this Act and inserting economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) ;\n**(3)**\nby striking subsection (j); and\n**(4)**\nby redesignating subsection (k) as subsection (j).\n#### 209. Fresh fruit and vegetable program\nSection 19(d) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1769a(d) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking paragraph (2) of this subsection and ;\n**(B)**\nin subparagraph (A), in the matter preceding clause (i), by striking school\u2014 and all that follows through submits in clause (ii) and inserting school that submits ;\n**(C)**\nin subparagraph (B), by striking schools and all that follows through Act and inserting high-need schools (as defined in section 2211(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6631(b) )) ; and\n**(D)**\nin subparagraph (D)\u2014\n**(i)**\nby striking clause (i); and\n**(ii)**\nby redesignating clauses (ii) through (iv) as clauses (i) through (iii), respectively; and\n**(2)**\nby striking paragraphs (2) and (3) and inserting the following:\n(2) Outreach to high-need schools Prior to making decisions regarding school participation in the program, a State agency shall inform high-need schools (as defined in section 2211(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6631(b) )), including Tribal schools, of the eligibility of the schools for the program. .\n#### 210. Training, technical assistance, and Food Service Management Institute\nSection 21(a)(1)(B) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1769b\u20131(a)(1)(B) ) is amended in the matter preceding clause (i) by striking certified to receive free or reduced price meals and inserting who are economically disadvantaged students (as identified under a measure described in section 1113(a)(5) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6313(a)(5) )) .\n#### 211. Reimbursement of school meal delinquent debt program\n##### (a) Definitions\nIn this section:\n**(1) Delinquent debt**\nThe term delinquent debt means the debt owed by a parent or guardian of a child to a school\u2014\n**(A)**\nas of the effective date specified in section 2; and\n**(B)**\nfor meals or meal supplements served by the school under\u2014\n**(i)**\nthe school breakfast program under section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 );\n**(ii)**\nthe school lunch program established under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ); or\n**(iii)**\nthe program established under section 17A of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766a ).\n**(2) Program**\nThe term program means the program established under subsection (b)(1).\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Reimbursement program\n**(1) Establishment**\nNot later than 60 days after the effective date specified in section 2, the Secretary shall establish a program under which the Secretary shall reimburse each school participating in a program described in clause (i), (ii), or (iii) of subsection (a)(1)(B) for all delinquent debt.\n**(2) Form for reimbursement**\nTo carry out the program, the Secretary shall design and distribute a form to State agencies to collect data on all delinquent debt in applicable schools in the State, grouped by school food authority.\n**(3) Completion date**\nThe Secretary shall provide all reimbursements under the program not later than 180 days after the effective date specified in section 2.\n##### (c) Report\nNot later than 2 years after the effective date specified in section 2, the Comptroller General of the United States shall submit to Congress and make publicly available a report that describes the successes and challenges of the program.\n#### 212. Conforming amendments\nThe Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) is amended\u2014\n**(1)**\nby striking or reduced price each place it appears;\n**(2)**\nby striking or a reduced price each place it appears;\n**(3)**\nby striking and reduced price each place it appears; and\n**(4)**\nby striking a reduced price each place it appears.\nIII\nReport\n#### 301. Report on free school meal programs\nNot later than 1 year after the effective date of this Act, the Administrator of the Food and Nutrition Service shall submit to Congress a report on how the school lunch program under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ) and the school breakfast program under section 4 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1773 ) impact students who participate in such programs, including\u2014\n**(1)**\nwhether the amendments made by this Act to such programs have resulted in any measurable positive academic outcomes for such students, including any increase in test scores or graduation rates;\n**(2)**\nwhether such programs increase student access to nutritional meals and locally sourced farm products (as such term is defined in section 4(b)(2)(B) of the Richard B. Russell National School Lunch Act, as amended by this Act); and\n**(3)**\nany recommendations for additional legislative or administrative actions to increase the use of locally sourced farm products in meals provided under such programs.",
      "versionDate": "2026-05-11",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-05-15T18:04:02Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8728ih.xml"
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
      "title": "Feed Our Kids Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T06:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Feed Our Kids Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T06:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Nutrition Act of 1966 and the Richard B. Russell National School Lunch Act to make breakfasts and lunches free for all children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T06:18:40Z"
    }
  ]
}
```
