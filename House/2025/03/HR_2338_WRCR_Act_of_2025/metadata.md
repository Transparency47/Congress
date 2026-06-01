# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2338
- Title: WRCR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2338
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-03-25T08:05:43Z
- Update date including text: 2026-03-25T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2338",
    "number": "2338",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "WRCR Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-25T08:05:43Z",
    "updateDateIncludingText": "2026-03-25T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:03:00Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "WI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "MN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "RI"
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
      "sponsorshipDate": "2026-03-24",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2338ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2338\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Ms. Moore of Wisconsin (for herself, Ms. Chu , Mr. Davis of Illinois , Mr. Gomez , Ms. Pingree , Ms. Norton , Ms. Tlaib , Ms. Scanlon , Mr. Khanna , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand and improve the earned income tax credit.\n#### 1. Short title\nThis Act may be cited as the Worker Relief and Credit Reform Act of 2025 or as the WRCR Act of 2025 .\n#### 2. Expansion and improvement of earned income tax credit\n##### (a) Application to students\n**(1) In general**\nSection 32(c)(1)(A)(i) of the Internal Revenue Code of 1986 is amended by inserting who is a qualifying student or after any individual .\n**(2) Qualifying student**\nSection 32(c) of such Code is amended by redesignating paragraph (4) as paragraph (5) and inserting after paragraph (3) the following new paragraph:\n(4) Qualifying student (A) In general The term qualifying student means, with respect to any taxable year, any individual who\u2014 (i) is an eligible student (as defined in section 25A(b)(3)) with respect to at least one academic period beginning during such taxable year, (ii) either\u2014 (I) qualifies for a Federal Pell Grant with respect to such academic period, or (II) meets the requirements of subparagraph (B) or (C) for the taxable year, and (iii) is not a dependent for whom a deduction is allowable under section 151 to another taxpayer for any taxable year beginning in the same calendar year as such taxable year. (B) Independent students In the case of any independent student, the requirements of this subparagraph are met for such taxable year if the household income of the taxpayer is less than 300 percent of the poverty line for the size of the family involved for the taxable year. (C) Other students (i) In general In the case of any individual who is not an independent student, the requirements of this subparagraph are met for such taxable year if the aggregate household incomes of all the individual\u2019s specified supporters (and the taxpayer if not otherwise taken into account) for the taxable years of such supporters which end in or with the calendar year in which such individual\u2019s taxable year begins is less than 300 percent of the poverty line for the size of the family involved (determined on a single aggregate basis) for the taxable year. (ii) Specified supporter The term specified supporter means, with respect to any individual described in clause (i), any taxpayer with respect to whom such individual was a dependent for any taxable year ending in the 3-year period described in subparagraph (D)(i). (D) Independent student defined (i) In general The term independent student means any individual if such individual was not a dependent of another taxpayer for any taxable year ending in the 3-year period which ends on the first day of the first academic period with respect to which such individual is an eligible student (as defined in section 25A(b)(3)). (ii) Certain academic periods disregarded An academic period shall be disregarded under clause (i) if such academic period ends more than 2 years before the beginning of the next academic period with respect to which the individual is an eligible student (as defined in section 25A(b)(3)). (E) Other definitions (i) Household income The term household income has the meaning given such term in section 36B(d)(2). (ii) Poverty line The term poverty line has the meaning given such term in section 36B(d)(3)(A). (iii) Family size The family size involved with respect to any taxpayer shall be determined under rules similar to the rules of section 36B(d)(1). .\n**(3) Conforming amendment**\nSection 32(c)(1)(A)(ii) of such Code is amended by striking any other individual who does not have a qualifying child and inserting any individual not described in clause (i) .\n##### (b) Modification of age requirements\nSection 32(c)(1)(A)(ii)(II) of such Code is amended by striking has attained age 25 but not attained age 65 and inserting has attained age 18 .\n##### (c) Care-Giving and learning taken into account as compensated work\nSection 32(a) of such Code is amended by adding at the end the following new paragraph:\n(3) Special rule for qualifying students and certain individuals with one or more qualifying dependents For purposes of paragraph (1), any individual\u2014 (A) who is a qualifying student, or (B) who has a qualifying dependent, shall be treated as having earned income for the taxable year which is equal to the earned income amount with respect to such individual for such taxable year. .\n##### (d) Treatment of certain qualifying relatives\n**(1) In general**\nSection 32(c)(3) of such Code is amended by striking all that precedes subparagraph (B) and inserting the following:\n(3) Qualifying dependent (A) In general The term qualifying dependent means\u2014 (i) a qualifying child of the taxpayer, as defined in section 152(c), determined\u2014 (I) by substituting 12 for 19 in paragraph (3)(A)(i) thereof, and (II) without regard to paragraphs (1)(D) and (3)(A)(ii) thereof and section 152(e), (ii) any individual who is physically or mentally incapable of caring for himself or herself (within the meaning of section 21(b)(1)) and who\u2014 (I) is the taxpayer\u2019s spouse, or (II) is a qualifying relative of the taxpayer, as defined in section 152(d), determined without regard to paragraph (1)(B) thereof and by treating an individual as a qualifying child of the taxpayer for purposes of paragraph (1)(D) thereof only if such individual is a qualifying child of the taxpayer as determined under clause (i) of this subparagraph, or (iii) any qualifying relative of the taxpayer (as defined in section 152(d), determined without regard to paragraph (1)(B) thereof) who has attained age 65 as of the close of the calendar year in which the taxable year of the taxpayer begins. For purposes of determining if any individual is a qualifying relative of the taxpayer under clause (ii)(II) or (iii), section 152(d)(1)(C) shall be applied by not taking into account any benefits received by such individual pursuant to any Federal program (or any State or local program financed in whole or in part with Federal funds) related to retirement (including social security benefits), disability, health care, cash aid, child care, food assistance, housing and development, social services, employment and training, or energy assistance. .\n**(2) Conforming amendments**\n**(A)**\nSection 32(c)(1)(A)(i) of such Code is amended by striking qualifying child and inserting qualifying dependent .\n**(B)**\nSection 32(c)(1)(B) of such Code is amended\u2014\n**(i)**\nby striking qualifying child and inserting qualifying dependent , and\n**(ii)**\nby striking child in the heading and inserting dependent .\n**(C)**\nSection 32(c)(3)(D)(i) of such Code is amended by striking qualifying child both places it appears and inserting qualifying dependent .\n##### (e) Modification of percentages and amounts\n**(1) 100 percent credit percentage**\nParagraph (1) and paragraph (2)(A) of section 32(a) of such Code are each amended by striking the credit percentage of .\n**(2) 20 percent phaseout percentage**\nSection 32(a)(2)(B) of such Code is amended by striking the phaseout percentage and inserting 20 percent .\n**(3) Modification of earned income and phaseout amounts**\nSection 32(b) of such Code is amended to read as follows:\n(b) Earned income amount; phaseout amount For purposes of this section\u2014 (1) Earned income amount The term earned income amount means $4,000 (twice such amount in the case of a joint return). (2) Phaseout amount The term phaseout amount means $30,000 ($50,000 in the case of a joint return). (3) Inflation adjustment In the case of any taxable year beginning after 2025, the $4,000 amount in paragraph (1) and each dollar amount in paragraph (2) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2024 for 2016 in subparagraph (A)(ii) thereof. If any increase under the preceding sentence is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. .\n**(4) Conforming amendments**\n**(A)**\nSection 32(i) of such Code is amended by adding at the end the following new paragraph:\n(3) Inflation adjustment (A) In general In the case of any taxable year beginning after 2021, the $10,000 amount in subsection (i)(1) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2020 for 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under subparagraph (A) is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. .\n**(B)**\nSection 32 of such Code is amended by striking subsection (j).\n##### (f) Increased credit for certain unmarried individuals with 2 or more qualifying children\n**(1) In general**\nSection 32 of such Code is amended by inserting after subsection (f) the following new subsection:\n(g) Increased credit for certain unmarried individuals with 2 or more qualifying children (1) In general In the case of a qualified individual, the amount of the credit otherwise determined under subsection (a) shall be increased by the amount of the credit determined under this section as such section was in effect for taxable years beginning in 2018 but with the modifications described in paragraph (2). (2) Modifications Solely for purposes of determining the increase under paragraph (1)\u2014 (A) Credit percentage The credit percentage shall be equal to\u2014 (i) in the case of a qualified individual with 2 qualifying children, 12.5 percent, and (ii) in the case of a qualified individual with 3 or more qualifying children, 18.75 percent. (B) Phaseout percentage The phaseout percentage shall be equal to 5 percent. (C) Application of inflation adjustment Section 32(j) as in effect for taxable years beginning in 2018 shall be applied by taking into account the taxable year for which the increase under paragraph (1) is determined. (3) Qualified individual For purposes of this subsection, the term qualified individual means any individual who\u2014 (A) is not married (as determined under section 7703), and (B) has 2 or more qualifying children. (4) Qualifying child For purposes of this subsection, the term qualifying child means a child described in subsection (c)(3)(A)(i) determined without regard to subclause (I) thereof. .\n##### (g) Advance payment\n**(1) In general**\nChapter 77 of such Code is amended by adding at the end the following new section:\n7531. Advance payment of earned income credit; earned income savings accounts (a) In general Not later than the date that is 2 years after the date of the enactment of this section, the Secretary shall establish a program for making direct advance monthly payments of the credit allowable under section 32 to taxpayers who elect to receive such payments. (b) Limitation The aggregate monthly payments made under subsection (a) with respect to any taxpayer for any taxable year shall not exceed 75 percent of the estimated amount of the credit allowable under section 32 to such taxpayer for such taxable year. (c) Election The election under subsection (a) may be made or changed for subsequent periods at any time during the taxable year. In the case of an election made after the beginning of a taxable year, the monthly advance payments shall be made for months beginning after the date that such election becomes effective and the total amount of advance payments (subject to the limitation of subsection (b)) shall be prorated among the remaining months. (d) Method of payment The program established under subsection (a) shall include an option for taxpayers to elect to receive payments under such program by prepaid debit card. (e) Reports to taxpayers (1) In general With respect to payments made under this section for any calendar year, not later than January 31 of the following calendar year, the Secretary shall issue a statement to each individual with respect to whom payments were made under this section setting forth\u2014 (A) the name, address, and TIN of such person, (B) the aggregate amount of payments made under this section with respect to such person for such calendar year, (C) a statement that such individual is required to file a return of tax with respect to taxable years which include any portion of such calendar year regardless of whether such individual has income tax liability with respect to such taxable years, and (D) such other information as the Secretary may provide. (2) Election to receive statement through on-line portal A taxpayer may elect to receive the statement described in paragraph (1) through the on-line portal described in subsection (f). (f) Recapture of excess payments If the aggregate payments made to any taxpayer under subsection (a) with respect to any taxable year exceed the credit allowable under section 32 (determined without regard to subsection (h) thereof) with respect to such taxpayer for such taxable year, the tax imposed by chapter 1 with respect to such taxpayer for such taxable year shall be increased by such excess. (g) Restriction on allowance of advance payment if excess payments not repaid In the case of a taxpayer who fails to pay any tax liability which includes an increase determined under subsection (f) before the date on which payment of such tax is due, no payment shall be made under subsection (a) to such taxpayer during the period beginning on such date and ending with the end of the 2-year period which begins on the date that such tax liability (and any interest or penalties in connection with such liability) has been paid in full. .\n**(2) Coordination with credit**\nSection 32 of such Code, as amended by subsection (f), is amended by inserting after subsection (g) the following new subsection:\n(h) Coordination with advance payment of credit With respect to any taxable year, the amount which would (but for this subsection) be allowed as a credit to the taxpayer under this section shall be reduced (but not below zero) by the aggregate payments made under section 7531 to such taxpayer for such taxable year. .\n**(3) One-on-one consultations**\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall ensure that in-person, telephonic, and virtual one-on-one consultations between taxpayers and the Internal Revenue Service are available to assist taxpayers at all times during regular business hours (and, in the case of in-person consultations, at all taxpayer assistance centers of the Internal Revenue Service) in determining\u2014\n**(A)**\ntheir eligibility for the advance payment program established under section 7531,\n**(B)**\nthe amount of the monthly payment for which the taxpayer is eligible under such program,\n**(C)**\nthe circumstances or changes in circumstances which, based on the particular characteristics of such taxpayer, are most likely to result in excess payments to such taxpayer which would be subject to recapture under section 7531(f), and\n**(D)**\nsuch other matters as such Secretary or delegate determines appropriate.\n**(4) On-line portal**\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall establish an on-line portal which allows taxpayers to\u2014\n**(A)**\nelect to receive advance monthly payments under section 7531, including determining the estimated amount described in subsection (b) of such section and determining the amount of such monthly payments,\n**(B)**\nreport changes in circumstances and modify the amount of future advance monthly payments under such section, and\n**(C)**\nstop future advance monthly payments under such section and pay back any advance monthly payments.\n**(5) Clerical amendment**\nThe table of sections for chapter 77 of such Code is amended by adding at the end the following new item:\nSec. 7531. Advance payment of earned income credit; earned income savings accounts. .\n##### (h) Outreach pilot program\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary\u2019s designee) shall establish a program to educate taxpayers regarding the availability of the earned income tax credit and the advance monthly payments of such credit. Pursuant to such program\u2014\n**(A) EITC educational letters**\nThe Secretary (or designee) shall provide a written notice describing the earned income tax credit, the qualifications for receiving such credit, and the program for the advance payment of such credit to each taxpayer that the Secretary (or designee) determines is likely to qualify for such credit.\n**(B) District office workshops**\nEach district office of the Internal Revenue Service shall provide workshops and seminars to assist and educate taxpayers regarding the earned income tax credit and the program to provide advance monthly payments of such credit.\n**(C) Quarterly reminders**\nThe Internal Revenue Service shall provide written reminders each calendar quarter to taxpayers participating in the program to provide advance monthly payments of the earned income tax credit that the amount of such payments are determined on the basis of estimates based on information previously provided by the taxpayer, that the taxpayer is responsible for repaying any amounts received that are in excess of the actual amount of the earned income tax credit, and that the taxpayer should review all the facts and circumstances that may affect the amount of the earned income tax credit of the taxpayer which the taxpayer is receiving in advance.\n**(2) Termination**\nThe program established under paragraph (1) shall terminate at the close of the 10-year period beginning on the date that such program is established by the Secretary (or designee).\n**(3) Report on effectiveness of program**\nOn the date which is 5 years after the establishment of the program under paragraph (1), the Secretary shall submit to Congress a report evaluating the effectiveness of the program, including a detailed examination of the effectiveness of each of the initiatives described in subparagraphs (A), (B), and (C) of paragraph (1).\n##### (i) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-03-25",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T13:24:54Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2338ih.xml"
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
      "title": "WRCR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WRCR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Worker Relief and Credit Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand and improve the earned income tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:28Z"
    }
  ]
}
```
