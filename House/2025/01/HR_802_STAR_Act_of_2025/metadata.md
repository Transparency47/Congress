# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/802?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/802
- Title: STAR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 802
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-03-10T17:06:22Z
- Update date including text: 2026-03-10T17:06:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/802",
    "number": "802",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "STAR Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-10T17:06:22Z",
    "updateDateIncludingText": "2026-03-10T17:06:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:04:40Z",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "WA"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-28",
      "state": "MI"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NY"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NJ"
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
      "sponsorshipDate": "2025-01-28",
      "state": "AL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
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
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "IN"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "DE"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "OR"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
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
      "sponsorshipDate": "2025-06-04",
      "state": "VA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "AZ"
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
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr802ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 802\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Moore of Utah (for himself, Ms. DelBene , Mr. McCaul , Ms. Matsui , Mr. Moolenaar , Mr. Krishnamoorthi , Ms. Tenney , Mr. Khanna , Mr. Morelle , Mr. Buchanan , Mr. Carson , Mr. Gottheimer , Ms. Sewell , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to add qualified semiconductor design expenditures to the advanced manufacturing investment credit.\n#### 1. Short title\nThis Act may be cited as the Semiconductor Technology Advancement and Research Act of 2025 or the STAR Act of 2025 .\n#### 2. Qualified semiconductor design expenditures added to advanced manufacturing investment credit\n##### (a) In general\nSection 48D of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a), by striking an amount equal to and all that follows through the period and inserting\n, with respect to an eligible taxpayer, an amount equal to the sum of\u2014 (1) 25 percent of the qualified investment for such taxable year with respect to any advanced manufacturing facility of such taxpayer, and (2) 25 percent of the qualified semiconductor design expenditures paid or incurred by such taxpayer during the taxable year. ,\n**(2)**\nby redesignating subsections (c), (d), and (e) as subsections (e), (f), and (g), respectively,\n**(3)**\nby inserting after subsection (b) the following new subsections:\n(c) Qualified semiconductor design expenditures (1) In general For purposes of subsection (a)(2), the term qualified semiconductor design expenditures means the sum of the following amounts which are paid or incurred by the taxpayer during the taxable year in carrying on any trade or business of the taxpayer for\u2014 (A) in-house semiconductor design expenses for semiconductor design conducted in the United States, and (B) contract design expenses for semiconductor design conducted in the United States. (2) In-house semiconductor design expenses (A) In general The term in-house semiconductor design expenses means\u2014 (i) any wages paid or incurred to an employee for qualified services performed by such employee, (ii) any amount paid or incurred for supplies used in the conduct of qualified semiconductor design, and (iii) under regulations prescribed by the Secretary, any amount paid or incurred to another person for the right to use computers in the conduct of qualified semiconductor design. Clause (iii) shall not apply to any amount to the extent that the taxpayer (or any person with whom the taxpayer must aggregate expenditures under paragraph (7) receives or accrues any amount from any other person for the right to use substantially identical personal property. (B) Qualified services The term qualified services means services consisting of\u2014 (i) engaging in qualified semiconductor design, or (ii) engaging in the direct supervision or direct support of design activities which constitute qualified semiconductor design. If substantially all of the services performed by an individual for the taxpayer during the taxable year consists of services meeting the requirements of clause (i) or (ii), the term \u201cqualified services\u201d means all of the services performed by such individual for the taxpayer during the taxable year. (C) Supplies The term supplies has the meaning given such term in section 41(b)(2)(C). (D) Wages The term wages has the meaning given such term in section 41(b)(2)(D). (3) Contract design expenses (A) In general The term contract design expenses means 100 percent of any amount paid or incurred by the taxpayer to any person (other than an employee of the taxpayer) for qualified semiconductor design. (B) Prepaid amounts If any contract design expenses paid or incurred during any taxable year are attributable to qualified semiconductor research to be conducted after the close of such taxable year, such amount shall be treated as paid or incurred during the period during which the qualified semiconductor design is conducted. (4) Trade or business requirement disregarded for in-house design expenses of certain startup ventures In the case of in-house semiconductor design expenses, a taxpayer shall be treated as meeting the trade or business requirement of paragraph (1) if, at the time such in-house semiconductor design expenses are paid or incurred, the principal purpose of the taxpayer in making such expenditures is to use the results of the design in the active conduct of a future trade or business\u2014 (A) of the taxpayer, or (B) of 1 or more persons who with the taxpayer are treated as single taxpayer under paragraph (7). (5) Qualified semiconductor design (A) In general The term qualified semiconductor design \u2014 (i) means the development (or direction of the development) of product design, design specifications, trade secrets, technology, or other intellectual property for the purpose of semiconductor manufacturing, substantially all of the activities of which constitute elements of a process of experimentation for a purpose described in subparagraph (B)(i), and (ii) does not include any activity described in subparagraph (B)(ii). (B) Purposes for which research may qualify for credit For purposes of subparagraph (A)\u2014 (i) In general Semiconductor design shall be treated as conducted for a purpose described in this paragraph if it relates to\u2014 (I) a new or improved function, (II) performance, or (III) reliability or quality. (ii) Certain purposes not qualified Semiconductor design shall in no event be treated as conducted for a purpose described in this paragraph if it is conducted for purposes of\u2014 (I) style, taste, cosmetic, or other design factors unrelated to a purpose described in clause (i), (II) design after the commencement of commercial production of the semiconductor, unless such design is related to firmware, software, or manufacturing process activities that would otherwise meet the requirements of clause (i), (III) duplication of an existing semiconductor product (in whole or in part) from a physical examination of the semiconductor itself or from plans, blueprints, detailed specifications, or publicly available information with respect to such semiconductor, or (IV) surveys or studies related to\u2014 (aa) efficiency, (bb) management function or techniques, (cc) market research, testing, or development, including advertising and promotions, (dd) routine data collection, or (ee) routine or ordinary testing or inspection for quality control. (6) United States For purposes of this subsection, the term United States includes the possessions of the United States. (7) Aggregation of expenditures For purposes of this subsection, in determining the amount of qualified semiconductor design expenditures, rules similar to the rules of section 41(f)(1) shall apply. (d) Coordination with credit for increasing research expenditures Any qualified semiconductor design expenditures for which a credit is allowed under this section shall not be taken into account for purposes of determining the credit allowable under section 41 for such taxable year. , and\n**(4)**\nby amending subsection (g) (as so redesignated) to read as follows:, by inserting or qualified semiconductor design expenditures paid or incurred after December 31, 2026 before the period.\n(g) Termination of credit The credit allowed under this section shall not apply to\u2014 (1) property the construction of which begins after December 31, 2036, or (2) qualified semiconductor design expenditures paid or incurred after December 31, 2036. .\n##### (b) Conforming amendment\nSection 56A(c)(9) of the Internal Revenue Code of 1986 is amended by striking 48D(d) and inserting 48D(f) .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act.",
      "versionDate": "2025-01-28",
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
        "name": "Taxation",
        "updateDate": "2025-04-07T16:27:40Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr802ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to add qualified semiconductor design expenditures to the advanced manufacturing investment credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T06:03:38Z"
    },
    {
      "title": "STAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Semiconductor Technology Advancement and Research Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:53:20Z"
    }
  ]
}
```
