# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/685?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/685
- Title: SAVE Moms and Babies Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 685
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-05-14T08:07:35Z
- Update date including text: 2026-05-14T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/685",
    "number": "685",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000566",
        "district": "5",
        "firstName": "Robert",
        "fullName": "Rep. Latta, Robert E. [R-OH-5]",
        "lastName": "Latta",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "SAVE Moms and Babies Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:35Z",
    "updateDateIncludingText": "2026-05-14T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:04:35Z",
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
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
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
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NE"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "KS"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MD"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
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
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
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
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "LA"
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
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WI"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "AL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "IL"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "ND"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-14",
      "state": "WY"
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
      "sponsorshipDate": "2026-04-14",
      "state": "IN"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "AL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "PA"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "OK"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "UT"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
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
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "IN"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "SC"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NE"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "FL"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "GA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "FL"
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
      "sponsorshipDate": "2026-04-21",
      "state": "IN"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "FL"
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
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
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
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
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
      "sponsorshipDate": "2026-04-28",
      "state": "AR"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr685ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 685\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Latta (for himself, Mr. Rouzer , Mr. Brecheen , Mr. Strong , Mrs. Miller of Illinois , Mr. Webster of Florida , Mr. Finstad , Mr. Aderholt , Mr. Feenstra , Mr. Smith of New Jersey , Mr. Fulcher , Mr. Flood , Mr. Mann , Mr. Harris of Maryland , Mr. Fong , Mr. Ellzey , Mr. Weber of Texas , Mr. McCormick , Mr. Moolenaar , Mr. Ogles , Mr. Guest , Mr. Higgins of Louisiana , Mr. Palmer , Mr. Moore of North Carolina , Mr. Shreve , and Mr. LaHood ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to prohibit the approval of new abortion drugs, to prohibit investigational use exemptions for abortion drugs, and to impose additional regulatory requirements with respect to previously approved abortion drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support And Value Expectant Moms and Babies Act of 2025 or the SAVE Moms and Babies Act of 2025 .\n#### 2. Abortion drugs prohibited\n##### (a) In general\nSection 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) (as amended by Public Law 117\u2013328 ) is amended by adding at the end the following:\n(aa) Abortion drugs (1) Prohibitions The Secretary shall not approve\u2014 (A) any application submitted under subsection (b) or (j) for marketing an abortion drug; or (B) grant an investigational use exemption under subsection (i) for\u2014 (i) an abortion drug; or (ii) any investigation in which the unborn child of a woman known to be pregnant is knowingly destroyed. (2) Previously approved abortion drugs If an approval described in paragraph (1) is in effect for an abortion drug as of the date of enactment of the Support And Value Expectant Moms and Babies Act of 2025 , the Secretary shall\u2014 (A) not approve any labeling change\u2014 (i) to approve the use of such abortion drug after 70 days gestation; or (ii) to approve the dispensing of such abortion drug by any means other than in-person administration by the prescribing health care practitioner; (B) treat such abortion drug as subject to section 503(b)(1); and (C) require such abortion drug to be subject to a risk evaluation and mitigation strategy under section 505\u20131 that at a minimum\u2014 (i) requires health care practitioners who prescribe such abortion drug\u2014 (I) to be certified in accordance with the strategy; and (II) to not be acting in their capacity as a pharmacist; (ii) as part of the certification process referred to in clause (i), requires such practitioners\u2014 (I) to have the ability to assess the duration of pregnancy accurately; (II) to have the ability to diagnose ectopic pregnancies; (III) to have the ability to provide surgical intervention in cases of incomplete abortion or severe bleeding; (IV) to have the ability to ensure patient access to medical facilities equipped to provide blood transfusions and resuscitation, if necessary; and (V) to report any deaths or other adverse events associated with the use of such abortion drug to the Food and Drug Administration and to the manufacturer of such abortion drug, identifying the patient by a non-identifiable reference and the serial number from each package of such abortion drug; (iii) limits the dispensing of such abortion drug to patients\u2014 (I) in a clinic, medical office, or hospital by means of in-person administration by the prescribing health care practitioner; and (II) not in pharmacies or any setting other than the health care settings described in subclause (I); (iv) requires the prescribing health care practitioner to give to the patient documentation on any risk of serious complications associated with use of such abortion drug and receive acknowledgment of such receipt from the patient; (v) requires all known adverse events associated with such abortion drug to be reported, excluding any individually identifiable patient information, to the Food and Drug Administration by the\u2014 (I) manufacturers of such abortion drug; and (II) prescribers of such abortion drug; and (vi) requires reporting of administration of the abortion drug as required by State law, or in the absence of a State law regarding such reporting, in the same manner as a surgical abortion. (3) Reporting on adverse events by other health care practitioners The Secretary shall require all other health care practitioners to report to the Food and Drug Administration any adverse events experienced by their patients that are connected to use of an abortion drug, excluding any individually identifiable patient information. (4) Rule of construction Nothing in this section shall be construed to restrict the authority of the Federal Government, or of a State, to establish, implement, and enforce requirements and restrictions with respect to abortion drugs under provisions of law other than this section that are in addition to the requirements and restrictions under this section. (5) Definitions In this section: (A) The term abortion drug means any drug, substance, or combination of drugs or substances that is intended for use or that is in fact used (irrespective of how the product is labeled) to intentionally kill the unborn child of a woman known to be pregnant, or to intentionally terminate the pregnancy of a woman known to be pregnant, with an intention other than\u2014 (i) to produce a live birth; (ii) to remove a dead unborn child; or (iii) to treat an ectopic pregnancy. (B) The term adverse event includes each of the following: (i) A fatality. (ii) An ectopic pregnancy. (iii) A hospitalization. (iv) A blood loss requiring a transfusion. (v) An infection, including endometritis, pelvic inflammatory disease, and pelvic infections with sepsis. (vi) A severe infection. (C) The term gestation means the period of days beginning on the first day of the last menstrual period. (D) The term health care practitioner means any individual who is licensed, registered, or otherwise permitted, by the United States or the jurisdiction in which the individual practices, to prescribe drugs subject to section 503(b)(1). (E) The term unborn child means an individual organism of the species homo sapiens, beginning at fertilization, until the point of being born alive as defined in section 8(b) of title 1, United States Code. .\n##### (b) Ongoing investigational use\nIn the case of any investigational use of a drug pursuant to an investigational use exemption under section 505(i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(i) ) that was granted before the date of enactment of this Act, such exemption is deemed to be rescinded as of the day that is 3 years after the date of enactment of this Act if the Secretary would be prohibited by section 505(aa)(1)(B) of the Federal Food, Drug, and Cosmetic Act, as added by subsection (a), from granting such exemption as of such day.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2026-01-27",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (Sponsor introductory remarks on measure: CR S292)"
      },
      "number": "3697",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAVE Moms and Babies Act of 2026",
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
            "name": "Abortion",
            "updateDate": "2025-03-19T16:02:43Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-03-19T16:02:43Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-03-19T16:02:43Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-03-19T16:02:43Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-19T16:02:43Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-03-19T16:02:43Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-03-19T16:02:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T13:45:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr685",
          "measure-number": "685",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr685v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Support And Value Expectant Moms and Babies Act of 2025 or the SAVE Moms and Babies Act of 2025</strong></p><p>This bill prohibits the Food and Drug Administration (FDA) from approving any new drug (either as a brand-name drug or a generic) intended to terminate a pregnancy and imposes additional restrictions on such drugs that are already approved.</p><p>Under the bill, an already-approved drug intended to terminate a pregnancy may be dispensed to a patient only with a prescription. Furthermore, the FDA may not approve any labeling change that would authorize (1) using the drug after 70 days of gestation, or (2) dispensing the drug by any means other than in-person administration by the prescribing health care practitioner.</p><p>The FDA must also impose additional restrictions on such already-approved drugs, including by (1) requiring the prescribing health care practitioner to receive a special certification, (2) prohibiting the practitioner from also acting as the dispensing pharmacist, and (3) requiring the practitioner to have the ability to provide surgical intervention to the patient.</p><p>The bill also rescinds any investigational use exemption already granted to such a drug if the bill would have prohibited the FDA from granting the exemption. (Currently, the FDA may grant an exemption to certain market approval requirements if a drug is intended solely for use in safety and effectiveness investigations.)</p>"
        },
        "title": "SAVE Moms and Babies Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr685.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Support And Value Expectant Moms and Babies Act of 2025 or the SAVE Moms and Babies Act of 2025</strong></p><p>This bill prohibits the Food and Drug Administration (FDA) from approving any new drug (either as a brand-name drug or a generic) intended to terminate a pregnancy and imposes additional restrictions on such drugs that are already approved.</p><p>Under the bill, an already-approved drug intended to terminate a pregnancy may be dispensed to a patient only with a prescription. Furthermore, the FDA may not approve any labeling change that would authorize (1) using the drug after 70 days of gestation, or (2) dispensing the drug by any means other than in-person administration by the prescribing health care practitioner.</p><p>The FDA must also impose additional restrictions on such already-approved drugs, including by (1) requiring the prescribing health care practitioner to receive a special certification, (2) prohibiting the practitioner from also acting as the dispensing pharmacist, and (3) requiring the practitioner to have the ability to provide surgical intervention to the patient.</p><p>The bill also rescinds any investigational use exemption already granted to such a drug if the bill would have prohibited the FDA from granting the exemption. (Currently, the FDA may grant an exemption to certain market approval requirements if a drug is intended solely for use in safety and effectiveness investigations.)</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr685"
    },
    "title": "SAVE Moms and Babies Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Support And Value Expectant Moms and Babies Act of 2025 or the SAVE Moms and Babies Act of 2025</strong></p><p>This bill prohibits the Food and Drug Administration (FDA) from approving any new drug (either as a brand-name drug or a generic) intended to terminate a pregnancy and imposes additional restrictions on such drugs that are already approved.</p><p>Under the bill, an already-approved drug intended to terminate a pregnancy may be dispensed to a patient only with a prescription. Furthermore, the FDA may not approve any labeling change that would authorize (1) using the drug after 70 days of gestation, or (2) dispensing the drug by any means other than in-person administration by the prescribing health care practitioner.</p><p>The FDA must also impose additional restrictions on such already-approved drugs, including by (1) requiring the prescribing health care practitioner to receive a special certification, (2) prohibiting the practitioner from also acting as the dispensing pharmacist, and (3) requiring the practitioner to have the ability to provide surgical intervention to the patient.</p><p>The bill also rescinds any investigational use exemption already granted to such a drug if the bill would have prohibited the FDA from granting the exemption. (Currently, the FDA may grant an exemption to certain market approval requirements if a drug is intended solely for use in safety and effectiveness investigations.)</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr685"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr685ih.xml"
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
      "title": "SAVE Moms and Babies Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAVE Moms and Babies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Support And Value Expectant Moms and Babies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to prohibit the approval of new abortion drugs, to prohibit investigational use exemptions for abortion drugs, and to impose additional regulatory requirements with respect to previously approved abortion drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:23Z"
    }
  ]
}
```
