# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/78?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/78
- Title: TRUE Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 78
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/78",
    "number": "78",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "TRUE Accountability Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-13",
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
            "date": "2025-01-13T23:26:48Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-13T23:26:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s78is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 78\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Lankford introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require certain agencies to develop plans for internal control in the event of an emergency or crisis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taxpayer Resources Used in Emergencies Accountability Act or the TRUE Accountability Act .\n#### 2. OMB Guidance\n##### (a) Definitions\nIn this section:\n**(1) Covered agency**\nThe term covered agency means an agency described in section 901(b) of title 31, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(3) Internal control**\nThe term internal control means a process that is\u2014\n**(A)**\neffected by the management and other personnel of an entity; and\n**(B)**\ndesigned to provide reasonable assurance with respect to the achievement of objectives relating to\u2014\n**(i)**\neffectiveness and efficiency of operations;\n**(ii)**\nreliability of financial reporting; and\n**(iii)**\ncompliance with applicable law.\n##### (b) Guidance\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Director shall issue guidance to covered agencies for the development of plans for internal control that are ready or adaptable for immediate use in future emergencies or crises.\n**(2) Contents**\nThe guidance issued under paragraph (1) shall\u2014\n**(A)**\nbe in alignment with the documents of the Government Accountability Office entitled A Framework for Managing Improper Payments in Emergency Assistance Programs and A Framework for Managing Fraud Risks in Federal Programs ; and\n**(B)**\nrequire plans for internal control of covered agencies to include\u2014\n**(i)**\nthe identification of a senior official of the covered agency to be responsible and accountable for the implementation of the plan; and\n**(ii)**\npolicies and procedures to timely\u2014\n**(I)**\nassess the risks of improper payments and fraud relating to the implementation of any supplemental appropriation, or other increase in budget authority, that may be made available to the covered agency for a purpose relating to disaster relief or response to a public health or other emergency; and\n**(II)**\ndevelop and implement appropriate responses to the risks described in subclause (I), including any changes to internal controls, to ensure that, to the greatest extent possible, appropriate controls are in place prior to the expenditure of funds.\n**(3) Review**\nNot later than 3 years after the date on which guidance is issued under paragraph (1), and not less frequently than once every 3 years thereafter, the Director shall review and, as necessary, revise the guidance.\n##### (c) Plan submission\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the head of each covered agency head shall submit to the Director the plan of the covered agency required under the guidance issued under subsection (b)(1).\n**(2) Revisions**\nNot later than 3 years after the date on which the head of a covered agency submits a plan under paragraph (1), and not less frequently than once every 3 years thereafter, the head of each covered agency shall\u2014\n**(A)**\nreview and, if necessary, revise the plan of the covered agency; and\n**(B)**\nsubmit to the Director any revised plan of the covered agency.\n**(3) Submission to Congress**\nNot later than 1 year after the date of the enactment of this Act, and not less frequently than annually thereafter, the Director shall submit to Congress, the Committee on Homeland Security and Governmental Affairs of the Senate, and the Committee on Oversight and Government Reform of the House of Representatives the plans submitted by covered agencies under this subsection.\n##### (d) Unavailability of judicial review\nA determination, finding, action, or omission under this section by the Director or the head of a covered agency shall not be subject to judicial review.\n##### (e) No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2025-01-13",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-13T16:20:54Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-03-13T16:20:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-13T16:20:49Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-13T16:21:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T19:14:39Z"
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
          "measure-id": "id119s78",
          "measure-number": "78",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s78v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Taxpayer Resources Used in Emergencies Accountability Act or the TRUE Accountability Act</strong></p><p>This bill requires the Office of Management and Budget (OMB) to issue guidance to certain executive branch agencies for the development of internal control plans that are available for immediate use in future emergencies or crises. (<em>Internal control</em> refers to a process that provides reasonable assurance of achieving effective and efficient operations, reliable financial reporting, and legal compliance.)</p><p>This guidance must be in alignment with the Government Accountability Office reports entitled <em>A Framework for Managing Improper Payments in Emergency Assistance Programs</em> and <em>A Framework for Managing Fraud Risks in Federal Programs</em>.\u00a0</p><p>Periodically, the agencies subject to this guidance must submit their internal control plan to\u00a0OMB and OMB must submit such agency plans to Congress.</p>"
        },
        "title": "TRUE Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s78.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Taxpayer Resources Used in Emergencies Accountability Act or the TRUE Accountability Act</strong></p><p>This bill requires the Office of Management and Budget (OMB) to issue guidance to certain executive branch agencies for the development of internal control plans that are available for immediate use in future emergencies or crises. (<em>Internal control</em> refers to a process that provides reasonable assurance of achieving effective and efficient operations, reliable financial reporting, and legal compliance.)</p><p>This guidance must be in alignment with the Government Accountability Office reports entitled <em>A Framework for Managing Improper Payments in Emergency Assistance Programs</em> and <em>A Framework for Managing Fraud Risks in Federal Programs</em>.\u00a0</p><p>Periodically, the agencies subject to this guidance must submit their internal control plan to\u00a0OMB and OMB must submit such agency plans to Congress.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119s78"
    },
    "title": "TRUE Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Taxpayer Resources Used in Emergencies Accountability Act or the TRUE Accountability Act</strong></p><p>This bill requires the Office of Management and Budget (OMB) to issue guidance to certain executive branch agencies for the development of internal control plans that are available for immediate use in future emergencies or crises. (<em>Internal control</em> refers to a process that provides reasonable assurance of achieving effective and efficient operations, reliable financial reporting, and legal compliance.)</p><p>This guidance must be in alignment with the Government Accountability Office reports entitled <em>A Framework for Managing Improper Payments in Emergency Assistance Programs</em> and <em>A Framework for Managing Fraud Risks in Federal Programs</em>.\u00a0</p><p>Periodically, the agencies subject to this guidance must submit their internal control plan to\u00a0OMB and OMB must submit such agency plans to Congress.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119s78"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s78is.xml"
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
      "title": "TRUE Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TRUE Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taxpayer Resources Used in Emergencies Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require certain agencies to develop plans for internal control in the event of an emergency or crisis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T03:03:29Z"
    }
  ]
}
```
