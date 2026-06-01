# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8104?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8104
- Title: Fertilizer Transparency Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8104
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-05T08:05:44Z
- Update date including text: 2026-05-05T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8104",
    "number": "8104",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Fertilizer Transparency Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-05T08:05:44Z",
    "updateDateIncludingText": "2026-05-05T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:00:20Z",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sponsorshipDate": "2026-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "KS"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NE"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8104ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8104\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Johnson of South Dakota (for himself, Ms. Craig , Mr. Finstad , Ms. Davids of Kansas , Mrs. Miller-Meeks , Ms. Budzinski , Mrs. Hinson , Mr. Riley of New York , Mr. Feenstra , Mr. Panetta , Mr. Nunn of Iowa , and Mr. Sorensen ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to establish a mandatory price reporting program for fertilizer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fertilizer Transparency Act of 2026 .\n#### 2. Fertilizer mandatory reporting\nSubtitle A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1621 et seq. ) is amended by adding at the end the following:\n210B. Fertilizer mandatory reporting (a) Definitions In this section: (1) Affiliate The term affiliate means, with respect to a manufacturer or wholesaler (excluding a cooperative), a person that directly or indirectly owns, controls, or holds, with voting power, not less than 5 percent of the outstanding voting securities of the manufacturer or wholesaler (excluding a cooperative). (2) Cooperative (A) In general The term cooperative means\u2014 (i) an association of agricultural producers acting pursuant to\u2014 (I) the Act entitled An Act to authorize association of producers of agricultural products (commonly known as the Capper-Volstead Act ) ( 7 U.S.C. 291 et seq. ); (II) the Agricultural Adjustment Act ( 7 U.S.C. 601 et seq. ), reenacted with amendments by the Agricultural Marketing Agreement Act of 1937; or (III) the Act of July 2, 1926 (commonly known as the Cooperative Marketing Act ) ( 7 U.S.C. 451 et seq. ); (ii) a farmers\u2019 cooperative organization described in subsection (b)(1) of section 521 of the Internal Revenue Code of 1986 and exempt from taxation under subsection (a) of that section; and (iii) an association of agricultural producers otherwise operating on a cooperative basis for the benefit of its members. (B) Inclusions The term cooperative includes any entity not less than 25 percent of which is owned by a cooperative, as defined in subparagraph (A). (3) Marketed The term marketed means the sale or other disposition in commerce of\u2014 (A) nitrogen, phosphorous, or potassium for use as fertilizer; or (B) a fertilizer product. (4) Retailer The term retailer means a person or entity that primarily sells fertilizer products at retail. (5) Secretary The term Secretary means the Secretary of Agriculture. (6) Wholesaler The term wholesaler means any person or entity, not including a cooperative, engaged in the business of buying and selling fertilizer or fertilizer products for resale or distribution. (b) Establishment The Secretary shall establish a program of fertilizer and fertilizer product price information reporting that will\u2014 (1) provide timely, accurate, and reliable market information that can be readily understood by farmers and market participants; (2) facilitate more informed marketing decisions; and (3) promote competition in the fertilizer and fertilizer products industry. (c) General reporting provisions applicable to manufacturers, wholesalers, and the Secretary Whenever the prices or quantities of fertilizer or fertilizer products are required to be reported or published under this section, the prices or quantities shall be categorized so as to clearly delineate\u2014 (1) the prices or quantities, as applicable, of the fertilizer or fertilizer product marketed in the United States by a domestic manufacturer or wholesaler or an affiliate of a domestic manufacturer or wholesaler; and (2) the prices or quantities, as applicable, of the fertilizer or fertilizer product marketed in the United States by a foreign manufacturer or wholesaler or an affiliate of a foreign manufacturer or wholesaler. (d) Weekly reporting (1) Nitrogen, phosphorous, and potassium The corporate officers or officially designated representatives of each manufacturer or wholesaler of nitrogen, phosphorous, or potassium for use as fertilizer shall report to the Secretary at least weekly\u2014 (A) the prices, as marketed, for nitrogen, phosphorous, or potassium, as applicable; and (B) the quantities of nitrogen, phosphorous, or potassium, as applicable, manufactured and marketed, as applicable. (2) Fertilizer products The corporate officers or officially designated representatives of each manufacturer or wholesaler of a fertilizer product shall report to the Secretary at least weekly\u2014 (A) the prices for the fertilizer product; and (B) the quantity of the fertilizer product manufactured or marketed, as applicable. (3) Mandatory reporting exemption for cooperatives and non-manufacturer retailers; voluntary reporting The Secretary shall\u2014 (A) exempt all cooperatives and retailers (except for retailers that are also manufacturers) from any mandatory price reporting under this section; and (B) provide a mechanism for cooperatives and retailers to voluntarily and confidentially report the prices and quantities described in subparagraphs (A) and (B) of paragraphs (1) and (2)\u2014 (i) directly to the Secretary; or (ii) through the program established under subsection (e). (4) Publication The Secretary shall make the information reported to the Secretary under this subsection available to the public\u2014 (A) not less frequently than weekly; and (B) in a manner that ensures the information is published\u2014 (i) on a national basis; and (ii) on a regional or statewide basis, as the Secretary determines to be appropriate. (5) Competitive effects analysis The Secretary may conduct a competitive effects analysis of the information reported to the Secretary under this subsection. (e) Fertilizer retail survey (1) In general The Secretary shall establish a program within Market News of the Agricultural Marketing Service\u2014 (A) to conduct not less frequently than weekly surveys of retail fertilizer prices; (B) to obtain commercially available estimates of the retail prices described in subparagraph (A); and (C) to provide State or regional estimates or benchmarks and formulas to allow estimation of local prices. (2) Maintenance of existing activities The program established under paragraph (1) shall supplement, and not supplant, existing input price collection activities of the Secretary. (f) Summary of data (1) In general The Secretary shall, directly or through 1 or more cooperative agreements with 1 or more affiliated agricultural research programs, not less frequently than weekly summarize and make available on a dashboard or other resource easily accessible to farmers and market participants\u2014 (A) the information reported to the Secretary under subsection (d); and (B) the retail survey prices and commercially available estimates obtained under subsection (e). (2) Protection of confidentiality In carrying out paragraph (1), the Secretary shall aggregate the information and data in a manner that prevents confidential business information and the identity of persons, including parties to a contract, from being disclosed publicly. (3) Disclosure by Federal Government employees (A) In general Subject to subparagraph (B), no officer, employee, or agent of the United States shall, without the consent of the manufacturer, wholesaler, or other person concerned, divulge or make known in any manner any facts or information regarding the business of the manufacturer, wholesaler, or other person that was acquired through reporting required under subsection (d). (B) Exception Information obtained by the Secretary under subsection (d) may be disclosed\u2014 (i) to agents or employees of the Department of Agriculture in the course of their official duties under this subtitle; (ii) as directed by the Secretary or the Attorney General, for enforcement purposes; or (iii) by a court of competent jurisdiction. (C) Disclosure under freedom of information act Notwithstanding any other provision of law, no facts or information obtained under this subtitle shall be disclosed in accordance with section 552 of title 5, United States Code. (g) Review Not less frequently than once every 2 years, the Secretary shall review the information required to be reported to the Secretary by manufacturers and wholesalers under this section. (h) Outdated information If the Secretary determines under a review under subsection (g) that information required to be reported under this section no longer accurately reflects the methods by which nitrogen, phosphorous, and potassium for use as fertilizer or fertilizer products are valued and priced by manufacturers and wholesalers, the Secretary shall, after public notice and an opportunity for comment, promulgate regulations to specify additional information that shall be reported under this section. (i) Application of antitrust laws (1) In general Nothing in this section modifies, impairs, or supersedes the operation of any of the antitrust laws. (2) Definition of antitrust laws In this subsection, the term antitrust laws \u2014 (A) has the meaning given the term in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ); and (B) includes section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that such section applies to unfair methods of competition. .",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-03-19",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1369-1370)"
      },
      "number": "4152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fertilizer Transparency Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-15T01:09:59Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8104ih.xml"
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
      "title": "Fertilizer Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T06:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fertilizer Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T06:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Marketing Act of 1946 to establish a mandatory price reporting program for fertilizer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T06:03:36Z"
    }
  ]
}
```
