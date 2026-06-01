# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/888?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/888
- Title: Stop Sports Blackouts Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 888
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-04-24T08:07:19Z
- Update date including text: 2026-04-24T08:07:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/888",
    "number": "888",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Stop Sports Blackouts Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-24T08:07:19Z",
    "updateDateIncludingText": "2026-04-24T08:07:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:08:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NJ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "OR"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "RI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr888ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 888\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Ryan (for himself, Mrs. McIver , Mr. Carson , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to direct the Federal Communications Commission to promulgate regulations with respect to rebates for certain video programming blackouts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Sports Blackouts Act of 2025 .\n#### 2. Rebates for video programming blackouts\nTitle VII of the Communications Act of 1934 ( 47 U.S.C. 601 et seq. ) is amended by adding at the end the following:\n723. Rebates for video programming blackouts (a) In general Not later than 90 days after the date of the enactment of this section, the Commission shall promulgate regulations\u2014 (1) to require a provider to issue to a subscriber of such provider a rebate with respect to any period during which the provider denies such subscriber, as a result of a covered negotiation, access to video programming that such provider agreed, at the time of subscription entry or renewal (as the case may be), to provide to such subscriber during such period; and (2) to establish the appropriate amount of a rebate issued under paragraph (1). (b) Definitions In this section: (1) Covered negotiation The term covered negotiation means a negotiation with respect to\u2014 (A) retransmission consent of a television broadcast station under section 325(b); or (B) carriage of video programming of an entity that is not a television broadcast station. (2) Provider The term provider means either of the following: (A) A cable operator (as defined in section 602). (B) A provider of direct broadcast satellite service (as defined in section 335(b)(5)). (3) Television broadcast station The term television broadcast station has the meaning given such term in section 325(b)(7). (4) Video programming The term video programming has the meaning given such term in section 602. .",
      "versionDate": "2025-01-31",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "328",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Sports Blackouts Act",
      "type": "S"
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
        "updateDate": "2025-03-04T17:11:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr888",
          "measure-number": "888",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr888v00",
            "update-date": "2025-03-13"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Sports Blackouts Act of 2025</strong></p><p>This bill requires cable and satellite broadcast providers to issue rebates to customers who are denied access to video programming included in their subscription because of programming negotiations.\u00a0</p><p>Specifically, where a provider\u2019s negotiations related to the retransmission or carriage of video programming result in the provider failing to offer access to programming included in a customer\u2019s subscription, the customer must be issued a rebate for the affected period. The Federal Communications Commission is directed to issue rules to this effect, including to establish the appropriate amount for such a rebate. \u00a0</p>"
        },
        "title": "Stop Sports Blackouts Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr888.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Sports Blackouts Act of 2025</strong></p><p>This bill requires cable and satellite broadcast providers to issue rebates to customers who are denied access to video programming included in their subscription because of programming negotiations.\u00a0</p><p>Specifically, where a provider\u2019s negotiations related to the retransmission or carriage of video programming result in the provider failing to offer access to programming included in a customer\u2019s subscription, the customer must be issued a rebate for the affected period. The Federal Communications Commission is directed to issue rules to this effect, including to establish the appropriate amount for such a rebate. \u00a0</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr888"
    },
    "title": "Stop Sports Blackouts Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Sports Blackouts Act of 2025</strong></p><p>This bill requires cable and satellite broadcast providers to issue rebates to customers who are denied access to video programming included in their subscription because of programming negotiations.\u00a0</p><p>Specifically, where a provider\u2019s negotiations related to the retransmission or carriage of video programming result in the provider failing to offer access to programming included in a customer\u2019s subscription, the customer must be issued a rebate for the affected period. The Federal Communications Commission is directed to issue rules to this effect, including to establish the appropriate amount for such a rebate. \u00a0</p>",
      "updateDate": "2025-03-13",
      "versionCode": "id119hr888"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr888ih.xml"
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
      "title": "Stop Sports Blackouts Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Sports Blackouts Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Communications Act of 1934 to direct the Federal Communications Commission to promulgate regulations with respect to rebates for certain video programming blackouts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:30Z"
    }
  ]
}
```
