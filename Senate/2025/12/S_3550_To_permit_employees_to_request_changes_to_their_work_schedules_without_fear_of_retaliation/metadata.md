# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3550?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3550
- Title: Schedules That Work Act
- Congress: 119
- Bill type: S
- Bill number: 3550
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-21T16:34:11Z
- Update date including text: 2026-01-21T16:34:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3550",
    "number": "3550",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Schedules That Work Act",
    "type": "S",
    "updateDate": "2026-01-21T16:34:11Z",
    "updateDateIncludingText": "2026-01-21T16:34:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T22:15:49Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3550is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3550\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Ms. Warren (for herself, Mr. Blumenthal , Mr. Van Hollen , Ms. Baldwin , Mr. Durbin , Mr. Reed , Mr. Booker , Mr. Markey , Mr. Sanders , Mr. Whitehouse , Mr. Murphy , Ms. Klobuchar , Ms. Duckworth , Mr. Welch , Mr. Schumer , Ms. Hirono , Mr. Merkley , Mr. Wyden , Mrs. Murray , Mr. Padilla , and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo permit employees to request changes to their work schedules without fear of retaliation and to ensure that employers consider these requests, and to require employers to provide more predictable and stable schedules for employees in certain occupations with evidence of unpredictable and unstable scheduling practices that negatively affect employees, and for other purposes.\n#### 1. Short title; findings\n##### (a) Short title\nThis Act may be cited as the Schedules That Work Act .\n##### (b) Findings\nCongress finds the following:\n**(1)**\nThe vast majority of the United States workforce today is juggling responsibilities at home and at work. In families with children, 45 percent of mothers are primary breadwinners and 25 percent are co-breadwinners.\n**(2)**\nDespite the dual responsibilities of today's workforce, many workers have little notice of their work schedules and lack the ability to make changes to the work hours in such schedules, which undermines their ability to accommodate family responsibilities.\n**(3)**\n**(A)**\nMothers working in low-paid jobs are more likely to be the primary or sole breadwinner for their families than mothers working in higher-paid jobs. For example, almost 90 percent mothers in the 1/5 of households in the United States with the lowest incomes bring home all or most of their families\u2019 income, which is almost 3 times higher when compared to counterparts in the highest-income quintile.\n**(B)**\nAt the same time, low-paid workers often have the least control over their work hours and face the most unpredictable schedules. In some industries, just-in-time scheduling practices, which base workers' schedules on perceived consumer demand to minimize labor costs, are particularly common. Employers using these practices often post work schedules with little notice, vary work hours widely from week to week, cancel shifts at the last minute, and schedule employees for on call shifts (requiring an employee to call in to work to find out whether the employee will have to work later that day) or clopening shifts (requiring an employee to work a closing shift at night followed by an opening shift a few hours later). For example, national survey data show that\u2014\n**(i)**\nabout 2/3 of hourly retail and food service workers receive their work schedules with less than 2 weeks\u2019 advance notice and about 1/3 receive their schedule with less than 1 week\u2019s notice;\n**(ii)**\nmore than 1 in 5 hourly retail and food service workers have been scheduled for on-call shifts, and more than 1 in 3 have worked clopening shifts; and\n**(iii)**\n65 percent of hourly retail and food service workers would like a more stable and predictable schedule.\n**(4)**\nUnfair work scheduling practices make it difficult for low-paid workers to\u2014\n**(A)**\nprovide necessary care for children and other family members, including securing and maintaining stable child care;\n**(B)**\naccess and receive needed care for the workers\u2019 own serious health conditions;\n**(C)**\npursue workforce training;\n**(D)**\nget or keep a second job, which many workers need to make ends meet;\n**(E)**\nplan for and access transportation to reach worksites; and\n**(F)**\nqualify for and maintain eligibility for needed public benefits and work supports, such as child care subsidies, Medicaid, and benefits under the supplemental nutrition assistance program, due to fluctuations in income and work hours.\n**(5)**\nA growing body of research demonstrates that unstable and unpredictable work schedules have significant detrimental impacts on sleep quality, mental health, and happiness, and are associated with unstable child care arrangements and negative health and behavioral outcomes for children. And impacts are likely to be the most severe for workers of color and their families, as workers of color are more likely than their White counterparts\u2014even compared to White coworkers at the same company\u2014to experience unstable work schedules. Unstable and unpredictable work schedules are also associated with higher rates of turnover, which creates further instability for employers and workers. Some examples of the detrimental impacts of unstable and unpredictable work schedules are as follows:\n**(A)**\nUnstable work schedules lead to more household economic strain and time conflicts and undermine the well-being of parents, all of which can negatively impact children\u2019s health and behavior.\n**(B)**\nWorkers with the most severe instability in their work schedules also face the highest risk of negative behavior and health outcomes for their children.\n**(C)**\nThe exposure of a parent to on-call shifts and last-minute shift changes are associated with more unstable child care arrangements and with the use of siblings to provide care.\n**(D)**\nWork schedule instability causes more work-family conflict, which increases the chance that a worker will be forced to leave his or her job, and is associated with downward mobility of the earnings of the worker.\n**(E)**\n**(i)**\nRelative to White workers, workers of color are more likely to\u2014\n**(I)**\nhave cancelled shifts;\n**(II)**\nhave on-call shifts;\n**(III)**\nbe involuntary part-time workers;\n**(IV)**\nhave trouble getting time off; and\n**(V)**\nwork clopening shifts, as described in paragraph (3)(B).\n**(ii)**\nThe statistics described in clause (i) remain true after controlling for demographics, human capital, worker power, firm segregation, and discordance with the race or ethnicity of the worker and the manager. Race gaps in job quality are greater for women of color.\n**(F)**\nWorkers who receive shorter advance notice, who work on-call shifts, who experience last-minute shift cancellation and timing changes, or who have more volatile work hours are more likely to experience hunger, housing insecurity, and greater overall economic hardship.\n**(6)**\nUnpredictable and unstable work schedules are common in a wide range of occupations, with evidence of particular concentration in food service, retail, cleaning, hospitality, and warehouse occupations. These occupations are critically important to the United States economy.\n**(7)**\nSince 2015, ten municipalities in the United States and the State of Oregon have enacted laws requiring employers to implement fair scheduling practices. Research from 3 municipalities affirms that workers in jobs covered by these laws report significantly better outcomes than their peers in uncovered positions, including more predictable schedules and compensation for employer-driven schedule changes. Survey research also indicates that covered workers experience improvements in well-being and financial security.\n**(8)**\nScheduling practices that benefit employees can benefit employers, too. Relative to their peers with lower-quality schedules, workers with more input, stability, and predictability in their work hours report greater job satisfaction and less work family-conflict, which can also improve productivity and reduce turnover. For example, a randomized experiment demonstrated that improving schedule stability and predictability for hourly employees at Gap Inc. stores increased store productivity and sales.\n**(9)**\nThis Act is a first step in responding to the needs of workers for a voice in the timing of their work hours and for more predictable schedules.\n#### 2. Definitions\nIn this Act:\n**(1) Bona fide business reason**\nThe term bona fide business reason means\u2014\n**(A)**\nthe identifiable burden of additional costs to an employer, including the cost of productivity loss, retraining or hiring employees, or transferring employees from one facility to another facility;\n**(B)**\na significant detrimental effect on the employer\u2019s ability to meet organizational needs or customer demand;\n**(C)**\na significant inability of the employer, despite best efforts, to reorganize work among existing (as of the date of the reorganization) staff;\n**(D)**\na significant detrimental effect on business performance;\n**(E)**\ninsufficiency of work during the periods an employee proposes to work;\n**(F)**\nthe need to balance competing scheduling requests when it is not possible to grant all such requests without a significant detrimental effect on the employer\u2019s ability to meet organizational needs; or\n**(G)**\nsuch other reason as may be specified by the Secretary of Labor (or, as applicable, the corresponding administrative officer specified in section 7(e)).\n**(2) Career-related educational or training program**\nThe term career-related educational or training program means an educational or training program or program of study offered by a public, private, or nonprofit career and technical education school, institution of higher education, or other entity that provides academic education, career and technical education, or training (including remedial education or English as a second language, as appropriate), that is a program that leads to a recognized postsecondary credential (as identified under section 122(d) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3152(d) ), and provides career awareness information. The term includes a program allowable under the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3101 et seq. ), the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2301 et seq. ), or the Higher Education Act of 1965 ( 20 U.S.C. 1001 et seq. ), without regard to whether or not the program is funded under the corresponding Act.\n**(3) Caregiver**\nThe term caregiver means an individual with the status of being a significant provider of\u2014\n**(A)**\nongoing care or education, including responsibility for securing the ongoing care or education, of a child; or\n**(B)**\nongoing care, including responsibility for securing the ongoing care, of\u2014\n**(i)**\na person with a serious health condition who is in a family relationship with the individual; or\n**(ii)**\na parent of the individual, who is age 65 or older.\n**(4) Child**\nThe term child means, regardless of age, a biological, adopted, or foster child, a stepchild, a child of a domestic partner, a legal ward, or a child of a person standing in loco parentis to that child.\n**(5) Commerce terms**\nThe terms commerce and industry or activity affecting commerce have the meanings given the terms in section 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 ).\n**(6) Covered employer**\n**(A) In general**\nThe term covered employer \u2014\n**(i)**\nmeans any person engaged in commerce or in any industry or activity affecting commerce who employs 15 or more employees (described in paragraph (10)(A));\n**(ii)**\nincludes any person who acts, directly or indirectly, in the interest of such an employer to any of the employees (described in paragraph (10)(A)) of such employer;\n**(iii)**\nincludes any successor in interest of such an employer; and\n**(iv)**\nincludes an agency described in subparagraph (A)(iii) of section 101(4) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611(4) ), to which subparagraph (B) of such section shall apply.\n**(B) Rule**\nFor purposes of determining the number of employees who work for a person described in subparagraph (A)(i), all employees (described in paragraph (10)(A)) performing work for compensation on a full-time, part-time, or temporary basis shall be counted, except that if the number of such employees who perform work for such a person for compensation fluctuates, the number may be determined for a calendar year based upon the average number of such employees who performed work for the person for compensation during the preceding calendar year.\n**(C) Person**\nIn this paragraph, the term person has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(7) Covered sector employee**\nThe term covered sector employee means\u2014\n**(A)**\na nonexempt employee who is employed in a hospitality establishment, in a warehouse establishment, or in any of the following occupations, as described by the Bureau of Labor Statistics Standard Occupational Classification System (as in effect on the day before the date of enactment of this Act)\u2014\n**(i)**\nretail sales occupations consisting of occupations described in 41\u20131010 and 41\u20132000, and all subdivisions thereof, of such System, which includes first-line supervisors of sales workers, cashiers, gambling change persons and booth cashiers, counter and rental clerks, parts salespersons, and retail salespersons;\n**(ii)**\nfood preparation and serving related occupations as described in 35\u20130000, and all subdivisions thereof, of such System, which includes supervisors of food preparation and serving workers, cooks and food preparation workers, food and beverage serving workers, and other food preparation and serving related workers; or\n**(iii)**\ncleaning occupations as described in 37\u20132011, 37\u20132012, and 37\u20132019 of such System, which includes janitors and cleaners, maids and housekeeping cleaners, and building cleaning workers; or\n**(B)**\na nonexempt employee who is employed in any occupation that is designated by the Secretary under section 9(a)(2)(A) as appropriate for coverage under section 4.\n**(8) Domestic partner**\nThe term domestic partner means the individual recognized as being in a relationship with an employee under any domestic partnership, civil union, or similar law of the State or political subdivision of a State in which the employee resides.\n**(9) Employ**\nThe term employ has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(10) Employee**\nThe term employee means an individual who is\u2014\n**(A)**\nan employee, as defined in section 3(e) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(e) ), who is not described in any of subparagraphs (B) through (G);\n**(B)**\na State employee described in section 304(a) of the Government Employee Rights Act of 1991 (42 U.S.C. 2000e\u201316c(a));\n**(C)**\na covered employee, as defined in section 101 of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 ), other than an applicant for employment;\n**(D)**\na covered employee, as defined in section 411(c) of title 3, United States Code;\n**(E)**\na Federal officer or employee covered under subchapter V of chapter 63 of title 5, United States Code (without regard to the limitation in section 6381(1)(B) of that title), who is not covered under subparagraph (D);\n**(F)**\nan employee of the Library of Congress; or\n**(G)**\nan employee of the Government Accountability Office.\n**(11) Employer**\nThe term employer means a person\u2014\n**(A)**\nwho is\u2014\n**(i)**\na covered employer, as defined in paragraph (6), who is not described in any of clauses (ii) through (vii);\n**(ii)**\nan entity employing a State employee described in section 304(a) of the Government Employee Rights Act of 1991;\n**(iii)**\nan employing office, as defined in section 101 of the Congressional Accountability Act of 1995;\n**(iv)**\nan employing office, as defined in section 411(c) of title 3, United States Code;\n**(v)**\nan employing agency covered under subchapter V of chapter 63 of title 5, United States Code;\n**(vi)**\nthe Librarian of Congress; or\n**(vii)**\nthe Comptroller General of the United States; and\n**(B)**\nwho is engaged in commerce (including government), in the production of goods for commerce, or in an enterprise engaged in commerce (including government) or in the production of goods for commerce.\n**(12) Family relationship**\nThe term family relationship means a relationship with\u2014\n**(A)**\na child, spouse, domestic partner, parent, grandchild, grandparent, sibling, or parent of a spouse or domestic partner; or\n**(B)**\nany individual related to the employee involved by blood or affinity, whose close association with the employee is the equivalent of a family relationship described in subparagraph (A).\n**(13) Grandchild**\nThe term grandchild means the child of a child.\n**(14) Grandparent**\nThe term grandparent means the parent of a parent.\n**(15) Hospitality establishment**\nThe term hospitality establishment means a hotel, motel, inn, or similar transient lodging establishment.\n**(16) Minimum number of expected work hours**\nThe term minimum number of expected work hours means the minimum number of hours an employee will be assigned to work on a weekly or monthly basis.\n**(17) Nonexempt employee**\nThe term nonexempt employee means an employee who is not employed in a bona fide executive, administrative, or professional capacity, as defined and delimited for purposes of section 13(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 213(a)(1) ).\n**(18) On-call shift**\nThe term on-call shift means any time during which an employer requires an employee to\u2014\n**(A)**\nbe available to work; and\n**(B)**\ncontact the employer or the designee of the employer, or wait to be contacted by the employer or designee, to determine whether the employee is required to report to work at that time.\n**(19) Parent**\nThe term parent means a biological or adoptive parent, a stepparent, or a person who stood in a parental relationship to an employee when the employee was a child.\n**(20) Parental relationship**\nThe term parental relationship means a relationship in which a person assumed the obligations incident to parenthood for a child and discharged those obligations before the child reached adulthood.\n**(21) Secretary**\nThe term Secretary means the Secretary of Labor.\n**(22) Serious health condition**\nThe term serious health condition has the meaning given the term in section 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 ).\n**(23) Sibling**\nThe term sibling means a brother or sister, whether related by half blood, whole blood, or adoption or as a stepsibling.\n**(24) Split shift**\nThe term split shift means a schedule of daily hours in which the hours worked are not consecutive, except that\u2014\n**(A)**\na schedule in which the total time out for meals does not exceed one hour shall not be treated as a split shift; and\n**(B)**\na schedule in which the break in the employee's work shift is requested by the employee shall not be treated as a split shift.\n**(25) Spouse**\nThe term spouse means a person with whom an individual entered into\u2014\n**(A)**\na marriage as defined or recognized under State law in the State in which the marriage was entered into; or\n**(B)**\nin the case of a marriage entered into outside of any State, a marriage that is recognized in the place where entered into and could have been entered into in at least 1 State.\n**(26) State**\nThe term State has the meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(27) Warehouse establishment**\nThe term warehouse establishment means any business that engages primarily in the storage of goods, wares, or commodities for hire or compensation, and, in connection with such storage, may include the loading, packing, sorting, stacking, wrapping, distribution, or delivery of those goods, wares, or commodities.\n**(28) Work schedule**\nThe term work schedule means all of an employee\u2019s work shifts and on-call shifts, including specific start and end times for each shift, during a consecutive 7-day period.\n**(29) Work schedule change**\nThe term work schedule change means any modification to an employee\u2019s work schedule, such as an addition or reduction of hours, cancellation of a shift, or a change in the date or time of a work shift, by an employer.\n**(30) Work shift**\nThe term work shift means the specific hours of the workday during which an employee works.\n#### 3. Right to request and receive a flexible, predictable, or stable work schedule\n##### (a) Right To request\nAn employee may request from their employer a change in the terms and conditions of employment as they relate to factors including\u2014\n**(1)**\nthe number of hours the employee is required to work or be on call for work;\n**(2)**\nthe times when the employee is required to work or be on call for work;\n**(3)**\nthe location where the employee is required to work;\n**(4)**\nthe amount of notification the employee receives of work schedule assignments; and\n**(5)**\nminimizing fluctuations in the number of hours the employee is scheduled to work on a daily, weekly, or monthly basis.\n##### (b) Employer obligation To engage in an interactive process\n**(1) In general**\nIf an employee requests a change in the terms and conditions of employment as set forth in subsection (a), the employer shall engage in a timely, good-faith interactive process with the employee that includes a discussion of potential schedule changes that would meet the employee\u2019s needs.\n**(2) Result**\nSuch process shall result in\u2014\n**(A)**\nsubject to subsections (c) and (d), either granting or denying the request; and\n**(B)**\nin the event of a denial\u2014\n**(i)**\nconsidering alternatives to the proposed change that might meet the employee\u2019s needs and granting or denying a request for an alternative change in the terms and conditions of employment as set forth in subsection (a); and\n**(ii)**\nstating the reason for denial, including whether any such reason is a bona fide business reason.\n**(3) Information**\nIf information provided by the employee making a request under this section requires clarification, the employer shall explain what further information is needed and give the employee reasonable time to produce the information.\n##### (c) Requests related to serious health condition, caregiving, enrollment in education or training, or another job\nIf an employee makes a request for a change in the terms and conditions of employment as set forth in subsection (a), specifying that the request is because of the employee's serious health condition, the employee\u2019s responsibilities as a caregiver, the employee's enrollment in a career-related educational or training program, or a reason related to another job of the employee, the employer shall grant the request, unless the employer has a bona fide business reason for denying the request.\n##### (d) Other requests\nIf an employee makes a request for a change in the terms and conditions of employment as set forth in subsection (a), for a reason other than those reasons set forth in subsection (c), the employer may deny the request for any reason that is not unlawful.\n#### 4. Requirements for advance notice of work schedules, predictability pay, and split shift pay for covered sector employees\n##### (a) Advance notice requirement\n**(1) Providing notice of work schedules**\n**(A) In general**\nAn employer shall provide a covered sector employee with the work schedule of the employee\u2014\n**(i)**\nnot less than 14 days before the first day of such work schedule; or\n**(ii)**\nin the case of a new covered sector employee on or before the first day of work of such employee.\n**(B) Compensation for failure to provide notice of work schedule**\nAn employer that violates subparagraph (A) shall compensate each affected employee in the amount of $75 per day that a work schedule is not provided in violation of such subparagraph.\n**(C) Work schedule change**\nAn employer may make a work schedule change for the work schedule of a covered sector employee provided in accordance with subparagraph (A) if\u2014\n**(i)**\nsuch work schedule change is made not less than 14 days prior to the first day on which the change is to take effect; or\n**(ii)**\nthe employer provides predictability pay for such change in accordance with subsection (b).\n**(D) Minimum expected work hours**\n**(i) In general**\nAn employer shall inform a covered sector employee of an estimate of the minimum number of expected work hours the employee will be assigned to work per month for the following 12-month period\u2014\n**(I)**\nin the case of a new covered sector employee, on or before the first day of work of such employee; or\n**(II)**\nin the case of a covered sector employee who is employed by the employer on the date of enactment of this Act, not later than 90 days after such date.\n**(ii) Updating minimum expected work hours**\nAn employer shall, not less than once each year, provide each covered sector employee an updated estimate of the minimum number of expected work hours the employee will be assigned to work per month for the following 12-month period. Such a revised estimate shall be provided not later than the earlier of (as applicable)\u2014\n**(I)**\n1 year after the date on which the estimate was provided under clause (i) or the most recent update of an estimate was provided under this clause; or\n**(II)**\nthe day before the effective date of a significant change to the minimum expected work hours of the employee due to changes in the availability of the employee or to the business needs of the employer.\n**(2) Notifications in writing**\nThe notifications required under subparagraphs (A) and (D) of paragraph (1) shall be made to the employee involved in writing.\n**(3) Schedule posting requirement**\n**(A) In general**\nAn employer shall post a copy of the work schedule of each covered sector employee in a conspicuous place that is readily accessible and visible to all covered sector employees at the workplace. Posting by electronic means accessible to all covered sector employees shall be considered compliance with this subparagraph. At the request of an employee, the employer shall carry out the posting so that the identity of the employee is not readily identifiable from the schedules posted.\n**(B) Right to decline**\nA covered sector employee may decline, without penalty, to work any hours not included in the work schedule posted under subparagraph (A) as work hours for the covered sector employee.\n**(C) Consent**\nExcept as described in subsection (b)(2), if a covered sector employee voluntarily consents to work any hours not posted under subparagraph (A), such consent must be recorded in writing.\n**(4) Rule of construction**\nNothing in this subsection shall be construed to prohibit an employer from\u2014\n**(A)**\nproviding greater advance notice of the work schedule of a covered sector employee than is required under this subsection; or\n**(B)**\nusing any means, in addition to the written means required under paragraph (2), of notifying a covered sector employee of the work schedule of the employee.\n##### (b) Predictability pay for work schedule changes made with less than 14 days' notice\n**(1) In general**\nExcept as provided in paragraph (2), for each work schedule change provided to a covered sector employee that occurs less than 14 days prior to the first day on which the change is to take effect, the employer of the affected employee shall be required to provide the affected employee with pay (referred to in this subsection as predictability pay ) at the following rates:\n**(A)**\nThe covered sector employee\u2019s regular rate of pay per hour that the employee works plus one additional hour at such regular rate per work schedule change if the employer\u2014\n**(i)**\nadds any hours to the hours the employee is scheduled to work under subsection (a); or\n**(ii)**\nchanges the date, time, or location of the work shift the employee is scheduled to work under subsection (a) with no loss of hours.\n**(B)**\nNot less than 1/2 times the covered sector employee\u2019s regular rate of pay per hour for any hour that the employee is scheduled to work under subsection (a) and does not work due to the employer reducing or canceling such scheduled hours of work.\n**(2) Exceptions to predictability pay**\nAn employer shall not be required to pay predictability pay under paragraph (1), or to obtain written consent pursuant to subsection (a)(3)(C), under any of the following circumstances:\n**(A)**\nA covered sector employee requests a shift change in writing, including through the use of sick leave, vacation leave, or any other leave policy offered by the employer.\n**(B)**\nA schedule change is the result of a mutually agreed upon shift trade or coverage arrangement between covered sector employees, subject to any policy of the employer regarding required conditions for employees to exchange shifts.\n**(C)**\nThe employer\u2019s operations cannot begin or continue due to\u2014\n**(i)**\na threat to the property of an employee or the employer;\n**(ii)**\nthe failure of a public utility or the shutdown of public transportation;\n**(iii)**\na fire, flood, or other natural disaster;\n**(iv)**\na state of emergency declared by the President of the United States or by the governor of the State, or the mayor of the city, in which the operations are located; or\n**(v)**\na severe weather condition that poses a threat to employee safety.\n##### (c) Split shift pay requirement\nAn employer shall pay a covered sector employee for 1 additional hour at the employee\u2019s regular rate of pay for each day during which the employee works a split shift.\n##### (d) Pay stub transparency\nAny pay provided to an employee pursuant to subsection (a), (b), or (c) (referred to in this subsection as additional pay ) shall be included in the employee's regular paycheck. The employer shall identify, in the corresponding written wage statement or pay stub, the total number of hours of additional pay provided for the pay period involved and whether the additional pay was due to the requirements of subsection (a), the requirements of subsection (b), or the requirements of subsection (c).\n#### 5. Right to rest between work shifts\n##### (a) In general\nAn employee of a covered employer may decline, without penalty, to work any work shift or on-call shift that is scheduled or otherwise occurs\u2014\n**(1)**\nless than 11 hours after the end of the work shift or on-call shift for the previous day; or\n**(2)**\nduring the 11 hours following the end of a work shift or on-call shift that spanned 2 days.\n##### (b) Consent\n**(1) In general**\nAn employee may consent to work a shift as described in subsection (a), if the covered employer obtains the employee\u2019s consent in writing. Such consent may be for each such shift or for multiple shifts.\n**(2) Revocation**\nAn employee may revoke the consent provided under paragraph (1), in writing, at any time during the employment.\n##### (c) Compensation\nFor each instance that an employee of a covered employer works a shift described in subsection (a), the covered employer shall compensate the employee at 1.5 times the employee\u2019s scheduled rate of pay for the hours worked that are less than 11 hours apart from the hours worked during the previous shift.\n#### 6. Prohibited acts\n##### (a) Interference with rights\nIt shall be unlawful for any employer to interfere with, restrain, or deny the exercise or the attempt to exercise, any right provided under section 3, 4, or 5.\n##### (b) Retaliation prohibited\nIt shall be unlawful for any employer to discharge, threaten to discharge, demote, suspend, reduce work hours of, or take any other adverse employment action against any employee in retaliation for exercising the rights of an employee under this Act or opposing any practice made unlawful by this Act. For purposes of section 3, such retaliation shall include taking an adverse employment action against any employee on the basis of that employee\u2019s request for a change in work schedule, or because of an employee's eligibility or perceived eligibility to request or receive a change in the terms and conditions of employment, as described in such section, on the basis of a reason set forth in section 3(c).\n##### (c) Interference with proceedings or inquiries\nIt shall be unlawful for any person to discharge or in any other manner discriminate against any individual because such individual\u2014\n**(1)**\nhas filed any charge, or has instituted or caused to be instituted any proceeding, under or related to this Act;\n**(2)**\nhas given or is about to give, any information in connection with any inquiry or proceeding relating to any right provided under this Act; or\n**(3)**\nhas testified, or is about to testify, in any inquiry or proceeding relating to any right provided under this Act.\n#### 7. Remedies and enforcement\n##### (a) Investigative authority\n**(1) In general**\nTo ensure compliance with this Act, or any regulation or order issued under this Act, the Secretary shall have, subject to paragraph (3), the investigative authority provided under section 11(a) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 211(a) ).\n**(2) Obligation to keep and preserve records**\nEach employer shall make, keep, and preserve records pertaining to compliance with this Act in accordance with regulations issued by the Secretary under section 9.\n**(3) Required submissions generally limited to an annual basis**\nThe Secretary shall not require, under the authority of this subsection, any employer to submit to the Secretary any books or records more than once during any 12-month period, unless the Secretary has reasonable cause to believe there may exist a violation of this Act or any regulation or order issued pursuant to this Act, or is investigating a charge pursuant to subsection (c).\n**(4) Subpoena powers**\nFor the purposes of any investigation provided for in this section, the Secretary shall have the subpoena authority provided for under section 9 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 209 ).\n##### (b) Civil action by employees\n**(1) Liability**\n**(A) In general**\nAny employer who violates subsection (a) of section 6 (with respect to a right provided under section 3 or 5 or subsection (a), (b), or (c) of section 4) or subsection (b) or (c) of such section (each such provision referred to in this section as a covered provision ) shall be liable to any employee affected for\u2014\n**(i)**\ndamages equal to the amount of\u2014\n**(I)**\nany wages, salary, employment benefits (as defined in section 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 )), or other compensation denied, lost, or owed to such employee by reason of the violation; or\n**(II)**\nin a case in which wages, salary, employment benefits (as so defined), or other compensation have not been denied, lost, or owed to the employee, any actual monetary losses sustained by the employee as a direct result of the violation;\n**(ii)**\ninterest on the amount described in clause (i) calculated at the prevailing rate;\n**(iii)**\nexcept as described in subparagraph (B), an additional amount as liquidated damages equal to the sum of the amount described in clause (i) and the interest described in clause (ii); and\n**(iv)**\nsuch equitable relief as may be appropriate, including employment, reinstatement, and promotion.\n**(B) Exception for liquidated damages**\nIf an employer who has violated a covered provision proves to the satisfaction of the court that the act or omission which violated the covered provision was in good faith and that the employer had reasonable grounds for believing that the act or omission was not a violation of a covered provision, such court may, in the discretion of the court, waive such liquidated damages.\n**(2) Right of action**\nAn action to recover the damages, interest, or equitable relief set forth in paragraph (1) may be maintained against any employer (including a public agency) in any Federal or State court of competent jurisdiction by any one or more employees for and on behalf of\u2014\n**(A)**\nthe employees; or\n**(B)**\nthe employees and any other employees similarly situated.\n**(3) Fees and costs**\nThe court in such an action shall, in addition to any judgment awarded to the plaintiff, allow a reasonable attorney\u2019s fee, reasonable expert witness fees, and other costs of the action to be paid by the defendant.\n**(4) Limitations**\nThe right provided by paragraph (2) to bring an action by or on behalf of any employee shall terminate on the filing of a complaint by the Secretary in an action under subsection (c)(4) in which a recovery is sought of the damages, interest, or equitable relief described in paragraph (1)(A) owing to an employee by an employer liable under paragraph (1) unless the action described is dismissed without prejudice on motion of the Secretary.\n##### (c) Actions by the secretary\n**(1) Administrative action**\nThe Secretary shall receive, investigate, and attempt to resolve complaints of violations of this Act in the same manner that the Secretary receives, investigates, and attempts to resolve complaints of violations of sections 6 and 7 of the Fair Labor Standards Act of 1938 (29 U.S.C. 206 and 207), and may issue an order making determinations, and assessing a civil penalty described in paragraph (3) (in accordance with paragraph (3)), with respect to such an alleged violation.\n**(2) Administrative review**\nAn affected person who takes exception to an order issued under paragraph (1) may request review of and a decision regarding such an order by an administrative law judge. In reviewing the order, the administrative law judge may hold an administrative hearing concerning the order, in accordance with the requirements of sections 554, 556, and 557 of title 5, United States Code. Such hearing shall be conducted expeditiously. If no affected person requests such review within 60 days after the order is issued under paragraph (1), the order shall be considered to be a final order that is not subject to judicial review.\n**(3) Civil penalty**\n**(A) In general**\nAn employer who willfully and repeatedly violates\u2014\n**(i)**\nsection 4 or 5 shall be subject to a civil penalty in an amount per violation that is not less than $500 and not more than $1,000; or\n**(ii)**\nsubsection (b) or (c) of section 6 shall be subject to a civil penalty in an amount per violation that is not less than $1,100 and not more than $5,000.\n**(B) Willfully and repeatedly**\nFor purposes of subparagraph (A):\n**(i) Repeatedly**\nThe term repeatedly , with respect to a violation, means 2 or more such violations.\n**(ii) Willfully**\nThe term willfully , with respect to a violation, means such a violation for which, based on all of the facts and circumstances surrounding the violation, an employer\u2014\n**(I)**\nknew that its conduct was prohibited by, as applicable, section 4 or 5 or subsection (b) or (c) of section 6; or\n**(II)**\nshowed reckless disregard for the requirements of, as applicable, section 4 or 5 or subsection (b) or (c) of section 6.\n**(4) Civil action**\nThe Secretary may bring an action in any court of competent jurisdiction on behalf of aggrieved employees to\u2014\n**(A)**\nrestrain violations of this Act;\n**(B)**\naward such equitable relief as may be appropriate, including employment, reinstatement, and promotion; and\n**(C)**\nin the case of a violation of a covered provision, recover the damages and interest described in clauses (i) through (iii) of subsection (b)(1)(A).\n##### (d) Limitation\n**(1) In general**\nExcept as provided in paragraph (2), an action may be brought under this section not later than 2 years after the date of the last event constituting the alleged violation for which the action is brought.\n**(2) Willful violation**\nIn the case of such action brought for a willful violation of section 6, such action may be brought within 3 years of the date of the last event constituting the alleged violation for which such action is brought.\n**(3) Commencement**\nIn determining when an action is commenced by the Secretary or by an employee under this section for the purposes of this subsection, it shall be considered to be commenced on the date when the complaint is filed.\n##### (e) Other administrative officers\n**(1) Board**\nIn the case of employees described in section 2(10)(C), the authority of the Secretary under this Act shall be exercised by the Board of Directors of the Office of Congressional Workplace Rights.\n**(2) President; merit systems protection board**\nIn the case of employees described in section 2(10)(D), the authority of the Secretary under this Act shall be exercised by the President and the Merit Systems Protection Board.\n**(3) Office of personnel management**\nIn the case of employees described in section 2(10)(E), the authority of the Secretary under this Act shall be exercised by the Office of Personnel Management.\n**(4) Librarian of Congress**\nIn the case of employees of the Library of Congress, the authority of the Secretary under this Act shall be exercised by the Librarian of Congress.\n**(5) Comptroller General**\nIn the case of employees of the Government Accountability Office, the authority of the Secretary under this Act shall be exercised by the Comptroller General of the United States.\n#### 8. Notice and posting\n##### (a) In general\nEach employer shall post and keep posted, in conspicuous places on the premises of the employer where notices to employees and applicants for employment are customarily posted, a notice, to be prepared or approved by the Secretary (or, as applicable, the corresponding administrative officer specified in section 7(e)) setting forth excerpts from, or summaries of, the pertinent provisions of this Act and information pertaining to the filing of a complaint under this Act.\n##### (b) Penalty\nAny employer that willfully violates this section may be assessed a civil money penalty not to exceed $100 for each separate offense.\n#### 9. Regulations\n##### (a) Secretary of Labor\n**(1) In general**\nExcept as provided in subsections (b) through (f), not later than 180 days after the date of enactment of this Act, the Secretary shall issue such regulations as may be necessary to implement this Act.\n**(2) Regulations regarding additional occupations to be covered**\n**(A) In general**\nIn carrying out paragraph (1), the Secretary shall issue regulations that specify a process the Secretary will follow, in accordance with subparagraph (B), to identify and designate occupations in addition to retail, food service, cleaning, hospitality, or warehouse occupations that are appropriate for coverage under section 4.\n**(B) Criteria**\nThe regulations under subparagraph (A) shall provide that the Secretary shall so designate an additional occupation\u2014\n**(i)**\nin which not less than 10 percent of workers employed in the occupation generally\u2014\n**(I)**\nreceive advance notice of their work schedules less than 14 days before the first day of the work schedules; or\n**(II)**\nexperience fluctuations in the number of hours the employees are scheduled to work on a daily, weekly, or monthly basis; or\n**(ii)**\nfor which the Secretary determines such designation is appropriate.\n**(C) Data review**\nIn issuing regulations under subparagraph (A), the Secretary shall specify the process by which the Department of Labor will review data from stakeholders, and data collected or generated by the Department, in designating occupations.\n##### (b) Board\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Board of Directors of the Office of Congressional Workplace Rights shall issue such regulations as may be necessary to implement this Act with respect to employees described in section 2(10)(C). The procedures applicable to regulations of the Board issued for the implementation of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ), prescribed in section 304 of that Act ( 2 U.S.C. 1384 ), shall be the procedures applicable to regulations issued under this subsection.\n**(2) Consideration**\nIn prescribing the regulations, the Board shall take into consideration the enforcement and remedies provisions concerning the Office, and applicable to rights and protections under the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. ), under the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ).\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this Act shall be the same as substantive regulations issued by the Secretary to implement this Act, except to the extent that the Board may determine, for good cause shown and stated together with the regulations issued by the Board, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this Act with respect to the employees described in section 2(10)(C).\n##### (c) President\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the President shall issue such regulations as may be necessary to implement this Act with respect to employees described in section 2(10)(D).\n**(2) Consideration**\nIn prescribing the regulations, the President shall take into consideration the enforcement and remedies provisions concerning the President and the Merit Systems Protection Board, and applicable to rights and protections under the Family and Medical Leave Act of 1993, under chapter 5 of title 3, United States Code.\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this Act shall be the same as substantive regulations issued by the Secretary to implement this Act, except to the extent that the President may determine, for good cause shown and stated together with the regulations issued by the President, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this Act with respect to the employees described in section 2(10)(D).\n##### (d) Office of Personnel Management\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Office of Personnel Management shall issue such regulations as may be necessary to implement this Act with respect to employees described in section 2(10)(E).\n**(2) Consideration**\nIn prescribing the regulations, the Office shall take into consideration the enforcement and remedies provisions concerning the Office under subchapter V of chapter 63 of title 5, United States Code.\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this Act shall be the same as substantive regulations issued by the Secretary to implement this Act, except to the extent that the Office may determine, for good cause shown and stated together with the regulations issued by the Office, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this Act with respect to the employees described in section 2(10)(E).\n##### (e) Librarian of Congress\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Librarian of Congress shall issue such regulations as may be necessary to implement this Act with respect to employees of the Library of Congress.\n**(2) Consideration**\nIn prescribing the regulations, the Librarian shall take into consideration the enforcement and remedies provisions concerning the Librarian of Congress under title I of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 et seq. ).\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this Act shall be the same as substantive regulations issued by the Secretary to implement this Act, except to the extent that the Librarian may determine, for good cause shown and stated together with the regulations issued by the Librarian, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this Act with respect to employees of the Library of Congress.\n##### (f) Comptroller General\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Comptroller General shall issue such regulations as may be necessary to implement this Act with respect to employees of the Government Accountability Office.\n**(2) Consideration**\nIn prescribing the regulations, the Comptroller General shall take into consideration the enforcement and remedies provisions concerning the Comptroller General under title I of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 et seq. ).\n**(3) Modifications**\nThe regulations issued under paragraph (1) to implement this Act shall be the same as substantive regulations issued by the Secretary to implement this Act, except to the extent that the Comptroller General may determine, for good cause shown and stated together with the regulations issued by the Comptroller General, that a modification of such substantive regulations would be more effective for the implementation of the rights and protections under this Act with respect to employees of the Government Accountability Office.\n#### 10. Research, education, and technical assistance program and surveys\n##### (a) In general\nThe Secretary shall provide information and technical assistance to employers, labor organizations, and the general public concerning compliance with this Act.\n##### (b) Program\nIn order to achieve the objectives of this Act\u2014\n**(1)**\nthe Secretary, acting through the Administrator of the Wage and Hour Division of the Department of Labor, shall issue guidance on compliance with this Act regarding providing a flexible, predictable, or stable work environment through changes in the terms and conditions of employment as provided in section 3(a); and\n**(2)**\nthe Secretary shall carry on a continuing program of research, education, and technical assistance, including\u2014\n**(A)**\n**(i)**\nconducting pilot programs that implement fairer work schedules, including by promoting cross-training, providing 3 weeks or more advance notice of schedules, providing employees with a minimum number of hours of work, and using electronic workforce management systems to provide more flexible, predictable, and stable schedules for employees; and\n**(ii)**\nevaluating the results of such pilot programs for employees, employee's families, and employers;\n**(B)**\npublishing and otherwise making available to employers, labor organizations, professional associations, educational institutions, the various communication media, and the general public the findings of studies regarding fair work scheduling policies and other materials for promoting compliance with this Act;\n**(C)**\nsponsoring and assisting State and community informational and educational programs; and\n**(D)**\nproviding technical assistance to employers, labor organizations, professional associations, and other interested persons on means of achieving and maintaining compliance with the provisions of this Act.\n##### (c) Current population survey\nThe Secretary, acting through the Commissioner of the Bureau of Labor Statistics, and the Director of the Bureau of the Census shall\u2014\n**(1)**\ninclude in the Current Population Survey questions on\u2014\n**(A)**\nthe magnitude of fluctuation in the number of hours the employee is scheduled to work on a daily, weekly, or monthly basis;\n**(B)**\nthe extent of advance notice an employee receives of the employee's work schedule;\n**(C)**\nthe extent to which an employee has input in the employee's work schedule; and\n**(D)**\nthe number of hours that an employee would prefer to work, relative to the number of hours the employee is currently working; and\n**(2)**\nat regular intervals, update and conduct the Contingent Worker Supplement, the Work Schedules and Work at Home Supplement, and other relevant supplements (as determined by the Secretary), to the Current Population Survey and the American Time Use Survey.\n#### 11. Rights retained by employees\nThis Act provides minimum requirements and shall not be construed to preempt, limit, or otherwise affect the applicability of any other law, requirement, policy, or standard that provides for greater rights for employees than are required in this Act.\n#### 12. Exemption\nThis Act shall not apply to any employee covered by a valid collective bargaining agreement if\u2014\n**(1)**\nthe terms of the collective bargaining agreement include terms that govern work scheduling practices; and\n**(2)**\nthe provisions of this Act are expressly waived in such collective bargaining agreement.\n#### 13. Effect on other law\n##### (a) In general\nNothing in this Act shall be construed as superseding, or creating or imposing any requirement in conflict with, any Federal, State, or local regulation or other law (including the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2601 et seq. ), the National Labor Relations Act ( 29 U.S.C. 151 et seq. ), the Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ), and title VII of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e et seq. )).\n##### (b) Relationship to collective bargaining rights\nNothing in this Act (including section 12) shall be construed to diminish or impair the rights of an employee under any valid collective bargaining agreement.",
      "versionDate": "2025-12-17",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-21T16:34:11Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3550is.xml"
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
      "title": "Schedules That Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Schedules That Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit employees to request changes to their work schedules without fear of retaliation and to ensure that employers consider these requests, and to require employers to provide more predictable and stable schedules for employees in certain occupations with evidence of unpredictable and unstable scheduling practices that negatively affect employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:29Z"
    }
  ]
}
```
