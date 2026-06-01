# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/94?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/94
- Title: A joint resolution proposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns.
- Congress: 119
- Bill type: SJRES
- Bill number: 94
- Origin chamber: Senate
- Introduced date: 2025-10-29
- Update date: 2025-11-03T15:12:26Z
- Update date including text: 2025-11-03T15:12:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-29: Introduced in Senate
- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-29: Introduced in Senate

## Actions

- 2025-10-29 - IntroReferral: Introduced in Senate
- 2025-10-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-29",
    "latestAction": {
      "actionDate": "2025-10-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/94",
    "number": "94",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "A joint resolution proposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns.",
    "type": "SJRES",
    "updateDate": "2025-11-03T15:12:26Z",
    "updateDateIncludingText": "2025-11-03T15:12:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-29",
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
          "date": "2025-10-29T20:26:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres94is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 94\nIN THE SENATE OF THE UNITED STATES\nOctober 29, 2025 Mr. Graham introduced the following joint resolution; which was read twice and referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. For any period during which there is a lapse in appropriations as a result of a failure to enact regular or continuing appropriations for one or more Federal agencies or departments, a Member of Congress shall forfeit and not receive any compensation for the services of the Member during such period. 2. Amounts forfeited under section 1 shall be transferred to the general fund of the Treasury to be used to reduce the Federal debt. 3. Congress shall have the power to enforce this article by appropriate legislation. .",
      "versionDate": "2025-10-29",
      "versionType": "IS"
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
        "updateDate": "2025-11-03T14:38:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-29",
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
          "measure-id": "id119sjres94",
          "measure-number": "94",
          "measure-type": "sjres",
          "orig-publish-date": "2025-10-29",
          "originChamber": "SENATE",
          "update-date": "2025-11-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres94v00",
            "update-date": "2025-11-03"
          },
          "action-date": "2025-10-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment that requires Members of Congress to forfeit their compensation during a government shutdown.\u00a0</p><p>Specifically, the amendment provides that Members of Congress must forfeit (and may not receive) any compensation for their services during any period in which there is a lapse in appropriations as a result of a failure to enact regular or continuing appropriations for one or more federal agencies or departments (i.e., government shutdown).</p><p>Any funds that are forfeited under the amendment must be transferred to the Treasury and used to reduce the federal debt.\u00a0</p>"
        },
        "title": "A joint resolution proposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres94.xml",
    "summary": {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution proposes a constitutional amendment that requires Members of Congress to forfeit their compensation during a government shutdown.\u00a0</p><p>Specifically, the amendment provides that Members of Congress must forfeit (and may not receive) any compensation for their services during any period in which there is a lapse in appropriations as a result of a failure to enact regular or continuing appropriations for one or more federal agencies or departments (i.e., government shutdown).</p><p>Any funds that are forfeited under the amendment must be transferred to the Treasury and used to reduce the federal debt.\u00a0</p>",
      "updateDate": "2025-11-03",
      "versionCode": "id119sjres94"
    },
    "title": "A joint resolution proposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns."
  },
  "summaries": [
    {
      "actionDate": "2025-10-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution proposes a constitutional amendment that requires Members of Congress to forfeit their compensation during a government shutdown.\u00a0</p><p>Specifically, the amendment provides that Members of Congress must forfeit (and may not receive) any compensation for their services during any period in which there is a lapse in appropriations as a result of a failure to enact regular or continuing appropriations for one or more federal agencies or departments (i.e., government shutdown).</p><p>Any funds that are forfeited under the amendment must be transferred to the Treasury and used to reduce the federal debt.\u00a0</p>",
      "updateDate": "2025-11-03",
      "versionCode": "id119sjres94"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres94is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution proposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-31T04:18:15Z"
    },
    {
      "title": "A joint resolution proposing an amendment to the Constitution of the United States requiring Members of Congress to forfeit their compensation during Government shutdowns.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T10:56:16Z"
    }
  ]
}
```
