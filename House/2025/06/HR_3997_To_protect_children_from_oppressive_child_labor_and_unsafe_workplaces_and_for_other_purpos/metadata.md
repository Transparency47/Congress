# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3997
- Title: Protecting Children Act
- Congress: 119
- Bill type: HR
- Bill number: 3997
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3997",
    "number": "3997",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "S000185",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
        "lastName": "Scott",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Protecting Children Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:00:15Z",
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
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "OR"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "KY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "LA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NC"
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
      "sponsorshipDate": "2025-06-27",
      "state": "DC"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3997ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3997\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Scott of Virginia (for himself, Ms. Omar , Ms. Bonamici , and Mr. McGarvey ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo protect children from oppressive child labor and unsafe workplaces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Children Act .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title.\nSec.\u20022.\u2002Table of contents.\nSec.\u20023.\u2002Effective date.\nTitle I\u2014Improving Enforcement\nSec.\u2002101.\u2002Adjusting civil monetary penalties.\nSec.\u2002102.\u2002Enhancing criminal penalties.\nSec.\u2002103.\u2002Expanding use of hot goods injunctions.\nSec.\u2002104.\u2002Enabling private enforcement.\nTitle II\u2014Strengthening Capacity to Protect Children\nSec.\u2002201.\u2002Increasing expertise for protecting children from unsafe employment and oppressive child labor.\nSec.\u2002202.\u2002Supporting implementation and interagency collaboration.\nTitle III\u2014Updating Standards to Protect Children\nSec.\u2002301.\u2002Improving process for updating standards on conditions of oppressive child labor.\nSec.\u2002302.\u2002Judicial review of rulemaking.\nTitle IV\u2014Increasing Research and Public Education\nSec.\u2002401.\u2002Coordinating research on child labor.\nSec.\u2002402.\u2002Developing a comprehensive statistical program.\nSec.\u2002403.\u2002Enabling training and public engagement.\n#### 3. Effective date\nThis Act, and the amendments made by this Act, shall take effect on the date that is 60 days after the date of enactment of this Act.\nI\nImproving Enforcement\n#### 101. Adjusting civil monetary penalties\n##### (a) Oppressive child labor\nSection 16(e) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(e) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)\u2014\n**(A)**\nby striking not to exceed\u2014 and inserting as follows: ;\n**(B)**\nby moving the margins for clauses (i) and (ii) 4 ems to the left;\n**(C)**\nin clause (i)\u2014\n**(i)**\nby striking $11,000 and inserting Not more than $150,000 but not less than $1,500 ; and\n**(ii)**\nby striking violation; or and inserting violation, which penalty may be doubled where the violation is a repeated or willful violation. ; and\n**(D)**\nin clause (ii), by striking $50,000 and inserting Not more than $700,000 but not less than $7,000 ; and\n**(2)**\nin paragraph (3), by striking charged and and inserting charged, the economic benefit of noncompliance, and .\n##### (b) Unsafe working conditions\n**(1) Structure and headers**\nSection 17 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 666 ) is amended\u2014\n**(A)**\nin subsection (a), by striking Any and inserting the following:\nCivil penalties .\u2014 (1) Base penalties (A) Any ;\n**(B)**\nby redesignating subsection (b) as subsection (a)(1)(B);\n**(C)**\nby redesignating subsection (d) as subsection (a)(1)(C);\n**(D)**\nby redesignating subsection (c) as subsection (a)(1)(D);\n**(E)**\nby redesignating subsection (i) as subsection (a)(1)(E);\n**(F)**\nin subsection (f), by striking Any and inserting the following:\nCriminal penalties .\u2014 (1) Any ;\n**(G)**\nby redesignating subsection (f), as so amended, as subsection (b);\n**(H)**\nby redesignating subsections (g), (h), and (e) as subsections (b)(2), (b)(3), and (b)(4) respectively; and\n**(I)**\nby redesignating subsections (j), (k), and (l) as subsections (c), (d), and (e) respectively.\n**(2) Penalty amounts**\nSection 17(a)(1) of the Occupational Safety and Health Act of 1970, as amended by paragraph (1), is further amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking $70,000 and inserting $700,000 ;\n**(II)**\nby striking $5,000 and inserting $50,000 ; and\n**(III)**\nby striking the word willful ;\n**(ii)**\nin subparagraph (B), by striking $7,000 and inserting $70,000, but not less than $7,000, ; and\n**(iii)**\nin subparagraph (C), by striking $7,000 and inserting $70,000, but not less than $7,000, ; and\n**(B)**\nby adding at the end the following:\n(2) Enhancements (A) Young workers If any significant violation caused or contributed to serious physical harm to an employee under 18 years of age, the minimum and maximum civil penalty otherwise allowed by paragraph (1) shall be doubled for each such violation. (B) Fatalities If any significant violation caused or contributed to the death of an employee\u2014 (i) the minimum and maximum civil penalty otherwise allowed by paragraph (1) shall be doubled for each such violation; and (ii) in a case in which such employee was under 18 years of age, such civil penalty shall be trebled for each such violation. .\n**(3) Considerations for penalty levels**\nSection 17(c) of the Occupational Safety and Health Act of 1970, as redesignated by paragraph (1), is further amended\u2014\n**(A)**\nby striking the first word and inserting Assessment of penalties. \u2014The ; and\n**(B)**\nby striking and the history and inserting the economic benefit of noncompliance, and the history .\n**(4) Definition**\nSection 17(d) of the Occupational Safety and Health Act of 1970, as redesignated by paragraph (1), is further amended\u2014\n**(A)**\nby striking For purposes of this section, the and inserting the following:\nDefinitions .\u2014For purposes of this section\u2014 (1) Serious The ; and\n**(B)**\nby adding at the end the following:\n(2) Significant The term significant violation means\u2014 (A) a serious, willful, or repeated violation; (B) a failure to correct, as described in paragraph (1)(C), where the underlying violation was a serious, willful, or repeated violation. .\n#### 102. Enhancing criminal penalties\n##### (a) Oppressive child labor\nSection 16(a) of the Fair Labor Standards Act ( 29 U.S.C. 216(a) ) is amended\u2014\n**(1)**\nby striking the first word and inserting the following:\nCriminal penalties .\u2014 (1) In general Except as provided in paragraph 2, any ;\n**(2)**\nby striking the word subsection each place it appears and inserting the word paragraph ; and\n**(3)**\nby adding at the end the following:\n(2) Oppressive child labor (A) Negligence with respect to a child Any person who knowingly or willfully violates section 15(a)(4) of this Act and thereby negligently places an employee employed in violation of such section in imminent danger of death or serious bodily injury shall be punished by a fine under title 18, United States Code, or by imprisonment for not more than 1 year, or both. If a conviction of any person under this subparagraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. (B) Knowing violation with respect to a child Any person who knowingly or willfully violates section 15(a)(4) of this Act and thereby knowingly places an employee employed in violation of such section in imminent danger of death or serious bodily injury shall be punished by a fine under title 18, United States Code, or by imprisonment of not more than 15 years, or both. Any person, other than an individual, committing such violation shall, upon conviction under this subparagraph, be subject to a fine of not more than $5,000,000 for each violation. If a conviction of any person under this subparagraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. (C) Cause of death to a child Any person who knowingly or willfully violates section 15(a)(4) of this Act and thereby knowingly places an employee employed in violation of such section in imminent danger of death or serious bodily injury, and such violation results in the death of a child, shall be punished by a fine under title 18, United States Code, and imprisonment for any term of years or for life. Any person, other than an individual, committing such violation shall, upon conviction under this subparagraph, be subject to a fine of not more than $10,000,000 for each violation. If a conviction of any person under this subparagraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. .\n##### (b) Unsafe working conditions\nSection 17(b) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 666(b) ), as so amended and redesignated by this Act, is further amended\u2014\n**(1)**\nin paragraph (1), by striking of not more and all that follows and inserting under title 18, imprisonment for not more than 5 years, or both. If a conviction of any person under this paragraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. ;\ncurrently 17(f)\n**(2)**\nin paragraph (2), by striking of not more and all that follows and inserting under title 18, imprisonment for not more than 5 years, or both. If a conviction of any person under this paragraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. ; and\ncurrently 17(g)\n**(3)**\nby amending paragraph (4) to read as follows:\n(4) Imminent danger or death (A) Any employer who negligently violates any standard, rule, or order promulgated pursuant to section 6 of this Act, or of any regulations prescribed pursuant to this Act, and thereby negligently places an employee in imminent danger of death or serious bodily injury, shall be punished by a fine under title 18, United States Code, imprisonment for not more than one year, or both. If a conviction of any person under this paragraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. (B) Any employer who knowingly or willfully violates any standard, rule, or order promulgated pursuant to section 6 of this Act, or of any regulations prescribed pursuant to this Act, and in so doing places an employee in imminent danger of death or serious bodily injury, shall be punished by a fine under title 18, United States Code, imprisonment for not more than 15 years, or both. Any person, other than an individual, committing such violation shall, upon conviction under this paragraph, be subject to a fine of not more than $5,000,000 for each violation. If a conviction of any person under this paragraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. (C) Any employer who knowingly or willfully violates any standard, rule, or order promulgated pursuant to section 6 of this Act, or of any regulations prescribed pursuant to this Act, and such violation causes the death of an employee, shall be punished by a fine under title 18, United States Code, and imprisonment for any term of years or for life. Any person, other than an individual, committing such violation shall, upon conviction under this paragraph, be subject to a fine of not more than $10,000,000 for each violation. If a conviction of any person under this paragraph is for a violation committed after a first conviction of such person under this paragraph, the maximum punishment shall be doubled with respect to both the fine and imprisonment. (5) Endangerment of young workers The maximum punishment otherwise prescribed by paragraph 4 shall be doubled with respect to both the fine and imprisonment for each violation that puts an employee under the age of 18 in imminent danger of death or serious bodily injury or causes the death of such employee, as the case may be. . currently 17(e)\n#### 103. Expanding use of hot goods injunctions\nSection 12(a) of the Fair Labor Standards Act ( 29 U.S.C. 212(a) ) is amended\u2014\n**(1)**\nby striking the first word and inserting the following:\nShipment of goods. \u2014 (1) In general No ;\n**(2)**\nby striking thirty and inserting ninety ;\n**(3)**\nby striking the colon after employed and inserting a period;\n**(4)**\nby striking Provided, That any and inserting the following:\n(2) Good faith Any ;\n**(5)**\nby striking the colon after prohibited by this subsection and inserting a period; and\n**(6)**\nby striking And provided further, That a and inserting the following:\n(3) Prosecution and conviction A .\n#### 104. Enabling private enforcement\nSection 16(b) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(b) ) is amended as follows:\n**(1) Structure and headers**\n**(A)**\nIn the first sentence, by striking the first word and inserting the following:\nPrivate enforcement .\u2014 (1) Remedies (A) Minimum wages and overtime Any .\n**(B)**\nIn the second sentence, by striking the first word and inserting the following:\n(B) Fair employment practices Any .\n**(C)**\nIn the third sentence, by striking the first word and inserting the following:\n(C) Tips Any .\n**(D)**\nIn the fourth sentence, by striking the first word and inserting the following:\n(2) Right of action (A) In general An .\n**(E)**\nIn the fifth sentence, by striking the first word and inserting the following:\n(B) Collective action No .\n**(F)**\nIn the sixth sentence, by striking the first word and inserting the following:\n(C) Fees and costs The .\n**(G)**\nIn the last sentence, by striking the first word and inserting the following:\n(3) Actions by the secretary The .\n**(2) New right of action**\nIn paragraph (1), as amended by the previous paragraph, by adding at the end the following:\n(D) Child labor Any employer who violates section 12 shall, if any child is harmed as a result of such violation, be liable to the child affected for compensatory and punitive damages. .\nII\nStrengthening Capacity to Protect Children\n#### 201. Increasing expertise for protecting children from unsafe employment and oppressive child labor\n##### (a) Establishment of advisory committee\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 204 ), as amended by title I of this Act, is further amended by inserting after section 4 the following new section:\n4A. Administration of child labor provisions (a) National Advisory Committee on Child Labor (1) Establishment There is hereby established a National Advisory Committee on Child Labor, which shall advise, consult with, and make recommendations to the Secretary of Labor and the Secretary of Health and Human Services on matters relating to\u2014 (A) oppressive child labor; (B) preventing children, including vulnerable children, from being exposed to oppressive child labor; and (C) protecting children\u2019s health, safety, and welfare with regard to employment. (2) Members (A) Appointment The Advisory Committee shall consist of 15 members appointed by the Secretary of Labor, five of whom are to be designated in consultation with the Secretary of Health and Human Services (acting through the Director of the National Institute for Occupational Safety and Health), without regard to the provisions of title 5, United States Code, governing appointments in the competitive service. (B) Qualification The members shall be selected upon the basis of their experience and competence in the field of occupational safety and health, child welfare, labor trafficking, and child labor. (C) Composition The membership of the Advisory Committee shall consist of qualified persons from Federal agencies, the States, and private life, including the following: (i) one or more representatives of State agencies focused on occupational safety and health established pursuant to section 18 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 667 ); (ii) one or more persons qualified by experience and affiliation to present the viewpoint of the employers involved, and one or more persons similarly qualified to present the viewpoint of the workers involved, provided that the number of persons presenting employer viewpoints is equal to the number of persons presenting workers\u2019 viewpoints; and (iii) such other persons as the Secretary may appoint who are qualified by knowledge and experience to make a useful contribution to the work of the Advisory Committee, provided that the number of persons so appointed shall not exceed the number appointed as representatives of Federal and State agencies. (D) Conflicts of interest No member of the Advisory Committee (other than representatives of employers and employees) shall have an economic interest in any proposed rule, order, or recommendation for rule or order. (E) Leadership The Secretary shall designate one of the public members as Chairperson. (F) Compensation Members of the Advisory Committee appointed from private life shall be compensated in the same manner as consultants or experts under section 3109 of title 5, United States Code. The Secretary shall pay to any State which is the employer of a member of the Advisory Committee who is a representative of the occupational safety and health or child welfare agency of that State, reimbursement sufficient to cover the actual cost to the State resulting from such representative\u2019s membership on the Advisory Committee. (G) Continuity A member of the Advisory Committee who is otherwise qualified may continue to serve until a successor is appointed. (3) Resources The Secretary shall furnish to the Advisory Committee an executive secretary and such secretarial, clerical, and other services as are deemed necessary to the conduct of its business. (4) Meetings The Advisory Committee shall hold no fewer than two meetings during each calendar year. All meetings of the Advisory Committee shall be open to the public and a transcript shall be kept and made available for public inspection. .\n##### (b) Definition\nSection 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ) is amended by adding at the end the following new paragraph:\n(z) Advisory Committee means the National Advisory Committee on Child Labor established under section 4A(a). .\n#### 202. Supporting implementation and interagency collaboration\n##### (a) Child labor and safety and health fund\nSection 4A of the Fair Labor Standards Act of 1938, as added by the previous section, is further amended by adding at the end the following:\n(b) Child labor and safety and health fund (1) In general There is established in the Treasury of the United States a fund, to be known as the Child Labor and Safety and Health Fund (referred to in this subsection as the Fund ), from which amounts may be obligated and expended without subsequent appropriation to carry out the program established under paragraph (3). (2) Transfers to Fund (A) Availability Amounts deposited into the Fund from the sources described in subparagraph (B) shall be available without fiscal year limitation solely for the uses described in paragraph (3). (B) Sources described The sources described in this paragraph are as follows: (i) Civil penalties described in section 16(e)(5). (ii) Civil penalties described in section 17(e) of the Occupational Safety and Health Act of 1970. (3) Program (A) In general The Secretary of Labor shall create and carry out a program to conduct, or award grants or contracts to entities to conduct, activities related to oppressive child labor and the occupational safety and health of employees under the age of 18 in accordance with subparagraph (B). (B) Uses of funds On request of the Secretary of Labor, the Secretary of Treasury shall transfer from the Fund to the Secretary of Labor, such amounts as the Secretary of Labor determines to be necessary to implement the program established by subparagraph (A) through the following activities: (i) Investigation, enforcement, implementation, and interagency collaboration. (ii) Training and education of children, employers, and teachers and other professionals who may reasonably be anticipated to identify children working in conditions of oppressive child labor, on oppressive child labor, occupational safety and health, and young employees\u2019 rights at work. (iii) Research on oppressive child labor in accordance with section 5 and the occupational safety and health of young employees in accordance with section 20 of the Occupational Safety and Health Act of 1970, to be conducted directly or through grant or contract by the Secretary of Health and Human Services, acting through the Director of the National Institute for Occupational Safety and Health. (4) Records and reports The Secretary shall keep adequate records regarding amounts so deposited and used. Not later than March 1 of each year, the Secretary shall submit a report to the Committees on Appropriations, the Committee on Education and Workforce of the House of Representatives, and the Committee on Health, Education, Labor, and Pensions of the Senate consisting of the following: (A) For the fiscal year preceding the year in which a report is required to be submitted, all funds received in the Fund, uses of such funds, and data about such uses, including the number of investigations and enforcement actions brought using such funds and the outcomes of such investigations and enforcement actions, trainings delivered, and research supported. (B) For the fiscal year in which a report is required to be submitted, all funds received and estimated to be received, all actual and estimated uses of such funds, and actual and estimated data about such uses. .\n##### (b) Retention of child labor penalties\nSection 16(e)(5) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216(e)(5) ) is amended by striking the last sentence and inserting Civil penalties collected for violations of section 12 shall be deposited in the fund established by section 4A(b). .\n##### (c) Retention of penalties for young workers\u2019 illness and injury\nSection 17(e) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 666(e) ), as redesignated by title I of this Act, is amended further\u2014\n**(1)**\nby striking the first word and inserting the following:\nProcedure for payment of civil penalties .\u2014 (1) In general Except as provided in paragraph 2, civil ; and\n**(2)**\nby adding at the end the following:\n(2) Penalties involving young workers Civil penalties enhanced pursuant to subsection (a)(2)(A) or subsection (a)(2)(B)(ii) shall be deposited in the fund established by section 4A(b) of the Fair Labor Standards Act of 1938. .\nIII\nUpdating Standards to Protect Children\n#### 301. Improving process for updating standards on conditions of oppressive child labor\n##### (a) Rulemaking policies\n**(1) Permitted work**\n**(A) In general**\nSection 12 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 212 ) is amended by adding at the end the following:\n(e) Children\u2019s welfare .\n**(B) Transfer amendment**\nThe last sentence of section 3(l) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(l) ) is\u2014\n**(i)**\ntransferred to subsection (e) of section 12 of such Act ( 29 U.S.C. 212 ); and\n**(ii)**\ninserted so as to appear after the subsection heading of such section 12.\n**(2) Hazardous occupations**\nSection 12 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 212 ) is further amended by adding at the end the following:\n(f) Hazardous occupations (1) Periodic review The Secretary shall periodically review the hazardous occupation orders promulgated by the Secretary to determine if, to more adequately protect children from oppressive child labor, a new hazardous occupation order should be promulgated, or an update to an existing such order should be promulgated. (2) Considerations In determining the need for promulgating a new hazardous occupation order or promulgating an update to an existing such order, the Secretary shall\u2014 (A) place preeminent value on assuring the safety, health, and well-being of children; (B) take into consideration the vulnerable, formative, and malleable nature of childhood and adolescence, which requires a higher standard of protection for children than that accorded to adults; (C) adopt any reasonable precautionary assumptions necessary to prevent children from being exposed in the workplace to hazards that may reasonably be anticipated to cause serious illness or injury, disability, premature mortality, or long-term health effects (including exposure to any substance which is known or may reasonably be anticipated to be carcinogenic, mutagenic, teratogenic, neurotoxic, reprotoxic, or asthmagenic); and (D) take into consideration any\u2014 (i) recommendations provided under paragraph (3) of this section by the Advisory Committee or the Secretary of Health and Human Services provided under paragraph (3) of this subsection; and (ii) any information provided under subsection (g). (3) Recommendations for orders (A) Advisory committee (i) In general In a case in which the Secretary determines that expert advice is needed to aid the Secretary\u2019s decision whether to promulgate a new hazardous occupation order (or an update to such an existing order), the Secretary\u2014 (I) may request the Advisory Committee to submit its recommendations to the Secretary relating to the proposed or existing order; and (II) in a case in which the Secretary requests recommendations pursuant to subclause (I), shall provide the Advisory Committee with\u2014 (aa) any proposals developed by the Secretary or by the Secretary of Health and Human Services relating to the proposed or existing order with respect to which the Secretary is requesting recommendations; and (bb) all pertinent factual information developed by the Secretary or the Secretary of Health and Human Services, including any applicable information provided under subparagraph (B) or otherwise available. (ii) Submission of recommendations (I) In general Subject to subclause (II), the Advisory Committee shall submit to the Secretary its recommendations relating to an existing or proposed order not later than 90 days after the date of the Committee\u2019s receipt of such request from the Secretary relating to such order. (II) Exceptions The Secretary may prescribe a period for the submission of recommendations by the Advisory Committee under subclause (I) relating to an existing or proposed order that is longer or shorter than the 90-day period referred to in subclause (I), except that such period may not exceed 180 days after the date of the Committee\u2019s receipt of the request for recommendations relating to such order. (iii) Receipt of recommendations In the case in which the Advisory Committee recommends the promulgation of a new order (or an update to an existing order), the Secretary shall, not later than 90 days after submission of such recommendation by the Advisory Committee or the expiration of the period prescribed by the Secretary for such submission\u2014 (I) promulgate pursuant to paragraph (4) such order (or update) in a manner consistent with such recommendations; or (II) publish such recommendations in the Federal Register along with a detailed and substantive statement of the Secretary\u2019s reasons for not promulgating the new order or update. (B) NIOSH criteria In a case in which the Secretary of Health and Human Services (acting through the Director of the National Institute for Occupational Safety and Health) recommends (accompanied by appropriate criteria) the promulgation of a new hazardous occupation order (or an update to an existing such order) by the Secretary of Labor, the Secretary of Labor shall, not later than 180 days after receiving such recommendation\u2014 (i) refer such recommendation to the Advisory Committee pursuant to paragraph (3) and carry out applicable requirements of such paragraph; (ii) promulgate pursuant to paragraph (4) such order (or update) in a manner consistent with the recommendation provided under this subparagraph; or (iii) publish such recommendation in the Federal Register along with a detailed and substantive statement of the Secretary\u2019s reasons for not promulgating the new order (or update). (4) Procedures (A) In general The Secretary shall, when acting on the Secretary\u2019s own initiative or in response to a recommendation by the Advisory Committee or Secretary of Health and Human Services, promulgate any hazardous occupation order (including an update to an existing such order) in accordance with this paragraph and in accordance with section 553 of title 5, United States Code (without regard to any reference in such section to sections 556 and 557 of such title). (B) Comment When publishing a proposed order pursuant to this paragraph, the Secretary shall afford interested persons a period of 60 days after such publication to submit written data or comments on the order. Such comment period may be extended by the Secretary for good cause but in any event shall last no more than 120 days. (C) Transparency For any rulemaking notice pursuant to this paragraph, the Secretary shall place in the public record not later than the date of such rulemaking notice the following: (i) The drafts of such rulemakings prepared before publication and submitted by the Secretary to the Office of Management and Budget for any interagency review process prior to publication. (ii) A summary of the substance of any changes between the text of the draft rulemaking that the agency provided to the Office of Management and Budget under section 6(a)(3)(B)(i) of Executive Order 12,866 and the text published in the Federal Register, excluding any non-substantive changes such as spelling or grammatical corrections or re-ordering of text that has no legal effect. (iii) A statement identifying any party or entity at whose request any such change was made. (5) Effect A hazardous occupation order or any update to such an order shall become effective upon promulgation, except that the Secretary may include a reasonable delay in the effective date. (g) Authoritative expertise When promulgating any order pursuant to this section, the Secretary may adopt, rely on, or presume to be the best available evidence of children\u2019s health, safety, and well-being or conditions of work particularly hazardous to children, any recommendation, finding, assessment, or research by the National Institute for Occupational Safety and Health, the National Academies of Science, Engineering, and Medicine, the National Toxicology Program, the Integrated Risk Information System of the Environmental Protection Agency, or the International Agency for Research on Cancer. (h) Hazardous occupation order defined In this section, the term hazardous occupation order means any rule, regulation, or order promulgated pursuant to subsection (f)(4) by the Secretary that deems one or more occupations or working conditions as oppressive child labor due to the determination by the Secretary that such occupations or working conditions are particularly hazardous for the employment of children of certain ages or detrimental to the health and well-being of children. .\n**(3) Preventing rollbacks of child labor standards**\nSection 12 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 212 ) is further amended further by adding at the end the following:\n(i) Maintaining protection No order, rule, or regulation promulgated pursuant to subsections (e) or (f) shall reduce the protection afforded children by an existing order, rule, or regulation promulgated under this Act. .\n#### 302. Judicial review of rulemaking\nSection 10 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 210 ) is amended to read as follows:\n10. Judicial review (a) Filing of petition Any person who may be adversely affected by an order, rule, or regulation pursuant to this Act may file a petition for review of such order, rule, or regulation with the United States court of appeals for the circuit where such person resides, where the principal place of business of such person is located, or in the United States Court of Appeals for the District of Columbia. The filing of a petition for review of any order, rule, or regulation under this section shall not operate as a stay of such order, rule, or regulation. (b) Timely filing Any petition for review under this section shall be filed not later than sixty days after the date on which there is notice of the rulemaking with respect to such order, rule, or regulation in the Federal Register. (c) Not subject to subsequent review Action of the Secretary with respect to which review could have been obtained under this section shall not be subject to judicial review in civil or criminal proceedings for enforcement. .\nIV\nIncreasing Research and Public Education\n#### 401. Coordinating research on child labor\n##### (a) Research and related activities\n**(1) In general**\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended by inserting after section 4 ( 29 U.S.C. 204 ) the following:\n5. Research and related activities ;\n**(2) Special exemptions relating to child labor**\nParagraph (2) of section 4(d) of such Act is\u2014\n**(A)**\ntransferred to section 5 of such Act;\n**(B)**\ninserted so as to appear after the section heading;\n**(C)**\nredesignated as subsection (a) of such section 5; and\n**(D)**\namended\u2014\n**(i)**\nby striking the first word and inserting Periodic review of exemptions .\u2014The ; and\n**(ii)**\nby striking January 1, 1976 and inserting five years after the effective date of the Protecting Children Act and shall update such studies and such report every ten years thereafter ;\n**(3) Studies on preventing curtailment of employment opportunities for manpower groups**\nParagraph (3) of section 4(d) of such Act is\u2014\n**(A)**\ntransferred to section 5 of such Act;\n**(B)**\ninserted so as to appear after subsection (a) of such section 5, as amended by paragraph (2);\n**(C)**\nredesignated as subsection (b) of such section 5; and\n**(D)**\namended by striking the first word and inserting Employment opportunity .\u2014The .\n**(4) Conforming amendment**\nSubsection (d) of section 4 of such Act is further amended\u2014\n**(A)**\nby striking (d)(1) The Secretary shall submit and inserting the following:\n(d) Biennial report The Secretary shall submit .\n##### (b) National research agenda on child labor\nSection 5 of the Fair Labor Standards Act of 1938 is further amended by adding at the end the following:\n(c) National research agenda on child labor (1) In general The Secretary of Health and Human Services (acting through the Director of the National Institute for Occupational Safety and Health), after consultation with the Secretary of Labor and with other appropriate Federal departments or agencies, shall conduct (directly or by grants or contracts) research, experiments, and demonstrations relating to oppressive child labor, the occupational safety and health of young workers, and the exposure or risk of such exposure of vulnerable children to oppressive child labor, including innovative methods, techniques, and approaches for preventing oppressive child labor, research relevant to strategic enforcement of the child labor provisions of this Act, surveillance of occupational illnesses and injuries for young workers, and identification of conditions of work that are particularly hazardous to children or harmful to their health and well-being. (2) Tracking work-related injury and illness The Secretary of Health and Human Services shall, in coordination with the Secretary of Labor, develop a comprehensive plan for monitoring work-related illnesses and injuries sustained by employees under the age of 18 and for monitoring the hazards to which such employees are exposed. Such plan shall include the following: (A) Evaluation Not later than two years after the date of enactment of the Protecting Children Act and from time to time thereafter, the Secretary of Health and Human Services shall evaluate whether existing data collections capture and generate sufficient representative data on work-related illnesses and injuries sustained by employees under the age of 18. (B) Leadership The Secretary of Health and Human Services shall coordinate other Federal departments or agencies and, to the extent feasible, State agencies with data collection or research programs to enhance data collection and research on work-related illnesses and injuries sustained by employees under the age of 18. The Secretary of Health and Human Services shall advise the Secretary of Labor on the effective design and implementation of relevant elements of the statistical program of the Secretary pursuant to this Act and section 24 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 673 ). (C) Supplemental research The Secretary of Health and Human Services shall identify and from time to time undertake such additional research as the Secretary of Health and Human Services determines is necessary to supplement existing data collections, close knowledge gaps, and improve information about the work-related illnesses and injuries sustained by employees under the age of 18. (3) Hazardous occupations The Secretary of Health and Human Services shall from time to time consult with the Secretary of Labor in order to develop specific plans for such research, demonstrations, and experiments as are necessary to produce criteria enabling the Secretary to meet the Secretary\u2019s responsibility for the formulation of hazardous occupation orders under section 12. The Secretary of Health and Human Services shall, on the basis of such research, demonstrations, experiments, and any other information available, develop and publish at least annually such criteria as will effectuate the purposes of this Act. The Secretary of Health and Human Services shall submit to the Secretary all pertinent criteria regarding any such occupations or conditions or work as such criteria are developed. (4) Precautionary guidance The Secretary of Health and Human Services shall, on the basis of research, demonstrations, and experiments, and any other information available to the Secretary of Health and Human Services, develop criteria or models to aid the Secretary in identifying conditions of oppressive child labor in the absence of substantial data about occupational risks specific to children. (5) Implementation support The Secretary of Health and Human Services shall, in consultation with the Secretary of Labor, undertake research relevant to developing evidence-based guidance for the Secretary of Labor on the implementation of this Act, including topics such as strategic enforcement, effective training of employees under age 18, deterrence, and assessment of the economic benefit of noncompliance. (6) Risk of exposure to oppressive child labor The Secretary of Health and Human Services shall from time to time, acting through the Director of the National Institute for Occupational Safety and Health, consult with the leadership of relevant Federal and State agencies and programs responsible for the welfare, placement, or custody of children, in order to develop specific plans for such research, demonstrations, and experiments as are necessary to produce precautionary and evidence-based guidance enabling the Secretary of Health and Human Services and such other leaders to prevent children from suffering conditions of oppressive child labor or being exposed to the risk of oppressive child labor. (7) Authority In furtherance of the purposes of this subsection, the Secretary of Health and Human Services shall have the same authority as available to the Secretary of Health and Human Services pursuant to sections 20, 21, and 22 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 669\u2013671 ). .\n##### (c) OSH Act\nSection 20(a) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 669(a) ) is amended\u2014\n**(1)**\nin paragraph (3), by striking his work experience and inserting such employee\u2019s work experience and exposures of particular concern to the development of employees under the age of 18 ; and\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nby striking aging adults and inserting aging adults and employees under the age of 18 ; and\n**(B)**\nby adding at the end the following:\n(8) Model (A) In general Not later than the date that is one year after the date enactment of the Protecting Children Act, the Secretary of Health and Human Services shall develop a model for estimating the total incidence and economic burden of fatal and nonfatal occupational injury and illness in the United States that\u2014 (i) adjusts for known underreporting of occupational injury and illness; (ii) estimates the incidence or prevalence of occupational injuries and illnesses from public health data through attributable risk proportions or other standard methodologies, and (iii) estimates both medical and indirect costs, such as lost earnings, benefits, and home production. (B) Annual report The Secretary of Health and Human Services shall publish an annual report using the model developed under subparagraph (A) that includes\u2014 (i) estimates of the total incidence and economic burden of occupational illness and injury; (ii) the proportion of the total economic burden not absorbed by workers\u2019 compensation insurance and shifted onto Federal programs (such as the Medicare program under title XVIII of the Social Security Act, the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), and disability insurance benefits under section 223 of the Social Security Act ( 42 U.S.C. 423 )); and (iii) the incidence of occupational illness and injury by employees under the age of 18, disaggregated, to the extent feasible, by the age groups, occupational categories, and school statuses that are relevant to the administration, investigation, or enforcement of the requirements relating to child labor under sections 12 or 13(c) of the Fair Labor Standards Act of 1938. .\n#### 402. Developing a comprehensive statistical program\n##### (a) FLSA\nSection 5 of the Fair Labor Standards Act of 1938 is further amended by adding at the end the following:\n(d) Statistical programs (1) In general In order to further the purposes of this Act, the Secretary shall develop and maintain an effective program of collection, compilation, and analysis of statistics on employment practices with respect to wages, hours, child labor, and other matters of concern for this Act, including such employment practices that may constitute violations of this Act. Such statistical program shall, to the extent feasible, include demographic information about employees subject to violations under this Act and facilitate comparisons of information in such statistical program and in the statistical program established pursuant to section 24 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 673 ). (2) Authority To carry out the Secretary\u2019s duties under this subsection, the Secretary may exercise the same authority available to the Secretary under section 24 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 673 ). (3) Child labor (A) Annual report The Secretary shall, not less frequently than annually, publish a report of statistical data covering\u2014 (i) the employment of children under the age of 18, including the numbers of such children and the hours worked, the demographics of such children, in total and disaggregated by the age groups, school statuses, and occupational categories that are relevant to the administration, investigation, or enforcement of the requirements relating to child labor under sections 12 or 13(c) of the Fair Labor Standards Act of 1938; (ii) the incidence and prevalence of oppressive child labor, including the number and demographics of children affected, the industries and occupations in which oppressive child labor occurred, and the types of child labor violations, based on enforcement data and, to the extent feasible and in consultation with the Secretary of Health and Human Services, such other data as may be useful to account for underreporting and limitations of enforcement data in capturing the full incidence and prevalence of oppressive child labor; and (iii) to the extent feasible, estimates of the data described in clauses (i) and (ii) at the State level. (B) Data collection The Secretary shall periodically develop targeted surveys or other data collections relevant to determining the experience of oppressive child labor by particularly vulnerable populations, including migrant children and children in poverty. (C) Coordination The Secretary shall coordinate statistical programs across the Federal Government that collect data related to children to ensure that such programs, to the extent practicable, shall collect and report data on the employment of children, oppressive child labor, and young workers\u2019 occupational illness and injury in standardized and compatible terms. .\n##### (b) OSH\nSection 24(a) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 673(a) ) is amended by adding at the end The Secretary shall report such statistics on an annual basis. Such annual report shall include the analysis of occupational illnesses, injuries, and fatalities disaggregated (1) by relevant demographics, and (2) by the age groups that are relevant to the administration, investigation, or enforcement of the requirements relating to child labor under sections 12 or 13(c) of the Fair Labor Standards Act of 1938, across country of origin, race, and ethnicity. .\n#### 403. Enabling training and public engagement\n##### (a) FLSA\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended by inserting after section 18D ( 29 U.S.C. 218d ) the following:\n18E. Public information initiatives (a) Training and engagement The Secretary shall, directly or by grants or contracts, provide for the establishment and supervision of programs for\u2014 (1) the education and training of employers and employees in the recognition, avoidance, and prevention of violations of this Act; (2) the education and training of professionals involved in the placement, education, or delivery of other services to children on identifying and responding to oppressive child labor and incorporating into their activities knowledge about risk factors for exposing children to oppressive child labor; and (3) identification of potential violations of this Act and support for victims of such violations. (b) Child labor report The Secretary shall publish an annual report on oppressive child labor and the employment of children. Such report, which may at the Secretary\u2019s discretion be consolidated with any other report about the activities of the Secretary related to children and employment, shall include\u2014 (1) a report of the Secretary\u2019s activities during the preceding year implementing the provisions of this Act related to child labor, including the number of directed investigations; (2) trends or other relevant analysis of youth employment, oppressive child labor, and the Secretary\u2019s enforcement activities; and (3) an evaluation and appraisal of the protections against oppressive child labor established by this Act, together with the Secretary\u2019s recommendations to the Congress. (c) Enforcement disclosure The Secretary shall publish, not later than March 1 of each year, an annual statement of the capacity available to the Secretary to enforce this Act, which shall include\u2014 (1) the size of the inspectorate available in the preceding fiscal year to investigate and conduct enforcement activities pursuant to this Act; (2) the number of establishments and employees subject to the jurisdiction of this Act; (3) the ratio of inspectors to establishments and the ratio of inspectors to employees; (4) historical trends in such ratios, including a comparison of the most recent fiscal year to the years of the lowest such ratios; and (5) illustrative metrics of enforcement capacity, including the number of years necessary for the inspectorate (based on the size of the inspectorate described in paragraph (1)) to inspect every workplace in the Secretary\u2019s jurisdiction under this Act at least once. .\n##### (b) OSHA\n**(1) Annual reports**\nSection 20(d) of the Occupational Safety and Health Act ( 29 U.S.C. 669(d) ) is amended\u2014\n**(A)**\nby striking the first word and inserting the following:\nPublic information initiatives .\u2014 (1) In general Information ; and\n**(B)**\nby adding at the end the following:\n(2) Young workers The Secretary shall produce an annual report of occupational illness and injury specific to employees under the age of 18. Such report, which may at the Secretary\u2019s discretion be consolidated with any other report about the activities of the Secretary related to children and employment, shall include\u2014 (A) complaints and enforcement activities during the preceding year involving employees under the age of 18; (B) statistics about occupational illness, injury, and fatality suffered by such employees, including the distribution by age group of such illness, injury, and fatality across demographic factors such as country of origin, race, and ethnicity; (C) reasonable estimates, informed by research and in consultation with the Secretary of Health and Human Services, of the incidence and prevalence of occupational injury, illness, and fatality for such employees, accounting for such factors as underreporting and illness latency, and including occupational illness likely to manifest after childhood because of exposure to a toxic substance or harmful physical agent during childhood employment; (D) trends or other relevant analysis of the matters described in the preceding subparagraphs; and (E) an evaluation and appraisal of the protections against occupational illness, injury, and fatality provided to such employees established by this Act, together with the Secretary\u2019s recommendations to the Congress. (3) Enforcement disclosure The Secretary shall publish, not later than March 1 of each year, an annual statement of the capacity available to the Secretary to enforce this Act, including the following: (A) the size of the inspectorate available in the preceding fiscal year to investigate and conduct enforcement activities pursuant to this Act; (B) the number of establishments and employees subject to the jurisdiction of this Act; (C) the ratio of inspectors to establishments and the ratio of inspectors to employees; (D) historical trends in such ratios, including a comparison of the most recent fiscal year to the years of the lowest such ratios; (E) to the extent feasible, such ratios for the State plans; and (F) illustrative metrics of enforcement capacity, including the number of years necessary for the inspectorate (based on the size of the inspectorate described in paragraph (1)) to inspect every workplace in the Secretary\u2019s jurisdiction under this Act at least once. .\n**(2) Training and employee education**\nSection 21 of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 670 ) is amended by adding at the end the following:\n(e) Effective training pedagogy The Secretary of Health and Human Services shall, directly or by grant or contract, periodically undertake research, demonstrations, experiments, and surveys relevant to the effective design and delivery of safety and health training, education, and information targeted to employees under the age of 18 and employers of such employees. .",
      "versionDate": "2025-06-12",
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
        "name": "Labor and Employment",
        "updateDate": "2025-07-08T13:43:27Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3997ih.xml"
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
      "title": "Protecting Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect children from oppressive child labor and unsafe workplaces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T04:48:30Z"
    }
  ]
}
```
