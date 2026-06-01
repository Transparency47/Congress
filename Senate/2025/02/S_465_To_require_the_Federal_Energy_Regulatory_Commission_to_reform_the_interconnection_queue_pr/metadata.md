# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/465?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/465
- Title: GRID Power Act
- Congress: 119
- Bill type: S
- Bill number: 465
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-04-17T13:12:24Z
- Update date including text: 2026-04-17T13:12:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/465",
    "number": "465",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "GRID Power Act",
    "type": "S",
    "updateDate": "2026-04-17T13:12:24Z",
    "updateDateIncludingText": "2026-04-17T13:12:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.",
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
          "date": "2025-02-06T19:25:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-15T19:37:20Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "IN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "KS"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s465is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 465\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Hoeven (for himself and Mr. Young ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Federal Energy Regulatory Commission to reform the interconnection queue process for the prioritization and approval of certain projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guaranteeing Reliability through the Interconnection of Dispatchable Power Act or the GRID Power Act .\n#### 2. Definitions\nIn this Act:\n**(1) Bulk-power system**\nThe term bulk-power system has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(2) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(3) Dispatchable power**\nThe term dispatchable power means an electric energy generation resource capable of providing known and forecastable electric supply in time intervals necessary to ensure grid reliability.\n**(4) Grid reliability**\nThe term grid reliability means the ability of the electric grid to deliver an adequate, secure, and stable flow of electricity in the quantity and with the quality demanded by users, taking into account the ability of the bulk-power system to withstand sudden disturbances.\n**(5) Grid resilience**\nThe term grid resilience means the ability of the electric grid to adapt to changing physical conditions and withstand and rapidly recover from significant disturbances, including natural disasters, cyber-attacks, and other unforeseen events.\n**(6) Independent System Operator**\nThe term Independent System Operator has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(7) Regional Transmission Organization**\nThe term Regional Transmission Organization has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(8) Resource adequacy**\nThe term resource adequacy means the ability of the electric system to meet the aggregate electrical demand and energy requirements of end-use customers at all times, accounting for scheduled and reasonably expected unscheduled outages of bulk-power system components.\n**(9) Transmission provider**\nThe term transmission provider means\u2014\n**(A)**\na public utility (as defined in section 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) )) that owns, operates, or controls 1 or more transmission facilities;\n**(B)**\nan Independent System Operator; and\n**(C)**\na Regional Transmission Organization.\n#### 3. Rulemaking to improve interconnection queue flexibility\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Commission shall initiate a rulemaking\u2014\n**(1)**\nto address the inefficiencies and ineffectiveness of existing procedures for processing interconnection requests to ensure that new dispatchable power projects that improve grid reliability and resource adequacy can interconnect to the electric grid quickly, cost-effectively, and reliably; and\n**(2)**\nto amend the pro forma Large Generator Interconnection Procedures and, as appropriate, the pro forma Large Generator Interconnection Agreement, promulgated pursuant to section 35.28(f) of title 18, Code of Federal Regulations (or successor regulations)\u2014\n**(A)**\nto authorize transmission providers to submit proposals to the Commission to adjust the interconnection queue of the transmission provider to prioritize new dispatchable power projects that will improve grid reliability and resource adequacy by assigning those projects higher positions in the interconnection queue; and\n**(B)**\nto require transmission providers\u2014\n**(i)**\nto provide in any proposal described in subparagraph (A)\u2014\n**(I)**\na demonstration of need for prioritization of the relevant projects; and\n**(II)**\na description of how the prioritization of those projects will improve grid reliability or grid resilience;\n**(ii)**\nto provide a process for public comment and stakeholder engagement before a proposal described in subparagraph (A) is submitted to the Commission; and\n**(iii)**\nto provide regular reporting to the Commission on the state of grid reliability and grid resilience, including reporting on any actions taken pursuant to this Act.\n##### (b) Commission approval\nTo ensure timely responses to grid reliability concerns, not later than 60 days after a proposal is submitted pursuant to subsection (a)(2), the Commission shall\u2014\n**(1)**\nreview the proposal; and\n**(2)**\napprove or deny the proposal.\n##### (c) Deadline for final rule\nNot later than 180 days after the date of enactment of this Act, the Commission shall promulgate final regulations to complete the rulemaking initiated under subsection (a).\n##### (d) Periodic review\nNot less frequently than once every 5 years, the Commission shall review and, if necessary, update the regulations promulgated under this section to ensure that those regulations remain effective and relevant to evolving grid reliability and grid resilience challenges.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-09-19",
        "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "1047",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GRID Power Act",
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
            "name": "Electric power generation and transmission",
            "updateDate": "2025-06-16T16:12:59Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-06-16T16:26:41Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-06-16T16:38:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-12T17:30:08Z"
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
          "measure-id": "id119s465",
          "measure-number": "465",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s465v00",
            "update-date": "2026-04-17"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Guaranteeing Reliability through the Interconnection of Dispatchable Power Act or the GRID Power Act</strong></p><p>This bill requires the Federal Energy Regulatory Commission (FERC) to issue and periodically review a rule that revises the approval process for interconnection requests of generating units that produce\u00a0electricity to prioritize dispatchable power projects (e.g., certain fossil fuel projects).\u00a0</p><p>Under the bill,<em> d</em><em>ispatchable power</em> generally refers to an electric energy generation resource, such as a generating unit that produces electricity from fossil fuels, capable of providing known and forecastable electric supply in time intervals necessary to ensure grid reliability.\u00a0Currently, FERC receives interconnection requests\u00a0from those projects and other generating units, such as units that produce electricity from renewable energy. Interconnection requests are\u00a0requests from generating units to connect to the high voltage transmission lines of the electric grid.</p><p>First, the rule must address the\u00a0efficiency and effectiveness of the existing procedures\u00a0for processing interconnection\u00a0requests to ensure that new dispatchable power projects that improve grid reliability and resource adequacy can interconnect to the electric grid quickly, cost-effectively, and reliably.\u00a0</p><p>Second, the rule must revise the pro forma Large Generator Interconnection Procedures, and the pro forma Large Generator Interconnection Agreement as appropriate,\u00a0to authorize transmission providers to submit proposals to FERC to prioritize new dispatchable power projects that will improve grid reliability and resource adequacy by assigning those projects higher positions in the interconnection queue of the provider. FERC must review and approve or deny such proposals within 60 days after the proposal is submitted.</p>"
        },
        "title": "GRID Power Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s465.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guaranteeing Reliability through the Interconnection of Dispatchable Power Act or the GRID Power Act</strong></p><p>This bill requires the Federal Energy Regulatory Commission (FERC) to issue and periodically review a rule that revises the approval process for interconnection requests of generating units that produce\u00a0electricity to prioritize dispatchable power projects (e.g., certain fossil fuel projects).\u00a0</p><p>Under the bill,<em> d</em><em>ispatchable power</em> generally refers to an electric energy generation resource, such as a generating unit that produces electricity from fossil fuels, capable of providing known and forecastable electric supply in time intervals necessary to ensure grid reliability.\u00a0Currently, FERC receives interconnection requests\u00a0from those projects and other generating units, such as units that produce electricity from renewable energy. Interconnection requests are\u00a0requests from generating units to connect to the high voltage transmission lines of the electric grid.</p><p>First, the rule must address the\u00a0efficiency and effectiveness of the existing procedures\u00a0for processing interconnection\u00a0requests to ensure that new dispatchable power projects that improve grid reliability and resource adequacy can interconnect to the electric grid quickly, cost-effectively, and reliably.\u00a0</p><p>Second, the rule must revise the pro forma Large Generator Interconnection Procedures, and the pro forma Large Generator Interconnection Agreement as appropriate,\u00a0to authorize transmission providers to submit proposals to FERC to prioritize new dispatchable power projects that will improve grid reliability and resource adequacy by assigning those projects higher positions in the interconnection queue of the provider. FERC must review and approve or deny such proposals within 60 days after the proposal is submitted.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s465"
    },
    "title": "GRID Power Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Guaranteeing Reliability through the Interconnection of Dispatchable Power Act or the GRID Power Act</strong></p><p>This bill requires the Federal Energy Regulatory Commission (FERC) to issue and periodically review a rule that revises the approval process for interconnection requests of generating units that produce\u00a0electricity to prioritize dispatchable power projects (e.g., certain fossil fuel projects).\u00a0</p><p>Under the bill,<em> d</em><em>ispatchable power</em> generally refers to an electric energy generation resource, such as a generating unit that produces electricity from fossil fuels, capable of providing known and forecastable electric supply in time intervals necessary to ensure grid reliability.\u00a0Currently, FERC receives interconnection requests\u00a0from those projects and other generating units, such as units that produce electricity from renewable energy. Interconnection requests are\u00a0requests from generating units to connect to the high voltage transmission lines of the electric grid.</p><p>First, the rule must address the\u00a0efficiency and effectiveness of the existing procedures\u00a0for processing interconnection\u00a0requests to ensure that new dispatchable power projects that improve grid reliability and resource adequacy can interconnect to the electric grid quickly, cost-effectively, and reliably.\u00a0</p><p>Second, the rule must revise the pro forma Large Generator Interconnection Procedures, and the pro forma Large Generator Interconnection Agreement as appropriate,\u00a0to authorize transmission providers to submit proposals to FERC to prioritize new dispatchable power projects that will improve grid reliability and resource adequacy by assigning those projects higher positions in the interconnection queue of the provider. FERC must review and approve or deny such proposals within 60 days after the proposal is submitted.</p>",
      "updateDate": "2026-04-17",
      "versionCode": "id119s465"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s465is.xml"
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
      "title": "GRID Power Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GRID Power Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guaranteeing Reliability through the Interconnection of Dispatchable Power Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal Energy Regulatory Commission to reform the interconnection queue process for the prioritization and approval of certain projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:35:01Z"
    }
  ]
}
```
