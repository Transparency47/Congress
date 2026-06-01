# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2828?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2828
- Title: Child Care Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2828
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-04-16T19:14:32Z
- Update date including text: 2026-04-16T19:14:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2828",
    "number": "2828",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Child Care Modernization Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T19:14:32Z",
    "updateDateIncludingText": "2026-04-16T19:14:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
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
        "item": [
          {
            "date": "2026-03-19T14:00:50Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-17T16:51:13Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "ME"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2828is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2828\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Mrs. Fischer (for herself, Mrs. Gillibrand , Ms. Collins , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Child Care and Development Block Grant Act of 1990 to reauthorize and update the Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Child Care Modernization Act of 2025 .\n#### 2. Purposes\n##### (a) Redesignation\nSection 658A of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 ) is redesignated as section 658 of such Act.\n##### (b) Amendment\nSubsection (b) of that section 658 is amended to read as follows:\n(b) Purposes The purposes of this subchapter are\u2014 (1) to allow each State maximum flexibility in developing and implementing a mixed delivery system to provide child care that best suits the needs of children and working parents within that State; (2) to promote parental choice to empower working parents to make their own decisions regarding the child care services that best suit their family\u2019s needs; (3) to encourage States to provide consumer education information to help parents make informed choices about child care services and to promote involvement by parents and family members in the development of their children in child care settings; (4) to assist States in delivering high-quality, coordinated child care services to maximize parents\u2019 options to cover the full workday and full work year, to support continuity of care for children, and to support parents trying to achieve independence from public assistance; (5) to assist States in improving the overall quality of child care by implementing the health, safety, licensing, early learning and development, professional, and oversight standards established in this subchapter and in State law (including State regulations); (6) to assist States\u2014 (A) in supporting the educational and professional development of child care staff; and (B) in supporting child care providers in the recruitment of, professional development for, and retention of a qualified child care workforce; and (7) to increase the number and percentage of low-income children in high-quality child care settings. .\n#### 3. Definitions\n##### (a) In general\nSection 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n ) is amended\u2014\n**(1)**\nby redesignating paragraphs (5) through (7), (8) and (9), and (10) through (15), as paragraphs (6) through (8), (10) and (11), and (13) through (18), respectively;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (B), by inserting and at the end;\n**(B)**\nin subparagraph (C), by striking ; and at the end and inserting a period; and\n**(C)**\nby striking subparagraph (D);\n**(3)**\nby striking paragraph (4) and inserting the following:\n(4) Eligible activity The term eligible activity , means an activity consisting of\u2014 (A) full-time or part-time employment; (B) self-employment; (C) job search activities; (D) job training; (E) secondary, postsecondary, or adult education, including education through a program of high school classes, a course of study at an institution of higher education, classes towards an equivalent of a high school diploma recognized by State law, or English as a second language classes; (F) health treatment (including mental health and substance use treatment) for a condition that prevents the parent involved from participating in other eligible activities; (G) activities to prevent child abuse or neglect, or family violence prevention or intervention activities; (H) employment and training activities under the employment and training program, of the supplemental nutrition assistance program, established under section 6(d)(4) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2015(d)(4) ); (I) employment and training activities under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ); (J) a work activity described in subsection (d) of section 407 of the Social Security Act ( 42 U.S.C. 607 ) for which, consistent with clauses (ii) and (iii) of section 402(a)(1)(A) of such Act ( 42 U.S.C. 602(a)(1)(A) ), a parent is treated as being engaged in work for a month in a fiscal year for purposes of the program of block grants to States for temporary assistance for needy families established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ); or (K) taking leave under the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. ) (or equivalent provisions for Federal employees), a State or local paid or unpaid leave law, or a program of employer-provided leave. (5) Eligible child The term eligible child means an individual\u2014 (A) who is less than 13 years of age; (B) (i) whose family income does not exceed\u2014 (I) 85 percent of the State median income for a family of the same size; or (II) a higher percentage of that income in a State with a waiver under section 658I(c)(1)(B); and (ii) whose family assets do not exceed $1,000,000 (as certified by a member of such family); and (C) who\u2014 (i) resides with a parent or parents who are participating in an eligible activity; (ii) is a child experiencing homelessness, a child in kinship care, or a child who is receiving, or needs to receive, child protective services; or (iii) resides with a parent who is more than 65 years of age. ;\n**(4)**\nin paragraph (7), as so redesignated\u2014\n**(A)**\nin subparagraph (A), by striking or at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; or ;\n**(C)**\nby added at the end the following:\n(C) notwithstanding section 645(a)(1)(B) of the Head Start Act ( 42 U.S.C. 9840(a)(1)(B) ), a Head Start agency. ; and\n**(D)**\nby adding at the end the following flush sentence:\nNotwithstanding subparagraph (B), a licensed, regulated, or registered child care provider (or a staff member of the child care provider) who is otherwise eligible for assistance under this Act shall continue to be eligible for such assistance for the care of children for whom the provider is the legal parent if other eligible children with respect to whom such provider is not the legal parent are also being cared for by that provider. ;\n**(5)**\nby striking paragraph (8), as so redesignated, and inserting the following:\n(8) Family child care provider The term family child care provider means an individual who provides child care services in a private residence\u2014 (A) for fewer than 24 hours per day per child; or (B) for 24 hours per day per child due to the nature of the work of the parent involved. (9) Homeless child The term homeless child means an individual described in section 725(2) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11434a(2) ). ;\n**(6)**\nin paragraph (10), as so redesignated, by striking (10) and all that follows through meaning and inserting the following:\n(10) Indian Tribe; Indian tribe The term Indian Tribe or Indian tribe has the meaning ;\n**(7)**\nby inserting after paragraph (11), as so redesignated, the following:\n(12) Mixed delivery system The term mixed delivery system means a system of child care services that\u2014 (A) promotes parental choice to empower working parents to make their own decisions regarding the child care services that best suit their family\u2019s needs; (B) delivers services through a combination of programs offered by eligible child care providers (including faith-based and community-based child care providers) in a variety of settings (including family child care homes, child care centers, Head Start centers, and public and private schools); and (C) may be supported with a combination of public and private funds. ;\n**(8)**\nin paragraph (15), as so redesignated, by striking unless the context specifies otherwise and inserting except as otherwise specified ; and\n**(9)**\nin paragraph (18), as so redesignated, by striking (18) and all that follows through has the meaning and inserting the following:\n(18) Tribal organization; tribal organization (A) In general The term Tribal organization or tribal organization has the meaning .\n##### (b) Redesignation\nThe Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 658P as section 658A; and\n**(2)**\nby moving section 658A, as so redesignated, to follow section 658, as redesignated by section 2.\n#### 4. Authorization of appropriations\n##### (a) Part\nThe Child Care and Development Block Grant Act of 1990 is amended by inserting before section 658B the following:\nI Child care services .\n##### (b) In general\nSection 658B of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858 ) is amended to read as follows:\n658B. Authorization of appropriations There is authorized to be appropriated to carry out this subchapter (other than section 658T) such sums as may be necessary for each of fiscal years 2026 through 2030. .\n#### 5. Lead agency\nSection 658D(b) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858b(b) ) is amended by striking paragraph (2) and inserting the following:\n(2) Development of plan The lead agency shall develop the State plan described in paragraph (1)(B) in meaningful consultation with\u2014 (A) parents of children eligible for services under this subchapter, which shall include parents of children in a priority population described in section 658E(c)(2)(M); (B) eligible child care providers that represent the various geographic areas and types of providers in the State; (C) employers of various sizes and with various hours and days of operations whose employees rely on reliable and accessible child care to work; and (D) appropriate representatives of units of general purpose local government and, as appropriate, of Indian Tribes and Tribal organizations. .\n#### 6. Application and plan\nSection 658E(c) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858c(c) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)(i)(I), by striking a child and inserting an eligible child ;\n**(B)**\nin subparagraph (D), by striking , not later and all that follows through subparagraph (K)(i), ;\n**(C)**\nin subparagraph (E)(i)\u2014\n**(i)**\nin the matter preceding subclause (I), by inserting , offered through a mixed delivery system, after full diversity of child care services ;\n**(ii)**\nin subclause (I), by inserting (including information on the hours and days of operation and ages served) after of child care services ; and\n**(iii)**\nin subclause (IV)\u2014\n**(I)**\nby striking and before the Medicaid ; and\n**(II)**\nby inserting before the semicolon the following: , and the Maternal, Infant, and Early Childhood Home Visiting Programs under section 511 of the Social Security Act ( 42 U.S.C. 711 ) ;\n**(D)**\nin subparagraph (G)\u2014\n**(i)**\nin the subparagraph heading, by striking Training and professional and inserting Professional ;\n**(ii)**\nin clause (i) and clause (ii) (in the matter preceding subclause (I)), by striking training and before professional development ;\n**(iii)**\nin clause (ii)(II), by striking , and may engage and all that follows through training framework ; and\n**(iv)**\nin clause (iii), by striking training and inserting professional development ;\n**(E)**\nin subparagraph (I)(i)(IX), by striking if applicable, ;\n**(F)**\nin subparagraph (J)\u2014\n**(i)**\nby striking that procedures and inserting the following:\nthat\u2014 (i) procedures ;\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(ii) the State will undertake a review of State and local health and safety requirements (including requirements for inspections under this subchapter and the child and adult care food program established under section 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 )) to determine redundancies and oversights that may exist, to ensure\u2014 (I) children receive child care services in healthy and safe environments; and (II) child care providers can easily identify, understand, and comply with applicable health and safety requirements. ;\n**(G)**\nin subparagraph (K)(i)\u2014\n**(i)**\nin the matter preceding subclause (I), by striking , not later and all that follows through 2014, ; and\n**(ii)**\nin subclause (IV), by striking section 658P(6)(B) and inserting section 658A(7)(B) ;\n**(H)**\nin subparagraph (M)\u2014\n**(i)**\nby redesignating clauses (ii) through (iv) as clauses (iv) through (vi), respectively;\n**(ii)**\nby striking clause (i) and inserting the following:\n(i) children in underserved areas, including areas that have significant concentrations of poverty or unemployment and that do not have a sufficient supply of eligible child care providers; (ii) children experiencing homelessness, children in foster care, children in kinship care, and children who are receiving, or need to receive, child protective services; and (iii) children in rural areas; ; and\n**(iii)**\nin clause (v), as so redesignated, by striking , as defined by the State ;\n**(I)**\nin subparagraph (N)(iii), by striking At the option of the State, the and inserting The ;\n**(J)**\nin subparagraph (O)(i), by striking full-day services and inserting full workday and full work year services ;\n**(K)**\nin subparagraph (S)(ii), by striking , to the extent and all that follows through fixed costs and inserting implement enrollment and eligibility policies that support the fixed and operational costs ;\n**(L)**\nin subparagraph (T)(i), by striking or implement and all that follows through of 2014) and inserting and implement developmental guidelines ;\n**(M)**\nin subparagraph (U)\u2014\n**(i)**\nin clause (ii), by inserting State and local health agencies, after licensing of child care providers, ; and\n**(ii)**\nin clause (iii)(II), by striking following the emergency or disaster, which may include and inserting during and following the emergency or disaster, which shall include guidelines for ;\n**(N)**\nin subparagraph (V), by striking develop and all that follow through services. and inserting\nsupport child care business technical assistance including supporting\u2014 (i) provision of strategies to support management coaching and the use of core best business practices; (ii) development and use of shared services initiatives including initiatives involving provider networks such as child care center alliances and family child care provider networks; and (iii) coordination of activities with programs of the Small Business Administration, programs of the Department of Agriculture, and other Federal, State, and local programs supporting child care businesses. ; and\n**(O)**\nby adding at the end the following:\n(W) Benchmarks The plan shall include benchmarks for the indicators described in the clauses of section 658K(a)(3)(B). ;\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (B)(ii), by striking Not later and all that follows through shall prepare and inserting Not later than September 30 of each fiscal year, the Secretary shall prepare ; and\n**(B)**\nin subparagraph (D)\u2014\n**(i)**\nby striking with respect to and all that follows through 2020 and inserting with respect to each fiscal year) ; and\n**(ii)**\nby striking described in clause (i), (ii), (iii), or (iv) of and inserting in priority populations described in ;\n**(3)**\nin paragraph (4)\u2014\n**(A)**\nby striking subparagraphs (A) and (B) and inserting the following:\n(A) In general The State plan shall certify that, not later than the later of the date that is 5 years after the date of submission of the application, and September 30, 2031, payment rates for the provision of child care services for which assistance is provided in accordance with this subchapter\u2014 (i) will be sufficient to meet the cost of providing the child care services, including the fixed and operational costs of providing the child care services; and (ii) will be set and paid in accordance with a cost estimation model described in subparagraph (B). (B) Cost estimation model The State plan shall\u2014 (i) demonstrate that the State, after consulting with eligible child care providers that represent the various geographic areas of the State and types of providers within the State\u2019s mixed delivery system, State and local child care program administrators, local child care resource and referral agencies, and other appropriate entities, has developed and uses (or if the State has not used such a model certify that the State, after such consultation but not later than the later of the date that is 5 years after the date of submission of the application described in subsection (a), and September 30, 2031, will develop and use) a statistically valid and reliable cost estimation model for the direct payment rates for providers of child care services in the State, that\u2014 (I) reflects the costs of service delivery, including fixed costs and operating expenses; (II) reflects the cost of staff salaries and benefits necessary to sufficiently recruit, train, and retain a qualified child care workforce; (III) reflects variations in the costs of service delivery by submarket, type of provider, and children served, including by\u2014 (aa) geographic area (such as location in a urban or rural area); (bb) ages of children; (cc) whether the children have particular needs (such as needs of children with disabilities and children served by child protective services); (dd) whether the providers provide services during weekend and other nontraditional hours; and (ee) quality of child care provider as determined by the State; and (IV) is reviewed once every 2 years and adjusted to\u2014 (aa) ensure payment rates remain sufficient to meet the requirements of this subchapter; and (bb) provide a cost of living increase to maintain the level of services provided during the year prior to the review; and (ii) describe how the State will provide for timely payments, set in accordance with the model described in clause (i), for child care services provided under this subchapter. ;\n**(B)**\nin subparagraph (C)\u2014\n**(i)**\nby striking clause (ii); and\n**(ii)**\nby striking (C) and all that follows through Nothing and inserting the following:\n(C) Construction Nothing ; and\n**(C)**\nby adding at the end the following:\n(D) No Federal control The Secretary may offer guidance to States on cost estimation models described in subparagraph (B), but shall not require a State to adopt a particular cost estimation model or an element of a particular cost estimation model (except that the model shall meet the requirements of subparagraph (B)(i)). ; and\n**(4)**\nby striking paragraph (5) and inserting the following:\n(5) Sliding fee scale The State plan shall provide that the State will establish and periodically revise by rule a sliding fee scale to determine a full copayment for a family receiving assistance under this subchapter (or, for a family receiving part-time care, a reduced copayment that is an appropriate amount of the full copayment) and that is not a barrier that restricts families from accessing child care services under this subchapter. .\n#### 7. Activities to improve the quality of child care\nSection 658G(a) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858e(a) )\u2014\n**(1)**\nin paragraph (1), by adding at the end the following: The State shall include, in the State's activities, developing and expanding initiatives to assist child care providers in their efforts to recruit, train, and retain a qualified child care workforce. ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking subparagraph (A) and inserting the following:\n(A) to carry out the activities described in paragraph (1), not less than 9 percent of the funds described in paragraph (1) for each fiscal year; and ; and\n**(B)**\nin subparagraph (B), by striking received not later and all that follows through succeeding full fiscal year and inserting received for each fiscal year .\n#### 8. Waivers of income requirement\nSection 658I(c) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858g(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking of not more than three years and inserting described in paragraph (5) ;\n**(B)**\nin subparagraph (A), by striking (A) and inserting (A)(i) ;\n**(C)**\nin subparagraph (B), by striking (B) and inserting the following:\n(ii) ;\n**(D)**\nin subparagraph (C), by striking (C) and inserting the following:\n(iii) ;\n**(E)**\nin subparagraph (D)\u2014\n**(i)**\nby striking (D) and inserting the following:\n(iv) ; and\n**(ii)**\nin clause (iv), as so redesignated, by striking the period and inserting ; or ; and\n**(F)**\nby adding at the end the following:\n(B) the State, on the date of the request, has a maximum income standard that meets section 658A(5)(B)(i), and requests the waiver to raise that standard. ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (B), by striking and at the end;\n**(B)**\nin subparagraph (C), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(D) if the State seeks a waiver of section 658A(5)(B)(i)(I) under paragraph (1)(B) include\u2014 (i) the maximum income standard that the State wishes to use; (ii) such information as determined necessary by the Secretary to demonstrate that the State is serving all eligible children to the best of the State's ability below the maximum income standard in that section, and will continue to prioritize and serve all eligible children below the maximum income standard if a waiver under paragraph (1)(B) should be approved; (iii) information demonstrating that the State is meeting the requirements of the State plan under section 658E(c), particularly the requirements of subparagraphs (M) and (Q) of paragraph (2) of that section; and (iv) information demonstrating that the payment rates described in that section are set and paid in accordance with a cost estimation model described in section 658E(c)(4)(B). ;\n**(3)**\nin paragraph (7)\u2014\n**(A)**\nby striking The Secretary may and inserting the following:\n(A) General renewals The Secretary may ;\n**(B)**\nin the first sentence, by inserting before the period the following: , in the case of a request for a waiver of a provision other than section 658A(5)(B)(i)(I) ;\n**(C)**\nin the second sentence, by striking seeking to renew their waiver approval and inserting seeking that renewal ;\n**(D)**\nin the third sentence, by striking extension request and inserting renewal request ; and\n**(E)**\nby adding at the end the following:\n(B) Renewals of income requirement waivers A State may seek a renewal, of an existing waiver of section 658A(5)(B)(i)(I) under paragraph (1)(B) (including a previously renewed waiver), for a period no longer than 3 years. A State seeking that renewal shall inform the Secretary of this intent no later than 30 days prior to the expiration date of the waiver. The State shall re-certify in its renewal request the provisions in paragraph (2). On determining that the State has accurately re-certified those provision, the Secretary shall grant the renewal. ; and\n**(4)**\nin paragraph (8)\u2014\n**(A)**\nby inserting , other than paragraph (1)(B), after this subchapter each place the term appears; and\n**(B)**\nby adding at the end the following: Nothing in this subsection, including paragraph (1)(B), shall be construed to permit a State to deny or limit access to, or increase copayments, as a direct result of obtaining this waiver, for child care services under this subchapter to any eligible child whose family income is below the maximum income standard described in paragraph (1)(B) and whose family assets are less than the asset limit described in section 658A(5)(B)(ii). .\n#### 9. Reports and audits\nSection 658K(a) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858i(a) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin the matter preceding subparagraph (A)\u2014\n**(i)**\nby striking Not later than and all that follows through a State and inserting A State ; and\n**(ii)**\nby inserting annually before prepare ;\n**(B)**\nin subparagraph (A), by striking section 658P(6) and inserting section 658A(7) ; and\n**(C)**\nin subparagraph (F), by striking section 658P(6)(B) and inserting section 658A(7)(B) ; and\n**(2)**\nby adding at the end the following:\n(3) Additional State reports (A) Information on percentage of income families are spending on child care In addition to the report described in paragraph (2), a State described in paragraph (1)(A) shall, not later than the date that the State submits a State plan under section 658E, prepare and submit to the Secretary a report that includes\u2014 (i) information on\u2014 (I) the percentage of income spent on child care for families that\u2014 (aa) have children that are eligible to receive but are not receiving assistance under this subchapter; and (bb) are residing in the State; and (II) the child care options that are available to such families at an affordable rate; and (ii) the results of a feasibility study on how, over the next 5 years, the State could\u2014 (I) lower the percentage of the family income, of families described in clause (i), that the families spend on child care copayments; and (II) increase access to child care so that all eligible children in the State receive child care. (B) Progress report The State shall, not later than the date that the State submits a State plan under section 658E, prepare and submit to the Secretary a report that includes an analysis of the progress the State has made over the preceding 10 years, on benchmarks described in the State plan under section 658E(c)(2)(W), in the child care program carried out under this subchapter, relating to indicators consisting of\u2014 (i) child and family eligibility and enrollment; (ii) affordability of child care for families with an eligible child; (iii) expansion of parental choice and equal access; (iv) payment rates and payment practices; (v) recruiting and retaining a skilled, qualified, and appropriately compensated child care workforce; (vi) quality improvement activities; (vii) lead agency coordination and partnership; (viii) family outreach and consumer education; and (ix) program integrity and accountability. (C) Reports to congress The Secretary shall submit a report to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives on the information reported to the Secretary by States as described in subparagraphs (A) and (B). .\n#### 10. Reports, hotline, and website\nSection 658L(a) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858j(a) ) is amended by striking Not later and all that follows through the Secretary shall and inserting The Secretary shall biennially .\n#### 11. Technical amendments\nSection 658O(a) of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858m(a) ) is amended\u2014\n**(1)**\nin paragraphs (1), (3), and (4) by striking this subchapter and inserting section 658B ; and\n**(2)**\nin paragraph (5) by striking this subchapter the first place it appears and inserting section 658B .\n#### 12. Child care supply and facilities grants\nThe Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) is amended by adding at the end the following:\nII Child care supply and facilities 658T. Child care supply and facilities grants (a) Purposes The purposes of this section are to provide grants to States, territories described in section 658O(a)(1) (referred to individually in this part as a territory ), Indian Tribes, and Tribal organization to\u2014 (1) expand the supply and capacity of qualified child care providers and staff so that working parents have multiple high-quality child care options to choose from in making their own decisions regarding the child care services that best suit their family\u2019s needs; and (2) ensure child care facilities are designed and equipped to keep children healthy and safe and to enhance children\u2019s physical, cognitive, and behavioral development. (b) Qualified child care provider In this section, the term qualified child care provider means\u2014 (1) an eligible child care provider as defined in section 658A(7)(A) that is providing, or seeking to provide, child care services to children eligible for services under this subchapter; or (2) a child care provider that has applied under this subchapter to become an eligible child care provider as defined in section 658A(7)(A) and that commits to provide child care services to children eligible for services under this subchapter. (c) Authorization of appropriations There is authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2027 through 2030. (d) Grants authorized; allotments (1) In general From funds made available under subsection (c), the Secretary shall make grants to States, territories, Indian Tribes, and Tribal organizations to carry out the activities described in subsection (f). (2) Reservation The Secretary shall reserve not more than 1 percent of the amount appropriated under subsection (c) for a fiscal year to carry out this section to pay for the costs of the Federal administration of this section. (3) Allotments From the amount appropriated to carry out this section for a fiscal year that remains after the Secretary makes the reservation under paragraph (2), the Secretary shall award to each lead agency with an approved plan under subsection (e), a child care supply and facilities grant in accordance with paragraphs (1) and (2) of subsection (a), and subsection (b), of section 658O, for the grants authorized under paragraph (1). A grant made under this paragraph in accordance with paragraph (1) or (2) of that subsection shall be for the purpose of carrying out the program described in this section, consistent, to the extent practicable as determined by the Secretary, with the requirements applicable to States. (e) State plan (1) In general In order to receive a grant under this section, a State shall submit a plan to the Secretary, at such time and in such manner as the Secretary may reasonably require. (2) Contents Each plan submitted by a State under this section shall include each of the following: (A) A description of how the State will use funds received under this section for State-level activities under subsection (f)(1). (B) A description of how the State will ensure that qualified child care providers in rural, suburban, and urban areas can readily apply for and access funding under this section, which shall include providing technical assistance either directly or through a third party which may include a resource and referral agency or a staffed family child care provider network. (C) A description of how the State will determine the prioritization of subgrants to qualified child care providers in accordance with subsection (f)(5). (D) An assurance that the State will make available to the public, which shall include, at a minimum, posting to an internet website of the lead agency\u2014 (i) a notice of funding availability through subgrants for qualified child care providers under this section; and (ii) the criteria for awarding subgrants for qualified child care providers, including the methodology the lead agency will use to determine the amounts of such subgrants for qualified child care providers. (E) A determination by the State of the duration of child care services required for qualified child care providers to receive subgrants under this subchapter. (f) State use of funds (1) Reservation A lead agency that receives a grant under subsection (d) shall reserve not more than 10 percent of the grant funds for State-level activities, consisting of administering subgrants and providing technical assistance and support, for activities supported under this section. (2) Subgrants The lead agency shall use the remainder of the grant funds awarded pursuant to subsection (d) to make subgrants as described in paragraphs (3) and (4). (3) Startup and supply expansion subgrants (A) In general The lead agency shall make startup and supply expansion subgrants to qualified child care providers that are providing, or seeking to provide, child care services under this subchapter to eligible children, to\u2014 (i) support the providers in paying for startup and expansion costs; (ii) assist such providers in meeting\u2014 (I) the health and safety requirements (including the requirements referred to in section 658E(c)(2)(I)) of the State, territory, Indian Tribe, or local government involved, as the case may be; (II) the child-to-provider ratio standards (including the requirements referred to in section 658E(c)(2)(H)) applicable to the provider; (III) licensing and other regulatory standards of the State, territory, Indian Tribe, or local government involved, as the case may be, for child care providers; and (IV) as applicable, the requirements of a State\u2019s tiered quality rating system for child care providers; (iii) establish or expand the operation of community-or neighborhood-based family child care networks; and (iv) support access to child care services facing a particular shortage of child care options, including child care services during nontraditional or extended hours, and child care services for children with disabilities (including, for purposes of this clause, a child who has documentation other than an individualized education program (as defined in section 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 )) establishing the child's disability (as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 ))). (B) Requirement As a condition of receiving a startup or supply expansion subgrant under this paragraph, a qualified child care provider shall commit to meeting the requirements for an eligible child care provider under this subchapter and to providing child care services under this subchapter to eligible children, on an ongoing basis, as determined by the State. (4) Facilities subgrants (A) In general The lead agency shall make facilities subgrants to qualified child care providers that are providing, or seeking to provide, child care services under this subchapter to eligible children, for, notwithstanding section 658F(b)\u2014 (i) remodeling, renovation, or repair of a building or facility used for providing direct child care services; and (ii) construction, permanent improvement, or major renovation of a building or facility used for providing direct child care services. (B) Requirement As a condition of receiving a facilities subgrant under this paragraph, a child care provider shall commit to meeting the requirements for an eligible child care provider under this subchapter and to providing child care services under this subchapter to eligible children on an ongoing basis, as determined by the State. (C) Federal interest (i) Family child care homes Federal law regarding a Federal interest in real property shall not apply to the renovation, remodeling, repair, or permanent improvement of privately owned family child care homes with funds provided under this paragraph, and the Secretary shall develop parameters for the use of such funds for family child care homes. (ii) Retention If the Secretary retains a Federal interest in any facility constructed, renovated, remodeled, repaired, or permanently improved with funds provided under this paragraph, the Secretary shall not retain the Federal interest for more than 10 years. (5) Priority In awarding subgrants under paragraphs (3) and (4), the lead agency shall give priority to qualified child care providers providing or seeking to provide child care services to priority populations of children described in section 658E(c)(2)(M). (g) Supplement not supplant Amounts made available to carry out this section shall be used to supplement and not supplant other Federal, State, and local public funds expended to increase the supply of child care and to improve child care facilities. (h) Documentation and reporting requirements (1) Documentation A State receiving a grant under subsection (d) shall provide documentation of any State expenditures from grant funds received under subsection (d) in accordance with section 658K(b), to the independent entity described in that section. (2) Reports (A) Lead agency annual report A lead agency receiving a grant under subsection (d) shall, not later than 12 months after making subgrants from the funds made available through such grant, and annually for the duration of the grant, submit a report to the Secretary that includes, for the State involved, a description of each of the lead agency\u2019s programs of subgrants carried out to meet the objectives of this section, including\u2014 (i) the number of eligible child care providers in operation at the start of the grant period, and the number of such providers 11 months later, disaggregated by age of children served, geographic region, and child care setting (including whether the provider was in a center-based or family child care setting); (ii) the number of child care slots, in the capacity of eligible child care providers given applicable group size limits and staff-to-child ratios, that were open for attendance of children at the start of the grant period and the number of such slots 11 months later, disaggregated by age of children served, geographic region, and child care setting (including whether the slot was in a center-based or family child care setting), and each priority population of children described in section 658E(c)(2)(M); (iii) (I) the number and percentage of qualified child care providers that received a subgrant under subsection (f)(3), disaggregated by age of children served, geographic region, and child care setting (including whether the provider was in a center-based or family child care setting), and the average and range of the amounts of the subgrants awarded; and (II) the number and percentage of qualified child care providers that received a subgrant under subsection (f)(4), disaggregated by age of children served, geographic region, and child care setting (including whether the provider was in a center-based or family child care setting), and the average and range of the amounts of the subgrants awarded; and (iv) information concerning how qualified child care providers receiving subgrants under subsection (f)(3) or (f)(4) used the subgrant funding received. (B) Report to Congress The Secretary shall transmit annually to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives a report that provides national and State-level data for the information collected under subparagraph (A). (i) Construction No reference in part 1 to this subchapter shall be considered to refer to a provision of this part. .\n#### 13. Department of Agriculture loan restrictions\nThe Secretary of Agriculture shall revise section 3555.102(c) of title 7, Code of Federal Regulations, as in effect on the date of enactment of this Act, to exclude a business that is licensed, regulated, or registered as a child care provider under State law.",
      "versionDate": "2025-09-17",
      "versionType": "Introduced in Senate"
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
            "name": "Accounting and auditing",
            "updateDate": "2026-04-16T19:14:23Z"
          },
          {
            "name": "Child care and development",
            "updateDate": "2026-04-16T19:14:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T19:14:32Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-16T19:14:19Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-16T19:14:28Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-16T19:14:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Families",
        "updateDate": "2025-11-19T12:10:17Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2828is.xml"
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
      "title": "Child Care Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Child Care Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Child Care and Development Block Grant Act of 1990 to reauthorize and update the Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:25Z"
    }
  ]
}
```
