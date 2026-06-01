# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2555
- Title: Freedom of Association in Higher Education Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2555
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-05-20T08:08:27Z
- Update date including text: 2026-05-20T08:08:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2555",
    "number": "2555",
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
    "title": "Freedom of Association in Higher Education Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:27Z",
    "updateDateIncludingText": "2026-05-20T08:08:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:07:30Z",
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "KS"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "SD"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "OH"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "AZ"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "SC"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "IA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "UT"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "VA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "AL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "sponsorshipWithdrawnDate": "2026-04-20",
      "state": "GA"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "OH"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "SC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NJ"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "IN"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "AZ"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "GA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "KS"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "WI"
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
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "GA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MD"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "OK"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NC"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2555ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2555\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mrs. Houchin (for herself and Mr. Garcia of California ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to provide for certain freedom of association protections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom of Association in Higher Education Act of 2025 .\n#### 2. Purposes\n##### (a) Purposes\nThe purposes of this Act are as follows:\n**(1)**\nProtect any student in a single-sex social organization or any single-sex social organization from any adverse action by an institution of higher education based solely on the membership practice of such organization of limiting membership only to individuals of one sex.\n**(2)**\nEnsure any student in a single-sex social organization or any single-sex social organization is treated without bias in comparison to students at an institution of higher education who do not participate in single-sex social organizations, or other social organizations at an institution of higher education that are not single-sex.\n**(3)**\nProtect the rights of students to freely associate with and participate in social organizations, including single-sex social organizations.\n#### 3. Freedom of association protections for students in social organizations\nPart B of title I of the Higher Education Act of 1965 ( 20 U.S.C. 1011 et seq. ) is amended by adding at the end the following:\n124. Freedom of association protections for students in social organizations (a) Upholding freedom of association protections Any student (or group of students) enrolled in an institution of higher education shall\u2014 (1) be able to form or apply to join any recognized or unrecognized social organization, including any single-sex social organization; and (2) if selected for membership by any social organization, be able to join such social organization and participate in such social organization. (b) Non-Retaliation against students of single-Sex social organizations An institution of higher education that receives funds under this Act, including through an institution\u2019s participation in any program under title IV, shall not\u2014 (1) take any action to require or coerce a student or prospective student who is a member or prospective member of a single-sex social organization to waive the protections provided under subsection (a) , including as a condition of enrolling in the institution; (2) take any adverse action against a single-sex social organization, or a student who is a member or a prospective member of a single-sex social organization, based solely on the membership practice of such organization limiting membership only to individuals of one sex; or (3) impose a recruitment restriction (including a recruitment restriction relating to the schedule for membership recruitment) on a single-sex social organization recognized by the institution, which is not imposed upon other student organizations by the institution, unless the organization (or a council of similar organizations) and the institution have entered into a mutually agreed-upon written agreement that allows the institution to impose such restriction. (c) Rules of construction Nothing in this section shall\u2014 (1) require an institution of higher education to officially recognize a social organization, including a single-sex social organization; (2) prohibit an institution of higher education from taking an adverse action against a student who joins a social organization, including a single-sex social organization, for a reason including academic misconduct or nonacademic misconduct, or because the organization\u2019s purpose poses a clear harm to students or employees of the institution, so long as that adverse action is not based solely on the membership practice of the organization of limiting membership only to individuals of one sex; (3) prevent a social organization from regulating its own membership; (4) inhibit the ability of the faculty of an institution of higher education to express an opinion (either individually or collectively) about membership in a single-sex social organization, or otherwise inhibit the academic freedom of such faculty to research, write, or publish material about membership in such an organization; or (5) create enforceable rights against a social organization or against an institution of higher education due to the decision of such social organization to deny membership to an individual student. (d) Definitions In this section: (1) Adverse action The term adverse action includes the following actions taken by an institution of higher education with respect to a single-sex social organization or a member or prospective member of a single-sex social organization: (A) Expulsion, suspension, probation, censure, condemnation, formal reprimand, or any other disciplinary action, coercive action, or sanction taken by an institution of higher education or administrative unit of such institution. (B) An oral or written warning with respect to an action described in subparagraph (A) made by an official of an institution of higher education acting in their official capacity. (C) An action to deny participation in any education program or activity, including the withholding of any rights, privileges, or opportunities afforded other students on campus. (D) An action to withhold, in whole or in part, any financial assistance (including scholarships and on-campus employment), or denying the opportunity to apply for financial assistance, a scholarship, a graduate fellowship, or on-campus employment. (E) An action to deny or restrict access to on-campus housing. (F) An act to deny any certification, endorsement, or letter of recommendation that may be required by a student\u2019s current or future employer, a government agency, a licensing board, an institution of higher education, a scholarship program, or a graduate fellowship to which the student applies or seeks to apply. (G) An action to deny participation in any sports team, club, or other student organization, including a denial of any leadership position in any sports team, club, or other student organization. (H) An action to withdraw the institution\u2019s official recognition of such organization. (I) An action to require any student to certify that such student is not a member of a single-sex social organization or to disclose the student\u2019s membership in a single-sex social organization. (J) An action to interject an institution\u2019s own criteria into the membership practices of the organization in any manner that conflicts with the rights of such organization under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ) or this section. (2) Single-sex social organization The term single-sex social organization means\u2014 (A) a social fraternity or sorority described in section 501(c) of the Internal Revenue Code of 1986 which is exempt from taxation under section 501(a) of such Code, or an organization that has been historically single-sex, the active membership of which consists primarily of students or alumni of an institution of higher education; or (B) a single-sex private social club (including an independent organization located off-campus) that consists primarily of students or alumni of an institution of higher education. .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1225",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Freedom of Association in Higher Education Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Higher education",
            "updateDate": "2026-04-20T17:48:04Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-04-20T17:47:59Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2026-04-20T17:48:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-04-06T14:30:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
    "originChamber": "House",
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
          "measure-id": "id119hr2555",
          "measure-number": "2555",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2026-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2555v00",
            "update-date": "2026-04-21"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Freedom of Association in Higher Education Act of </strong><strong>2025</strong></p><p>This bill establishes freedom of association protections for college students in single-sex social organizations.</p><p>Specifically, the bill gives students (or groups of students) enrolled at institutions of higher education (IHEs) the right to form or join social organizations, including single-sex social organizations.</p><p>Additionally, the bill prohibits IHEs that participate in federal student\u00a0aid programs from</p><ul><li>taking adverse actions against single-sex social organizations or students who are members or prospective members of such organizations based solely on the practice of limiting membership to only individuals of one sex;</li><li>taking actions that require or coerce members or prospective members of such organizations to waive protections provided under the bill, including as a condition of enrolling in the IHE; or</li><li>imposing a recruitment restriction on a single-sex social organization that is not imposed upon other student organizations, unless the organization and IHE have entered into a written agreement allowing the restriction.</li></ul>"
        },
        "title": "Freedom of Association in Higher Education Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2555.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom of Association in Higher Education Act of </strong><strong>2025</strong></p><p>This bill establishes freedom of association protections for college students in single-sex social organizations.</p><p>Specifically, the bill gives students (or groups of students) enrolled at institutions of higher education (IHEs) the right to form or join social organizations, including single-sex social organizations.</p><p>Additionally, the bill prohibits IHEs that participate in federal student\u00a0aid programs from</p><ul><li>taking adverse actions against single-sex social organizations or students who are members or prospective members of such organizations based solely on the practice of limiting membership to only individuals of one sex;</li><li>taking actions that require or coerce members or prospective members of such organizations to waive protections provided under the bill, including as a condition of enrolling in the IHE; or</li><li>imposing a recruitment restriction on a single-sex social organization that is not imposed upon other student organizations, unless the organization and IHE have entered into a written agreement allowing the restriction.</li></ul>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr2555"
    },
    "title": "Freedom of Association in Higher Education Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Freedom of Association in Higher Education Act of </strong><strong>2025</strong></p><p>This bill establishes freedom of association protections for college students in single-sex social organizations.</p><p>Specifically, the bill gives students (or groups of students) enrolled at institutions of higher education (IHEs) the right to form or join social organizations, including single-sex social organizations.</p><p>Additionally, the bill prohibits IHEs that participate in federal student\u00a0aid programs from</p><ul><li>taking adverse actions against single-sex social organizations or students who are members or prospective members of such organizations based solely on the practice of limiting membership to only individuals of one sex;</li><li>taking actions that require or coerce members or prospective members of such organizations to waive protections provided under the bill, including as a condition of enrolling in the IHE; or</li><li>imposing a recruitment restriction on a single-sex social organization that is not imposed upon other student organizations, unless the organization and IHE have entered into a written agreement allowing the restriction.</li></ul>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr2555"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2555ih.xml"
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
      "title": "Freedom of Association in Higher Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom of Association in Higher Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to provide for certain freedom of association protections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:57Z"
    }
  ]
}
```
