# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1599?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1599
- Title: Midwives for MOMS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1599
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2026-05-19T11:03:44Z
- Update date including text: 2026-05-19T11:03:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1599",
    "number": "1599",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Midwives for MOMS Act of 2025",
    "type": "S",
    "updateDate": "2026-05-19T11:03:44Z",
    "updateDateIncludingText": "2026-05-19T11:03:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
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
            "date": "2025-05-05T22:41:32Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-05T22:41:32Z",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AK"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "AZ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1599is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1599\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Luj\u00e1n (for himself, Ms. Murkowski , Mr. Merkley , Ms. Klobuchar , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo address maternity care shortages and promote optimal maternity outcomes by expanding educational opportunities for midwives, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Midwives for Maximizing Optimal Maternity Services Act of 2025 or the Midwives for MOMS Act of 2025 .\n#### 2. Midwifery schools and programs\n##### (a) In general\nTitle VII of the Public Health Service Act is amended by inserting after section 760 of such Act ( 42 U.S.C. 294k ) the following:\n760A. Midwifery schools and programs (a) In general The Secretary may award grants to institutions of higher education (as defined in subsections (a) and (b) of section 101 of the Higher Education Act of 1965) for the following: (1) Direct support of students in an accredited midwifery school or program. (2) Establishment or expansion of an accredited midwifery school or program. (3) Securing, preparing, or providing support for increasing the number of, qualified preceptors for training the students of an accredited midwifery school or program. (b) Special considerations In awarding grants under subsection (a), the Secretary shall give special consideration to any institution of higher education that\u2014 (1) agrees to prioritize students who plan to practice in a health professional shortage area designated under section 332; and (2) demonstrates a focus on increasing racial and ethnic minority representation in midwifery education. (c) Restriction The Secretary shall not provide any assistance under this section to be used with respect to a midwifery school or program within a school of nursing (as defined in section 801). (d) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section $15,000,000 for the period of fiscal years 2025 through 2029. (2) Allocation Of the amounts made available to carry out this section for any fiscal year, the Secretary shall use\u2014 (A) 50 percent for subsection (a)(1); (B) 25 percent for subsection (a)(2); and (C) 25 percent for subsection (a)(3). .\n##### (b) Definitions\n**(1) Midwifery school or program**\nSection 799B(1)(A) of the Public Health Service Act ( 42 U.S.C. 295p(1)(A) ) is amended\u2014\n**(A)**\nby inserting midwifery school or program , before and school of chiropractic ;\n**(B)**\nby inserting a degree or certificate in midwifery or an equivalent degree or certificate, before and a degree of doctor of chiropractic or an equivalent degree ; and\n**(C)**\nby striking any such school and inserting any such school or program .\n**(2) Accredited**\nSection 799B(1)(E) of the Public Health Service Act ( 42 U.S.C. 295p(1)(E) ) is amended by inserting or a midwifery school or program, before or a graduate program in health administration .\n#### 3. Nurse-midwives\nTitle VIII of the Public Health Service Act is amended by inserting after section 811 of such Act ( 42 U.S.C. 296j ) the following:\n812. Midwifery expansion program (a) In general The Secretary may award grants to schools of nursing for the following: (1) Direct support of students in an accredited nurse-midwifery school or program. (2) Establishment or expansion of an accredited nurse-midwifery school or program. (3) Securing, preparing, or providing support for increasing the numbers of, preceptors at clinical training sites to precept students training to become certified nurse-midwives. (b) Special considerations In awarding grants under subsection (a), the Secretary shall give special consideration to any school of nursing that\u2014 (1) agrees to prioritize students who choose to pursue an advanced education degree in nurse-midwifery to practice in a health professional shortage area designated under section 332; and (2) demonstrates a focus on increasing racial and ethnic minority representation in nurse-midwifery education. (c) Authorization of appropriations (1) In general To carry out this section, there is authorized to be appropriated $20,000,000 for the period of fiscal years 2025 through 2029. (2) Allocation Of the amounts made available to carry out this section for any fiscal year, the Secretary shall use\u2014 (A) 50 percent for subsection (a)(1); (B) 25 percent for subsection (a)(2); and (C) 25 percent for subsection (a)(3). .",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-12-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6394",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Midwives for MOMS Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-05-27T15:02:58Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1599is.xml"
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
      "title": "Midwives for MOMS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Midwives for MOMS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Midwives for Maximizing Optimal Maternity Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address maternity care shortages and promote optimal maternity outcomes by expanding educational opportunities for midwives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:33Z"
    }
  ]
}
```
