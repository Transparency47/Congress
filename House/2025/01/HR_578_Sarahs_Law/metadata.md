# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/578?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/578
- Title: Sarah’s Law
- Congress: 119
- Bill type: HR
- Bill number: 578
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2025-04-18T15:16:31Z
- Update date including text: 2025-04-18T15:16:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/578",
    "number": "578",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Sarah\u2019s Law",
    "type": "HR",
    "updateDate": "2025-04-18T15:16:31Z",
    "updateDateIncludingText": "2025-04-18T15:16:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:00:50Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "AZ"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "KS"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
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
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TN"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NE"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "FL"
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
      "sponsorshipDate": "2025-01-21",
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
      "sponsorshipDate": "2025-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "SC"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MI"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "LA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "KS"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WI"
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
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "AZ"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "CO"
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
      "sponsorshipDate": "2025-01-21",
      "state": "SC"
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
      "sponsorshipDate": "2025-01-21",
      "state": "MI"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WI"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TN"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "OK"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "IA"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MT"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "PA"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "SD"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "SC"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "GA"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "UT"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "FL"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr578ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 578\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. Feenstra (for himself, Ms. Tenney , Mr. Ciscomani , Mr. Estes , Mr. Bost , Mr. Rouzer , Mr. Nehls , Mr. DesJarlais , Mr. Finstad , Mr. Bacon , Ms. Salazar , Mr. Aderholt , Mrs. Miller of Illinois , Mr. Garbarino , Mr. McClintock , Ms. Mace , Mr. Bergman , Mr. Meuser , Mrs. Miller-Meeks , Mr. Balderson , Mr. Higgins of Louisiana , Mrs. Hinson , Mr. Babin , Mr. Edwards , Mr. Schmidt , Mr. Tiffany , Mr. Weber of Texas , Mr. Hamadeh of Arizona , Mr. Evans of Colorado , Mr. Timmons , Mr. Moolenaar , Mr. LaMalfa , Mr. Crenshaw , Mr. Wied , Mr. Ogles , Mr. Brecheen , Mr. Nunn of Iowa , Mr. Ellzey , Mr. Rulli , Mr. Downing , Mr. Thompson of Pennsylvania , Mr. Sessions , Mr. McDowell , Mr. Johnson of South Dakota , Mrs. Biggs of South Carolina , and Mr. McCormick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require U.S. Immigration and Customs Enforcement to take into custody certain aliens who have been charged in the United States with a crime that resulted in the death or serious bodily injury of another person, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Sarah\u2019s Law .\n#### 2. Mandatory detention of certain aliens charged with a crime resulting in death or serious bodily injury\nSection 236(c) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (C)\u2014\n**(i)**\nby striking sentence and inserting sentenced ; and\n**(ii)**\nby striking or ;\n**(B)**\nin subparagraph (D), by striking the comma at the end and inserting , or ; and\n**(C)**\nby inserting after subparagraph (D) the following:\n(E) (i) (I) is inadmissible under paragraph (6)(A), (6)(C), or (7) of section 212(a), (II) is deportable under section 237(a)(1)(B) as an alien whose nonimmigrant visa (or other documentation authorizing admission into the United States as a nonimmigrant) has been revoked under section 221(i), or (III) is deportable under section 237(a)(1)(C)(i), and (ii) is charged with, is arrested for, is convicted of, admits having committed, or admits committing acts which constitute the essential elements of any offense that resulted in the death or serious bodily injury (as defined in section 1365(h)(3) of title 18, United States Code) of another person, ; and\n**(2)**\nby adding at the end the following:\n(3) Notification requirement Upon encountering or gaining knowledge of an alien described in paragraph (1), the Secretary of Homeland Security shall\u2014 (A) obtain information from law enforcement agencies and from other available sources regarding the identity of any victims of the crimes for which such alien was charged, arrested, or convicted; and (B) provide the victim or, if the victim is deceased, a parent, guardian, spouse, or closest living relative of such victim, with information, on a timely and ongoing basis, including\u2014 (i) the alien\u2019s full name, aliases, date of birth, and country of nationality; (ii) the alien\u2019s immigration status and criminal history; (iii) the alien\u2019s custody status and any changes related to the alien\u2019s custody; and (iv) a description of any efforts by the United States Government to remove the alien from the United States. (4) Detainer The Secretary of Homeland Security shall issue a detainer for an alien described in paragraph (1)(E) and, if the alien is not otherwise detained by Federal, State, or local officials, shall effectively and expeditiously take custody of the alien. .\n#### 3. Savings provision\nNothing in this Act, or the amendments made by this Act, may be construed to limit the rights of crime victims under any other provision of law, including section 3771 of title 18, United States Code.",
      "versionDate": "2025-01-21",
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
        "name": "Immigration",
        "updateDate": "2025-02-20T19:12:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr578",
          "measure-number": "578",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-04-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr578v00",
            "update-date": "2025-04-18"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sarah's Law</strong></p><p>This bill requires the Department of Justice or the Department of Homeland Security (DHS) to detain a non-U.S. national (<em>alien</em> under federal law) who is unlawfully present in the United States and has been charged with, arrested for, convicted of, or admits to having committed acts that constitute the essential elements of\u00a0a crime that resulted in the death or serious bodily injury of another person.</p><p>DHS must obtain information about the identity of any victims of the crimes for which the detained individual was charged or convicted. DHS shall provide the victim, or a relative or guardian of a deceased victim, with information about the detained individual, including name, date of birth, nationality, immigration status, criminal history, and a description of any related removal efforts.</p>"
        },
        "title": "Sarah\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr578.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sarah's Law</strong></p><p>This bill requires the Department of Justice or the Department of Homeland Security (DHS) to detain a non-U.S. national (<em>alien</em> under federal law) who is unlawfully present in the United States and has been charged with, arrested for, convicted of, or admits to having committed acts that constitute the essential elements of\u00a0a crime that resulted in the death or serious bodily injury of another person.</p><p>DHS must obtain information about the identity of any victims of the crimes for which the detained individual was charged or convicted. DHS shall provide the victim, or a relative or guardian of a deceased victim, with information about the detained individual, including name, date of birth, nationality, immigration status, criminal history, and a description of any related removal efforts.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr578"
    },
    "title": "Sarah\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sarah's Law</strong></p><p>This bill requires the Department of Justice or the Department of Homeland Security (DHS) to detain a non-U.S. national (<em>alien</em> under federal law) who is unlawfully present in the United States and has been charged with, arrested for, convicted of, or admits to having committed acts that constitute the essential elements of\u00a0a crime that resulted in the death or serious bodily injury of another person.</p><p>DHS must obtain information about the identity of any victims of the crimes for which the detained individual was charged or convicted. DHS shall provide the victim, or a relative or guardian of a deceased victim, with information about the detained individual, including name, date of birth, nationality, immigration status, criminal history, and a description of any related removal efforts.</p>",
      "updateDate": "2025-04-18",
      "versionCode": "id119hr578"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr578ih.xml"
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
      "title": "Sarah\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sarah\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require U.S. Immigration and Customs Enforcement to take into custody certain aliens who have been charged in the United States with a crime that resulted in the death or serious bodily injury of another person, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:26Z"
    }
  ]
}
```
