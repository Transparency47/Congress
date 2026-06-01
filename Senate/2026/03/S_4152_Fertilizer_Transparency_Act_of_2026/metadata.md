# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4152?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4152
- Title: Fertilizer Transparency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4152
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-04-23T11:03:26Z
- Update date including text: 2026-04-23T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1369-1370)
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1369-1370)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4152",
    "number": "4152",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Fertilizer Transparency Act of 2026",
    "type": "S",
    "updateDate": "2026-04-23T11:03:26Z",
    "updateDateIncludingText": "2026-04-23T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1369-1370)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-19T20:37:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MN"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "IA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "WI"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "NC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4152is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4152\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Mr. Thune (for himself, Ms. Klobuchar , Mr. Grassley , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to establish a mandatory price reporting program for fertilizer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fertilizer Transparency Act of 2026 .\n#### 2. Fertilizer mandatory reporting\nSubtitle A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1621 et seq. ) is amended by adding at the end the following:\n210B. Fertilizer mandatory reporting (a) Definitions In this section: (1) Affiliate The term affiliate means, with respect to a manufacturer or wholesaler (excluding a cooperative), a person that directly or indirectly owns, controls, or holds, with voting power, not less than 5 percent of the outstanding voting securities of the manufacturer or wholesaler (excluding a cooperative). (2) Cooperative (A) In general The term cooperative means\u2014 (i) an association of agricultural producers acting pursuant to\u2014 (I) the Act entitled An Act to authorize association of producers of agricultural products (commonly known as the Capper-Volstead Act ) ( 7 U.S.C. 291 et seq. ); (II) the Agricultural Adjustment Act ( 7 U.S.C. 601 et seq. ), reenacted with amendments by the Agricultural Marketing Agreement Act of 1937; or (III) the Act of July 2, 1926 (commonly known as the Cooperative Marketing Act ) ( 7 U.S.C. 451 et seq. ); (ii) a farmers' cooperative organization described in subsection (b)(1) of section 521 of the Internal Revenue Code of 1986 and exempt from taxation under subsection (a) of that section; and (iii) an association of agricultural producers otherwise operating on a cooperative basis for the benefit of its members. (B) Inclusions The term cooperative includes any entity not less than 25 percent of which is owned by a cooperative, as defined in subparagraph (A). (3) Marketed The term marketed means the sale or other disposition in commerce of\u2014 (A) nitrogen, phosphorous, or potassium for use as fertilizer; or (B) a fertilizer product. (4) Retailer The term retailer means a person or entity that primarily sells fertilizer products at retail. (5) Secretary The term Secretary means the Secretary of Agriculture. (6) Wholesaler The term wholesaler means any person or entity, not including a cooperative, engaged in the business of buying and selling fertilizer or fertilizer products for resale or distribution. (b) Establishment The Secretary shall establish a program of fertilizer and fertilizer product price information reporting that will\u2014 (1) provide timely, accurate, and reliable market information that can be readily understood by farmers and market participants; (2) facilitate more informed marketing decisions; and (3) promote competition in the fertilizer and fertilizer products industry. (c) General reporting provisions applicable to manufacturers, wholesalers, and the Secretary Whenever the prices or quantities of fertilizer or fertilizer products are required to be reported or published under this section, the prices or quantities shall be categorized so as to clearly delineate\u2014 (1) the prices or quantities, as applicable, of the fertilizer or fertilizer product marketed in the United States by a domestic manufacturer or wholesaler or an affiliate of a domestic manufacturer or wholesaler; and (2) the prices or quantities, as applicable, of the fertilizer or fertilizer product marketed in the United States by a foreign manufacturer or wholesaler or an affiliate of a foreign manufacturer or wholesaler. (d) Weekly reporting (1) Nitrogen, phosphorous, and potassium The corporate officers or officially designated representatives of each manufacturer or wholesaler of nitrogen, phosphorous, or potassium for use as fertilizer shall report to the Secretary at least weekly\u2014 (A) the prices, as marketed, for nitrogen, phosphorous, or potassium, as applicable; and (B) the quantities of nitrogen, phosphorous, or potassium, as applicable, manufactured and marketed, as applicable. (2) Fertilizer products The corporate officers or officially designated representatives of each manufacturer or wholesaler of a fertilizer product shall report to the Secretary at least weekly\u2014 (A) the prices for the fertilizer product; and (B) the quantity of the fertilizer product manufactured or marketed, as applicable. (3) Mandatory reporting exemption for cooperatives and non-manufacturer retailers; voluntary reporting The Secretary shall\u2014 (A) exempt all cooperatives and retailers (except for retailers that are also manufacturers) from any mandatory price reporting under this section; and (B) provide a mechanism for cooperatives and retailers to voluntarily and confidentially report the prices and quantities described in subparagraphs (A) and (B) of paragraphs (1) and (2)\u2014 (i) directly to the Secretary; or (ii) through the program established under subsection (e). (4) Publication The Secretary shall make the information reported to the Secretary under this subsection available to the public\u2014 (A) not less frequently than weekly; and (B) in a manner that ensures the information is published\u2014 (i) on a national basis; and (ii) on a regional or statewide basis, as the Secretary determines to be appropriate. (5) Competitive effects analysis The Secretary may conduct a competitive effects analysis of the information reported to the Secretary under this subsection. (e) Fertilizer retail survey (1) In general The Secretary shall establish a program within Market News of the Agricultural Marketing Service\u2014 (A) to conduct not less frequently than weekly surveys of retail fertilizer prices; (B) to obtain commercially available estimates of the retail prices described in subparagraph (A); and (C) to provide State or regional estimates or benchmarks and formulas to allow estimation of local prices. (2) Maintenance of existing activities The program established under paragraph (1) shall supplement, and not supplant, existing input price collection activities of the Secretary. (f) Summary of data (1) In general The Secretary shall, directly or through 1 or more cooperative agreements with 1 or more affiliated agricultural research programs, not less frequently than weekly summarize and make available on a dashboard or other resource easily accessible to farmers and market participants\u2014 (A) the information reported to the Secretary under subsection (d); and (B) the retail survey prices and commercially available estimates obtained under subsection (e). (2) Protection of confidentiality In carrying out paragraph (1), the Secretary shall aggregate the information and data in a manner that prevents confidential business information and the identity of persons, including parties to a contract, from being disclosed publicly. (3) Disclosure by Federal Government employees (A) In general Subject to subparagraph (B), no officer, employee, or agent of the United States shall, without the consent of the manufacturer, wholesaler, or other person concerned, divulge or make known in any manner any facts or information regarding the business of the manufacturer, wholesaler, or other person that was acquired through reporting required under subsection (d). (B) Exception Information obtained by the Secretary under subsection (d) may be disclosed\u2014 (i) to agents or employees of the Department of Agriculture in the course of their official duties under this subtitle; (ii) as directed by the Secretary or the Attorney General, for enforcement purposes; or (iii) by a court of competent jurisdiction. (C) Disclosure under freedom of information act Notwithstanding any other provision of law, no facts or information obtained under this subtitle shall be disclosed in accordance with section 552 of title 5, United States Code. (g) Review Not less frequently than once every 2 years, the Secretary shall review the information required to be reported to the Secretary by manufacturers and wholesalers under this section. (h) Outdated information If the Secretary determines under a review under subsection (g) that information required to be reported under this section no longer accurately reflects the methods by which nitrogen, phosphorous, and potassium for use as fertilizer or fertilizer products are valued and priced by manufacturers and wholesalers, the Secretary shall, after public notice and an opportunity for comment, promulgate regulations to specify additional information that shall be reported under this section. (i) Application of antitrust laws (1) In general Nothing in this section modifies, impairs, or supersedes the operation of any of the antitrust laws. (2) Definition of antitrust laws In this subsection, the term antitrust laws \u2014 (A) has the meaning given the term in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ); and (B) includes section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to the extent that such section applies to unfair methods of competition. .",
      "versionDate": "2026-03-19",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-03-26",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "8104",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fertilizer Transparency Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-30T22:27:42Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4152is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2026-04-23T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fertilizer Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-27T02:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Marketing Act of 1946 to establish a mandatory price reporting program for fertilizer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T02:48:31Z"
    }
  ]
}
```
