# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4641?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4641
- Title: Keep Kids Covered Act
- Congress: 119
- Bill type: HR
- Bill number: 4641
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:53:49Z
- Update date including text: 2025-12-05T22:53:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4641",
    "number": "4641",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Keep Kids Covered Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:53:49Z",
    "updateDateIncludingText": "2025-12-05T22:53:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:02:00Z",
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
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "LA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CO"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-26",
      "state": "HI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CO"
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
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MN"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4641ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4641\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Castor of Florida (for herself, Mr. Tran , Ms. Schrier , Mr. Ruiz , Mr. Veasey , Ms. Barrag\u00e1n , Mrs. Fletcher , Mr. Landsman , Ms. Schakowsky , Ms. McClellan , Mr. Soto , Mr. Carter of Louisiana , Ms. Matsui , and Mrs. Trahan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend titles XIX and XXI of the Social Security Act to provide for continuous eligibility for certain children under the Medicaid program and the Children\u2019s Health Insurance Program.\n#### 1. Short title\nThis Act may be cited as the Keep Kids Covered Act .\n#### 2. Requiring States to provide for continuous eligibility for children under Medicaid and CHIP\n##### (a) Continuous eligibility for deemed newborns until age 6\n**(1) Medicaid**\nSection 1902(e)(4) of the Social Security Act ( 42 U.S.C. 1396a(e)(4) ) is amended by striking one year and inserting 6 years .\n**(2) CHIP**\nSection 2112(e) of the Social Security Act ( 42 U.S.C. 1397ll(e) ) is amended by striking 1 year of age and inserting 6 years of age (except that such a child who is enrolled under the State child health plan or waiver may be transferred to the Medicaid program under title XIX for the remaining duration of the 6-year continuous eligibility period, if the child becomes eligible for full benefits under title XIX during such period) .\n##### (b) Continuous eligibility for children under age 19 and former foster youth\n**(1) Medicaid**\nSection 1902(e)(12) of the Social Security Act ( 42 U.S.C. 1396a(e)(12) ) is amended\u2014\n**(A)**\nin the paragraph heading, by striking 1 year of continuous and inserting Continuous ;\n**(B)**\nin the text preceding subparagraph (A), by inserting has attained the age of 6 and after an individual who ;\n**(C)**\nin subparagraph (A), by striking the 12-month period and inserting the 24-month period ;\n**(D)**\nby redesignating subparagraphs (A) through (C) as clauses (i) through (iii), respectively, and adjusting the margins accordingly;\n**(E)**\nby striking The State plan and inserting:\n(A) Children under age 6 The State plan (or waiver of such State plan) shall provide that an individual who is under the age of 6 and who is determined to be eligible for benefits under a State plan (or waiver of such plan) approved under this title under subsection (a)(10)(A) shall remain eligible for such benefits until the earlier of\u2014 (i) the time that such individual attains the age of 6; or (ii) the date that such individual ceases to be a resident of such State. (B) Children ages 6 through 18 The State plan ; and\n**(F)**\nby adding at the end the following new subparagraph:\n(C) Former foster youth The State plan (or waiver of such State plan) shall provide that an individual who is determined to be eligible for benefits under a State plan (or waiver of such plan) approved under this title under subsection (a)(10)(A)(i)(IX) shall remain eligible for such benefits until the earlier of\u2014 (i) the time that such individual attains the age of 26; or (ii) the date that such individual ceases to be a resident of such State. .\n**(2) CHIP**\nSection 2107(e)(1)(L) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(L) ), as redesignated by section 71103(b)(1) of Public Law 119\u201321 , is amended\u2014\n**(A)**\nby striking 1 year of ; and\n**(B)**\nby striking 12-month and inserting applicable .\n##### (c) Updating contact information during continuous eligibility period\n**(1) Medicaid**\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ), as amended by sections 71103(a)(1) and 71104 of Public Law 119\u201321 , is amended\u2014\n**(A)**\nin paragraph (88), by striking and at the end;\n**(B)**\nin paragraph (89), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (89) the following new paragraph:\n(90) provide for a process\u2014 (A) to obtain, not less frequently than annually, the up-to-date contact information for individuals enrolled under such plan (or a waiver of such plan) who have been so enrolled for a period of longer than 12 months pursuant to a continuous eligibility provision under this title; and (B) to inform each such individual of their enrollment under such plan (or waiver) pursuant to such continuous eligibility provision and of the remaining duration of the applicable period of continuous eligibility. .\n**(2) CHIP**\nSection 2107(e)(1) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1) ), as amended by sections 71103(b)(1) and 71109(b) of Public Law 119\u201321 , is amended\u2014\n**(A)**\nby redesignating subparagraphs (I) through (W) as subparagraphs (J) through (X), respectively; and\n**(B)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) Section 1902(a)(90) (relating to the verification of contact information and provision of information regarding enrollment during a period of continuous eligibility). .\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date that is 1 year after the date of the enactment of this section.\n#### 3. Adjusting application of provision providing coverage continuity for former foster children up to age 26 under Medicaid\nSection 1002(a)(2) of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 1396a note) is amended by striking shall take effect with respect to and all that follows through the period at the end and inserting the following:\nshall apply\u2014 (A) beginning January 1, 2023, with respect to foster youth who attain 18 years of age on or after such date; and (B) beginning on the date that is 180 days after the date of enactment of the Keep Kids Covered Act, with respect to foster youth not described in subparagraph (A). .",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2496",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keep Kids Covered Act",
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
        "updateDate": "2025-09-17T16:42:06Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4641ih.xml"
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
      "title": "Keep Kids Covered Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Kids Covered Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XIX and XXI of the Social Security Act to provide for continuous eligibility for certain children under the Medicaid program and the Children's Health Insurance Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:31Z"
    }
  ]
}
```
