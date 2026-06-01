# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/7?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/7
- Title: Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year.
- Congress: 119
- Bill type: HJRES
- Bill number: 7
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-15T08:05:29Z
- Update date including text: 2025-03-15T08:05:29Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/7",
    "number": "7",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
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
    "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year.",
    "type": "HJRES",
    "updateDate": "2025-03-15T08:05:29Z",
    "updateDateIncludingText": "2025-03-15T08:05:29Z"
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
          "date": "2025-01-03T16:17:00Z",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres7ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 7\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Fitzpatrick submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. A Member of Congress may not receive a compensation for service as a Member of Congress during a fiscal year unless both Houses of Congress have agreed to an identical concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year. 2. This article shall apply with respect to fiscal years which begin after this article becomes a valid part of the Constitution. .",
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
            "name": "Budget process",
            "updateDate": "2025-01-15T18:54:22Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-01-15T18:54:22Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-01-15T18:54:22Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-15T18:54:22Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-01-15T18:54:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-07T12:13:35Z"
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
          "measure-id": "id119hjres7",
          "measure-number": "7",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres7v00",
            "update-date": "2025-01-14"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes amending the Constitution to prohibit Members of Congress from receiving compensation unless both chambers have agreed to a fiscal year budget prior to the start of the fiscal year.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.\u00a0The amendment applies beginning in the fiscal year after the amendment is ratified and becomes a valid part of the Constitution.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres7.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes amending the Constitution to prohibit Members of Congress from receiving compensation unless both chambers have agreed to a fiscal year budget prior to the start of the fiscal year.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.\u00a0The amendment applies beginning in the fiscal year after the amendment is ratified and becomes a valid part of the Constitution.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres7"
    },
    "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes amending the Constitution to prohibit Members of Congress from receiving compensation unless both chambers have agreed to a fiscal year budget prior to the start of the fiscal year.</p><p>The joint resolution provides that the amendment shall be valid when ratified by the legislatures of three-fourths of the states within seven years after the date of its submission for ratification.\u00a0The amendment applies beginning in the fiscal year after the amendment is ratified and becomes a valid part of the Constitution.</p><p>Under Article V of the Constitution, both chambers of Congress may propose an amendment by a vote of two-thirds of all Members present for such vote. A proposed amendment must be ratified by the states as prescribed in Article V and as specified by Congress.</p>",
      "updateDate": "2025-01-14",
      "versionCode": "id119hjres7"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres7ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:38:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to prohibit Members of Congress from receiving compensation during a fiscal year unless both Houses of Congress have agreed to a concurrent resolution on the budget for that fiscal year prior to the beginning of that fiscal year.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:38:37Z"
    }
  ]
}
```
