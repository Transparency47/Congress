# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1296?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1296
- Title: Expanding Child Care Access Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1296
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-03-31T13:59:47Z
- Update date including text: 2026-03-31T13:59:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1296",
    "number": "1296",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001136",
        "district": "3",
        "firstName": "Herbert",
        "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
        "lastName": "Conaway",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Expanding Child Care Access Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T13:59:47Z",
    "updateDateIncludingText": "2026-03-31T13:59:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:02:40Z",
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
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "DC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-13",
      "state": "WA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CT"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "GA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "LA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MI"
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
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "OH"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NJ"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1296ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1296\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Conaway (for himself, Mrs. Foushee , Ms. Barrag\u00e1n , Ms. S\u00e1nchez , Ms. Pressley , Ms. Chu , Ms. Titus , Ms. Norton , Ms. Ross , Ms. Brownley , Mr. Takano , Mr. Frost , Mr. Casten , Mrs. Watson Coleman , Mrs. Ramirez , Ms. Perez , Ms. Garcia of Texas , Mr. Carson , Mr. Carbajal , Mr. Garcia of California , Mrs. Hayes , Mr. Peters , Ms. Tokuda , Mr. Johnson of Georgia , Ms. Bynum , Ms. McDonald Rivet , Ms. Salinas , Mr. Ruiz , Mrs. McIver , and Mrs. Cherfilus-McCormick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a refundable credit for qualified child care startup expenses.\n#### 1. Short title\nThis Act may be cited as the Expanding Child Care Access Act of 2025 .\n#### 2. Licensed family child care credit\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Licensed family child care credit (a) In general In the case of a qualified taxpayer, there shall be allowed as a credit against the tax imposed by this subtitle for any taxable year an amount equal to so much of the qualified child care startup expenses of the taxpayer for such taxable year or for the preceding taxable year as do not exceed $5,000. (b) Qualified taxpayer For purposes of this section, the term qualified taxpayer means, with respect to a taxable year, a taxpayer that operates a qualified family child care provider. (c) Qualified family child care provider For purposes of this section, the term qualified family child care provider means a family child care provider that, with respect to a taxable year\u2014 (1) provides child care services for compensation that, as of the last day of such taxable year, is licensed or registered under State law and satisfies State and local requirements applicable to the child care services it provides, (2) primarily provides child care at the taxpayer\u2019s primary residence, and (3) provided child care services to not less than 2 children (excluding children of such taxpayer) for a significant portion of such taxable year. (d) Qualified child care startup expenses For purposes of this section, the term qualified child care startup expenses means amounts paid or incurred for any of the following in order to establish and operate a qualified family child care provider: (1) Child care licensing fees. (2) Child care supplies including diapers, food, toys, and learning materials. (3) Liability insurance. (4) Fencing and installation of such fencing. (5) Outdoor playground equipment and installation of such equipment. (6) Furniture necessary to provide child care. (7) Salary of an employee other than the taxpayer. (8) Printer and computers. (9) Professional training required as a condition of State licensure or registration. (10) Remediation or renovation of the taxpayer\u2019s primary residence required as a condition of State licensure or registration. (e) Limitations No credit shall be allowed under subsection (a) to any taxpayer to whom a credit was allowed under such subsection in any other taxable year. (f) Denial of double benefit No credit shall be allowed under subsection (a) for any expense for which a deduction or credit is allowed under any other provision of this chapter. (g) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations relating to such information reporting and coordination with state and local licensing or registration entities as the Secretary determines appropriate. (h) Sunset No credit shall be allowed under subsection (a) for any taxable year beginning after the date that is 7 years after the date of the enactment of this section. .\n##### (b) Conforming amendment\nSection 1324(b)(2) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n##### (c) Clerical amendment\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Licensed family child care credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act.",
      "versionDate": "2025-02-13",
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
        "updateDate": "2025-05-06T15:49:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1296",
          "measure-number": "1296",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1296v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expanding Child Care Access Act of 2025</strong></p><p>This bill establishes a temporary (for seven years) refundable tax credit for certain expenses incurred to establish and operate a qualified family child care provider. (Conditions and limitations apply.)</p><p>Under\u00a0the bill, <em>a qualified family child care provider</em> is a child care provider that \u00a0</p><ul><li>provides child care services at the taxpayer's primary residence for at least two children (other than the children of such taxpayer) for a significant portion of the tax year,</li><li>receives compensation for such child care services, and</li><li>is licensed or registered to provide such child care services by the state in which such services are provided.</li></ul><p> The bill allows a taxpayer that operates a qualified family child care provider to claim a tax credit of up to $5,000 for</p><ul><li>child care licensing fees;</li><li>child care supplies (e.g., diapers, food, toys, and learning materials);</li><li>liability insurance;</li><li>fencing (including installation costs);</li><li>outdoor playground equipment (including installation costs);</li><li>furniture necessary to provide child care;</li><li>the salary of an employee (other than the taxpayer);</li><li>printers and computers;</li><li>professional training required by the state for licensing or registration; and</li><li>remediation or renovation of a primary residence to meet state licensing or registration requirements.</li></ul><p>The tax credit may only be claimed once and may not be claimed for expenses for which another tax deduction or tax credit is allowed.</p><p>Finally, the bill requires the Internal Revenue Service to issue guidance on the tax credit, including guidance related to information reporting requirements.</p>"
        },
        "title": "Expanding Child Care Access Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1296.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Child Care Access Act of 2025</strong></p><p>This bill establishes a temporary (for seven years) refundable tax credit for certain expenses incurred to establish and operate a qualified family child care provider. (Conditions and limitations apply.)</p><p>Under\u00a0the bill, <em>a qualified family child care provider</em> is a child care provider that \u00a0</p><ul><li>provides child care services at the taxpayer's primary residence for at least two children (other than the children of such taxpayer) for a significant portion of the tax year,</li><li>receives compensation for such child care services, and</li><li>is licensed or registered to provide such child care services by the state in which such services are provided.</li></ul><p> The bill allows a taxpayer that operates a qualified family child care provider to claim a tax credit of up to $5,000 for</p><ul><li>child care licensing fees;</li><li>child care supplies (e.g., diapers, food, toys, and learning materials);</li><li>liability insurance;</li><li>fencing (including installation costs);</li><li>outdoor playground equipment (including installation costs);</li><li>furniture necessary to provide child care;</li><li>the salary of an employee (other than the taxpayer);</li><li>printers and computers;</li><li>professional training required by the state for licensing or registration; and</li><li>remediation or renovation of a primary residence to meet state licensing or registration requirements.</li></ul><p>The tax credit may only be claimed once and may not be claimed for expenses for which another tax deduction or tax credit is allowed.</p><p>Finally, the bill requires the Internal Revenue Service to issue guidance on the tax credit, including guidance related to information reporting requirements.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr1296"
    },
    "title": "Expanding Child Care Access Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanding Child Care Access Act of 2025</strong></p><p>This bill establishes a temporary (for seven years) refundable tax credit for certain expenses incurred to establish and operate a qualified family child care provider. (Conditions and limitations apply.)</p><p>Under\u00a0the bill, <em>a qualified family child care provider</em> is a child care provider that \u00a0</p><ul><li>provides child care services at the taxpayer's primary residence for at least two children (other than the children of such taxpayer) for a significant portion of the tax year,</li><li>receives compensation for such child care services, and</li><li>is licensed or registered to provide such child care services by the state in which such services are provided.</li></ul><p> The bill allows a taxpayer that operates a qualified family child care provider to claim a tax credit of up to $5,000 for</p><ul><li>child care licensing fees;</li><li>child care supplies (e.g., diapers, food, toys, and learning materials);</li><li>liability insurance;</li><li>fencing (including installation costs);</li><li>outdoor playground equipment (including installation costs);</li><li>furniture necessary to provide child care;</li><li>the salary of an employee (other than the taxpayer);</li><li>printers and computers;</li><li>professional training required by the state for licensing or registration; and</li><li>remediation or renovation of a primary residence to meet state licensing or registration requirements.</li></ul><p>The tax credit may only be claimed once and may not be claimed for expenses for which another tax deduction or tax credit is allowed.</p><p>Finally, the bill requires the Internal Revenue Service to issue guidance on the tax credit, including guidance related to information reporting requirements.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr1296"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1296ih.xml"
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
      "title": "Expanding Child Care Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Child Care Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a refundable credit for qualified child care startup expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:36Z"
    }
  ]
}
```
