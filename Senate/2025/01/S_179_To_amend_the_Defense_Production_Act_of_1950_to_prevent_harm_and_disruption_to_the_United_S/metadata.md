# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/179?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/179
- Title: FARM Act
- Congress: 119
- Bill type: S
- Bill number: 179
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2026-04-09T15:17:36Z
- Update date including text: 2026-04-09T15:17:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/179",
    "number": "179",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "FARM Act",
    "type": "S",
    "updateDate": "2026-04-09T15:17:36Z",
    "updateDateIncludingText": "2026-04-09T15:17:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T16:27:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "PA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "KS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ND"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "ND"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MT"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "NE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s179is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 179\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Mr. Tuberville (for himself, Mr. Fetterman , Mr. Marshall , Mrs. Britt , Mr. Scott of Florida , Mr. Schmitt , Mr. Sheehy , Mr. Cramer , Mr. Hoeven , Mrs. Blackburn , Mr. Daines , Mrs. Fischer , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Defense Production Act of 1950 to prevent harm and disruption to the United States agriculture industry by protecting against foreign influence over agriculture production and supply chains, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Adversary Risk Management Act or the FARM Act .\n#### 2. United States agriculture included in Committee on Foreign Investment in the United States\n##### (a) Agriculture representative\nSection 721(k)(2) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(k)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (H), (I), and (J) as subparagraphs (I), (J), and (K), respectively; and\n**(2)**\nby inserting after subparagraph (G) the following:\n(H) The Secretary of Agriculture. .\n##### (b) Review of agriculture investments by foreign entities\nSection 721(a)(4) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) any transaction described in subparagraph (B)(vi) that is proposed, pending, or completed on or after the date of the enactment of the Foreign Adversary Risk Management Act . ; and\n**(2)**\nin subparagraph (B), by adding at the end the following:\n(vi) Any transaction, merger, acquisition, transfer, agreement, takeover, or other arrangement that could result in foreign control of any United States business that is engaged in agriculture and uses agricultural products (as defined in the first section of the Act of July 2, 1926 (44 Stat. 802, chapter 725; 7 U.S.C. 451 )). .\n##### (c) Agricultural supply chains included in critical infrastructure\nSection 721(a)(5) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(5) ) is amended\u2014\n**(1)**\nby striking critical infrastructure means and inserting the following:\ncritical infrastructure \u2014 (A) means ;\n**(2)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(B) includes, subject to regulations prescribed by the Committee, agricultural systems and supply chains. .\n##### (d) Agricultural supply chains included as critical technologies\nSection 721(a)(6)(A) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(6)(A) ) is amended by adding at the end the following:\n(vii) Agricultural supply chains used for agricultural products (as defined in the first section of the Act of July 2, 1926 (44 Stat. 802, chapter 725; 7 U.S.C. 451 )). .\n#### 3. Reports on investments by foreign countries in United States agriculture industry\nNot later than one year after the date of the enactment of this Act, the Secretary of Agriculture and the Comptroller General of the United States shall each\u2014\n**(1)**\nconduct an analysis of foreign influence in the United States agriculture industry; and\n**(2)**\nsubmit to Congress a report that includes a summary of\u2014\n**(A)**\nforeign investments in the United States agriculture industry;\n**(B)**\nthe potential for foreign investment to undermine United States agriculture production and agricultural supply chains;\n**(C)**\nthe largest international threats for increased foreign control of, and investment in, the United States agriculture sector; and\n**(D)**\nagriculture-related espionage and theft techniques used by foreign governments, including any attempts to target United States agricultural intellectual property, innovation, research and development, cost or pricing data, or internal strategy documents.",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-02-28",
        "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture."
      },
      "number": "620",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FARM Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-13T15:37:14Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-03-13T15:37:14Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-13T15:37:14Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-09T15:17:36Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-03-13T15:37:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-02-27T16:51:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119s179",
          "measure-number": "179",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s179v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Foreign Adversary Risk Management Act or the FARM Act</strong></p><p>This bill places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS). It also requires CFIUS to review any investment that could result in foreign control of any U.S. agricultural business.</p><p>Further, the bill includes agricultural systems and supply chains in the definitions of <em>critical infrastructure</em> and <em>critical technologies</em> for the purposes of reviewing such investments.</p><p>The Department of Agriculture and the Government Accountability Office must each analyze and report on foreign influence in the U.S. agricultural industry.</p>"
        },
        "title": "FARM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s179.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Foreign Adversary Risk Management Act or the FARM Act</strong></p><p>This bill places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS). It also requires CFIUS to review any investment that could result in foreign control of any U.S. agricultural business.</p><p>Further, the bill includes agricultural systems and supply chains in the definitions of <em>critical infrastructure</em> and <em>critical technologies</em> for the purposes of reviewing such investments.</p><p>The Department of Agriculture and the Government Accountability Office must each analyze and report on foreign influence in the U.S. agricultural industry.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s179"
    },
    "title": "FARM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Foreign Adversary Risk Management Act or the FARM Act</strong></p><p>This bill places the Secretary of Agriculture on the Committee on Foreign Investment in the United States (CFIUS). It also requires CFIUS to review any investment that could result in foreign control of any U.S. agricultural business.</p><p>Further, the bill includes agricultural systems and supply chains in the definitions of <em>critical infrastructure</em> and <em>critical technologies</em> for the purposes of reviewing such investments.</p><p>The Department of Agriculture and the Government Accountability Office must each analyze and report on foreign influence in the U.S. agricultural industry.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s179"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s179is.xml"
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
      "title": "FARM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FARM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Foreign Adversary Risk Management Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Defense Production Act of 1950 to prevent harm and disruption to the United States agriculture industry by protecting against foreign influence over agriculture production and supply chains, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:20Z"
    }
  ]
}
```
