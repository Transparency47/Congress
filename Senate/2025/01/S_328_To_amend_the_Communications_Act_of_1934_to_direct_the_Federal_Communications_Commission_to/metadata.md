# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/328?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/328
- Title: Stop Sports Blackouts Act
- Congress: 119
- Bill type: S
- Bill number: 328
- Origin chamber: Senate
- Introduced date: 2025-01-30
- Update date: 2025-05-27T14:12:53Z
- Update date including text: 2025-05-27T14:12:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-30: Introduced in Senate
- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-01-30: Introduced in Senate

## Actions

- 2025-01-30 - IntroReferral: Introduced in Senate
- 2025-01-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-30",
    "latestAction": {
      "actionDate": "2025-01-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/328",
    "number": "328",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Stop Sports Blackouts Act",
    "type": "S",
    "updateDate": "2025-05-27T14:12:53Z",
    "updateDateIncludingText": "2025-05-27T14:12:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-30",
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
          "date": "2025-01-30T17:43:08Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s328is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 328\nIN THE SENATE OF THE UNITED STATES\nJanuary 30, 2025 Mr. Murphy introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Communications Act of 1934 to direct the Federal Communications Commission to promulgate regulations with respect to rebates for certain video programming blackouts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Sports Blackouts Act .\n#### 2. Rebates for video programming blackouts\nTitle VII of the Communications Act of 1934 ( 47 U.S.C. 601 et seq. ) is amended by adding at the end the following:\n723. Rebates for video programming blackouts (a) Definitions In this section: (1) Covered negotiation The term covered negotiation means a negotiation with respect to\u2014 (A) retransmission consent of a television broadcast station under section 325(b); or (B) carriage of video programming of an entity that is not a television broadcast station. (2) Provider The term provider means either of the following: (A) A cable operator, as defined in section 602. (B) A provider of direct broadcast satellite service, as defined in section 335(b)(5). (3) Television broadcast station The term television broadcast station has the meaning given the term in section 325(b)(7). (4) Video programming The term video programming has the meaning given the term in section 602. (b) Promulgation of regulations Not later than 90 days after the date of enactment of this section, the Commission shall promulgate regulations\u2014 (1) to require a provider to issue to a subscriber of that provider a rebate with respect to any period during which the provider denies that subscriber, as a result of a covered negotiation, access to video programming that such provider agreed, at the time of subscription entry or renewal (as applicable), to provide to that subscriber during that period; and (2) to establish the appropriate amount of a rebate issued under paragraph (1). .",
      "versionDate": "2025-01-30",
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
        "actionDate": "2025-01-31",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "888",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Sports Blackouts Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-03T17:30:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-30",
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
          "measure-id": "id119s328",
          "measure-number": "328",
          "measure-type": "s",
          "orig-publish-date": "2025-01-30",
          "originChamber": "SENATE",
          "update-date": "2025-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s328v00",
            "update-date": "2025-03-13"
          },
          "action-date": "2025-01-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Sports Blackouts Act</strong></p><p>This bill requires cable and satellite broadcast providers to issue rebates to customers who are denied access to video programming included in their subscription because of programming negotiations.\u00a0</p><p>Specifically, where a provider\u2019s negotiations related to the retransmission or carriage of video programming result in the provider failing to offer access to programming included in a customer\u2019s subscription, the customer must be issued a rebate for the affected period. The Federal Communications Commission is directed to issue rules to this effect, including to establish the appropriate amount for such a rebate. \u00a0</p>"
        },
        "title": "Stop Sports Blackouts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s328.xml",
    "summary": {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Sports Blackouts Act</strong></p><p>This bill requires cable and satellite broadcast providers to issue rebates to customers who are denied access to video programming included in their subscription because of programming negotiations.\u00a0</p><p>Specifically, where a provider\u2019s negotiations related to the retransmission or carriage of video programming result in the provider failing to offer access to programming included in a customer\u2019s subscription, the customer must be issued a rebate for the affected period. The Federal Communications Commission is directed to issue rules to this effect, including to establish the appropriate amount for such a rebate. \u00a0</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119s328"
    },
    "title": "Stop Sports Blackouts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Sports Blackouts Act</strong></p><p>This bill requires cable and satellite broadcast providers to issue rebates to customers who are denied access to video programming included in their subscription because of programming negotiations.\u00a0</p><p>Specifically, where a provider\u2019s negotiations related to the retransmission or carriage of video programming result in the provider failing to offer access to programming included in a customer\u2019s subscription, the customer must be issued a rebate for the affected period. The Federal Communications Commission is directed to issue rules to this effect, including to establish the appropriate amount for such a rebate. \u00a0</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119s328"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s328is.xml"
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
      "title": "Stop Sports Blackouts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Sports Blackouts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Communications Act of 1934 to direct the Federal Communications Commission to promulgate regulations with respect to rebates for certain video programming blackouts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:19Z"
    }
  ]
}
```
