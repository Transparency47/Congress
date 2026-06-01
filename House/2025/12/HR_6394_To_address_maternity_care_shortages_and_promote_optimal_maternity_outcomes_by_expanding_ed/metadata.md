# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6394?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6394
- Title: Midwives for MOMS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6394
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-03-31T15:33:37Z
- Update date including text: 2026-03-31T15:33:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6394",
    "number": "6394",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Midwives for MOMS Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T15:33:37Z",
    "updateDateIncludingText": "2026-03-31T15:33:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6394ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6394\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mrs. Hinson (for herself and Mr. Gray ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo address maternity care shortages and promote optimal maternity outcomes by expanding educational opportunities for midwives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Midwives for Maximizing Optimal Maternity Services Act of 2025 or the Midwives for MOMS Act of 2025 .\n#### 2. Midwifery schools and programs\n##### (a) In general\nTitle VII of the Public Health Service Act is amended by inserting after section 760 of such Act ( 42 U.S.C. 294k ) the following:\n760A. Midwifery schools and programs (a) In general The Secretary may award grants to institutions of higher education (as defined in subsections (a) and (b) of section 101 of the Higher Education Act of 1965) for the following: (1) Direct support of students in an accredited midwifery school or program. (2) Establishment or expansion of an accredited midwifery school or program. (3) Securing, preparing, or providing support for increasing the number of, qualified preceptors for training the students of an accredited midwifery school or program. (b) Priority evaluation In awarding grants under subsection (a), the Secretary shall give precedence to any institution of higher education that\u2014 (1) agrees to prioritize students who plan to practice in a health professional shortage area designated under section 332; and (2) demonstrates a focus on recruitment and retention of students from rural and economically disadvantaged communities through\u2014 (A) enhanced recruitment strategies; (B) mentorship programs; (C) academic remediation; or (D) internships and fellowships. (c) Restriction The Secretary shall not provide any assistance under this section to be used with respect to a midwifery school or program within a school of nursing (as defined in section 801). (d) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section $15,000,000 for the period of fiscal years 2026 through 2030. (2) Allocation Of the amounts made available to carry out this section for any fiscal year, the Secretary shall use\u2014 (A) 50 percent for subsection (a)(1); (B) 25 percent for subsection (a)(2); and (C) 25 percent for subsection (a)(3). .\n##### (b) Definitions\n**(1) Midwifery school or program**\nSection 799B(1)(A) of the Public Health Service Act ( 42 U.S.C. 295p(1)(A) ) is amended\u2014\n**(A)**\nby inserting midwifery school or program , before and school of chiropractic ;\n**(B)**\nby inserting a degree or certificate in midwifery or an equivalent degree or certificate, before and a degree of doctor of chiropractic or an equivalent degree ; and\n**(C)**\nby striking any such school and inserting any such school or program .\n**(2) Accredited**\nSection 799B(1)(E) of the Public Health Service Act ( 42 U.S.C. 295p(1)(E) ) is amended by inserting a midwifery school or program, before or a graduate program in health administration .\n#### 3. Nurse-midwives\nTitle VIII of the Public Health Service Act is amended by inserting after section 811 of such Act ( 42 U.S.C. 296j ) the following:\n812. Midwifery expansion program (a) In general The Secretary may award grants to schools of nursing for the following: (1) Direct support of students in an accredited nurse-midwifery school or program. (2) Establishment or expansion of an accredited nurse-midwifery school or program. (3) Securing, preparing, or providing support for increasing the numbers of, preceptors at clinical training sites to precept students training to become certified nurse-midwives. (b) Priority evaluation In awarding grants under subsection (a), the Secretary shall give precedence to any school of nursing that\u2014 (1) agrees to prioritize students who choose to pursue an advanced education degree in nurse-midwifery to practice in a health professional shortage area designated under section 332; and (2) demonstrates a focus on recruitment and retention of students from rural and economically disadvantaged communities through\u2014 (A) enhanced recruitment strategies; (B) mentorship programs; (C) academic remediation; or (D) internships and fellowships. (c) Authorization of appropriations (1) In general To carry out this section, there is authorized to be appropriated $20,000,000 for the period of fiscal years 2026 through 2030. (2) Allocation Of the amounts made available to carry out this section for any fiscal year, the Secretary shall use\u2014 (A) 50 percent for subsection (a)(1); (B) 25 percent for subsection (a)(2); and (C) 25 percent for subsection (a)(3). .",
      "versionDate": "2025-12-03",
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
        "actionDate": "2025-05-05",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1599",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Midwives for MOMS Act of 2025",
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
        "updateDate": "2026-01-05T16:38:52Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6394ih.xml"
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
      "title": "Midwives for MOMS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Midwives for MOMS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Midwives for Maximizing Optimal Maternity Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address maternity care shortages and promote optimal maternity outcomes by expanding educational opportunities for midwives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:18:25Z"
    }
  ]
}
```
