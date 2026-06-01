# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/137
- Title: TCJA Permanency Act
- Congress: 119
- Bill type: HR
- Bill number: 137
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-04-21T15:02:20Z
- Update date including text: 2026-04-21T15:02:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/137",
    "number": "137",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TCJA Permanency Act",
    "type": "HR",
    "updateDate": "2026-04-21T15:02:20Z",
    "updateDateIncludingText": "2026-04-21T15:02:20Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-01-03T16:25:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NE"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IL"
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
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "WV"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
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
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OH"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IN"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OH"
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MS"
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
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NV"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "ID"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "WI"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NC"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OH"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MS"
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "KY"
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "UT"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MO"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SC"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IN"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "IN"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-07",
      "state": "PA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "NJ"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr137ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 137\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Buchanan (for himself, Mr. Smith of Nebraska , Mr. LaHood , Mr. Estes , Mrs. Miller of West Virginia , Mr. Kustoff , Ms. Tenney , Ms. Van Duyne , Mr. Feenstra , Mr. Carey , Mr. Yakym , Mr. Moran , Mr. Miller of Ohio , Mr. Rutherford , Mr. Crenshaw , Mr. Guest , Mr. Moolenaar , Mr. Amodei of Nevada , Mr. Fulcher , Mr. Ellzey , Mr. Grothman , Mr. Meuser , Mr. Clyde , Mr. Rouzer , Mrs. Hinson , Mr. Rulli , Mr. Ezell , Mr. Bost , Mr. Barr , Mr. Weber of Texas , and Mr. Carter of Georgia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to make permanent certain provisions of the Tax Cuts and Jobs Act affecting individuals, families, and small businesses, and for other purposes.\n#### 1. Short title, etc\n##### (a) Short title\nThis Act may be cited as the TCJA Permanency Act .\n##### (b) Amendment of 1986 code\nExcept as otherwise expressly provided, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a section or other provision, the reference shall be considered to be made to a section or other provision of the Internal Revenue Code of 1986.\n##### (c) References to the Tax Cuts and Jobs Act\nTitle I of Public Law 115\u201397 may be cited as the Tax Cuts and Jobs Act .\n##### (d) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title, etc.\nTitle I\u2014Individual reform made permanent\nSubtitle A\u2014Rate reform\nSec. 101. Modification of rates.\nSubtitle B\u2014Deduction for qualified business income of pass-Thru entities\nSec. 111. Deduction for qualified business income.\nSec. 112. Limitation on losses for taxpayers other than corporations.\nSubtitle C\u2014Tax benefits for families and individuals\nSec. 121. Increase in standard deduction.\nSec. 122. Increase in and modification of child tax credit.\nSec. 123. Increased limitation for certain charitable contributions.\nSec. 124. Increased contributions to ABLE accounts.\nSec. 125. Rollovers to ABLE programs from 529 programs.\nSec. 126. Treatment of certain individuals performing services in the Sinai Peninsula of Egypt.\nSubtitle D\u2014Education\nSec. 131. Treatment of student loan discharges.\nSec. 132. 529 account funding for homeschool and additional elementary and secondary expenses.\nSubtitle E\u2014Deductions and exclusions\nSec. 141. Repeal of deduction for personal exemptions.\nSec. 142. Limitation on deduction for State and local, etc., taxes.\nSec. 143. Limitation on deduction for qualified residence interest.\nSec. 144. Modification of deduction for personal casualty losses.\nSec. 145. Termination of miscellaneous itemized deductions.\nSec. 146. Repeal of overall limitation on itemized deductions.\nSec. 147. Termination of exclusion for qualified bicycle commuting reimbursement.\nSec. 148. Qualified moving expense reimbursement exclusion limited to members of Armed Forces.\nSec. 149. Deduction for moving expenses limited to members of Armed Forces.\nSec. 150. Limitation on wagering losses.\nSubtitle F\u2014Increase in estate and gift tax exemption\nSec. 151. Increase in estate and gift tax exemption.\nTitle II\u2014Increased exemption for Alternative Minimum Tax made permanent\nSec. 201. Increased exemption for individuals.\nI\nIndividual reform made permanent\nA\nRate reform\n#### 101. Modification of rates\n##### (a) Married individuals filing joint returns and surviving spouses\nSection 1(a) is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $19,050 10% of taxable income. Over $19,050 but not over $77,400 $1,905, plus 12% of the excess over $19,050. Over $77,400 but not over $165,000 $8,907, plus 22% of the excess over $77,400. Over $165,000 but not over $315,000 $28,179, plus 24% of the excess over $165,000. Over $315,000 but not over $400,000 $64,179, plus 32% of the excess over $315,000. Over $400,000 but not over $600,000 $91,379, plus 35% of the excess over $400,000. Over $600,000 $161,379, plus 37% of the excess over $600,000. .\n##### (b) Heads of households\nSection 1(b) is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $13,600 10% of taxable income. Over $13,600 but not over $51,800 $1,360, plus 12% of the excess over $13,600. Over $51,800 but not over $82,500 $5,944, plus 22% of the excess over $51,800. Over $82,500 but not over $157,500 $12,698, plus 24% of the excess over $82,500. Over $157,500 but not over $200,000 $30,698, plus 32% of the excess over $157,500. Over $200,000 but not over $500,000 $44,298, plus 35% of the excess over $200,000. Over $500,000 $149,298, plus 37% of the excess over $500,000. .\n##### (c) Unmarried individuals other than surviving spouses and heads of households\nSection 1(c) is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $9,525 10% of taxable income. Over $9,525 but not over $38,700 $952.50, plus 12% of the excess over $9,525. Over $38,700 but not over $82,500 $4,453.50, plus 22% of the excess over $38,700. Over $82,500 but not over $157,500 $14,089.50, plus 24% of the excess over $82,500. Over $157,500 but not over $200,000 $32,089.50, plus 32% of the excess over $157,500. Over $200,000 but not over $500,000 $45,689.50, plus 35% of the excess over $200,000. Over $500,000 $150,689.50, plus 37% of the excess over $500,000. .\n##### (d) Married individuals filing separate returns\nSection 1(d) is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $9,525 10% of taxable income. Over $9,525 but not over $38,700 $952.50, plus 12% of the excess over $9,525. Over $38,700 but not over $82,500 $4,453.50, plus 22% of the excess over $38,700. Over $82,500 but not over $157,500 $14,089.50, plus 24% of the excess over $82,500. Over $157,500 but not over $200,000 $32,089.50, plus 32% of the excess over $157,500. Over $200,000 but not over $300,000 $45,689.50, plus 35% of the excess over $200,000. Over $300,000 $80,689.50, plus 37% of the excess over $300,000. .\n##### (e) Estates and trusts\nSection 1(e) is amended by striking the table contained therein and inserting the following:\nIf taxable income is: The tax is: Not over $2,550 10% of taxable income. Over $2,550 but not over $9,150 $255, plus 24% of the excess over $2,550. Over $9,150 but not over $12,500 $1,839, plus 35% of the excess over $9,150. Over $12,500 $3,011.50, plus 37% of the excess over $12,500. .\n##### (f) Inflation adjustments\nSection 1(f) is amended\u2014\n**(1)**\nby amending paragraph (2)(A) to read as follows:\n(A) by increasing the minimum and maximum dollar amounts for each bracket for which a tax is imposed under such table by the cost-of-living adjustment for such calendar year, determined under this subsection for such calendar year by substituting \u20182017\u2019 for \u20182016\u2019 in paragraph (3)(A)(ii), ,\n**(2)**\nby amending paragraph (7) to read as follows:\n(7) Rounding (A) In general Except as provided in subparagraph (B), if any increase determined under paragraph (2)(A) is not a multiple of $25, such increase shall be rounded to the next lowest multiple of $25. (B) Joint returns, etc In the case of a table prescribed under subsection (a), subparagraph (A) shall be applied by substituting $50 for $25 both places it appears. ,\n**(3)**\nby striking paragraph (8), and\n**(4)**\nin the heading, by striking Phaseout of marriage penalty in 15-percent bracket; adjustments and inserting Adjustments .\n##### (g) Application of income tax brackets to capital gains brackets\nSection 1(h) is amended\u2014\n**(1)**\nin paragraph (1)(B)(i), by striking 25 percent and inserting 22 percent ,\n**(2)**\nin paragraph (1)(C)(ii)(I), by striking which would (without regard to this paragraph) be taxed at a rate below 39.6 percent and inserting below the maximum 15-percent rate amount , and\n**(3)**\nby adding at the end the following new paragraphs:\n(12) Maximum 15-percent rate amount defined For purposes of this subsection, the maximum 15-percent rate amount shall be\u2014 (A) in the case of a joint return or surviving spouse (as defined in section 2(a)), $479,000 ( \u00bd such amount in the case of a married individual filing a separate return), (B) in the case of an individual who is a head of household (as defined in section 2(b)), $452,400, (C) in the case of any other individual (other than an estate or trust), $425,800, and (D) in the case of an estate or trust, $12,700. (13) Determination of 0 percent rate bracket for estates and trusts In the case of any estate or trust, paragraph (1)(B) shall be applied by treating the amount determined in clause (i) thereof as being equal to $2,600. (14) Inflation adjustment (A) In general Each of the dollar amounts in paragraphs (12) and (13) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under subsection (f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2017 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under subparagraph (A) is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. .\n##### (h) Conforming amendments\n**(1)**\nSection 1 is amended by striking subsections (i) and (j).\n**(2)**\nSection 3402(q)(1) is amended by striking third lowest and inserting fourth lowest .\n##### (i) Application of section 15\n**(1) In general**\nSubsection (a) of section 15 is amended by striking If any rate of tax and inserting In the case of a corporation, if any rate of tax .\n**(2) Conforming amendments**\n**(A)**\nSection 15 is amended by striking subsections (d) and (f).\n**(B)**\nSection 6013(c) is amended by striking sections 15, 443, and 7851(a)(1)(A) and inserting section 443 .\n**(C)**\nThe heading of section 15 is amended by inserting on corporations after Effect of changes .\n**(D)**\nThe table of sections for part III of subchapter A of chapter 1 is amended by striking the item relating to section 15 and inserting the following new item:\nSec. 15. Effect of changes on corporations. .\n##### (j) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n**(2) Application of section 15**\nSection 15 of the Internal Revenue Code of 1986 shall not apply to any change in a rate of tax by reason of\u2014\n**(A)**\nsection 1(j) of such Code (as in effect before its repeal by this section), or\n**(B)**\nany amendment made by this Act.\nB\nDeduction for qualified business income of pass-Thru entities\n#### 111. Deduction for qualified business income\n##### (a) In general\nSection 199A is amended by striking subsection (i).\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 112. Limitation on losses for taxpayers other than corporations\n##### (a) In general\nSection 461 is amended\u2014\n**(1)**\nby amending subsection (l)(1) to read as follows:\n(1) Limitation In the case of a taxpayer other than a corporation, any excess business loss of the taxpayer for the taxable year shall not be allowed. , and\n**(2)**\nby striking subsection (j) and redesignating subsections (k) and (l) (as amended) as subsections (j) and (k), respectively.\n##### (b) Conforming amendments\n**(1)**\nSection 58(a)(2)(A) is amended by striking 461(k) and inserting 461(j) .\n**(2)**\nSection 461(i)(4) is amended by striking subsection (k) and inserting subsection (j) .\n**(3)**\nSection 464(d)(2)(B)(iii) is amended by striking section 461(k)(2)(E) and inserting section 461(j)(2)(E) .\n**(4)**\nSubparagraphs (B) and (C) of section 1256(e)(3) are each amended by striking section 461(k)(4) and inserting section 461(j)(4) .\n**(5)**\nSection 1258(d)(5)(C) is amended by striking section 461(k)(4) and inserting section 461(j)(4) .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\nC\nTax benefits for families and individuals\n#### 121. Increase in standard deduction\n##### (a) In general\nSection 63(c)(2) is amended\u2014\n**(1)**\nby striking $4,400 in subparagraph (B) and inserting $18,000 , and\n**(2)**\nby striking $3,000 in subparagraph (C) and inserting $12,000 .\n##### (b) Inflation adjustment\nSection 63(c)(4) is amended to read as follows:\n(4) Adjustments for inflation (A) In general Each dollar amount in paragraph (2)(B), (2)(C), or (5) or subsection (f) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting for 2016 in subparagraph (A)(ii) thereof\u2014 (I) in the case of the dollar amounts contained in paragraph (2)(B) or (2)(C), 2017 , (II) in the case of the dollar amounts contained in paragraph (5)(A) or subsection (f), 1987 , and (III) in the case of the dollar amount contained in paragraph (5)(B), 1997 . (B) Rounding If any increase under subparagraph (A) is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. .\n##### (c) Conforming amendment\nSection 63(c) is amended by striking paragraph (7).\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 122. Increase in and modification of child tax credit\n##### (a) In general\nSection 24 is amended by striking subsections (a), (b), and (c) and inserting the following new subsections:\n(a) Allowance of credit There shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the sum of\u2014 (1) $2,000 for each qualifying child of the taxpayer, and (2) $500 for each qualifying dependent (other than a qualifying child) of the taxpayer. (b) Limitation based on adjusted gross income The amount of the credit allowable under subsection (a) shall be reduced (but not below zero) by $50 for each $1,000 (or fraction thereof) by which the taxpayer's modified adjusted gross income exceeds $400,000 in the case of a joint return ($200,000 in any other case). For purposes of the preceding sentence, the term \u201cmodified adjusted gross income\u201d means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. (c) Qualifying child; qualifying dependent For purposes of this section\u2014 (1) Qualifying child The term qualifying child means any qualifying dependent of the taxpayer\u2014 (A) who is a qualifying child (as defined in section 7706(c)) of the taxpayer, (B) who has not attained age 17 at the close of the calendar year in which the taxable year of the taxpayer begins, and (C) whose name and social security number are included on the taxpayer\u2019s return of tax for the taxable year. (2) Qualifying dependent The term qualifying dependent means any dependent of the taxpayer (as defined in section 7706 without regard to all that follows resident of the United States in section 7706(b)(3)(A)) whose name and TIN are included on the taxpayer\u2019s return of tax for the taxable year. (3) Social security number defined For purposes of this subsection, the term social security number means, with respect to a return of tax, a social security number issued to an individual by the Social Security Administration, but only if the social security number is issued\u2014 (A) to a citizen of the United States or pursuant to subclause (I) (or that portion of subclause (III) that relates to subclause (I)) of section 205(c)(2)(B)(i) of the Social Security Act, and (B) on or before the due date of filing such return. .\n##### (b) Portion of credit refundable\n**(1) In general**\nSection 24(d)(1)(A) is amended to read as follows:\n(A) the credit which would be allowed under this section determined\u2014 (i) by substituting $1,400 for $2,000 in subsection (a)(1), (ii) without regard to subsection (a)(2), and (iii) without regard to this subsection (other than this subparagraph) and the limitation under section 26(a), or .\n**(2) Modification of limitation based on earned income**\nSection 24(d)(1)(B)(i) is amended by striking $3,000 and inserting $2,500 .\n**(3) Inflation adjustment**\nSection 24(d) is amended by inserting after paragraph (3) the following new paragraph:\n(4) Adjustment for inflation (A) In general The $1,400 amount in paragraph (1)(A)(i) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2017 for 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under subparagraph (A) is not a multiple of $100, such increase shall be rounded to the next lowest multiple of $100. (C) Limitation The amount of any increase under subparagraph (A) (after the application of subparagraph (B)) shall not exceed $600. .\n**(4) Conforming amendments**\n**(A)**\nSection 24(e) is amended to read as follows:\n(e) Taxpayer identification requirement No credit shall be allowed under this section if the identifying number of the taxpayer was issued after the due date for filing the return of tax for the taxable year. .\n**(B)**\nSection 24 is amended by striking subsection (h).\n##### (c) Repeal of certain later enacted provisions\n**(1)**\nSection 24 is amended by striking subsections (i), (j), and (k).\n**(2)**\nChapter 77 is amended by striking section 7527A (and by striking the item relating to section 7527A in the table of sections for such chapter).\n**(3)**\nSection 26(b)(2) is amended by inserting and at the end of subparagraph (X), by striking , and at the end of subparagraph (Y) and inserting a period, and by striking subparagraph (Z).\n**(4)**\nSection 3402(f)(1)(C) is amended by striking section 24 (determined after application of subsection (j) thereof) and inserting section 24(a) .\n**(5)**\nSection 6211(b)(4)(A) is amended\u2014\n**(A)**\nby striking 24 by reason of subsections (d) and (i)(1) thereof and inserting 24(d) , and\n**(B)**\nby striking 6428B, and 7527A and inserting and 6428B .\n**(6)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by striking 6431, or 7527A and inserting or 6431 .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 123. Increased limitation for certain charitable contributions\n##### (a) In general\nSection 170(b)(1)(G) is amended to read as follows:\n(G) Cash contributions (i) In general Any contribution of cash to an organization described in subparagraph (A) shall be allowed to the extent that the aggregate of such contributions does not exceed 60 percent of the taxpayer\u2019s contribution base for the taxable year, reduced by the aggregate amount of contributions allowable under subparagraph (A) for such taxpayer for such year. (ii) Carryover If the aggregate amount of contributions described in clause (i) exceeds the limitation of clause (i), such excess shall be treated (in a manner consistent with the rules of subsection (d)(1)) as a charitable contribution to which clause (i) applies in each of the 5 succeeding years in order of time. .\n##### (b) Coordination with limitations on other contributions\n**(1) Coordination with 50 percent limitation**\nSection 170(b)(1)(A) is amended by striking Any charitable contribution and inserting Any charitable contribution other than a contribution described in subparagraph (G) .\n**(2) Coordination with 30 percent limitation**\nSection 170(b)(1)(B) is amended\u2014\n**(A)**\nin the matter preceding clause (i), by striking to which subparagraph (A) applies and inserting to which subparagraph (A) or (G) applies ,\n**(B)**\nby amending clause (ii) to read as follows:\n(ii) the excess of\u2014 (I) the sum of 50 percent of the taxpayer\u2019s contribution base for the taxable year, plus so much of the amount of charitable contributions allowable under subparagraph (G) as does not exceed 10 percent of such contribution base, over (II) the amount of charitable contributions allowable under subparagraphs (A) and (G) (determined without regard to subparagraph (C)). , and\n**(C)**\nin the matter following clause (ii), by striking (to which subparagraph (A) does not apply) and inserting (to which neither subparagraph (A) nor (G) applies) .\n##### (c) Effective date\nThe amendments made by this section shall apply to contributions made in taxable years beginning after the date of the enactment of this Act.\n#### 124. Increased contributions to ABLE accounts\n##### (a) Increase in limitation for contributions from compensation of individuals with disabilities\nSection 529A(b)(2)(B)(ii) is amended by striking before January 1, 2026 .\n##### (b) Allowance of saver\u2019s credit for ABLE contributions by account holder\nSection 25B(d)(1)(D) is amended by striking made before January 1, 2026, .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 125. Rollovers to ABLE programs from 529 programs\n##### (a) In general\nSection 529(c)(3)(C)(i)(III) is amended by striking before January 1, 2026, .\n##### (b) Effective date\nThe amendments made by this section shall apply to distributions after the date of the enactment of this Act.\n#### 126. Treatment of certain individuals performing services in the Sinai Peninsula of Egypt\n##### (a) In general\nSection 112(c)(2) is amended\u2014\n**(1)**\nby striking means any area and inserting\nmeans\u2014 (A) any area , and\n**(2)**\nby striking the period at the end and inserting\n, and (B) the Sinai Peninsula of Egypt. .\n##### (b) Period of treatment\nSection 112(c)(3) is amended\u2014\n**(1)**\nby striking only if performed and inserting\nonly if\u2014 (A) in the case of an area described in paragraph (2)(A), such service is performed , and\n**(2)**\nby striking the period at the end and inserting\n, and (B) in the case of the area described in paragraph (2)(B), such service is performed during any period with respect to which one or more members of the Armed Forces of the United States are entitled to special pay under section 310 of title 37, United States Code (relating to special pay; duty subject to hostile fire or imminent danger), for service performed in such area. .\n##### (c) Conforming amendment\nThe Tax Cuts and Jobs Act is amended by striking section 11026.\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to services performed on or after the date of the enactment of this Act.\nD\nEducation\n#### 131. Treatment of student loan discharges\n##### (a) Sunset of special rule for discharges of certain loans\nSection 108(f)(5) is amended\u2014\n**(1)**\nin the heading, by striking 2025 and inserting 2024 , and\n**(2)**\nby striking January 1, 2026 and inserting January 1, 2025 .\n##### (b) Reinstatement of rule for discharges on account of death or disability after 2024\nSection 108(f) is amended by adding at the end the following new paragraph:\n(6) Discharges on account of death or disability after 2024 (A) In general In the case of an individual, gross income does not include any amount which (but for this subsection) would be includible in gross income for such taxable year by reasons of the discharge (in whole or in part) of any loan described in subparagraph (B) after December 31, 2024, if such discharge was\u2014 (i) pursuant to subsection (a) or (d) of section 437 of the Higher Education Act of 1965 or the parallel benefit under part D of title IV of such Act (relating to the repayment of loan liability), (ii) pursuant to section 464(c)(1)(F) of such Act, or (iii) otherwise discharged on account of the death or total and permanent disability of the student. (B) Loans described A loan is described in this subparagraph if such loan is\u2014 (i) a student loan (as defined in paragraph (2)), or (ii) a private education loan (as defined in section 140(7) of the Consumer Credit Protection Act ( 15 U.S.C. 1650(7) )). .\n##### (c) Effective date\nThe amendments made by this section shall apply to discharges of indebtedness after December 31, 2024.\n#### 132. 529 account funding for homeschool and additional elementary and secondary expenses\n##### (a) In general\nSection 529(c)(7) of the Internal Revenue Code of 1986 is amended to read as follows:\n(7) Treatment of elementary and secondary tuition Any reference in this section to the term qualified higher education expense shall include a reference to the following expenses in connection with enrollment or attendance at, or for students enrolled at or attending, an elementary or secondary public, private, or religious school: (A) Tuition. (B) Curriculum and curricular materials. (C) Books or other instructional materials. (D) Online educational materials. (E) Tuition for tutoring or educational classes outside of the home, including at a tutoring facility, but only if the tutor or instructor is not related to the student and\u2014 (i) is licensed as a teacher in any State, (ii) has taught at an eligible educational institution, or (iii) is a subject matter expert in the relevant subject. (F) Fees for a nationally standardized norm-referenced achievement test, an advanced placement examination, or any examinations related to college or university admission. (G) Fees for dual enrollment in an institution of higher education. (H) Educational therapies for students with disabilities provided by a licensed or accredited practitioner or provider, including occupational, behavioral, physical, and speech-language therapies. Such term shall include expenses for the purposes described in subparagraphs (A) through (H) in connection with a homeschool (whether treated as a homeschool or a private school for purposes of applicable State law). .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after the date of the enactment of this Act.\nE\nDeductions and exclusions\n#### 141. Repeal of deduction for personal exemptions\n##### (a) In general\nPart V of subchapter B of chapter 1 is hereby repealed.\n##### (b) Definition of dependent retained\nSection 152, prior to the repeal made by subsection (a), is hereby redesignated as section 7706 and moved to the end of chapter 79.\n##### (c) Application to trusts and estates\nSection 642(b) is amended\u2014\n**(1)**\nin paragraph (2)(C)\u2014\n**(A)**\nin clause (i), by striking the exemption amount under section 151(d) and all that follows through the period at the end and inserting the dollar amount in effect under section 7706(d)(1)(B). , and\n**(B)**\nby striking clause (iii),\n**(2)**\nby striking paragraph (3), and\n**(3)**\nby striking Deduction For Personal Exemption in the heading thereof and inserting Basic Deduction .\n##### (d) Application to nonresident aliens\nSection 873(b) is amended by striking paragraph (3).\n##### (e) Modification of return requirement\n**(1) In general**\nSection 6012(a)(1) is amended to read as follows:\n(1) Every individual who has gross income for the taxable year, except that a return shall not be required of\u2014 (A) an individual who is not married (determined by applying section 7703) and who has gross income for the taxable year which does not exceed the standard deduction applicable to such individual for such taxable year under section 63, or (B) an individual entitled to make a joint return if\u2014 (i) the gross income of such individual, when combined with the gross income of such individual\u2019s spouse, for the taxable year does not exceed the standard deduction which would be applicable for such taxable year under section 63 if such individual and such individual\u2019s spouse made a joint return, (ii) such individual\u2019s spouse does not make a separate return, and (iii) neither such individual nor such individual\u2019s spouse is an individual described in section 63(c)(4) who has income (other than earned income) in excess of the amount in effect under section 63(c)(4)(A). .\n**(2) Bankruptcy estates**\nSection 6012(a)(8) is amended by striking the sum of the exemption amount plus the basic standard deduction under section 63(c)(2)(C) and inserting the standard deduction in effect under section 63(c)(1)(B) .\n**(3) Conforming amendment**\nSection 6012 is amended by striking subsection (f).\n##### (f) Conforming amendments\n**(1)**\nSection 1(g)(5)(A) is amended by striking section 152(e) and inserting section 7706(e) .\n**(2)**\nSection 2(a)(1)(B) is amended\u2014\n**(A)**\nby striking section 152 and inserting section 7706 , and\n**(B)**\nby striking with respect to whom the taxpayer is entitled to a deduction for the taxable year under section 151 and inserting whose TIN is included on the taxpayer\u2019s return of tax for the taxable year .\n**(3)**\nSection 2(b)(1)(A)(i) is amended\u2014\n**(A)**\nin the matter preceding subclause (I)\u2014\n**(i)**\nby striking section 152(c) and inserting section 7706(c) , and\n**(ii)**\nby striking section 152(e) and inserting section 7706(e) , and\n**(B)**\nin subclause (II), by striking section 152(b)(2) or 152(b)(3) and inserting section 7706(b)(2) or 7706(b)(3) .\n**(4)**\nSection 2(b)(1)(A)(ii) is amended by striking if the taxpayer is entitled to a deduction for the taxable year for such person under section 151 and inserting if the taxpayer included such person\u2019s TIN on the return of tax for the taxable year .\n**(5)**\nSection 2(b)(1)(B) is amended by striking if the taxpayer is entitled to a deduction for the taxable year for such father or mother under section 151 and inserting if such father or mother is a dependent of the taxpayer and the taxpayer included such father or mother\u2019s TIN on the return of tax for the taxable year .\n**(6)**\nSection 2(b)(3)(B) is amended\u2014\n**(A)**\nby striking section 152(d)(2) in clause (i) and inserting section 7706(d)(2) , and\n**(B)**\nby striking section 152(d) in clause (ii) and inserting section 7706(d) .\n**(7)**\nSection 21(b)(1)(A) is amended by striking section 152(a)(1) and inserting section 7706(a)(1) .\n**(8)**\nSection 21(b)(1)(B) is amended by striking section 152 and inserting section 7706 .\n**(9)**\nSection 21(e)(5)(A) is amended by striking section 152(e) and inserting section 7706(e) .\n**(10)**\nSection 21(e)(5) is amended by striking section 152(e)(4)(A) in the matter following subparagraph (B) and inserting section 7706(e)(4)(A) .\n**(11)**\nSection 21(e)(6)(A) is amended to read as follows:\n(A) who is a dependent of either the taxpayer or the taxpayer\u2019s spouse for the taxable year, or .\n**(12)**\nSection 21(e)(6)(B) is amended by striking section 152(f)(1) and inserting section 7706(f)(1) .\n**(13)**\nSection 25A(f)(1)(A)(iii) is amended by striking with respect to whom the taxpayer is allowed a deduction under section 151 .\n**(14)**\nSection 25A(g)(3) is amended by striking If a deduction under section 151 with respect to an individual is allowed to another taxpayer and inserting If an individual is a dependent of another taxpayer .\n**(15)**\nSection 25B(c)(2)(A) is amended by striking any individual with respect to whom a deduction under section 151 is allowed to another taxpayer and inserting any individual who is a dependent of another taxpayer .\n**(16)**\nSection 25B(c)(2)(B) is amended by striking section 152(f)(2) and inserting section 7706(f)(2) .\n**(17)**\nSection 32(c)(1)(A)(ii)(III) is amended by striking a dependent for whom a deduction is allowable under section 151 to another taxpayer and inserting a dependent of another taxpayer .\n**(18)**\nSection 32(c)(3) is amended\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking section 152(c) and inserting section 7706(c) , and\n**(ii)**\nby striking section 152(e) and inserting section 7706(e) ,\n**(B)**\nin subparagraph (B), by striking unless the taxpayer is entitled to a deduction under section 151 for such taxable year with respect to such individual (or would be so entitled but for section 152(e) and inserting if such individual is not treated as a dependent of such taxpayer for such taxable year by reason of section 7706(b)(2) (determined without regard to section 7706(e)) , and\n**(C)**\nin subparagraph (C), by striking section 152(c)(1)(B) and inserting section 7706(c)(1)(B) .\n**(19)**\nSection 35(d)(1)(B) is amended by striking with respect to whom the taxpayer is entitled to a deduction under section 151(c) and inserting if the taxpayer included such person\u2019s TIN on the return of tax for the taxable year .\n**(20)**\nSection 35(d)(2) is amended\u2014\n**(A)**\nby striking section 152(e) and inserting section 7706(e) , and\n**(B)**\nby striking section 152(e)(4)(A) and inserting section 7706(e)(4)(A) .\n**(21)**\nSection 36B(b)(2)(A) is amended by striking section 152 and inserting section 7706 .\n**(22)**\nSection 36B(b)(3)(B) is amended\u2014\n**(A)**\nin clause (ii)(I)(aa), by striking who is not allowed a deduction under section 151 for the taxable year with respect to a dependent and inserting who does not have any dependents for the taxable year , and\n**(B)**\nin the flush matter at the end, by striking unless a deduction is allowed under section 151 for the taxable year with respect to a dependent and inserting unless the taxpayer has a dependent for the taxable year (and the taxpayer included such dependent\u2019s TIN on the return of tax for the taxable year) .\n**(23)**\nSection 36B(c)(1)(D) is amended by striking with respect to whom a deduction under section 151 is allowable to another taxpayer and inserting who is a dependent of another taxpayer .\n**(24)**\nSection 36B(d)(1) is amended by striking equal to the number of individuals for whom the taxpayer is allowed a deduction under section 151 (relating to allowance of deduction for personal exemptions) for the taxable year and inserting the sum of 1 (2 in the case of a joint return) plus the number of individuals who are dependents of the taxpayer for the taxable year .\n**(25)**\nSection 36B(e)(1) is amended by striking 1 or more individuals for whom a taxpayer is allowed a deduction under section 151 (relating to allowance of deduction for personal exemptions) for the taxable year (including the taxpayer or his spouse) and inserting 1 or more of the taxpayer, the taxpayer\u2019s spouse, or any dependent of the taxpayer .\n**(26)**\nSection 42(i)(3)(D)(ii)(I) is amended by striking section 152 and inserting section 7706 .\n**(27)**\nSection 45R(e)(1)(A)(iv) is amended\u2014\n**(A)**\nby striking section 152(d)(2) and inserting section 7706(d)(2) , and\n**(B)**\nby striking section 152(d)(2)(H) and inserting section 7706(d)(2)(H) .\n**(28)**\nSection 51(i)(1) is amended\u2014\n**(A)**\nby striking section 152(d)(2) in subparagraphs (A) and (B) and inserting section 7706(d)(2) , and\n**(B)**\nby striking section 152(d)(2)(H) in subparagraph (C) and inserting section 7706(d)(2)(H) .\n**(29)**\nSection 56(b)(1)(D) is amended\u2014\n**(A)**\nby striking , the deduction for personal exemptions under section 151, , and\n**(B)**\nby striking and deduction for personal exemptions in the heading thereof.\n**(30)**\nSection 63(b) is amended by adding and at the end of paragraph (1), by striking paragraph (2), and by redesignating paragraph (3) as paragraph (2).\n**(31)**\nSection 63(c), as amended by section 121, is amended by striking paragraph (3) and redesignating paragraphs (4), (5), and (6) as paragraphs (3), (4), and (5), respectively.\n**(32)**\nSection 63(c)(4), as redesignated, is amended\u2014\n**(A)**\nby striking with respect to whom a deduction under section 151 is allowable to and inserting who is a dependent of , and\n**(B)**\nby striking certain in the heading thereof.\n**(33)**\nSection 63(f) is amended by striking all that precedes paragraph (3) and inserting the following:\n(f) Additional standard deduction for the aged and blind (1) In general For purposes of subsection (c)(1), the additional standard deduction is, with respect to a taxpayer for a taxable year, the sum of\u2014 (A) $600 if the taxpayer has attained age 65 before the close of such taxable year, and (B) $600 if the taxpayer is blind as of the close of such taxable year. (2) Application to married individuals (A) Joint returns In the case of a joint return, paragraph (1) shall be applied separately with respect to each spouse. (B) Certain married individuals filing separately In the case of a married individual filing a separate return, if\u2014 (i) the spouse of such individual has no gross income for the calendar year in which the taxable year of such individual begins, (ii) such spouse is not the dependent of another taxpayer for a taxable year beginning in the calendar year in which such individual\u2019s taxable year begins, and (iii) the TIN of such spouse is included on such individual\u2019s return of tax for the taxable year, the additional standard deduction shall be determined in the same manner as if such individual and such individual\u2019s spouse filed a joint return. .\n**(34)**\nSection 63(f)(3) is amended by striking paragraphs (1) and (2) and inserting subparagraphs (A) and (B) of paragraph (1) .\n**(35)**\nSection 72(t)(2)(D)(i)(III) is amended by striking section 152 and inserting section 7706 .\n**(36)**\nSection 72(t)(7)(A)(iii) is amended by striking section 152(f)(1) and inserting section 7706(f)(1) .\n**(37)**\nSection 105(b) is amended\u2014\n**(A)**\nby striking as defined in section 152 and inserting as defined in section 7706 ,\n**(B)**\nby striking section 152(f)(1) and inserting section 7706(f)(1) , and\n**(C)**\nby striking section 152(e) and inserting section 7706(e) .\n**(38)**\nSection 105(c)(1) is amended by striking section 152 and inserting section 7706 .\n**(39)**\nSection 125(e)(1)(D) is amended by striking section 152 and inserting section 7706 .\n**(40)**\nSection 129(c)(1) is amended to read as follows:\n(1) who is a dependent of such employee or of such employee\u2019s spouse, or .\n**(41)**\nSection 129(c)(2) is amended by striking section 152(f)(1) and inserting section 7706(f)(1) .\n**(42)**\nSection 132(h)(2)(B) is amended\u2014\n**(A)**\nby striking section 152(f)(1) and inserting section 7706(f)(1) , and\n**(B)**\nby striking section 152(e) and inserting section 7706(e) .\n**(43)**\nSection 139D(c)(5) is amended by striking section 152 and inserting section 7706 .\n**(44)**\nSection 139E(c)(2) is amended by striking section 152 and inserting section 7706 .\n**(45)**\nSection 162(l)(1)(D) is amended by striking section 152(f)(1) and inserting section 7706(f)(1) .\n**(46)**\nSection 170(g)(1) is amended by striking section 152 and inserting section 7706 .\n**(47)**\nSection 170(g)(3) is amended by striking section 152(d)(2) and inserting section 7706(d)(2) .\n**(48)**\nSection 172(d) is amended by striking paragraph (3).\n**(49)**\nSection 213(a) is amended by striking section 152 and inserting section 7706 .\n**(50)**\nSection 213(d)(5) is amended by striking section 152(e) and inserting section 7706(e) .\n**(51)**\nSection 213(d)(11) is amended by striking section 152(d)(2) in the matter following subparagraph (B) and inserting section 7706(d)(2) .\n**(52)**\nSection 220(b)(6) is amended by striking with respect to whom a deduction under section 151 is allowable to and inserting who is a dependent of .\n**(53)**\nSection 220(d)(2)(A) is amended by striking section 152 and inserting section 7706 .\n**(54)**\nSection 221(d)(4) is amended by striking section 152 and inserting section 7706 .\n**(55)**\nSection 223(b)(6) is amended by striking with respect to whom a deduction under section 151 is allowable to and inserting who is a dependent of .\n**(56)**\nSection 223(d)(2)(A) is amended by striking section 152 and inserting section 7706 .\n**(57)**\nSection 401(h) is amended by striking section 152(f)(1) in the last sentence and inserting section 7706(f)(1) .\n**(58)**\nSection 402(l)(4)(D) is amended by striking section 152 and inserting section 7706 .\n**(59)**\nSection 409A(a)(2)(B)(ii)(I) is amended by striking section 152(a) and inserting section 7706(a) .\n**(60)**\nSection 441(f)(2)(B)(iii) is amended by striking , but only the adjusted amount of the deductions for personal exemptions as described in section 443(c) .\n**(61)**\nSection 443 is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nby striking paragraph (3), and\n**(ii)**\nby striking modified taxable income and inserting taxable income each place such term appears,\n**(B)**\nby striking subsection (c), and\n**(C)**\nby redesignating subsections (d) and (e) as subsections (c) and (d), respectively.\n**(62)**\nSection 501(c)(9) is amended by striking section 152(f)(1) and inserting section 7706(f)(1) .\n**(63)**\nSection 529(e)(2)(B) is amended by striking section 152(d)(2) and inserting section 7706(d)(2) .\n**(64)**\nSection 529A(e)(4) is amended\u2014\n**(A)**\nby striking section 152(d)(2)(B) and inserting section 7706(d)(2)(B) , and\n**(B)**\nby striking section 152(f)(1)(B) and inserting section 7706(f)(1)(B) .\n**(65)**\nSection 643(a)(2) is amended\u2014\n**(A)**\nby striking (relating to deduction for personal exemptions) and inserting (relating to basic deduction) , and\n**(B)**\nby striking Deduction for personal exemption in the heading thereof and inserting Basic deduction .\n**(66)**\nSection 703(a)(2) is amended by striking subparagraph (A) and by redesignating subparagraphs (B) through (F) as subparagraphs (A) through (E), respectively.\n**(67)**\nSection 874 is amended by striking subsection (b) and by redesignating subsection (c) as subsection (b).\n**(68)**\nSection 891 is amended by striking under section 151 and .\n**(69)**\nSection 904(b)(1) is amended to read as follows:\n(1) Deduction for estates and trusts For purposes of subsection (a), the taxable income of an estate or trust shall be computed without any deduction under section 642(b). .\n**(70)**\nSection 931(b)(1) is amended to read as follows:\n(1) any deduction from gross income, or .\n**(71)**\nSection 933 is amended\u2014\n**(A)**\nby striking as a deduction from his gross income any deductions (other than the deduction under section 151, relating to personal exemptions) in paragraph (1) and inserting any deduction from gross income , and\n**(B)**\nby striking as a deduction from his gross income any deductions (other than the deduction for personal exemptions under section 151) in paragraph (2) and inserting any deduction from gross income .\n**(72)**\nSection 1212(b)(2)(B)(ii) is amended to read as follows:\n(ii) in the case of an estate or trust, the deduction allowed for such year under section 642(b). .\n**(73)**\nSection 1361(c)(1)(C) is amended by striking section 152(f)(1)(C) and inserting section 7706(f)(1)(C) .\n**(74)**\nSection 1402(a) is amended by striking paragraph (7).\n**(75)**\nSection 2032A(c)(7)(D) is amended by striking section 152(f)(2) and inserting section 7706(f)(2) .\n**(76)**\nSection 3402(f)(1)(A) is amended by striking for whom a deduction is allowable with respect to another taxpayer under section 151 and inserting who is a dependent of another taxpayer .\n**(77)**\nSection 3402(m)(1) is amended by striking other than the deductions referred to in section 151 and .\n**(78)**\nSection 3402(m)(3) is amended by striking section 63(c)(3) and inserting section 63(f) .\n**(79)**\nSection 3402(r)(2) is amended by striking the sum of\u2014 and all that follows and inserting the basic standard deduction (as defined in section 63(c)) for an individual to whom section 63(c)(2)(C) applies. .\n**(80)**\nSection 5000A(b)(3)(A) is amended by striking section 152 and inserting section 7706 .\n**(81)**\nSection 5000A(c)(4)(A) is amended by striking the number of individuals for whom the taxpayer is allowed a deduction under section 151 (relating to allowance of deduction for personal exemptions) for the taxable year and inserting the sum of 1 (2 in the case of a joint return) plus the number of the taxpayer\u2019s dependents for the taxable year .\n**(82)**\nSection 6013(b)(3)(A) is amended\u2014\n**(A)**\nby striking had less than the exemption amount of gross income in clause (ii) and inserting had no gross income ,\n**(B)**\nby striking had gross income of the exemption amount or more in clause (iii) and inserting had any gross income , and\n**(C)**\nby striking the flush language following clause (iii).\n**(83)**\nSection 6014(a) is amended by striking section 6012(a)(1)(C)(i) and inserting section 6012(a)(1)(B)(iii) .\n**(84)**\nSection 6014(b)(4) is amended by striking 63(c)(5) and inserting 63(c)(4) .\n**(85)**\nSection 6103(l)(13) is amended\u2014\n**(A)**\nin subparagraph (A), by striking clause (iv) and redesignating clauses (v) and (vi) as clauses (iv) and (v), respectively, and\n**(B)**\nin subparagraph (C)(i), by striking clauses (i) through (iv) and inserting clauses (i) through (iii) .\n**(86)**\nSection 6103(l)(21)(A)(iii) is amended to read as follows:\n(iii) the number of the taxpayer\u2019s dependents, .\n**(87)**\nSection 6213(g)(2)(H) is amended by striking section 21 (relating to expenses for household and dependent care services necessary for gainful employment) or section 151 (relating to allowance of deductions for personal exemptions) and inserting subsection (a)(1)(B), (b)(1)(A)(ii), or (b)(1)(B) of section 2 or section 21, 35(d)(1)(B), 36B(b)(3)(B), or 63(f)(2)(B) .\n**(88)**\nSection 6334(d) is amended\u2014\n**(A)**\nby amending paragraph (2) to read as follows:\n(2) Exempt amount (A) In general For purposes of paragraph (1), the term exempt amount means an amount equal to\u2014 (i) the sum of the amount determined under subparagraph (B) and the standard deduction, divided by (ii) 52. (B) Amount determined For purposes of subparagraph (A), the amount determined under this subparagraph is\u2014 (i) the dollar amount in effect under section 7706(d)(1)(B), multiplied by (ii) the number of the taxpayer\u2019s dependents for the taxable year in which the levy occurs. (C) Verified statement Unless the taxpayer submits to the Secretary a written and properly verified statement specifying the facts necessary to determine the proper amount under subparagraph (A), subparagraph (A) shall be applied as if the taxpayer were a married individual filing a separate return with no dependents. , and\n**(B)**\nby striking paragraph (4).\n**(89)**\nSection 7702B(f)(2)(C)(iii) is amended by striking section 152(d)(2) and inserting section 7706(d)(2) .\n**(90)**\nSection 7703(a) is amended by striking part V of subchapter B of chapter 1 and .\n**(91)**\nSection 7703(b)(1) is amended by striking section 152(f)(1)) and all that follows and inserting section 7706(f)(1)) who is a dependent of such individual for the taxable year (or would be but for section 7706(e)), .\n**(92)**\nSection 7706(a), as redesignated by this section, is amended by striking this subtitle and inserting this title .\n**(93)**\n**(A)**\nSection 7706(d)(1)(B), as redesignated by this section, is amended by striking the exemption amount (as defined in section 151(d)) and inserting $4,150 .\n**(B)**\nSection 7706(d), as redesignated by this section, is amended by adding at the end the following new paragraph:\n(6) Inflation adjustment The $4,150 amount in paragraph (1)(B) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins, determined by substituting calendar year 2017 for calendar year 2016 in subparagraph (A)(ii) thereof. If any increase determined under the preceding sentence is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. .\n**(94)**\nSection 7706(e)(3), as redesignated by this section, is amended by inserting (as in effect before its repeal) after section 151 .\n**(95)**\nSection 7706(f)(6)(B), as redesignated by this section, is amended by striking clause (i) and designating clauses (ii), (iii), and (iv) as clauses (i), (ii), and (iii), respectively.\n**(96)**\nThe table of parts for subchapter B of chapter 1 is amended by striking the item relating to part V.\n**(97)**\nThe table of sections for chapter 79 is amended by adding at the end the following new item:\nSec. 7706. Dependent defined. .\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 142. Limitation on deduction for State and local, etc., taxes\n##### (a) In general\nSection 164(b)(6) is amended by striking all that precedes The preceding sentence and inserting the following:\n(6) Limitation on individual deductions In the case of an individual\u2014 (A) no deduction shall be allowed under this chapter for foreign real property taxes paid or accrued during the taxable year, and (B) the aggregate amount of the deduction allowed under this chapter for taxes described in paragraphs (1), (2), and (3) of subsection (a) and paragraph (5) of this subsection (and any tax described in any such paragraph taken into account under section 216(a)(1)) paid or accrued by the taxpayer during the taxable year shall not exceed $10,000 ($5,000 in the case of a married individual filing a separate return). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 143. Limitation on deduction for qualified residence interest\n##### (a) Interest on home equity indebtedness\nSection 163(h)(3)(A) is amended by striking during the taxable year on and all that follows through residence of the taxpayer. and inserting during the taxable year on acquisition indebtedness with respect to any qualified residence of the taxpayer. .\n##### (b) Limitation on acquisition indebtedness\nSection 163(h)(3)(B)(ii) is amended to read as follows:\n(ii) Limitation The aggregate amount treated as acquisition indebtedness for any period shall not exceed the excess (if any) of\u2014 (I) $750,000 ($375,000, in the case of a married individual filing a separate return), over (II) the sum of the aggregate outstanding pre-October 13, 1987, indebtedness (as defined in subparagraph (D)) plus the aggregate outstanding pre-December 15, 2017, indebtedness (as defined in subparagraph (C)). .\n##### (c) Treatment of indebtedness incurred on or before December 15, 2017\nSection 163(h)(3)(C) is amended to read as follows:\n(C) Treatment of indebtedness incurred on or before December 15, 2017 (i) In general In the case of any pre-December 15, 2017, indebtedness, subparagraph (B)(ii) shall not apply and the aggregate amount of such indebtedness treated as acquisition indebtedness for any period shall not exceed the excess (if any) of\u2014 (I) $1,000,000 ($500,000, in the case of a married individual filing a separate return), over (II) the aggregate outstanding pre-October 13, 1987, indebtedness (as defined in subparagraph (D)). (ii) Pre-December 15, 2017, indebtedness For purposes of this subparagraph\u2014 (I) In general The term pre-December 15, 2017, indebtedness means indebtedness (other than pre-October 13, 1987, indebtedness) incurred on or before December 15, 2017. (II) Binding written contract exception In the case of a taxpayer who enters into a written binding contract before December 15, 2017, to close on the purchase of a principal residence before January 1, 2018, and who purchases such residence before April 1, 2018, the term pre-December 15, 2017, indebtedness shall include indebtedness secured by such residence. (iii) Refinancing indebtedness (I) In general In the case of any indebtedness which is incurred to refinance indebtedness, such refinanced indebtedness shall be treated for purposes of this subparagraph as incurred on the date that the original indebtedness was incurred to the extent the amount of the indebtedness resulting from such refinancing does not exceed the amount of the refinanced indebtedness. (II) Limitation on period of refinancing Subclause (I) shall not apply to any indebtedness after the expiration of the term of the original indebtedness or, if the principal of such original indebtedness is not amortized over its term, the expiration of the term of the 1st refinancing of such indebtedness (or if earlier, the date which is 30 years after the date of such 1st refinancing). .\n##### (d) Coordination with treatment of indebtedness incurred on or before October 13, 1987\nSection 163(h)(3)(D) is amended\u2014\n**(1)**\nby striking clause (ii) and redesignating clauses (iii) and (iv) as clauses (ii) and (iii), respectively, and\n**(2)**\nin clause (iii) (as so redesignated)\u2014\n**(A)**\nby striking clause (iii) in the matter preceding subclause (I) and inserting clause (ii) , and\n**(B)**\nby striking clause (iii)(I) in subclauses (I) and (II) and inserting clause (ii)(I) .\n##### (e) Coordination with exclusion of income from discharge of indebtedness\nSection 108(h)(2) is amended by striking applied by substituting $750,000 ($375,000 for $1,000,000 ($500,000 in clause (ii) thereof and .\n##### (f) Conforming amendment\nSection 163(h)(3) is amended by striking subparagraph (F).\n##### (g) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 144. Modification of deduction for personal casualty losses\n##### (a) In general\nSection 165(h)(5)(A) is amended by striking in a taxable year beginning after December 31, 2017, and before January 1, 2026, .\n##### (b) Conforming amendments\n**(1)**\nSection 165(h)(5)(B) is amended by striking for any taxable year to which subparagraph (A) applies .\n**(2)**\nSection 165(h)(5) is amended by striking for taxable years 2018 through 2025 in the heading thereof and inserting to losses attributable to Federally declared disasters .\n##### (c) Effective date\nThe amendments made by this section shall apply to losses sustained in taxable years beginning after the date of the enactment of this Act.\n#### 145. Termination of miscellaneous itemized deductions\n##### (a) In general\nSection 67 is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) In general In the case of an individual, miscellaneous itemized deductions shall not be allowed. , and\n**(2)**\nby striking subsection (g).\n##### (b) Movement of definition of adjusted gross income for estates and trusts\n**(1)**\nSection 67 is amended by striking subsection (e).\n**(2)**\nSection 641 is amended by adding at the end the following new subsection:\n(d) Computation of adjusted gross income For purposes of this title, the adjusted gross income of an estate or trust shall be computed in the same manner as in the case of an individual, except that\u2014 (1) the deductions for costs which are paid or incurred in connection with the administration of the estate or trust and which would not have been incurred if the property were not held in such trust or estate, and (2) the deductions allowable under sections 642(b), 651, and 661, shall be treated as allowable in arriving at adjusted gross income. .\n##### (c) Conforming amendments\n**(1)**\nSection 56(b)(1)(A) is amended to read as follows:\n(A) Certain taxes No deduction (other than a deduction allowable in computing adjusted gross income) shall be allowed for any taxes described in paragraph (1), (2), or (3) of section 164(a) or clause (ii) of section 164(b)(5)(A). .\n**(2)**\nSection 56(b)(1)(C), as amended by the preceding provisions of this Act, is amended by striking subparagraph (A)(ii) and inserting subparagraph (A) .\n**(3)**\nSection 62(a) is amended by striking subtitle in the matter preceding paragraph (1) and inserting title .\n**(4)**\nSection 641(c)(2)(E) is amended to read as follows:\n(E) Section 642(c) shall not apply. .\n**(5)**\nSection 1411(a)(2) is amended by striking (as defined in section 67(e)) .\n**(6)**\nSection 6654(d)(1)(C) is amended by striking clause (iii).\n**(7)**\nSection 67 is amended in the heading, by striking 2-percent floor on and inserting Denial of .\n**(8)**\nThe table of sections for part 1 of subchapter B of chapter 1 is amended by striking the item relating to section 67 and inserting the following new item:\nSec. 67. Denial of miscellaneous itemized deductions. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 146. Repeal of overall limitation on itemized deductions\n##### (a) In general\nPart 1 of subchapter B of chapter 1 is amended by striking section 68 (and the item relating to such section in the table of sections for such part).\n##### (b) Conforming amendments\n**(1)**\nSection 56(b)(1), as amended by the preceding provisions of this Act, is amended by striking subparagraph (E).\n**(2)**\nSection 164(b)(5)(H)(ii)(III) is amended by striking (as determined under section 68(b)) .\n**(3)**\nSection 164(b)(5)(H) is amended by adding at the end the following new clause:\n(iii) Applicable amount defined For purposes of clause (ii), the term applicable amount means\u2014 (I) $300,000 in the case of a joint return or a surviving spouse, (II) $275,000 in the case of a head of household, (III) $250,000 in the case of an individual who is not married and who is not a surviving spouse or head of household, and (IV) \u00bd the amount applicable under subclause (I) in the case of a married individual filing a separate return. For purposes of this paragraph, marital status shall be determined under section 7703. In the case of any taxable year beginning in calendar years after the date of the enactment of this clause, each of the dollar amounts in this clause shall be increased by an amount equal to such dollar amount, multiplied by the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting 2012 for 2016 in subparagraph (A)(ii) thereof. If any amount after adjustment under the preceding sentence is not a multiple of $50, such amount shall be rounded to the next lowest multiple of $50. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 147. Termination of exclusion for qualified bicycle commuting reimbursement\n##### (a) In general\nSection 132(f)(1) is amended by striking subparagraph (D).\n##### (b) Conforming amendments\n**(1)**\nSection 132(f)(2) is amended by adding and at the end of subparagraph (A), striking , and at the end of subparagraph (B) and inserting a period, and striking subparagraph (C).\n**(2)**\nSection 132(f)(4) is amended by striking (other than a qualified bicycle commuting reimbursement) .\n**(3)**\nSection 132(f) is amended by striking paragraph (8).\n**(4)**\nSection 274(l)(2) is amended by striking after December 31, 2017, and before January 1, 2026 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 148. Qualified moving expense reimbursement exclusion limited to members of Armed Forces\n##### (a) In general\nSection 132(g) is amended\u2014\n**(1)**\nby striking by an individual in paragraph (1) and inserting by a qualified military individual , and\n**(2)**\nby striking paragraph (2) and inserting the following new paragraph:\n(2) Qualified military individual For purposes of this subsection, the term qualified military individual means a member of the Armed Forces of the United States on active duty who moves pursuant to a military order and incident to a permanent change of station. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 149. Deduction for moving expenses limited to members of Armed Forces\n##### (a) In general\nSection 217 is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) Deduction allowed There shall be allowed as a deduction moving expenses paid or incurred during the taxable year by a member of the Armed Forces of the United States on active duty who moves pursuant to a military order and incident to a permanent change of station. ,\n**(2)**\nby striking subsections (c), (d), (f), (g), and (k) and redesignating subsections (h), (i), and (j) as subsections (c), (d), and (f), respectively, and\n**(3)**\nby inserting after subsection (d), as so redesignated, the following new subsection:\n(e) Expenses furnished In-Kind Any moving and storage expenses which are furnished in-kind (or for which reimbursement or an allowance is provided, but only to the extent of the expenses paid or incurred)\u2014 (1) to a member described in subsection (a), or to such member\u2019s spouse or dependents, shall not be includible in gross income, and no reporting with respect to such expenses shall be required by the Secretary of Defense or the Secretary of Transportation, as the case may be, and (2) to the spouse and dependents of a member described in subsection (a) with regard to moving to a location other than the one to which such member moves (or from a location other than the one from which such member moves), this section shall apply with respect to the moving expenses of such spouse and dependents as if such spouse were a member described in subsection (a). .\n##### (b) Conforming amendments\n**(1)**\nSubsections (d)(3)(C) and (e) of section 23 are each amended by striking section 217(h)(3) and inserting section 217(c)(3) .\n**(2)**\nSection 7872(f) is amended by striking paragraph (11).\n**(3)**\nSection 217 is amended in the heading by striking Moving expenses and inserting Certain moving expenses of members of Armed Forces .\n**(4)**\nThe table of sections for part VII of subchapter B of chapter 1 is amended by striking the item relating to section 217 and inserting the following new item:\nSec. 217. Certain moving expenses of members of Armed Forces. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 150. Limitation on wagering losses\n##### (a) In general\nSection 165(d) is amended by striking in the case of taxable years beginning after December 31, 2017, and before January 1, 2026, .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\nF\nIncrease in estate and gift tax exemption\n#### 151. Increase in estate and gift tax exemption\n##### (a) In general\nSection 2010(c)(3) is amended in subparagraph (A), by striking $5,000,000 and inserting $10,000,000 .\n##### (b) Conforming amendment\nSection 2010(c)(3) is amended by striking subparagraph (C).\n##### (c) Effective date\nThe amendments made by this section shall apply to estates of decedents dying and gifts made after the date of the enactment of this Act.\nII\nIncreased exemption for Alternative Minimum Tax made permanent\n#### 201. Increased exemption for individuals\n##### (a) In general\nSection 55(d)(1) is amended\u2014\n**(1)**\nby striking $78,750 in subparagraph (A) and inserting $109,400 , and\n**(2)**\nby striking $50,600 in subparagraph (B) and inserting $70,300 .\n##### (b) Phase-Out of exemption amount\nSection 55(d)(2) is amended\u2014\n**(1)**\nby striking $150,000 in subparagraph (A) and inserting $1,000,000 , and\n**(2)**\nby striking subparagraphs (B) and (C) and by inserting the following new subparagraphs:\n(B) 50 percent of the dollar amount applicable under subparagraph (A) in the case of a taxpayer described in paragraph (1)(B) or (1)(C), and (C) $75,000 in the case of a taxpayer described in paragraph (1)(D). .\n##### (c) Inflation adjustment\nSection 55(d)(3) is amended to read as follows:\n(3) Inflation adjustment Each dollar amount described in clause (i) or (ii) of subparagraph (B) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting\u2014 (i) in the case of a dollar amount contained in paragraph (1)(D) or (2)(C) or in subsection (b)(1)(A), calendar year 2011 for calendar year 2016 in subparagraph (A)(ii) thereof, and (ii) in the case of a dollar amount contained in paragraph (1)(A), (1)(B), or (2)(A), calendar year 2017 for calendar year 2016 in subparagraph (A)(ii) thereof. Any increased amount determined under this paragraph shall be rounded to the nearest multiple of $100 ($50 in the case of the dollar amount contained in paragraph (2)(C)). .\n##### (d) Repeal of coordination with rules relating to the taxation of unearned children\nSection 59 is amended by striking subsection (j).\n##### (e) Conforming amendment\nSection 55(d) is amended by striking paragraph (4).\n##### (f) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "523",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Permanent Tax Cuts for American Families Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Student Empowerment Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "939",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Student Empowerment Act",
      "type": "HR"
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
            "name": "Capital gains tax",
            "updateDate": "2025-02-25T16:25:30Z"
          },
          {
            "name": "Charitable contributions",
            "updateDate": "2025-02-25T16:25:51Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-02-25T16:26:24Z"
          },
          {
            "name": "Egypt",
            "updateDate": "2025-02-25T16:26:50Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-02-25T16:26:32Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2025-02-25T16:25:43Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-02-25T16:25:35Z"
          },
          {
            "name": "Income tax rates",
            "updateDate": "2025-02-25T16:25:23Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-02-25T16:26:57Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-02-25T16:26:42Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-02-25T16:24:46Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-02-25T16:26:05Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-02-25T16:25:57Z"
          },
          {
            "name": "Tax treatment of families",
            "updateDate": "2025-02-25T16:25:01Z"
          },
          {
            "name": "Transfer and inheritance taxes",
            "updateDate": "2025-02-25T16:26:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-05T14:51:20Z"
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
          "measure-id": "id119hr137",
          "measure-number": "137",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr137v00",
            "update-date": "2026-04-21"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>TCJA Permanency Act </strong></p><p>This bill makes permanent multiple federal tax provisions enacted in 2017 by the Tax Cuts and Jobs Act.</p><p>The bill makes permanent the\u00a0</p><ul><li>individual tax rates of 10%, 12%, 22%, 24%, 32%, 35%, and 37%;</li><li>increased standard deduction;</li><li>personal exemption allowance repeal;</li><li>exclusion from income of student loans discharged due to death or disability;</li><li>qualified business income tax deduction (199A tax deduction);</li><li>allowance of ABLE account contributions in excess of the annual gift tax exclusion amount;</li><li>base estate and gift tax exclusion amount of $10 million (adjusted annually); and</li><li>alternative minimum tax exemption and phaseout amounts for noncorporate taxpayers.</li></ul><p>The bill makes permanent the child tax credit amounts of $2,000 per child and $500 for dependents, the $200,000 phaseout threshold ($400,000 for joint filers), and the refundable portion of the tax credit.\u00a0</p><p>The bill expands the expenses eligible for tax-free withdrawals from qualified tuition plans (529 plans) to include additional expenses associated with homeschool and\u00a0elementary and secondary schools (e.g.,\u00a0instructional materials, tutoring, test and enrollment fees, and educational therapies).\u00a0</p><p>The bill permanently eliminates certain miscellaneous itemized deductions and makes permanent the\u00a0</p><ul><li>state and local tax deduction limit of $10,000 ($5,000 for married individuals filing separately),</li><li>mortgage interest tax deduction limit of $750,000 ($375,000 for married individuals filing separately),</li><li>limit on the deduction of cash charitable contributions to 60% of a taxpayer\u2019s adjusted gross income, and</li><li>certain limits on casualty loss tax deductions.\u00a0</li></ul><p>The bill also permanently eliminates the exclusion from income for employer-reimbursed bicycle commuting expenses.</p>"
        },
        "title": "TCJA Permanency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr137.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>TCJA Permanency Act </strong></p><p>This bill makes permanent multiple federal tax provisions enacted in 2017 by the Tax Cuts and Jobs Act.</p><p>The bill makes permanent the\u00a0</p><ul><li>individual tax rates of 10%, 12%, 22%, 24%, 32%, 35%, and 37%;</li><li>increased standard deduction;</li><li>personal exemption allowance repeal;</li><li>exclusion from income of student loans discharged due to death or disability;</li><li>qualified business income tax deduction (199A tax deduction);</li><li>allowance of ABLE account contributions in excess of the annual gift tax exclusion amount;</li><li>base estate and gift tax exclusion amount of $10 million (adjusted annually); and</li><li>alternative minimum tax exemption and phaseout amounts for noncorporate taxpayers.</li></ul><p>The bill makes permanent the child tax credit amounts of $2,000 per child and $500 for dependents, the $200,000 phaseout threshold ($400,000 for joint filers), and the refundable portion of the tax credit.\u00a0</p><p>The bill expands the expenses eligible for tax-free withdrawals from qualified tuition plans (529 plans) to include additional expenses associated with homeschool and\u00a0elementary and secondary schools (e.g.,\u00a0instructional materials, tutoring, test and enrollment fees, and educational therapies).\u00a0</p><p>The bill permanently eliminates certain miscellaneous itemized deductions and makes permanent the\u00a0</p><ul><li>state and local tax deduction limit of $10,000 ($5,000 for married individuals filing separately),</li><li>mortgage interest tax deduction limit of $750,000 ($375,000 for married individuals filing separately),</li><li>limit on the deduction of cash charitable contributions to 60% of a taxpayer\u2019s adjusted gross income, and</li><li>certain limits on casualty loss tax deductions.\u00a0</li></ul><p>The bill also permanently eliminates the exclusion from income for employer-reimbursed bicycle commuting expenses.</p>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr137"
    },
    "title": "TCJA Permanency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>TCJA Permanency Act </strong></p><p>This bill makes permanent multiple federal tax provisions enacted in 2017 by the Tax Cuts and Jobs Act.</p><p>The bill makes permanent the\u00a0</p><ul><li>individual tax rates of 10%, 12%, 22%, 24%, 32%, 35%, and 37%;</li><li>increased standard deduction;</li><li>personal exemption allowance repeal;</li><li>exclusion from income of student loans discharged due to death or disability;</li><li>qualified business income tax deduction (199A tax deduction);</li><li>allowance of ABLE account contributions in excess of the annual gift tax exclusion amount;</li><li>base estate and gift tax exclusion amount of $10 million (adjusted annually); and</li><li>alternative minimum tax exemption and phaseout amounts for noncorporate taxpayers.</li></ul><p>The bill makes permanent the child tax credit amounts of $2,000 per child and $500 for dependents, the $200,000 phaseout threshold ($400,000 for joint filers), and the refundable portion of the tax credit.\u00a0</p><p>The bill expands the expenses eligible for tax-free withdrawals from qualified tuition plans (529 plans) to include additional expenses associated with homeschool and\u00a0elementary and secondary schools (e.g.,\u00a0instructional materials, tutoring, test and enrollment fees, and educational therapies).\u00a0</p><p>The bill permanently eliminates certain miscellaneous itemized deductions and makes permanent the\u00a0</p><ul><li>state and local tax deduction limit of $10,000 ($5,000 for married individuals filing separately),</li><li>mortgage interest tax deduction limit of $750,000 ($375,000 for married individuals filing separately),</li><li>limit on the deduction of cash charitable contributions to 60% of a taxpayer\u2019s adjusted gross income, and</li><li>certain limits on casualty loss tax deductions.\u00a0</li></ul><p>The bill also permanently eliminates the exclusion from income for employer-reimbursed bicycle commuting expenses.</p>",
      "updateDate": "2026-04-21",
      "versionCode": "id119hr137"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr137ih.xml"
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
      "title": "TCJA Permanency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T13:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TCJA Permanency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T13:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to make permanent certain provisions of the Tax Cuts and Jobs Act affecting individuals, families, and small businesses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T13:18:20Z"
    }
  ]
}
```
