# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8374?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8374
- Title: Equal Treatment for Farmers Act
- Congress: 119
- Bill type: HR
- Bill number: 8374
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-20T08:07:02Z
- Update date including text: 2026-05-20T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8374",
    "number": "8374",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001102",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Harris, Mark [R-NC-8]",
        "lastName": "Harris",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Equal Treatment for Farmers Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:02Z",
    "updateDateIncludingText": "2026-05-20T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MD"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "CO"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "WI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NC"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "GA"
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
      "sponsorshipDate": "2026-04-20",
      "state": "IL"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "PA"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "GA"
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
      "sponsorshipDate": "2026-04-20",
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
      "sponsorshipDate": "2026-04-20",
      "state": "GA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "LA"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sponsorshipDate": "2026-04-20",
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
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "AL"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "WI"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "VA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NE"
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
      "sponsorshipDate": "2026-04-28",
      "state": "IN"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NC"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8374ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8374\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Harris of North Carolina (for himself, Mr. Harris of Maryland , Ms. Boebert , Mr. Wied , Mr. Harrigan , Mr. Fine , Mr. Brecheen , Mr. Clyde , Mrs. Miller of Illinois , Mr. Perry , Mr. Ogles , Mr. Steube , Mr. Collins , Mr. Nehls , Mr. Carter of Georgia , Ms. Letlow , Mr. Burchett , Mr. Self , Mr. Roy , Mr. Norman , Mr. Moore of Alabama , Mr. Van Orden , Mr. Cline , and Mr. Smith of Nebraska ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo strike references to socially disadvantaged farmers and ranchers in Federal law, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Equal Treatment for Farmers Act .\n#### 2. Striking references to socially disadvantaged farmers and ranchers in Federal law\n##### (a)\nSection 524(a)(3) of the Federal Crop Insurance Act ( 7 U.S.C. 1524(a)(3) ) is amended\u2014\n**(1)**\nby striking subparagraph (C); and\n**(2)**\nby redesignating subparagraphs (D) through (F) as subparagraphs (C) through (E), respectively.\n##### (b)\nSection 210A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraph (11); and\n**(B)**\nby redesignating paragraphs (12) and (13) as paragraphs (11) and (12), respectively;\n**(2)**\nin subsection (d)(5)(C)(i)\u2014\n**(A)**\nby striking subclause (II); and\n**(B)**\nby redesignating subclauses (III) and (IV) as subclauses (II) and (III), respectively; and\n**(3)**\nin subsection (i)(3)(A)(ii)(II)\u2014\n**(A)**\nin the subclause heading, by striking Beginning, veteran, and socially disadvantaged and inserting Beginning and veteran ; and\n**(B)**\nby striking beginning, veteran, and socially disadvantaged and inserting beginning and veteran .\n##### (c)\nThe Consolidated Farm and Rural Development Act ( 7 U.S.C. 1921 et seq. ) is amended\u2014\n**(1)**\nin section 304 ( 7 U.S.C. 1924 )\u2014\n**(A)**\nin subsection (d)(1), by striking and socially disadvantaged farmers or ranchers ; and\n**(B)**\nin subsection (e)(2), by striking socially disadvantaged farmer or rancher or a ;\n**(2)**\nin section 310B(e) ( 7 U.S.C. 1932(e) )\u2014\n**(A)**\nby striking paragraph (11); and\n**(B)**\nby redesignating paragraphs (12) and (13) as paragraphs (11) and (12), respectively;\n**(3)**\nin section 310E ( 7 U.S.C. 1935 )\u2014\n**(A)**\nin subsection (d)(4)\u2014\n**(i)**\nin subparagraph (A), by adding or at the end;\n**(ii)**\nby striking subparagraph (B);\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B); and\n**(iv)**\nin subparagraph (B), as so redesignated, by striking ; and at the end; and\n**(B)**\nin subsection (e)\u2014\n**(i)**\nin paragraph (1), by adding and at the end;\n**(ii)**\nby striking paragraph (2); and\n**(iii)**\nby redesignating paragraph (3) as paragraph (2);\n**(4)**\nin section 310F ( 7 U.S.C. 1936 )\u2014\n**(A)**\nin the section heading, by striking and socially disadvantaged farmer or rancher ;\n**(B)**\nin subsection (a), by striking or socially disadvantaged farmer or rancher (as defined in section 355(e)(2)) ;\n**(C)**\nin subsection (b)(1), by striking or socially disadvantaged farmer or rancher ;\n**(D)**\nin subsection (c)(1), by striking or socially disadvantaged farmer or rancher ; and\n**(E)**\nin subsection (f), by striking and Socially Disadvantaged Farmer or Rancher each place it appears;\n**(5)**\nin section 310I ( 7 U.S.C. 1936c )\u2014\n**(A)**\nin subsection (b)(2), by striking socially disadvantaged farmers and ranchers (as defined in subsection (a) of section 2501 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279 )) or ; and\n**(B)**\nby amending subsection (d) to read as follows:\n(d) Preference In making loans under subsection (a), the Secretary shall give preference to eligible entities in States that have adopted a statute consisting of an enactment or adoption of the Uniform Partition of Heirs Property Act, as approved and recommended for enactment in all States by the National Conference of Commissioners on Uniform State Laws in 2010, that relend to owners of heirs property (as defined in that Act). ;\n**(6)**\nin section 333B(c)(3)(A) ( 7 U.S.C. 1983b(c)(3)(A) ), by striking , including, as appropriate, socially disadvantaged farmers or ranchers (as defined in section 355(e)(2)) ;\n**(7)**\nin section 352(c) ( 7 U.S.C. 2000(c) ), by amending paragraph (4) to read as follows:\n(4) The period of occupancy allowed the prior owner of homestead property under this section shall be the period requested in writing by the prior owner, except that such period shall not exceed 5 years. ; and\n**(8)**\nby striking section 355 ( 7 U.S.C. 2003 ).\n##### (d)\nSection 5413 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2008x ) is amended\u2014\n**(1)**\nin subsection (b)(1)(C), by striking and socially disadvantaged ; and\n**(2)**\nin subsection (c)(1)(B), by striking and socially disadvantaged .\n##### (e)\nSection 2501 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraphs (5) and (6); and\n**(B)**\nby redesignating paragraph (7) as paragraph (5);\n**(2)**\nin subsection (b), by striking socially disadvantaged farmers and ranchers, veteran farmers and ranchers, and inserting veteran farmers and ranchers ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin the subsection heading, by striking socially disadvantaged and ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i), by striking socially disadvantaged farmers and ranchers and ; and\n**(II)**\nin clause (ii), by striking socially disadvantaged farmers or ranchers and ;\n**(ii)**\nby striking subparagraphs (E) and (F); and\n**(iii)**\nby redesignating subparagraph (G) as subparagraph (E);\n**(C)**\nin paragraph (3)(B)(i), by striking socially disadvantaged farmers or ranchers and ;\n**(D)**\nin paragraph (4)\u2014\n**(i)**\nin subparagraph (A), by striking socially disadvantaged farmers and ranchers and ;\n**(ii)**\nin subparagraph (D)\u2014\n**(I)**\nby striking clauses (iii) and (iv);\n**(II)**\nby redesignating clauses (v) through (vii) as clauses (iii) through (v), respectively;\n**(III)**\nin clause (iv), as so redesignated, by striking and socially disadvantaged farmers or ranchers ; and\n**(IV)**\nin clause (v), as so redesignated, by striking clause (vi) and inserting clause (iv) ; and\n**(iii)**\nin subparagraph (F), by striking socially disadvantaged farmers and ranchers or ; and\n**(E)**\nby striking paragraph (5);\n**(4)**\nin subsection (f)\u2014\n**(A)**\nby striking paragraph (2);\n**(B)**\nby redesignating paragraphs (3) through (7) as paragraphs (2) through (6), respectively; and\n**(C)**\nin paragraph (3), as so redesignated\u2014\n**(i)**\nin subparagraph (A), by adding or at the end;\n**(ii)**\nby striking subparagraph (B); and\n**(iii)**\nby redesignating subparagraph (C) as subparagraph (B);\n**(5)**\nin subsection (g)(2), by striking socially disadvantaged farmers and ranchers or ;\n**(6)**\nby striking subsections (h) and (j);\n**(7)**\nby redesignating subsections (i), (k), and (l) as subsections (h), (i), and (j), respectively;\n**(8)**\nin subsection (i), as so redesignated\u2014\n**(A)**\nin paragraph (1)(A), by striking and members of socially disadvantaged groups ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking and members of socially disadvantaged groups ;\n**(ii)**\nin subparagraph (B), by adding and at the end;\n**(iii)**\nby striking subparagraphs (C) and (E);\n**(iv)**\nby redesignating subparagraph (D) as subparagraph (C); and\n**(v)**\nin subparagraph (C), as so redesignated, by striking ; and and inserting a period; and\n**(9)**\nin subsection (j)(4)(A), as redesignated by paragraph (7)\u2014\n**(A)**\nin clause (i), by adding and at the end;\n**(B)**\nby striking clause (ii); and\n**(C)**\nby redesignating clause (iii) as clause (ii).\n##### (f)\nThe Federal Crop Insurance Reform and Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6901 et seq. ) is amended\u2014\n**(1)**\nin section 226B ( 7 U.S.C. 6934 )\u2014\n**(A)**\nin subsection (a), by striking paragraph (3);\n**(B)**\nin subsection (b)(1)(B)\u2014\n**(i)**\nby striking clause (iii); and\n**(ii)**\nby redesignating clauses (iv) and (v) as clauses (iii) and (iv), respectively;\n**(C)**\nin subsection (c)\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking veteran farmers and ranchers, and socially disadvantaged farmers or ranchers and inserting and veteran farmers and ranchers ;\n**(ii)**\nin paragraph (1), by striking socially disadvantaged, ; and\n**(iii)**\nin paragraph (5), by striking veteran farmers or ranchers, and socially disadvantaged farmers or ranchers and inserting and veteran farmers or ranchers ;\n**(D)**\nby striking subsection (d); and\n**(E)**\nby redesignating subsections (e) and (f) as subsections (d) and (e), respectively; and\n**(2)**\nby striking section 305 ( 7 U.S.C. 2279a ).\n##### (g)\nSection 201 of division HH of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ; 136 Stat. 5971) is repealed.\n##### (h)\nSection 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ) is amended\u2014\n**(1)**\nin subsection (k)(2), by striking , beginning, or socially disadvantaged and inserting or beginning ; and\n**(2)**\nin subsection (l)(3)\u2014\n**(A)**\nin the paragraph heading, by striking veteran, and socially disadvantaged and inserting and veteran ; and\n**(B)**\nby striking , beginning, and socially disadvantaged and inserting and beginning .\n##### (i)\nSection 405(c) of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7625(c) ) is amended by striking socially disadvantaged farmers, .\n##### (j)\nSection 9011 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8111 ) is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (9); and\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (2)(B), by amending clause (v) to read as follows:\n(v) the participation rate by beginning farmers or ranchers (as defined in accordance with section 343(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a) )); ; and\n**(B)**\nin paragraph (5), by amending subparagraph (B) to read as follows:\n(B) Amount of establishment payments The amount of an establishment payment under this subsection shall be not more than 50 percent of the costs of establishing an eligible perennial crop covered by the contract but not to exceed $500 per acre, including\u2014 (i) the cost of seeds and stock for perennials; (ii) the cost of planting the perennial crop, as determined by the Secretary; and (iii) in the case of nonindustrial private forestland, the costs of site preparation and tree planting. .\n##### (k)\nThe Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 8701 et seq. ) is amended\u2014\n**(1)**\nin section 1101(d) ( 7 U.S.C. 8711(d) ), by amending paragraph (2) to read as follows:\n(2) Exception Paragraph (1) shall not apply to a farm owned by a limited resource farmer or rancher, as defined by the Secretary. ; and\n**(2)**\nin section 1302(d) ( 7 U.S.C. 8752(d) ), by amending paragraph (2) to read as follows:\n(2) Exception Paragraph (1) shall not apply to a farm owned by a limited resource farmer or rancher, as defined by the Secretary. .\n##### (l)\nThe Agricultural Act of 2014 ( 7 U.S.C. 9001 et seq. ) is amended\u2014\n**(1)**\nin section 1114(d)(2) ( 7 U.S.C. 9014(d)(2) )\u2014\n**(A)**\nby striking subparagraph (A); and\n**(B)**\nby redesignating subparagraphs (B) through (D) as subparagraphs (A) through (C), respectively;\n**(2)**\nin section 1404(c)(4) ( 7 U.S.C. 9054(c)(4) ), by striking veteran, or socially disadvantaged and inserting or veteran ; and\n**(3)**\nin section 1501(a)(1)(A) ( 7 U.S.C. 9081(a)(1)(A) )\u2014\n**(A)**\nin clause (i), by adding or at the end;\n**(B)**\nby striking clause (ii); and\n**(C)**\nby redesignating clause (iii) as clause (ii).\n##### (m)\nSubclause (III) of section 8(b)(5)(B)(iii) of the Soil Conservation and Domestic Allotment Act ( 16 U.S.C. 590h(b)(5)(B)(iii) ) is amended to read as follows:\n(III) Nominations To be eligible for nomination and election to the applicable county, area, or local committee, as determined by the Secretary, an agricultural producer shall be located within the area under the jurisdiction of a county, area, or local committee, and participate or cooperate in programs administered within that area. .\n##### (n)\nSection 402A(b) of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2202a(b) ) is amended by striking , a socially disadvantaged farmer or rancher (as defined in subsection (a) of section 2501 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279 ), .\n##### (o)\nSection 623 of the Agricultural Credit Act of 1987 ( 7 U.S.C. 1985 note) is repealed.\n##### (p)\nThe Food Security Act of 1985 ( Public Law 99\u2013198 ; 99 Stat. 1504) is amended\u2014\n**(1)**\nin section 1201(a) ( 16 U.S.C. 3801(a) )\u2014\n**(A)**\nby striking paragraph (23); and\n**(B)**\nby redesignating paragraphs (24) through (27) as paragraphs (23) through (26), respectively;\n**(2)**\nin section 1231C(b)(3)(E) ( 16 U.S.C. 3831c(b)(3)(E) )\u2014\n**(A)**\nin the subparagraph heading, by striking socially disadvantaged, ;\n**(B)**\nin the matter preceding clause (i), by striking socially disadvantaged, ; and\n**(C)**\nin clause (i)(II), by striking socially disadvantaged, ;\n**(3)**\nin section 1240B(d)(4)(A) ( 16 U.S.C. 3839aa\u20132(d)(4)(A) ), by striking socially disadvantaged farmer or rancher, ;\n**(4)**\nin section 1241(h) ( 16 U.S.C. 3841(h) ), by amending paragraph (1) to read as follows:\n(1) Assistance (A) Fiscal years 2009 through 2018 Of the funds made available for each of fiscal years 2009 through 2018 to carry out the environmental quality incentives program and the acres made available for each of such fiscal years to carry out the conservation stewardship program, the Secretary shall use, to the maximum extent practicable, 5 percent to assist beginning farmers or ranchers. (B) Fiscal years 2019 through 2031 Of the funds made available for each of fiscal years 2019 through 2031 to carry out the environmental quality incentives program under subchapter A of chapter 4 of subtitle D and the conservation stewardship program under subchapter B of chapter 4 of subtitle D, the Secretary shall use, to the maximum extent practicable, 5 percent to assist beginning farmers or ranchers. ; and\n**(5)**\nin section 1271E(d) ( 16 U.S.C. 3871e(d) ), by striking socially disadvantaged farmers and ranchers, .\n#### 3. Prohibition on racial and gender preferences in USDA programs\nNotwithstanding any other law, no program of the Department of Agriculture may provide any preference, priority consideration, or enhanced benefits to any individual or entity on the basis of race or gender.",
      "versionDate": "2026-04-20",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-27T22:49:04Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8374ih.xml"
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
      "title": "Equal Treatment for Farmers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-25T04:38:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Equal Treatment for Farmers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-25T04:38:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strike references to socially disadvantaged farmers and ranchers in Federal law, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-25T04:33:36Z"
    }
  ]
}
```
