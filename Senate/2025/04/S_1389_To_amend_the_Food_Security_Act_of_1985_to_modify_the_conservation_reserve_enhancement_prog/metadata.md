# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1389
- Title: Conservation Reserve Enhancement Program Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1389
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2025-12-05T21:58:35Z
- Update date including text: 2025-12-05T21:58:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1389",
    "number": "1389",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:58:35Z",
    "updateDateIncludingText": "2025-12-05T21:58:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T19:50:21Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CO"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "KS"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1389is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1389\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Marshall (for himself, Mr. Bennet , Mr. Moran , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food Security Act of 1985 to modify the conservation reserve enhancement program.\n#### 1. Short title\nThis Act may be cited as the Conservation Reserve Enhancement Program Improvement Act of 2025 .\n#### 2. Conservation reserve enhancement program\n##### (a) In general\nSection 1231A of the Food Security Act of 1985 ( 16 U.S.C. 3831a ) is amended\u2014\n**(1)**\nin subsection (a)(4), in the matter preceding subparagraph (A), by inserting (other than an agreement described in subsection (e)) after this subchapter ;\n**(2)**\nin subsection (b)(2)(A)(vi), by inserting or other appropriate practices, such as dryland agricultural uses and grazing, after conservation practices ;\n**(3)**\nin subsection (c), by adding at the end the following:\n(5) Variable allocation An owner or operator may elect to determine the amounts of annual payments under this section allocated to each year of the agreement under subsection (b)(1). (6) Drought and water conservation agreements (A) Retirement of water rights In the case of an agreement described in subsection (e) that includes a permanent retirement of water rights, the payment rates for annual payments shall be equal to the irrigated acre payment rates determined by the Secretary. (B) Dryland agricultural uses (i) In general In the case of an agreement described in subsection (e) that permits dryland agricultural uses pursuant to paragraph (2) of that subsection, the payment rates for annual payments shall be equal to the difference between\u2014 (I) the irrigated acre payment rates determined by the Secretary; and (II) the dryland acre payment rates determined by the Secretary. (ii) Retroactive application In the case of an agreement covered by clause (i) entered into before the date of enactment of this paragraph under which the payment rate is lower than the payment rate that would be calculated for the agreement under that clause, the Secretary shall modify the agreement by calculating the payment rate in accordance with that clause. ; and\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking may\u2014 and inserting shall\u2014 ;\n**(B)**\nin paragraph (1), by inserting (including agricultural land on which a continuous crop or crop rotation is maintained) after agricultural land ;\n**(C)**\nin paragraph (2), by striking with the adoption of best management practices on and inserting in accordance with a conservation plan adopted with respect to ; and\n**(D)**\nin paragraph (3), by inserting subject to subsection (c)(6), before calculate .\n##### (b) Exemption from payment limitation\nSection 1234(g) of the Food Security Act of 1985 ( 16 U.S.C. 3834(g) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking paragraph (2) and inserting paragraphs (2) and (3) ; and\n**(2)**\nby adding at the end the following:\n(3) Conservation reserve enhancement program Paragraph (1) shall not apply to rental payments received under agreements entered into under section 1231A. .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "2758",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
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
        "updateDate": "2025-05-07T13:20:39Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s1389",
          "measure-number": "1389",
          "measure-type": "s",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2025-09-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1389v00",
            "update-date": "2025-09-17"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Conservation Reserve Enhancement Program Improvement Act of 2025</strong></p><p>This bill revises the Conservation Reserve Enhancement Program (CREP), which is a component of the Farm Service Agency's (FSA's) Conservation Reserve Program (CRP). CREP is a public-private partnership program which allows states, tribal governments, and nonprofit and private entities to partner with FSA to implement CRP practices. CRP is a land conservation program that provides an annual rental payment to farmers in exchange for removing environmentally sensitive land from agricultural production and planting species that will improve environmental health and quality.</p><p>The bill specifies that dryland agricultural uses and grazing are included as appropriate practices under CREP.</p><p>The bill also allows a land owner or operator to elect to determine the annual payment amount allocated for each year of a CREP agreement, instead of a fixed payment per year for the contract period.</p><p>For drought and water conservation agreements that include the permanent retirement of water rights, annual payment rates must be equal to the irrigated acre payment rates determined by the Department of Agriculture (USDA). In the case of an agreement that permits dryland agricultural uses, the annual payment rates must be equal to the difference between the irrigated acre payment rates and the dryland acre payment rates determined by USDA. The payment formula is retroactive for certain\u00a0existing drought and water conservation agreements.</p><p>Further, the bill exempts CREP payments from the $50,000 annual payment limitation under CRP.</p>"
        },
        "title": "Conservation Reserve Enhancement Program Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1389.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Conservation Reserve Enhancement Program Improvement Act of 2025</strong></p><p>This bill revises the Conservation Reserve Enhancement Program (CREP), which is a component of the Farm Service Agency's (FSA's) Conservation Reserve Program (CRP). CREP is a public-private partnership program which allows states, tribal governments, and nonprofit and private entities to partner with FSA to implement CRP practices. CRP is a land conservation program that provides an annual rental payment to farmers in exchange for removing environmentally sensitive land from agricultural production and planting species that will improve environmental health and quality.</p><p>The bill specifies that dryland agricultural uses and grazing are included as appropriate practices under CREP.</p><p>The bill also allows a land owner or operator to elect to determine the annual payment amount allocated for each year of a CREP agreement, instead of a fixed payment per year for the contract period.</p><p>For drought and water conservation agreements that include the permanent retirement of water rights, annual payment rates must be equal to the irrigated acre payment rates determined by the Department of Agriculture (USDA). In the case of an agreement that permits dryland agricultural uses, the annual payment rates must be equal to the difference between the irrigated acre payment rates and the dryland acre payment rates determined by USDA. The payment formula is retroactive for certain\u00a0existing drought and water conservation agreements.</p><p>Further, the bill exempts CREP payments from the $50,000 annual payment limitation under CRP.</p>",
      "updateDate": "2025-09-17",
      "versionCode": "id119s1389"
    },
    "title": "Conservation Reserve Enhancement Program Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Conservation Reserve Enhancement Program Improvement Act of 2025</strong></p><p>This bill revises the Conservation Reserve Enhancement Program (CREP), which is a component of the Farm Service Agency's (FSA's) Conservation Reserve Program (CRP). CREP is a public-private partnership program which allows states, tribal governments, and nonprofit and private entities to partner with FSA to implement CRP practices. CRP is a land conservation program that provides an annual rental payment to farmers in exchange for removing environmentally sensitive land from agricultural production and planting species that will improve environmental health and quality.</p><p>The bill specifies that dryland agricultural uses and grazing are included as appropriate practices under CREP.</p><p>The bill also allows a land owner or operator to elect to determine the annual payment amount allocated for each year of a CREP agreement, instead of a fixed payment per year for the contract period.</p><p>For drought and water conservation agreements that include the permanent retirement of water rights, annual payment rates must be equal to the irrigated acre payment rates determined by the Department of Agriculture (USDA). In the case of an agreement that permits dryland agricultural uses, the annual payment rates must be equal to the difference between the irrigated acre payment rates and the dryland acre payment rates determined by USDA. The payment formula is retroactive for certain\u00a0existing drought and water conservation agreements.</p><p>Further, the bill exempts CREP payments from the $50,000 annual payment limitation under CRP.</p>",
      "updateDate": "2025-09-17",
      "versionCode": "id119s1389"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1389is.xml"
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
      "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Conservation Reserve Enhancement Program Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food Security Act of 1985 to modify the conservation reserve enhancement program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:23Z"
    }
  ]
}
```
