# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/11?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/11
- Title: .Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified.
- Congress: 119
- Bill type: HJRES
- Bill number: 11
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-27T08:07:25Z
- Update date including text: 2025-03-27T08:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/11",
    "number": "11",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified.",
    "type": "HJRES",
    "updateDate": "2025-03-27T08:07:25Z",
    "updateDateIncludingText": "2025-03-27T08:07:25Z"
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
          "date": "2025-01-03T16:21:30Z",
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
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MT"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres11ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 11\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Perry (for himself, Mr. Cloud , Mr. Ogles , and Mr. Zinke ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing a balanced budget amendment to the Constitution requiring that each agency and department\u2019s funding is justified.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. Total outlays for any fiscal year shall not exceed total receipts for that fiscal year, unless three-fifths of the whole number of each House of Congress shall provide by law for a specific excess of outlays over receipts by a rollcall vote, but in no event shall total outlays for any fiscal year exceed the following: for the first fiscal year for which this article takes effect, 20 percent of the estimated gross domestic product of the United States for that year, and for each subsequent fiscal year, a percentage of the estimated gross domestic product equal to the applicable percentage for the preceding fiscal year reduced by .1 percentage point. Under this section, total spending for any fiscal year is not required to be less than 16 percent of the estimated gross domestic product of the United States. 2. The limit on the debt of the United States held by the public shall not be increased, unless three-fifths of the whole number of each House shall provide by law for such an increase by a rollcall vote. 3. Prior to each fiscal year, the President shall transmit to the Congress a proposed budget for the United States Government for that fiscal year in which total outlays do not exceed total receipts. 4. No bill to increase revenue shall become law unless approved by a three-fifths majority of the whole number of each House by a rollcall vote. 5. Any budget plan for a fiscal year for the Government submitted by the President to the Congress shall include a justification by each department or agency of the Government for any funding proposed for that department or agency in that plan. The justification shall include a justification of each line item in the budget of that department or agency based upon its effect on carrying out its mission and its effect, if any, on the gross domestic product of the United States and an additional funding level below the requested number that would allow that department or agency to complete all of its critical mission functions. 6. Total receipts shall include all receipts of the United States Government except those derived from borrowing. Total outlays shall include all outlays of the United States Government except for those for repayment of debt principal. 7. The Congress shall enforce and implement this article by appropriate legislation, which may rely on estimates of outlays and receipts. 8. The Congress may waive the provisions of this article for any fiscal year in which a declaration of war is in effect. The provisions of this article may be waived for any fiscal year in which the United States is engaged in military conflict or after any event which causes an imminent and serious military threat to national security and is so declared by a joint resolution or during which a natural disaster is declared by a joint resolution, adopted by a vote by two-thirds of each House, which becomes law. 9. This article shall take effect beginning with the earlier of the tenth fiscal year beginning after its ratification or the first fiscal year beginning after any fiscal year in which the budget of the United States is not in deficit. .",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-01-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "17",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Proposing a balanced budget amendment to the Constitution of the United States.",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2",
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
            "updateDate": "2025-01-15T18:37:23Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-01-15T18:37:23Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:37:23Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-01-15T18:37:23Z"
          },
          {
            "name": "Income tax rates",
            "updateDate": "2025-01-15T18:37:23Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:37:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-01-14T16:22:00Z"
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
          "measure-id": "id119hjres11",
          "measure-number": "11",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres11v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless (1) Congress authorizes the excess by a three-fifths vote of each chamber, and (2) total outlays do not exceed a specified percentage of the estimated gross domestic product of the United States. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing. </p> <p>The amendment requires a three-fifths vote of each chamber of Congress to increase revenue or increase the limit on the debt of the United States. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts. The President's budget must also include justifications and specified details regarding funding proposed for departments and agencies. </p> <p>Congress may waive the requirements due to a declaration of war, a military conflict, an event that causes an imminent and serious military threat to national security, or a natural disaster.</p>"
        },
        "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres11.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless (1) Congress authorizes the excess by a three-fifths vote of each chamber, and (2) total outlays do not exceed a specified percentage of the estimated gross domestic product of the United States. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing. </p> <p>The amendment requires a three-fifths vote of each chamber of Congress to increase revenue or increase the limit on the debt of the United States. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts. The President's budget must also include justifications and specified details regarding funding proposed for departments and agencies. </p> <p>Congress may waive the requirements due to a declaration of war, a military conflict, an event that causes an imminent and serious military threat to national security, or a natural disaster.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres11"
    },
    "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting total outlays for a fiscal year from exceeding total receipts for that fiscal year unless (1) Congress authorizes the excess by a three-fifths vote of each chamber, and (2) total outlays do not exceed a specified percentage of the estimated gross domestic product of the United States. The prohibition excludes outlays for repayment of debt principal and receipts derived from borrowing. </p> <p>The amendment requires a three-fifths vote of each chamber of Congress to increase revenue or increase the limit on the debt of the United States. </p> <p>The amendment also requires the President to submit an annual budget in which total outlays do not exceed total receipts. The President's budget must also include justifications and specified details regarding funding proposed for departments and agencies. </p> <p>Congress may waive the requirements due to a declaration of war, a military conflict, an event that causes an imminent and serious military threat to national security, or a natural disaster.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres11"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres11ih.xml"
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
      "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": ".Proposing a balanced budget amendment to the Constitution requiring that each agency and department's funding is justified.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:20Z"
    }
  ]
}
```
