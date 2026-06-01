# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1901?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1901
- Title: CHIPP Act
- Congress: 119
- Bill type: HR
- Bill number: 1901
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-04-15T08:05:40Z
- Update date including text: 2025-04-15T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1901",
    "number": "1901",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001300",
        "district": "44",
        "firstName": "Nanette",
        "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
        "lastName": "Barrag\u00e1n",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CHIPP Act",
    "type": "HR",
    "updateDate": "2025-04-15T08:05:40Z",
    "updateDateIncludingText": "2025-04-15T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:06:00Z",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "GA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "OR"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "TN"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-06",
      "state": "DC"
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
      "sponsorshipDate": "2025-03-06",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NV"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "VA"
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
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MD"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "AZ"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CT"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WI"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NM"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1901ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1901\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Ms. Barrag\u00e1n (for herself, Mr. Johnson of Georgia , Ms. Bonamici , Mr. Cohen , Ms. Castor of Florida , Ms. Schakowsky , Mr. Vargas , Ms. Norton , Ms. Scholten , Mrs. Watson Coleman , Ms. Titus , Mr. Mullin , Mr. Tonko , Mrs. Trahan , Ms. Strickland , Ms. Waters , Mr. Soto , Ms. McClellan , Mr. Morelle , Mr. Mfume , Ms. Ansari , Mrs. Cherfilus-McCormick , Mrs. Hayes , Mr. Espaillat , Mr. Pocan , and Mr. Vasquez ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXI of the Social Security Act to permanently extend the Children\u2019s Health Insurance Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Children\u2019s Health Insurance Program Permanency Act or the CHIPP Act .\n#### 2. Permanent extension of children\u2019s health insurance program\n##### (a) In general\nSection 2104(a)(28) of the Social Security Act ( 42 U.S.C. 1397dd(a)(28) ) is amended to read as follows:\n(28) for fiscal year 2029 and each subsequent year, such sums as are necessary to fund allotments to States under subsections (c) and (m). .\n##### (b) Allotments\n**(1) In general**\nSection 2104(m) of the Social Security Act ( 42 U.S.C. 1397dd(m) ) is amended\u2014\n**(A)**\nin paragraph (2)(B)(i), by striking , 2023, and 2029 and inserting and 2023 ;\n**(B)**\nin paragraph (5)\u2014\n**(i)**\nby striking for a fiscal year and inserting for a fiscal year before 2029 ; and\n**(ii)**\nby striking 2023, or 2029 and inserting or 2023 ;\n**(C)**\nin paragraph (7)\u2014\n**(i)**\nin subparagraph (A), by striking and ending with fiscal year 2029, ; and\n**(ii)**\nin the flush left matter at the end, by striking or fiscal year 2028 and inserting fiscal year 2028, or a subsequent even-numbered fiscal year ;\n**(D)**\nin paragraph (9)\u2014\n**(i)**\nby striking (10), or (11) and inserting or (10) ; and\n**(ii)**\nby striking 2023, or 2029, and inserting or 2023 ; and\n**(E)**\nby striking paragraph (11).\n**(2) Conforming amendment**\nSection 50101(b)(2) of the Bipartisan Budget Act of 2018 ( Public Law 115\u2013123 ) is repealed.\n#### 3. Permanent extensions of other programs and demonstration projects\n##### (a) Pediatric quality measures program\nSection 1139A(i)(1) of the Social Security Act (42 U.S.C. 1320b\u20139a(i)(1)) is amended\u2014\n**(1)**\nin subparagraph (D), by striking at the end and ;\n**(2)**\nin subparagraph (E), by striking the period at the end and insert a semicolon; and\n**(3)**\nby adding at the end the following new subparagraphs:\n(E) for fiscal year 2030, $15,000,000 for the purpose of carrying out this section (other than subsections (e), (f), and (g)); and (F) for a subsequent fiscal year, the amount appropriated under this paragraph for the previous fiscal year, increased by the percentage increase in the consumer price index for all urban consumers (all items; United States city average) over such previous fiscal year, for the purpose of carrying out this section (other than subsections (e), (f), and (g)). .\n##### (b) Express lane eligibility option\nSection 1902(e)(13) of the Social Security Act ( 42 U.S.C. 1396a(e)(13) ) is amended by striking subparagraph (I).\n##### (c) Assurance of affordability standard for children and families\n**(1) In general**\nSection 2105(d)(3) of the Social Security Act ( 42 U.S.C. 1397ee(d)(3) ) is amended\u2014\n**(A)**\nin the paragraph heading, by striking through September 30, 2029 ; and\n**(B)**\nin subparagraph (A), in the matter preceding clause (i)\u2014\n**(i)**\nby striking During the period that begins on the date of enactment of the Patient Protection and Affordable Care Act and ends on September 30, 2029 and inserting Beginning on the date of the enactment of the Patient Protection and Affordable Care Act ;\n**(ii)**\nby striking During the period that begins on October 1, 2019, and ends on September 30, 2029 and inserting Beginning on October 1, 2019 ; and\n**(iii)**\nby striking The preceding sentences shall not be construed as preventing a State during any such periods from and inserting The preceding sentences shall not be construed as preventing a State from .\n**(2) Conforming amendments**\nSection 1902(gg)(2) of the Social Security Act ( 42 U.S.C. 1396a(gg)(2) ) is amended\u2014\n**(A)**\nin the paragraph heading, by striking through September 30, 2029 ; and\n**(B)**\nby striking through September 30 and all that follows through ends on September 30, 2029 and inserting (but beginning on October 1, 2019,) .\n##### (d) Qualifying States option\nSection 2105(g)(4) of the Social Security Act ( 42 U.S.C. 1397ee(g)(4) ) is amended\u2014\n**(1)**\nin the paragraph heading, by striking for fiscal years 2009 through 2029 and inserting after fiscal year 2008 ; and\n**(2)**\nin subparagraph (A), by striking for any of fiscal years 2009 through 2029 and inserting for any fiscal year after fiscal year 2008 .\n##### (e) Outreach and enrollment program\nSection 2113 of the Social Security Act ( 42 U.S.C. 1397mm ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking during the period of fiscal years 2009 through 2029 and inserting , beginning with fiscal year 2009, ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking 10 percent of such amounts and inserting 10 percent of such amounts for the period or the fiscal year for which such amounts are appropriated ; and\n**(ii)**\nby striking during such period and inserting , during such period or such fiscal year, ; and\n**(C)**\nin paragraph (3), by striking For the period of fiscal years 2024 through 2029, an amount equal to 10 percent of such amounts and inserting Beginning with fiscal year 2024, an amount equal to 10 percent of such amounts for the period or the fiscal year for which such amounts are appropriated ; and\n**(2)**\nin subsection (g)\u2014\n**(A)**\nby striking and $40,000,000 and inserting $40,000,000 ; and\n**(B)**\nby inserting after and 2029 the following: , $12,000,000 for fiscal year 2030, and, for each fiscal year after fiscal year 2030, the amount appropriated under this subsection for the previous fiscal year, increased by the percentage increase in the consumer price index for all urban consumers (all items; United States city average) over such previous fiscal year .\n##### (f) Child enrollment contingency fund\nSection 2104(n) of the Social Security Act ( 42 U.S.C. 1397dd(n) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)(ii)\u2014\n**(i)**\nby striking and 2024 through 2028 and inserting beginning with fiscal year 2024 ; and\n**(ii)**\nby striking 2023, and 2029 and inserting , and 2023 ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking 2024 through 2028 and inserting beginning with fiscal year 2024 ; and\n**(ii)**\nby striking 2023, and 2029 and inserting , and 2023 ; and\n**(2)**\nin paragraph (3)(A)\u2014\n**(A)**\nby striking fiscal years 2024 through 2028 and inserting fiscal year 2024 or any subsequent fiscal year ; and\n**(B)**\nby striking 2023, or 2029 and inserting , or 2023 .\n#### 4. State option to increase children\u2019s eligibility for medicaid and chip\nSection 2110(b)(1)(B)(ii) of the Social Security Act ( 42 U.S.C. 1397jj(b)(1)(B)(ii) ) is amended\u2014\n**(1)**\nin subclause (II), by striking or at the end;\n**(2)**\nin subclause (III), by striking and at the end and inserting or ; and\n**(3)**\nby inserting after subclause (III) the following new subclause:\n(IV) at the option of the State, whose family income exceeds the maximum income level otherwise established for children under the State child health plan as of the date of the enactment of this subclause; and .",
      "versionDate": "2025-03-06",
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
        "name": "Health",
        "updateDate": "2025-03-23T11:07:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1901",
          "measure-number": "1901",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1901v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Children\u2019s Health Insurance Program Permanency Act or the CHIPP Act</b></p> <p>This bill permanently extends the Children's Health Insurance Program (CHIP) and related measures, programs, and authorities. </p> <p>Specifically, the bill permanently funds CHIP and related programs that support the development of child health quality measures and outreach and enrollment efforts. The bill also permanently authorizes the Medicaid and CHIP express lane eligibility option, which allows states to use information from designated programs (e.g., the Supplemental Nutrition Assistance Program) to streamline eligibility determinations for children. Additionally, under the bill, states may expand eligibility to children whose family income exceeds the otherwise applicable limits.</p>"
        },
        "title": "CHIPP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1901.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Children\u2019s Health Insurance Program Permanency Act or the CHIPP Act</b></p> <p>This bill permanently extends the Children's Health Insurance Program (CHIP) and related measures, programs, and authorities. </p> <p>Specifically, the bill permanently funds CHIP and related programs that support the development of child health quality measures and outreach and enrollment efforts. The bill also permanently authorizes the Medicaid and CHIP express lane eligibility option, which allows states to use information from designated programs (e.g., the Supplemental Nutrition Assistance Program) to streamline eligibility determinations for children. Additionally, under the bill, states may expand eligibility to children whose family income exceeds the otherwise applicable limits.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr1901"
    },
    "title": "CHIPP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Children\u2019s Health Insurance Program Permanency Act or the CHIPP Act</b></p> <p>This bill permanently extends the Children's Health Insurance Program (CHIP) and related measures, programs, and authorities. </p> <p>Specifically, the bill permanently funds CHIP and related programs that support the development of child health quality measures and outreach and enrollment efforts. The bill also permanently authorizes the Medicaid and CHIP express lane eligibility option, which allows states to use information from designated programs (e.g., the Supplemental Nutrition Assistance Program) to streamline eligibility determinations for children. Additionally, under the bill, states may expand eligibility to children whose family income exceeds the otherwise applicable limits.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr1901"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1901ih.xml"
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
      "title": "CHIPP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHIPP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Children\u2019s Health Insurance Program Permanency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXI of the Social Security Act to permanently extend the Children's Health Insurance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:24Z"
    }
  ]
}
```
