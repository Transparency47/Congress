# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4074
- Title: Optimizing Postpartum Outcomes Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4074
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2026-05-13T08:06:47Z
- Update date including text: 2026-05-13T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4074",
    "number": "4074",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Optimizing Postpartum Outcomes Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:47Z",
    "updateDateIncludingText": "2026-05-13T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:02:40Z",
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
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "MA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
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
      "sponsorshipDate": "2025-07-07",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "OR"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NJ"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
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
      "sponsorshipDate": "2025-07-29",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "AR"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CO"
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
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "MD"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NM"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "IA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "HI"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "RI"
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
      "sponsorshipDate": "2025-10-08",
      "state": "NC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "DE"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "ME"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
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
      "sponsorshipDate": "2025-12-05",
      "state": "IN"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "CT"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "PA"
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
      "sponsorshipDate": "2026-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4074ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4074\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Bacon (for himself and Mrs. Trahan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to issue guidance on coverage under the Medicaid program under title XIX of the Social Security Act of certain pelvic health services furnished during the postpartum period, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Optimizing Postpartum Outcomes Act of 2025 .\n#### 2. CMS guidance\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue guidance on coverage under State plans (or waivers of such plans) under the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) or State child health plans (or waivers of such plans) under the Children\u2019s Health Insurance Program under title XXI of such Act ( 42 U.S.C. 1397aa et seq. ) of covered pelvic health services furnished during the prenatal or postpartum period. Such guidance shall include\u2014\n**(1)**\nbest practices from States with respect to innovative or evidenced-based payment models to increase access to covered pelvic health services;\n**(2)**\nrecommendations for States on available financing options under\u2014\n**(A)**\nthe Medicaid program under title XIX of such Act ( 42 U.S.C. 1396 et seq. ); and\n**(B)**\nthe Children\u2019s Health Insurance Program under title XXI of such Act ( 42 U.S.C. 1397aa et seq. ), specifically funds made available through a Children\u2019s Health Insurance Program Health Services Initiative;\n**(3)**\nguidance and technical assistance to State agencies responsible for administering State plans (or waivers of such plans) under the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) regarding additional flexibilities and incentives related to screening and referral for, and access to, covered pelvic health services; and\n**(4)**\nguidance regarding suggested terminology and diagnosis codes, such as the International Classification of Diseases code set, to identify women with pelvic floor dysfunction and disorders.\n##### (b) GAO study\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall conduct a study on, and submit to Congress a report that addresses, gaps in coverage for\u2014\n**(1)**\ncovered pelvic health services under State plans (or waivers of such plans) under the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) for postpartum women; and\n**(2)**\nother services for postpartum women who received medical assistance under a State plan (or a waiver of such plan) under the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) during their pregnancy.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term postpartum period means the longer of the period of lactation or the 6-month period beginning on the last day of a woman\u2019s pregnancy.\n**(2)**\nThe term covered pelvic health services means\u2014\n**(A)**\npelvic floor examinations (as defined in section 317L\u20132 of the Public Health Service Act, as added by section 2 of this Act); and\n**(B)**\npelvic health physical therapy (as defined in such section 317L\u20132).\n#### 3. Postpartum pelvic health education campaign\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by inserting after section 317L\u20131 ( 42 U.S.C. 247b\u201313a ) the following:\n317L\u20132. Postpartum pelvic health education campaign (a) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, in collaboration with the Administrator of the Health Resources and Services Administration and the heads of other agencies, and in consultation with appropriate health professional associations, shall develop and carry out a program\u2014 (1) to educate and train health professionals on pelvic floor examinations and the benefits of pelvic health physical therapy; and (2) to educate postpartum women on\u2014 (A) with respect to pelvic floor examinations\u2014 (i) the importance of such examinations during the postpartum period; (ii) how to obtain such an examination, including information relating to obtaining referrals; and (iii) what is involved in such an examination; and (B) with respect to pelvic health physical therapy\u2014 (i) the benefits of, and availability of such physical therapy; and (ii) how to obtain a referral for such physical therapy. (b) Definitions In this section: (1) The term pelvic floor examination means an examination to assess a patient for pelvic health related conditions that is composed of\u2014 (A) an external evaluation that includes analysis of posture, joint integrity, muscle performance, quality of movement, and palpation and observation of the pelvic floor; and (B) if deemed necessary based on the health care professional\u2019s clinical reasoning, an internal vaginal or rectal examination, or both, to gather relevant information about the tone, strength, control, ability to contract and relax the muscles of the pelvic floor individually and together, the condition of the surrounding fascia, and the position of the organs. (2) The term pelvic health physical therapy means a personalized physical therapy plan implemented by a pelvic health physical therapist, after performing a pelvic floor examination and making a diagnosis, that is based on best available evidence to improve the patient condition, with respect to the anatomy of the pelvic floor, improve mobility, recover from injury, prevent future injury, and manage pain and chronic conditions. (3) The term pelvic health related condition includes urinary dysfunction, bowel dysfunction, musculoskeletal dysfunction, sexual dysfunction, cancer-related rehabilitation, and the pre-partum state and pre-partum conditions. (c) Authorization of appropriations There are authorized to be appropriated to carry out this section $2,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-06-23",
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
        "updateDate": "2025-07-17T10:45:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-23",
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
          "measure-id": "id119hr4074",
          "measure-number": "4074",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-23",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4074v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Optimizing Postpartum Outcomes Act of </strong><strong>2025</strong></p><p>This bill requires (1) the Centers for Medicare & Medicaid Services to issue guidance to support coverage of prenatal and postpartum pelvic health services under Medicaid and the Children's Health Insurance Program (CHIP), (2) the Government Accountability Office to study gaps in Medicaid coverage of these and other services for postpartum women, and (3) the Centers for Disease Control and Prevention to educate health professionals and postpartum women on pelvic health services.</p>"
        },
        "title": "Optimizing Postpartum Outcomes Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4074.xml",
    "summary": {
      "actionDate": "2025-06-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Optimizing Postpartum Outcomes Act of </strong><strong>2025</strong></p><p>This bill requires (1) the Centers for Medicare & Medicaid Services to issue guidance to support coverage of prenatal and postpartum pelvic health services under Medicaid and the Children's Health Insurance Program (CHIP), (2) the Government Accountability Office to study gaps in Medicaid coverage of these and other services for postpartum women, and (3) the Centers for Disease Control and Prevention to educate health professionals and postpartum women on pelvic health services.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr4074"
    },
    "title": "Optimizing Postpartum Outcomes Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Optimizing Postpartum Outcomes Act of </strong><strong>2025</strong></p><p>This bill requires (1) the Centers for Medicare & Medicaid Services to issue guidance to support coverage of prenatal and postpartum pelvic health services under Medicaid and the Children's Health Insurance Program (CHIP), (2) the Government Accountability Office to study gaps in Medicaid coverage of these and other services for postpartum women, and (3) the Centers for Disease Control and Prevention to educate health professionals and postpartum women on pelvic health services.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr4074"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4074ih.xml"
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
      "title": "Optimizing Postpartum Outcomes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Optimizing Postpartum Outcomes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to issue guidance on coverage under the Medicaid program under title XIX of the Social Security Act of certain pelvic health services furnished during the postpartum period, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T09:18:30Z"
    }
  ]
}
```
