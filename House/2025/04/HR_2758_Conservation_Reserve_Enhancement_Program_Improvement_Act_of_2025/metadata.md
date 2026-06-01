# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2758?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2758
- Title: Conservation Reserve Enhancement Program Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2758
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-04-15T08:05:56Z
- Update date including text: 2026-04-15T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2758",
    "number": "2758",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B000825",
        "district": "4",
        "firstName": "Lauren",
        "fullName": "Rep. Boebert, Lauren [R-CO-4]",
        "lastName": "Boebert",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:56Z",
    "updateDateIncludingText": "2026-04-15T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:07:00Z",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "CO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "CO"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "KS"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2758ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2758\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Ms. Boebert (for herself and Mr. Evans of Colorado ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to modify the conservation reserve enhancement program.\n#### 1. Short title\nThis Act may be cited as the Conservation Reserve Enhancement Program Improvement Act of 2025 .\n#### 2. Conservation reserve enhancement program\n##### (a) In general\nSection 1231A of the Food Security Act of 1985 ( 16 U.S.C. 3831a ) is amended\u2014\n**(1)**\nin subsection (a)(4), in the matter preceding subparagraph (A), by inserting (other than an agreement described in subsection (e)) after this subchapter ;\n**(2)**\nin subsection (b)(2)(A)(vi), by inserting or other appropriate practices, such as dryland agricultural uses and grazing, after conservation practices ;\n**(3)**\nin subsection (c), by adding at the end the following:\n(5) Variable allocation An owner or operator may elect to determine the amounts of annual payments under this section allocated to each year of the agreement under subsection (b)(1). (6) Drought and water conservation agreements (A) Retirement of water rights In the case of an agreement described in subsection (e) that includes a permanent retirement of water rights, the payment rates for annual payments shall be equal to the irrigated acre payment rates determined by the Secretary. (B) Dryland agricultural uses (i) In general In the case of an agreement described in subsection (e) that permits dryland agricultural uses pursuant to paragraph (2) of that subsection, the payment rates for annual payments shall be equal to the difference between\u2014 (I) the irrigated acre payment rates determined by the Secretary; and (II) the dryland acre payment rates determined by the Secretary. (ii) Retroactive application In the case of an agreement covered by clause (i) entered into before the date of enactment of this paragraph under which the payment rate is lower than the payment rate that would be calculated for the agreement under that clause, the Secretary shall modify the agreement by calculating the payment rate in accordance with that clause. ; and\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking may\u2014 and inserting shall\u2014 ;\n**(B)**\nin paragraph (1), by inserting (including agricultural land on which a continuous crop or crop rotation is maintained) after agricultural land ;\n**(C)**\nin paragraph (2), by striking with the adoption of best management practices on and inserting in accordance with a conservation plan adopted with respect to ; and\n**(D)**\nin paragraph (3), by inserting subject to subsection (c)(6), before calculate .\n##### (b) Exemption from payment limitation\nSection 1234(g) of the Food Security Act of 1985 ( 16 U.S.C. 3834(g) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking paragraph (2) and inserting paragraphs (2) and (3) ; and\n**(2)**\nby adding at the end the following:\n(3) Conservation reserve enhancement program Paragraph (1) shall not apply to rental payments received under agreements entered into under section 1231A. .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1389",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
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
        "updateDate": "2025-05-07T13:14:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119hr2758",
          "measure-number": "2758",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-09",
          "originChamber": "HOUSE",
          "update-date": "2025-09-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2758v00",
            "update-date": "2025-09-17"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Conservation Reserve Enhancement Program Improvement Act of 2025</strong></p><p>This bill revises the Conservation Reserve Enhancement Program (CREP), which is a component of the Farm Service Agency's (FSA's) Conservation Reserve Program (CRP). CREP is a public-private partnership program which allows states, tribal governments, and nonprofit and private entities to partner with FSA to implement CRP practices. CRP is a land conservation program that provides an annual rental payment to farmers in exchange for removing environmentally sensitive land from agricultural production and planting species that will improve environmental health and quality.</p><p>The bill specifies that dryland agricultural uses and grazing are included as appropriate practices under CREP.</p><p>The bill also allows a land owner or operator to elect to determine the annual payment amount allocated for each year of a CREP agreement, instead of a fixed payment per year for the contract period.</p><p>For drought and water conservation agreements that include the permanent retirement of water rights, annual payment rates must be equal to the irrigated acre payment rates determined by the Department of Agriculture (USDA). In the case of an agreement that permits dryland agricultural uses, the annual payment rates must be equal to the difference between the irrigated acre payment rates and the dryland acre payment rates determined by USDA. The payment formula is retroactive for certain\u00a0existing drought and water conservation agreements.</p><p>Further, the bill exempts CREP payments from the $50,000 annual payment limitation under CRP.</p>"
        },
        "title": "Conservation Reserve Enhancement Program Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2758.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Conservation Reserve Enhancement Program Improvement Act of 2025</strong></p><p>This bill revises the Conservation Reserve Enhancement Program (CREP), which is a component of the Farm Service Agency's (FSA's) Conservation Reserve Program (CRP). CREP is a public-private partnership program which allows states, tribal governments, and nonprofit and private entities to partner with FSA to implement CRP practices. CRP is a land conservation program that provides an annual rental payment to farmers in exchange for removing environmentally sensitive land from agricultural production and planting species that will improve environmental health and quality.</p><p>The bill specifies that dryland agricultural uses and grazing are included as appropriate practices under CREP.</p><p>The bill also allows a land owner or operator to elect to determine the annual payment amount allocated for each year of a CREP agreement, instead of a fixed payment per year for the contract period.</p><p>For drought and water conservation agreements that include the permanent retirement of water rights, annual payment rates must be equal to the irrigated acre payment rates determined by the Department of Agriculture (USDA). In the case of an agreement that permits dryland agricultural uses, the annual payment rates must be equal to the difference between the irrigated acre payment rates and the dryland acre payment rates determined by USDA. The payment formula is retroactive for certain\u00a0existing drought and water conservation agreements.</p><p>Further, the bill exempts CREP payments from the $50,000 annual payment limitation under CRP.</p>",
      "updateDate": "2025-09-17",
      "versionCode": "id119hr2758"
    },
    "title": "Conservation Reserve Enhancement Program Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Conservation Reserve Enhancement Program Improvement Act of 2025</strong></p><p>This bill revises the Conservation Reserve Enhancement Program (CREP), which is a component of the Farm Service Agency's (FSA's) Conservation Reserve Program (CRP). CREP is a public-private partnership program which allows states, tribal governments, and nonprofit and private entities to partner with FSA to implement CRP practices. CRP is a land conservation program that provides an annual rental payment to farmers in exchange for removing environmentally sensitive land from agricultural production and planting species that will improve environmental health and quality.</p><p>The bill specifies that dryland agricultural uses and grazing are included as appropriate practices under CREP.</p><p>The bill also allows a land owner or operator to elect to determine the annual payment amount allocated for each year of a CREP agreement, instead of a fixed payment per year for the contract period.</p><p>For drought and water conservation agreements that include the permanent retirement of water rights, annual payment rates must be equal to the irrigated acre payment rates determined by the Department of Agriculture (USDA). In the case of an agreement that permits dryland agricultural uses, the annual payment rates must be equal to the difference between the irrigated acre payment rates and the dryland acre payment rates determined by USDA. The payment formula is retroactive for certain\u00a0existing drought and water conservation agreements.</p><p>Further, the bill exempts CREP payments from the $50,000 annual payment limitation under CRP.</p>",
      "updateDate": "2025-09-17",
      "versionCode": "id119hr2758"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2758ih.xml"
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
      "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-23T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to modify the conservation reserve enhancement program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T07:48:18Z"
    }
  ]
}
```
