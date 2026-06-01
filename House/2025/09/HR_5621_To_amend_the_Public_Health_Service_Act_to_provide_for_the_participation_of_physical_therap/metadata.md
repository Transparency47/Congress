# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5621?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5621
- Title: Physical Therapist Workforce and Patient Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5621
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-05-30T08:06:08Z
- Update date including text: 2026-05-30T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5621",
    "number": "5621",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000197",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. DeGette, Diana [D-CO-1]",
        "lastName": "DeGette",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Physical Therapist Workforce and Patient Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:08Z",
    "updateDateIncludingText": "2026-05-30T08:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:02:30Z",
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
          "date": "2025-09-30T16:02:25Z",
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
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-11",
      "state": "DC"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "TN"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IN"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "AZ"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "VT"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "AZ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "KS"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "LA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "ME"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "IL"
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
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "DE"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "WI"
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
      "sponsorshipDate": "2026-05-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5621ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5621\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. DeGette (for herself and Mr. Griffith ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Health Service Act to provide for the participation of physical therapists in the National Health Service Corps Loan Repayment program, to amend title XVIII of the Social Security Act to expand Medicare Rural Health Clinic Services and Federally Qualified Health Center Services to include physical therapy services, and for other purposes.\n#### 1. Short title; findings\n##### (a) Short title\nThis Act may be cited as the Physical Therapist Workforce and Patient Access Act of 2025 .\n##### (b) Findings\nCongress finds as follows:\n**(1)**\nPhysical therapists play an important role in the prevention, treatment, or management of pain for individuals, including those with substance use disorders, or at risk of developing a substance use disorder.\n**(2)**\nPhysical therapists are also playing an important role in the physical rehabilitation needs of individuals who have developed chronic health conditions as a result of COVID\u201319.\n**(3)**\nPhysical therapist services are an essential component of the multidisciplinary undertaking that will be required to improve patient access and outcomes in medically underserved areas.\n#### 2. National Health Service Corps; participation of physical therapists in loan repayment program\n##### (a) Mission of corps; definition of primary health services\nSection 331(a)(3)(D) of the Public Health Service Act ( 42 U.S.C. 254d(a)(3)(D) ) is amended by striking or mental health, and inserting mental health, or physical therapy, .\n##### (b) Physical therapy health professional target areas\nSection 332 of the Public Health Service Act ( 42 U.S.C. 254e ) is amended by adding at the end the following:\n(l) Physical therapy health professional target areas (1) In general The Secretary shall carry out a program of\u2014 (A) identifying physical therapy health professional target areas; and (B) assigning members of the Corps who are physical therapists to such areas. (2) Applicable provisions The provisions of paragraphs (1), (2), (3), (4), and (6) of subsection (k) shall apply to the identification of physical therapy health professional target areas and the assignment of physical therapists under this subsection except that\u2014 (A) references to maternity care health professional target areas shall be treated as references to physical therapy health professional target areas; and (B) references to maternity care health professionals and maternity care shall be treated as references to physical therapists and physical therapy, respectively. .\n##### (c) Loan repayment program\nSection 338B of the Public Health Service Act ( 42 U.S.C. 254l\u20131 ) is amended\u2014\n**(1)**\nin subsection (a)(1), by inserting physical therapists, after dentists, ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking (1)(A) have a degree in and all that follows through the end of subparagraph (A) of paragraph (1) and inserting the following:\n(1) (A) (i) have a degree in medicine, osteopathic medicine, dentistry, or another health profession, or an appropriate degree from a graduate program of behavioral and mental health; (ii) be certified as a nurse midwife, nurse practitioner, or physician assistant; or (iii) have a doctoral or master\u2019s degree in physical therapy; ;\n**(B)**\nin paragraph (1)(B), by inserting physical therapy, after mental health, ; and\n**(C)**\nin paragraph (1)(C)(ii), by inserting physical therapy, after dentistry, ; and\n**(3)**\nby adding at the end the following:\n(i) Eligibility to participate in other programs Nothing in this section shall be construed to prohibit any health care professional who is eligible to participate in the program under this section from participating in any other loan repayment program established by the Secretary for which such professional is eligible. .\n#### 3. Additional funding for participation of physical therapists in the National Health Service Corps Loan Repayment Program\nSection 10503(b)(2)(K) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 254b\u20132(b)(2)(K) ) is amended\u2014\n**(1)**\nby striking $172,972,603 and inserting $187,972,603 ; and\n**(2)**\nby inserting before the period at the end the following: , provided that of such amount the Secretary shall use not less than $15,000,000 for making loan repayments for physical therapists participating in the National Health Service Corps Loan Repayment Program under section 338B of the Public Health Service Act .\n#### 4. Expanding Medicare Rural Health Clinic Services and Federally Qualified Health Center Services to include physical therapy services\n##### (a) In general\nSection 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (C), by striking at the end and ;\n**(B)**\nin subparagraph (D), by adding and at the end; and\n**(C)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) such physical therapy services (as defined in subsection (p)) furnished by a physical therapist, ; and\n**(2)**\nin paragraph (3)(A), by striking subparagraphs (A) through (D) and inserting subparagraphs (A) through (E) .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to services furnished on or after January 1, 2027.",
      "versionDate": "2025-09-30",
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
        "updateDate": "2025-11-18T16:38:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hr5621",
          "measure-number": "5621",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5621v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Physical Therapist Workforce and Patient Access Act of 2025</strong></p><p>This bill expands certain health professional programs and Medicare covered services to include physical therapists.</p><p>Specifically, the bill expands the National Health Service Corps to include physical therapists and provides for the designation of specific health professional target areas for physical therapists under the program. The bill also expands covered services of rural health clinics and federally qualified health centers under Medicare to include physical therapy services.</p><p>The bill increases funds for FY2025 for the corps and requires a certain amount of funds to be used for student loan repayments for participating physical therapists in the National Health Service Corps Loan Repayment Program.</p><p>\u00a0</p>"
        },
        "title": "Physical Therapist Workforce and Patient Access Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5621.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Physical Therapist Workforce and Patient Access Act of 2025</strong></p><p>This bill expands certain health professional programs and Medicare covered services to include physical therapists.</p><p>Specifically, the bill expands the National Health Service Corps to include physical therapists and provides for the designation of specific health professional target areas for physical therapists under the program. The bill also expands covered services of rural health clinics and federally qualified health centers under Medicare to include physical therapy services.</p><p>The bill increases funds for FY2025 for the corps and requires a certain amount of funds to be used for student loan repayments for participating physical therapists in the National Health Service Corps Loan Repayment Program.</p><p>\u00a0</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5621"
    },
    "title": "Physical Therapist Workforce and Patient Access Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Physical Therapist Workforce and Patient Access Act of 2025</strong></p><p>This bill expands certain health professional programs and Medicare covered services to include physical therapists.</p><p>Specifically, the bill expands the National Health Service Corps to include physical therapists and provides for the designation of specific health professional target areas for physical therapists under the program. The bill also expands covered services of rural health clinics and federally qualified health centers under Medicare to include physical therapy services.</p><p>The bill increases funds for FY2025 for the corps and requires a certain amount of funds to be used for student loan repayments for participating physical therapists in the National Health Service Corps Loan Repayment Program.</p><p>\u00a0</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5621"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5621ih.xml"
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
      "title": "Physical Therapist Workforce and Patient Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Physical Therapist Workforce and Patient Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T08:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for the participation of physical therapists in the National Health Service Corps Loan Repayment program, to amend title XVIII of the Social Security Act to expand Medicare Rural Health Clinic Services and Federally Qualified Health Center Services to include physical therapy services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T08:18:24Z"
    }
  ]
}
```
