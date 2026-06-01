# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/17?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/17
- Title: Proposing a balanced budget amendment to the Constitution of the United States.
- Congress: 119
- Bill type: HJRES
- Bill number: 17
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2026-02-27T23:41:17Z
- Update date including text: 2026-02-27T23:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/17",
    "number": "17",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
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
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:01:10Z",
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
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres17ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 17\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Obernolte (for himself and Mr. Weber of Texas ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing a balanced budget amendment to the Constitution of the United States.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. Total outlays for any fiscal year shall not exceed total receipts for that fiscal year, unless two-thirds of the whole number of each House of Congress shall provide by law for a specific excess of outlays over receipts by a rollcall vote. 2. Prior to each fiscal year, the President shall transmit to the Congress a proposed budget for the United States Government for that fiscal year in which total outlays do not exceed total receipts. 3. The Congress shall enforce and implement this article by appropriate legislation, which may rely on estimates of outlays and receipts. 4. Total receipts shall include all receipts of the United States Government except those derived from borrowing. Total outlays shall include all outlays of the United States Government except for those for repayment of debt principal. 5. This article shall take effect beginning with the fifth fiscal year beginning after its ratification. .",
      "versionDate": "2025-01-13",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "11",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified.",
      "type": "HJRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "10",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Budget deficits and national debt",
            "updateDate": "2025-02-03T17:15:35Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-02-03T17:15:35Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-02-03T17:15:35Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-02-03T17:15:35Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-02-03T17:15:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-27T23:02:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hjres17",
          "measure-number": "17",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-01-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres17v00",
            "update-date": "2025-01-28"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds roll call vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing.</p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts. </p>"
        },
        "title": "Proposing a balanced budget amendment to the Constitution of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres17.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds roll call vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing.</p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts. </p>",
      "updateDate": "2025-01-28",
      "versionCode": "id119hjres17"
    },
    "title": "Proposing a balanced budget amendment to the Constitution of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds roll call vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing.</p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts. </p>",
      "updateDate": "2025-01-28",
      "versionCode": "id119hjres17"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres17ih.xml"
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
      "updateDate": "2025-01-14T09:33:16Z"
    },
    {
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-14T09:05:56Z"
    }
  ]
}
```
