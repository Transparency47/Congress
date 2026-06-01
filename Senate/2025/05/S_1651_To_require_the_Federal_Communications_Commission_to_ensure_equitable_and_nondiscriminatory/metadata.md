# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1651?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1651
- Title: Lowering Broadband Costs for Consumers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1651
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-03-24T11:03:18Z
- Update date including text: 2026-03-24T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1651",
    "number": "1651",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Lowering Broadband Costs for Consumers Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T11:03:18Z",
    "updateDateIncludingText": "2026-03-24T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-07",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-07",
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
            "date": "2025-05-07T20:54:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-07T20:54:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "AZ"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "ID"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "ND"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1651is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1651\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Mullin (for himself, Mr. Kelly , Mr. Crapo , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Federal Communications Commission to ensure equitable and nondiscriminatory contributions to the mechanisms that preserve and advance universal service, to reduce the financial burden on consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lowering Broadband Costs for Consumers Act of 2025 .\n#### 2. Lowering broadband costs for consumers\n##### (a) Definitions\nIn this section:\n**(1) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Broadband provider**\nThe term broadband provider means a provider of broadband internet access service.\n**(3) Commission**\nThe term Commission means the Federal Communications Commission.\n**(4) Edge provider**\nThe term edge provider means a provider of online content or services, including\u2014\n**(A)**\na digital advertising service;\n**(B)**\na search engine;\n**(C)**\na social media platform;\n**(D)**\na streaming service;\n**(E)**\nan app store;\n**(F)**\na cloud computing service;\n**(G)**\nan over-the-top messaging service or any other service that enables texting;\n**(H)**\na videoconferencing service;\n**(I)**\na video gaming service; and\n**(J)**\nan e-commerce platform.\n**(5) Eligible telecommunications carrier**\nThe term eligible telecommunications carrier means a common carrier designated as an eligible telecommunications carrier under section 214(e) of the Communications Act of 1934 ( 47 U.S.C. 214(e) ).\n##### (b) Lowering broadband costs for consumers\nSection 254(d) of the Communications Act of 1934 ( 47 U.S.C. 254(d) ) is amended\u2014\n**(1)**\nby striking Every and inserting the following:\n(1) In general Every ; and\n**(2)**\nby adding at the end the following:\n(2) Rulemaking (A) Initial rulemaking Not later than 18 months after the date of enactment of the Lowering Broadband Costs for Consumers Act of 2025 , the Commission shall complete a rulemaking to reform the Universal Service Fund by expanding the contribution base so that broadband providers and edge providers, except as provided in paragraph (3) of this subsection, contribute on an equitable and nondiscriminatory basis to the specific, predictable, and sufficient mechanisms established by the Commission to preserve and advance universal service. (B) Revisions From time to time after the rulemaking described in subparagraph (A), the Commission may revise the rules adopted under that subparagraph, as necessary, to ensure that broadband providers and edge providers continue to contribute on an equitable and nondiscriminatory basis to the specific, predictable, and sufficient mechanisms established by the Commission to preserve and advance universal service. (3) Exempted edge providers and broadband providers The requirement to contribute described in paragraph (2) shall not apply to\u2014 (A) an edge provider that\u2014 (i) transmitted less than 3 percent of the estimated quantity of broadband data that was transmitted in the United States during the most recent year, as determined by the Commission; and (ii) earned less than $5,000,000,000 in revenue in the United States during the most recent year; or (B) an edge provider or broadband provider or class of edge providers or broadband providers if the revenue of the provider is such that the level of contribution of the provider to the preservation and advancement of universal service would be de minimis. (4) Broadband provider; edge provider defined In this subsection, the terms broadband provider and edge provider have the meanings given those terms in section 2 of the Lowering Broadband Costs for Consumers Act of 2025 . .\n##### (c) Supporting broadband providers\n**(1) Adoption of mechanism**\nNot later than 18 months after the date of enactment of this Act, the Commission shall complete a rulemaking to adopt a new mechanism under the high-cost program of the Universal Service Fund that will provide specific, predictable, and sufficient support for expenses incurred by a broadband provider that is an eligible telecommunications carrier in providing supported services to the extent that such expenses are not otherwise recovered from revenues earned from the assessment of just, reasonable, and affordable rates on end users in high-cost areas or from other universal service support mechanisms.\n**(2) Limit on eligible telecommunications carriers**\nThe Commission shall ensure that not more than 1 eligible telecommunications carrier for any area receives support from the mechanism adopted through the rulemaking conducted under paragraph (1).\n##### (d) Enforcement by the Federal Communications Commission\n**(1) Powers of Commission**\nExcept as otherwise provided, the Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) were incorporated into and made a part of this Act.\n**(2) Penalties, privileges, and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ).\n##### (e) Purpose; rule of construction\n**(1) Purpose**\nThe purpose of this section is to direct the Commission to require contributions to the Universal Service Fund from edge providers and broadband providers and to modify the high cost program to promote affordable and available broadband.\n**(2) Rule of construction**\nNothing in this section shall be construed to provide the Commission with\u2014\n**(A)**\nany new authority over broadband providers; or\n**(B)**\nany authority over edge providers other than as described in paragraph (1).",
      "versionDate": "2025-05-07",
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
        "actionDate": "2025-06-17",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4032",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lowering Broadband Costs for Consumers Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-09-16T19:43:45Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-09-16T19:43:45Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-09-16T19:43:45Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-09-16T19:43:45Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-09-16T19:43:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-27T14:20:20Z"
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
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1651is.xml"
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
      "title": "Lowering Broadband Costs for Consumers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lowering Broadband Costs for Consumers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Communications Commission to ensure equitable and nondiscriminatory contributions to the mechanisms that preserve and advance universal service, to reduce the financial burden on consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:21Z"
    }
  ]
}
```
