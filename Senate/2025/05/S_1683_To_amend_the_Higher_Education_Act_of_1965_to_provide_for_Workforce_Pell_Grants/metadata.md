# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1683?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1683
- Title: PELL Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1683
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-07-03T22:01:41Z
- Update date including text: 2025-07-03T22:01:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1683",
    "number": "1683",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "PELL Act of 2025",
    "type": "S",
    "updateDate": "2025-07-03T22:01:41Z",
    "updateDateIncludingText": "2025-07-03T22:01:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T17:15:40Z",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IA"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "PA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WV"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1683is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1683\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Budd (for himself, Mr. Grassley , Mr. Ricketts , Mr. McCormick , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to provide for Workforce Pell Grants.\n#### 1. Short title\nThis Act may be cited as the Promoting Employment and Lifelong Learning Act of 2025 or the PELL Act of 2025 .\n#### 2. Workforce pell grants\n##### (a) In general\nSection 401 of the Higher Education Act of 1965 ( 20 U.S.C. 1070a ) is amended by adding at the end the following:\n(k) Workforce pell grant program (1) In general For the award year beginning on July 1, 2026, and each subsequent award year, the Secretary shall award grants (to be known as Workforce Pell Grants ) to eligible students under paragraph (2) in accordance with this subsection. (2) Eligible students To be eligible to receive a Workforce Pell Grant under this subsection for any period of enrollment, a student shall meet the eligibility requirements for a Federal Pell Grant under this section, except that the student\u2014 (A) shall be enrolled, or accepted for enrollment, in an eligible program under section 481(b)(3) (hereinafter referred to as an eligible workforce program ); and (B) may not\u2014 (i) be enrolled, or accepted for enrollment, in a program of study that leads to a graduate credential; or (ii) have attained such a credential. (3) Terms and conditions of awards The Secretary shall award Workforce Pell Grants under this subsection in the same manner and with the same terms and conditions as the Secretary awards Federal Pell Grants under this section, except that\u2014 (A) each use of the term eligible program (except in subsections (b)(9)(A) and (d)(2)) shall be substituted by eligible workforce program under section 481(b)(3) ; and (B) a student who is eligible for a grant equal to less than the amount of the minimum Federal Pell Grant because the eligible workforce program in which the student is enrolled or accepted for enrollment is less than an academic year (in hours of instruction or weeks of duration) may still be eligible for a Workforce Pell Grant in an amount that is prorated based on the length of the program. (4) Prevention of double benefits No eligible student described in paragraph (2) may concurrently receive a grant under both this subsection and\u2014 (A) subsection (b); or (B) subsection (c). (5) Duration limit Any period of study covered by a Workforce Pell Grant awarded under this subsection shall be included in determining a student\u2019s duration limit under subsection (d)(5). .\n##### (b) Program eligibility for workforce pell grants\nSection 481(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1088(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (5), respectively;\n**(2)**\nby inserting after paragraph (2) the following:\n(3) (A) A program is an eligible program for purposes of the Workforce Pell Grant program under section 401(k) only if\u2014 (i) it is a program of at least 150 clock hours of instruction, but less than 600 clock hours of instruction, or an equivalent number of credit hours, offered by an eligible institution during a minimum of 8 weeks, but less than 15 weeks; (ii) it is not offered as a correspondence course, as defined in 600.2 of title 34, Code of Federal Regulations (as in effect on September 20, 2020); (iii) the Governor of a State, after consultation with the State board, makes a determination that the program\u2014 (I) provides an education aligned with the requirements of high-skill, high-wage (as identified by the State pursuant to section 122 of the Carl D. Perkins Career and Technical Education Act ( 20 U.S.C. 2342 )), or in-demand industry sectors or occupations; (II) meets the hiring requirements of potential employers in the sectors or occupations described in subclause (I); (III) either\u2014 (aa) leads to a recognized postsecondary credential that is stackable and portable across more than one employer; or (bb) with respect to students enrolled in the program\u2014 (AA) prepares such students for employment in an occupation for which there is only one recognized postsecondary credential; and (BB) provides such students with such a credential upon completion of such program; and (IV) prepares students to pursue 1 or more certificate or degree programs at 1 or more institutions of higher education (which may include the eligible institution providing the program), including by ensuring\u2014 (aa) that a student, upon completion of the program and enrollment in such a related certificate or degree program, will receive academic credit for the program that will be accepted toward meeting such certificate or degree program requirements; and (bb) the acceptability of such credit toward meeting such certificate or degree program requirements; (iv) after the Governor of such State makes the determination that the program meets the requirements under clause (iii), the Secretary determines that\u2014 (I) the program has been offered by the eligible institution for not less than 1 year prior to the date on which the Secretary makes a determination under this clause; (II) for each award year, the program has a verified completion rate of at least 70 percent, within 150 percent of the normal time for completion; and (III) for each award year, the program has a verified job placement rate of at least 70 percent, measured 180 days after completion; and (v) for each award year, the total amount of the published tuition and fees of the program for such year is an amount that does not exceed the value-added earnings of students who received Federal financial aid under this title and who completed the program 3 years prior to the award year, as such earnings are determined by calculating the difference between\u2014 (I) the median earnings of such students, as adjusted by the State and metropolitan area regional price parities of the Bureau of Economic Analysis based on the location of such program; and (II) 150 percent of the poverty line applicable to a single individual as determined under section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) ) for such year. (B) In the case of a program that has not previously participated in programs under this title and is being determined eligible for the first time under this paragraph, the Secretary may consider such program to be an eligible program for purposes of the Workforce Pell Grants program under section 401(k) for a provisional eligibility period that may not exceed 3 years, if such program\u2014 (i) subject to clause (ii), meets the requirements of subparagraph (A); and (ii) in lieu of the determination of median earnings under subclause (I) of subparagraph (A)(v), provides to the Secretary for purposes of meeting the requirements of subparagraph (A)(v), alternate earnings of students who complete the program, which are statistically rigorous, accurate, comparable, and representative of students who complete such program. (C) In this paragraph: (i) The term eligible institution means an institution of higher education (as defined in section 102), or any other entity that has entered into a program participation agreement with the Secretary under section 487(a) (without regard to whether that entity is accredited by a national recognized accrediting agency or association), which has not been subject, during any of the preceding 3 years, to\u2014 (I) any suspension, emergency action, or termination under this title; (II) in the case of an institution of higher education, any adverse action by the institution\u2019s accrediting agency or association that revokes or denies accreditation for the institution of higher education; or (III) any final action by the State in which the institution or other entity holds its legal domicile, authorization, or accreditation that revokes the institution\u2019s or entity\u2019s license or other authority to operate in such State. (ii) The term Governor means the chief executive of a State. (iii) The terms industry or sector partnership , in-demand industry sector or occupation , recognized postsecondary credential , and State board have the meanings given such terms in section 3 of the Workforce Innovation and Opportunity Act. .\n**(3) Student eligibility**\nSection 484(a)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1091(a)(1) ) is amended by inserting or, for purposes of section 401(k), at an entity (other than an institution of higher education) that meets the requirements of section 481(b)(3)(B)(i), after section 487 .\n**(4) Effective date; applicability**\nThe amendments made by this section shall take effect on July 1, 2026, and shall apply with respect to award year 2026\u20132027 and each succeeding award year.",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-07-03",
        "actionTime": "14:31:40",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
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
        "name": "Education",
        "updateDate": "2025-05-29T15:34:52Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1683is.xml"
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
      "title": "PELL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PELL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Promoting Employment and Lifelong Learning Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to provide for Workforce Pell Grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:45Z"
    }
  ]
}
```
