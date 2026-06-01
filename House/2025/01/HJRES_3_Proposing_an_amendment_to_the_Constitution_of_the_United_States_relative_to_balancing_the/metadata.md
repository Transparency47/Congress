# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/3?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/3
- Title: Proposing an amendment to the Constitution of the United States relative to balancing the budget.
- Congress: 119
- Bill type: HJRES
- Bill number: 3
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-06-12T08:06:42Z
- Update date including text: 2025-06-12T08:06:42Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/3",
    "number": "3",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States relative to balancing the budget.",
    "type": "HJRES",
    "updateDate": "2025-06-12T08:06:42Z",
    "updateDateIncludingText": "2025-06-12T08:06:42Z"
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
          "date": "2025-01-03T16:25:35Z",
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
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres3ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 3\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Buchanan submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States relative to balancing the budget.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. Total outlays for any fiscal year shall not exceed total receipts for that fiscal year, unless two-thirds of the duly chosen and sworn Members of each House of Congress shall provide by law for a specific excess of outlays over receipts by a rollcall vote. 2. Total outlays for any fiscal year shall not exceed 18 percent of the gross domestic product of the United States for the calendar year ending before the beginning of such fiscal year, unless two-thirds of the duly chosen and sworn Members of each House of Congress shall provide by law for a specific amount in excess of such 18 percent by a rollcall vote. 3. Prior to each fiscal year, the President shall transmit to the Congress a proposed budget for the United States Government for that fiscal year in which\u2014 (1) total outlays do not exceed total receipts; and (2) total outlays do not exceed 18 percent of the gross domestic product of the United States for the calendar year ending before the beginning of such fiscal year. 4. Any bill that imposes a new tax or increases the statutory rate of any tax or the aggregate amount of revenue may pass only by a two-thirds majority of the duly chosen and sworn Members of each House of Congress by a rollcall vote. For the purpose of determining any increase in revenue under this section, there shall be excluded any increase resulting from the lowering of the statutory rate of any tax. 5. The limit on the debt of the United States shall not be increased, unless three-fifths of the duly chosen and sworn Members of each House of Congress shall provide for such an increase by a rollcall vote. 6. The Congress may waive the provisions of sections 1, 2, 3, and 5 of this article for any fiscal year in which a declaration of war against a nation-state is in effect and in which a majority of the duly chosen and sworn Members of each House of Congress shall provide for a specific excess by a rollcall vote. 7. The Congress may waive the provisions of sections 1, 2, 3, and 5 of this article in any fiscal year in which the United States is engaged in a military conflict that causes an imminent and serious military threat to national security and is so declared by three-fifths of the duly chosen and sworn Members of each House of Congress by a rollcall vote. Such suspension must identify and be limited to the specific excess of outlays for that fiscal year made necessary by the identified military conflict. 8. No court of the United States or of any State shall order any increase in revenue to enforce this article. 9. Total receipts shall include all receipts of the United States Government except those derived from borrowing. Total outlays shall include all outlays of the United States Government except those for repayment of debt principal. 10. The Congress shall have power to enforce and implement this article by appropriate legislation, which may rely on estimates of outlays, receipts, and gross domestic product. 11. This article shall take effect beginning with the fifth fiscal year beginning after its ratification. .",
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
            "updateDate": "2025-01-15T18:39:42Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-01-15T18:39:42Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:39:42Z"
          },
          {
            "name": "Income tax rates",
            "updateDate": "2025-01-15T18:39:42Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:39:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-14T15:39:56Z"
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
          "measure-id": "id119hjres3",
          "measure-number": "3",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres3v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing. </p> <p>The amendment prohibits total outlays for any fiscal year from exceeding 18% of the gross domestic product of the United States unless two-thirds of each chamber of Congress provides for a specific increase above this amount. </p> <p>The amendment requires a two-thirds vote of each chamber of Congress to impose a new tax, increase the statutory rate of any tax, or increase the aggregate amount of revenue. It requires a three-fifths vote of each chamber to increase the limit on the debt of the United States. </p> <p>The President must submit an annual budget in which total outlays do not exceed total receipts or 18% of the gross domestic product of the United States. </p> <p>The amendment prohibits a court from ordering a revenue increase to enforce the requirements. </p> <p>Congress may waive specified requirements when a declaration of war is in effect or the United States is engaged in a military conflict that causes an imminent and serious military threat to national security. </p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States relative to balancing the budget."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres3.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing. </p> <p>The amendment prohibits total outlays for any fiscal year from exceeding 18% of the gross domestic product of the United States unless two-thirds of each chamber of Congress provides for a specific increase above this amount. </p> <p>The amendment requires a two-thirds vote of each chamber of Congress to impose a new tax, increase the statutory rate of any tax, or increase the aggregate amount of revenue. It requires a three-fifths vote of each chamber to increase the limit on the debt of the United States. </p> <p>The President must submit an annual budget in which total outlays do not exceed total receipts or 18% of the gross domestic product of the United States. </p> <p>The amendment prohibits a court from ordering a revenue increase to enforce the requirements. </p> <p>Congress may waive specified requirements when a declaration of war is in effect or the United States is engaged in a military conflict that causes an imminent and serious military threat to national security. </p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres3"
    },
    "title": "Proposing an amendment to the Constitution of the United States relative to balancing the budget."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless Congress authorizes the excess by a two-thirds vote of each chamber. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing. </p> <p>The amendment prohibits total outlays for any fiscal year from exceeding 18% of the gross domestic product of the United States unless two-thirds of each chamber of Congress provides for a specific increase above this amount. </p> <p>The amendment requires a two-thirds vote of each chamber of Congress to impose a new tax, increase the statutory rate of any tax, or increase the aggregate amount of revenue. It requires a three-fifths vote of each chamber to increase the limit on the debt of the United States. </p> <p>The President must submit an annual budget in which total outlays do not exceed total receipts or 18% of the gross domestic product of the United States. </p> <p>The amendment prohibits a court from ordering a revenue increase to enforce the requirements. </p> <p>Congress may waive specified requirements when a declaration of war is in effect or the United States is engaged in a military conflict that causes an imminent and serious military threat to national security. </p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres3"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres3ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States relative to balancing the budget.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States relative to balancing the budget.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:26Z"
    }
  ]
}
```
