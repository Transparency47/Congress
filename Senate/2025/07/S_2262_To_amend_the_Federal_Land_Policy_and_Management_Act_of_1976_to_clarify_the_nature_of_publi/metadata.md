# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2262
- Title: American Voices in Federal Lands Act
- Congress: 119
- Bill type: S
- Bill number: 2262
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S4317-4318)
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S4317-4318)
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2262",
    "number": "2262",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "American Voices in Federal Lands Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
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
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S4317-4318)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-10",
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
            "date": "2025-12-17T14:30:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-10T18:54:31Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:48Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "WY"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "ID"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "ID"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "UT"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2262is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2262\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Barrasso (for himself, Ms. Lummis , Mr. Crapo , Mr. Risch , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Land Policy and Management Act of 1976 to clarify the nature of public involvement for purposes of certain rulemaking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Voices in Federal Lands Act .\n#### 2. Public involvement in certain public land rulemaking\n##### (a) Definition of public involvement\nSection 103(d) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702(d) ) is amended by striking citizens and inserting citizens of the United States, in accordance with section 310(d), as applicable, .\n##### (b) Public involvement relating to certain rules and regulations\nSection 310 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1740 ) is amended to read as follows:\n310. Rules and regulations (a) Authorization (1) Secretary Subject to subsection (d), the Secretary, with respect to public lands, shall promulgate rules and regulations to carry out the purposes of\u2014 (A) this Act; and (B) other laws applicable to public lands. (2) Secretary of Agriculture The Secretary of Agriculture, with respect to land in the National Forest System, shall promulgate rules and regulations to carry out the purposes of this Act. (b) Requirement The promulgation of rules and regulations pursuant to this section shall be in accordance with chapter 5 of title 5, United States Code, without regard to section 553(a)(2) of that title. (c) Absence of regulation Before the promulgation of a rule or regulation pursuant to this section with respect to public lands or land in the National Forest System, the applicable land shall be administered under existing rules and regulations concerning the land, to the maximum extent practicable. (d) Public involvement relating to Bureau land Notwithstanding any other provision of law, with respect to public lands managed by the Bureau, the Secretary\u2014 (1) in promulgating any applicable regulations pursuant to this or any other Act, may take into consideration only public comments received from citizens of the United States; and (2) in any public involvement under this Act or any other provision of law (including regulations), shall establish and implement a process commonly known as Completely Automated Public Test to tell Computers and Humans Apart (CAPTCHA) to deter attempts at public involvement via artificial intelligence. .",
      "versionDate": "2025-07-10",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-01-07T16:52:31Z"
          },
          {
            "name": "Department of Agriculture",
            "updateDate": "2026-01-07T16:52:36Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-07T16:52:40Z"
          },
          {
            "name": "Public participation and lobbying",
            "updateDate": "2026-01-07T16:52:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:38:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-10",
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
          "measure-id": "id119s2262",
          "measure-number": "2262",
          "measure-type": "s",
          "orig-publish-date": "2025-07-10",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2262v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-07-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>American Voices in Federal Lands Act</strong></p><p>This bill directs the Bureau of Land Management to modify its public comment system by (1) only considering public comments from U.S. citizens; and (2) deterring attempts at public involvement via artificial intelligence (AI), such as\u00a0AI\u00a0bots,\u00a0by establishing and implementing a Completely Automated Public Turing Test to tell Computers and Humans Apart (CAPTCHA test).\u00a0\u00a0</p>"
        },
        "title": "American Voices in Federal Lands Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2262.xml",
    "summary": {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Voices in Federal Lands Act</strong></p><p>This bill directs the Bureau of Land Management to modify its public comment system by (1) only considering public comments from U.S. citizens; and (2) deterring attempts at public involvement via artificial intelligence (AI), such as\u00a0AI\u00a0bots,\u00a0by establishing and implementing a Completely Automated Public Turing Test to tell Computers and Humans Apart (CAPTCHA test).\u00a0\u00a0</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s2262"
    },
    "title": "American Voices in Federal Lands Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Voices in Federal Lands Act</strong></p><p>This bill directs the Bureau of Land Management to modify its public comment system by (1) only considering public comments from U.S. citizens; and (2) deterring attempts at public involvement via artificial intelligence (AI), such as\u00a0AI\u00a0bots,\u00a0by establishing and implementing a Completely Automated Public Turing Test to tell Computers and Humans Apart (CAPTCHA test).\u00a0\u00a0</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s2262"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2262is.xml"
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
      "title": "American Voices in Federal Lands Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Voices in Federal Lands Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Land Policy and Management Act of 1976 to clarify the nature of public investment for purposes of certain rulemaking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:58Z"
    }
  ]
}
```
