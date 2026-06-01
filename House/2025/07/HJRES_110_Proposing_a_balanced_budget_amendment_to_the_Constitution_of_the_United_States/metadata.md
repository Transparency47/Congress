# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/110
- Title: Proposing a balanced budget amendment to the Constitution of the United States.
- Congress: 119
- Bill type: HJRES
- Bill number: 110
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-02-27T23:41:17Z
- Update date including text: 2026-02-27T23:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/110",
    "number": "110",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
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
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:09:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres110ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 110\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Moran submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing a balanced budget amendment to the Constitution of the United States.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. Expenditures and receipts shall be balanced, which may occur over more than one year. Expenditures shall include all expenditures of the United States except those for payment of debt, and receipts shall include all receipts of the United States except those derived from borrowing. Congress shall achieve balance within ten years following the ratification of this article. 2. For emergency situations, two-thirds of the House of Representatives and the Senate may for limited times authorize expenditures exceeding those pursuant to rules established under section 1. Debts incurred from such expenditures shall be paid as soon as practicable. .",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-15T17:41:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hjres110",
          "measure-number": "110",
          "measure-type": "hjres",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-09-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres110v00",
            "update-date": "2025-09-15"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment that requires federal expenditures and receipts to be balanced, which may occur over more than one year. </p> <p>Under the amendment, expenditures include all federal expenditures except those for payment of debt. Receipts do not include receipts derived from borrowing. </p> <p>The amendment requires Congress to achieve balance within 10 years of the ratification of the amendment.</p> <p>In an emergency situation, two-thirds of the House of Representatives and the Senate may authorize additional expenditures that are not otherwise permitted by the amendment. The additional expenditures must be for a limited time, and debts incurred from the expenditures must be paid as soon as practicable.</p>"
        },
        "title": "Proposing a balanced budget amendment to the Constitution of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres110.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that requires federal expenditures and receipts to be balanced, which may occur over more than one year. </p> <p>Under the amendment, expenditures include all federal expenditures except those for payment of debt. Receipts do not include receipts derived from borrowing. </p> <p>The amendment requires Congress to achieve balance within 10 years of the ratification of the amendment.</p> <p>In an emergency situation, two-thirds of the House of Representatives and the Senate may authorize additional expenditures that are not otherwise permitted by the amendment. The additional expenditures must be for a limited time, and debts incurred from the expenditures must be paid as soon as practicable.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hjres110"
    },
    "title": "Proposing a balanced budget amendment to the Constitution of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that requires federal expenditures and receipts to be balanced, which may occur over more than one year. </p> <p>Under the amendment, expenditures include all federal expenditures except those for payment of debt. Receipts do not include receipts derived from borrowing. </p> <p>The amendment requires Congress to achieve balance within 10 years of the ratification of the amendment.</p> <p>In an emergency situation, two-thirds of the House of Representatives and the Senate may authorize additional expenditures that are not otherwise permitted by the amendment. The additional expenditures must be for a limited time, and debts incurred from the expenditures must be paid as soon as practicable.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hjres110"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres110ih.xml"
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
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T04:48:35Z"
    },
    {
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T08:06:46Z"
    }
  ]
}
```
