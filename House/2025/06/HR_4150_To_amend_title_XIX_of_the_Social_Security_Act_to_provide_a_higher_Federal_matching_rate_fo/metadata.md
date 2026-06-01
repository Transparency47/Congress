# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4150
- Title: Advancing Maternal Health Equity Under Medicaid Act
- Congress: 119
- Bill type: HR
- Bill number: 4150
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-11-26T09:05:45Z
- Update date including text: 2025-11-26T09:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4150",
    "number": "4150",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Advancing Maternal Health Equity Under Medicaid Act",
    "type": "HR",
    "updateDate": "2025-11-26T09:05:45Z",
    "updateDateIncludingText": "2025-11-26T09:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:02:20Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "OR"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "DC"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-25",
      "state": "VA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "WI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NC"
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
      "sponsorshipDate": "2025-06-25",
      "state": "AL"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NM"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MI"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "FL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "WA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "TX"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NJ"
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
      "sponsorshipDate": "2025-07-02",
      "state": "NC"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "TN"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4150ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4150\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Ms. Williams of Georgia (for herself, Ms. Bonamici , Ms. Chu , Ms. Norton , Mr. Huffman , Ms. McClellan , Ms. Moore of Wisconsin , Ms. Ross , Ms. Sewell , Ms. Stansbury , Ms. Tlaib , Ms. Wasserman Schultz , Ms. Strickland , Mr. Morelle , and Mr. Kennedy of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to provide a higher Federal matching rate for increased expenditures under Medicaid for maternal health care services.\n#### 1. Short title\nThis Act may be cited as the Advancing Maternal Health Equity Under Medicaid Act .\n#### 2. Higher FMAP for increased expenditures under medicaid for maternal health services\nSection 1903 of the Social Security Act ( 42 U.S.C. 1396b ) is amended\u2014\n**(1)**\nin subsection (a)(5)\u2014\n**(A)**\nby striking an amount equal and inserting (A) an amount equal ; and\n**(B)**\nby adding at the end the following:\nand (B) for calendar quarters beginning on or after January 1 of the year beginning after one year after the date of the enactment of this subparagraph, an amount equal to 90 percent of the amounts by which\u2014 (i) the sum of the amounts expended which are attributable to the offering, arranging, and furnishing (directly or on a contract basis) under the State plan (or waiver of the plan) of maternal health care services (as described in subsection (b)(6)(B)) for such quarter, exceeds (ii) the sum of the amounts expended which are attributable to the offering, arranging, and furnishing (directly or on a contract basis) under the State plan (or waiver of the plan) of such services for the corresponding quarter in the four-quarter period ending on December 31, 2019, plus ; and\n**(2)**\nin subsection (b), by adding at the end the following new paragraph:\n(6) Accountability and maintenance of effort requirements for additional federal funding for increased expenditures for maternal health care services (A) In general As conditions for receiving the funds the Secretary is otherwise obligated to pay to a State under subsection (a)(5)(B), a State shall meet the following requirements: (i) Supplement, not supplant The State shall use the funds received under such subsection to supplement, not supplant, the level of State funds expended for the offering, arranging, and furnishing (directly or on a contract basis) under the State plan (or under a waiver of the plan) of maternal health care services (as described in subparagraph (B)) through programs and activities in effect as of January 1, 2023. (ii) Use of funds for activities that improve delivery of maternal health care services The State shall use the funds received under such subsection for activities that increase the capacity, efficiency, and quality in the provision of maternal health care services. (B) Definitions For purposes of this paragraph and subsection (a)(5)(B): (i) Maternal health care services Maternal health care services described in this subparagraph are services furnished by a maternity care provider or perinatal health worker, such as the following: (I) Prenatal, labor and delivery, and postpartum health care services that are furnished in a licensed and accredited hospital, birth center, midwifery practice, or other health care practice that provides prenatal services, labor and delivery services, and postpartum services. (II) Telehealth services during the prenatal and postpartum periods. (III) Home visiting services during the prenatal and postpartum periods. (IV) Mental or behavioral health care services for individuals during the prenatal and postpartum periods. (ii) Maternity care provider The term maternity care provider means a health care provider who\u2014 (I) is a physician, physician assistant, midwife who meets at a minimum the international definition of the midwife and global standards for midwifery education as established by the International Confederation of Midwives, nurse practitioner, or clinical nurse specialist; and (II) has a focus on maternal or perinatal health. (iii) Perinatal health worker The term perinatal health worker means a doula, community health worker, breastfeeding and lactation educator or counselor, nutritionist or dietitian, childbirth educator, social worker, home visitor, or language interpreter. (iv) Postpartum and postpartum period The terms postpartum and postpartum period each refer to the 1-year period beginning on the last day of the pregnancy of an individual. .",
      "versionDate": "2025-06-25",
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
        "updateDate": "2025-07-17T11:01:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-25",
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
          "measure-id": "id119hr4150",
          "measure-number": "4150",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-25",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4150v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Advancing Maternal Health Equity Under Medicaid Act</b></p> <p>This bill provides a 90% federal matching rate for Medicaid maternal health care expenditures that exceed 2019 levels. Qualifying services must be provided by maternity care providers or perinatal health workers (e.g., doulas) and include prenatal and postpartum telehealth services, home visits, and behavioral health care.</p>"
        },
        "title": "Advancing Maternal Health Equity Under Medicaid Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4150.xml",
    "summary": {
      "actionDate": "2025-06-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Advancing Maternal Health Equity Under Medicaid Act</b></p> <p>This bill provides a 90% federal matching rate for Medicaid maternal health care expenditures that exceed 2019 levels. Qualifying services must be provided by maternity care providers or perinatal health workers (e.g., doulas) and include prenatal and postpartum telehealth services, home visits, and behavioral health care.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr4150"
    },
    "title": "Advancing Maternal Health Equity Under Medicaid Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-25",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Advancing Maternal Health Equity Under Medicaid Act</b></p> <p>This bill provides a 90% federal matching rate for Medicaid maternal health care expenditures that exceed 2019 levels. Qualifying services must be provided by maternity care providers or perinatal health workers (e.g., doulas) and include prenatal and postpartum telehealth services, home visits, and behavioral health care.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr4150"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4150ih.xml"
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
      "title": "Advancing Maternal Health Equity Under Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Maternal Health Equity Under Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to provide a higher Federal matching rate for increased expenditures under Medicaid for maternal health care services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:22Z"
    }
  ]
}
```
