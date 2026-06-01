# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3474?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3474
- Title: Federal Mechanical Insulation Act
- Congress: 119
- Bill type: HR
- Bill number: 3474
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-02-19T23:41:15Z
- Update date including text: 2026-02-19T23:41:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-15 - Committee: Referred to the Subcommittee on Energy.
- 2025-11-19 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-11-19 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 51 - 0.
- 2026-02-04 - Calendars: Placed on the Union Calendar, Calendar No. 411.
- 2026-02-04 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-481.
- 2026-02-04 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-481.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-15 - Committee: Referred to the Subcommittee on Energy.
- 2025-11-19 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-11-19 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 51 - 0.
- 2026-02-04 - Calendars: Placed on the Union Calendar, Calendar No. 411.
- 2026-02-04 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-481.
- 2026-02-04 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-481.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3474",
    "number": "3474",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Federal Mechanical Insulation Act",
    "type": "HR",
    "updateDate": "2026-02-19T23:41:15Z",
    "updateDateIncludingText": "2026-02-19T23:41:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-04",
      "calendarNumber": {
        "calendar": "U00411"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 411.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-04",
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
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-481.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-481.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 51 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
        "item": [
          {
            "date": "2026-02-04T16:15:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-03T21:59:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-15T14:06:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-19T21:56:05Z",
                "name": "Reported by"
              },
              {
                "date": "2025-11-19T21:55:32Z",
                "name": "Markup by"
              },
              {
                "date": "2025-05-15T20:51:50Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MI"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
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
      "sponsorshipDate": "2025-06-24",
      "state": "FL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
      "state": "IL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-07",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NE"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "IA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NC"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "IL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "WI"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "TX"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "OH"
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
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "IN"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
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
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NC"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "RI"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "LA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "VA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NJ"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3474ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3474\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Weber of Texas (for himself and Ms. S\u00e1nchez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo clarify that the installation of mechanical insulation property is an energy or water efficiency measure that may be used in Federal buildings for purposes of section 543(f) of the National Energy Conservation Policy Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Mechanical Insulation Act .\n#### 2. Installation of mechanical insulation property as an energy or water efficiency measure in Federal buildings\n##### (a) Definition of mechanical insulation property\nSection 543(f)(1) of the National Energy Conservation Policy Act ( 42 U.S.C. 8253(f)(1) ) is amended by adding at the end the following:\n(I) Mechanical insulation property The term mechanical insulation property means insulation materials, facings, and accessory products\u2014 (i) placed in service\u2014 (I) in connection with a mechanical system; and (II) in a manner that meets or exceeds the minimum requirements of the American Society of Heating, Refrigerating and Air-Conditioning Engineers Standard 90.1, as in effect on the date of enactment of this subparagraph; and (ii) which result in a reduction in energy loss from the mechanical system. .\n##### (b) Comprehensive energy and water evaluations\nSection 543(f)(3)(A) of the National Energy Conservation Policy Act ( 42 U.S.C. 8253(f)(3)(A) ) is amended by inserting , including identification of energy- and water-saving measures (including the installation of mechanical insulation property, if applicable), after a comprehensive energy and water evaluation .",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr3474rh.xml",
      "text": "IB\nUnion Calendar No. 411\n119th CONGRESS\n2d Session\nH. R. 3474\n[Report No. 119\u2013481]\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Weber of Texas (for himself and Ms. S\u00e1nchez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nFebruary 4, 2026 Additional sponsors: Mr. Lawler , Ms. Scholten , Mrs. Torres of California , Mr. Fitzpatrick , Mr. Bilirakis , Mr. Garbarino , Mr. Tonko , Ms. Budzinski , Ms. Kelly of Illinois , Ms. Schakowsky , Mrs. Miller of Illinois , Mr. Babin , Mr. Bacon , Mr. Gimenez , Mrs. Miller-Meeks , Mrs. Fletcher , Ms. Schrier , Mr. Murphy , Mr. Mullin , Ms. Barrag\u00e1n , Mr. Davis of Illinois , Ms. Moore of Wisconsin , Mr. Nehls , Mr. Turner of Ohio , Mr. Vindman , Mr. Messmer , Mrs. Dingell , Mr. Davis of North Carolina , Mr. Kean , Mr. Hudson , Mr. Magaziner , Mr. Carter of Louisiana , Mr. Wittman , Mr. Smith of New Jersey , and Mr. Griffith\nFebruary 4, 2026 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo clarify that the installation of mechanical insulation property is an energy or water efficiency measure that may be used in Federal buildings for purposes of section 543(f) of the National Energy Conservation Policy Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Mechanical Insulation Act .\n#### 2. Installation of mechanical insulation property as an energy or water efficiency measure in Federal buildings\n##### (a) Definition of mechanical insulation property\nSection 543(f)(1) of the National Energy Conservation Policy Act ( 42 U.S.C. 8253(f)(1) ) is amended by adding at the end the following:\n(I) Mechanical insulation property The term mechanical insulation property means insulation materials, facings, and accessory products\u2014 (i) placed in service\u2014 (I) in connection with a mechanical system; and (II) in a manner that meets or exceeds the minimum requirements of the American Society of Heating, Refrigerating and Air-Conditioning Engineers Standard 90.1, as in effect on the date of enactment of this subparagraph; and (ii) which result in a reduction in energy loss from the mechanical system. .\n##### (b) Comprehensive energy and water evaluations\nSection 543(f)(3)(A) of the National Energy Conservation Policy Act ( 42 U.S.C. 8253(f)(3)(A) ) is amended by inserting , including identification of energy- and water-saving measures (including the installation of mechanical insulation property, if applicable), after a comprehensive energy and water evaluation .",
      "versionDate": "2026-02-04",
      "versionType": "Reported in House"
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
            "name": "Building construction",
            "updateDate": "2025-12-11T19:09:33Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-12-11T19:17:11Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-12-11T19:09:39Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2025-12-11T19:16:57Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-12-11T19:17:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-29T15:23:07Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3474ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr3474rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Federal Mechanical Insulation Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-05T08:38:22Z"
    },
    {
      "title": "Federal Mechanical Insulation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Mechanical Insulation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify that the installation of mechanical insulation property is an energy or water efficiency measure that may be used in Federal buildings for purposes of section 543(f) of the National Energy Conservation Policy Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:22Z"
    }
  ]
}
```
