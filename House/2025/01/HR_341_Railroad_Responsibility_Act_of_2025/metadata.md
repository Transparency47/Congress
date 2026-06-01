# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/341
- Title: Railroad Responsibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 341
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-02-13T15:58:15Z
- Update date including text: 2025-02-13T15:58:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-14 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-14 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/341",
    "number": "341",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Railroad Responsibility Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-13T15:58:15Z",
    "updateDateIncludingText": "2025-02-13T15:58:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-14T15:33:27Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr341ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 341\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to provide States the authority to limit blocking grade rail crossings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Railroad Responsibility Act of 2025 .\n#### 2. State authority to limit blocking grade rail crossings\n##### (a) General jurisdiction of Surface Transportation Board\nSection 10501(c)(3) of title 49, United States Code, is amended by adding at the end the following:\n(C) State authority To limit blocking grade rail crossings Notwithstanding any other provision of law, this title does not preempt a State from the adoption or enactment of any law, regulation, order, or other requirement related to limiting the duration that a railroad carrier may block a grade rail crossing. .\n##### (b) Preemption\nSection 20106(a) of title 49, United States Code, is amended by adding at the end the following:\n(3) State authority To limit blocking grade rail crossings (A) In general Notwithstanding any other provision of law, this title does not preempt a State from the adoption or enactment of any law, regulation, order, or other requirement related to limiting the duration that a railroad carrier may block a grade rail crossing. (B) State defined In this paragraph, the term State means a State of the United States and the District of Columbia. .",
      "versionDate": "2025-01-13",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-12T17:50:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr341",
          "measure-number": "341",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr341v00",
            "update-date": "2025-02-13"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Railroad Responsibility Act of 2025</strong></p><p>This bill provides states with the authority to adopt or enact any law, regulation, order, or other requirement limiting the duration that a railroad carrier may block a grade rail crossing. Specifically, this bill states that federal transportation laws do not preempt a state from adopting or enacting these limits.\u00a0</p><p>As background, state and federal courts have generally found that state laws regarding obstructed crossings are preempted by one or more federal laws, thereby\u00a0rendering the state laws\u00a0unenforceable.</p>"
        },
        "title": "Railroad Responsibility Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr341.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Railroad Responsibility Act of 2025</strong></p><p>This bill provides states with the authority to adopt or enact any law, regulation, order, or other requirement limiting the duration that a railroad carrier may block a grade rail crossing. Specifically, this bill states that federal transportation laws do not preempt a state from adopting or enacting these limits.\u00a0</p><p>As background, state and federal courts have generally found that state laws regarding obstructed crossings are preempted by one or more federal laws, thereby\u00a0rendering the state laws\u00a0unenforceable.</p>",
      "updateDate": "2025-02-13",
      "versionCode": "id119hr341"
    },
    "title": "Railroad Responsibility Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Railroad Responsibility Act of 2025</strong></p><p>This bill provides states with the authority to adopt or enact any law, regulation, order, or other requirement limiting the duration that a railroad carrier may block a grade rail crossing. Specifically, this bill states that federal transportation laws do not preempt a state from adopting or enacting these limits.\u00a0</p><p>As background, state and federal courts have generally found that state laws regarding obstructed crossings are preempted by one or more federal laws, thereby\u00a0rendering the state laws\u00a0unenforceable.</p>",
      "updateDate": "2025-02-13",
      "versionCode": "id119hr341"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr341ih.xml"
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
      "title": "Railroad Responsibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Railroad Responsibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to provide States the authority to limit blocking grade rail crossings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:03:28Z"
    }
  ]
}
```
