# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1225?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1225
- Title: Freedom of Association in Higher Education Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1225
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1225",
    "number": "1225",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Freedom of Association in Higher Education Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
            "date": "2025-04-01T17:59:54Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-01T17:59:54Z",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1225is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1225\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Banks (for himself and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to provide for certain freedom of association protections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom of Association in Higher Education Act of 2025 .\n#### 2. Purposes\n##### (a) Purposes\nThe purposes of this Act are as follows:\n**(1)**\nProtect any student in a single-sex social organization or any single-sex social organization from any adverse action by an institution of higher education based solely on the membership practice of such organization of limiting membership only to individuals of one sex.\n**(2)**\nEnsure any student in a single-sex social organization or any single-sex social organization is treated without bias in comparison to students at an institution of higher education who do not participate in single-sex social organizations, or other social organizations at an institution of higher education that are not single-sex.\n**(3)**\nProtect the rights of students to freely associate with and participate in social organizations, including single-sex social organizations.\n#### 3. Freedom of association protections for students in social organizations\nPart B of title I of the Higher Education Act of 1965 ( 20 U.S.C. 1011 et seq. ) is amended by adding at the end the following:\n124. Freedom of association protections for students in social organizations (a) Upholding freedom of association protections Any student (or group of students) enrolled in an institution of higher education shall\u2014 (1) be able to form or apply to join any recognized or unrecognized social organization, including any single-sex social organization; and (2) if selected for membership by any social organization, be able to join such social organization and participate in such social organization. (b) Non-Retaliation against students of single-Sex social organizations An institution of higher education that receives funds under this Act, including through an institution\u2019s participation in any program under title IV, shall not\u2014 (1) take any action to require or coerce a student or prospective student who is a member or prospective member of a single-sex social organization to waive the protections provided under subsection (a) , including as a condition of enrolling in the institution; (2) take any adverse action against a single-sex social organization, or a student who is a member or a prospective member of a single-sex social organization, based solely on the membership practice of such organization limiting membership only to individuals of one sex; or (3) impose a recruitment restriction (including a recruitment restriction relating to the schedule for membership recruitment) on a single-sex social organization recognized by the institution, which is not imposed upon other student organizations by the institution, unless the organization (or a council of similar organizations) and the institution have entered into a mutually agreed-upon written agreement that allows the institution to impose such restriction. (c) Rules of construction Nothing in this section shall\u2014 (1) require an institution of higher education to officially recognize a social organization, including a single-sex social organization; (2) prohibit an institution of higher education from taking an adverse action against a student who joins a social organization, including a single-sex social organization, for a reason including academic misconduct or nonacademic misconduct, or because the organization\u2019s purpose poses a clear harm to students or employees of the institution, so long as that adverse action is not based solely on the membership practice of the organization of limiting membership only to individuals of one sex; (3) prevent a social organization from regulating its own membership; (4) inhibit the ability of the faculty of an institution of higher education to express an opinion (either individually or collectively) about membership in a single-sex social organization, or otherwise inhibit the academic freedom of such faculty to research, write, or publish material about membership in such an organization; or (5) create enforceable rights against a social organization or against an institution of higher education due to the decision of such social organization to deny membership to an individual student. (d) Definitions In this section: (1) Adverse action The term adverse action includes the following actions taken by an institution of higher education with respect to a single-sex social organization or a member or prospective member of a single-sex social organization: (A) Expulsion, suspension, probation, censure, condemnation, formal reprimand, or any other disciplinary action, coercive action, or sanction taken by an institution of higher education or administrative unit of such institution. (B) An oral or written warning with respect to an action described in subparagraph (A) made by an official of an institution of higher education acting in their official capacity. (C) An action to deny participation in any education program or activity, including the withholding of any rights, privileges, or opportunities afforded other students on campus. (D) An action to withhold, in whole or in part, any financial assistance (including scholarships and on-campus employment), or denying the opportunity to apply for financial assistance, a scholarship, a graduate fellowship, or on-campus employment. (E) An action to deny or restrict access to on-campus housing. (F) An act to deny any certification, endorsement, or letter of recommendation that may be required by a student\u2019s current or future employer, a government agency, a licensing board, an institution of higher education, a scholarship program, or a graduate fellowship to which the student applies or seeks to apply. (G) An action to deny participation in any sports team, club, or other student organization, including a denial of any leadership position in any sports team, club, or other student organization. (H) An action to withdraw the institution\u2019s official recognition of such organization. (I) An action to require any student to certify that such student is not a member of a single-sex social organization or to disclose the student\u2019s membership in a single-sex social organization. (J) An action to interject an institution\u2019s own criteria into the membership practices of the organization in any manner that conflicts with the rights of such organization under title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ) or this section. (2) Single-sex social organization The term single-sex social organization means\u2014 (A) a social fraternity or sorority described in section 501(c) of the Internal Revenue Code of 1986 which is exempt from taxation under section 501(a) of such Code, or an organization that has been historically single-sex, the active membership of which consists primarily of students or alumni of an institution of higher education; or (B) a single-sex private social club (including an independent organization located off-campus) that consists primarily of students or alumni of an institution of higher education. .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2555",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Freedom of Association in Higher Education Act of 2025",
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
            "name": "Higher education",
            "updateDate": "2026-04-20T17:48:49Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-04-20T17:48:49Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2026-04-20T17:48:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-04-11T12:57:19Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1225is.xml"
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
      "title": "Freedom of Association in Higher Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom of Association in Higher Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to provide for certain freedom of association protections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:31Z"
    }
  ]
}
```
