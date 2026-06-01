# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3134
- Title: Emergency Care Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 3134
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-05-22T08:07:26Z
- Update date including text: 2026-05-22T08:07:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3134",
    "number": "3134",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Emergency Care Improvement Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:26Z",
    "updateDateIncludingText": "2026-05-22T08:07:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:03:10Z",
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
          "date": "2025-05-01T13:03:05Z",
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
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NY"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "TX"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "TX"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3134ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3134\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Arrington (for himself, Mr. Vicente Gonzalez of Texas , Mr. Crenshaw , and Ms. Van Duyne ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to provide for coverage of certain services furnished by freestanding emergency centers.\n#### 1. Short title\nThis Act may be cited as the Emergency Care Improvement Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nTo expand provider capacity to respond to the COVID\u201319 pandemic, in April of 2020 the Centers for Medicare & Medicaid Services issued a waiver allowing freestanding emergency centers (FECs) to enroll as Medicare-certified hospitals and receive Medicare reimbursement for the duration of the COVID\u201319 public health emergency.\n**(2)**\nFECs are fully licensed emergency departments that are staffed by both Emergency Medicine trained physicians and registered nurses who are on-site 24 hours a day, seven days a week, and possess licensed pharmacies, clinical laboratories, and advanced imaging services. FECs are State-licensed, and adhere to the same standards and provide the same level of care as Hospital Based Emergency Rooms, including State EMTALA regulations on treating all patients.\n**(3)**\nOver 118 FECs, mostly located in Texas, have enrolled and provided high-quality emergency services for all kinds of emergency conditions at significant savings to the Medicare program and to thousands of Medicare beneficiaries.\n**(4)**\nAn actuarial study of Medicare claims data found that FECs did not increase overall utilization of emergency care services and saved the Medicare program 21.8 percent in lower emergency care payments for patients of similar acuity.\n#### 3. Coverage of freestanding emergency centers under Medicare and Medicaid\n##### (a) Coverage under Medicare part B\nSection 1832(a)(2) of the Social Security Act ( 42 U.S.C. 1395k(a) ) is amended\u2014\n**(1)**\nin subparagraph (I), by striking and at the end;\n**(2)**\nin subparagraph (J), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(K) specified emergency services furnished by a freestanding emergency center (as such terms are defined in section 1861(nnn)). .\n##### (b) Definitions\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Freestanding emergency center; specified emergency services (1) Freestanding emergency center The term freestanding emergency center means a health care facility that\u2014 (A) is an independent freestanding emergency department (as defined in section 2799A\u20131(a)(3)(D) of the Public Health Service Act); (B) is staffed 24 hours a day, 7 days a week, with a physician (as defined in subsection (r)(1)) available to furnish emergency services (as defined in section 2799A\u20131(a)(3)(C)(i) of the Public Health Service Act) in such facility 24 hours a day; (C) has arrangements with one or more hospitals, having agreements in effect under section 1866, for the referral and admission of patients requiring inpatient services or such diagnostic or other specialized services as are not available at such facility; (D) has established a governing body to determine, implement, and monitor policies governing the total operation of the facility; (E) develops, implements, and maintains an ongoing, data-driven quality assessment and performance improvement program, and has oversight and accountability for such program, ensuring that facility policies and such program are administered so as to provide quality health care in a safe environment; (F) is located\u2014 (i) in a metropolitan statistical area; or (ii) (I) in the case of a facility established prior to 2022, in a rural county; or (II) in the case of a facility established on or after January 1, 2022, in a rural county that does not have a Medicare-certified hospital or a rural emergency hospital (as defined in subsection (kkk)(2)); and (G) meets all State requirements applicable to facilities that furnish emergency medical services to individuals but do not typically provide for stays in excess of 24 hours, and meets such other requirements as the Secretary may prescribe not in excess of the conditions of participation under this title that are applicable to off campus dedicated emergency departments of hospitals (as described in section 482.55 of title 42, Code of Federal Regulations (or any successor regulation)). (2) Specified emergency services The term specified emergency services means emergency services (as defined in section 2799A\u20131(a)(3)(C)(i) of the Public Health Service Act) other than a service identified, as of the date of the enactment of the Emergency Care Improvement Act , by any of HCPCS evaluation and service management service codes 99281 through 99282. .\n##### (c) Application of EMTALA\nSection 1867(e) of the Social Security Act ( 42 U.S.C. 1395dd(e) ) is amended\u2014\n**(1)**\nin paragraph (2), by\u2014\n**(A)**\ninserting other than a freestanding emergency center (as defined in section 1861(nnn)) after a hospital ; and\n**(B)**\ninserting or a freestanding emergency center (as so defined) participating under this title before the period at the end; and\n**(2)**\nin paragraph (5), by inserting at the end the following new sentence: Beginning on the date of the enactment of the Emergency Care Improvement Act , such term also includes a freestanding emergency center (as defined in section 1861(nnn)), and any reference to a hospital that has a hospital emergency department includes such a freestanding emergency center. .\n##### (d) Payment under Medicare\nSection 1833(a)(2) of the Social Security Act ( 42 U.S.C. 1395l(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (G)(ii), by striking and at the end;\n**(2)**\nin subparagraph (H), by striking the comma at the end and inserting ; and ; and\n**(3)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) with respect to specified emergency services furnished by a freestanding emergency center (as such terms are defined in section 1861(nnn)), the amount that would have been determined under subsection (t) if such services had been covered OPD services, .\n##### (e) Coverage under Medicaid\nSection 1905(a)(2) of the Social Security Act ( 42 U.S.C. 1396d(a)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking and at the end; and\n**(2)**\nby inserting before the semicolon at the end the following: , and (D) specified emergency services furnished by freestanding emergency centers (as such terms are defined in section 1861(nnn)) .\n##### (f) Exclusion from prohibition on physician self-Referral\nSection 1877(b) of the Social Security Act ( 42 U.S.C. 1395nn(b) ) is amended by adding at the end the following new paragraph:\n(6) Freestanding emergency centers In the case of laboratory services and imaging services furnished by a freestanding emergency center in connection with specified emergency services (as such terms are defined in section 1861(nnn)). .\n##### (g) Effective date\nThe amendments made by this Act shall apply with respect to items and services furnished on or after the date of the enactment of this Act.",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-21T10:59:19Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3134ih.xml"
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
      "title": "Emergency Care Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:59Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Emergency Care Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to provide for coverage of certain services furnished by freestanding emergency centers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:48:33Z"
    }
  ]
}
```
