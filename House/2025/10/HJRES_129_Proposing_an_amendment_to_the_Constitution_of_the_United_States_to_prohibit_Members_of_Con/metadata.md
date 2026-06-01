# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/129
- Title: Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect.
- Congress: 119
- Bill type: HJRES
- Bill number: 129
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-12-05T21:27:06Z
- Update date including text: 2025-12-05T21:27:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/129",
    "number": "129",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect.",
    "type": "HJRES",
    "updateDate": "2025-12-05T21:27:06Z",
    "updateDateIncludingText": "2025-12-05T21:27:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:33:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres129ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 129\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mr. Van Orden submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. A Representative or Senator may not receive compensation with respect to any period during which a Government shutdown is in effect. For purposes of this article, a Government shutdown shall be considered to be in effect if there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution. 2. Congress shall have the power to enforce this article through appropriate legislation. .",
      "versionDate": "2025-10-03",
      "versionType": "IH"
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
        "actionDate": "2025-09-30",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "128",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect.",
      "type": "HJRES"
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
        "name": "Congress",
        "updateDate": "2025-10-06T16:42:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119hjres129",
          "measure-number": "129",
          "measure-type": "hjres",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2025-10-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres129v00",
            "update-date": "2025-10-06"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment that prohibits Members of Congress from receiving compensation for any period during which a government shutdown is in effect. Under the amendment, a government shutdown is considered to be in effect if there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres129.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that prohibits Members of Congress from receiving compensation for any period during which a government shutdown is in effect. Under the amendment, a government shutdown is considered to be in effect if there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p>",
      "updateDate": "2025-10-06",
      "versionCode": "id119hjres129"
    },
    "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect."
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that prohibits Members of Congress from receiving compensation for any period during which a government shutdown is in effect. Under the amendment, a government shutdown is considered to be in effect if there is a lapse in appropriations for any federal agency or department as a result of a failure to enact a regular appropriations bill or a continuing resolution.</p>",
      "updateDate": "2025-10-06",
      "versionCode": "id119hjres129"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres129ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T08:18:25Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation for any period during which a Government shutdown is in effect.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T08:05:52Z"
    }
  ]
}
```
