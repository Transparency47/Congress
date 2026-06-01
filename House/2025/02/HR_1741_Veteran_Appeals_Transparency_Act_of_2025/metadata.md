# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1741
- Title: Veteran Appeals Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1741
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-07-24T14:39:49Z
- Update date including text: 2025-07-24T14:39:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1741",
    "number": "1741",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Veteran Appeals Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-24T14:39:49Z",
    "updateDateIncludingText": "2025-07-24T14:39:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T17:59:51Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1741ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1741\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Self introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the online publication of the docket of the Board of Veterans\u2019 Appeals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Appeals Transparency Act of 2025 .\n#### 2. Board of Veterans\u2019 Appeals publication of dates of docket activity\nSection 7107 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(f) Publication of expected actions (1) On a weekly basis, for each docket, the Board shall publish, on a website of the Department, notice of the docket dates of the cases assigned to a Board member for a decision for that week. (2) Each notice published under paragraph (1) shall include a statement that an assignment described in such paragraph does not require the Board to issue a decision regarding the case during such week. (3) Paragraph (1) shall not apply to a case\u2014 (A) that has been advanced under subsection (b); or (B) remanded by the United States Court of Appeals for Veterans Claims. .",
      "versionDate": "2025-02-27",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:07:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1741",
          "measure-number": "1741",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-07-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1741v00",
            "update-date": "2025-07-24"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veteran Appeals Transparency Act of 2025</strong></p><p>This bill requires the Board of Veterans Appeals to publish a weekly notice of the docket dates of the cases assigned to a board member for a decision that week. The requirement does not apply to cases that have been advanced or remanded. The notice must include a statement that a case assignment appearing on the notice does not require the board to issue a decision regarding the case during that week.</p>"
        },
        "title": "Veteran Appeals Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1741.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran Appeals Transparency Act of 2025</strong></p><p>This bill requires the Board of Veterans Appeals to publish a weekly notice of the docket dates of the cases assigned to a board member for a decision that week. The requirement does not apply to cases that have been advanced or remanded. The notice must include a statement that a case assignment appearing on the notice does not require the board to issue a decision regarding the case during that week.</p>",
      "updateDate": "2025-07-24",
      "versionCode": "id119hr1741"
    },
    "title": "Veteran Appeals Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran Appeals Transparency Act of 2025</strong></p><p>This bill requires the Board of Veterans Appeals to publish a weekly notice of the docket dates of the cases assigned to a board member for a decision that week. The requirement does not apply to cases that have been advanced or remanded. The notice must include a statement that a case assignment appearing on the notice does not require the board to issue a decision regarding the case during that week.</p>",
      "updateDate": "2025-07-24",
      "versionCode": "id119hr1741"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1741ih.xml"
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
      "title": "Veteran Appeals Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran Appeals Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the online publication of the docket of the Board of Veterans' Appeals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:24Z"
    }
  ]
}
```
