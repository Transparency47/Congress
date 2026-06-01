# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2410?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2410
- Title: Revitalizing Downtowns and Main Streets Act
- Congress: 119
- Bill type: HR
- Bill number: 2410
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-02-24T09:05:31Z
- Update date including text: 2026-02-24T09:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2410",
    "number": "2410",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Revitalizing Downtowns and Main Streets Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:31Z",
    "updateDateIncludingText": "2026-02-24T09:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:09:45Z",
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
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
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
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "AL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "WV"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
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
      "sponsorshipDate": "2025-03-27",
      "state": "UT"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
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
      "sponsorshipDate": "2025-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
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
      "sponsorshipDate": "2025-03-27",
      "state": "NV"
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
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "AZ"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NV"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "WA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "KS"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "GU"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "VI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NJ"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-25",
      "state": "VA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "LA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "OH"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "IL"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CT"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-23",
      "state": "FL"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2410ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2410\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Carey (for himself, Mr. Gomez , Mr. Larson of Connecticut , Mr. Fitzpatrick , Ms. Sewell , Ms. Tenney , Mr. Beyer , Mr. Kustoff , Ms. Chu , Mr. Kelly of Pennsylvania , Mr. Panetta , Mrs. Miller of West Virginia , Mr. Davis of Illinois , Mr. Moore of Utah , Mr. Evans of Pennsylvania , Ms. Malliotakis , Mr. Suozzi , Mr. Moran , Mr. Boyle of Pennsylvania , Mr. LaHood , Ms. S\u00e1nchez , Mr. Miller of Ohio , Ms. Moore of Wisconsin , Mr. Amodei of Nevada , Mr. Schneider , Mr. Ciscomani , Mr. Horsford , and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an investment credit for converting non-residential buildings to affordable housing.\n#### 1. Short title\nThis Act may be cited as the Revitalizing Downtowns and Main Streets Act .\n#### 2. Investment credit for conversion of non-residential buildings to affordable housing\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Affordable housing conversion credit (a) Allowance of credit For purposes of section 46, the affordable housing conversion credit for any taxable year is an amount equal to 20 percent of the qualified conversion expenditures of the taxpayer with respect to a qualified affordable housing building placed in service by the taxpayer during the taxable year. (b) Qualified conversion expenditures For purposes of this section\u2014 (1) In general The term qualified conversion expenditures means, with respect to any qualified affordable housing building, any amount properly chargeable to capital account\u2014 (A) for property for which depreciation is allowable under section 168, and (B) in connection with the qualified conversion of a qualified affordable housing building. (2) Certain expenditures not included The term qualified conversion expenditures does not include\u2014 (A) Limitation on period of conversion Except as provided in subsection (f), any amount paid or incurred other than during the 2-year period ending on the date on which the taxpayer places the qualified affordable housing building in service. (B) Cost of acquisition The cost of acquiring any building or interest therein. (3) Special rule for brownfields Paragraph (1)(A) shall not apply with respect to any expenditure for clean up of qualifying brownfield property (as defined in section 512(b)(19)). (4) Coordination with rehabilitation credit In the case of any qualified conversion expenditures which are taken into account for purposes of determining the rehabilitation credit under section 47, the amount of such expenditures taken into account under this section (determined without regard to this paragraph) shall be reduced by 50 percent. (c) Qualified conversion For purposes of this section\u2014 (1) In general The term qualified conversion means the conversion of an eligible commercial building into a qualified affordable housing building if the qualified conversion expenditures of the taxpayer with respect to such conversion exceed the greater of\u2014 (A) an amount equal to 50 percent of the adjusted basis of such building (determined immediately prior to such conversion), or (B) $100,000. (2) Eligible commercial building The term eligible commercial building means any building which, with respect to any conversion\u2014 (A) was originally placed in service not less than 20 years before the date on which such conversion begins, and (B) immediately prior to such conversion, was nonresidential real property (as defined in section 168). (d) Qualified affordable housing building For purposes of this section\u2014 (1) In general The term qualified affordable housing building means any residential building if during the 30-year period beginning on the date on which such building is placed in service by the taxpayer, not less than 20 percent of the residential units in the building are both rent-restricted and reserved for individuals whose income is 80 percent or less of the area median income. (2) Rent and income limitation For purposes of this subsection, rules similar to the rules of subsection (g) of section 42 shall apply to determine whether a unit is rent-restricted, treatment of units occupied by individuals whose incomes rise above the limit, and the treatment of units where Federal rental assistance is reduced as tenant\u2019s income increases. (e) Limitation on aggregate credit allowable (1) Credit may not exceed credit amount allocated to building (A) In general The amount of the credit determined under this section with respect to any building shall not exceed the qualified conversion credit dollar amount allocated to such building under this subsection by the housing credit agency of the State in which such building is located. (B) Time for making allocation Except in the case of an allocation which meets the requirements of subparagraph (C), an allocation shall be taken into account under subparagraph (A) only if it is made not later than the close of the calendar year in which the building is placed in service. (C) Exception where binding commitment An allocation meets the requirements of this subparagraph if there is a binding commitment (not later than the close of the calendar year in which the building is placed in service) by the housing credit agency to allocate a specified housing credit dollar amount to such building beginning in a later taxable year. (2) State limitation (A) In general The aggregate qualified conversion credit dollar amount which a housing credit agency of any State may allocate is the sum of\u2014 (i) the amount which bears the same ratio to the national qualified conversion credit limitation as\u2014 (I) the population of such State, bears to (II) the population of all States, plus (ii) the sum of any amounts determined under subparagraph (C). (B) National qualified conversion credit limitation The national qualified conversion credit limitation is $12,000,000,000. (C) Additional amounts provided for certain buildings in economically distressed areas (i) In general For purposes of subparagraph (A)(ii), in any case in which\u2014 (I) the housing credit agency of a State allocates an amount to a building which is located in an economically distressed area, and (II) the Secretary subsequently designates such amount for purposes of this paragraph, the amount determined under this paragraph with respect to such building shall be the amount originally allocated by the housing credit agency of the State under clause (i). (ii) Limitation The aggregate amount which the Secretary may designate under clause (i)(II) shall not exceed $3,000,000,000. (iii) Manner of designation Not later than 120 days after the date of the enactment of this section, the Secretary shall establish a program for determining the designation of amounts that may be designated under this subparagraph. (D) Reallocation of certain amounts (i) In general Notwithstanding subparagraph (A)\u2014 (I) no amount may be allocated under paragraph (1) by a housing credit agency of an undersubscribed State after December 31, 2028, and (II) the dollar amount determined under subparagraph (A) with respect to any oversubscribed State after such date shall be increased by such State\u2019s share of the reallocation amount. (ii) State share For purposes of clause (i), an oversubscribed State's share of the reallocation amount is the amount which bears the same ratio to the reallocation amount as\u2014 (I) the population of such State, bears to (II) the population of all oversubscribed States. (iii) Definitions For purposes of this subparagraph\u2014 (I) Undersubscribed State The term undersubscribed State means any State that is not an oversubscribed State. (II) Oversubscribed State The term oversubscribed State means any State the housing credit agency of which has allocated all of the qualified conversion credit dollar amount which may be allocated by it before the date described in clause (i)(I). (III) Reallocation amount The term reallocation amount means the sum of the amounts described in subparagraph (A) which have not been allocated by undersubscribed States before the date described in clause (i)(I). (3) Manner of allocation (A) Plan for allocation (i) In general Notwithstanding any other provision of this section, the qualified conversion credit dollar amount with respect to any building shall be zero unless such amount was allocated pursuant to a conversion credit allocation plan of the housing credit agency which is approved by the governmental unit (in accordance with rules similar to the rules of section 147(f)(2) (other than subparagraph (B)(ii) thereof)) of which such agency is a part. (ii) Conversion credit allocation plan For purposes of this subparagraph, the term conversion credit allocation plan means a plan\u2014 (I) which sets selection criteria for allocations, taking into account\u2014 (aa) whether the credit is needed to assure the financial feasibility of the conversion, (bb) the extent to which the conversion results in the creation of affordable housing, (cc) the extent to which the conversion results in the creation of housing near transportation, employment, and commercial opportunities, (dd) the extent to which the conversion will support small businesses and economic revitalization in the surrounding area, (ee) the degree of local government support for the conversion, and (ff) the readiness of the building for a qualified conversion, and (II) which provides a procedure that the agency (or an agent or other private contractor of such agency) will follow in monitoring for noncompliance with the requirements of subsection (d) and in notifying the Internal Revenue Service of such noncompliance. (B) Binding allocation agreements; reporting In making allocations of qualified conversion credit dollar amounts, each housing credit agency shall\u2014 (i) enter into binding agreements with taxpayers for the allocation of qualified conversion credit dollar amounts, which agreements shall specify the amount of qualified conversion credit dollar amount allocated to the building and the terms for any modifications or withdrawal of such allocation, and (ii) report to the Secretary, at such time and in such manner as the Secretary may require, the amount of allocations made with respect to any building. (C) State extended use requirements permitted past 30 years For purposes of this paragraph, a housing credit agency\u2019s plan shall not fail to be treated as a conversion credit allocation plan merely because it includes, and nothing in this section shall be construed to limit a binding allocation agreement from including, affordability or rent restriction requirements with respect to the building that apply for a longer period than the 30-year period described in subsections (d) and (g)(1)(B). (4) Definitions and other rules (A) Housing credit agency The term housing credit agency means, with respect to any State, the housing credit agency authorized under section 42(h)(8) or such other agency as authorized by the State for purposes of this section. (B) Economically distressed area The term economically distressed area means any area which\u2014 (i) has been designated as a qualified census tract under section 42(d)(5)(B)(ii) or as a difficult development area under section 42(d)(5)(B)(iii), or (ii) meets the requirement of section 301(a)(3) of the Public Works and Economic Development Act of 1965. (C) State The term State includes a possession of the United States. (D) Other rules Rules similar to the rules of subparagraphs (A) and (B) of section 42(h)(7) shall apply for purposes of this section. (f) Progress expenditures If the Secretary determines, on the basis of architectural plans and specifications that a qualified conversion is reasonably expected to exceed 2 years, rules similar to the rules of section 47(d) shall apply with respect to such conversion for purposes of this section. (g) Special rules for certain areas (1) Qualified census tracts and difficult development areas In the case of a qualified affordable housing building\u2014 (A) which is located in any area which is designated as a qualified census tract under section 42(d)(5)(B)(ii) or as a difficult development area under section 42(d)(5)(B)(iii)), and (B) with respect to which during 30-year period beginning on the date on which such building is placed in service by the taxpayer, not less than 20 percent of the residential units in the building are both rent-restricted and reserved for individuals whose income is 60 percent or less of the area median income, subsection (a) shall be applied by substituting 30 percent for 20 percent . (2) Historic preservation in rural areas (A) In general In the case of a qualified affordable housing building which is in a rural area and is part of an historic preservation project, the taxpayer may elect to substitute 35 percent for 20 percent under subsection (a) with respect to such portion of the aggregate qualified conversion expenditures taken into account under such subsection as does not exceed $2,000,000. (B) Definitions For purposes of this paragraph\u2014 (i) Rural area The term rural area shall have the meaning given such term under section 1393(a)(2). (ii) Historic preservation project The term historic preservation project means a qualified conversion which involves the certified rehabilitation of a certified historic structure. Whether conversion of a certified historic structure involves certified rehabilitation shall be determined under rules similar to the rules of section 47(c)(2)(C). (h) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations or other guidance\u2014 (1) providing for the recapture of the credit determined under subsection (a) if the qualified affordable housing building ceases to be a qualified affordable housing building during the 30-year period beginning on the date that such building is placed in service by the taxpayer, (2) detailing any certifications required from the taxpayer or any housing credit agency of a State, (3) with respect to the application of subsection (b)(4), (4) with respect to information reporting on allocations of qualified conversion credit dollar amounts, (5) providing rules for making a determination as to whether an area is described in subsection (e)(4)(B), and (6) which encourages housing credit agencies to allocate, to the extent practicable, qualified conversion credit dollar amounts to non-metropolitan counties within a State in proportion to the non-metropolitan population of the State, but only to the extent it is demonstrated within such non-metropolitan counties that there are sufficient qualified conversion expenditures to warrant such allocations. .\n##### (b) Transferability of credit\nSection 6418(f)(1)(A) of such Code is amended by adding at the end the following new clause:\n(xii) The affordable housing conversion credit determined under section 48F. .\n##### (c) Conforming amendments\n**(1)**\nSection 46 of such Code is amended in paragraph (5) by striking and at the end, in paragraph (6) by striking the period at the end and inserting , and , and by adding at the end the following new paragraph:\n(7) the affordable housing conversion credit. .\n**(2)**\nSection 49(a)(1)(C) of such Code is amended by striking and at the end of clause (v), in clause (vi) by striking the period at the end and inserting , and , and by adding at the end the follow new clause:\n(vii) the basis of any property which is being converted as part of a qualified conversion under section 48F. .\n**(3)**\nSection 50(a)(2)(E) of such Code is amended by striking or 48E(e) and inserting 48E(e), or 48F(f) .\n**(4)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of subtitle A of such Code is amended by adding at the end the following new item:\nSec. 48F. Affordable housing conversion credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to qualified affordable housing buildings (as defined in section 48F of the Internal Revenue Code of 1986, as added by this section) placed in service after the date of the enactment of this Act.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-03",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Armed Services, Homeland Security, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6390",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Make Housing Affordable and Defend Democracy Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-09T14:57:50Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2410ih.xml"
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
      "title": "Revitalizing Downtowns and Main Streets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Revitalizing Downtowns and Main Streets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide an investment credit for converting non-residential buildings to affordable housing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:35Z"
    }
  ]
}
```
