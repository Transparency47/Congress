# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/415?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/415
- Title: Stop Act
- Congress: 119
- Bill type: HR
- Bill number: 415
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-03-21T14:15:52Z
- Update date including text: 2025-03-21T14:15:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/415",
    "number": "415",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001296",
        "district": "2",
        "firstName": "Brendan",
        "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
        "lastName": "Boyle",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Stop Act",
    "type": "HR",
    "updateDate": "2025-03-21T14:15:52Z",
    "updateDateIncludingText": "2025-03-21T14:15:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr415ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 415\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Boyle of Pennsylvania introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prohibit individuals holding Federal office from directly soliciting contributions to or on behalf of any political committee under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Act .\n#### 2. Prohibiting direct solicitation of campaign contributions or funds for Federal election activity by Federal officeholders\n##### (a) Prohibition\nSection 323(e) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30125(e) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (2) through (4) as paragraphs (3) through (5), respectively; and\n**(2)**\nby inserting after paragraph (1) the following new paragraph:\n(2) Prohibiting direct solicitations for Federal election purposes by Federal officeholders (A) Prohibition In addition to the prohibitions on soliciting funds set forth under paragraph (1), an individual holding Federal office shall not solicit funds directly from any person\u2014 (i) for or on behalf of any political committee; or (ii) for or on behalf of any person for use for Federal election activity (as defined in section 301(20)). (B) Rule of construction regarding participation in fundraising events Nothing in this paragraph may be construed to prohibit an individual holding Federal office from participating in a fundraising event, including planning or attending the event, speaking at the event, or serving as a featured guest at the event, so long as the individual does not engage in any written or verbal solicitation of funds in connection with the event. .\n##### (b) Conforming amendment relating to attendance at State and local political party fundraising events\nSection 323(e)(4) of such Act ( 52 U.S.C. 30125(e)(4) ), as redesignated by subsection (a)(1), is amended\u2014\n**(1)**\nby striking Notwithstanding paragraph (1) or subsection (b)(2)(C), and inserting Notwithstanding paragraph (1), paragraph (2), or subsection (b)(2)(C), ; and\n**(2)**\nby striking the period at the end and inserting the following: , so long as, in the case of an individual holding Federal office, the individual does not engage in any written or verbal solicitation of funds in connection with the event. .\n#### 3. Effective date\nThe amendments made by this Act shall apply with respect to solicitations made on or after the date of the enactment of this Act.",
      "versionDate": "2025-01-15",
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
        "item": {
          "name": "Elections, voting, political campaign regulation",
          "updateDate": "2025-02-19T21:20:40Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-15T14:33:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr415",
          "measure-number": "415",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr415v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Act</strong></p><p>This bill prohibits federal officeholders from directly soliciting contributions for certain federal election purposes.\u00a0</p><p>Specifically, the bill prohibits a federal officeholder from soliciting funds directly from any person (1) for or on behalf of any political committee, or (2) for or on the behalf of any person for use for federal election activity. However, a federal officeholder may participate in a fundraising event (e.g., planning, attending, or speaking at an event), as long as the federal officeholder does not engage in any written or verbal solicitation of funds in connection with the event.</p>"
        },
        "title": "Stop Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr415.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Act</strong></p><p>This bill prohibits federal officeholders from directly soliciting contributions for certain federal election purposes.\u00a0</p><p>Specifically, the bill prohibits a federal officeholder from soliciting funds directly from any person (1) for or on behalf of any political committee, or (2) for or on the behalf of any person for use for federal election activity. However, a federal officeholder may participate in a fundraising event (e.g., planning, attending, or speaking at an event), as long as the federal officeholder does not engage in any written or verbal solicitation of funds in connection with the event.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr415"
    },
    "title": "Stop Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Act</strong></p><p>This bill prohibits federal officeholders from directly soliciting contributions for certain federal election purposes.\u00a0</p><p>Specifically, the bill prohibits a federal officeholder from soliciting funds directly from any person (1) for or on behalf of any political committee, or (2) for or on the behalf of any person for use for federal election activity. However, a federal officeholder may participate in a fundraising event (e.g., planning, attending, or speaking at an event), as long as the federal officeholder does not engage in any written or verbal solicitation of funds in connection with the event.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr415"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr415ih.xml"
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
      "title": "Stop Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T10:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to prohibit individuals holding Federal office from directly soliciting contributions to or on behalf of any political committee under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T10:48:15Z"
    }
  ]
}
```
