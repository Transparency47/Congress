# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1710?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1710
- Title: MIL FMLA Act
- Congress: 119
- Bill type: S
- Bill number: 1710
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2026-01-21T06:56:32Z
- Update date including text: 2026-01-21T06:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1710",
    "number": "1710",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "MIL FMLA Act",
    "type": "S",
    "updateDate": "2026-01-21T06:56:32Z",
    "updateDateIncludingText": "2026-01-21T06:56:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
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
      "actionDate": "2025-05-12",
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
          "date": "2025-05-12T20:17:12Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "CT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MD"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1710is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1710\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Ms. Duckworth (for herself, Ms. Klobuchar , Mr. Blumenthal , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo improve family and medical leave for military families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making It Likely for Families of the Military to Live with Leave Access Act or the MIL FMLA Act .\nI\nAmendments to Family and Medical Leave Act of 1993\n#### 101. Definitions\nSection 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 ) is amended\u2014\n**(1)**\nin paragraph (7), by striking employee each place it appears and inserting employee or covered servicemember ;\n**(2)**\nby amending paragraph (12) to read as follows:\n(12) Son or daughter (A) In general Subject to subparagraph (B), the term son or daughter means a biological, adopted, or foster child, a stepchild, a legal ward, or a child of a person standing in loco parentis, who is\u2014 (i) under 18 years of age; or (ii) 18 years of age or older and incapable of self-care because of a mental or physical disability. (B) Servicemember and veteran leave For the purposes of leave under paragraphs (1)(E) and (3) of section 102(a), the term son or daughter means, regardless of age, a biological, adopted, or foster child, a stepchild, a legal ward, a child of a person standing in loco parentis, or the child of a covered servicemember\u2019s domestic partner. ;\n**(3)**\nin paragraph (14), by amending subparagraph (B) to read as follows:\n(B) in the case of a member of a reserve component of the Armed Forces\u2014 (i) duty during the deployment of the member with the Armed Forces under a call or order to active duty under a provision of law referred to in section 101(a)(13)(B) of title 10, United States Code; (ii) duty pursuant to title 32, United States Code; or (iii) covered State active duty. ;\n**(4)**\nin paragraph (15)(B), by striking and who was a member of the Armed Forces and all that follows through the period at the end of the subparagraph and inserting a period;\n**(5)**\nin paragraph (18)\u2014\n**(A)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking at any time during a period described in paragraph (15)(B) ; and\n**(ii)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) in the case of either a member of the Armed Forces (including a member of the National Guard or Reserves), or a veteran who was such a member, a serious health condition that was incurred by the member in line of duty on active duty in the Armed Forces (or existed before the beginning of the member\u2019s active duty and was aggravated by service in line of duty on active duty in the Armed Forces). .\n**(6)**\nby adding at the end the following:\n(20) Any other individual whose close association is the equivalent of a family relationship The term any other individual whose close association is the equivalent of a family relationship , used with respect to a covered servicemember, means any person with whom the covered servicemember has a significant personal bond that is or is like a family relationship, regardless of biological or legal relationship. (21) Domestic partner The term domestic partner , used with respect to an employee or covered servicemember, means an adult in a committed relationship with the employee or covered servicemember, including same-sex and opposite-sex relationships. (22) Grandchild The term grandchild , used with respect to a covered servicemember, means the son or daughter of the covered servicemember. (23) Grandparent The term grandparent , used with respect to a covered servicemember, means a parent of a parent of the covered servicemember. (24) Nephew; niece The terms nephew and niece , used with respect to a covered servicemember, mean a son or daughter of the sibling of the covered servicemember. (25) Parent-in-law The term parent-in-law , used with respect to a covered servicemember, means a parent of the spouse or domestic partner of the covered servicemember. (26) Sibling The term sibling , used with respect to a covered servicemember, means any person who is a son or daughter of parent of the covered servicemember (other than the covered servicemember). (27) Son-in-law; daughter-in-law The terms son-in-law and daughter-in-law , used with respect to a covered servicemember, mean any person who is a spouse or domestic partner of a son or daughter, as the case may be, of the covered servicemember. (28) Uncle; aunt The terms uncle and aunt , used with respect to a covered servicemember, mean the son or daughter, as the case may be, of the grandparent of the covered servicemember (other than the parent of the covered servicemember). (29) Covered State active duty The term covered State active duty means State active duty for a period of 14 days or more, State active duty in response to a national emergency declared by the President under the National Emergencies Act ( 50 U.S.C. 1601 et seq. ), or State active duty in response to a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ). (30) State active duty The term State active duty has the same meaning given the term in section 4303(15) of title 38, United States Code. .\n#### 102. Leave requirement\n##### (a) In General\nSection 102(a) of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2612(a) ) is amended\u2014\n**(1)**\nin paragraph (1)(E), by inserting or domestic partner after spouse ;\n**(2)**\nby amending paragraph (3) to read as follows:\n(3) Servicemember family leave Notwithstanding paragraph (1) and subject to section 103, an eligible employee who is the spouse or domestic partner, son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, sibling, uncle or aunt, nephew or niece, or next of kin of a covered servicemember, or any other individual whose close association is the equivalent of a family relationship with a covered servicemember, shall be entitled to a total of 26 workweeks of leave during a 12-month period to care for the servicemember. ;\n**(3)**\nby amending paragraph (4) to read as follows:\n(4) Combined leave total Subject to subsection (d)(3), an eligible employee shall be entitled to not more than a combined total of 26 workweeks of leave under paragraphs (1), (3), and (6) during any 12-month period. ; and\n**(4)**\nby adding at the end the following:\n(6) Veteran leave Notwithstanding paragraph (1) and subject to section 103, an eligible employee who is a covered servicemember described in section 101(15)(B) shall be entitled to a total of 26 workweeks of leave during a 12-month period because of a serious injury or illness that makes the employee unable to perform the functions of the position of such employee. .\n##### (b) Leave Taken Intermittently or on a Reduced Leave Schedule\n**(1) In general**\nSection 102(b)(1) of such Act ( 29 U.S.C. 2612(b)(1) ) is amended by striking subsection (a)(3) and inserting paragraph (3) or (6) of subsection (a) .\n**(2) Alternative position**\nSection 102(b)(2) of such Act ( 29 U.S.C. 2612(b)(2) ) is amended by striking subsection (a)(3) and inserting paragraph (3) or (6) of subsection (a) .\n##### (c) Relationship to paid leave\nSection 102(d) of such Act ( 29 U.S.C. 2612(d) ) is amended\u2014\n**(1)**\nin paragraph (1) by striking under subsection (a)(3)) and inserting under paragraph (3) or (6) of subsection (a)) ; and\n**(2)**\nin paragraph (2)(B), by striking subsection (a)(3) and inserting paragraph (3) or (6) of subsection (a) .\n##### (d) Notice\nSection 102(e) of such Act ( 29 U.S.C. 2612(e) ) is amended by adding at the end the following:\n(4) Notice for veteran leave In any case in which the necessity for leave under subsection (a)(6) is foreseeable, the employee shall provide such notice to the employer as is reasonable and practicable. .\n##### (e) Certification\nSection 103(a) of such Act ( 29 U.S.C. 2613(a) ) is amended by inserting or (6) after paragraph (3) .\n##### (f) Maintenance of health benefits\nSection 104(c) of such Act ( 29 U.S.C. 2614(c) ) is amended\u2014\n**(1)**\nin paragraph (2)(B)(i)\u2014\n**(A)**\nby inserting or a serious injury or illness, as the case may be, after serious health condition ; and\n**(B)**\nby striking section 102(a)(3) and inserting paragraph (3) or (6) of section 102(a) ; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (ii), by striking or ;\n**(ii)**\nin clause (iii), by striking the period at the end and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(iv) a certification issued by the health care provider of the eligible employee, in the case of an employee unable to return to work because of a serious injury or illness specified in section 102(a)(6). ; and\n**(B)**\nin subparagraph (C), by adding at the end the following:\n(iii) Leave due to a serious injury or illness of employee The certification described in subparagraph (A)(iv) shall be sufficient if the certification states that a serious injury or illness prevented the employee from being able to perform the functions of the position of the employee on the date that the leave of the employee expired. (iv) Leave due to a serious injury or illness of a family member who is a servicemember The certification described in subparagraph (A)(i) shall be sufficient if the certification states that the employee is needed to care for covered servicemember on the date that the leave of the employee expired. .\n##### (g) Enforcement\nSection 107(a)(1)(A)(i)(II) of such Act ( 29 U.S.C. 2617(a)(1)(A)(i)(II) ) is amended by striking section 102(a)(3) and inserting paragraph (3) or (6) of section 102(a) .\nII\nFederal Civilian Employees\n#### 201. Employees covered by title 5, United States Code\n##### (a) Definitions\nSection 6381 of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by striking employee each place it appears and inserting employee or covered servicemember ;\n**(2)**\nby striking paragraphs (6) and (7) and inserting the following:\n(6) the term son or daughter means a biological, adopted, or foster child, a stepchild, a legal ward, or a child of a person standing in loco parentis\u2014 (A) who is\u2014 (i) under 18 years of age; or (ii) 18 years of age or older and incapable of self-care because of a mental or physical disability; or (B) for the purposes of leave under section 6382(a)(1)(e) or section 6382(a)(3)(A), includes (regardless of age) any child, stepchild, legal ward, or child of a person standing in loco parentis; (7) the term covered active duty means\u2014 (A) in the case of a member of a regular component of the Armed Forces, duty during the deployment of the member with the Armed Forces to a foreign country; and (B) in the case of a member of a reserve component of the Armed Forces\u2014 (i) duty during the deployment of the member with the Armed Forces under a call or order to active duty under a provision of law referred to in section 101(a)(13)(B) of title 10; (ii) duty pursuant to title 32; or (iii) State active duty (defined for purposes of this clause as having the meaning of such term in section 4303(15) of title 38) for a period of 14 days or more, State active duty in response to a national emergency declared by the President under the National Emergencies Act ( 50 U.S.C. 1601 et seq. ), or State active duty in response to a major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ); ;\n**(3)**\nin paragraph (8)(B), by striking and who was through therapy; and inserting a semicolon;\n**(4)**\nin paragraph (11)\u2014\n**(A)**\nby striking and at the end of subparagraph (A);\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking at any time during a period described in paragraph (8)(B) ; and\n**(ii)**\nby striking and at the end; and\n**(C)**\nby inserting after subparagraph (B) the following:\n(C) in the case of either a member of the Armed Forces (including a member of the National Guard or Reserves), or a veteran who was such a member, a serious health condition that was incurred by the member in line of duty on active duty in the Armed Forces (or existed before the beginning of the member\u2019s active duty and was aggravated by service in line of duty on active duty in the Armed Forces); ;\n**(5)**\nin paragraph (12), by striking the period at the end and inserting ; and ; and\n**(6)**\nby adding at the end the following:\n(13) the term spouse , used with respect to an employee for leave under section 6382(a)(1)(E), includes a domestic partner (defined as an adult in a committed relationship with another adult, including same-sex and opposite-sex relationships). .\n##### (b) Servicemember care and veteran leave\nSection 6382 of title 5, United States Code, is amended\u2014\n**(1)**\nby striking subsection (a)(3) and inserting the following:\n(3) (A) Subject to section 6383, an employee who is the spouse, son or daughter, son-in-law or daughter-in-law, parent, parent-in-law, grandparent, sibling, uncle or aunt, nephew or niece, or next of kin of a covered servicemember, or any other individual whose close association is the equivalent of a family relationship with a covered servicemember, shall be entitled to a total of 26 workweeks of leave during a 12-month period to care for the servicemember. (B) Subject to section 6383, an employee who is a covered servicemember shall be entitled to a total of 26 workweeks of leave during a 12-month period because of a serious injury or illness that makes the employee unable to perform the functions of the position of such employee. (C) For the purposes of subparagraph (A), the following definitions apply: (i) Any other individual whose close association is the equivalent of a family relationship The term any other individual whose close association is the equivalent of a family relationship , used with respect to a covered servicemember, means any person with whom the covered servicemember has a significant personal bond that is or is like a family relationship, regardless of biological or legal relationship. (ii) Grandchild The term grandchild , used with respect to a covered servicemember, means the son or daughter of the covered servicemember. (iii) Grandparent The term grandparent , used with respect to a covered servicemember, means a parent of a parent of the covered servicemember. (iv) Nephew; niece The terms nephew and niece , used with respect to a covered servicemember, mean a son or daughter of the sibling of the covered servicemember. (v) Parent-in-law The term parent-in-law , used with respect to a covered servicemember, means a parent of the spouse or domestic partner of the covered servicemember. (vi) Sibling The term sibling , used with respect to a covered servicemember, means any person who is a son or daughter of parent of the covered servicemember (other than the covered servicemember). (vii) Son-in-law; daughter-in-law The terms son-in-law and daughter-in-law , used with respect to a covered servicemember, mean any person who is a spouse or domestic partner of a son or daughter, as the case may be, of the covered servicemember. (viii) Uncle; aunt The terms uncle and aunt , used with respect to a covered servicemember, mean the son or daughter, as the case may be, of the grandparent of the covered servicemember (other than the parent of the covered servicemember). ; and\n**(2)**\nin subsection (e), by adding at the end the following:\n(4) In any case in which the necessity for leave under subsection (a)(3)(B) is foreseeable, the employee shall provide such notice to the employer as is reasonable and practicable. .\n##### (c) Certification\nSection 6383 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking subparagraph (C) or (D) of section 6382(a)(1) and inserting subparagraph (C) or (D) of paragraph (1) of section 6382(a) or subparagraph (A) or (B) of paragraph (3) of such section ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting or serious injury or illness, as the case may be, after serious health condition ; and\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby striking section 6382(a)(1)(C) and inserting paragraph (1)(C) or paragraph (3)(A) of section 6382(a) ; and\n**(II)**\nby inserting covered servicemember, before son in each place it appears; and\n**(ii)**\nin subparagraph (B), by striking section 6382(a)(1)(D) and inserting paragraph (1)(D) or paragraph (3)(B) of section 6382(a) .",
      "versionDate": "2025-05-12",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on Oversight and Government Reform, and House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MIL FMLA Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-11T14:52:29Z"
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
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1710is.xml"
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
      "title": "MIL FMLA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T10:58:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MIL FMLA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making It Likely for Families of the Military to Live with Leave Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve family and medical leave for military families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:21Z"
    }
  ]
}
```
