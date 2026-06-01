# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3289
- Title: Fiscal Commission Act
- Congress: 119
- Bill type: HR
- Bill number: 3289
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-03-04T09:06:49Z
- Update date including text: 2026-03-04T09:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-08 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3289",
    "number": "3289",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Fiscal Commission Act",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:49Z",
    "updateDateIncludingText": "2026-03-04T09:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-08T13:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
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
      "sponsorshipDate": "2025-05-08",
      "state": "SC"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "HI"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NJ"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
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
      "sponsorshipDate": "2025-05-08",
      "state": "UT"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NE"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "ME"
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
      "sponsorshipDate": "2025-05-08",
      "state": "PA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "SD"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "OH"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WI"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "FL"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AZ"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
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
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "IL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "IN"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "KY"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "MN"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "VA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
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
      "sponsorshipDate": "2025-07-17",
      "state": "AR"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "NC"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "MI"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "IN"
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
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "S000929",
      "district": "5",
      "firstName": "Victoria",
      "fullName": "Rep. Spartz, Victoria [R-IN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Spartz",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "IN"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3289ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3289\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mr. Huizenga (for himself, Mr. Peters , Mr. Timmons , Mr. Case , Mr. Mills , Mr. Conaway , Mr. Bergman , Mr. Cuellar , Mr. Moore of Utah , Ms. Perez , Mr. Smith of Nebraska , Mr. Golden of Maine , Mr. Fitzpatrick , Mr. Gray , Mr. Johnson of South Dakota , Mr. Landsman , Mr. Grothman , Mr. Moskowitz , Mr. Schweikert , Mr. Quigley , Mr. Moolenaar , Ms. Scholten , Mr. Rouzer , Mr. Schneider , Mrs. Houchin , Mr. Suozzi , Mr. Valadao , Mr. Panetta , and Mr. Barr ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a commission on fiscal responsibility and reform.\n#### 1. Short title\nThis Act may be cited as the Fiscal Commission Act .\n#### 2. Definitions\nIn this Act:\n**(1) Co-chair**\nThe term co-chair means an individual appointed to serve as a co-chair of the Fiscal Commission under section 3(a)(3)(B)(i).\n**(2) Fiscal Commission**\nThe term Fiscal Commission means the commission established under section 3(a).\n**(3) Implementing bill**\nThe term implementing bill means a bill or joint resolution consisting solely of the legislative text the Fiscal Commission approves and submits under clauses (i) and (v), respectively, of section 3(a)(2)(B).\n**(4) Outside expert**\nThe term outside expert is an individual who is not an elected official or an officer or employee of the Federal Government or of any State.\n#### 3. Establishment of Fiscal Commission\n##### (a) Establishment of fiscal commission\n**(1) Establishment**\n**(A) In general**\nNot later than 60 days after the date of enactment of this Act, there is established in Congress a Fiscal Commission.\n**(B) Goals**\nThe goals of the Commission shall be to educate, and bring awareness to, the American public about the fiscal path the Nation is on, including\u2014\n**(i)**\neducating the American people so they understand the fiscal state of the Nation and the cost of not addressing such state; and\n**(ii)**\ninforming the American people about the deterioration of our Nation\u2019s fiscal health, and that the debt poses a significant risk to the Nation\u2019s long-term fiscal sustainability with implications for future generations.\n**(2) Duties**\n**(A) Improve fiscal situation**\n**(i) In general**\nThe Fiscal Commission shall identify policies to\u2014\n**(I)**\nmeaningfully improve the long-term fiscal condition of the Federal Government, including reducing the debt and deficit;\n**(II)**\nachieve a sustainable ratio of the public debt of the Federal Government to the gross domestic product of the United States, which shall be not more than 100 percent, by fiscal year 2039; and\n**(III)**\nimprove the solvency of Federal programs for which a Federal trust fund exists for a period of at least 75 years.\n**(ii) Requirements**\nIn carrying out clause (i), the Fiscal Commission shall, to the extent practicable, consider the budgetary effects of changes in economic output, employment, capital stock, and other macroeconomic variables resulting from public and private investments and propose recommendations that meaningfully improve the long-term fiscal condition of the Federal Government, including\u2014\n**(I)**\nchanges to address the current levels of discretionary appropriations, direct spending, and revenues and the gap between current revenues and expenditures of the Federal Government; and\n**(II)**\nchanges to address the growth of discretionary appropriations, direct spending, and revenues and the gap between the projected revenues and expenditures of the Federal Government.\n**(iii) Recommendations of committees**\nNot later than 60 days after the date described in paragraph (1), each committee of the Senate and the House of Representatives may transmit to the Fiscal Commission any recommendations of the committee relating to changes in law to further the duties described in clause (ii).\n**(iv) Interim report**\nThe Fiscal Commission may meet to consider, and vote on, an interim report on\u2014\n**(I)**\nany findings, conclusions, or recommendations of the Fiscal Commission described in subparagraph (A)(i);\n**(II)**\nany findings or recommendations with respect to carrying out the goals described in paragraph (1)(B); and\n**(III)**\nas the Fiscal Commission determines appropriate, any findings resulting from any hearing held or evidence received by the Commission.\n**(B) Report identified policies**\n**(i) In general**\nNotwithstanding paragraph (4)(D)(ii)(II), and consistent with clause (vi), not earlier than November 4, 2026, but not later than November 13, 2026, the Fiscal Commission shall meet to consider, and vote on\u2014\n**(I)**\na report that contains a detailed statement of the findings, conclusions, and recommendations of the Fiscal Commission described in subparagraph (A)(i) and the estimate of the Congressional Budget Office required under paragraph (4)(D)(ii); and\n**(II)**\nlegislative language to carry out the recommendations of the Fiscal Commission in the report described in subclause (I), which shall include a statement of the economic and budgetary effects of the recommendations.\n**(ii) Approval of report and legislative language**\nA report and legislative language of the Fiscal Commission under clause (i) shall require the approval of a majority of the members of the Fiscal Commission, provided that such majority shall be required to include not less than 2 members of the Fiscal Commission appointed by members of the Republican Party and 2 members appointed by members of the Democratic party.\n**(iii) Additional views**\n**(I) In general**\nA member of the Fiscal Commission who gives notice of an intention to file supplemental, minority, or additional views at the time of the final Fiscal Commission vote on the approval of the report and legislative language of the Fiscal Commission under clause (i) shall be entitled to 3 days to file those views in writing with the staff director of the Fiscal Commission.\n**(II) Inclusion in report**\nViews filed under subclause (I) shall be included in the report of the Fiscal Commission under clause (i) and printed in the same volume, or part thereof, and such inclusion shall be noted on the cover of the report, except that, in the absence of timely notice, the report may be printed and transmitted immediately without such views.\n**(iv) Report and legislative language to be made public**\nUpon the approval or disapproval of a report and legislative language under clause (i) by the Fiscal Commission, the Fiscal Commission shall promptly, and not more than 24 hours after the approval or disapproval or, if timely notice is given under clause (iii), not more than 24 hours after additional views are filed under such clause, make the report, the legislative language, and a record of the vote on the report and legislative language available to the public.\n**(v) Submission of report and legislative language**\nIf a report and legislative language are approved by the Fiscal Commission under clause (i), not later than 3 days after the date on which the report and legislative language are made available to the public under clause (iv), the Fiscal Commission shall submit the report and legislative language to the President, the Vice President, the Speaker of the House of Representatives, and the majority and minority leaders of each House of Congress.\n**(vi) Extension**\nThe Fiscal Commission may extend the deadline set forth in clause (i) to April 13, 2027, if the Fiscal Commission determines that additional time is necessary to complete their duties under this Act. Such extension shall require the approval of a majority of the members of the Fiscal Commission, provided that such majority shall be required to include not less than 2 members of the Fiscal Commission appointed by members of the Republican Party and 2 members appointed by members of the Democratic party.\n**(C) Public awareness campaign**\nNot later than 30 days after the date the Fiscal Commission submits the report under paragraph (2)(B)(v), the Fiscal Commission shall complete a national campaign to increase public awareness and education with respect to the fiscal condition of the Federal Government.\n**(3) Membership**\n**(A) In general**\nThe Fiscal Commission shall be composed of 16 members appointed, not later than 14 days after the date described in paragraph (1) and with due consideration to chairs and ranking minority members of the committees and subcommittees of subject matter jurisdiction (as applicable), as follows:\n**(i)**\n3 individuals from among the Members of the Senate, and 1 outside expert, appointed by the majority leader of the Senate.\n**(ii)**\n3 individuals from among the Members of the Senate, and 1 outside expert, appointed by the minority leader of the Senate.\n**(iii)**\n3 individuals from among the Members of the House of Representatives, and 1 outside expert, appointed by the Speaker of the House of Representatives.\n**(iv)**\n3 individuals from among the Members of the House of Representatives, and 1 outside expert, appointed by the minority leader of the House of Representatives.\n**(B) Co-chairs**\n**(i) In general**\nNot later than 14 days after the date described in paragraph (1), with respect to the Fiscal Commission\u2014\n**(I)**\nthe leadership of the Senate and House of Representatives of the same political party as the President shall appoint 1 individual from among the members of the Fiscal Commission who shall serve as a co-chair of the Fiscal Commission; and\n**(II)**\nthe leadership of the Senate and House of Representatives of the opposite political party as the President shall appoint 1 individual from among the members of the Fiscal Commission who shall serve as a co-chair of the Fiscal Commission.\n**(ii) Staff director**\nWith respect to the Fiscal Commission, the co-chairs of the Fiscal Commission, acting jointly, shall hire the staff director of the Fiscal Commission.\n**(C) Period of appointment**\n**(i) In general**\nThe members of the Fiscal Commission shall be appointed for the life of the Fiscal Commission.\n**(ii) Vacancy**\n**(I) In general**\nAny vacancy in the Fiscal Commission shall not affect the powers of the Fiscal Commission, but shall be filled not later than 14 days after the date on which the vacancy occurs, in the same manner as the original appointment was made.\n**(II) Ineligible members**\nIf a member of the Fiscal Commission who was appointed as a Member of the Senate or the House Representatives ceases to be a Member of the Senate or the House of Representatives, as applicable\u2014\n**(aa)**\nthe member shall no longer be a member of the Fiscal Commission; and\n**(bb)**\na vacancy in the Fiscal Commission exists.\n**(4) Administration**\n**(A) In general**\nWith respect to the Fiscal Commission, to enable the Fiscal Commission to exercise the powers, functions, and duties of the Fiscal Commission, there are authorized to be disbursed by the Senate the actual and necessary expenses of the Fiscal Commission approved by the co-chairs of the Fiscal Commission, subject to the rules and regulations of the Senate.\n**(B) Expenses**\nWith respect to the Fiscal Commission, in carrying out the functions of the Fiscal Commission, the Fiscal Commission is authorized to incur expenses in the same manner and under the same conditions as the Joint Economic Committee is authorized under section 11(d) of the Employment Act of 1946 ( 15 U.S.C. 1024(d) ).\n**(C) Quorum**\nWith respect to the Fiscal Commission, 7 members of the Fiscal Commission shall constitute a quorum for purposes of voting, meeting, and holding hearings. Outside experts shall not count for purposes of determining whether there is a quorum under this subparagraph.\n**(D) Voting**\n**(i) Proxy voting**\nNo proxy voting shall be allowed on behalf of any member of the Fiscal Commission.\n**(ii) Congressional budget office estimates**\n**(I) In general**\nThe Director of the Congressional Budget Office shall, with respect to the legislative language of the Fiscal Commission under paragraph (2)(B)(i)(II), provide to the Fiscal Commission\u2014\n**(aa)**\nestimates of the legislative language in accordance with sections 308(a) and 201(f) of the Congressional Budget Act of 1974 ( 2 U.S.C. 639(a) and 601(f)); and\n**(bb)**\ninformation on the budgetary effects of the legislative language on the long-term fiscal outlook.\n**(II) Limitation**\nThe Fiscal Commission may not vote on any version of the report, recommendations, or legislative language of the Fiscal Commission under paragraph (2)(B)(i) unless the estimates and information described in subclause (I) of this clause are made available for consideration by all members of the Fiscal Commission not later than 48 hours before that vote, as certified by the co-chairs of the Fiscal Commission.\n**(iii) Limitations on outside experts**\nOnly members of the Fiscal Commission who are Members of the Senate or the House of Representatives may vote on any matter of the Fiscal Commission. An outside expert serving as a member of the Fiscal Commission shall be a nonvoting member.\n**(E) Meetings**\n**(i) Initial meeting**\nNot later than 45 days after the date described in paragraph (1), the Fiscal Commission shall hold the first meeting of the Fiscal Commission.\n**(ii) Agenda**\nFor each meeting of the Fiscal Commission, the co-chairs of the Fiscal Commission shall provide an agenda to the members of the Fiscal Commission not later than 48 hours before the meeting.\n**(F) Hearings**\n**(i) In general**\nThe Fiscal Commission may, for the purpose of carrying out this section, hold such hearings, sit and act at such times and places, require attendance of witnesses and production of books, papers, and documents, take such testimony, receive such evidence, and administer such oaths as the Fiscal Commission considers advisable.\n**(ii) Hearing procedures and responsibilities of co-chairs**\n**(I) Announcement**\nThe co-chairs of the Fiscal Commission shall make a public announcement of the date, place, time, and subject matter of any hearing to be conducted under this subparagraph not later than 7 days before the date of the hearing, unless the co-chairs determine that there is good cause to begin such hearing on an earlier date.\n**(II) Written statement**\nA witness appearing before the Fiscal Commission shall file a written statement of the proposed testimony of the witness not later than 2 days before the date of the appearance of the witness, unless the co-chairs of the Fiscal Commission\u2014\n**(aa)**\ndetermine that there is good cause for the witness to not file the written statement; and\n**(bb)**\nwaive the requirement that the witness file the written statement.\n**(iii) Hearing requirements**\nThe Fiscal Commission shall hold not less than 6 hearings under this subparagraph, which shall include\u2014\n**(I)**\nfield hearings through the Nation;\n**(II)**\nhearings to solicit testimony from appropriate officials of the executive branch; and\n**(III)**\nhearings to solicit testimony from Members of Congress (in this subclause defined as a member of the Senate or the House of Representatives, a Delegate to the House of Representatives, and the Resident Commissioner from Puerto Rico).\n**(G) Technical assistance and consultation**\nUpon written request of the co-chairs of the Fiscal Commission, the head of a Federal agency (including legislative branch agencies) shall provide technical assistance to, and consult with, the Fiscal Commission in order for the Fiscal Commission to carry out their duties.\n**(H) Outside expert**\nAny outside expert appointed to the Fiscal Commission\u2014\n**(i)**\nshall not be considered to be a Federal employee for any purpose by reason of service on the Fiscal Commission; and\n**(ii)**\nshall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Commission.\n##### (b) Staff of Fiscal Commission\n**(1) In general**\nThe co-chairs of the Fiscal Commission may jointly appoint and fix the compensation of staff of the Fiscal Commission as the co-chairs determine necessary, in accordance with the guidelines, rules, and requirements relating to employees of the Senate.\n**(2) Ethical standards**\n**(A) Senate**\nMembers appointed by Members of the Senate who serve on the Fiscal Commission and staff of the Fiscal Commission shall adhere to the ethics rules of the Senate.\n**(B) House of representatives**\nMembers appointed by Members of the House of Representatives who serve on the Fiscal Commission shall be governed by the ethics rules and requirements of the House of Representatives.\n##### (c) Termination\nThe Fiscal Commission shall terminate on the date that is 30 days after the date the Fiscal Commission submits the report under subsection (a)(2)(B)(v).\n#### 4. Expedited consideration of implementing bills\n##### (a) Qualifying legislation\nOnly an implementing bill shall be entitled to expedited consideration under this section.\n##### (b) Consideration in the House of Representatives\n**(1) Introduction**\nIf the Fiscal Commission approves and submits legislative language under clauses (i) and (v), respectively, of section 3(a)(2)(B), the implementing bill consisting solely of that legislative language shall be introduced in the House of Representatives (by request)\u2014\n**(A)**\nby the majority leader of the House of Representatives, or by a Member of the House of Representatives designated by the majority leader of the House of Representatives, on the third legislative day after the date the Fiscal Commission approves and submits such legislative language; or\n**(B)**\nif the implementing bill is not introduced under subparagraph (A), by any Member of the House of Representatives on any legislative day beginning on the legislative day after the legislative day described in subparagraph (A).\n**(2) Referral and reporting**\nAny committee of the House of Representatives to which an implementing bill is referred shall report the implementing bill to the House of Representatives without amendment not later than 5 legislative days after the date on which the implementing bill was so referred. If any committee of the House of Representatives to which an implementing bill is referred fails to report the implementing bill within that period, that committee shall be automatically discharged from consideration of the implementing bill, and the implementing bill shall be placed on the appropriate calendar.\n**(3) Proceeding to consideration**\nAfter the last committee authorized to consider an implementing bill reports it to the House of Representatives or has been discharged from its consideration, it shall be in order to move to proceed to consider the implementing bill in the House of Representatives. Such a motion shall not be in order after the House of Representatives has disposed of a motion to proceed with respect to the implementing bill. The previous question shall be considered as ordered on the motion to its adoption without intervening motion.\n**(4) Consideration**\nThe implementing bill shall be considered as read. All points of order against the implementing bill and against its consideration are waived. The previous question shall be considered as ordered on the implementing bill to its passage without intervening motion except 2 hours of debate equally divided and controlled by the proponent and an opponent.\n**(5) Vote on passage**\nThe vote on passage of the implementing bill shall occur pursuant to the constraints under clause 8 of rule XX of the Rules of the House of Representatives.\n##### (c) Expedited procedure in the Senate\n**(1) Introduction in the Senate**\nOn the day on which an implementing bill is submitted to the Senate under section 3(a)(2)(B)(v), the implementing bill shall be introduced, by request, by the majority leader of the Senate for himself or herself and the minority leader of the Senate, or by any Member so designated by them. If the Senate is not in session on the day on which such implementing bill is submitted, it shall be introduced as provided on the first day thereafter on which the Senate is in session. Such implementing bill shall be placed on the Calendar of Business under General Orders.\n**(2) Proceeding**\nNotwithstanding rule XXII of the Standing Rules of the Senate, it is in order, not later than 2 days of session after the date on which an implementing bill is placed on the Calendar, for the majority leader of the Senate or the designee of the majority leader to move to proceed to the consideration of the implementing bill. It shall also be in order for any Member of the Senate to move to proceed to the consideration of the implementing bill at any time after the conclusion of such 2-day period. A motion to proceed is in order even though a previous motion to the same effect has been disagreed to. All points of order against the motion to proceed to the implementing bill are waived. The motion to proceed is not debatable. The motion is not subject to a motion to postpone. A motion to reconsider the vote by which the motion is agreed to or disagreed to shall not be in order. If a motion to proceed to the consideration of the implementing bill is agreed to, it shall remain the unfinished business until disposed of. All points of order against the implementing bill and against its consideration are waived.\n**(3) No amendments**\nAn amendment to the implementing bill, a motion to postpone, a motion to proceed to the consideration of other business, or a motion to commit the implementing bill is not in order.\n**(4) Rulings of the chair on procedure**\nAppeals from the decisions of the Chair relating to the application of the rules of the Senate, as the case may be, to the procedure relating to an implementing bill shall be decided without debate.\n##### (d) Amendment\nAn implementing bill shall not be subject to amendment in either the Senate or the House of Representatives.\n##### (e) Consideration by the other House\n**(1) In general**\nIf, before passing an implementing bill, one House receives from the other House an implementing bill consisting solely of the text of the implementing bill approved by the Fiscal Commission\u2014\n**(A)**\nthe implementing bill of the other House shall not be referred to a committee; and\n**(B)**\nthe procedure in the receiving House shall be the same as if no implementing bill had been received from the other House until the vote on passage, when the implementing bill received from the other House shall supplant the implementing bill of the receiving House.\n**(2) Revenue measures**\nThis subsection shall not apply to the House of Representatives if an implementing bill received from the Senate is a revenue measure.\n##### (f) Rules To coordinate action with other house\n**(1) Treatment of implementing bill of other House**\nIf an implementing bill is not introduced in the Senate or the Senate fails to consider an implementing bill under this section, the implementing bill of the House of Representatives consisting of legislative language approved by the same Fiscal Commission as the implementing bill in the Senate shall be entitled to expedited floor procedures under this section.\n**(2) Treatment of companion measures in the Senate**\nIf, following passage of an implementing bill in the Senate, the Senate then receives from the House of Representatives an implementing bill consisting of the same text as the Senate-passed implementing bill, the House-passed implementing bill shall not be debatable. The vote on passage of the implementing bill in the Senate shall be considered to be the vote on passage of the implementing bill received from the House of Representatives.\n**(3) Vetoes**\nIf the President vetoes an implementing bill, consideration of a veto message in the Senate under this paragraph shall be 10 hours equally divided between the majority and minority leaders of the Senate or the designees of the majority and minority leaders of the Senate.\n#### 5. Funding\nFunding for the Fiscal Commission shall be derived in equal portions from\u2014\n**(1)**\nthe contingent fund of the Senate from the appropriations account Miscellaneous Items , subject to the rules and regulations of the Senate; and\n**(2)**\nthe applicable accounts of the House of Representatives.\n#### 6. Rulemaking\nThe provisions of this Act are enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and, as such, the provisions\u2014\n**(A)**\nshall be considered as part of the rules of each House, respectively, or of that House to which they specifically apply; and\n**(B)**\nshall supersede other rules only to the extent that they are inconsistent therewith; and\n**(2)**\nwith full recognition of the constitutional right of either House to change such rules (so far as relating to such House) at any time, in the same manner, and to the same extent as in the case of any other rule of such House.",
      "versionDate": "2025-05-08",
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
        "name": "Congress",
        "updateDate": "2025-05-20T14:57:39Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3289ih.xml"
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
      "title": "Fiscal Commission Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fiscal Commission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a commission on fiscal responsibility and reform.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:39Z"
    }
  ]
}
```
