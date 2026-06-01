# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7962
- Title: Export Dispute Resolution Act
- Congress: 119
- Bill type: HR
- Bill number: 7962
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-05-13T19:05:38Z
- Update date including text: 2026-05-13T19:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.
- Latest action: 2026-03-17: Introduced in House

## Actions

- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7962",
    "number": "7962",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Export Dispute Resolution Act",
    "type": "HR",
    "updateDate": "2026-05-13T19:05:38Z",
    "updateDateIncludingText": "2026-05-13T19:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-17",
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
            "date": "2026-04-22T20:02:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-17T14:01:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7962ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7962\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Mr. McCormick introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 relating to the review of the interagency dispute resolution process.\n#### 1. Short title\nThis Act may be cited as the Export Dispute Resolution Act .\n#### 2. Review of interagency dispute resolution process\nSection 1763(c) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4822(c) ) is amended\u2014\n**(1)**\nby striking In any case and inserting the following:\n(1) In general In any case ;\n**(2)**\nby inserting countries subject to a comprehensive United States arms embargo, after matters relating to ;\n**(3)**\nby striking may be decided and inserting shall be decided ;\n**(4)**\nby adding at the end the following: The chair of the Committee is authorized to decide any case or matter described in the preceding sentence in which the Committee is unable to decide the case or matter by majority vote. ; and\n**(5)**\nby further adding at the end the following:\n(2) Definition In paragraph (1), the term country subject to a comprehensive United States arms embargo means\u2014 (A) any country listed on table 1 to paragraph (d)(1) of section 126.1 of title 22, Code of Federal Regulations (as such section is in effect on the day before the date of the enactment of this paragraph); and (B) the Russian Federation. .",
      "versionDate": "2026-03-17",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-01T18:41:21Z"
          },
          {
            "name": "Arms control and nonproliferation",
            "updateDate": "2026-05-01T18:41:21Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:41:21Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-05-01T18:41:21Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2026-05-01T18:41:21Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-01T18:41:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-02T22:21:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-17",
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
          "measure-id": "id119hr7962",
          "measure-number": "7962",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7962v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2026-03-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Export Dispute Resolution Act</strong></p><p>This bill revises the interagency dispute resolution process for export license applications. In particular, the bill requires the Operating Committee for Export Policy (an interagency body within the Department of Commerce's Bureau of Industry and Security) to resolve disputes related to specified matters by majority vote, including matters relating to countries that are subject to comprehensive U.S. arms\u00a0embargoes.</p><p>The bill also authorizes the\u00a0committee chair to decide cases and matters that cannot be decided by majority vote.</p>"
        },
        "title": "Export Dispute Resolution Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7962.xml",
    "summary": {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Export Dispute Resolution Act</strong></p><p>This bill revises the interagency dispute resolution process for export license applications. In particular, the bill requires the Operating Committee for Export Policy (an interagency body within the Department of Commerce's Bureau of Industry and Security) to resolve disputes related to specified matters by majority vote, including matters relating to countries that are subject to comprehensive U.S. arms\u00a0embargoes.</p><p>The bill also authorizes the\u00a0committee chair to decide cases and matters that cannot be decided by majority vote.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr7962"
    },
    "title": "Export Dispute Resolution Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Export Dispute Resolution Act</strong></p><p>This bill revises the interagency dispute resolution process for export license applications. In particular, the bill requires the Operating Committee for Export Policy (an interagency body within the Department of Commerce's Bureau of Industry and Security) to resolve disputes related to specified matters by majority vote, including matters relating to countries that are subject to comprehensive U.S. arms\u00a0embargoes.</p><p>The bill also authorizes the\u00a0committee chair to decide cases and matters that cannot be decided by majority vote.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr7962"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7962ih.xml"
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
      "title": "Export Dispute Resolution Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T07:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Export Dispute Resolution Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Export Control Reform Act of 2018 relating to the review of the interagency dispute resolution process.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T07:48:39Z"
    }
  ]
}
```
