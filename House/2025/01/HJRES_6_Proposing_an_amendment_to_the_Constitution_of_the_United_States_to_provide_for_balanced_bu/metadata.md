# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/6?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/6
- Title: Proposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government.
- Congress: 119
- Bill type: HJRES
- Bill number: 6
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-02-27T23:41:17Z
- Update date including text: 2026-02-27T23:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/6",
    "number": "6",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government.",
    "type": "HJRES",
    "updateDate": "2026-02-27T23:41:17Z",
    "updateDateIncludingText": "2026-02-27T23:41:17Z"
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
          "date": "2025-01-03T16:08:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres6ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 6\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. Total outlays for any fiscal year shall not exceed total receipts for that fiscal year, unless two-thirds of the whole number of each House of Congress shall provide by law for a specific excess of outlays over receipts by a rollcall vote. 2. Prior to each fiscal year, the President shall transmit to the Congress a proposed budget for the United States Government for that fiscal year in which total outlays do not exceed total receipts. 3. The Congress may waive the provisions of this article for any fiscal year in which a declaration of war is in effect by a rollcall vote. 4. The Congress may waive the provisions of this article for any fiscal year in which a declaration of national emergency is in effect, as so declared by a joint resolution, adopted by a majority of the whole number of each House, which becomes law. 5. The Congress may waive the provisions of this article for any fiscal year in which a declaration of a natural disaster is in effect, as so declared by a joint resolution, adopted by a majority of the whole number of each House, which becomes law. 6. The Congress shall enforce and implement this article by appropriate legislation, which may rely on estimates of outlays and receipts. 7. This article shall take effect beginning with the fifth fiscal year beginning after its ratification. .",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Budget deficits and national debt",
            "updateDate": "2025-01-15T18:39:18Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:39:18Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:39:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-14T16:52:20Z"
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
          "measure-id": "id119hjres6",
          "measure-number": "6",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres6v00",
            "update-date": "2025-01-15"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds roll call vote of each chamber. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays for the fiscal year do not exceed total receipts. </p> <p>Congress may waive the requirements for any fiscal year in which (1) a declaration of war is in effect by a roll call vote, or (2) a declaration of a natural disaster or a national emergency is in effect that was declared by a joint resolution that became law after being adopted by a majority of each chamber of Congress. </p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres6.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds roll call vote of each chamber. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays for the fiscal year do not exceed total receipts. </p> <p>Congress may waive the requirements for any fiscal year in which (1) a declaration of war is in effect by a roll call vote, or (2) a declaration of a natural disaster or a national emergency is in effect that was declared by a joint resolution that became law after being adopted by a majority of each chamber of Congress. </p>",
      "updateDate": "2025-01-15",
      "versionCode": "id119hjres6"
    },
    "title": "Proposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds roll call vote of each chamber. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays for the fiscal year do not exceed total receipts. </p> <p>Congress may waive the requirements for any fiscal year in which (1) a declaration of war is in effect by a roll call vote, or (2) a declaration of a natural disaster or a national emergency is in effect that was declared by a joint resolution that became law after being adopted by a majority of each chamber of Congress. </p>",
      "updateDate": "2025-01-15",
      "versionCode": "id119hjres6"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres6ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to provide for balanced budgets for the Government.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:45Z"
    }
  ]
}
```
