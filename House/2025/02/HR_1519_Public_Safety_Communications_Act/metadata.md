# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1519?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1519
- Title: Public Safety Communications Act
- Congress: 119
- Bill type: HR
- Bill number: 1519
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-01-27T18:19:29Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-24 - Committee: Referred to the Subcommittee on Communications and Technology.
- 2026-01-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-01-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-24 - Committee: Referred to the Subcommittee on Communications and Technology.
- 2026-01-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-01-15 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1519",
    "number": "1519",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Public Safety Communications Act",
    "type": "HR",
    "updateDate": "2026-01-27T18:19:29Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Communications and Technology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-01-15T22:08:46Z",
                "name": "Reported by"
              },
              {
                "date": "2026-01-15T22:07:59Z",
                "name": "Markup by"
              },
              {
                "date": "2025-02-24T22:07:16Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Communications and Technology Subcommittee",
          "systemCode": "hsif16"
        }
      },
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1519ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1519\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mrs. Cammack introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the National Telecommunications and Information Administration Organization Act to establish the Office of Public Safety Communications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Safety Communications Act .\n#### 2. Establishment of the Office of Public Safety Communications\nPart A of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 901 et seq. ) is amended by adding at the end the following:\n106. Establishment of the Office of Public Safety Communications (a) Establishment There is established within the NTIA the Office of Public Safety Communications (in this section referred to as the Office ). (b) Head of office (1) In general The head of the Office shall be the Associate Administrator for Public Safety Communications. (2) Career position The position of Associate Administrator shall be a career position in the Senior Executive Service occupied by a career appointee (as that term is defined in section 3132(a)(4) of title 5, United States Code). (3) Requirement to report The Associate Administrator shall report to the Assistant Secretary. (c) Duties The Associate Administrator shall\u2014 (1) administer any grant program of the Federal Government related to Next Generation 9\u20131\u20131 on behalf of the Assistant Secretary; (2) analyze public safety policy communications issues, including by obtaining such analysis; (3) provide to the Assistant Secretary advice and assistance with respect to the Assistant Secretary\u2014 (A) carrying out the responsibilities of NTIA related to public safety communications policy; and (B) evaluating the domestic impact of public safety communications matters pending before the Commission, Congress, or other entities of the executive branch of the Federal Government; (4) carrying out any duties established under section 10 of Department Organizational Order 25\u20137 of the Department of Commerce titled National Telecommunications and Information Administration , effective September 17, 2012; and (5) be responsible for the oversight of\u2014 (A) the studies carried out by the Federal Government relating to enhancing public safety communication; and (B) the prototyping (including leading edge prototyping) and deployment by the Federal Government of advanced communications technologies that enhance public safety communications, including through test-protocol, model, or simulation tool for the testing and validation of such technologies; (6) manage the First Responder Network Authority established under section 6206 of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1426 ), including by being responsible for the oversight of the duties and responsibilities carried out by the First Responder Network Authority; (7) at the direction of the Assistant Secretary, communicate public safety communications policies to public entities, including the Commission and Congress, or private entities; and (8) carry out any duties regarding the responsibilities of the NTIA with respect to public safety communications policy as the Assistant Secretary may designate. (d) Audit The Associate Administrator\u2014 (1) shall annually conduct an audit of the activities of the First Responder Network Authority in accordance with general accounting principles and procedures; and (2) may conduct such audit (or parts thereof) through a contractor whose services were procured in accordance with title 41, United States Code. .",
      "versionDate": "2025-02-24",
      "versionType": "Introduced in House"
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-01-27T18:18:50Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-01-27T18:12:05Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2026-01-27T18:16:28Z"
          },
          {
            "name": "Technology assessment",
            "updateDate": "2026-01-27T18:19:28Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-01-27T18:17:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-14T13:02:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1519",
          "measure-number": "1519",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-06-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1519v00",
            "update-date": "2025-06-23"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Public Safety Communications Act</strong></p><p>This bill provides statutory authority for the Office of Public Safety Communications within the National Telecommunications and Information Administration to support efforts related to public safety communications. The duties of the office include (1) administering federal grant programs for Next Generation 9-1-1 systems, which are interoperable Internet Protocol-based systems for receiving 9-1-1 calls; and (2) managing and auditing the First Responder Network Authority (known as FirstNet), which oversees the communications network for emergency responders and the public safety community.</p>"
        },
        "title": "Public Safety Communications Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1519.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Public Safety Communications Act</strong></p><p>This bill provides statutory authority for the Office of Public Safety Communications within the National Telecommunications and Information Administration to support efforts related to public safety communications. The duties of the office include (1) administering federal grant programs for Next Generation 9-1-1 systems, which are interoperable Internet Protocol-based systems for receiving 9-1-1 calls; and (2) managing and auditing the First Responder Network Authority (known as FirstNet), which oversees the communications network for emergency responders and the public safety community.</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119hr1519"
    },
    "title": "Public Safety Communications Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Public Safety Communications Act</strong></p><p>This bill provides statutory authority for the Office of Public Safety Communications within the National Telecommunications and Information Administration to support efforts related to public safety communications. The duties of the office include (1) administering federal grant programs for Next Generation 9-1-1 systems, which are interoperable Internet Protocol-based systems for receiving 9-1-1 calls; and (2) managing and auditing the First Responder Network Authority (known as FirstNet), which oversees the communications network for emergency responders and the public safety community.</p>",
      "updateDate": "2025-06-23",
      "versionCode": "id119hr1519"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1519ih.xml"
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
      "title": "Public Safety Communications Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T12:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Safety Communications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Telecommunications and Information Administration Organization Act to establish the Office of Public Safety Communications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T12:18:37Z"
    }
  ]
}
```
