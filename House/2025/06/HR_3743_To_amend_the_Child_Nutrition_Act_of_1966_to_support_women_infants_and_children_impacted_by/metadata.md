# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3743?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3743
- Title: Supporting Healthy Mothers and Infants Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3743
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-01-17T09:05:58Z
- Update date including text: 2026-01-17T09:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3743",
    "number": "3743",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Supporting Healthy Mothers and Infants Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-17T09:05:58Z",
    "updateDateIncludingText": "2026-01-17T09:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:00:35Z",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "IA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "IN"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
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
      "sponsorshipDate": "2025-06-30",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "GA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "NE"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "DE"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "TX"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "GU"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CO"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "GA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "IL"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3743ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3743\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Vindman (for himself, Mr. Thompson of Pennsylvania , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Nutrition Act of 1966 to support women, infants, and children impacted by substance use disorder, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Healthy Mothers and Infants Act of 2025 .\n#### 2. Amendments to special supplemental nutrition program\n##### (a) Special supplemental nutrition program for women, infants, and children\nSection 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ) is amended\u2014\n**(1)**\nin subsection (a), by striking drug abuse and inserting substance use disorder ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (8), by striking drug abuse and inserting substance use disorder ; and\n**(B)**\nin paragraph (16)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking Drug abuse education and inserting Substance use disorder education ;\n**(ii)**\nin subparagraph (A), by striking dangers of drug abuse and inserting harm of substance use during pregnancy and lactation ; and\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nby striking are suspected drug abusers and inserting may have a substance use disorder ;\n**(II)**\nby striking drug abuse clinics, ; and\n**(III)**\nby striking drug abuse professionals and inserting resources ;\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking drug abuse each place it appears and inserting substance use disorder ; and\n**(ii)**\nby striking effects of drug and inserting effects of a substance use disorder ; and\n**(B)**\nin paragraph (5), by striking substance abuse and inserting substance use disorder ;\n**(4)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)(C)(ix), by striking drugs and inserting illicit or other harmful substances ; and\n**(B)**\nin paragraph (13), by striking drug abuse education and inserting substance use disorder education ;\n**(5)**\nin subsection (k)(1)\u2014\n**(A)**\nby striking 1 member and inserting one member ; and\n**(B)**\nby striking drug abuse and inserting substance use disorder ; and\n**(6)**\nby redesignating subsections (l) through (q) as subsections (m) through (r), respectively, and by inserting after subsection (k) the following:\n(l) Activities To support WIC-Eligible individuals impacted by substance use disorder (1) In general The Secretary shall\u2014 (A) develop and disseminate nutrition education materials for individuals eligible for the program; and (B) conduct outreach to individuals who are potentially eligible for the program and who are impacted by a substance use disorder. (2) Purpose The purpose of this subsection is to ensure that individuals participating in the program who are impacted by a substance use disorder receive accurate nutrition education from trained staff in an effective and unbiased manner. (3) Nutrition education materials (A) In general The Secretary shall collaborate with the Secretary of Health and Human Services to develop appropriate evidence-based nutrition education materials for individuals impacted by a substance use disorder, including\u2014 (i) nutrition education materials for individuals with substance use disorder during pregnancy and in the postpartum period; and (ii) nutrition education materials for infants impacted by prenatal substance exposure and neonatal abstinence syndrome. (B) Educational materials update The materials developed pursuant to subparagraph (A) shall be included in the educational materials developed under paragraph (15) of section 515(b) of the Public Health Service Act ( 42 U.S.C. 290bb\u201321(b) ) and guidance issued under section 1005 of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 1396a note). (4) Nutrition education clearinghouse The Secretary shall make available to all State agencies through an online clearinghouse any nutrition education and training materials related to nutrition for individuals impacted by a substance use disorder or neonatal abstinence syndrome that have been produced by the Secretary or the Secretary of Health and Human Services (or produced by a State agency and approved by the Secretary), including educational materials developed under paragraph (15) of section 515(b) of the Public Health Service Act ( 42 U.S.C. 290bb\u201321(b) ) and guidance issued under section 1005 of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 1396a note). (5) Authorization of appropriations There are authorized to be appropriated to carry out this subsection $1,000,000 for fiscal year 2026, to remain available until expended. .\n##### (b) Conforming amendments\nSection 17(q) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(q) ), as redesignated by subsection (a) is amended\u2014\n**(1)**\nin paragraph (1), by striking subsection (o)(1)(A) and inserting subsection (p)(1)(A) ; and\n**(2)**\nin paragraph (2)(B), by striking subsection (o)(1)(A) and inserting subsection (p)(1)(A) .",
      "versionDate": "2025-06-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-11T17:28:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-04",
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
          "measure-id": "id119hr3743",
          "measure-number": "3743",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-04",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3743v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting Healthy Mothers and Infants Act of 2025</strong></p><p>This bill modifies the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) to add requirements for supporting individuals impacted by a substance use disorder.</p><p>Specifically, the bill requires the Department of Agriculture to</p><ul><li>collaborate with the Department of Health and Human Services (HHS) to develop and disseminate nutrition education materials for individuals impacted by a substance use disorder, including materials for infants impacted by prenatal substance exposure and neonatal abstinence syndrome;</li><li>conduct outreach to individuals who are potentially eligible for the WIC program and who are impacted by such a disorder; and</li><li>make available to states through an online clearinghouse any nutrition education and training materials related to nutrition for individuals impacted by a substance use disorder or neonatal abstinence syndrome.</li></ul><p>In addition, the nutrition education materials developed in collaboration with HHS must be included in (1) Center for Substance Abuse Prevention-developed education materials, and (2) HHS guidance on improving care for infants with neonatal abstinence syndrome and their families.</p><p>Under current law, the WIC program includes certain education\u00a0related to drug abuse. This bill replaces references to drug abuse with substance use disorder.</p>"
        },
        "title": "Supporting Healthy Mothers and Infants Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3743.xml",
    "summary": {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Healthy Mothers and Infants Act of 2025</strong></p><p>This bill modifies the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) to add requirements for supporting individuals impacted by a substance use disorder.</p><p>Specifically, the bill requires the Department of Agriculture to</p><ul><li>collaborate with the Department of Health and Human Services (HHS) to develop and disseminate nutrition education materials for individuals impacted by a substance use disorder, including materials for infants impacted by prenatal substance exposure and neonatal abstinence syndrome;</li><li>conduct outreach to individuals who are potentially eligible for the WIC program and who are impacted by such a disorder; and</li><li>make available to states through an online clearinghouse any nutrition education and training materials related to nutrition for individuals impacted by a substance use disorder or neonatal abstinence syndrome.</li></ul><p>In addition, the nutrition education materials developed in collaboration with HHS must be included in (1) Center for Substance Abuse Prevention-developed education materials, and (2) HHS guidance on improving care for infants with neonatal abstinence syndrome and their families.</p><p>Under current law, the WIC program includes certain education\u00a0related to drug abuse. This bill replaces references to drug abuse with substance use disorder.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr3743"
    },
    "title": "Supporting Healthy Mothers and Infants Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Healthy Mothers and Infants Act of 2025</strong></p><p>This bill modifies the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) to add requirements for supporting individuals impacted by a substance use disorder.</p><p>Specifically, the bill requires the Department of Agriculture to</p><ul><li>collaborate with the Department of Health and Human Services (HHS) to develop and disseminate nutrition education materials for individuals impacted by a substance use disorder, including materials for infants impacted by prenatal substance exposure and neonatal abstinence syndrome;</li><li>conduct outreach to individuals who are potentially eligible for the WIC program and who are impacted by such a disorder; and</li><li>make available to states through an online clearinghouse any nutrition education and training materials related to nutrition for individuals impacted by a substance use disorder or neonatal abstinence syndrome.</li></ul><p>In addition, the nutrition education materials developed in collaboration with HHS must be included in (1) Center for Substance Abuse Prevention-developed education materials, and (2) HHS guidance on improving care for infants with neonatal abstinence syndrome and their families.</p><p>Under current law, the WIC program includes certain education\u00a0related to drug abuse. This bill replaces references to drug abuse with substance use disorder.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr3743"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3743ih.xml"
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
      "title": "Supporting Healthy Mothers and Infants Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Healthy Mothers and Infants Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Nutrition Act of 1966 to support women, infants, and children impacted by substance use disorder, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T06:48:51Z"
    }
  ]
}
```
