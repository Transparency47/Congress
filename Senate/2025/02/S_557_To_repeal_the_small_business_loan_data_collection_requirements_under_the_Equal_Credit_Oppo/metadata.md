# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/557?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/557
- Title: 1071 Repeal to Protect Small Business Lending Act
- Congress: 119
- Bill type: S
- Bill number: 557
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-12-06T07:05:17Z
- Update date including text: 2025-12-06T07:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/557",
    "number": "557",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "1071 Repeal to Protect Small Business Lending Act",
    "type": "S",
    "updateDate": "2025-12-06T07:05:17Z",
    "updateDateIncludingText": "2025-12-06T07:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T23:01:55Z",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AR"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WY"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "SD"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AL"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "KS"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "IA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s557is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 557\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Kennedy (for himself, Mrs. Hyde-Smith , Ms. Ernst , Mr. Boozman , Mr. Wicker , Mr. Barrasso , Mr. Rounds , Mr. Daines , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo repeal the small business loan data collection requirements under the Equal Credit Opportunity Act.\n#### 1. Short title\nThis Act may be cited as the 1071 Repeal to Protect Small Business Lending Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSection 704B of the Equal Credit Opportunity Act, as added by section 1071 of the Dodd-Frank Wall Street Reform and Consumer Protection Act ( Public Law 111\u2013203 ; 124 Stat. 2056), imposes data collection and reporting requirements on financial institutions regarding small business loans.\n**(2)**\nThese requirements have resulted in increased compliance costs for financial institutions, potentially reducing access to credit for small businesses.\n**(3)**\nThe regulatory burdens created by these requirements disproportionately impact smaller financial institutions, such as community banks and credit unions, which are critical to small business lending.\n**(4)**\nRepealing these requirements will reduce regulatory barriers and support greater access to credit for small businesses.\n#### 3. Repeal of the small business loan data collection requirements\n##### (a) In general\nSection 704B of the Equal Credit Opportunity Act ( 15 U.S.C. 1691c\u20132 ) is repealed.\n##### (b) Conforming amendments\n**(1) Dodd-Frank Wall Street Reform and Consumer Protection Act**\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(A)**\nin the table of contents in section 1(b) of such Act, by striking the item relating to section 1071; and\n**(B)**\nby striking section 1071 ( Public Law 111\u2013203 ; 124 Stat. 1056).\n**(2) Equal Credit Opportunity Act**\nThe Equal Credit Opportunity Act ( 15 U.S.C. 1691 et seq. ) is amended\u2014\n**(A)**\nin the table of contents for such Act, by striking the item relating to section 704B; and\n**(B)**\nin section 701(b) ( 15 U.S.C. 1691(b) )\u2014\n**(i)**\nin paragraph (3), by adding or at the end;\n**(ii)**\nin paragraph (4), by striking ; or and inserting a period; and\n**(iii)**\nby striking paragraph (5).",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-05-06",
        "text": "Placed on the Union Calendar, Calendar No. 65."
      },
      "number": "976",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "1071 Repeal to Protect Small Business Lending Act",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-04-08T14:42:43Z"
          },
          {
            "name": "Consumer credit",
            "updateDate": "2025-04-08T14:42:43Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-04-08T14:42:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-12T14:12:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s557",
          "measure-number": "557",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s557v00",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>1071 Repeal to Protect Small Business Lending Act</strong></p><p>This bill repeals the statute that requires financial institutions to collect data regarding applications for women-owned, minority-owned, or small business loans. Currently, financial institutions must collect and report to the Consumer Financial Protection Bureau information on (1) how many applications were received; (2) the disposition of each application; (3) the type of loan; (4) the amount applied for; (5) the amount approved; and (6) each applicant\u2019s census tract, revenue, race, sex, and ethnicity.</p>"
        },
        "title": "1071 Repeal to Protect Small Business Lending Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s557.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>1071 Repeal to Protect Small Business Lending Act</strong></p><p>This bill repeals the statute that requires financial institutions to collect data regarding applications for women-owned, minority-owned, or small business loans. Currently, financial institutions must collect and report to the Consumer Financial Protection Bureau information on (1) how many applications were received; (2) the disposition of each application; (3) the type of loan; (4) the amount applied for; (5) the amount approved; and (6) each applicant\u2019s census tract, revenue, race, sex, and ethnicity.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s557"
    },
    "title": "1071 Repeal to Protect Small Business Lending Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>1071 Repeal to Protect Small Business Lending Act</strong></p><p>This bill repeals the statute that requires financial institutions to collect data regarding applications for women-owned, minority-owned, or small business loans. Currently, financial institutions must collect and report to the Consumer Financial Protection Bureau information on (1) how many applications were received; (2) the disposition of each application; (3) the type of loan; (4) the amount applied for; (5) the amount approved; and (6) each applicant\u2019s census tract, revenue, race, sex, and ethnicity.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s557"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s557is.xml"
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
      "title": "1071 Repeal to Protect Small Business Lending Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "1071 Repeal to Protect Small Business Lending Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the small business loan data collection requirements under the Equal Credit Opportunity Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:46Z"
    }
  ]
}
```
