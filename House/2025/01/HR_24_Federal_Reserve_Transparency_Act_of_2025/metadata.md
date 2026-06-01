# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/24?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/24
- Title: Federal Reserve Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 24
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-01-14T02:56:57Z
- Update date including text: 2026-01-14T02:56:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/24",
    "number": "24",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Federal Reserve Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T02:56:57Z",
    "updateDateIncludingText": "2026-01-14T02:56:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:27:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "B000825",
      "district": "3",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CO"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OK"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MO"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "VA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AR"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OH"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "KS"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "PA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "VA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "WY"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "SC"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001218",
      "district": "6",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MI"
    },
    {
      "bioguideId": "M001212",
      "district": "2",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "SC"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AL"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "S000929",
      "district": "5",
      "firstName": "Victoria",
      "fullName": "Rep. Spartz, Victoria [R-IN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Spartz",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IN"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KY"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MD"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WI"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr24ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 24\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Massie (for himself, Mr. Biggs of Arizona , Ms. Boebert , Mr. Bost , Mr. Brecheen , Mr. Burchett , Mr. Burlison , Mrs. Cammack , Mr. Cline , Mr. Cloud , Mr. Collins , Mr. Crane , Mr. Crawford , Mr. Davidson , Mr. Estes , Mr. Finstad , Mr. Fitzpatrick , Mr. Gosar , Ms. Greene of Georgia , Mr. Griffith , Ms. Hageman , Mrs. Luna , Ms. Mace , Mr. McClintock , Mr. McCormick , Mrs. Miller of Illinois , Mr. Moolenaar , Mr. Moore of Alabama , Mr. Norman , Mr. Ogles , Mr. Palmer , Mr. Perry , Mr. Roy , Mr. Rutherford , Mrs. Spartz , Mr. Steube , Ms. Tenney , Mr. Weber of Texas , and Mr. Webster of Florida ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require a full audit of the Board of Governors of the Federal Reserve System and the Federal reserve banks by the Comptroller General of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Reserve Transparency Act of 2025 .\n#### 2. Audit reform and transparency for the board of governors of the Federal Reserve System\n##### (a) In general\nNotwithstanding section 714 of title 31, United States Code, or any other provision of law, the Comptroller General of the United States shall complete an audit of the Board of Governors of the Federal Reserve System and the Federal reserve banks under subsection (b) of such section 714 within 12 months after the date of the enactment of this Act.\n##### (b) Report\n**(1) In general**\nNot later than 90 days after the audit required pursuant to subsection (a) is completed, the Comptroller General\u2014\n**(A)**\nshall submit to Congress a report on such audit; and\n**(B)**\nshall make such report available to the Speaker of the House, the majority and minority leaders of the House of Representatives, the majority and minority leaders of the Senate, the Chairman and Ranking Member of the committee and each subcommittee of jurisdiction in the House of Representatives and the Senate, and any other Member of Congress who requests the report.\n**(2) Contents**\nThe report under paragraph (1) shall include a detailed description of the findings and conclusion of the Comptroller General with respect to the audit that is the subject of the report, together with such recommendations for legislative or administrative action as the Comptroller General may determine to be appropriate.\n##### (c) Repeal of certain limitations\nSubsection (b) of section 714 of title 31, United States Code, is amended by striking the second sentence.\n##### (d) Technical and conforming amendments\n**(1) In general**\nSection 714 of title 31, United States Code, is amended\u2014\n**(A)**\nin subsection (d)(3), by striking or (f) each place such term appears;\n**(B)**\nin subsection (e), by striking the third undesignated paragraph of section 13 and inserting section 13(3) ; and\n**(C)**\nby striking subsection (f).\n**(2) Federal Reserve Act**\nSubsection (s) (relating to Federal Reserve Transparency and Release of Information ) of section 11 of the Federal Reserve Act ( 12 U.S.C. 248 ) is amended\u2014\n**(A)**\nin paragraph (4)(A), by striking has the same meaning as in section 714(f)(1)(A) of title 31, United States Code and inserting means a program or facility, including any special purpose vehicle or other entity established by or on behalf of the Board of Governors of the Federal Reserve System or a Federal reserve bank, authorized by the Board of Governors under section 13(3), that is not subject to audit under section 714(e) of title 31, United States Code ;\n**(B)**\nin paragraph (6), by striking or in section 714(f)(3)(C) of title 31, United States Code, the information described in paragraph (1) and information concerning the transactions described in section 714(f) of such title, and inserting the information described in paragraph (1) ; and\n**(C)**\nin paragraph (7), by striking and section 13(3)(C), section 714(f)(3)(C) of title 31, United States Code, and and inserting , section 13(3)(C), and .",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-12-11",
        "text": "Committee on Homeland Security and Governmental Affairs. Hearings held."
      },
      "number": "2327",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Reserve Transparency Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-06-03T18:05:47Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-06-03T18:05:47Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T18:05:47Z"
          },
          {
            "name": "Federal Reserve System",
            "updateDate": "2025-06-03T18:05:47Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-03T18:05:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-03T15:23:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr24",
          "measure-number": "24",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr24v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Reserve Transparency Act of 2025</strong></p><p>This bill directs the Government Accountability Office (GAO) to complete, within 12 months, an audit of the Federal Reserve Board and Federal Reserve banks. In addition, the bill allows the GAO to audit the Federal Reserve Board and Federal Reserve banks with respect to (1) international financial transactions; (2) deliberations, decisions,\u00a0or actions on monetary policy matters; (3) transactions made under the direction of the Federal Open Market Committee; and (4) discussions or communications among Federal Reserve officers, board members, and employees regarding any of these matters.</p><p></p>"
        },
        "title": "Federal Reserve Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr24.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Reserve Transparency Act of 2025</strong></p><p>This bill directs the Government Accountability Office (GAO) to complete, within 12 months, an audit of the Federal Reserve Board and Federal Reserve banks. In addition, the bill allows the GAO to audit the Federal Reserve Board and Federal Reserve banks with respect to (1) international financial transactions; (2) deliberations, decisions,\u00a0or actions on monetary policy matters; (3) transactions made under the direction of the Federal Open Market Committee; and (4) discussions or communications among Federal Reserve officers, board members, and employees regarding any of these matters.</p><p></p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr24"
    },
    "title": "Federal Reserve Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Reserve Transparency Act of 2025</strong></p><p>This bill directs the Government Accountability Office (GAO) to complete, within 12 months, an audit of the Federal Reserve Board and Federal Reserve banks. In addition, the bill allows the GAO to audit the Federal Reserve Board and Federal Reserve banks with respect to (1) international financial transactions; (2) deliberations, decisions,\u00a0or actions on monetary policy matters; (3) transactions made under the direction of the Federal Open Market Committee; and (4) discussions or communications among Federal Reserve officers, board members, and employees regarding any of these matters.</p><p></p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr24"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr24ih.xml"
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
      "title": "Federal Reserve Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Reserve Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a full audit of the Board of Governors of the Federal Reserve System and the Federal reserve banks by the Comptroller General of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T06:18:28Z"
    }
  ]
}
```
