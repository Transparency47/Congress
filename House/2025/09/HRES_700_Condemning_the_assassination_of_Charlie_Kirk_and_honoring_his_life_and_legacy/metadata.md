# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/700
- Title: Condemning the assassination of Charlie Kirk and honoring his life and legacy.
- Congress: 119
- Bill type: HRES
- Bill number: 700
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2026-04-06T15:50:54Z
- Update date including text: 2026-04-06T15:50:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-11 - IntroReferral: Submitted in House
- Latest action: 2025-09-11: Submitted in House

## Actions

- 2025-09-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-11 - IntroReferral: Submitted in House
- 2025-09-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/700",
    "number": "700",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Condemning the assassination of Charlie Kirk and honoring his life and legacy.",
    "type": "HRES",
    "updateDate": "2026-04-06T15:50:54Z",
    "updateDateIncludingText": "2026-04-06T15:50:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-09-11T13:02:15Z",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "UT"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "UT"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "UT"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "SC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OK"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WV"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
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
      "sponsorshipDate": "2025-09-15",
      "state": "NJ"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AL"
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
      "sponsorshipDate": "2025-09-15",
      "state": "OH"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OH"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OH"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "MO"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TN"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "IN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WI"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "MT"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WI"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "KY"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "PA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
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
      "sponsorshipDate": "2025-09-15",
      "state": "GA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "WY"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "AL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "SC"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MD"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres700ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 700\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Kennedy of Utah (for himself, Mr. Owens , Mr. Moore of Utah , and Ms. Maloy ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nCondemning the assassination of Charlie Kirk and honoring his life and legacy.\nThat the House\u2014\n**(1)**\ncondemns the assassination of Charlie Kirk in the strongest possible terms;\n**(2)**\nextends its deepest condolences and sympathies to Charlie Kirk\u2019s family, including his wife, Erika, and their two young children; and\n**(3)**\nhonors Charlie Kirk\u2019s commitment to the constitutional principles of civil discussion and debate between all people of the United States, regardless of political affiliation.",
      "versionDate": "2025-09-11",
      "versionType": "IH"
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
        "actionDate": "2025-09-16",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6637; text: CR S6652)"
      },
      "number": "391",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution condemning the assassination of Charlie Kirk and honoring his life and legacy.",
      "type": "SRES"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-02T16:31:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-11",
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
          "measure-id": "id119hres700",
          "measure-number": "700",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-11",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres700v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-09-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution condemns the assassination of Charlie Kirk, extends condolences and sympathies to his family, and honors his commitment to civil discussion and debate.\u00a0</p>"
        },
        "title": "Condemning the assassination of Charlie Kirk and honoring his life and legacy."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres700.xml",
    "summary": {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns the assassination of Charlie Kirk, extends condolences and sympathies to his family, and honors his commitment to civil discussion and debate.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres700"
    },
    "title": "Condemning the assassination of Charlie Kirk and honoring his life and legacy."
  },
  "summaries": [
    {
      "actionDate": "2025-09-11",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns the assassination of Charlie Kirk, extends condolences and sympathies to his family, and honors his commitment to civil discussion and debate.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres700"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres700ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Condemning the assassination of Charlie Kirk and honoring his life and legacy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-25T06:18:21Z"
    },
    {
      "title": "Condemning the assassination of Charlie Kirk and honoring his life and legacy.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T08:07:03Z"
    }
  ]
}
```
