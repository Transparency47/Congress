# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/8?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/8
- Title: Proposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President.
- Congress: 119
- Bill type: HJRES
- Bill number: 8
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-14T17:40:04Z
- Update date including text: 2025-01-14T17:40:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/8",
    "number": "8",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President.",
    "type": "HJRES",
    "updateDate": "2025-01-14T17:40:04Z",
    "updateDateIncludingText": "2025-01-14T17:40:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:23:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres8ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 8\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. McClintock (for himself and Mr. Weber of Texas ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. In approving and signing a bill or joint resolution that is presented under section 7 of article I, the President may reduce an appropriation in such bill or joint resolution, and such bill or joint resolution shall become law with such reduction incorporated. 2. If the President reduces an appropriation under section 1 of this article\u2014 (1) not later than 10 days after the date of such reduction, the President shall notify the House of Representatives and the Senate of such reduction; (2) the House of Representatives and the Senate may consider disapproval of such reduction; and (3) if two-thirds of each House votes to disapprove of such reduction, the amount of the appropriation in law subject to such reduction shall be treated as returned to the amount originally presented to the President under section 1. .",
      "versionDate": "2025-01-03",
      "versionType": "IH"
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-14T16:22:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hjres8",
          "measure-number": "8",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres8v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment that authorizes the President to use a line item veto to reduce an appropriation in a bill or joint resolution. </p> <p>Under the amendment, the President must notify Congress within 10 days of using this authority to reduce an appropriation. The House and Senate may then consider disapproval of the reduction. </p> <p>If at least two-thirds of each chamber of Congress votes to disapprove the reduction, the amount of the appropriation that is subject to the reduction must be returned to the amount that was originally presented to the President. </p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres8.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that authorizes the President to use a line item veto to reduce an appropriation in a bill or joint resolution. </p> <p>Under the amendment, the President must notify Congress within 10 days of using this authority to reduce an appropriation. The House and Senate may then consider disapproval of the reduction. </p> <p>If at least two-thirds of each chamber of Congress votes to disapprove the reduction, the amount of the appropriation that is subject to the reduction must be returned to the amount that was originally presented to the President. </p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres8"
    },
    "title": "Proposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that authorizes the President to use a line item veto to reduce an appropriation in a bill or joint resolution. </p> <p>Under the amendment, the President must notify Congress within 10 days of using this authority to reduce an appropriation. The House and Senate may then consider disapproval of the reduction. </p> <p>If at least two-thirds of each chamber of Congress votes to disapprove the reduction, the amount of the appropriation that is subject to the reduction must be returned to the amount that was originally presented to the President. </p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres8"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres8ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Proposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to provide certain line item veto authority to the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:39Z"
    }
  ]
}
```
