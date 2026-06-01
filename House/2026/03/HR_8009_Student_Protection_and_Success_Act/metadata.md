# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8009
- Title: Student Protection and Success Act
- Congress: 119
- Bill type: HR
- Bill number: 8009
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-06T13:16:47Z
- Update date including text: 2026-04-06T13:16:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8009",
    "number": "8009",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Student Protection and Success Act",
    "type": "HR",
    "updateDate": "2026-04-06T13:16:47Z",
    "updateDateIncludingText": "2026-04-06T13:16:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:03:00Z",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8009ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8009\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mrs. Houchin (for herself and Ms. Perez ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to provide for institutional ineligibility based on low cohort repayment rates and to require risk-sharing payments of institutions of higher education.\n#### 1. Short title\nThis Act may be cited as the Student Protection and Success Act .\n#### 2. Institutional ineligibility based on low cohort repayment rate\n##### (a) In general\nSection 455 of the Higher Education Act of 1965 ( 20 U.S.C. 1087e ) is amended by adding at the end the following:\n(r) Ineligibility due to low cohort repayment rate (1) In general Beginning with fiscal year 2028 and each succeeding fiscal year, an institution that has a cohort repayment rate that is equal to or less than 15 percent shall not be eligible to participate in a program under this part for such fiscal year and for the 2 succeeding fiscal years. (2) Appeals (A) In general An institution may appeal the loss of eligibility under this subsection to the Secretary within 30 days of receiving notification from the Secretary of the loss of eligibility under this subsection. (B) Continued participation During an appeal under subparagraph (A), the Secretary may permit the institution to continue to participate in a program under this part if the institution demonstrates to the satisfaction of the Secretary that the Secretary's calculation of its cohort repayment rate is not accurate, and that recalculation would increase its cohort repayment rate to be more than 15 percent. (C) Required payment If an institution continues to participate in a program under this part, and the institution's appeal of the loss of eligibility is unsuccessful, the institution shall be required to pay to the Secretary an amount equal to the amount of loans made by the Secretary under this part to borrowers attending, or planning to attend, that institution during the pendency of such appeal and the interest, special allowance, reinsurance, and any related payments made by the Secretary (or which the Secretary is obligated to make) with respect to such loans. (3) Cohort repayment rate (A) In general In this subsection, the term cohort repayment rate means, for any fiscal year beginning with fiscal year 2028\u2014 (i) in the case in which 30 or more borrowers at the institution enter repayment on Federal Direct Stafford Loans, Federal Direct Unsubsidized Stafford Loans, Federal Direct PLUS Loans, or Federal Direct Consolidation Loans, received for attendance at the institution, the percentage of those borrowers who are not in default and who make at least a one dollar reduction on their initial student loan principal balance before the end of the second fiscal year following the fiscal year in which the borrowers entered repayment, except as provided in subparagraph (B); and (ii) in the case in which less than 30 borrowers at the institution enter repayment on Federal Direct Stafford Loans, Federal Direct Unsubsidized Stafford Loans, Federal Direct PLUS Loans, or Federal Direct Consolidation Loans, received for attendance at the institution, the percentage of those borrowers plus all of the borrowers at the institution who entered repayment on such loans (or on the portion of a loan made under section 428C that is used to repay any such loans) in the 3 fiscal years preceding the fiscal year for which the determination is made, who are not in default and who make at least a one dollar reduction on their initial student loan principal balance before the end of the second fiscal year following the year in which the borrowers entered repayment, except as provided in subparagraph (B). (B) Exception The cohort repayment rate calculation under subparagraph (A) shall not include in the calculation a borrower who is\u2014 (i) in deferment on repayment of a loan described in subparagraph (A) due to study in an approved graduate fellowship program or in an approved rehabilitation training program for the disabled; (ii) in deferment on repayment of a loan described in subparagraph (A) during a period of at least half-time enrollment in college or a career school; (iii) in deferment on repayment of a loan described in subparagraph (A) during a period of service qualifying for loan discharge or cancellation under part E; (iv) in deferment on repayment of a loan described in subparagraph (A) due to active duty military service of the borrower during a war, military operation, or national emergency; (v) in deferment on repayment of a loan described in subparagraph (A) during the 13 months following the conclusion of qualifying active duty military service by the borrower, or until the borrower returns to enrollment on at least a half-time basis, whichever is earlier, if the borrower is a member of the National Guard or other reserve component of the Armed Forces and was called or ordered to active duty while enrolled at least half-time at an eligible school or within 6 months of having been enrolled at least half-time; (vi) in mandatory forbearance on repayment of a loan described in subparagraph (A) for the full fiscal year; or (vii) serving as a volunteer under the Peace Corps Act ( 22 U.S.C. 2501 et seq. ) or the Domestic Volunteer Service Act of 1973 ( 42 U.S.C. 4950 et seq. ). (C) Publication of repayment rates The Secretary shall publish the cohort repayment rates for institutions determined under this subsection. (4) Notification Beginning with the first fiscal year for which data are available after the date of enactment of the Student Protection and Success Act and each succeeding fiscal year until fiscal year 2028, the Secretary shall notify each institution that has a cohort repayment rate that is equal to or less than 15 percent that the institution risks losing eligibility to participate in a program under this part. .\n##### (b) Ineligibility in other programs\n**(1) Pell grants**\nSection 401(j) of the Higher Education Act of 1965 ( 20 U.S.C. 1070a(j) ) is amended\u2014\n**(A)**\nin the heading, by striking based on default rates ;\n**(B)**\nin paragraph (1), by inserting until fiscal year 2028 after succeeding fiscal year ;\n**(C)**\nin paragraph (2), by inserting or cohort repayment rate determination after default rate determination ; and\n**(D)**\nby adding at the end the following:\n(3) Ineligibility based on low cohort repayment rates No institution of higher education shall be an eligible institution for purposes of this subpart if such institution of higher education is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r). .\n**(2) Student loan insurance program**\nSection 435(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1085(a) ) is amended\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin the heading, by striking based on high default rates ;\n**(ii)**\nin subparagraph (A), by striking An institution and inserting Until fiscal year 2028, an institution ; and\n**(iii)**\nby adding at the end the following:\n(E) No institution of higher education shall be an eligible institution for purposes of this part if such institution of higher education is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r). ; and\n**(B)**\nin paragraph (6)(A), by inserting and until fiscal year 2028, after July 1, 1999, .\n**(3) Federal Perkins Loans**\nSection 462 of the Higher Education Act of 1965 ( 20 U.S.C. 1087bb ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by inserting or the institution is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r) after subsection (f) ; and\n**(ii)**\nin paragraph (2)(D), by inserting or the institution is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r) after subsection (f) ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (2), by inserting or the institution is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r) after subsection (f) ; and\n**(ii)**\nin paragraph (3), by inserting or the institution is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r) after subsection (f) ;\n**(C)**\nin subsection (e)\u2014\n**(i)**\nin paragraph (2), by inserting until fiscal year 2028, after succeeding fiscal year ; and\n**(ii)**\nin paragraph (3)\u2014\n**(I)**\nin subparagraph (A), by inserting until fiscal year 2028, after any succeeding fiscal year ; and\n**(II)**\nby adding at the end the following:\n(F) Low cohort repayment rates An institution that is ineligible to participate in a program under part D due to a low cohort repayment rate, as determined under section 455(r), shall not be eligible to participate in a program under this part. ; and\n**(D)**\nin subsection (f)(2), by inserting until fiscal year 2028, after subsequent years .\n#### 3. College opportunity bonus program\nSubpart 1 of part A of title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070a et seq. ) is amended by adding at the end the following:\n401B. College opportunity bonus program (a) Program authority (1) In general Beginning with fiscal year 2028 and each succeeding fiscal year, the Secretary shall award grants to eligible institutions of higher education that are distributed under a formula determined by the Secretary under subsection (d). (2) Eligible institution In this section, the term eligible institution of higher education means an institution of higher education that has a cohort repayment rate (as defined in section 455(r)(3)) that is greater than 25 percent. (b) Grants The Secretary shall award grants to eligible institutions of higher education that the Secretary determines have a strong record of making college more affordable and increasing college access and success for low-income and moderate-income students. (c) Uses of funds Each eligible institution of higher education that receives a grant under this section may use the grant funds to support reforms to further increase college access and success for low- and moderate-income students, by making key investments and adopting best practices, including by considering best practices reported under section 5 of the Student Protection and Success Act , and by\u2014 (1) awarding additional need-based financial aid to students enrolled at the institution who are eligible to receive a Federal Pell Grant; (2) enhancing academic and student support services; and (3) establishing or expanding accelerated learning opportunities. (d) Amount of grant funds (1) In general Each eligible institution of higher education that receives a grant under this section shall receive annual grant funds based on a formula determined by the Secretary that equally considers\u2014 (A) the number and percentage of students enrolled at the institution who are eligible to receive a Federal Pell Grant; (B) the cohort repayment rate (as defined in section 455(r)(3)) of students enrolled at the institution who are eligible to receive a Federal Pell Grant; and (C) the institution\u2019s student service expenditures as a percentage of the institution\u2019s student service resources. (2) Cap Each eligible institution of higher education that receives a grant under this section shall receive grant funds for a fiscal year in an amount that is not more than 2.5 percent of the amount equal to the eligible institution's total annual revenues and investment returns less auxiliary enterprise revenues and hospital revenues, as defined in the IPEDS Finance Survey, for the most recent fiscal year upon which the eligible institution\u2019s audited financial reports are available. (e) Supplement not supplant Funds made available under this section shall be used to supplement, and not supplant\u2014 (1) other State funds that States would otherwise expend to carry out activities under this section to improve college affordability and graduate additional low- and moderate-income students; and (2) institutional funds that eligible institutions of higher education receiving a grant under this section would otherwise expend to carry out activities under this section to improve college affordability and graduate additional low- and moderate-income students. (f) Funding The grant program under this section shall be funded only with risk-sharing payments received by the Secretary under section 454(d). .\n#### 4. Risk-sharing payments\nSection 454 of the Higher Education Act of 1965 ( 20 U.S.C. 1087d ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (6), by striking and after the semicolon;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(8) provide that the institution accepts the institutional risk-sharing requirements under subsection (d), if applicable. ; and\n**(2)**\nby adding at the end the following:\n(e) Institutional risk-Sharing based on cohort nonrepayment loan balances (1) In general Beginning with fiscal year 2028 and each succeeding fiscal year, each institution of higher education participating in the direct student loan program under this part shall remit to the Secretary, at such times as the Secretary may specify, a risk-sharing payment based on the cohort nonrepayment loan balance of the institution, as determined under paragraph (2). (2) Determination of risk-sharing payments (A) Determination of cohort loan balance The cohort loan balance of an institution for a fiscal year equals the total principal amount of all loans made under this part to attend such institution for the cohort of borrowers who entered repayment, deferment, or forbearance on such loans in the third preceding fiscal year for which the determination is made. (B) Determination of cohort nonrepayment loan balance (i) In general The cohort nonrepayment loan balance of an institution for a fiscal year equals, from the total amount of the loans described in subparagraph (A), the total loan balance of those borrowers who have not made at least a 1 dollar reduction in their principal balance in the 3 consecutive fiscal years since their loans entered repayment, deferment, or forbearance. (ii) Exception The cohort nonrepayment loan balance calculation under clause (i) shall not take into consideration a borrower who was\u2014 (I) in deferment on repayment of a loan described in subparagraph (A) in the 3 consecutive fiscal years described in clause (i) due to study in an approved graduate fellowship program or in an approved rehabilitation training program for the disabled; (II) in deferment on repayment of a loan described in subparagraph (A) in the 3 consecutive fiscal years described in clause (i) during which time the borrower was in a period of at least half-time enrollment in college or a career school; (III) in deferment on repayment of a loan described in subparagraph (A) in the 3 consecutive fiscal years described in clause (i) during which time the borrower was in a period of service qualifying for loan discharge or cancellation under part E; (IV) in deferment on repayment of a loan described in subparagraph (A) in the 3 consecutive fiscal years described in clause (i) during which time the borrower was on active duty military service during a war, military operation, or national emergency; (V) in mandatory forbearance on repayment of a loan described in subparagraph (A) for the full fiscal year; or (VI) serving as a volunteer under the Peace Corps Act ( 22 U.S.C. 2501 et seq. ) or the Domestic Volunteer Service Act of 1973 ( 42 U.S.C. 4950 et seq. ), during the 3 consecutive fiscal years described in clause (i). (C) Determination of payment (i) In general (I) In general Except as provided in subclause (II), the risk-sharing payment of an institution for a fiscal year equals 2 percent of the amount determined under clause (ii). (II) Cap The risk-sharing payment of an institution for a fiscal year shall not be more than 2.5 percent of the amount equal to the institution's total annual revenues and investment returns less auxiliary enterprise revenues and hospital revenues, as defined in the IPEDS Finance Survey, for the most recent fiscal year upon which the institution\u2019s audited financial reports are available. (ii) Amount based on cohort nonrepayment loan balance and unemployment rate (I) In general The amount under this clause is determined by subtracting the amount determined under subclause (II) from the cohort nonrepayment loan balance determined under subparagraph (B). (II) Amount based on unemployment rate The amount under this subclause is determined by multiplying the average national unemployment rate, as defined by the Bureau of Labor Statistics, for the 3 previous fiscal years from the date of the determination by the cohort loan balance determined under subparagraph (A). (3) Notification Beginning with the first fiscal year for which data are available after the date of enactment of the Student Protection and Success Act and each succeeding fiscal year until fiscal year 2028, the Secretary shall notify each institution of higher education participating in the direct student loan program under this part of what the risk-sharing payment based on the cohort nonrepayment loan balance of the institution, as determined under paragraph (2), would be for such institution if such provision were in effect. .\n#### 5. Report\nNot later than 6 months after the date of enactment of the Student Protection and Success Act , the Secretary of Education shall submit to Congress a report\u2014\n**(1)**\non best practices for institutions of higher education to improve repayment rates; and\n**(2)**\nthat makes recommendations on how institutions of higher education can improve repayment rates, with a particular emphasis on institutions that serve a high proportion of low-income students.\n#### 6. Student service expenditures and resources\nSection 153(a)(1)(I) of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9543(a)(1)(I) ) is amended to read as follows:\n(I) the financing and management of education, including data on revenues and expenditures, and information regarding\u2014 (i) student service expenditures, that\u2014 (I) includes instruction, information technology, and other activities whose primary purpose is to contribute to students\u2019 emotional and physical well-being and to their intellectual, cultural, and social development inside and outside the context of the formal instructional program; and (II) does not include expenditures on marketing, recruitment, or intercollegiate athletic programs; (ii) student service resources, which is a measure of an institution\u2019s resources that could reasonably be allocated towards student service expenditures, including net tuition revenues, State and local appropriations, endowment income, and revenues related to student housing and food services less expenditures on student housing, food services, and the operations and maintenance of a plant; and (iii) recruitment and marketing expenditures; .",
      "versionDate": "2026-03-19",
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
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4114",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Student Protection and Success Act",
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
        "name": "Education",
        "updateDate": "2026-04-06T13:16:47Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8009ih.xml"
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
      "title": "Student Protection and Success Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Student Protection and Success Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to provide for institutional ineligibility based on low cohort repayment rates and to require risk-sharing payments of institutions of higher education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:23Z"
    }
  ]
}
```
