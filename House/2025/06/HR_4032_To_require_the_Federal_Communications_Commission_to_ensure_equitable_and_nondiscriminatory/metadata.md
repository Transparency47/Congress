# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4032
- Title: Lowering Broadband Costs for Consumers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4032
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-05-13T08:06:14Z
- Update date including text: 2026-05-13T08:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4032",
    "number": "4032",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Lowering Broadband Costs for Consumers Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:14Z",
    "updateDateIncludingText": "2026-05-13T08:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:01:40Z",
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
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NM"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "KS"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "KY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NM"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "OK"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "SD"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "IN"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "OR"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "MI"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MO"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "KS"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "WI"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NM"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "MO"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IN"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "OK"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NV"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "NE"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
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
      "sponsorshipDate": "2026-02-23",
      "state": "NE"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "IA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4032ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4032\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Feenstra (for himself, Ms. Leger Fernandez , Mr. Mann , Mr. Rogers of Kentucky , and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Federal Communications Commission to ensure equitable and nondiscriminatory contributions to the mechanisms that preserve and advance universal service, to reduce the financial burden on consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lowering Broadband Costs for Consumers Act of 2025 .\n#### 2. Lowering broadband costs for consumers\n##### (a) Definitions\nIn this section:\n**(1) Broadband internet access service**\nThe term broadband internet access service has the meaning given the term in section 8.1(b) of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Broadband provider**\nThe term broadband provider means a provider of broadband internet access service.\n**(3) Commission**\nThe term Commission means the Federal Communications Commission.\n**(4) Edge provider**\nThe term edge provider means a provider of online content or services, including\u2014\n**(A)**\na digital advertising service;\n**(B)**\na search engine;\n**(C)**\na social media platform;\n**(D)**\na streaming service;\n**(E)**\nan app store;\n**(F)**\na cloud computing service;\n**(G)**\nan over-the-top messaging service or any other service that enables texting;\n**(H)**\na videoconferencing service;\n**(I)**\na video gaming service; and\n**(J)**\nan e-commerce platform.\n**(5) Eligible telecommunications carrier**\nThe term eligible telecommunications carrier means a common carrier designated as an eligible telecommunications carrier under section 214(e) of the Communications Act of 1934 ( 47 U.S.C. 214(e) ).\n##### (b) Lowering broadband costs for consumers\nSection 254(d) of the Communications Act of 1934 ( 47 U.S.C. 254(d) ) is amended\u2014\n**(1)**\nby striking Every and inserting the following:\n(1) In general Every ; and\n**(2)**\nby adding at the end the following:\n(2) Rulemaking (A) Initial rulemaking Not later than 18 months after the date of enactment of the Lowering Broadband Costs for Consumers Act of 2025 , the Commission shall complete a rulemaking to reform the Universal Service Fund by expanding the contribution base so that broadband providers and edge providers, except as provided in paragraph (3) of this subsection, contribute on an equitable and nondiscriminatory basis to the specific, predictable, and sufficient mechanisms established by the Commission to preserve and advance universal service. (B) Revisions From time to time after the rulemaking described in subparagraph (A), the Commission may revise the rules adopted under that subparagraph, as necessary, to ensure that broadband providers and edge providers continue to contribute on an equitable and nondiscriminatory basis to the specific, predictable, and sufficient mechanisms established by the Commission to preserve and advance universal service. (3) Exempted edge providers and broadband providers The requirement to contribute described in paragraph (2) shall not apply to\u2014 (A) an edge provider that\u2014 (i) transmitted less than 3 percent of the estimated quantity of broadband data that was transmitted in the United States during the most recent year, as determined by the Commission; and (ii) earned less than $5,000,000,000 in revenue in the United States during the most recent year; or (B) an edge provider or broadband provider or class of edge providers or broadband providers if the revenue of the provider is such that the level of contribution of the provider to the preservation and advancement of universal service would be de minimis. (4) Broadband provider; edge provider defined In this subsection, the terms broadband provider and edge provider have the meanings given those terms in section 2 of the Lowering Broadband Costs for Consumers Act of 2025 . .\n##### (c) Supporting broadband providers\n**(1) Adoption of mechanism**\nNot later than 18 months after the date of enactment of this Act, the Commission shall complete a rulemaking to adopt a new mechanism under the high-cost program of the Universal Service Fund that will provide specific, predictable, and sufficient support for expenses incurred by a broadband provider that is an eligible telecommunications carrier in providing supported services to the extent that such expenses are not otherwise recovered from revenues earned from the assessment of just, reasonable, and affordable rates on end users in high-cost areas or from other universal service support mechanisms.\n**(2) Limit on eligible telecommunications carriers**\nThe Commission shall ensure that not more than 1 eligible telecommunications carrier for any area receives support from the mechanism adopted through the rulemaking conducted under paragraph (1).\n##### (d) Enforcement by the Federal Communications Commission\n**(1) Powers of Commission**\nExcept as otherwise provided, the Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) were incorporated into and made a part of this Act.\n**(2) Penalties, privileges, and immunities**\nAny person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ).\n##### (e) Purpose; rule of construction\n**(1) Purpose**\nThe purpose of this section is to direct the Commission to require contributions to the Universal Service Fund from edge providers and broadband providers and to modify the high cost program to promote affordable and available broadband.\n**(2) Rule of construction**\nNothing in this section shall be construed to provide the Commission with\u2014\n**(A)**\nany new authority over broadband providers; or\n**(B)**\nany authority over edge providers other than as described in paragraph (1).",
      "versionDate": "2025-06-17",
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lowering Broadband Costs for Consumers Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2025-09-16T18:19:47Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-09-16T19:43:22Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-09-16T19:27:55Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-09-16T19:17:32Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-09-16T19:09:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-07-08T12:58:07Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4032ih.xml"
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
      "title": "Lowering Broadband Costs for Consumers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lowering Broadband Costs for Consumers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Communications Commission to ensure equitable and nondiscriminatory contributions to the mechanisms that preserve and advance universal service, to reduce the financial burden on consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T07:18:32Z"
    }
  ]
}
```
