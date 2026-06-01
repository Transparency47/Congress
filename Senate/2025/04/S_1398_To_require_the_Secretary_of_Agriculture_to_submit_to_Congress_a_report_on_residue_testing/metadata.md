# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1398
- Title: Organic Imports Verification Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1398
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-03-11T11:03:19Z
- Update date including text: 2026-03-11T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1398",
    "number": "1398",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Organic Imports Verification Act of 2025",
    "type": "S",
    "updateDate": "2026-03-11T11:03:19Z",
    "updateDateIncludingText": "2026-03-11T11:03:19Z"
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
        "item": [
          {
            "date": "2025-04-09T20:51:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-09T20:51:11Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "SC"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-03-10",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1398is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1398\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Ricketts (for himself, Ms. Smith , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture to submit to Congress a report on residue testing for all imported organic feedstuffs shipped in bulk, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Organic Imports Verification Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Covered organic feedstuff**\nThe term covered organic feedstuff means any organic feedstuff included on the list established under section 4(b)\u2014\n**(A)**\nthat is shipped in bulk; and\n**(B)**\nfor which there is a national organic program import certificate.\n**(2) National organic program import certificate**\nThe term national organic program import certificate has the meaning given the term in section 2103 of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6502 ).\n**(3) Organic**\nThe term organic , with respect to a feedstuff, means that the feedstuff is organically produced (as defined in section 2103 of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6502 )).\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Administrator of the Agricultural Marketing Service.\n**(5) Shipped in bulk**\n**(A) In general**\nThe term shipped in bulk , with respect to a feedstuff, means that the feedstuff is shipped loose in a ship hold, railcar, container, or super sack, or by another similar method.\n**(B) Exclusion**\nThe term shipped in bulk , with respect to a feedstuff, does not include the shipment of that feedstuff as a packaged good.\n#### 3. Annual report on residue testing for covered organic feedstuffs and other imported organic feedstuffs\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to Congress a report on the residue testing described in subsection (b) that was carried out during the year covered by the report for\u2014\n**(1)**\neach covered organic feedstuff; and\n**(2)**\neach other imported organic feedstuff\u2014\n**(A)**\nthat is shipped in bulk; and\n**(B)**\nfor which there is a national organic program import certificate.\n##### (b) Residue testing described\nThe residue testing referred to in subsection (a) is residue testing carried out under any of the following:\n**(1)**\nSection 4(c).\n**(2)**\nSection 2107(a)(6) of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6506(a)(6) ).\n**(3)**\nSection 2112(a) of that Act ( 7 U.S.C. 6511(a) ).\n**(4)**\nSection 205.670(c) of title 7, Code of Federal Regulations (or a successor regulation).\n##### (c) Requirements\nEach report under subsection (a) shall include information on\u2014\n**(1)**\nthe frequency of the applicable residue testing;\n**(2)**\nthe methods used for that residue testing;\n**(3)**\nthe results of that residue testing;\n**(4)**\nthe standards used to analyze those results; and\n**(5)**\nany actions taken as a result of that residue testing.\n#### 4. Annual testing and corrective action\n##### (a) Risk-Based protocol\nThe Secretary, in consultation with the Secretary of Homeland Security and the organic agricultural product imports interagency working group established under section 2122A of the Organic Foods Production Act of 1990 ( 7 U.S.C. 6521a ), shall develop and regularly update risk-based protocols for\u2014\n**(1)**\ndetermining which imported organic feedstuffs shall be included on the list of covered organic feedstuffs described in subsection (b) each year; and\n**(2)**\ndetermining necessary parameters of residue testing for those imported organic feedstuffs, including\u2014\n**(A)**\nfrequency of testing;\n**(B)**\nquantity to be tested;\n**(C)**\ntype of testing;\n**(D)**\nresponsibility for testing; and\n**(E)**\nother necessary parameters.\n##### (b) List of covered organic feedstuffs\n**(1) In general**\nThe Secretary, using the risk-based protocol established under subsection (a)(1), shall establish and annually update a list of imported organic feedstuffs for which the Secretary shall carry out residue testing under subsection (c) during that year.\n**(2) Confidentiality**\nThe list established under paragraph (1) shall not be made publicly available.\n##### (c) Annual testing\nEach year, the Secretary shall carry out residue testing for each covered organic feedstuff.\n##### (d) Corrective action\nBeginning on the date of enactment of this Act, if any residue testing required under subsection (c) indicates any detectable prohibited substance at a level in excess of the level permitted by the national organic program established under the Organic Foods Production Act of 1990 ( 7 U.S.C. 6501 et seq. ) or the relevant, equivalent organic certification program of a State, the applicable shipment of that covered organic feedstuff\u2014\n**(1)**\nshall be excluded from organic sale; and\n**(2)**\nmay not be sold, labeled, or represented as organically produced.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-07T14:40:30Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1398is.xml"
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
      "title": "Organic Imports Verification Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Organic Imports Verification Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture to submit to Congress a report on residue testing for all imported organic feedstuffs shipped in bulk, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:28Z"
    }
  ]
}
```
