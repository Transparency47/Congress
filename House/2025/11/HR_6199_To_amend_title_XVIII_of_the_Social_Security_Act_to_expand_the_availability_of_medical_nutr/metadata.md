# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6199?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6199
- Title: Medical Nutrition Therapy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6199
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-27T08:05:31Z
- Update date including text: 2026-05-27T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6199",
    "number": "6199",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000385",
        "district": "2",
        "firstName": "Robin",
        "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
        "lastName": "Kelly",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Medical Nutrition Therapy Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:31Z",
    "updateDateIncludingText": "2026-05-27T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:05:45Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WV"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "AL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "KS"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "HI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NJ"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "OR"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "DC"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "VT"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "PA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MN"
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
      "sponsorshipDate": "2026-05-26",
      "state": "VA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6199ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6199\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Kelly of Illinois (for herself, Mrs. Kiggans of Virginia , Mr. Veasey , Mrs. Miller of West Virginia , Ms. Sewell , Mr. Casten , Ms. Tlaib , Ms. Barrag\u00e1n , and Mr. Lieu ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to expand the availability of medical nutrition therapy services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Medical Nutrition Therapy Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOver two-thirds of Medicare fee-for-service beneficiaries have 2 or more chronic conditions, many of which can be prevented, delayed, treated, or managed through nutrition.\n**(2)**\nIndividuals from many racial and ethnic minority backgrounds are more likely to be diagnosed with chronic diseases such as diabetes, prediabetes, chronic kidney disease, end-stage renal disease, and obesity.\n**(3)**\nCoverage for medical nutrition therapy is only available to Medicare Part B beneficiaries with diabetes or a renal disease, despite medical nutrition therapy being part of the standard of care, in clinical guidelines, and medically necessary for many more chronic conditions.\n**(4)**\nMedical nutrition therapy has been shown to be a cost-effective component of treatment for obesity, diabetes, hypertension, dyslipidemia, HIV infection, unintended weight loss in older adults, and other chronic conditions.\n#### 3. Expanding the availability of medical nutrition therapy services under the medicare program\n##### (a) In general\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)(V), by striking in the case of and all that follows through organizations ; and\n**(2)**\nin subsection (vv)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking disease management and inserting the prevention, management, or treatment of a disease or condition specified in paragraph (4) ;\n**(ii)**\nby striking by a physician and all that follows through the period at the end and inserting the following:\nby\u2014 (A) a physician (as defined in subsection (r)(1)); (B) a physician assistant (as defined in subsection (aa)(5)); (C) a nurse practitioner (as defined in subsection (aa)(5)); (D) a clinical nurse specialist (as defined in subsection (aa)(5)(B)); or (E) in the case of such services furnished to manage such a disease or condition that is an eating disorder, a clinical psychologist (as defined by the Secretary). ; and\n**(iii)**\nby adding at the end the following new sentence: Such term shall not include any such services furnished to an individual for the prevention, management, or treatment of a renal disease if such individual is receiving maintenance dialysis for which payment is made under section 1881. ; and\n**(B)**\nby adding at the end the following new paragraph:\n(4) For purposes of paragraph (1), the diseases and conditions specified in this paragraph are the following: (A) Diabetes. (B) Prediabetes. (C) A renal disease. (D) Obesity (as defined for purposes of subsection (yy)(2)(C) or as otherwise defined by the Secretary). (E) Hypertension. (F) Dyslipidemia. (G) Malnutrition. (H) Eating disorders. (I) Cancer. (J) Gastrointestinal diseases, including Celiac disease. (K) HIV. (L) AIDS. (M) Cardiovascular disease. (N) Any other disease or condition\u2014 (i) specified by the Secretary relating to unintentional weight loss; (ii) for which the Secretary determines the services described in paragraph (1) to be medically necessary and appropriate for the prevention, management, or treatment of such disease or condition, consistent with any applicable recommendations of the United States Preventive Services Task Force; or (iii) for which the Secretary determines the services described in paragraph (1) are medically necessary, consistent either with protocols established by registered dietitian or nutrition professional organizations or with accepted clinical guidelines identified by the Secretary. .\n##### (b) Exclusion modification\nSection 1862(a)(1) is amended\u2014\n**(1)**\nin subparagraph (O), by striking and at the end;\n**(2)**\nin subparagraph (P), by striking the semicolon at the end and inserting , and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of medical nutrition therapy services (as defined in section 1861(vv)), which are not furnished for the prevention, management, or treatment of a disease or condition specified in paragraph (4) of such section; .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished in years beginning on or after the date that is 2 years after the date of the enactment of this Act.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S709)"
      },
      "number": "3934",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medical Nutrition Therapy Act of 2026",
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
        "updateDate": "2025-12-05T15:19:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119hr6199",
          "measure-number": "6199",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-20",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6199v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-11-20",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Medical Nutrition Therapy Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of medical nutrition therapy services.</p><p>Currently, Medicare covers such services for individuals with diabetes or kidney disease under certain circumstances; such services must also be provided by a registered dietitian or nutrition professional pursuant to a physician referral. The bill extends coverage to individuals with other diseases and conditions, including obesity, eating disorders, cancer, and HIV/AIDS; such services may also be referred by a physician assistant, nurse practitioner, clinical nurse specialist, or (for eating disorders) a clinical psychologist.</p>"
        },
        "title": "Medical Nutrition Therapy Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6199.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medical Nutrition Therapy Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of medical nutrition therapy services.</p><p>Currently, Medicare covers such services for individuals with diabetes or kidney disease under certain circumstances; such services must also be provided by a registered dietitian or nutrition professional pursuant to a physician referral. The bill extends coverage to individuals with other diseases and conditions, including obesity, eating disorders, cancer, and HIV/AIDS; such services may also be referred by a physician assistant, nurse practitioner, clinical nurse specialist, or (for eating disorders) a clinical psychologist.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6199"
    },
    "title": "Medical Nutrition Therapy Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Medical Nutrition Therapy Act of </strong><strong>2025</strong></p><p>This bill expands Medicare coverage of medical nutrition therapy services.</p><p>Currently, Medicare covers such services for individuals with diabetes or kidney disease under certain circumstances; such services must also be provided by a registered dietitian or nutrition professional pursuant to a physician referral. The bill extends coverage to individuals with other diseases and conditions, including obesity, eating disorders, cancer, and HIV/AIDS; such services may also be referred by a physician assistant, nurse practitioner, clinical nurse specialist, or (for eating disorders) a clinical psychologist.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6199"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6199ih.xml"
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
      "title": "Medical Nutrition Therapy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T13:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medical Nutrition Therapy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T13:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to expand the availability of medical nutrition therapy services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T13:03:43Z"
    }
  ]
}
```
