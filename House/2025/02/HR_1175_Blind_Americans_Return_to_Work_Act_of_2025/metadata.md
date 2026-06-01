# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1175?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1175
- Title: Blind Americans Return to Work Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1175
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2026-05-21T08:08:36Z
- Update date including text: 2026-05-21T08:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1175",
    "number": "1175",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S000250",
        "district": "17",
        "firstName": "Pete",
        "fullName": "Rep. Sessions, Pete [R-TX-17]",
        "lastName": "Sessions",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Blind Americans Return to Work Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:36Z",
    "updateDateIncludingText": "2026-05-21T08:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:00:15Z",
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
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "LA"
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
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MN"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "IN"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "DE"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CO"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
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
      "sponsorshipDate": "2025-05-29",
      "state": "VA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "WI"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AZ"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OK"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "WI"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OH"
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
      "sponsorshipDate": "2025-10-14",
      "state": "ME"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VT"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NH"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "CO"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-02",
      "state": "DC"
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
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "OR"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "KS"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "KS"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "MS"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
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
      "sponsorshipDate": "2026-02-24",
      "state": "GA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CO"
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
      "sponsorshipDate": "2026-04-21",
      "state": "AZ"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MD"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
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
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sponsorshipDate": "2026-04-29",
      "state": "UT"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NC"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1175ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1175\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Sessions (for himself, Mr. Mfume , Mr. Fields , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to require the Commissioner of Social Security to carry out a demonstration project relating to disability benefits of blind individuals.\n#### 1. Short title\nThis Act may be cited as the Blind Americans Return to Work Act of 2025 .\n#### 2. Demonstration project for blind Americans\nTitle II of the Social Security Act ( 42 U.S.C. 401 et seq. ) is amended by adding at the end the following:\n235. Demonstration project for blind Americans (a) In general For a 20-year period beginning not later than 180 days after the date of enactment of this section, the Commissioner shall carry out the demonstration project described in subsection (b). (b) Benefit offset (1) In general The demonstration project described in this subsection is a project under which benefits under section 223 are modified pursuant to paragraph (2) for individuals\u2014 (A) who are entitled to a benefit under 223(a)(1) for a month during the 120-month period beginning with the first month of the 20-year period described in subsection (a); and (B) whose disability is by reason of blindness (as defined in section 216(i)(1)). (2) Modification For purposes of paragraph (1), the benefit under section 223 of an individual described in paragraph (1) is modified as follows: (A) In determining eligibility for such benefit, a determination of whether the individual is disabled under section 223(d)(1)(B) shall be made without respect to substantial gainful activity. (B) Any benefit payable to the individual for a month (other than a benefit payable for any month prior to the first month beginning after the date on which the individual\u2019s entitlement to such benefit is determined) shall be reduced, except such benefit may not be reduced below $0, by $1 for every $2 by which the individual\u2019s earnings derived from services paid during such month exceeds the sum of\u2014 (i) the exempt amount described in section 223(d)(4)(A); and (ii) an amount equal to the individual\u2019s expenses reasonably attributable to the earning of any income for such month. (C) Entitlement to any such benefit shall not terminate due to earnings derived from services. (D) The period of trial work described in section 222(c) shall not apply. (E) The provisions related to the termination month in subsection (a)(1) of section 223 shall not apply. (c) Authority To waive compliance with certain requirements In carrying out the demonstration project under this section, the Commissioner may waive compliance with the benefit requirements of this title and the requirements of section 1148 as they relate to the programs established under this title, insofar as necessary to carry out the demonstration project. (d) Opt out After the 120-month period described in subsection (b)(1)(A), an individual described in such subsection may opt out of the demonstration project. .",
      "versionDate": "2025-02-10",
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
        "actionDate": "2026-04-16",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4334",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Blind Americans Return to Work Act of 2026",
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
            "name": "Disability and paralysis",
            "updateDate": "2025-04-24T16:22:20Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-04-24T16:22:09Z"
          },
          {
            "name": "Hearing, speech, and vision care",
            "updateDate": "2025-04-24T16:22:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-03-17T14:32:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
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
          "measure-id": "id119hr1175",
          "measure-number": "1175",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-08-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1175v00",
            "update-date": "2025-08-04"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Blind Americans Return to Work Act of 2025</strong></p><p>This bill requires the Social Security Administration to carry out a demonstration project during which blind Social Security Disability Insurance (SSDI)\u00a0beneficiaries receive reduced benefits commensurate with income above certain thresholds.</p><p>Under current law, only individuals who earn under a specified monthly income, known as the <em>substantial gainful activity</em> (SGA) threshold, are considered disabled and thereby eligible for SSDI benefits. For blind workers, this limit is $2,700 per month in 2025. SSDI beneficiaries may earn beyond the SGA threshold for a limited period of time, known as the <em>trial work period</em>, before their benefits are suspended and ultimately terminate.</p><p>The bill establishes a 20-year demonstration project during which individuals who are entitled to SSDI benefits by reason of blindness and who earn above the SGA threshold continue to receive benefits at an amount gradually reduced commensurate with their earnings beyond a specified amount.</p><p>During this period, blind workers\u2019 SSDI benefits must be reduced by $1 for every $2 that a worker earns above the sum of (1) the SGA threshold, and (2) the worker\u2019s expenses reasonably attributable to their work. The SGA threshold may not be used to determine whether an individual is disabled during this period, and blind workers\u2019 SSDI benefits may not be terminated due to work-related earnings. The trial work period also must not apply.\u00a0</p><p>After 10 years, affected beneficiaries may opt out of the modified benefits structure.\u00a0</p>"
        },
        "title": "Blind Americans Return to Work Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1175.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Blind Americans Return to Work Act of 2025</strong></p><p>This bill requires the Social Security Administration to carry out a demonstration project during which blind Social Security Disability Insurance (SSDI)\u00a0beneficiaries receive reduced benefits commensurate with income above certain thresholds.</p><p>Under current law, only individuals who earn under a specified monthly income, known as the <em>substantial gainful activity</em> (SGA) threshold, are considered disabled and thereby eligible for SSDI benefits. For blind workers, this limit is $2,700 per month in 2025. SSDI beneficiaries may earn beyond the SGA threshold for a limited period of time, known as the <em>trial work period</em>, before their benefits are suspended and ultimately terminate.</p><p>The bill establishes a 20-year demonstration project during which individuals who are entitled to SSDI benefits by reason of blindness and who earn above the SGA threshold continue to receive benefits at an amount gradually reduced commensurate with their earnings beyond a specified amount.</p><p>During this period, blind workers\u2019 SSDI benefits must be reduced by $1 for every $2 that a worker earns above the sum of (1) the SGA threshold, and (2) the worker\u2019s expenses reasonably attributable to their work. The SGA threshold may not be used to determine whether an individual is disabled during this period, and blind workers\u2019 SSDI benefits may not be terminated due to work-related earnings. The trial work period also must not apply.\u00a0</p><p>After 10 years, affected beneficiaries may opt out of the modified benefits structure.\u00a0</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hr1175"
    },
    "title": "Blind Americans Return to Work Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Blind Americans Return to Work Act of 2025</strong></p><p>This bill requires the Social Security Administration to carry out a demonstration project during which blind Social Security Disability Insurance (SSDI)\u00a0beneficiaries receive reduced benefits commensurate with income above certain thresholds.</p><p>Under current law, only individuals who earn under a specified monthly income, known as the <em>substantial gainful activity</em> (SGA) threshold, are considered disabled and thereby eligible for SSDI benefits. For blind workers, this limit is $2,700 per month in 2025. SSDI beneficiaries may earn beyond the SGA threshold for a limited period of time, known as the <em>trial work period</em>, before their benefits are suspended and ultimately terminate.</p><p>The bill establishes a 20-year demonstration project during which individuals who are entitled to SSDI benefits by reason of blindness and who earn above the SGA threshold continue to receive benefits at an amount gradually reduced commensurate with their earnings beyond a specified amount.</p><p>During this period, blind workers\u2019 SSDI benefits must be reduced by $1 for every $2 that a worker earns above the sum of (1) the SGA threshold, and (2) the worker\u2019s expenses reasonably attributable to their work. The SGA threshold may not be used to determine whether an individual is disabled during this period, and blind workers\u2019 SSDI benefits may not be terminated due to work-related earnings. The trial work period also must not apply.\u00a0</p><p>After 10 years, affected beneficiaries may opt out of the modified benefits structure.\u00a0</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hr1175"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1175ih.xml"
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
      "title": "Blind Americans Return to Work Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Blind Americans Return to Work Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to require the Commissioner of Social Security to carry out a demonstration project relating to disability benefits of blind individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T06:18:33Z"
    }
  ]
}
```
