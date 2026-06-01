# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/292
- Title: Educational Choice for Children Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 292
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-05T21:33:50Z
- Update date including text: 2025-12-05T21:33:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/292",
    "number": "292",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Educational Choice for Children Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:33:50Z",
    "updateDateIncludingText": "2025-12-05T21:33:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T17:36:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TX"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SD"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MS"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AR"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "LA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WV"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ID"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WY"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NC"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "IN"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MO"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "PA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "ND"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NE"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "OH"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "TN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WV"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "IN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AR"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "SC"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s292is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 292\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Cassidy (for himself, Mr. Scott of South Carolina , Mr. Cornyn , Mr. Daines , Mr. Thune , Mrs. Hyde-Smith , Mr. Schmitt , Mr. Sheehy , Mr. Budd , Mr. Cotton , Mr. Kennedy , Mr. Tuberville , Mr. Justice , Mr. Risch , Mr. Barrasso , Mr. Tillis , Mr. Marshall , Mr. Young , Mr. Hawley , Mrs. Britt , Mrs. Blackburn , Mr. McCormick , Mr. Cramer , Mr. Wicker , Ms. Lummis , Mr. Ricketts , and Mr. Husted ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing education scholarships to qualified elementary and secondary students.\n#### 1. Short title\nThis Act may be cited as the Educational Choice for Children Act of 2025 .\n#### 2. Tax credit for contributions to scholarship granting organizations\n##### (a) Credit for individuals\n**(1) In general**\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Qualified elementary and secondary education scholarships (a) Allowance of credit In the case of an individual who is a citizen or resident of the United States (as defined in section 7701(a)(9)), there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the aggregate amount of qualified contributions made by the taxpayer during the taxable year. (b) Limitations (1) In general The credit allowed under subsection (a) to any taxpayer for any taxable year shall not exceed an amount equal to the greater of\u2014 (A) 10 percent of the adjusted gross income of the taxpayer for the taxable year, or (B) $5,000. (2) Allocation of volume cap The credit allowed under subsection (a) to any taxpayer for any taxable year shall not exceed the amount of the volume cap allocated by the Secretary to such taxpayer under section 3 of the Educational Choice for Children Act of 2025 with respect to qualified contributions made by the taxpayer during the taxable year. (3) Reduction based on State credit The amount allowed as a credit under subsection (a) for a taxable year shall be reduced by the amount allowed as a credit on any State tax return of the taxpayer for qualified contributions made by the taxpayer during the taxable year. (c) Definitions For purposes of this section\u2014 (1) Eligible student The term eligible student means an individual who\u2014 (A) is a member of a household with an income which is not greater than 300 percent of the area median gross income (as such term is used in section 42), and (B) is eligible to enroll in a public elementary or secondary school. (2) Qualified contribution The term qualified contribution means a charitable contribution (as defined by section 170(c)) to a scholarship granting organization in the form of cash or marketable securities. (3) Qualified elementary or secondary education expense The term qualified elementary or secondary education expense means the following expenses in connection with enrollment or attendance at, or for students enrolled at or attending, a public or private elementary or secondary school (including a religious elementary or secondary school): (A) Tuition. (B) Curricula and curricular materials. (C) Books or other instructional materials. (D) Online educational materials. (E) Tuition for tutoring or educational classes outside of the home, including at a tutoring facility, but only if the tutor or instructor is not related to the student and\u2014 (i) is licensed as a teacher in any State, (ii) has taught at\u2014 (I) a public or private elementary or secondary school, or (II) an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) )), or (iii) is a subject matter expert in the relevant subject. (F) Fees for a nationally standardized norm-referenced achievement test, an advanced placement examination, or any examinations related to admission to an institution of higher education. (G) Fees for dual enrollment in an institution of higher education. (H) Educational therapies for students with disabilities provided by a licensed or accredited practitioner or provider, including occupational, behavioral, physical, and speech-language therapies. Such term shall include expenses for the purposes described in subparagraphs (A) through (H) in connection with a home school (whether treated as a home school or a private school for purposes of applicable State law). (4) Scholarship granting organization The term scholarship granting organization means any organization\u2014 (A) which\u2014 (i) is described in section 501(c)(3) and exempt from tax under section 501(a), and (ii) is not a private foundation, (B) substantially all of the activities of which are providing scholarships for qualified elementary or secondary education expenses of eligible students, (C) which prevents the co-mingling of qualified contributions with other amounts by maintaining one or more separate accounts exclusively for qualified contributions, and (D) which either\u2014 (i) meets the requirements of subsection (d), or (ii) pursuant to State law, was able (as of the date of the enactment of this section) to receive contributions that are eligible for a State tax credit if such contributions are used by the organization to provide scholarships to individual elementary and secondary students, including scholarships for attending private schools. (d) Requirements for scholarship granting organizations (1) In general An organization meets the requirements of this subsection if\u2014 (A) such organization provides scholarships to 2 or more students, provided that not all such students attend the same school, (B) such organization does not provide scholarships for any expenses other than qualified elementary or secondary education expenses, (C) such organization provides a scholarship to eligible students with a priority for\u2014 (i) students awarded a scholarship the previous school year, and (ii) after application of clause (i), any such students who have a sibling who was awarded a scholarship from such organization, (D) such organization does not earmark or set aside contributions for scholarships on behalf of any particular student, (E) such organization takes appropriate steps to verify the annual household income and family size of eligible students to whom it awards scholarships, and limits them to a member of a household for which the income does not exceed the amount established under subsection (c)(1)(A), (F) such organization\u2014 (i) obtains from an independent certified public accountant annual financial and compliance audits, and (ii) certifies to the Secretary (at such time, and in such form and manner, as the Secretary may prescribe) that the audit described in clause (i) has been completed, and (G) no officer or board member of such organization has been convicted of a felony. (2) Income verification For purposes of paragraph (1)(E), review of all of the following (as applicable) shall be treated as satisfying the requirement to take appropriate steps to verify annual household income: (A) Federal and State income tax returns or tax return transcripts with applicable schedules for the taxable year prior to application. (B) Income reporting statements for tax purposes or wage and income transcripts from the Internal Revenue Service. (C) Notarized income verification letter from employers. (D) Unemployment or workers compensation statements. (E) Budget letters regarding public assistance payments and Supplemental Nutrition Assistance Program (SNAP) payments including a list of household members. (3) Independent certified public accountant For purposes of paragraph (1)(F), the term independent certified public accountant means, with respect to an organization, a certified public accountant who is not a person described in section 465(b)(3)(A) with respect to such organization or any employee of such organization. (4) Prohibition on self-dealing (A) In general A scholarship granting organization may not award a scholarship to any disqualified person. (B) Disqualified person For purposes of this paragraph, a disqualified person shall be determined pursuant to rules similar to the rules of section 4946. (e) Denial of double benefit Any qualified contribution for which a credit is allowed under this section shall not be taken into account as a charitable contribution for purposes of section 170. (f) Carryforward of unused credit (1) In general If the credit allowable under subsection (a) for any taxable year exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under this subpart (other than this section, section 23, and section 25D), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such taxable year. (2) Limitation No credit may be carried forward under this subsection to any taxable year following the fifth taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in first-out basis. .\n**(2) Conforming amendments**\n**(A)**\nSection 25(e)(1)(C) of such Code is amended by striking and 25D and inserting 25D, and 25F .\n**(B)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Qualified elementary and secondary education scholarships. .\n##### (b) Credit for corporations\n**(1) In general**\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding after section 45AA the following:\n45BB. Contributions to scholarship granting organizations (a) General rule For purposes of section 38, in the case of a corporation, the education scholarship credit determined under this section for the taxable year is the aggregate amount of qualified contributions for the taxable year. (b) Amount of credit The credit allowed under subsection (a) for any taxable year shall not exceed 5 percent of the taxable income (as defined in section 170(b)(2)(D)) of the corporation for such taxable year. (c) Qualified contributions For purposes of this section, the term qualified contribution has the meaning given such term under section 25F. (d) Denial of double benefit No deduction shall be allowed under any provision of this chapter for any expense for which a credit is allowed under this section. (e) Application of volume cap A qualified contribution shall be taken into account under this section only if such contribution is not in excess of the volume cap established under section 3 of the Educational Choice for Children Act of 2025 . .\n**(2) Conforming amendments**\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period and inserting , plus at the end of paragraph (41), and by adding at the end the following new paragraph:\n(42) the education scholarship credit determined under section 45BB(a). .\n**(3) Clerical amendment**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Contributions to scholarship granting organizations. .\n##### (c) Failure of scholarship granting organizations To make distributions\n**(1) In general**\nChapter 42 of such Code is amended by adding at the end the following new subchapter:\nI Scholarship Granting Organizations Sec. 4969. Failure to distribute receipts. 4969. Failure to distribute receipts (a) In general In the case of any scholarship granting organization (as defined in section 25F) which has been determined by the Secretary to have failed to satisfy the requirement under subsection (b) for any taxable year, any contribution made to such organization during the first taxable year beginning after the date of such determination shall not be treated as a qualified contribution (as defined in section 25F(c)(2)) for purposes of sections 25F and 45BB. (b) Requirement The requirement described in this subsection is that the amount of receipts of the scholarship granting organization for the taxable year which are distributed before the distribution deadline with respect to such receipts shall not be less than the required distribution amount with respect to such taxable year. (c) Definitions For purposes of this section\u2014 (1) Required distribution amount (A) In general The required distribution amount with respect to a taxable year is the amount equal to 100 percent of the total receipts of the scholarship granting organization for such taxable year\u2014 (i) reduced by the sum of such receipts that are retained for reasonable administrative expenses for the taxable year or are carried to the succeeding taxable year under subparagraph (C), and (ii) increased by the amount of the carryover under subparagraph (C) from the preceding taxable year. (B) Safe harbor for reasonable administrative expenses For purposes of subparagraph (A)(i), if the percentage of total receipts of a scholarship granting organization for a taxable year which are used for administrative purposes is equal to or less than 10 percent, such expenses shall be deemed to be reasonable for purposes of such subparagraph. (C) Carryover With respect to the amount of the total receipts of a scholarship granting organization with respect to any taxable year, an amount not greater than 15 percent of such amount may, at the election of such organization, be carried to the succeeding taxable year. (2) Distributions The term distribution includes amounts which are formally committed but not distributed. A formal commitment described in the preceding sentence may include contributions set aside for eligible students for more than one year. (3) Distribution deadline The distribution deadline with respect to receipts for a taxable year is the first day of the third taxable year following the taxable year in which such receipts are received by the scholarship granting organization. .\n**(2) Clerical amendment**\nThe table of subchapters for chapter 42 of such Code is amended by adding at the end the following new item:\nSubchapter I. Scholarship Granting Organizations .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years ending after December 31, 2025.\n#### 3. Volume cap\n##### (a) In general\nFor purposes of sections 25F(b)(2) and 45BB(e) of the Internal Revenue Code of 1986 (as added by this Act), the volume cap applicable under this section shall be $10,000,000,000 for calendar year 2026 and each subsequent year thereafter. Such amount shall be allocated by the Secretary as provided in subsection (b) to taxpayers with respect to qualified contributions made by such taxpayers, except that 10 percent of such amount shall be divided evenly among the States, and shall be available with respect to\u2014\n**(1)**\nindividuals residing in such States to claim the credit allowed under section 25F of the Internal Revenue Code of 1986, and\n**(2)**\ncorporations created or organized in such State to claim the credit determined under section 45BB of such Code.\n##### (b) First-Come, first-Serve\nFor purposes of applying the volume cap under this section, such volume cap for any calendar year shall be allocated by the Secretary on a first-come, first-serve basis, as determined based on the time (during such calendar year) at which the taxpayer made the qualified contribution with respect to which the allocation is made. The Secretary shall not make any allocation of volume cap for any calendar year after December 31 of such calendar year.\n##### (c) Real-Time information\nFor purposes of this section, the Secretary shall develop a system to track the amount of qualified contributions made during the calendar year for which a credit may be claimed under section 25F or 45BB of the Internal Revenue Code of 1986, with such information to be updated in real time.\n##### (d) Annual increases\n**(1) In general**\nIn the case of the calendar year after a high use calendar year, the dollar amount otherwise in effect under subsection (a) for such calendar year shall be equal to 105 percent of the dollar amount in effect for such high use calendar year.\n**(2) High use calendar year**\nFor purposes of this subsection, the term high use calendar year means any calendar year for which 90 percent or more of the volume cap in effect for such calendar year under subsection (a) is allocated to taxpayers.\n**(3) Prevention of decreases in annual volume cap**\nThe volume cap in effect under subsection (a) for any calendar year shall not be less than the volume cap in effect under such subsection for the preceding calendar year.\n**(4) Publication of annual volume cap**\nThe Secretary shall make publicly available the dollar amount of the volume cap in effect under subsection (a) for each calendar year.\n##### (e) States\nFor purposes of this section, the term State includes the District of Columbia.\n#### 4. Exemption from gross income for scholarships for qualified elementary or secondary education expenses of eligible students\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139J. Scholarships for qualified elementary or secondary education expenses of eligible students (a) In general In the case of an individual, gross income shall not include any amounts provided to any dependent of such individual pursuant to a scholarship for qualified elementary or secondary education expenses of an eligible student which is provided by a scholarship granting organization. (b) Definitions In this section, the terms qualified elementary or secondary education expense , eligible student , and scholarship granting organization have the same meaning given such terms under section 25F(c). .\n##### (b) Conforming amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before the item relating to section 140 the following new item:\nSec. 139J. Scholarships for qualified elementary or secondary education expenses of eligible students. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2025, in taxable years ending after such date.\n#### 5. Organizational and parental autonomy\n##### (a) Prohibition of control over scholarship organizations\n**(1) In general**\n**(A) Treatment**\nA scholarship granting organization shall not, by virtue of participation under any provision of this Act or any amendment made by this Act, be regarded as acting on behalf of any governmental entity.\n**(B) No governmental control**\nNothing in this Act, or any amendment made by this Act, shall be construed to permit, allow, encourage, or authorize any Federal, State, or local government entity, or officer or employee thereof, to mandate, direct, or control any aspect of any scholarship granting organization.\n**(C) Maximum freedom**\nTo the extent permissible by law, this Act, and any amendment made by this Act, shall be construed to allow scholarship granting organizations maximum freedom to provide for the needs of the participants without governmental control.\n**(2) Prohibition of control over non-public schools**\n**(A) No governmental control**\nNothing in this Act, or any amendment made by this Act, shall be construed to permit, allow, encourage, or authorize any Federal, State, or local government entity, or officer or employee thereof, to mandate, direct, or control any aspect of any private or religious elementary or secondary education institution.\n**(B) No exclusion of private or religious schools**\nNo Federal, State, or local government entity, or officer or employee thereof, shall impose or permit the imposition of any conditions or requirements that would exclude or operate to exclude educational expenses at private or religious elementary and secondary education institutions from being considered qualified elementary or secondary education expenses.\n**(C) No exclusion of qualified expenses due to institution's religious character or affiliation**\nNo Federal, State, or local government entity, or officer or employee thereof, shall exclude, discriminate against, or otherwise disadvantage any elementary or secondary education institution with respect to qualified elementary or secondary education expenses at that institution based in whole or in part on the institution\u2019s religious character or affiliation, including religiously based or mission-based policies or practices.\n**(3) Parental rights to use scholarships**\nNo Federal, State, or local government entity, or officer or employee thereof, shall disfavor or discourage the use of scholarships granted by participating scholarship granting organizations for qualified elementary or secondary education expenses at private or nonprofit elementary and secondary education institutions, including faith-based schools.\n**(4) Parental right to intervene**\nIn any action filed in any State or Federal court which challenges the constitutionality (under the constitution of such State or the Constitution of the United States) of any provision of this Act (or any amendment made by this Act), any parent of an eligible student who has received a scholarship from a scholarship granting organization shall have the right to intervene in support of the constitutionality of such provision or amendment. To avoid duplication of efforts and reduce the burdens placed on the parties to the action, the court in any such action may require interveners taking similar positions to file joint papers or to be represented by a single attorney at oral argument, provided that the court does not require such interveners to join any brief filed on behalf of any State which is a defendant in such action.\n##### (b) Definitions\nFor purposes of this section, the terms eligible student , scholarship granting organization , and qualified elementary or secondary education expense shall have the same meanings given such terms under section 25F(c) of the Internal Revenue Code of 1986 (as added by section 2(a) of this Act).",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "817",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing education scholarships to qualified elementary and secondary students.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-31",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "833",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Educational Choice for Children Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-04-28T21:54:49Z"
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
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s292is.xml"
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
      "title": "Educational Choice for Children Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Educational Choice for Children Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations to nonprofit organizations providing education scholarships to qualified elementary and secondary students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:25Z"
    }
  ]
}
```
