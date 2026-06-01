# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3934?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3934
- Title: Medical Nutrition Therapy Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3934
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-05-20T11:03:29Z
- Update date including text: 2026-05-20T11:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S709)
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S709)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3934",
    "number": "3934",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Medical Nutrition Therapy Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T11:03:29Z",
    "updateDateIncludingText": "2026-05-20T11:03:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S709)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T18:08:23Z",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "KS"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3934is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3934\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Ms. Collins (for herself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to expand the availability of medical nutrition therapy services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Medical Nutrition Therapy Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOver two-thirds of Medicare fee-for-service beneficiaries have 2 or more chronic conditions, many of which can be prevented, delayed, treated, or managed through nutrition.\n**(2)**\nIndividuals from many racial and ethnic minority backgrounds are more likely to be diagnosed with chronic diseases such as diabetes, prediabetes, chronic kidney disease, end-stage renal disease, and obesity.\n**(3)**\nCoverage for medical nutrition therapy is only available to Medicare Part B beneficiaries with diabetes or a renal disease, despite medical nutrition therapy being part of the standard of care, in clinical guidelines, and medically necessary for many more chronic conditions.\n**(4)**\nMedical nutrition therapy has been shown to be a cost-effective component of treatment for obesity, diabetes, hypertension, dyslipidemia, HIV infection, unintended weight loss in older adults, and other chronic conditions.\n#### 3. Expanding the availability of medical nutrition therapy services under the medicare program\n##### (a) In general\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)(V), by striking in the case of and all that follows through organizations ; and\n**(2)**\nin subsection (vv)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking disease management and inserting the prevention, management, or treatment of a disease or condition specified in paragraph (4) ;\n**(ii)**\nby striking by a physician and all that follows through the period at the end and inserting the following:\nby\u2014 (A) a physician (as defined in subsection (r)(1)); (B) a physician assistant (as defined in subsection (aa)(5)); (C) a nurse practitioner (as defined in subsection (aa)(5)); (D) a clinical nurse specialist (as defined in subsection (aa)(5)(B)); or (E) in the case of such services furnished to manage such a disease or condition that is an eating disorder, a clinical psychologist (as defined by the Secretary). ; and\n**(iii)**\nby adding at the end the following new sentence: Such term shall not include any such services furnished to an individual for the prevention, management, or treatment of a renal disease if such individual is receiving maintenance dialysis for which payment is made under section 1881. ; and\n**(B)**\nby adding at the end the following new paragraph:\n(4) For purposes of paragraph (1), the diseases and conditions specified in this paragraph are the following: (A) Diabetes. (B) Prediabetes. (C) A renal disease. (D) Obesity (as defined for purposes of subsection (yy)(2)(C) or as otherwise defined by the Secretary). (E) Hypertension. (F) Dyslipidemia. (G) Malnutrition. (H) Eating disorders. (I) Cancer. (J) Gastrointestinal diseases, including Celiac disease. (K) HIV. (L) AIDS. (M) Cardiovascular disease. (N) Any other disease or condition\u2014 (i) specified by the Secretary relating to unintentional weight loss; (ii) for which the Secretary determines the services described in paragraph (1) to be medically necessary and appropriate for the prevention, management, or treatment of such disease or condition, consistent with any applicable recommendations of the United States Preventive Services Task Force; or (iii) for which the Secretary determines the services described in paragraph (1) are medically necessary, consistent either with protocols established by registered dietitian or nutrition professional organizations or with accepted clinical guidelines identified by the Secretary. .\n##### (b) Exclusion modification\nSection 1862(a)(1) is amended\u2014\n**(1)**\nin subparagraph (O), by striking and at the end;\n**(2)**\nin subparagraph (P), by striking the semicolon at the end and inserting , and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of medical nutrition therapy services (as defined in section 1861(vv)), which are not furnished for the prevention, management, or treatment of a disease or condition specified in paragraph (4) of such section; .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished in years beginning on or after the date that is 2 years after the date of the enactment of this Act.",
      "versionDate": "2026-02-26",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6199",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medical Nutrition Therapy Act of 2025",
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
        "updateDate": "2026-03-16T18:36:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-26",
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
          "measure-id": "id119s3934",
          "measure-number": "3934",
          "measure-type": "s",
          "orig-publish-date": "2026-02-26",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3934v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2026-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Medical Nutrition Therapy Act of </strong><strong>2026</strong></p><p>This bill expands Medicare coverage of medical nutrition therapy services.</p><p>Currently, Medicare covers such services for individuals with diabetes or kidney disease under certain circumstances; such services must also be provided by a registered dietitian or nutrition professional pursuant to a physician referral. The bill extends coverage to individuals with other diseases and conditions, including obesity, eating disorders, cancer, and HIV/AIDS; such services may also be referred by a physician assistant, nurse practitioner, clinical nurse specialist, or (for eating disorders) a clinical psychologist.</p>"
        },
        "title": "Medical Nutrition Therapy Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3934.xml",
    "summary": {
      "actionDate": "2026-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Medical Nutrition Therapy Act of </strong><strong>2026</strong></p><p>This bill expands Medicare coverage of medical nutrition therapy services.</p><p>Currently, Medicare covers such services for individuals with diabetes or kidney disease under certain circumstances; such services must also be provided by a registered dietitian or nutrition professional pursuant to a physician referral. The bill extends coverage to individuals with other diseases and conditions, including obesity, eating disorders, cancer, and HIV/AIDS; such services may also be referred by a physician assistant, nurse practitioner, clinical nurse specialist, or (for eating disorders) a clinical psychologist.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3934"
    },
    "title": "Medical Nutrition Therapy Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Medical Nutrition Therapy Act of </strong><strong>2026</strong></p><p>This bill expands Medicare coverage of medical nutrition therapy services.</p><p>Currently, Medicare covers such services for individuals with diabetes or kidney disease under certain circumstances; such services must also be provided by a registered dietitian or nutrition professional pursuant to a physician referral. The bill extends coverage to individuals with other diseases and conditions, including obesity, eating disorders, cancer, and HIV/AIDS; such services may also be referred by a physician assistant, nurse practitioner, clinical nurse specialist, or (for eating disorders) a clinical psychologist.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3934"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3934is.xml"
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
      "title": "Medical Nutrition Therapy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medical Nutrition Therapy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-14T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to expand the availability of medical nutrition therapy services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-14T03:48:26Z"
    }
  ]
}
```
