# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7156
- Title: SCAM Act
- Congress: 119
- Bill type: HR
- Bill number: 7156
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-04-24T08:06:32Z
- Update date including text: 2026-04-24T08:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7156",
    "number": "7156",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "E000294",
        "district": "6",
        "firstName": "Tom",
        "fullName": "Rep. Emmer, Tom [R-MN-6]",
        "lastName": "Emmer",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "SCAM Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:06:32Z",
    "updateDateIncludingText": "2026-04-24T08:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:00:10Z",
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
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "MN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "MN"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "MN"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "MO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "SC"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "VA"
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
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "AL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
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
      "sponsorshipDate": "2026-01-20",
      "state": "AL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
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
      "sponsorshipDate": "2026-01-20",
      "state": "GA"
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
      "sponsorshipDate": "2026-01-20",
      "state": "AZ"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "UT"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "MS"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "AL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "GA"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NC"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "AZ"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "SC"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "SC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NC"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
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
      "sponsorshipDate": "2026-01-20",
      "state": "GA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TX"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "SC"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "GA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "AL"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
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
      "sponsorshipDate": "2026-03-16",
      "state": "SC"
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
      "sponsorshipDate": "2026-03-16",
      "state": "IL"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "OK"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7156ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7156\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mr. Emmer (for himself, Mr. Stauber , Mrs. Fischbach , Mr. Finstad , Mr. Gooden , Mr. Nehls , Mr. Roy , Mr. Alford , Ms. Mace , Mr. Baird , Mr. McGuire , Mr. Weber of Texas , Mr. Donalds , Mr. Rogers of Alabama , Mr. Gill of Texas , Mr. Palmer , Ms. Van Duyne , Mr. Carter of Georgia , Mr. Gosar , Mr. Kennedy of Utah , Mr. Guest , Mr. Moore of Alabama , Mr. Bean of Florida , Mr. Hunt , Mr. Patronis , Mr. Jack , Mr. Moore of North Carolina , Mr. Rose , Mr. Self , Mr. Crane , Mr. Bost , Mr. Norman , Mr. Shreve , Mrs. Luna , Mr. Timmons , Mr. McDowell , Mr. Jackson of Texas , Mr. Collins , Mr. Goldman of Texas , Mr. Williams of Texas , Mr. Wilson of South Carolina , Mr. Austin Scott of Georgia , and Mr. Burchett ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo expand and clarify the grounds for civil denaturalization proceedings for individuals who have defrauded a governmental program, joined a terrorist organization, or committed certain criminal offenses.\n#### 1. Short titles\nThis Act may be cited as the Stop Citizenship Abuse and Misrepresentation Act or the SCAM Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nBecoming a naturalized United States citizen means not only having the right to live and work in the United States and gaining access to various social, economic, and political benefits, but also accepting sacred duties and obligations to our Nation.\n**(2)**\nIn recent years, many naturalized citizens have betrayed those sacred duties and obligations, eschewed responsible citizenship, and instead viewed their new citizenship status as a purely administrative benefit granting them access to privileges, immunities, and benefits they can leverage for their own personal gain.\n**(3)**\nNaturalization is a long-standing, time-honored, and essential American tradition.\n**(4)**\nAn applicant wishing to become a citizen of the United States must demonstrate, at the time of naturalization, that he or she is\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(5)**\nAny person who has been convicted of fraud against a governmental program demonstrates moral turpitude and any person who has been convicted of fraud against a governmental program after being extended the privilege of United States citizenship demonstrates, both at the time of such conviction and at the time of his or her naturalization, that he or she is not and was not\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(6)**\nAny person who affiliates with a foreign terrorist organization, such as a drug cartel, or engages in espionage puts our Nation's security at great risk of degradation and any person who affiliates with a foreign terrorist organization or engages in espionage after being extended the privilege of United States citizenship demonstrates, both at the time of such affiliation or espionage and at the time of his or her naturalization, that he or she is not and was not\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(7)**\nAny alien who has been convicted of an aggravated felony is deportable and designated as permanently ineligible for naturalization and any person who has been convicted of an aggravated felony after being extended the privilege of United States citizenship demonstrates, both at the time of such conviction and at the time of his or her naturalization, that he or she is not and was not\u2014\n**(A)**\na person of good moral character;\n**(B)**\nattached to the principles of the Constitution of the United States; and\n**(C)**\nwell disposed to the good order and happiness of the United States.\n**(8)**\nAs the Supreme Court has noted: An alien has no moral nor constitutional right to retain the privileges of citizenship if, by false evidence or the like, an imposition has been practiced upon the court, without which the certificate could not and would not have been issued. (Johannessen v. United States, 225 U.S. 227, 241 (1912)).\n**(9)**\nThe Supreme Court has also explained: No alien has the slightest right to naturalization unless all statutory requirements are complied with; and every certificate of citizenship must be treated as granted upon condition that the government may challenge it . . . and demand its cancelation unless issued in accordance with such requirements. If procured when prescribed qualifications have no existence in fact, it is illegally procured . . . . (United States v. Ginsberg, 243 U.S. 472, 475 (1917)).\n##### (b) Sense of Congress\nIt is the sense of Congress that the Supreme Court, in Costello v. INS, 376 U.S. 120 (1964), misconstrued the effects of denaturalization under section 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) for the reasons stated in the concurring opinion in Castillo v. Bondi, 140 F.4th 777 (6th Cir. 2025) (Thapar, J., concurring).\n#### 3. Purpose\nThe purpose of this Act is to expand and clarify the grounds for the United States to pursue civil denaturalization proceedings against individuals who have proven, by defrauding a governmental program, affiliating with a foreign terrorist organization, or committing certain criminal offenses, that, at the time they were naturalized, they lacked the good moral character, attachment to the Constitution of the United States, and disposition to the good order and happiness of the United States that our Nation demands of those who desire to become naturalized citizens.\n#### 4. Expanding and clarifying denaturalization for individuals who lack good moral character and an attachment to the Constitution of the United States and are not well disposed to the good order and happiness of the United States\nSection 340 of the Immigration and Nationality Act ( 8 U.S.C. 1451 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting the Attorney General or after It shall be the duty of ;\n**(2)**\nby redesignating subsections (d), (e), (f), (g), and (h) as subsections (i), (j), (k), (l), and (m), respectively; and\n**(3)**\nby inserting after subsection (c) the following:\n(d) Membership in foreign terrorist organization If a person, during the 10-year period beginning on the date on which he or she was naturalized under this chapter, associates with, conspires with, aids, or abets any foreign terrorist organization (as designated under section 219(a)), such action shall be considered prima facie and sufficient evidence that\u2014 (1) such person, at the time of his or her naturalization\u2014 (A) was not a person of good moral character; (B) was not attached to the principles of the Constitution of the United States; and (C) was not well disposed to the good order and happiness of the United States; (2) the order admitting such person to citizenship\u2014 (A) was obtained by concealment of a material fact or by willful misrepresentation; and (B) shall be revoked and set aside, along with the cancellation of his or her certificate of naturalization; and (3) such revocation and setting aside of such admission order and such cancellation of such certificate of naturalization shall be effective as of the original date of such order and certificate, respectively. (e) Defrauding Federal, State, local, or tribal governments If a person who has been naturalized under this chapter is convicted of, admits to having committed, or admits to committing acts constituting the essential elements of, an offense involving fraud, an attempt to defraud, or conspiracy to defraud the Federal Government, a State government, a local government, or a tribal government (such as defrauding the United States Government of a Federal public benefit (as defined in section 401 of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1611(c) ))) or defrauding a State or local government of a State or local public benefit (as defined in section 411(c) of such Act ( 8 U.S.C. 1621(c) )), of at least $10,000, and any act or acts leading to such conviction or admission began or occurred during the 10-year period beginning on the date of his or her naturalization, such conviction or admission shall be considered prima facie and sufficient evidence that\u2014 (1) such person, at the time of his or her naturalization\u2014 (A) was not a person of good moral character; (B) was not attached to the principles of the Constitution of the United States; and (C) was not well disposed to the good order and happiness of the United States; (2) the order admitting such person to citizenship\u2014 (A) was obtained by concealment of a material fact or by willful misrepresentation; and (B) shall be revoked and set aside, along with the cancellation of his or her certificate of naturalization; and (3) such revocation and setting aside of such admission order and such cancellation of such certificate of naturalization shall be effective as of the original date of such order and certificate, respectively. (f) Committing an aggravated felony or espionage offense If a person who has been naturalized under this chapter is convicted of, admits to having committed, or admits to committing acts constituting the essential elements of, an aggravated felony or espionage offense (including any offense described in section 792, 793, 794, 795, 796, 797, 798, 951, 1030(a)(1), 1831, 1832, 2152, 2153, 2154, 2155, or 2156 of title 18, United States Code; or an offense described in section 783 or 3121 of title 50, United States Code), and any act or acts leading to such conviction or admission began or occurred during the 10-year period beginning on the date on which he or she was naturalized, such conviction or admission shall be considered prima facie and sufficient evidence that\u2014 (1) such person, at the time of his or her naturalization\u2014 (A) was not a person of good moral character; (B) was not attached to the principles of the Constitution of the United States; and (C) was not well disposed to the good order and happiness of the United States; (2) the order admitting such person to citizenship\u2014 (A) was obtained by concealment of a material fact or by willful misrepresentation; and (B) shall be revoked and set aside, along with the cancellation of his or her certificate of naturalization; and (3) such revocation and setting aside of such admission order and such cancellation of such certificate of naturalization shall be effective as of the original date of such order and certificate, respectively. (g) Fallback provision If the 10-year period set forth in subsection (d), (e), or (f) is held to be unconstitutional or constitutionally insufficient by final judicial decision, for purposes of interpreting this Act\u2014 (1) such 10-year period shall be deemed to be a 5-year period, consistent with the published judicial opinion in Luria v. United States, 231 U.S. 27 (1913); and (2) every court of the United States shall construe such period to be 5 years. (h) Effects of denaturalization (1) Effective date The revocation and setting aside of a person\u2019s admission order and cancellation of the person\u2019s certificate of naturalization under this section shall be effective as of the original date of such order and certificate, respectively. Such denaturalization shall have retroactive effect, and the certificate of naturalization shall be treated as void from the date on which it was issued. (2) Removability Any person whose certificate of naturalization is cancelled under this section shall be removable pursuant to expedited proceedings described in section 238, regardless of\u2014 (A) the person\u2019s immigration status after denaturalization; and (B) the time that has elapsed since the date on which such person was naturalized. .\n#### 5. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any particular person or circumstance is held to be unconstitutional, the remaining provisions of this Act and amendments made by this Act, and the application of such provisions and amendments to any other person or circumstance, shall not be affected.",
      "versionDate": "2026-01-20",
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
        "actionDate": "2026-01-26",
        "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 301."
      },
      "number": "3674",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SCAM Act",
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
        "name": "Immigration",
        "updateDate": "2026-02-18T14:40:46Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7156ih.xml"
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
      "title": "SCAM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCAM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Citizenship Abuse and Misrepresentation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand and clarify the grounds for civil denaturalization proceedings for individuals who have defrauded a governmental program, joined a terrorist organization, or committed certain criminal offenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:24Z"
    }
  ]
}
```
