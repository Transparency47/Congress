# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1827?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1827
- Title: Child Care Availability and Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 1827
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-05-01T08:08:25Z
- Update date including text: 2026-05-01T08:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1827",
    "number": "1827",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Child Care Availability and Affordability Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:25Z",
    "updateDateIncludingText": "2026-05-01T08:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:00:30Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "KS"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "OH"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "IA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "WA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "PA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "OH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "VA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "OR"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "CA"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NC"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "VA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NH"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1827ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1827\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Carbajal (for himself, Mr. Lawler , Ms. Davids of Kansas , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the employer-provided child care credit and the dependent care assistance exclusion.\n#### 1. Short title\nThis Act may be cited as the Child Care Availability and Affordability Act .\n#### 2. Expansion of employer-provided child care credit\n##### (a) Increase of amount of qualified child care expenditures taken into account\nSection 45F(a)(1) of the Internal Revenue Code of 1986 is amended by striking 25 percent and inserting 50 percent .\n##### (b) Increase of maximum credit amount\nSection 45F(b) of the Internal Revenue Code of 1986 is amended by striking $150,000 and inserting $500,000 .\n##### (c) Treatment of jointly owned or operated childcare facility\nSection 45F(c)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Jointly owned or operated childcare facility For purposes of subparagraph (A)(i)(I), a facility shall not fail to be treated as a qualified childcare facility of the taxpayer merely because such facility is jointly owned or operated by the taxpayer and other persons. .\n##### (d) Special rule for small businesses\nSection 45F(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Small businesses (A) In general In the case of a taxpayer described in subparagraph (B)\u2014 (i) subsection (a)(1) shall be applied by substituting 60 percent for 50 percent , and (ii) subsection (b) shall be applied by substituting $600,000 for $500,000 . (B) Taxpayer described A taxpayer described in this subparagraph is a taxpayer that meets the gross receipts test of section 448(c), determined\u2014 (i) by substituting 5-taxable-year for 3-taxable-year in paragraph (1) thereof, and (ii) by substituting 5-year for 3-year each place such term appears in paragraph (3)(A) thereof. .\n##### (e) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this section.\n#### 3. Increase in amount excludable for dependent care assistance programs\n##### (a) In general\nSection 129(a)(2)(A) of the Internal Revenue Code of 1986 is amended by striking $5,000 ($2,500 and inserting $7,500 ($3,750 .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid or incurred after the date of the enactment of this section.\n#### 4. Household and dependent care credit increased and made refundable\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amending by inserting after section 36B the following new section:\n36C. Expenses for household and dependent care services necessary for gainful employment (a) Allowance of credit (1) In general In the case of an individual for which there are 1 or more qualifying individuals with respect to such individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the applicable percentage of the employment-related expenses paid by such individual during the taxable year. (2) Applicable percentage defined For purposes of paragraph (1), the term applicable percentage means 50 percent\u2014 (A) reduced (but not below 35 percent) by 1 percentage point for each $2,000 (or fraction thereof) by which the taxpayer\u2019s adjusted gross income for the taxable year exceeds $15,000, and (B) further reduced (but not below zero) by 1 percentage point for each $2,000 (or fraction thereof) by which the taxpayer\u2019s adjusted gross income for the taxable year exceeds $150,000. (b) Definitions of qualifying individual and employment-Related expenses For purposes of this section\u2014 (1) Qualifying individual The term qualifying individual means\u2014 (A) a dependent of the taxpayer (as defined in section 152(a)(1)) who has not attained age 13, (B) a dependent of the taxpayer (as defined in section 152, determined without regard to subsections (b)(1), (b)(2), and (d)(1)(B)) who is physically or mentally incapable of caring for himself or herself and who has the same principal place of abode as the taxpayer for more than one-half of such taxable year, or (C) the spouse of the taxpayer, if the spouse is physically or mentally incapable of caring for himself or herself and who has the same principal place of abode as the taxpayer for more than one-half of such taxable year. (2) Employment-related expenses (A) In general The term employment-related expenses means amounts paid for the following expenses, but only if such expenses are incurred to enable the taxpayer to be gainfully employed for any period for which there are 1 or more qualifying individuals with respect to the taxpayer: (i) Expenses for household services. (ii) Expenses for the care of a qualifying individual. Such term shall not include any amount paid for services outside the taxpayer\u2019s household at a camp where the qualifying individual stays overnight. (B) Exception Employment-related expenses described in subparagraph (A) which are incurred for services outside the taxpayer\u2019s household shall be taken into account only if incurred for the care of\u2014 (i) a qualifying individual described in paragraph (1)(A), or (ii) a qualifying individual (not described in paragraph (1)(A)) who regularly spends at least 8 hours each day in the taxpayer\u2019s household. (C) Dependent care centers Employment-related expenses described in subparagraph (A) which are incurred for services provided outside the taxpayer\u2019s household by a dependent care center (as defined in subparagraph (D)) shall be taken into account only if\u2014 (i) such center complies with all applicable laws and regulations of a State or unit of local government, and (ii) the requirements of subparagraph (B) are met. (D) Dependent care center defined For purposes of this paragraph, the term dependent care center means any facility which\u2014 (i) provides care for more than 6 individuals (other than individuals who reside at the facility), and (ii) receives a fee, payment, or grant for providing services for any of the individuals (regardless of whether such facility is operated for profit). (c) Dollar limit on amount creditable The amount of the employment-related expenses incurred during any taxable year which may be taken into account under subsection (a) shall not exceed\u2014 (1) $5,000 if there is 1 qualifying individual with respect to the taxpayer for such taxable year, or (2) $8,000 if there are 2 or more qualifying individuals with respect to the taxpayer for such taxable year. (d) Earned income limitation (1) In general Except as otherwise provided in this subsection, the amount of the employment-related expenses incurred during any taxable year which may be taken into account under subsection (a) shall not exceed\u2014 (A) in the case of an individual who is not married at the close of such year, such individual\u2019s earned income for such year, or (B) in the case of an individual who is married at the close of such year, the lesser of such individual\u2019s earned income or the earned income of his spouse for such year. (2) Special rule for spouse who is a student or incapable of caring for self In the case of a spouse who is a student or a qualifying individual described in subsection (b)(1)(C), for purposes of paragraph (1), such spouse shall be deemed for each month during which such spouse is a full-time student at an educational institution, or is such a qualifying individual, to be gainfully employed and to have earned income of not less than\u2014 (A) $250 if subsection (c)(1) applies for the taxable year, or (B) $500 if subsection (c)(2) applies for the taxable year. (e) Special rules For purposes of this section\u2014 (1) Place of abode An individual shall not be treated as having the same principal place of abode of the taxpayer if at any time during the taxable year of the taxpayer the relationship between the individual and the taxpayer is in violation of local law. (2) Married couples must file joint return If the taxpayer is married at the close of the taxable year, the credit shall be allowed under subsection (a) only if the taxpayer and the taxpayer's spouse file a joint return for the taxable year. (3) Marital status An individual legally separated from the individual's spouse under a decree of divorce or of separate maintenance shall not be considered as married. (4) Certain married individuals living apart If\u2014 (A) an individual who is married and who files a separate return\u2014 (i) maintains as the individual's home a household which constitutes for more than 1/2 of the taxable year the principal place of abode of a qualifying individual, and (ii) furnishes over half of the cost of maintaining such household during the taxable year, and (B) during the last 6 months of such taxable year such individual\u2019s spouse is not a member of such household, such individual shall not be considered as married. (5) Special dependency test in case of divorced parents, etc If\u2014 (A) section 152(e) applies to any child with respect to any calendar year, and (B) such child is under the age of 13 or is physically or mentally incapable of caring for himself or herself, in the case of any taxable year beginning in such calendar year, such child shall be treated as a qualifying individual described in subparagraph (A) or (B) of subsection (b)(1) (whichever is appropriate) with respect to the custodial parent (as defined in section 152(e)(4)(A)), and shall not be treated as a qualifying individual with respect to the noncustodial parent. (6) Payments to related individuals No credit shall be allowed under subsection (a) for any amount paid by the taxpayer to an individual\u2014 (A) with respect to whom, for the taxable year, a deduction under section 151(c) (relating to deduction for personal exemptions for dependents) is allowable either to the taxpayer or the taxpayer's spouse, or (B) who is a child of the taxpayer (within the meaning of section 152(f)(1)) who has not attained the age of 19 at the close of the taxable year. For purposes of this paragraph, the term taxable year means the taxable year of the taxpayer in which the service is performed. (7) Student The term student means an individual who during each of 5 calendar months during the taxable year is a full-time student at an educational organization. (8) Educational organization The term educational organization means an educational organization described in section 170(b)(1)(A)(ii). (9) Identifying information required with respect to service provider No credit shall be allowed under subsection (a) for any amount paid to any person unless\u2014 (A) the name, address, and taxpayer identification number of such person are included on the return claiming the credit, or (B) if such person is an organization described in section 501(c)(3) and exempt from tax under section 501(a), the name and address of such person are included on the return claiming the credit. In the case of a failure to provide the information required under the preceding sentence, the preceding sentence shall not apply if it is shown that the taxpayer exercised due diligence in attempting to provide the information so required. (10) Identifying information required with respect to qualifying individuals No credit shall be allowed under this section with respect to any qualifying individual unless the TIN of such individual is included on the return claiming the credit. (f) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Conforming amendments\n**(1)**\nSection 1324(b) of title 31 is amended by inserting 36C, after 36B, .\n**(2)**\nSection 21 of the Internal Revenue Code of 1986 is repealed.\n**(3)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by striking the item relating to section 21.\n**(4)**\nSection 6211(b)(4)(A) of such Code is amended by striking 21 by reason of subsection (g) thereof, .\n**(5)**\nSection 6213(g)(2) of such Code is amended\u2014\n**(A)**\nin subparagraph (H), by striking section 21 and inserting section 36C , and\n**(B)**\nin subparagraph (L)\u2014\n**(i)**\nby striking 21, , and\n**(ii)**\nby inserting 36C, after 32, .\n**(6)**\nThe following sections of such Code are each amended by striking section 21(e) and inserting section 36C(e) .\n**(A)**\nSection 23(f)(1).\n**(B)**\nSection 35(g)(6).\n**(C)**\nSection 129(a)(2)(C).\n**(7)**\nSection 129 of such Code is further amended\u2014\n**(A)**\nin subsection (b)(2), by striking section 21(d)(2) and inserting section 36C(d)(2) , and\n**(B)**\nin subsection (e)(1), by striking section 21(b)(2) and inserting section 36C(b)(2) .\n**(8)**\nSection 213(e) of such Code is amended by striking section 21 and inserting section 36C .\n##### (c) Clerical amendment\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Expenses for household and dependent care services necessary for gainful employment. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this section.",
      "versionDate": "2025-03-04",
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
        "actionDate": "2025-03-04",
        "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S1499-1500)"
      },
      "number": "847",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Child Care Availability and Affordability Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T18:27:03Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1827ih.xml"
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
      "title": "Child Care Availability and Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:00Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Child Care Availability and Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the employer-provided child care credit and the dependent care assistance exclusion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:21Z"
    }
  ]
}
```
