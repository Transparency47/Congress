# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/451?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/451
- Title: Restoring State Mineral Revenues Act
- Congress: 119
- Bill type: S
- Bill number: 451
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/451",
    "number": "451",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Restoring State Mineral Revenues Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T17:51:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:06Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ND"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "UT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WY"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ND"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s451is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 451\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Daines (for himself, Mr. Cramer , Ms. Lummis , Mr. Curtis , Mr. Barrasso , Mr. Hoeven , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Mineral Leasing Act to eliminate an administrative fee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring State Mineral Revenues Act .\n#### 2. Elimination of an administrative fee under the Mineral Leasing Act\n##### (a) In general\nSection 35 of the Mineral Leasing Act ( 30 U.S.C. 191 ) is amended\u2014\n**(1)**\nin subsection (a), in the first sentence, by striking and, subject to the provisions of subsection (b), ;\n**(2)**\nby striking subsection (b);\n**(3)**\nby redesignating subsections (c) and (d) as subsections (b) and (c), respectively;\n**(4)**\nin paragraph (3)(B)(ii) of subsection (b) (as so redesignated), by striking subsection (d) and inserting subsection (c) ; and\n**(5)**\nin paragraph (3)(A)(ii) of subsection (c) (as so redesignated), by striking subsection (c)(2)(B) and inserting subsection (b)(2)(B) .\n##### (b) Conforming amendments\n**(1)**\nSection 6(a) of the Mineral Leasing Act for Acquired Lands ( 30 U.S.C. 355(a) ) is amended\u2014\n**(A)**\nin the first sentence, by striking Subject to the provisions of section 35(b) of the Mineral Leasing Act ( 30 U.S.C. 191(b) ), all and inserting All ; and\n**(B)**\nin the second sentence, by striking of the Act of February 25, 1920 (41 Stat. 450; 30 U.S.C. 191 ), and inserting of the Mineral Leasing Act ( 30 U.S.C. 191 ) .\n**(2)**\nSection 20(a) of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1019(a) ) is amended, in the second sentence of the matter preceding paragraph (1), by striking the provisions of subsection (b) of section 35 of the Mineral Leasing Act ( 30 U.S.C. 191(b) ) and section 5(a)(2) of this Act and inserting section 5(a)(2) .\n**(3)**\nSection 205(f) of the Federal Oil and Gas Royalty Management Act of 1982 ( 30 U.S.C. 1735(f) ) is amended\u2014\n**(A)**\nin the first sentence, by striking this Section and inserting this section ; and\n**(B)**\nby striking the fourth, fifth, and sixth sentences.",
      "versionDate": "2025-02-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Coal",
            "updateDate": "2025-12-03T16:19:10Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-12-03T16:16:08Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-12-03T16:15:05Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-12-03T16:19:05Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-12-03T16:15:52Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-12-03T16:14:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-12T16:50:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s451",
          "measure-number": "451",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-01-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s451v00",
            "update-date": "2026-01-27"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Restoring State Mineral Revenues Act</strong></p><p>This bill increases payments states receive for specified revenue generated from\u00a0oil, gas, geothermal steam, coal, and certain\u00a0other natural resources\u00a0on onshore federal land. Specifically, the bill eliminates the 2% administrative fee that the\u00a0Bureau of Land Management currently deducts from a state's payment for such natural resources developed within the state.</p>"
        },
        "title": "Restoring State Mineral Revenues Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s451.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restoring State Mineral Revenues Act</strong></p><p>This bill increases payments states receive for specified revenue generated from\u00a0oil, gas, geothermal steam, coal, and certain\u00a0other natural resources\u00a0on onshore federal land. Specifically, the bill eliminates the 2% administrative fee that the\u00a0Bureau of Land Management currently deducts from a state's payment for such natural resources developed within the state.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119s451"
    },
    "title": "Restoring State Mineral Revenues Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Restoring State Mineral Revenues Act</strong></p><p>This bill increases payments states receive for specified revenue generated from\u00a0oil, gas, geothermal steam, coal, and certain\u00a0other natural resources\u00a0on onshore federal land. Specifically, the bill eliminates the 2% administrative fee that the\u00a0Bureau of Land Management currently deducts from a state's payment for such natural resources developed within the state.</p>",
      "updateDate": "2026-01-27",
      "versionCode": "id119s451"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s451is.xml"
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
      "title": "Restoring State Mineral Revenues Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring State Mineral Revenues Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Mineral Leasing Act to eliminate an administrative fee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:50Z"
    }
  ]
}
```
