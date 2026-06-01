# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/383?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/383
- Title: JOBS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 383
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-04-08T15:18:44Z
- Update date including text: 2026-04-08T15:18:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/383",
    "number": "383",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "JOBS Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T15:18:44Z",
    "updateDateIncludingText": "2026-04-08T15:18:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
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
            "date": "2025-02-04T17:43:54Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-04T17:43:54Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "KS"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ND"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NH"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ND"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NH"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AK"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ID"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OH"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "WV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NM"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s383is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 383\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Kaine (for himself, Ms. Collins , Ms. Smith , Mr. Marshall , Ms. Baldwin , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Mr. Boozman , Mrs. Capito , Mr. Coons , Ms. Cortez Masto , Mr. Cramer , Mr. Daines , Ms. Duckworth , Mrs. Gillibrand , Ms. Hassan , Mr. Heinrich , Mr. Hickenlooper , Mr. Hoeven , Mrs. Hyde-Smith , Mr. Kelly , Mr. King , Ms. Klobuchar , Mr. Merkley , Mr. Ossoff , Mr. Peters , Ms. Rosen , Mrs. Shaheen , Mr. Sullivan , Mr. Tillis , Mr. Tuberville , Mr. Van Hollen , Mr. Warner , Mr. Wicker , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo extend Federal Pell Grant eligibility of certain short-term programs.\n#### 1. Short title\nThis Act may be cited as the Jumpstart Our Businesses by Supporting Students Act of 2025 or the JOBS Act of 2025 .\n#### 2. Extending Federal Pell Grant eligibility of certain short-term programs\n##### (a) Job training Federal Pell Grant program\nSection 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ) is amended by adding at the end the following:\n(k) Job training Federal Pell Grant program (1) Definitions In this subsection: (A) Eligible career pathway program The term eligible career pathway program means a program that\u2014 (i) meets the requirements of section 484(d)(2); (ii) is listed on the provider list under section 122(d) of the Workforce Innovation and Opportunity Act; (iii) is part of a career pathway, as defined in section 3 of that Act; and (iv) is aligned to a program of study as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006. (B) Eligible job training program (i) In General The term eligible job training program means a career and technical education program at an institution of higher education that\u2014 (I) provides not less than 150, and not more than 600, clock hours of instructional time over a period of not less than 8 weeks and not more than 15 weeks; (II) provides training aligned with the requirements of high-skill, high-wage, or in-demand industry sectors or occupations in the State or local area, as determined by an industry or sector partnership; (III) is a program of training services, and provided through an eligible training provider, as described under section 122(d) of the Workforce Innovation and Opportunity Act; (IV) provides a student, upon completion of the program, with a recognized postsecondary credential that is recognized by employers in the relevant industry, including credentials recognized by industry or sector partnerships in the relevant industry in the State or local area where the industry is located and the job training program is provided; (V) has been determined by the institution of higher education (after validation of that determination by an industry or sector partnership) to provide academic content, an amount of instructional time, and a recognized postsecondary credential that are sufficient to\u2014 (aa) meet the hiring requirements of potential employers; and (bb) satisfy any applicable educational prerequisite requirement for professional licensure or certification, so that the student who completes the program and seeks employment qualifies to take any licensure or certification examination needed to practice or find employment in an occupation that the program prepares students to enter; (VI) may include integrated education and training; (VII) may be offered as part of an eligible career pathway program; (VIII) does not exceed by more than 50 percent the minimum number of clock hours required for training if the State has established such a requirement; and (IX) shall include institutional credit articulation for a student enrolled in a noncredit job training program. (ii) Approval by the Secretary In the case of a program that is seeking to establish eligibility as an eligible job training program under this subparagraph, the Secretary shall make a determination about whether the program meets the requirements of this subparagraph not more than 60 days after the date on which such program is submitted for consideration as an eligible job training program. (iii) Additional assurance The Secretary shall not determine that a program is an eligible job training program in accordance with clause (ii) unless the Secretary receives a certification from the appropriate State board containing an assurance that the program meets the requirements of clause (i). (C) Institution of higher education The term institution of higher education means\u2014 (i) an institution of higher education, as defined in section 101; or (ii) a postsecondary vocational institution, as defined in section 102(c). (D) Institutional credit articulation The term institutional credit articulation means an institution of higher education provides a student who has completed a noncredit program with the equivalent academic credit that may be applied to a subsequent credit-bearing certificate or degree program upon enrollment in such program at such institution. (E) WIOA Definitions The terms industry or sector partnership , in-demand industry sector or occupation , recognized postsecondary credential , and State board have the meanings given such terms in section 3 of the Workforce Innovation and Opportunity Act. (2) In general For the award year beginning on July 1, 2025, and each subsequent award year, the Secretary shall carry out a program through which the Secretary shall award Federal Pell Grants to students in eligible job training programs (referred to as a job training Federal Pell Grant ). Each eligible job training Federal Pell Grant awarded under this subsection shall have the same terms and conditions, and be awarded in the same manner, as other Federal Pell Grants awarded under subsection (b), except as follows: (A) A student who is eligible to receive a job training Federal Pell Grant under this subsection is a student who\u2014 (i) has not yet attained a postbaccalaureate degree; (ii) attends an institution of higher education; (iii) is enrolled, or accepted for enrollment, in an eligible job training program at such institution of higher education; and (iv) meets all other eligibility requirements for a Federal Pell Grant (except with respect to the type of program of study, as provided in clause (iii)). (B) The amount of a job training Federal Pell Grant for an eligible student shall be determined under subsection (b), except that notwithstanding subsection (b)(1)(B) a student who is eligible for less than the minimum Federal Pell Grant for an academic year in which the student is enrolled in an eligible program full time may still be eligible for a Federal Pell Grant. (3) Inclusion in total eligibility period Any period during which a student receives a job training Federal Pell Grant under this subsection shall be included in calculating the student's period of eligibility for Federal Pell Grants under subsection (d), and the eligibility requirements regarding students who are enrolled in an undergraduate program on less than a full-time basis shall similarly apply to students who are enrolled in an eligible job training program at an eligible institution on less than a full-time basis. .\n##### (b) Accrediting agency recognition of eligible job training programs\nSection 496(a)(4) of the Higher Education Act of 1965 ( 20 U.S.C. 1099b(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and after the semicolon;\n**(2)**\nin subparagraph (B)(ii), by inserting and after the semicolon; and\n**(3)**\nby adding at the end the following:\n(C) if such agency or association has or seeks to include within its scope of recognition the evaluation of the quality of institutions of higher education participating in the job training Federal Pell Grant program under section 401(k), such agency or association shall, in addition to meeting the other requirements of this subpart, demonstrate to the Secretary that, with respect to such eligible job training programs (as defined in that subsection)\u2014 (i) the agency or association\u2019s standards include a process for determining if the institution has the capability to effectively offer an eligible job training program; and (ii) the agency or association requires a demonstration that the program\u2014 (I) has identified each recognized postsecondary credential offered and the corresponding industry or sector partnership that actively recognizes each credential in the relevant industry in the State or local area where the industry is located; and (II) provides the academic content and amount of instructional time that is sufficient to\u2014 (aa) meet the hiring requirements of potential employers; and (bb) satisfy any applicable educational prerequisites for professional licensure or certification requirements so that the student who completes the program and seeks employment qualifies to take any licensure or certification examination that is needed to practice or find employment in an occupation that the program prepares students to enter. .\n##### (c) Interagency data sharing\nThe Secretary of Education shall coordinate and enter into a data sharing agreement with the Secretary of Labor to ensure access to data related to indicators of performance collected under section 116 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141 ). Under such data sharing agreement, the Commissioner of the National Center for Education Statistics shall collect and review the contents of performance reports for eligible providers of training services described in section 116(d)(4) of that Act not less frequently than once each year.\n##### (d) Minimum Federal Pell Grant\nSection 401(a)(2)(F) of the Higher Education Act of 1965 ( 20 U.S.C. 1070a(a)(2)(F) ) is amended by striking 10 percent and inserting 5 percent .\n##### (e) Effective date\nThis section, and the amendments made by this section, shall take effect on July 1, 2025.",
      "versionDate": "2025-02-04",
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
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T15:18:44Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-04-04T12:54:32Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-04-04T12:54:32Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-04-04T12:54:32Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-04-04T12:54:32Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-04-04T12:54:32Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-04-04T12:54:32Z"
          },
          {
            "name": "Vocational and technical education",
            "updateDate": "2025-04-04T12:54:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-10T14:49:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s383",
          "measure-number": "383",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s383v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Jumpstart Our Businesses by Supporting Students Act of 2025 or the JOBS Act of 2025</strong></p><p>This bill expands student eligibility for Pell Grants by establishing the Job Training Federal Pell Grant program.</p><p>Specifically, the bill requires the Department of Education to award a job training Pell Grant to a student who does not have a degree; attends an institution of higher education (IHE); is enrolled in a career and technical education program at an IHE that provides 150 to 600 clock hours of instructional time over a period of 8 to 15 weeks and provides training aligned with high-skill, high-wage, or in-demand industry sectors (i.e., job training programs); and meets all other eligibility requirements for a Pell Grant.</p><p>The bill also specifies that any period during which a student receives a job training Pell Grant counts toward that student's Pell Grant eligibility period.</p>"
        },
        "title": "JOBS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s383.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Jumpstart Our Businesses by Supporting Students Act of 2025 or the JOBS Act of 2025</strong></p><p>This bill expands student eligibility for Pell Grants by establishing the Job Training Federal Pell Grant program.</p><p>Specifically, the bill requires the Department of Education to award a job training Pell Grant to a student who does not have a degree; attends an institution of higher education (IHE); is enrolled in a career and technical education program at an IHE that provides 150 to 600 clock hours of instructional time over a period of 8 to 15 weeks and provides training aligned with high-skill, high-wage, or in-demand industry sectors (i.e., job training programs); and meets all other eligibility requirements for a Pell Grant.</p><p>The bill also specifies that any period during which a student receives a job training Pell Grant counts toward that student's Pell Grant eligibility period.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s383"
    },
    "title": "JOBS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Jumpstart Our Businesses by Supporting Students Act of 2025 or the JOBS Act of 2025</strong></p><p>This bill expands student eligibility for Pell Grants by establishing the Job Training Federal Pell Grant program.</p><p>Specifically, the bill requires the Department of Education to award a job training Pell Grant to a student who does not have a degree; attends an institution of higher education (IHE); is enrolled in a career and technical education program at an IHE that provides 150 to 600 clock hours of instructional time over a period of 8 to 15 weeks and provides training aligned with high-skill, high-wage, or in-demand industry sectors (i.e., job training programs); and meets all other eligibility requirements for a Pell Grant.</p><p>The bill also specifies that any period during which a student receives a job training Pell Grant counts toward that student's Pell Grant eligibility period.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s383"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s383is.xml"
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
      "title": "JOBS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "JOBS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Jumpstart Our Businesses by Supporting Students Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend Federal Pell Grant eligibility of certain short-term programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:27Z"
    }
  ]
}
```
