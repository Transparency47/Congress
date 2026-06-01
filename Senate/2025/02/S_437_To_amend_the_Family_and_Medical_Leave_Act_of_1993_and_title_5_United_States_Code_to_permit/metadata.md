# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/437
- Title: Caring for All Families Act
- Congress: 119
- Bill type: S
- Bill number: 437
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-03-17T11:03:20Z
- Update date including text: 2026-03-17T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S668-671)
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S668-671)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/437",
    "number": "437",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Caring for All Families Act",
    "type": "S",
    "updateDate": "2026-03-17T11:03:20Z",
    "updateDateIncludingText": "2026-03-17T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S668-671)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
            "date": "2025-02-06T00:21:03Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T00:21:03Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "VT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MN"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s437is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 437\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Durbin (for himself, Mr. Hickenlooper , Mrs. Gillibrand , Mr. Merkley , Mr. Blumenthal , Mr. Welch , Ms. Smith , Mrs. Murray , Mr. Padilla , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Family and Medical Leave Act of 1993 and title 5, United States Code, to permit leave to care for a domestic partner, parent-in-law, or adult child, or another related individual, who has a serious health condition, and to allow employees to take, as additional leave, parental involvement and family wellness leave to participate in or attend their children\u2019s and grandchildren\u2019s educational and extracurricular activities or meet family care needs.\n#### 1. Short title\nThis Act may be cited as the Caring for All Families Act .\n#### 2. Leave to care for a domestic partner, son-in-law, daughter-in-law, parent-in-law, adult child, grandparent, grandchild, or sibling of the employee, or another related individual\n##### (a) Definitions\n**(1) Inclusion of related individuals**\nSection 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 ) is amended by adding at the end the following:\n(20) Any other individual whose close association is the equivalent of a family relationship The term any other individual whose close association is the equivalent of a family relationship , used with respect to an employee or a covered servicemember, means any person with whom the employee or covered servicemember, as the case may be, has a significant personal bond that is or is like a family relationship, regardless of biological or legal relationship. (21) Domestic partner The term domestic partner , used with respect to an employee or a covered servicemember, means\u2014 (A) the person recognized as the domestic partner of the employee or covered servicemember under any domestic partnership or civil union law of a State or political subdivision of a State; or (B) in the case of an unmarried employee or covered servicemember, an unmarried adult person who is in a committed, personal relationship with the employee or covered servicemember, is not a domestic partner as described in subparagraph (A) to or in such a relationship with any other person, and who is designated to the employer by such employee or covered service member as the domestic partner of that employee or covered servicemember. (22) Grandchild The term grandchild , used with respect to an employee or a covered servicemember, means the son or daughter of a son or daughter of the employee or covered service member. (23) Grandparent The term grandparent , used with respect to an employee or a covered servicemember, means a parent of a parent of the employee or covered service member. (24) Nephew; niece The terms nephew and niece , used with respect to an employee or a covered servicemember, mean a son or daughter of the sibling of the employee or covered service member. (25) Parent-in-law The term parent-in-law , used with respect to an employee or a covered servicemember, means a parent of the spouse or domestic partner of the employee or covered service member. (26) Sibling The term sibling , used with respect to an employee or a covered servicemember, means any person who is a son or daughter of parent of the employee or covered service member (other than the employee or covered servicemember). (27) Son-in-law; daughter-in-law The terms son-in-law and daughter-in-law , used with respect to an employee or a covered servicemember, mean any person who is a spouse or domestic partner of a son or daughter, as the case may be, of the employee or covered service member. (28) Uncle; Aunt The terms uncle and aunt , used with respect to an employee or a covered servicemember, mean the son or daughter, as the case may be, of the grandparent of the employee or covered servicemember (other than the parent of the employee or covered service member). .\n**(2) Inclusion of adult children and children of a domestic partner**\nSection 101(12) of such Act ( 29 U.S.C. 2611(12) ) is amended\u2014\n**(A)**\nby inserting a child of an individual\u2019s domestic partner, after a legal ward, ; and\n**(B)**\nby striking who is\u2014 and all that follows and inserting and includes an adult child. .\n##### (b) Leave Requirement\nSection 102 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (C), by striking spouse, or a son, daughter, or parent, of the employee, if such spouse, son, daughter, or parent and inserting spouse or domestic partner, or a son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, if such spouse, domestic partner, son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece, or such other individual ; and\n**(ii)**\nin subparagraph (E), by striking spouse, or a son, daughter, or parent of the employee and inserting spouse or domestic partner, or a son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee ; and\n**(B)**\nin paragraph (3), by striking spouse, son, daughter, parent, or next of kin of a covered servicemember and inserting spouse or domestic partner, son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, sibling, uncle or aunt, nephew or niece, or next of kin of a covered servicemember, or any other individual whose close association is the equivalent of a family relationship with the covered servicemember ;\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)(A), by striking son, daughter, spouse, parent, or covered servicemember of the employee, as appropriate and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, nephew or niece, or covered servicemember of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate ; and\n**(B)**\nin paragraph (3), by striking spouse, or a son, daughter, or parent, of the employee and inserting spouse or domestic partner, or a son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate, ; and\n**(3)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting , or domestic partners, after husband and wife ; and\n**(ii)**\nin subparagraph (B), by inserting or parent-in-law after parent ; and\n**(B)**\nin paragraph (2), by inserting , or those domestic partners, after husband and wife each place it appears.\n##### (c) Certification\nSection 103 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2613 ) is amended\u2014\n**(1)**\nin subsection (a), by striking son, daughter, spouse, or parent of the employee, or of the next of kin of an individual in the case of leave taken under such paragraph (3), as appropriate and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or the next of kin of an individual, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (4)(A), by striking son, daughter, spouse, or parent and an estimate of the amount of time that such employee is needed to care for the son, daughter, spouse, or parent and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate, and an estimate of the amount of time that such employee is needed to care for such son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece, or such other individual ; and\n**(B)**\nin paragraph (7), by striking son, daughter, parent, or spouse who has a serious health condition, or will assist in their recovery, and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece, with a serious health condition, of the employee, or an individual, with a serious health condition, who is any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate, or will assist in the recovery, .\n##### (d) Employment and Benefits Protection\nSection 104(c)(3) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2614(c)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A)(i), by striking son, daughter, spouse, or parent of the employee, as appropriate, and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate, ; and\n**(2)**\nin subparagraph (C)(ii), by striking son, daughter, spouse, or parent and inserting employee's son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece, or (with relation to the employee) any other individual whose close association is the equivalent of a family relationship, as appropriate, .\n#### 3. Leave to care for a domestic partner, son-in-law, daughter-in-law, parent-in-law, adult child, grandparent, grandchild, or sibling of the employee, or another related individual for Federal employees\n##### (a) Definitions\n**(1) Inclusion of a domestic partner, son-in-law, daughter-in-law, parent-in-law, adult child, grandparent, grandchild, or sibling of the employee, or another individual whose close association is the equivalent of a family relationship**\nSection 6381 of title 5, United States Code, is amended\u2014\n**(A)**\nin paragraph (11) by striking ; and and inserting a semicolon;\n**(B)**\nin paragraph (12), by striking the period and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(13) the term any other individual whose close association is the equivalent of a family relationship , used with respect to an employee or a covered servicemember, means any person with whom the employee or covered servicemember, as the case may be, has a significant personal bond that is or is like a family relationship, regardless of biological or legal relationship; (14) the term domestic partner , used with respect to an employee or a covered servicemember, means\u2014 (A) the person recognized as the domestic partner of the employee or covered servicemember under any domestic partnership or civil union law of a State or political subdivision of a State; or (B) in the case of an unmarried employee or covered servicemember, an unmarried adult person who is in a committed, personal relationship with the employee or covered servicemember, is not a domestic partner as described in subparagraph (A) to or in such a relationship with any other person, and who is designated to the employing agency by such employee or covered service member as the domestic partner of that employee or covered servicemember; (15) the term grandchild , used with respect to an employee or a covered servicemember, means the son or daughter of a son or daughter of the employee or covered service member; (16) the term grandparent , used with respect to an employee or a covered servicemember, means a parent of a parent of the employee or covered service member; (17) the terms nephew and niece , used with respect to an employee or a covered servicemember, mean a son or daughter of the sibling of the employee or covered service member; (18) the term parent-in-law , used with respect to an employee or a covered servicemember, means a parent of the spouse or domestic partner of the employee or covered service member; (19) the term sibling , used with respect to an employee or a covered servicemember, means any person who is a son or daughter of parent of the employee or covered service member (other than the employee or covered servicemember); (20) the terms son-in-law and daughter-in-law , used with respect to an employee or a covered servicemember, mean any person who is a spouse or domestic partner of a son or daughter, as the case may be, of the employee or covered service member; (21) the term State has the same meaning given the term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ); and (22) terms uncle and aunt , used with respect to an employee or a covered servicemember, mean the son or daughter, as the case may be, of the grandparent of the employee or covered servicemember (other than the parent of the employee or covered service member). .\n**(2) Inclusion of adult children and children of a domestic partner**\nSection 6381(6) of such title is amended\u2014\n**(A)**\nby inserting a child of an individual\u2019s domestic partner, after a legal ward, ; and\n**(B)**\nby striking who is\u2014 and all that follows and inserting and includes an adult child .\n##### (b) Leave Requirement\nSection 6382 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (C), by striking spouse, or a son, daughter, or parent, of the employee, if such spouse, son, daughter, or parent and inserting spouse or domestic partner, or a son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association with the employee is the equivalent of a family relationship, if such spouse, domestic partner, son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece, or such other individual ; and\n**(ii)**\nin subparagraph (E), by striking spouse, or a son, daughter, or parent of the employee and inserting spouse or domestic partner, or a son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee ; and\n**(B)**\nin paragraph (3), by striking spouse, son, daughter, parent, or next of kin of a covered servicemember and inserting spouse or domestic partner, son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, sibling, uncle or aunt, nephew or niece, or next of kin of a covered servicemember, or any other individual whose close association is the equivalent of a family relationship with the covered servicemember ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)(A), by striking son, daughter, spouse, parent, or covered servicemember of the employee, as appropriate and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, nephew or niece, or covered servicemember of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate ; and\n**(B)**\nin paragraph (3), by striking spouse, or a son, daughter, or parent, of the employee and inserting spouse or domestic partner, or a son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate, .\n##### (c) Certification\nSection 6383 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking son, daughter, spouse, or parent of the employee, as appropriate and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate ; and\n**(2)**\nin subsection (b)(4)(A), by striking son, daughter, spouse, or parent, and an estimate of the amount of time that such employee is needed to care for such son, daughter, spouse, or parent and inserting son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece of the employee, or any other individual whose close association is the equivalent of a family relationship with the employee, as appropriate, and an estimate of the amount of time that such employee is needed to care for such son or daughter, son-in-law or daughter-in-law, spouse or domestic partner, parent, parent-in-law, grandparent, grandchild, sibling, uncle or aunt, or nephew or niece, or such other individual .\n#### 4. Entitlement to additional leave under the FMLA for parental involvement and family wellness\n##### (a) Leave requirement\nSection 102(a) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a) ), as amended by section 2(b), is further amended\u2014\n**(1)**\nby redesignating paragraph (5) as paragraph (6); and\n**(2)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Entitlement to additional leave for parental involvement and family wellness (A) In general Subject to subparagraph (B) and section 103(g), an eligible employee shall be entitled to leave under this paragraph to\u2014 (i) participate in or attend an activity that is sponsored by a school or community organization and relates to a program of the school or organization that is attended by a son or daughter or a grandchild of the employee; or (ii) meet routine family medical care needs (including by attending medical and dental appointments of the employee or a son or daughter, spouse or domestic partner, or grandchild of the employee) or attend to the care needs of an elderly individual who is any other individual whose close association is the equivalent of a family relationship with the employee (including by making visits to nursing homes or group homes). (B) Limitations (i) In general An eligible employee shall be entitled to\u2014 (I) not to exceed 4 hours of leave under this paragraph during any 30-day period; and (II) not to exceed 24 hours of leave under this paragraph during any 12-month period described in paragraph (4). (ii) Coordination rule Leave under this paragraph shall be in addition to any leave provided under any other paragraph of this subsection. (C) Definitions As used in this paragraph: (i) Community organization The term community organization means a private nonprofit organization that is representative of a community or a significant segment of a community and provides activities for individuals described in section 101(12), such as a scouting or sports organization. (ii) School The term school means an elementary school or secondary school (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )), a Head Start program assisted under the Head Start Act ( 42 U.S.C. 9831 et seq. ), and a child care facility licensed under State law. .\n##### (b) Schedule\nSection 102(b)(1) of such Act ( 29 U.S.C. 2612(b)(1) ) is amended by inserting after the third sentence the following new sentence: Subject to subsection (e)(4) and section 103(g), leave under subsection (a)(5) may be taken intermittently or on a reduced leave schedule. .\n##### (c) Substitution of paid leave\nSection 102(d)(2) of such Act ( 29 U.S.C. 2612(d)(2) ) is amended by adding at the end the following new subparagraph:\n(C) Parental involvement leave and family wellness leave (i) Vacation leave; personal leave; family leave An eligible employee may elect, or an employer may require the employee, to substitute any of the accrued paid vacation leave, personal leave, or family leave of the employee for any part of the period of leave under subsection (a)(5). (ii) Medical or sick leave An eligible employee may elect, or an employer may require the employee, to substitute any of the accrued paid medical or sick leave of the employee for any part of the period of leave provided under clause (ii) of subsection (a)(5)(A), except that nothing in this title shall require an employer to provide paid sick leave or paid medical leave in any situation in which such employer would not normally provide any such paid leave. (iii) Prohibition on restrictions and limitations If the employee elects or the employer requires the substitution of accrued paid leave for leave under subsection (a)(5), the employer shall not restrict or limit the leave that may be substituted or impose any additional terms and conditions on the substitution of such leave that are more stringent for the employee than the terms and conditions set forth in this Act. .\n##### (d) Notice\nSection 102(e) of such Act ( 29 U.S.C. 2612(e) ), as amended by section 2(b), is further amended by adding at the end the following new paragraph:\n(4) Notice relating to parental involvement and family wellness leave In any case in which an employee requests leave under paragraph (5) of subsection (a), the employee shall\u2014 (A) provide the employer with not less than 7 days\u2019 notice, or (if such notice is impracticable) such notice as is practicable, before the date the leave is to begin, of the employee\u2019s intention to take leave under such paragraph; and (B) in the case of leave to be taken under subsection (a)(5)(A)(ii), make a reasonable effort to schedule the activity or care involved so as not to disrupt unduly the operations of the employer, subject to the approval of the health care provider involved (if any). .\n##### (e) Certification\nSection 103 of such Act ( 29 U.S.C. 2613 ) is amended by adding at the end the following new subsection:\n(g) Certification related to parental involvement and family wellness leave An employer may require that a request for leave under section 102(a)(5) be supported by a certification issued at such time and in such manner as the Secretary may by regulation prescribe. .\n#### 5. Entitlement of Federal employees to leave for parental involvement and family wellness\n##### (a) Leave requirement\nSection 6382(a) of title 5, United States Code, as amended by section 3(b), is further amended by adding at the end the following new paragraph:\n(5) (A) Subject to subparagraph (B) and section 6383(f), an employee shall be entitled to leave under this paragraph to\u2014 (i) participate in or attend an activity that is sponsored by a school or community organization and relates to a program of the school or organization that is attended by a son or daughter or a grandchild of the employee; or (ii) meet routine family medical care needs (including by attending medical and dental appointments of the employee or a son or daughter, spouse or domestic partner, or grandchild of the employee) or to attend to the care needs of an elderly individual who is any other individual whose close association is the equivalent of a family relationship with the employee (including by making visits to nursing homes and group homes). (B) (i) An employee is entitled to\u2014 (I) not to exceed 4 hours of leave under this paragraph during any 30-day period; and (II) not to exceed 24 hours of leave under this paragraph during any 12-month period described in paragraph (4). (ii) Leave under this paragraph shall be in addition to any leave provided under any other paragraph of this subsection. (C) For the purpose of this paragraph\u2014 (i) the term community organization means a private nonprofit organization that is representative of a community or a significant segment of a community and provides activities for individuals described in section 6381(6), such as a scouting or sports organization; and (ii) the term school means an elementary school or secondary school (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )), a Head Start program assisted under the Head Start Act ( 42 U.S.C. 9831 et seq. ), and a child care facility licensed under State law. .\n##### (b) Schedule\nSection 6382(b)(1) of such title is amended\u2014\n**(1)**\nby inserting after the third sentence the following new sentence: Subject to subsection (e)(4) and section 6383(f), leave under subsection (a)(5) may be taken intermittently or on a reduced leave schedule. ; and\n**(2)**\nin the last sentence, by striking involved, and inserting involved (or, in the case of leave under subsection (a)(5), for purposes of the 30-day or 12-month period involved), .\n##### (c) Substitution of paid leave\nSection 6382(d) of such title is amended by adding at the end the following:\n(3) An employee may elect to substitute for any part of the period of leave under subsection (a)(5), any of the employee\u2019s accrued or accumulated annual or sick leave. If the employee elects the substitution of that accrued or accumulated annual or sick leave for leave under subsection (a)(5), the employing agency shall not restrict or limit the leave that may be substituted or impose any additional terms and conditions on the substitution of such leave that are more stringent for the employee than the terms and conditions set forth in this subchapter. .\n##### (d) Notice\nSection 6382(e) of such title, as amended by section 3(b)(2), is further amended by adding at the end the following new paragraph:\n(4) In any case in which an employee requests leave under paragraph (5) of subsection (a), the employee shall\u2014 (A) provide the employing agency with not less than 7 days\u2019 notice, or (if such notice is impracticable) such notice as is practicable, before the date the leave is to begin, of the employee\u2019s intention to take leave under such paragraph; and (B) in the case of leave to be taken under subsection (a)(5)(A)(ii), make a reasonable effort to schedule the activity or care involved so as not to disrupt unduly the operations of the employing agency, subject to the approval of the health care provider involved (if any). .\n##### (e) Certification\nSection 6383(f) of such title is amended by striking paragraph (1)(E) or (3) of and inserting paragraph (1)(E), (3) or (5) of .",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Oversight and Government Reform, and House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1002",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Caring for All Families Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aging",
            "updateDate": "2025-04-15T14:05:27Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-04-15T14:05:27Z"
          },
          {
            "name": "Employee leave",
            "updateDate": "2025-04-15T14:05:27Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-04-15T14:05:27Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-15T14:05:27Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-04-15T14:05:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-12T16:28:16Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s437is.xml"
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
      "title": "Caring for All Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Family and Medical Leave Act of 1993 and title 5, United States Code, to permit leave to care for a domestic partner, parent-in-law, or adult child, or another related individual, who has a serious health condition, and to allow employees to take, as additional leave, parental involvement and family wellness leave to participate in or attend their children's and grand children's educational and extracurricular activities or meet family care needs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Caring for All Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
