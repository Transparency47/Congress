# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7033
- Title: Federal Correctional Officer Paycheck Protection Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7033
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-04-14T08:05:31Z
- Update date including text: 2026-04-14T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7033",
    "number": "7033",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Federal Correctional Officer Paycheck Protection Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:31Z",
    "updateDateIncludingText": "2026-04-14T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
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
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:02:15Z",
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
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NH"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NE"
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
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CO"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "PA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NH"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "MN"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "MA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
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
      "sponsorshipDate": "2026-01-30",
      "state": "NJ"
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
      "sponsorshipDate": "2026-02-02",
      "state": "TX"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NJ"
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
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
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
      "sponsorshipDate": "2026-02-04",
      "state": "DC"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CT"
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
      "sponsorshipDate": "2026-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
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
      "sponsorshipDate": "2026-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "GA"
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
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "OH"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "WV"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
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
      "sponsorshipDate": "2026-03-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MD"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "GA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7033ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7033\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Goldman of New York (for himself, Ms. Goodlander , Mr. Bresnahan , Mrs. Trahan , Mr. Bacon , Mr. Fitzpatrick , Mr. Boyle of Pennsylvania , Mr. LaLota , Mr. McGovern , Mr. Ciscomani , Mr. Deluzio , Mr. Lawler , Mr. Riley of New York , Mr. Mackenzie , Mr. Neguse , Mr. Meuser , Mr. Pappas , Mr. Moulton , Mr. Stanton , and Ms. Gillen ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to improve recruitment and retention of Federal correctional officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Correctional Officer Paycheck Protection Act of 2026 .\n#### 2. Special base rates of pay for Federal correctional officers\n##### (a) In general\nSubchapter III of chapter 53 of title 5, United States Code, is amended by inserting after section 5332a the following:\n5332b. Special base rates of pay for Federal correctional officers (a) Definitions In this section\u2014 (1) the term Federal correctional officer means a correctional officer (without regard to whether the position of the individual is classified in the 0007 series established by the Office of Personnel Management)\u2014 (A) who is employed by the Bureau of Prisons; and (B) (i) the duties of the position of whom\u2014 (I) primarily relate to the custody, control, or supervision of inmates within the Bureau of Prisons; or (II) routinely include direct inmate contact in a custodial setting; (ii) who, in the case of an employee who holds a supervisory or administrative position and is subject to subchapter III of chapter 83 or chapter 84, but who does not qualify to be considered a law enforcement officer within the meaning of section 8331(20) or 8401(17), as applicable, holds a position, the duties of which, if they included routine custodial inmate contact, would be as described in clause (i); or (iii) who, in the case of an employee who is not subject to subchapter III of chapter 83 or chapter 84, holds a position that the Office of Personnel Management, pursuant to written position classification applicable to the Bureau of Prisons, determines would satisfy clause (i) or (ii) if the employee were subject to subchapter III of chapter 83 or chapter 84; (2) the term General Schedule base rate means an annual rate of basic pay established under section 5332 before any additions, such as a locality-based comparability payment under section 5304 or 5304a or a special rate supplement under section 5305; and (3) the term LEO special base rate has the meaning given the term in section 531.602 of title 5, Code of Federal Regulations, or any successor regulation. (b) Special base rates of pay (1) Entitlement to special rate Notwithstanding section 5332, a Federal correctional officer is entitled to a special base rate of pay, which shall\u2014 (A) replace the otherwise applicable General Schedule base rate or LEO special base rate for the Federal correctional officer; (B) be basic pay for all purposes, including the purposes of applying\u2014 (i) sections 5304, 5304a, and 5595; (ii) subchapter V of chapter 55; and (iii) chapters 83 and chapter 84; and (C) be computed as provided in paragraph (2) and adjusted at the time of adjustments in the General Schedule base rate or LEO special base rate. (2) Computation The special base rate for a Federal correctional officer shall be calculated by increasing the applicable General Schedule base rate or LEO special base rate for the Federal correctional officer by 35 percent and rounding the result to the nearest whole dollar, provided that such special base rate does not exceed the rate of basic pay payable for level V of the Executive Schedule. .\n##### (b) Clerical amendment\nThe table of sections for subchapter III of chapter 53 of title 5, United States Code, is amended by inserting after the item relating to section 5332a the following:\n5332b. Special base rates of pay for Federal correctional officers. .\n##### (c) Certain prevailing rate employees\nSection 5343 of title 5, United States Code, is amended by adding at the end the following:\n(h) (1) In this subsection, the term covered employee means an employee\u2014 (A) who is described in section 5342(a)(2)(A) and is employed by the Bureau of Prisons; (B) the duties of the position of whom\u2014 (i) primarily relate to the custody, control, or supervision of inmates; or (ii) routinely include direct inmate contact in a custodial setting; and (C) the position of whom is classified as not higher than grade 9 of the Federal Wage System. (2) The Attorney General shall increase the wage rates of each covered employee by 35 percent. (3) An increased wage rate under paragraph (2) shall be basic pay for the same purposes as the wage rate otherwise established under this section. (4) An increase under this subsection may not cause the wage rate of an employee to increase to a rate that would produce an annualized rate in excess of the annual rate for level IV of the Executive Schedule. .\n#### 3. Application\n##### (a) Definition\nIn this section, the term Federal correctional officer has the meaning given the term in section 5332b(a) of title 5, United States Code, as added by section 2 of this Act.\n##### (b) Sunset\nSubject to subsection (c), on the date that is 5 years after the date of enactment of this Act, the authority provided under sections 5332b and 5343(h) of title 5, United States Code, as added by section 2 of this Act, shall terminate and those sections are repealed.\n##### (c) Review and determination\n**(1) Review**\nNot later than 180 days before the expiration of the 5-year period described in subsection (b), the Inspector General of the Department of Justice (referred to in this section as the Inspector General ) shall conduct a review, and submit a report on that review to Congress, of\u2014\n**(A)**\nthe extent to which the Bureau of Prisons has, pursuant to the authority provided under sections 5332b and 5343(h) of title 5, United States Code, as added by section 2 of this Act\u2014\n**(i)**\nreduced or eliminated the use of non-custodial employees to perform the duties of Federal correctional officers (commonly known as, and referred to in this section as, augmentation ); and\n**(ii)**\nreduced excessive mandatory overtime for Federal correctional officers; and\n**(B)**\nthe impact of the special base rates of pay under sections 5332b and 5343(h) of title 5, United States Code, as added by section 2 of this Act, on recruitment, retention, and institutional safety with respect to Federal correctional officers.\n**(2) Continuing authority**\n**(A) Determination**\nIf, under the review conducted under paragraph (1), the Inspector General determines that the Bureau of Prisons has demonstrated measurable progress in eliminating augmentation and reducing excessive mandatory overtime for Federal correctional officers, subsection (b) of this section shall have no force or effect and the authority provided under sections 5332b and 5343(h) of title 5, United States Code, as added by section 2 of this Act, shall continue to apply.\n**(B) Notice**\nThe Inspector General shall include a determination made under subparagraph (A) in the report submitted to Congress under paragraph (1).",
      "versionDate": "2026-01-13",
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
        "actionDate": "2026-01-13",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3626",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Correctional Officer Paycheck Protection Act of 2026",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-22T20:51:58Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7033ih.xml"
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
      "title": "Federal Correctional Officer Paycheck Protection Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Correctional Officer Paycheck Protection Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to improve recruitment and retention of Federal correctional officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:32Z"
    }
  ]
}
```
