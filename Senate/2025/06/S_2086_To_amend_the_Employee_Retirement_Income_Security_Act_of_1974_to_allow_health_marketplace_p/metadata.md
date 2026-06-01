# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2086?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2086
- Title: Health Marketplace for All Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2086
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2026-02-04T04:11:37Z
- Update date including text: 2026-02-04T04:11:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2086",
    "number": "2086",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Health Marketplace for All Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T04:11:37Z",
    "updateDateIncludingText": "2026-02-04T04:11:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T17:02:24Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2086is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2086\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to allow health marketplace pools to be deemed an employer under section 3(5) of such Act for purposes of offering a group health plan or group health insurance coverage, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Marketplace for All Act of 2025 .\n#### 2. Health marketplace pools deemed an employer for purposes of offering group health plans or group health insurance coverage\n##### (a) Definition of employer\nSection 3(5) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(5) ) is amended by adding at the end the following: Such term shall be deemed to include, for purposes of offering a group health plan (as defined in section 733(a)(1)) or group health insurance coverage (as defined in section 733(b)(4)) (which, notwithstanding any other provision of law, may include such a plan or coverage covering prescription or nonprescription drugs as the only benefit offered by the plan or coverage in accordance with section 736(b)(5)(B)), any entity that meets the requirements under section 736(b). .\n##### (b) Group health plans and group health insurance coverage\nPart 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1181 et seq. ) is amended by adding at the end the following:\n736. Health marketplace pools deemed an employer for purposes of offering group health plans or group health insurance coverage (a) In general An entity (referred to in this section as a health marketplace pool ) that meets the requirements under subsection (b) shall be deemed an employer under section 3(5) for purposes of offering a group health plan or group health insurance coverage (which, notwithstanding any other provision of law, may include such a plan or coverage covering prescription or nonprescription drugs as the only benefit offered by the plan or coverage in accordance with subsection (b)(5)(B)). (b) Requirements for health marketplace pools The requirements under this subsection are each of the following: (1) Organization The health marketplace pool shall\u2014 (A) be formed and maintained in good faith for a purpose that includes the formation of a risk pool in order to offer group health insurance coverage or a group health plan to its members; and (B) not condition membership in the health marketplace pool on any health status-related factor relating to an individual (including an employee of an employer or a dependent of an employee). (2) Offering group health plans and group health insurance coverage (A) Different groups (i) In general The health marketplace pool, which may be in conjunction with a health insurance issuer that offers group health insurance coverage through the health marketplace pool, shall make available a group health plan or group health insurance coverage to all members of the health marketplace pool (and, in the case of members that are employers, employees of the employers) at rates that\u2014 (I) are established by the health marketplace pool, or a health insurance issuer contracting with such health marketplace pool, on a policy or product specific basis; and (II) subject to sections 701 and 702, may vary for individuals covered through the health marketplace pool. (ii) Permissible coverage for dependents Such group health plan or group health insurance coverage may be made available under clause (i) to any dependents of members of the health marketplace pool or dependents of employees of employers that are such members. (B) Nondiscrimination in coverage offered (i) In general Subject to clause (ii), the health marketplace pool may not offer coverage under a group health plan or group health insurance coverage to a member of the health marketplace pool unless the same coverage is offered to all such members of the health marketplace pool. (ii) Construction Nothing in this subsection shall be construed as requiring a health insurance issuer or group health plan to provide coverage outside the service area of the issuer or plan, or preventing a health insurance issuer or group health plan from underwriting or from excluding or limiting the coverage on any individual, subject to the requirements under sections 701 and 702. (C) Assumption of risk The health marketplace pool may provide\u2014 (i) group health insurance coverage through a contract with a health insurance issuer; or (ii) a group health plan through self-insurance. (3) Geographic areas Nothing in this subsection shall be construed as preventing the establishment and operation of more than 1 health marketplace pool in a geographic area or as limiting the number of health marketplace pools that may operate in any area. (4) Provision of administrative services to purchasers The health marketplace pool may provide administrative services for members. Such services may include accounting, billing, and enrollment information. (5) Drug coverage The group health plan or group health insurance coverage offered by the health marketplace pool may offer\u2014 (A) drug coverage, including coverage of over-the-counter drugs, in combination with other benefits covered by the group health plan or group health insurance coverage; or (B) notwithstanding any other provision of law, drug coverage, including coverage of over-the-counter drugs, as the only benefit covered by the group health plan or group health insurance coverage. (6) Members (A) In general With respect to an individual who is a member of the health marketplace pool\u2014 (i) the individual may enroll for coverage under the group health plan or group health insurance coverage offered by the health marketplace pool (including, if applicable, enrollment for coverage for a dependent of such individual); or (ii) the employer of the individual may enroll the individual for coverage under the group health plan or group health insurance coverage offered by the health marketplace pool (including, if applicable, enrollment for coverage for a dependent of such individual). (B) Eligibility An individual shall be eligible to be a member of the health marketplace pool if such individual is\u2014 (i) a member of an entity that establishes or joins the health marketplace pool (or a dependent of such a member, as applicable); (ii) an employee of a member of an entity described in clause (i) (or a dependent of such an employee, as applicable); or (iii) an employee of an entity (or a dependant of such an employee, as applicable) controlled by a member of an entity described in clause (i). (C) Rules for enrollment Nothing in this paragraph shall preclude the health marketplace pool from establishing rules of enrollment and reenrollment of members. Such rules shall be applied consistently to all members within the health marketplace pool and shall not be based in any manner on health status-related factors in accordance with sections 701 and 702. (c) Determination of employer and joint employer status Participating in or facilitating a group health plan or group health insurance coverage under this section shall not be construed as establishing under any Federal or State law\u2014 (1) an employer relationship for any purpose other than offering the group health plan or group health insurance coverage; or (2) a joint employer relationship for any purpose. (d) Definition In this section, the term dependent , as applied to a group health plan or group health insurance coverage offered in a State, shall have the meaning applied to such term with respect to such plan or coverage under the State law applying to such plan or coverage. Such term may include the spouse and children of the individual involved in accordance with such State law. .\n#### 3. Conforming amendments\nSection 3 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002 ) is amended\u2014\n**(1)**\nin paragraph (6), by inserting before the period , except (with respect to an entity meeting the requirements under section 736(b)) such term includes any member of such entity ;\n**(2)**\nin paragraph (21)\u2014\n**(A)**\nin subparagraph (A), by striking subparagraph (B) and inserting subparagraphs (B) and (C) ; and\n**(B)**\nby adding at the end the following:\n(C) With respect to a person that is a member of an entity (referred to in section 736 and this subparagraph as a health marketplace pool ) that meets the requirements of section 736(b) and offers a group health plan (as defined in section 733(a)(1)) or group health insurance coverage (as defined in section 733(b)(4)) (which, notwithstanding any other provision of law, may include such a plan or coverage covering prescription or nonprescription drugs as the only benefit offered by the plan or coverage), membership in the health marketplace pool shall not by itself cause the person to be a fiduciary with respect to the group health plan or group health insurance coverage. ; and\n**(3)**\nin paragraph (40)(A)\u2014\n**(A)**\nin clause (ii), by striking , or and inserting , ;\n**(B)**\nin clause (iii), by striking the period and inserting , or ; and\n**(C)**\nby adding at the end the following:\n(iv) as a group health plan (as defined in section 733(a)(1)), or group health insurance coverage (as defined in section 733(b)(4)), offered by an entity meeting the requirements under section 736(b) (which, notwithstanding any other provision of law, may include such an entity offering such a plan or coverage covering prescription or nonprescription drugs as the only benefit offered by the plan or coverage). .",
      "versionDate": "2025-06-17",
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3362",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Health Marketplace and Savings Accounts for All Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-07-08T13:29:04Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2086is.xml"
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
      "title": "Health Marketplace for All Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Marketplace for All Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to allow health marketplace pools to be deemed an employer under section 3(5) of such Act for purposes of offering a group health plan or group health insurance coverage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:20Z"
    }
  ]
}
```
