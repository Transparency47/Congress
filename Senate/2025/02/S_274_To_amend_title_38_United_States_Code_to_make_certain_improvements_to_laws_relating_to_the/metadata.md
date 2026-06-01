# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/274?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/274
- Title: Next of Kin Collections Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 274
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2025-03-11T16:50:41Z
- Update date including text: 2025-03-11T16:50:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/274",
    "number": "274",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Next of Kin Collections Protection Act of 2025",
    "type": "S",
    "updateDate": "2025-03-11T16:50:41Z",
    "updateDateIncludingText": "2025-03-11T16:50:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T19:32:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s274is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 274\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Daines (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to laws relating to the payment of certain benefits administered by the Secretary of Veterans Affairs that are affected by death, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Next of Kin Collections Protection Act of 2025 .\n#### 2. Payment by Secretary of Veterans Affairs of certain benefits affected by death\n##### (a) Effective date of certain reductions and discontinuances of compensation, dependency and indemnity compensation, and pension under laws administered by Secretary of Veterans Affairs\n**(1) In general**\nSection 5112(b) of title 38, United States Code, is amended\u2014\n**(A)**\nin paragraph (1), by inserting (except in the case of a pension under an existing rating or decision), after death of a payee ;\n**(B)**\nby redesignating paragraphs (3) through (10) as paragraphs (4) through (11), respectively; and\n**(C)**\nby inserting, after paragraph (2), the following new paragraph (3):\n(3) by reason of death of a payee in the case of a pension under an existing rating or decision, shall be the last day of the month in which such death occurs; .\n**(2) Conforming amendment**\nSection 1832(b)(4) of such title is amended by striking paragraphs (1), (6), (9), and (10) and inserting paragraphs (1), (7), (10), and (11) .\n##### (b) Payment of benefits for month of death\nSection 5310(b) of title 38, United States Code, is amended by inserting , or in the case of a payment for the month of the death of a payee under section 5112(b)(2) of this title, before an amount equal .\n##### (c) Effective date\nThe amendments to title 38, United States Code, made by this section shall apply with respect to a payment of a benefit affected by a death that occurs on or after the date of the enactment of this Act.",
      "versionDate": "2025-02-28",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T21:13:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119s274",
          "measure-number": "274",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s274v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Next of Kin Collections Protection Act of 2025</strong></p><p>This bill modifies the effective date of a reduction or discontinuance of a Department of Veterans Affairs pension under an existing rating or decision in cases where the payee has died. Specifically, the bill provides that the effective date of a reduction or discontinuance of a pension that is under an existing rating or decision must be the last day of the month in which the death of the payee occurs.</p>"
        },
        "title": "Next of Kin Collections Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s274.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Next of Kin Collections Protection Act of 2025</strong></p><p>This bill modifies the effective date of a reduction or discontinuance of a Department of Veterans Affairs pension under an existing rating or decision in cases where the payee has died. Specifically, the bill provides that the effective date of a reduction or discontinuance of a pension that is under an existing rating or decision must be the last day of the month in which the death of the payee occurs.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s274"
    },
    "title": "Next of Kin Collections Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Next of Kin Collections Protection Act of 2025</strong></p><p>This bill modifies the effective date of a reduction or discontinuance of a Department of Veterans Affairs pension under an existing rating or decision in cases where the payee has died. Specifically, the bill provides that the effective date of a reduction or discontinuance of a pension that is under an existing rating or decision must be the last day of the month in which the death of the payee occurs.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s274"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s274is.xml"
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
      "title": "Next of Kin Collections Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Next of Kin Collections Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to make certain improvements to laws relating to the payment of certain benefits administered by the Secretary of Veterans Affairs that are affected by death, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:28Z"
    }
  ]
}
```
