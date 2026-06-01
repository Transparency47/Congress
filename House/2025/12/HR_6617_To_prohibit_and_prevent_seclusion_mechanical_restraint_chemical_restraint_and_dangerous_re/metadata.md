# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6617?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6617
- Title: Keeping All Students Safe Act
- Congress: 119
- Bill type: HR
- Bill number: 6617
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-20T08:08:41Z
- Update date including text: 2026-05-20T08:08:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6617",
    "number": "6617",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Keeping All Students Safe Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:41Z",
    "updateDateIncludingText": "2026-05-20T08:08:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-11T16:01:35Z",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "VA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "OR"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
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
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "WA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-11",
      "state": "NC"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "OH"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
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
      "sponsorshipDate": "2025-12-11",
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
      "sponsorshipDate": "2025-12-11",
      "state": "FL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "WA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "ME"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PR"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "WI"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "IN"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "MA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "VT"
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
      "sponsorshipDate": "2026-03-04",
      "state": "DC"
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
      "sponsorshipDate": "2026-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "OH"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "OH"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6617ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6617\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Beyer (for himself, Mr. Hamadeh of Arizona , Mr. Scott of Virginia , Mr. Lynch , Mr. Davis of Illinois , Mr. Peters , Ms. Bonamici , Ms. McCollum , Ms. Tlaib , Mr. Castro of Texas , Mrs. McBath , Ms. Dean of Pennsylvania , Ms. Schakowsky , Ms. DelBene , Ms. Simon , Ms. Chu , Ms. Ross , Mr. DeSaulnier , Mr. Moulton , Ms. Brown , Mr. Evans of Pennsylvania , Ms. Barrag\u00e1n , Ms. Castor of Florida , Ms. S\u00e1nchez , Ms. Jayapal , Mr. Vicente Gonzalez of Texas , Mrs. Hayes , Ms. Pingree , Ms. Lee of Pennsylvania , and Mr. Hern\u00e1ndez ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit and prevent seclusion, mechanical restraint, chemical restraint, and dangerous restraints that restrict breathing, and to prevent and reduce the use of physical restraint in schools, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Keeping All Students Safe Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Prohibitions on restraint and seclusion and additional requirements\nSec. 101. Prohibition, additional requirements.\nTITLE II\u2014State plan, reporting requirements, and grants for State educational agencies\nSec. 201. Definitions.\nSec. 202. State plan.\nSec. 203. Grants for State educational agencies.\nTITLE III\u2014General provisions\nSec. 301. National assessment.\nSec. 302. Protection and advocacy systems.\nSec. 303. Schools operated or funded by the Department of the Interior or the Department of Defense.\nSec. 304. Rule of construction.\nSec. 305. Applicability to private schools and home schools.\nSec. 306. Severability.\nSec. 307. Authorization of appropriations.\n#### 2. Definitions\nIn this Act:\n**(1) Chemical restraint**\nThe term chemical restraint means a drug or medication used on a student to control behavior or restrict freedom of movement that is not\u2014\n**(A)**\nprescribed by a licensed physician, or other qualified health professional acting under the scope of the professional\u2019s authority under State law, for the standard treatment of a student\u2019s medical or psychiatric condition; and\n**(B)**\nadministered as prescribed by the licensed physician or other qualified health professional acting under the scope of the professional\u2019s authority under State law.\n**(2) ESEA terms**\nThe terms early childhood education program , educational service agency , elementary school , local educational agency , other staff , paraprofessional , parent , school leader , secondary school , specialized instructional support personnel , State , and State educational agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Law enforcement officer**\nThe term law enforcement officer \u2014\n**(A)**\nmeans any person who\u2014\n**(i)**\nis a State, Tribal, or local law enforcement officer (as defined in section 1204 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10284 )); and\n**(ii)**\nis assigned by the employing law enforcement agency to a program, who is contracting with a program, or who is employed by a program; and\n**(B)**\nincludes an individual referred to as a school resource officer if that individual meets the definition in subparagraph (A).\n**(4) Mechanical restraint**\nThe term mechanical restraint means the use of devices as a means of restricting a student\u2019s freedom of movement.\n**(5) Physical escort**\nThe term physical escort means the temporary touching or holding of the hand, wrist, arm, shoulder, or back for the purpose of inducing a student who is acting out to walk to a safe location.\n**(6) Physical restraint**\nThe term physical restraint means a personal restriction that immobilizes or reduces the ability of an individual to move the individual\u2019s arms, legs, torso, or head freely, except that such term does not include a physical escort, mechanical restraint, or chemical restraint.\n**(7) Positive behavioral interventions and supports**\nThe term positive behavioral interventions and supports \u2014\n**(A)**\nmeans a schoolwide, systematic approach that embeds evidence-based practices and data-driven decision making to improve school climate and culture in order to achieve improved academic and social outcomes and increase learning for all students (including students with the most complex and intensive behavioral needs); and\n**(B)**\nencompasses a range of systemic and individualized positive strategies to teach and reinforce school-expected behaviors, while discouraging and diminishing undesirable behaviors.\n**(8) Program**\nThe term program means\u2014\n**(A)**\nall of the operations of a local educational agency, system of vocational education, or other school system;\n**(B)**\na program that serves children who receive services for which financial assistance is provided in accordance with the Head Start Act ( 42 U.S.C. 9831 et seq. ); or\n**(C)**\nan elementary school or secondary school that is not a public school that enrolls a student who receives special education and related services under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ).\n**(9) Program personnel**\n**(A) In General**\nSubject to subparagraph (B), the term program personnel means any agent of a program, including an individual who is employed by a program, or who performs services for a program on a contractual basis, including\u2014\n**(i)**\nschool leaders;\n**(ii)**\nteachers;\n**(iii)**\nspecialized instructional support personnel;\n**(iv)**\nparaprofessionals; or\n**(v)**\nother staff.\n**(B) Exclusion**\nNotwithstanding subparagraph (A), program personnel shall not include a law enforcement officer or a school security guard.\n**(10) Protection and advocacy system**\nThe term protection and advocacy system means a protection and advocacy system established under section 143 of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15043 ).\n**(11) School security guard**\nThe term school security guard means an individual who is not a sworn law enforcement officer and who is responsible for addressing one or more of the following safety and crime prevention activities in and around a program:\n**(A)**\nAssisting program personnel in safety incidents.\n**(B)**\nEducating students in crime and illegal drug use prevention and safety.\n**(C)**\nDeveloping or expanding community justice initiatives for students.\n**(D)**\nTraining students in conflict resolution and supporting restorative justice programs.\n**(E)**\nServing as a liaison between the program and outside agencies, including other law enforcement agencies.\n**(F)**\nScreening students or visitors to the program for prohibited items.\n**(12) Seclusion**\nThe term seclusion means the involuntary confinement of a student alone in a room or area from which the student is physically prevented from leaving, except that such term does not include a time out.\n**(13) Secretary**\nThe term Secretary means the Secretary of Education.\n**(14) Special education school**\nThe term special education school means a school that focuses primarily on serving the needs of students with disabilities under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ) or section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ).\n**(15) State-approved crisis intervention training program**\nThe term State-approved crisis intervention training program means a training program approved by a State and the Secretary that, at a minimum, provides\u2014\n**(A)**\ntraining in evidence-based techniques shown to be effective in the prevention of physical restraint;\n**(B)**\nevidence-based skills training related to positive behavioral interventions and supports, safe physical escort, conflict prevention, understanding antecedents, deescalation, and conflict management;\n**(C)**\ntraining in evidence-based techniques shown to be effective in keeping both school personnel and students safe when imposing physical restraint;\n**(D)**\ntraining in first aid and cardiopulmonary resuscitation;\n**(E)**\ninformation describing State policies and procedures to ensure compliance with section 101; and\n**(F)**\ncertification for school personnel, law enforcement officers, and school security guards in the techniques and skills described in subparagraphs (A) through (D), which shall be required to be renewed on a periodic basis.\n**(16) Student**\nThe term student means\u2014\n**(A)**\nfor purposes of title I, a student enrolled in a program; and\n**(B)**\nfor purposes of title II, a student enrolled in an elementary school or secondary school.\n**(17) Time out**\n**(A) In general**\nThe term time out means a behavior management technique that may involve the separation of the student from the group or classroom in a non-locked setting.\n**(B) Clarification**\nThe term time out does not include\u2014\n**(i)**\nseclusion; or\n**(ii)**\na separation of the student described in subparagraph (A) from which such student is physically or otherwise prohibited from leaving.\nI\nProhibitions on restraint and seclusion and additional requirements\n#### 101. Prohibition, additional requirements\n##### (a) Prohibition\nNo student shall be subjected to unlawful seclusion or restraint by program personnel, a law enforcement officer, or a school security guard, while attending any program that receives Federal financial assistance.\n##### (b) Unlawful seclusion or restraint defined\n**(1) In general**\nIn this section, the term unlawful seclusion or restraint means\u2014\n**(A)**\nseclusion;\n**(B)**\nmechanical restraint;\n**(C)**\nchemical restraint;\n**(D)**\nphysical restraint or physical escort that is life threatening, that restricts breathing, or that restricts blood flow to the brain, including prone and supine restraint;\n**(E)**\nphysical restraint that is contraindicated based on the student\u2019s disability, health care needs, or medical or psychiatric condition, as documented in\u2014\n**(i)**\na health care directive or medical management plan;\n**(ii)**\na behavior intervention plan;\n**(iii)**\nan individualized education program or an individualized family service plan (as defined in section 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 ));\n**(iv)**\na plan developed pursuant to section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) or title II of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ); or\n**(v)**\nanother relevant record made available to the State or program involved; or\n**(F)**\nphysical restraint that is not in compliance with subsection (e)(1).\n**(2) Not included**\nThe term unlawful seclusion or restraint shall not include\u2014\n**(A)**\na time out; or\n**(B)**\na device implemented by trained school personnel, or utilized by a student, for the specific and approved therapeutic or safety purposes for which such devices were designed and, if applicable, prescribed, provided that such devices are not used to purposefully cause a student pain as a means of behavioral modification, including\u2014\n**(i)**\nrestraints for medical immobilization;\n**(ii)**\nadaptive devices or mechanical supports used to achieve proper body position, balance, or alignment to allow greater freedom of mobility than would be possible without the use of such devices or mechanical supports; or\n**(iii)**\nvehicle safety restraints when used as intended during the transport of a student in a moving vehicle.\n##### (c) Private right of action\n**(1) In general**\nA student who has been subjected to unlawful seclusion or restraint in violation of subsection (a), or the parent of such student, may file a civil action against the program under which the violation is alleged to have occurred in an appropriate district court of the United States or in State court for declaratory judgement, injunctive relief, compensatory relief, attorneys\u2019 fees, or expert fees.\n**(2) Limitation on liability**\nProgram personnel shall not be liable to any person in a proceeding described in paragraph (1) or in an arbitration proceeding for a violation of subsection (a).\n**(3) No sovereign immunity**\nNo program shall be immune under the Eleventh Amendment of the Constitution of the United States from suit in Federal or State court for a violation of subsection (a) of this section.\n##### (d) Enforcement\n**(1) Investigations**\n**(A) In General**\nThe Secretary shall address any complaints alleging a violation of subsection (a) by an entity described in subparagraphs (A) or (C) of section 2(8) for an appropriate investigation.\n**(B) Head Start**\nThe Secretary of Health and Human Services shall address any complaints alleging a violation of subsection (a) by an entity described in section 2(8)(B) for an appropriate investigation.\n**(2) Withholding payments**\nIn the event a student has been subjected to unlawful seclusion or restraint in violation of subsection (a), the Secretary shall withhold from the program under which the violation occurred, in whole or in part, further payments (including payments for administrative costs) in accordance with section 455 of the General Education Provisions Act ( 20 U.S.C. 1234d ).\n**(3) Head start programs**\nThe Secretary of Health and Human Services, in coordination with the Secretary, shall\u2014\n**(A)**\nensure that entities described in section 2(8)(B) meet the requirements described in subsection (e);\n**(B)**\npromulgate regulations with respect to how the reporting requirements described in section 202(b) shall be carried out with respect to Head Start agencies (including Early Head Start agencies) under the Head Start Act ( 42 U.S.C. 9801 et seq. ); and\n**(C)**\nin the event a student served by a program that serves children who receive services for which financial assistance is provided in accordance with the Head Start Act ( 42 U.S.C. 9831 et seq. ) has been subjected to unlawful seclusion or restraint in violation of subsection (a), withhold from the program under which the violation occurred, in whole or in part, further payments (including payments for administrative costs) in accordance with section 646 of the Head Start Act ( 42 U.S.C. 9841 ).\n##### (e) Additional Requirements\nThe Secretary shall ensure that each program that receives Federal financial assistance meets the following requirements:\n**(1) Physical restraint**\nThe use of physical restraint by any program personnel, a school security guard, or a law enforcement officer shall be considered in compliance with the requirements of this subsection only if each of the following requirements are met:\n**(A)**\nThe student\u2019s behavior poses an imminent danger of serious physical injury to the student, program personnel, a school security guard, a law enforcement officer, or another individual.\n**(B)**\nBefore using physical restraint, less restrictive interventions would be ineffective in stopping such imminent danger of serious physical injury.\n**(C)**\nSuch physical restraint is imposed by\u2014\n**(i)**\nprogram personnel, a school security guard, or a law enforcement officer trained and certified by a State-approved crisis intervention training program; or\n**(ii)**\nprogram personnel, a school security guard, or a law enforcement officer not trained and certified as described in clause (i), in the case of a rare and clearly unavoidable emergency circumstance when program personnel, a school security guard, or a law enforcement officer trained and certified as described in clause (i) is not immediately available due to the unforeseeable nature of the emergency circumstance.\n**(D)**\nSuch physical restraint ends immediately upon the cessation of the imminent danger of serious physical injury to the student, any program personnel, a school security guard, a law enforcement officer, or another individual.\n**(E)**\nThe physical restraint does not interfere with the student\u2019s ability to communicate in the student\u2019s primary language or primary mode of communication.\n**(F)**\nDuring the physical restraint, the least amount of force necessary is used to protect the student or others from the threatened injury.\n**(2) Training**\nEach State, in consultation with program officials and State Directors of Head Start Collaboration (as described in section 642B of the Head Start Act ( 42 U.S.C. 9837b )), shall ensure that a sufficient number of program personnel are trained and certified by a State-approved crisis intervention training program to meet the needs of the specific student population in each program.\n**(3) Prohibition on planned intervention**\nThe use of physical restraint as a planned intervention shall not be written into a student\u2019s education plan, individual safety plan, behavioral intervention plan, or individualized education program (as defined in section 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 )), except that a program may establish policies and procedures for use of physical restraint in program safety or crisis plans, provided that such a plan is not specific to any individual student.\n**(4) Procedures following physical restraint**\nEach program shall establish procedures to be followed after an incident involving the imposition of physical restraint upon a student, which shall include each of the following:\n**(A)**\nProcedures to provide to the parent of the student, with respect to such incident\u2014\n**(i)**\nan immediate verbal or electronic communication, as soon as is practicable and not later than the same day as the incident; and\n**(ii)**\nwritten notification, as soon as is practicable, and not later than 24 hours after the incident that shall include, at minimum\u2014\n**(I)**\na description of the incident, including precipitating events;\n**(II)**\npositive interventions used prior to restraint;\n**(III)**\nthe length of time of restraint; and\n**(IV)**\na description of the serious physical injury of the student or others that occurred or was about to occur that necessitated the use of restraint.\n**(B)**\nA meeting between parents of the student and the program, as soon as is practicable, and not later than 5 school days following the incident (unless such meeting is delayed by written mutual agreement of the parent and program)\u2014\n**(i)**\nwhich meeting shall include, at a minimum\u2014\n**(I)**\nthe parent of such student;\n**(II)**\nthe student involved (if appropriate);\n**(III)**\nthe program personnel, law enforcement officer, or school security guard who imposed the restraint;\n**(IV)**\na teacher of such student;\n**(V)**\na program leader of such student; and\n**(VI)**\nan expert on behavior interventions, who may be a special education teacher;\n**(ii)**\nthe purpose of which shall be to discuss the incident, as described by both the student and the program personnel, law enforcement officer, or school security guard involved, including\u2014\n**(I)**\nany precipitating events;\n**(II)**\nhow the incident occurred; and\n**(III)**\nprior positive behavioral interventions and supports used to deescalate the situation; and\n**(iii)**\nwhich meeting shall include\u2014\n**(I)**\nthe discussion of proactive strategies to prevent future need for the use of physical restraint;\n**(II)**\n**(aa)**\nfor a student identified as eligible to receive accommodations under section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ) or title II of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ), or accommodations or special education or related services under the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ), a discussion of the need for a functional behavioral assessment and a behavior intervention plan; or\n**(bb)**\nfor a student not identified as eligible to receive accommodations under the provisions of law described in item (aa), evidence of a referral for such accommodations or special education or related services, or documentation of the basis for declining to make such a referral for the student; and\n**(III)**\nproviding to the parent, for use during the meeting, a written statement from each adult witness who was in the proximity of the student immediately before and during the time of the physical restraint, but was not directly involved in such restraint.\nII\nState plan, reporting requirements, and grants for State educational agencies\n#### 201. Definitions\nIn this title:\n**(1) School**\nThe term school means an elementary school, secondary school, or special education school.\n**(2) Head Start program**\nThe term Head Start program means a program that serves children who receive services for which financial assistance is provided in accordance with the Head Start Act ( 42 U.S.C. 9831 et seq. ).\n#### 202. State plan\n##### (a) State plan\nNot later than 2 years after the date of enactment of this Act and each year thereafter, each State educational agency shall submit to the Secretary a State plan that provides\u2014\n**(1)**\ndemonstrations to the Secretary that the State has in effect\u2014\n**(A)**\nState policies and procedures that comply with section 101, including with respect to State-approved crisis intervention training programs; and\n**(B)**\na State mechanism to effectively monitor and enforce compliance with section 101;\n**(2)**\na description of the State policies and procedures, including a description of the State-approved crisis intervention training programs in such State and how the State ensures accurate and timely reporting to the Department of Education;\n**(3)**\na description of the State plan to ensure program personnel, students, and parents (including private school personnel, students, and parents) are aware of the State policies and procedures;\n**(4)**\na description of the State activities described in the State\u2019s plan under section 1111(g) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(g) ) that reduce aversive behavioral interventions and improve school conditions;\n**(5)**\nfor public comment\u2014\n**(A)**\nnot less than 60 days prior to submission of the State plan, which shall provide stakeholders with the opportunity to provide written comments on the State plan, which shall be included in the State plan, including\u2014\n**(i)**\nhow the policies and procedures comply with section 101;\n**(ii)**\nthe policies and procedures related to State-approved crisis intervention programs;\n**(iii)**\ntraining provided to program personnel; and\n**(iv)**\nnotification procedures for parents; and\n**(B)**\nnotice of which shall be provided in an accessible format, which is compliant with the most recent Web Content Accessibility Guidelines, or successor guidelines, for stakeholders and posted on a website;\n**(6)**\nwritten response to the public comments provided by stakeholders under paragraph (5); and\n**(7)**\na description of State oversight of schools that includes\u2014\n**(A)**\nmonitoring use of restraint in the schools;\n**(B)**\nmonitoring compliance with the prohibition on seclusion in schools;\n**(C)**\nnot less than every 6 months, discussions between State educational agency officials and school leaders to examine the progress of reducing the use of physical restraint in schools;\n**(D)**\nnot less than annual site visits to the special education schools in the State; and\n**(E)**\ntechnical assistance to focus on the use of proactive, positive behavioral interventions and supports.\n##### (b) Reporting\n**(1) Reporting requirements**\nNot later than 2 years after the date of enactment of this Act, and each year thereafter\u2014\n**(A)**\neach State educational agency shall (in compliance with the requirements of section 444 of the General Education Provisions Act (commonly known as the Family Educational Rights and Privacy Act of 1974) ( 20 U.S.C. 1232g )) prepare and submit to the Secretary, and make available to the public, a report that includes the information described in paragraph (2), with respect to each local educational agency, each special education school, and each school not under the jurisdiction of a local educational agency, located in the same State as such State educational agency; and\n**(B)**\neach Head Start agency (including each Early Head Start agency) designated under the Head Start Act ( 42 U.S.C. 9831 et seq. ) shall prepare and submit to the Secretary and the Secretary of Health and Human Services, and make available to the public, a report that includes the information described in paragraph (2), except that\u2014\n**(i)**\nsuch information shall be provided with respect to each program served by the agency and with respect to children enrolled in Head Start programs; and\n**(ii)**\nthe information described in subclause (II)(bb), subclause (III), and subclause (IV) of paragraph (2)(B)(i) shall not be required.\n**(2) Information requirements**\n**(A) General information requirements**\nThe report described in paragraph (1) shall include with respect to physical restraint imposed upon students in the preceding full academic or program year\u2014\n**(i)**\nthe total number of such incidents;\n**(ii)**\nthe total number of students upon whom such physical restraint was imposed;\n**(iii)**\nin the case in which such physical restraint was imposed more than twice on a student, the number of times such student or child was so restrained; and\n**(iv)**\nthe total number of such incidents where the use of physical restraint is referred to law enforcement.\n**(B) Disaggregation**\n**(i) General disaggregation requirements**\nThe information described in subparagraph (A) shall be disaggregated as follows:\n**(I)**\nWith respect to the total number of incidents in which physical restraint was imposed upon a student, disaggregated by each of the following:\n**(aa)**\nBy those that resulted in injury.\n**(bb)**\nBy those that resulted in death.\n**(cc)**\nBy those in which the program personnel imposing physical restraint was not trained and certified, as described in section 101(e)(1)(C)(i).\n**(II)**\nBy the demographic characteristics of all students upon whom physical restraint was imposed, including disaggregation\u2014\n**(aa)**\nby each major racial and ethnic group, economically disadvantaged students as compared to students who are not economically disadvantaged, English proficiency status, and sex;\n**(bb)**\nby students with an individualized education program under section 614(d) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1414(d) );\n**(cc)**\nby students who have a plan developed pursuant to section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ); and\n**(dd)**\nby students who have a plan developed pursuant to title II of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ).\n**(III)**\nBy the total number of incidents of physical restraint in which a law enforcement officer or school security guard was involved, which may include the law enforcement officer or school security guard imposing the physical restraint or assisting with the physical restraint.\n**(IV)**\nBy the type of school, including disaggregation by special education school, charter school, and private school.\n**(ii) Unduplicated count; exception**\nThe information and disaggregation required under subparagraphs (A) and (B) shall\u2014\n**(I)**\nbe carried out in a manner to ensure an unduplicated count of the total number of incidents in the preceding full academic year in which physical restraint was imposed upon a student; and\n**(II)**\nnot be required in a case in which the number of students in a category would reveal personally identifiable information about an individual student.\n#### 203. Grants for State educational agencies\n##### (a) Grants authorized\n**(1) In general**\nFrom the amount appropriated under section 307 to carry out this section for a fiscal year, the Secretary shall award grants to State educational agencies with an application approved under subsection (c), on the basis of their relative need, as determined with the Secretary in accordance with paragraph (2), to assist the State educational agencies in\u2014\n**(A)**\nestablishing, implementing, and enforcing the policies and procedures that ensure compliance with section 101;\n**(B)**\nimproving State and local capacity to collect and analyze data related to physical restraint; and\n**(C)**\nimproving school climate and culture by implementing schoolwide positive behavioral interventions and supports, mental health supports, restorative justice programs, trauma-informed care, and crisis and de-escalation interventions.\n**(2) Determination of relative need**\nIn determining the relative need of State educational agencies under paragraph (1), the Secretary shall consider\u2014\n**(A)**\nthe physical restraint and seclusion incidents that occurred at a school served by the State educational agencies for the most recent academic year for which data are available;\n**(B)**\nthe capacity needs of the State educational agency and the local educational agencies served by the State educational agency to collect and analyze the data described in paragraph (1)(B); and\n**(C)**\nwhether the State educational agency has been carrying out the activities described in paragraph (1)(C) and, if so, how the activities are being implemented.\n**(3) Report**\nThe Secretary shall provide a report to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives not later than 60 days after the date the Secretary awards a grant to a State under this section detailing why the State was chosen and how the criteria described in subparagraphs (A), (B), and (C) of paragraph (2) were applied to select the State.\n##### (b) Duration of grant\nA grant under this section shall be awarded to a State educational agency for a 3-year period.\n##### (c) Application\n**(1) In general**\nTo be eligible to receive a grant under this section, each State educational agency desiring a grant shall submit an application to the Secretary at such time, in such manner, and accompanied by such information as the Secretary may require.\n**(2) Contents**\nEach application submitted under paragraph (1) shall include\u2014\n**(A)**\nthe total number of incidents in which physical restraint was imposed upon students for the most recent school year;\n**(B)**\nthe total number of incidents in which seclusion was imposed upon students for the most recent school year;\n**(C)**\na description of the State\u2019s data collection policies and procedures;\n**(D)**\na description of crisis intervention or prevention trainings used in the State to prevent or reduce physical restraint and seclusion (if applicable);\n**(E)**\na description of statewide initiatives regarding school climate and culture (if applicable), such as schoolwide positive behavioral interventions and supports, mental health supports, restorative justice programs, trauma-informed care, and crisis and de-escalation interventions;\n**(F)**\na description of activities to be funded under the grant and the goals of such activities, including how the activities will eliminate seclusion and reduce and prevent physical restraint; and\n**(G)**\na description of how the activities under the grant will coordinate and align with current Federal, State, and local policies, programs, or activities regarding seclusion and physical restraint, crisis intervention, and school climate or culture.\n##### (d) Authority To make subgrants\n**(1) In general**\nA State educational agency receiving a grant under this section may use such grant funds to award subgrants, in the manner determined by the State educational agency, to local educational agencies served by the State educational agency.\n**(2) Application**\nA local educational agency desiring to receive a subgrant under this section shall submit an application to the applicable State educational agency at such time, in such manner, and containing such information as the State educational agency may require.\n**(3) Early childhood education program participation**\nA local educational agency receiving subgrant funds under this section shall ensure that educators working in an early childhood education program, as defined in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 ), may participate, to the extent practicable, on an equitable basis in activities supported by subgrant funds under this section that are trainings on developmentally appropriate practices for meeting the needs of young children.\n##### (e) Private school participation\n**(1) In general**\nA local educational agency receiving subgrant funds under this section shall, after timely and meaningful consultation with appropriate private school officials, ensure that private school personnel may participate, on an equitable basis, in activities supported by subgrant funds under this section.\n**(2) Public control of funds**\nThe control of grant and subgrant funds under this section, and title to materials, equipment, and property purchased with such funds, shall be in a public agency for the uses and purposes provided in this Act, and a public agency shall administer such funds, materials, equipment, and property.\n**(3) Provision of services**\n**(A) In general**\nServices described under this section shall be provided\u2014\n**(i)**\nby employees of a public agency; or\n**(ii)**\nthrough contract by the public agency with an individual or entity.\n**(B) Independence; public agency**\nAn individual or entity described in subparagraph (A)(ii) that contracts with a public agency to provide services under this section shall be independent of a private school and of any religious organization. Individuals providing such services shall be employed by and under the control and supervision of the public agency.\n**(C) Commingling of funds prohibited**\nFunds used to provide services under this section shall not be commingled with non-Federal funds.\n##### (f) Required activities\nA State educational agency receiving a grant, or a local educational agency receiving a subgrant, under this section shall use such grant or subgrant funds to carry out the following:\n**(1)**\nEstablishing and implementing policies to prohibit seclusion, mechanical restraint, chemical restraint, and other forms of prohibited restraint in schools, consistent with section 101.\n**(2)**\nImplementing and evaluating strategies and procedures to prevent seclusion and to prevent and reduce physical restraint in schools, consistent with such policies.\n**(3)**\nProviding professional development, training, and certification for school personnel to comply with such policies.\n**(4)**\nAnalyzing the information included in a report prepared under section 202(b) to identify student, school personnel, and school needs related to preventing seclusion, and preventing and reducing the use of physical restraint.\n**(5)**\nProviding training to school security guards and, as appropriate, school personnel, on how to comply with education and civil rights laws, including the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ) and the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ), when interacting with students with disabilities, including, when conducting disciplinary actions involving students with disabilities.\n##### (g) Additional authorized activities\nIn addition to the required activities described in subsection (f), a State educational agency receiving a grant, or a local educational agency receiving a subgrant, under this section may use such grant or subgrant funds for one or more of the following:\n**(1)**\nDeveloping and implementing high-quality professional development and training programs to implement evidence-based systematic approaches to schoolwide positive behavioral interventions and supports, including improving coaching, facilitation, and training capacity for administrators, school leaders, teachers, specialized instructional support personnel, paraprofessionals, and other staff.\n**(2)**\nProviding technical assistance to implement evidence-based systematic approaches to schoolwide positive behavioral interventions and supports, including technical assistance for data-driven decision making related to behavioral supports and interventions in the classroom.\n**(3)**\nResearching, evaluating, and disseminating high-quality evidence-based programs and activities that implement schoolwide positive behavioral interventions and supports with fidelity.\n**(4)**\nSupporting other local positive behavioral interventions and supports implementation activities consistent with this subsection.\n**(5)**\nDeveloping, implementing, and providing technical assistance to support evidence-based programs that reduce the likelihood of physical restraint, such as mental health supports, restorative justice programs, trauma-informed care, and crisis and de-escalation interventions.\n##### (h) Evaluation and report\nEach State educational agency receiving a grant under this section shall, at the end of the 3-year grant period for such grant\u2014\n**(1)**\nevaluate the State\u2019s progress toward the elimination of seclusion and the prevention and reduction of physical restraint in the schools located in the State, consistent with section 101;\n**(2)**\nsubmit to the Secretary a report on such progress; and\n**(3)**\npublish such report on the State educational agency website in an accessible format.\nIII\nGeneral provisions\n#### 301. National assessment\n##### (a) National assessment\nThe Secretary shall carry out a national assessment to determine the effectiveness of this Act, which shall include\u2014\n**(1)**\nanalyzing data related to incidents of physical restraint in schools and programs that serve children who receive services for which financial assistance is provided in accordance with the Head Start Act ( 42 U.S.C. 9831 et seq. ) (referred to in this title as Head Start programs );\n**(2)**\nanalyzing the effectiveness of Federal, State, and local efforts to eliminate seclusion and prevent and reduce the number of physical restraint incidents in schools and Head Start programs;\n**(3)**\nidentifying the types of programs and services that have demonstrated the greatest effectiveness in eliminating and preventing seclusion and preventing and reducing the number of physical restraint incidents in schools and Head Start programs; and\n**(4)**\nidentifying evidence-based personnel training models with demonstrated success in preventing seclusion and preventing and reducing the number of physical restraint incidents in schools and Head Start programs, including models that emphasize positive behavioral interventions and supports and de-escalation techniques over physical intervention.\n##### (b) Report\nThe Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Education and Workforce of the House of Representatives\u2014\n**(1)**\nnot later than 3 years after the date of the enactment of this Act, an interim report that summarizes the preliminary findings of the assessment described in subsection (a); and\n**(2)**\nnot later than 5 years after the date of the enactment of this Act, a final report of the findings of the assessment.\n#### 302. Protection and advocacy systems\n##### (a) Notification\nIn a case in which physical injury or death of a student or of a child enrolled in a Head Start program occurs in conjunction with the use of seclusion or physical restraint or any intervention used to control behavior at a school or Head Start program, the local educational agency serving such school or the agency administering a Head Start program under the Head Start Act ( 42 U.S.C. 9801 et seq. ) shall have procedures to\u2014\n**(1)**\nnotify, in writing, not later than 24 hours after such injury or death occurs\u2014\n**(A)**\nthe State educational agency, or in the case of an agency administering a Head Start program, the appropriate official at the Department of Health and Human Services;\n**(B)**\nthe local law enforcement agency; and\n**(C)**\nthe relevant protection and advocacy system; and\n**(2)**\nprovide any information that the protection and advocacy system may require.\n##### (b) Restatement of authority\nProtection and advocacy systems shall have the same authorities and rights provided under subtitle C of title I of the Developmental Disabilities Assistance and Bill of Rights Act of 2000 ( 42 U.S.C. 15041 et seq. ) with respect to protections provided for students or children enrolled in Head Start programs under this Act when such students or children are otherwise eligible to be clients of the protection and advocacy system, including investigating, monitoring, and enforcing such protections.\n#### 303. Schools operated or funded by the Department of the Interior or the Department of Defense\n##### (a) Schools operated or funded by Department of the Interior\nThe Secretary of the Interior shall promulgate regulations to ensure that schools operated or funded by the Department of the Interior comply with the requirements of title I and section 202(b).\n##### (b) Schools operated or funded by the Department of Defense\nThe Secretary of Defense shall promulgate regulations to ensure that schools operated or funded by the Department of Defense Education Activity or otherwise operated or funded by the Department of Defense for the education of military-connected dependents (as described in subparagraph (B) or (D)(i) of section 7003(a)(1) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7703(a)(1) )) comply with the requirements of title I and section 202(b).\n#### 304. Rule of construction\nSubject to section 101(e), nothing in this Act shall be construed to prohibit a sworn law enforcement officer with probable cause from arresting a student for violating a Federal or State criminal law.\n#### 305. Applicability to private schools and home schools\n##### (a) Private schools\nNothing in this Act shall be construed to affect any private school that does not receive, or does not serve students who receive, support in any form from any program or activity supported, in whole or in part, with Federal funds.\n##### (b) Home schools\nNothing in this Act shall be construed to\u2014\n**(1)**\naffect a home school, whether or not a home school is treated as a private school or home school under State law; or\n**(2)**\nconsider parents who are schooling a child at home as program personnel.\n#### 306. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of the provisions of such to any person or circumstance shall not be affected thereby.\n#### 307. Authorization of appropriations\nThere are authorized to be appropriated $40,000,000 for each of fiscal years 2026 through 2030 to carry out this Act.",
      "versionDate": "2025-12-11",
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
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3448",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Keeping All Students Safe Act",
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
        "name": "Education",
        "updateDate": "2026-01-07T18:56:03Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6617ih.xml"
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
      "title": "Keeping All Students Safe Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keeping All Students Safe Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit and prevent seclusion, mechanical restraint, chemical restraint, and dangerous restraints that restrict breathing, and to prevent and reduce the use of physical restraint in schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T07:18:26Z"
    }
  ]
}
```
