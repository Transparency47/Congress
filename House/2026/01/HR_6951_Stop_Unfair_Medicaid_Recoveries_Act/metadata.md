# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6951?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6951
- Title: Stop Unfair Medicaid Recoveries Act
- Congress: 119
- Bill type: HR
- Bill number: 6951
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-04-22T08:07:27Z
- Update date including text: 2026-04-22T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6951",
    "number": "6951",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Stop Unfair Medicaid Recoveries Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:27Z",
    "updateDateIncludingText": "2026-04-22T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-06",
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
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
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
          "date": "2026-01-06T23:32:05Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TN"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TX"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NY"
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
      "sponsorshipDate": "2026-01-06",
      "state": "DC"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "IL"
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
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "ME"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "IL"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "IL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "WA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "FL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "WI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6951ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6951\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2026 Ms. Schakowsky (for herself, Ms. Barrag\u00e1n , Ms. Castor of Florida , Mrs. Cherfilus-McCormick , Mr. Cohen , Mr. Doggett , Ms. Garcia of Texas , Mr. Goldman of New York , Ms. Norton , Ms. Kelly of Illinois , Ms. Matsui , Ms. Ocasio-Cortez , Ms. Omar , Ms. Pingree , Mr. Quigley , Mrs. Ramirez , Ms. Strickland , Mr. Tonko , Mrs. Trahan , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to repeal the requirement that States establish a Medicaid Estate Recovery Program and to limit the circumstances in which a State may place a lien on a Medicaid beneficiary\u2019s property.\n#### 1. Short title\nThis Act may be cited as the Stop Unfair Medicaid Recoveries Act .\n#### 2. Liens, adjustments, and recoveries for medical assistance\n##### (a) Liens\nSection 1917(a) of the Social Security Act ( 42 U.S.C. 1396p(a) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking plan, except\u2014 and inserting plan, except, subject to paragraph (4)\u2014 ; and\n**(B)**\nin subparagraph (B), by striking in the case of and inserting with respect to liens imposed before the date of the enactment of the Stop Unfair Medicaid Recoveries Act, in the case of ; and\n**(2)**\nby adding at the end the following:\n(4) Notwithstanding any preceding provision of this subsection, not later than 90 days after the date of the enactment of this paragraph, a State shall\u2014 (A) withdraw any lien imposed under paragraph (1)(B) that is in effect as of such date; and (B) notify each individual (or legal representative of such individual (or of such individual\u2019s estate)) subject to such a lien so withdrawn of the withdrawal of such lien. .\n##### (b) Adjustments and recoveries\nSection 1917(b) of the Social Security Act ( 42 U.S.C. 1396p(b) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking except that and inserting except that, subject to paragraph (6), ; and\n**(2)**\nby adding at the end the following:\n(6) Notwithstanding any preceding provision of this subsection, no adjustment or recovery of any medical assistance correctly paid on behalf of an individual under the State plan may be initiated, maintained, or collected on or after the date of the enactment of this paragraph. Not later than 90 days after such date, a State shall\u2014 (A) withdraw any lien in effect as of such date with respect to such medical assistance correctly paid; and (B) notify each individual (or legal representative of such individual (or of such individual\u2019s estate)) subject to such a lien so withdrawn of the withdrawal of such lien and the prohibition on adjustment or recovery under this paragraph. .",
      "versionDate": "2026-01-06",
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
        "updateDate": "2026-01-09T15:28:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-06",
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
          "measure-id": "id119hr6951",
          "measure-number": "6951",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-06",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6951v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2026-01-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Unfair Medicaid Recoveries Act\u00a0</strong></p><p>This bill prohibits state Medicaid programs from using estate recovery to recoup the costs of benefits. States must withdraw property liens within 90 days of the bill's enactment and notify affected individuals of the\u00a0withdrawals.</p>"
        },
        "title": "Stop Unfair Medicaid Recoveries Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6951.xml",
    "summary": {
      "actionDate": "2026-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Unfair Medicaid Recoveries Act\u00a0</strong></p><p>This bill prohibits state Medicaid programs from using estate recovery to recoup the costs of benefits. States must withdraw property liens within 90 days of the bill's enactment and notify affected individuals of the\u00a0withdrawals.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6951"
    },
    "title": "Stop Unfair Medicaid Recoveries Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Unfair Medicaid Recoveries Act\u00a0</strong></p><p>This bill prohibits state Medicaid programs from using estate recovery to recoup the costs of benefits. States must withdraw property liens within 90 days of the bill's enactment and notify affected individuals of the\u00a0withdrawals.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6951"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6951ih.xml"
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
      "title": "Stop Unfair Medicaid Recoveries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T06:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Unfair Medicaid Recoveries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to repeal the requirement that States establish a Medicaid Estate Recovery Program and to limit the circumstances in which a State may place a lien on a Medicaid beneficiary's property.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T06:03:14Z"
    }
  ]
}
```
