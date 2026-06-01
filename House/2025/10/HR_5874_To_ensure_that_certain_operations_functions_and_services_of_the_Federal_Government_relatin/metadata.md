# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5874
- Title: Firearm Access During Shutdowns Act
- Congress: 119
- Bill type: HR
- Bill number: 5874
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-04-16T08:07:10Z
- Update date including text: 2026-04-16T08:07:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-31 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-31 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5874",
    "number": "5874",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Firearm Access During Shutdowns Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:07:10Z",
    "updateDateIncludingText": "2026-04-16T08:07:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-31T17:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "AL"
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
      "sponsorshipDate": "2025-10-31",
      "state": "WY"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
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
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MO"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "CO"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TN"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "SC"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "WI"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "IA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "LA"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MT"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "FL"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "WV"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "SC"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "ID"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "CO"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "IN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "MD"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "NC"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "KY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "MN"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "KS"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "OH"
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
      "sponsorshipDate": "2025-11-12",
      "state": "IL"
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
      "sponsorshipDate": "2025-11-19",
      "state": "OH"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NE"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MS"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "AK"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "ND"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5874ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5874\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Cline (for himself, Mr. Carter of Georgia , Mr. Hunt , Mr. Moore of Alabama , Ms. Hageman , Mr. Harris of North Carolina , Mr. Collins , Mr. McCormick , Mr. Cloud , Mr. Weber of Texas , Mr. Burlison , Ms. Boebert , Mr. DesJarlais , Mr. Webster of Florida , Mr. Gooden , Ms. Mace , Mr. Fitzgerald , Mr. Feenstra , Mr. Jackson of Texas , Mr. Higgins of Louisiana , Mr. Downing , Mr. Fine , and Mr. Moore of West Virginia ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure that certain operations, functions, and services of the Federal Government relating to enforcement of firearms laws and firearm export licensing continue during a lapse in appropriations.\n#### 1. Short title\nThis Act may be cited as the Firearm Access During Shutdowns Act .\n#### 2. Continuation of certain firearm-related operations during Government shutdowns\n##### (a) In general\nThe operations, functions, and services described in subsection (b) shall be deemed to relate to an emergency involving the safety of human life or the protection of property for purposes of section 1342 of title 31, United States Code, and the employees carrying out those operations, functions, and services shall be deemed to be excepted employees, as defined in section 1341(c) of that title.\n##### (b) Operations, functions, and services\nThe operations, functions, and services described in this subsection are the operations, functions, and services of\u2014\n**(1)**\nthe National Instant Criminal Background Check System of the Federal Bureau of Investigation, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives;\n**(2)**\nthe Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives;\n**(3)**\nthe Bureau of Industry and Security of the Department of Commerce relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and\n**(4)**\nthe Directorate of Defense Trade Controls of the Department of State relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.",
      "versionDate": "2025-10-31",
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
        "actionDate": "2025-10-30",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3085",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Firearm Access During Shutdowns Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-10T16:17:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-31",
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
          "measure-id": "id119hr5874",
          "measure-number": "5874",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-31",
          "originChamber": "HOUSE",
          "update-date": "2025-11-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5874v00",
            "update-date": "2025-11-10"
          },
          "action-date": "2025-10-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Firearm Access During Shutdowns Act</strong></p><p>This bill requires various federal agencies to continue certain operations, functions, and services related to firearms during a government shutdown.</p><p>The bill applies to\u00a0</p><ul><li>the Federal Bureau of Investigation's National Instant Criminal Background Check System, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF);</li><li>the ATF's Directorate of Enforcement Programs and Services;</li><li>the activities of the Department of Commerce's Bureau of Industry and Security relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and</li><li>the activities of the Department of State's Directorate of Defense Trade Controls relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.</li></ul><p>Under the bill, (1) these operations, functions, and services are deemed to relate to an emergency involving the safety of human life or the protection of property; and (2) employees carrying out the operations, functions, and services are deemed to be excepted employees. (Under an exception in the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown. Employees who are required to work during a government shutdown because they fall under this or other exceptions are known as excepted employees.)</p>"
        },
        "title": "Firearm Access During Shutdowns Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5874.xml",
    "summary": {
      "actionDate": "2025-10-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Firearm Access During Shutdowns Act</strong></p><p>This bill requires various federal agencies to continue certain operations, functions, and services related to firearms during a government shutdown.</p><p>The bill applies to\u00a0</p><ul><li>the Federal Bureau of Investigation's National Instant Criminal Background Check System, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF);</li><li>the ATF's Directorate of Enforcement Programs and Services;</li><li>the activities of the Department of Commerce's Bureau of Industry and Security relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and</li><li>the activities of the Department of State's Directorate of Defense Trade Controls relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.</li></ul><p>Under the bill, (1) these operations, functions, and services are deemed to relate to an emergency involving the safety of human life or the protection of property; and (2) employees carrying out the operations, functions, and services are deemed to be excepted employees. (Under an exception in the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown. Employees who are required to work during a government shutdown because they fall under this or other exceptions are known as excepted employees.)</p>",
      "updateDate": "2025-11-10",
      "versionCode": "id119hr5874"
    },
    "title": "Firearm Access During Shutdowns Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Firearm Access During Shutdowns Act</strong></p><p>This bill requires various federal agencies to continue certain operations, functions, and services related to firearms during a government shutdown.</p><p>The bill applies to\u00a0</p><ul><li>the Federal Bureau of Investigation's National Instant Criminal Background Check System, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF);</li><li>the ATF's Directorate of Enforcement Programs and Services;</li><li>the activities of the Department of Commerce's Bureau of Industry and Security relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and</li><li>the activities of the Department of State's Directorate of Defense Trade Controls relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.</li></ul><p>Under the bill, (1) these operations, functions, and services are deemed to relate to an emergency involving the safety of human life or the protection of property; and (2) employees carrying out the operations, functions, and services are deemed to be excepted employees. (Under an exception in the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown. Employees who are required to work during a government shutdown because they fall under this or other exceptions are known as excepted employees.)</p>",
      "updateDate": "2025-11-10",
      "versionCode": "id119hr5874"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5874ih.xml"
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
      "title": "Firearm Access During Shutdowns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T08:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Firearm Access During Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T08:38:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that certain operations, functions, and services of the Federal Government relating to enforcement of firearms laws and firearm export licensing continue during a lapse in appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T08:33:21Z"
    }
  ]
}
```
