# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3959?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3959
- Title: Protecting Private Job Creators Act
- Congress: 119
- Bill type: HR
- Bill number: 3959
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-04-08T19:47:51Z
- Update date including text: 2026-04-08T19:47:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 41 - 11.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 448.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-523.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-523.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 41 - 11.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 448.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-523.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-523.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3959",
    "number": "3959",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Protecting Private Job Creators Act",
    "type": "HR",
    "updateDate": "2026-04-08T19:47:51Z",
    "updateDateIncludingText": "2026-04-08T19:47:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-25",
      "calendarNumber": {
        "calendar": "U00448"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 448.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-523.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-523.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 41 - 11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
        "item": [
          {
            "date": "2026-02-25T16:25:31Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T20:20:47Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:20:40Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-12T14:05:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "LA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "GA"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "MO"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3959ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3959\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Downing (for himself and Mr. Fields ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo except quotations of fixed-income securities from certain regulatory requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Private Job Creators Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn September 16, 2020, the Securities and Exchange Commission adopted a final rule amending Rule 15c2\u201311 under the Securities Exchange Act of 1934 ( 15 U.S.C. 78a et seq. ) which addresses disclosures in the OTC markets and imposes requirements upon broker-dealers who publish quotations in such markets.\n**(2)**\nRule 15c2\u201311 was promulgated in 1971, and has generally been understood to apply to OTC equity markets since that time.\n**(3)**\nThe amendments to Rule 15c2\u201311 were based on the economic analysis of OTC equity markets.\n**(4)**\nThe fixed-income markets are different in structure and function than OTC equity markets.\n**(5)**\nThe fixed-income markets are critical to the ability of thousands of businesses\u2019 ability to raise capital.\n**(6)**\nRule 144A requires that issuers make their financial and operational information available to qualified institutional buyers upon request.\n**(7)**\nFollowing No-Action Letters issued on September 24, 2021, and December 16, 2021, the Securities and Exchange Commission indicated that it would apply Rule 15c2\u201311 to fixed-income markets in a manner that made significant changes to long-standing regulatory requirements, without a rulemaking process, without analysis of the costs and benefits of the action, and without regard for the input of the public. According to a subsequent No-Action Letter, which was issued on November 30, 2022, the Securities and Exchange Commission will apply Rule 15c2\u201311 to fixed-income securities sold pursuant to Rule 144A after no-action relief expired on January 4, 2025.\n**(8)**\nOn October 30, 2023, the Securities and Exchange Commission exempted fixed-income securities sold pursuant to Rule 144A from Rule 15c2\u201311 compliance, finding doing so is appropriate in the public interest, and consistent with the protection of investors .\n**(9)**\nOn November 22, 2024, the Securities and Exchange Commission granted exemptive relief from Rule 15c2\u201311 compliance to all fixed-incomes securities that meet certain criteria.\n#### 3. Exception relating to quotations of fixed-income securities\n##### (a) In general\nSection 240.15c2\u201311 of title 17, Code of Federal Regulations, shall not apply with respect to quotations of fixed-income securities.\n##### (b) Fixed-Income security defined\nIn this section, the term fixed-income security means\u2014\n**(1)**\nany note, bond, debenture, certificate of deposit for a security, certificate of deposit, asset-backed security, or any other evidence of indebtedness; and\n**(2)**\nany security described under paragraph (1) that is convertible, with or without consideration, into any equity security or carrying any warrant or right to subscribe to or purchase any equity security.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr3959rh.xml",
      "text": "IB\nUnion Calendar No. 448\n119th CONGRESS\n2d Session\nH. R. 3959\n[Report No. 119\u2013523]\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Downing (for himself and Mr. Fields ) introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Gottheimer , Mr. David Scott of Georgia , Mrs. Wagner , Mr. Sessions , Mr. Moore of North Carolina , and Mr. Lawler\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on June 12, 2025\nA BILL\nTo except quotations of fixed-income securities from certain regulatory requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Private Job Creators Act .\n#### 2. Exception relating to quotations of fixed-income securities\n##### (a) In general\nSection 240.15c2\u201311 of title 17, Code of Federal Regulations, shall not apply with respect to quotations of fixed-income securities.\n##### (b) Fixed-Income security defined\nIn this section, the term fixed-income security means\u2014\n**(1)**\nany note, bond, debenture, certificate of deposit for a security, certificate of deposit, asset-backed security, or any other evidence of indebtedness; and\n**(2)**\nany security described under paragraph (1) that is convertible, with or without consideration, into any equity security or carrying any warrant or right to subscribe to or purchase any equity security.",
      "versionDate": "2026-02-25",
      "versionType": "Reported in House"
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-06T18:05:16Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-01-06T18:04:01Z"
          },
          {
            "name": "Securities",
            "updateDate": "2026-01-06T17:53:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-02T18:06:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-25",
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
          "measure-id": "id119hr3959",
          "measure-number": "3959",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3959v07",
            "update-date": "2026-04-08"
          },
          "action-date": "2026-02-25",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Protecting Private Job Creators Act</strong></p><p>This bill provides statutory authority for an exemption from specified disclosure requirements applicable to fixed-income securities (e.g., corporate bonds or a certificate of deposit).</p><p>Under current securities regulations, brokers and dealers are generally prohibited from publishing securities quotations (i.e., the sale price) in over-the-counter (i.e., not on a national exchange) markets unless they have certain information about the securities issuer in their records. The Securities and Exchange Commission issued a series of orders (with the latest order issued in November 2024) granting an exemption to this rule to fixed-income securities that comply with specified safe-harbor rules. The bill provides statutory authority for this exemption.</p>"
        },
        "title": "Protecting Private Job Creators Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3959.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Protecting Private Job Creators Act</strong></p><p>This bill provides statutory authority for an exemption from specified disclosure requirements applicable to fixed-income securities (e.g., corporate bonds or a certificate of deposit).</p><p>Under current securities regulations, brokers and dealers are generally prohibited from publishing securities quotations (i.e., the sale price) in over-the-counter (i.e., not on a national exchange) markets unless they have certain information about the securities issuer in their records. The Securities and Exchange Commission issued a series of orders (with the latest order issued in November 2024) granting an exemption to this rule to fixed-income securities that comply with specified safe-harbor rules. The bill provides statutory authority for this exemption.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr3959"
    },
    "title": "Protecting Private Job Creators Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Protecting Private Job Creators Act</strong></p><p>This bill provides statutory authority for an exemption from specified disclosure requirements applicable to fixed-income securities (e.g., corporate bonds or a certificate of deposit).</p><p>Under current securities regulations, brokers and dealers are generally prohibited from publishing securities quotations (i.e., the sale price) in over-the-counter (i.e., not on a national exchange) markets unless they have certain information about the securities issuer in their records. The Securities and Exchange Commission issued a series of orders (with the latest order issued in November 2024) granting an exemption to this rule to fixed-income securities that comply with specified safe-harbor rules. The bill provides statutory authority for this exemption.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr3959"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3959ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr3959rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Protecting Private Job Creators Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:53:29Z"
    },
    {
      "title": "Protecting Private Job Creators Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Private Job Creators Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To except quotations of fixed-income securities from certain regulatory requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:21Z"
    }
  ]
}
```
